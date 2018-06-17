"""
Class based extension to argparse: https://docs.python.org/3/library/argparse.html
"""
import argparse

# Exposing all argparse here so that users don't have to import it as well.
import sys

# noinspection PyUnresolvedReferences
from argparse import *

import six


# todo:
# sub command (add_defaults..)

# help, version common code refactor
# exceptions refactor
# is there a better way to do sub-commands?
# is there a better way to do argument groups?
# should we somehow separate the Argument result class from the parser class (can we?)
# Can we find a better name than ParserHolder

# types
# docstrings
# order!
# think about names

# changes list
# 1) sane defaults...
# 2) No parents argument for parser, inheritance is a perfect and working replacement
# 3) added set_default

# tests:
# 1) Inherit twice from two classes with different orders, output strings should differ
# 2) 

# readme
# pypi


_keep_default = object()


def _argument_call_patch(argument_instance, argument_holder):

    parent = type(argument_instance)

    class Replacer(parent):

        def __call__(self, parser, namespace, values, option_string=None):
            del namespace
            return super(Replacer, self).__call__(parser, argument_holder, values, option_string)

    Replacer.__name__ = parent.__name__
    argument_instance.__class__ = Replacer


def _subparser_call_patch(argument_instance, argument_holder):

    parent = type(argument_instance)

    class Replacer(parent):

        def __call__(self, parser, namespace, values, option_string=None):

            alias = values[0]
            alias_to_name = getattr(self, "__alias_to_name")
            name_to_namespace = getattr(self, "__name_to_namespace")

            # Set all parsers to None, only the one that was chosen will get overwritten
            for name in six.viewkeys(name_to_namespace):
                setattr(argument_holder, name, None)

            name = alias_to_name[alias]
            setattr(argument_holder, name, name_to_namespace[name])

            return super(Replacer, self).__call__(parser, namespace, values, option_string)

    Replacer.__name__ = parent.__name__
    argument_instance.__class__ = Replacer


class SuppressError(ValueError):
    def __init__(self):
        super(SuppressError, self).__init__(
            "SUPPRESS is not supported for argument defaults since it makes no sense in class context"
        )


class ActionName(object):
    """ Use this for string actions, because named variables get auto completion and strings don't... """

    store = "store"
    store_true = "store_true"
    store_false = "store_false"
    store_const = "store_const"
    append = "append"
    append_const = "append_const"
    count = "count"
    help = "help"
    version = "version"

    # This one should not be used directly, and is undocumented.
    parsers = "parsers"


class _Sortable(object):

    _index_counter = 0

    def __init__(self):

        # No need to protect from racing access, since in a case of a "race" it will happen with two different classes
        # and so both will raise the counter and will have the same index value, but internally the class arguments will
        # still have sorted different indexes..
        _Sortable._index_counter += 1
        self._instance_index = _Sortable._index_counter

        super(_Sortable, self).__init__()


class _KwargsHolder(object):
    """
    An inner class used to hold keyword arguments for functions and classes that we don't want to immediately evaluate
    """

    _kwarg_names = ()
    _kwargs_name_prefix = ""
    _kwargs_name_postfix = ""

    def _get_kwargs(self):
        class_ = type(self)
        all_kwarg_pairs = ((k, getattr(self, class_._kwargs_name_prefix + k)) for k in class_._kwarg_names)
        return {k: v for k, v in all_kwarg_pairs if v is not _keep_default}


class _ParsedProperty(object):
    """
    Implements __get__ and __set__ methods that make sure that we don't access an instance of this class
    that wasn't parsed (aka __set__) first..
    """

    def __init__(self):

        self._instance_to_value = {}

        super(_ParsedProperty, self).__init__()

    def __get__(self, instance, owner):

        if instance not in self._instance_to_value:
            raise AttributeError("Tried to access an unparsed property")

        return self._instance_to_value[instance]

    def __set__(self, instance, value):
        self._instance_to_value[instance] = value


"""
When default is not set the argparse would use None instead of [] or 0 in places where these value are far more 
logical (a.k.a sane) if this is set to True we overwrite this "insane" behaviour.

There was a dilemma of whether this change should be added or not, since we usually want to work as a one to one
wrapper to argparse.
But our goal is to achieve easy type friendly arguments, and with the old defaults it breaks that.
The user can still define the argument with default=None if he wants that specific behaviour, but when nothing is 
defined the new behaviour is used.

This variable allows us to change the behaviour of this library to be more strict in that matter, we can also add
an overwrite in a class and/or in an instance level of ArgumentHolder, but I see no reason to do so right now.
"""
USE_SANE_DEFAULTS = True


class _BaseArg(_Sortable, _ParsedProperty, _KwargsHolder):

    def __repr__(self):
        # We can do better here, but for now its mostly a debugging functionality
        names = (n for n in dir(self) if not n.startswith("_"))
        name_and_values_full = ((n, getattr(self, n, "NOT PARSED")) for n in names)
        name_and_values = ((n, v) for n, v in name_and_values_full if not callable(v))
        variables = ", ".join("%s=%r" % (n, v) for n, v in sorted(name_and_values, key=lambda nv: nv[0]))
        return "%s(%s)" % (type(self).__name__, variables)


class Arg(_BaseArg):

    _kwarg_names = (
        "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar", "version"
    )

    # noinspection PyShadowingBuiltins
    def __init__(
            self,
            *flags,
            action=_keep_default,
            nargs=_keep_default,
            const=_keep_default,
            default=_keep_default,
            type=_keep_default,
            choices=_keep_default,
            required=_keep_default,
            help=_keep_default,
            metavar=_keep_default,
            version=_keep_default,
            group=None,
    ):

        super(Arg, self).__init__()

        self.flags = flags
        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices = choices
        self.required = required
        self.help = help
        self.metavar = metavar
        self.version = version

        self.group = group
        self._default = default  # This is overwritten by the next line, and is only set to make the ide happy.
        self.default = default  # Keep at the end since the setter does checks that can depend on the other values

    @property
    def default(self):
        """ An alternative to ArgumentParser.get_default """
        return self._default

    @default.setter
    def default(self, value):
        """ An alternative to ArgumentParser.set_defaults """

        # we also make sure SUPPRESS is not used here
        if value == SUPPRESS:
            raise SuppressError()

        if USE_SANE_DEFAULTS and value is _keep_default:

            if self.action == ActionName.append or self.nargs == "*" or self.nargs == "+" or self.nargs == REMAINDER:
                value = []

            if self.action == ActionName.count:
                value = 0

        self._default = value


class HelpArg(Arg):
    """ A convenience subclass for help arguments """

    # noinspection PyShadowingBuiltins
    def __init__(
            self,
            *flags,
            help=_keep_default,
    ):

        if not flags:
            flags = ["--help", "-h"]

        super(HelpArg, self).__init__(*flags, help=help, action=ActionName.help)


class VersionArg(Arg):

    # noinspection PyShadowingBuiltins
    def __init__(
            self,
            *flags,
            version=None,
            help=_keep_default,
    ):

        if not flags:
            flags = ["--version", "-v"]

        super(VersionArg, self).__init__(*flags, version=version, help=help, action=ActionName.version)


class Args(_BaseArg):

    def __init__(self, args=None, args_default=None):
        """
        Lets a couple of args set a value to the same destination, useful for example with set_const
        where each arg sets a different constant value.
        :param args: A list of Arg objects
        :param args_default: A default value to set when none of args was invoked
        """

        super(Args, self).__init__()

        if args is None:
            args = []

        self.args = args
        self.args_default = args_default


class ArgumentGroup(object):

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description


class MutuallyExclusiveGroup(Args):

    def __init__(self, required=False, args=None, args_default=None):
        """
        :param required: Same as in the add_mutually_exclusive_group call
        :param args: When used as an argument, this list of arguments will be added to the group with
        their result put in the groups variable name.
        :param args_default: when used as an argument and required is set to false, this will be used when none of
        the grouped argument is selected
        """
        super(MutuallyExclusiveGroup, self).__init__(args=args, args_default=args_default)

        self.required = required


class SubParserConfig(_KwargsHolder):

    _kwarg_names = (
        "title", "description", "prog", "parser_class", "action", "option_string", "help", "metavar",
    )

    # noinspection PyShadowingBuiltins
    def __init__(self,
                 title=_keep_default,
                 description=_keep_default,
                 prog=_keep_default,
                 parser_class=_keep_default,
                 action=_keep_default,
                 option_string=_keep_default,
                 help=_keep_default,
                 metavar=_keep_default):
        self.title = title
        self.description = description
        self.prog = prog
        self.parser_class = parser_class
        self.action = action
        self.option_string = option_string
        self.help = help
        self.metavar = metavar


class _ParserHolderMeta(type, _KwargsHolder):
    """
    We use this meta class for two reasons:
    1) To give our classes the _sorted_arguments variable that allows to get only the _Sortable variables defined in
       the class (and not in the parents). We use __new__ to do that and it allows us to easily implement proper
       ArgumentParser.parents behaviour in our __init__ method
    2) To supply the _get_kwargs method for the ParserHolder class (if ParserHolder were to inherit _KwargsHolder
       it would have been an instance method and that is useless to us..)
    """

    _kwarg_names = (
        "description", "prog", "usage", "epilog", "formatter_class", "prefix_chars", "fromfile_prefix_chars",
        "argument_default", "conflict_handler", "add_help"
    )
    _kwargs_name_prefix = "_"

    def __new__(mcs, name, bases, attrs):

        _sortable_arguments = ((k, v) for k, v in attrs.items() if isinstance(v, _BaseArg))
        # noinspection PyProtectedMember
        attrs["_sorted_arguments"] = list(sorted(_sortable_arguments, key=lambda kv: kv[1]._instance_index))

        return super(_ParserHolderMeta, mcs).__new__(mcs, name, bases, attrs)


_not_named_argument = object()


@six.add_metaclass(_ParserHolderMeta)
class ParserHolder(_BaseArg):
    """
    A base class for all the ParserHolders

    I wanted to allow people to be able to choose between full ease of use, where you just create an instance of you
    child class and it comes ready to use as in ParserHolder with no potential name conflict for the arguments you
    added to it, and between exposing every interface you might need in ArgumentParser and giving you more control over
    parsing, but with a bit stronger restriction on argument names (due to the added method names)

    This class just holds the common code of those options.
    """

    _description = _keep_default

    # All these have sane auto values
    _prog = _keep_default
    _usage = _keep_default
    _epilog = _keep_default
    _formatter_class = _keep_default
    _prefix_chars = _keep_default
    _fromfile_prefix_chars = _keep_default
    _argument_default = _keep_default
    _conflict_handler = _keep_default
    _add_help = _keep_default

    """ Supported only in python>=3.5 on other versions it is silently ignored """
    _allow_abbrev = _keep_default

    """ Change the parser class (Useful in cases where you would inherit and overwrite a method like """
    _parser_class = argparse.ArgumentParser

    """ 
    Overwrite to add a help argument manually
    Set it to a string to get a default HelpArg with the help parameter set to this string
    Set it to a HelpArg for more control
    You can also use Arg but that is less comfortable, more error prone and should not be necessary since HelpArg
    is built in a way that is supposed to let you achieve everything that is possible with this type of arguments
    """
    _help = None

    """ 
    Overwrite to add a version argument manually
    Set it to a string to get a default VersionArg with the version parameter set to this string
    Set it to a VersionArg for more control
    You can also use Arg but that is less comfortable, more error prone and should not be necessary since VersionArg
    is built in a way that is supposed to let you achieve everything that is possible with this type of arguments
    """
    _version = None

    """
    Set this property to configure the subparser used for sub-commands (It accepts the same parameters as the 
    add_subparsers that you would have used with ArgumentParser.
    There is no need to supply this argument when you use sub-parsers, but if left empty the add_subparsers will be
    called without arguments.
    You should only supply a SubParser argument here, or leave it as None.
    """
    _subparser_config = None

    # Used when the holder is used as an argument
    _kwarg_names = ("prog", "aliases", "help")
    _kwargs_name_prefix = "__"

    # noinspection PyShadowingBuiltins
    def __init__(self, prog=_keep_default, aliases=_keep_default, help=_keep_default, _add_help=None, _namespace=None):
        """
        :param prog: When initiated as a subparser it is used to set the prog argument, ignored otherwise
        :param aliases: When initiated as a subparser it is used to set the aliases argument, ignored otherwise
        :param help: When initiated as a subparser it is used to set the help argument, ignored otherwise
        :param _add_help: Used internally, Setting this will overwrite the class parameter but using this parameter
                          like that should be avoided.
        :param _namespace: Used internally, we pass self to parent class using this argument to make sure they add
                           parameters to this object, and not to the temporary parent instance.
        """

        super(ParserHolder, self).__init__()

        # noinspection PyProtectedMember
        setattr(self, "__prog", prog)
        setattr(self, "__aliases", aliases)
        setattr(self, "__help", help)

        # We never call super __init__, this choice escapes the MRO which is usually not a good idea, but in our
        # case the MRO will not function for the most simple (and probably common) usage of parents that we try to
        # emulate.
        # If we have a class with two parents that provide arguments, depending on when we call super (at the start or
        # at the end) Arguments order will happen:
        # 1) The first arguments will come from the child class and then from the parents left to right
        # 2) The first arguments will come from the parents right to left and from the child class and then
        # While the behaviour in the argparse library is parent left to right first and then the child arguments

        """
        The parser is not exposed since the name might be used for an argument and since direct usage will most likely
        break things.
        But if there is a missing feature in this implementation, or a bug that is possible to overcome by directly
        using _parser, then nothing stops you from doing so.
        Do note that you most likely can achieve what you want by implementing it in a subclass, instead of acessing
        the instance's "_parser" variable.
        
        Note that in subparser mode this parameter will be overwritten, but add it in init to make auto completion
        and type checking work better.
        """

        if _add_help is None:
            _add_help = self._add_help

        if _namespace is None:
            _namespace = self
        self._namespace = _namespace

        self._parser_kwargs = self._get_parser_kwargs(add_help=_add_help)
        self._parser = self._parser_class(**self._parser_kwargs)

        self._group_to_group_parser = {}
        self._subparser = None

    def _get_parser_kwargs(self, add_help):

        if self._argument_default == SUPPRESS:
            raise SuppressError()

        class_ = type(self)
        # noinspection PyUnresolvedReferences,PyProtectedMember
        parser_kwargs = class_._get_kwargs(self)

        if self._help is not None and add_help is _keep_default:
            add_help = False
        if add_help is not _keep_default:
            parser_kwargs["add_help"] = add_help

        allow_abbrev = self._allow_abbrev
        if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 5):
            allow_abbrev = _keep_default
        if allow_abbrev is not _keep_default:
            parser_kwargs["allow_abbrev"] = allow_abbrev

        parser_kwargs["parents"] = list(self._get_parent_argument_parsers())

        return parser_kwargs

    def _get_parent_argument_parsers(self):

        # There is no super call here, see why in the comment in the __init__ function
        for base in self.__class__.__bases__:
            if hasattr(base, "_sorted_arguments"):
                parent_holder = base(_add_help=False, _namespace=self._namespace)
                # noinspection PyProtectedMember
                parent_holder._fill_parser()

                # noinspection PyProtectedMember
                yield parent_holder._parser

    def _fill_parser(self):

        # noinspection PyProtectedMember,PyUnresolvedReferences
        for action in self._parser._actions:
            if action.dest is not SUPPRESS and action.default is not SUPPRESS:
                if action.dest not in dir(self._namespace):
                    # I think if that happens we have a bug
                    raise AttributeError(
                        "class '%s' doesn't have the attribute '%s'" % (type(self._namespace), action.dest))
                setattr(self._namespace, action.dest, action.default)

        # noinspection PyProtectedMember,PyUnresolvedReferences
        for dest, value in self._parser._defaults.items():
            if dest not in dir(self._namespace):
                # I think if that happens we have a bug
                raise AttributeError(
                    "class '%s' doesn't have the attribute '%s'" % (type(self._namespace), dest))
            setattr(self._namespace, dest, value)

        for argument_name, argument in self._sorted_arguments:
            if isinstance(argument, ParserHolder):
                self._add_subparser(argument=argument, argument_name=argument_name)
            elif isinstance(argument, Args):
                for group_argument in argument.args:
                    if isinstance(argument, MutuallyExclusiveGroup):
                        group_argument.group = argument
                    self._add_argument(argument=group_argument, argument_name=argument_name)
                self._parser.set_defaults(**{argument_name: argument.args_default})
            elif isinstance(argument, Arg):
                self._add_argument(argument=argument, argument_name=argument_name)
            else:
                raise ValueError("Unsupported argument type '%s'" % type(argument))

        if self._help is not None:
            if isinstance(self._help, six.string_types):
                help_argument = HelpArg(
                    *[a.format(p=self._parser.prefix_chars) for a in ("{p}{p}help", "{p}h")],
                    help=self._help)
            elif isinstance(self._help, Arg):
                help_argument = self._help
            else:
                raise ValueError("Unsupported help argument type '%s'" % type(self._help))

            self._add_argument(argument=help_argument)

        if self._version is not None:
            if isinstance(self._version, six.string_types):
                version_argument = VersionArg(
                    *[a.format(p=self._parser.prefix_chars) for a in ("{p}{p}version", "{p}v")],
                    version=self._version)
            elif isinstance(self._version, Arg):
                version_argument = self._version
            else:
                raise ValueError("Unsupported version argument type '%s'" % type(self._version))

            self._add_argument(argument=version_argument)

    def _add_subparser(self, argument, argument_name):

        # todo: Add magic for the subparser to be able to write straight to the parser object..

        if self._subparser is None:
            if self._subparser_config is None:
                subparser_config = SubParserConfig()
            else:
                subparser_config = self._subparser_config
            # noinspection PyProtectedMember
            subparser_config_kwargs = subparser_config._get_kwargs()
            self._subparser = self._parser.add_subparsers(**subparser_config_kwargs)

            setattr(self._subparser, "__alias_to_name", {})
            setattr(self._subparser, "__name_to_namespace", {})

            _subparser_call_patch(self._subparser, self._namespace)

        # noinspection PyProtectedMember
        add_parser_kwargs = dict(argument._parser_kwargs)
        # noinspection PyProtectedMember
        add_parser_kwargs.update(argument._get_kwargs())

        argument._parser = self._subparser.add_parser(argument_name, **add_parser_kwargs)

        alias_to_name = getattr(self._subparser, "__alias_to_name")
        name_to_namespace = getattr(self._subparser, "__name_to_namespace")
        name_to_namespace[argument_name] = argument
        alias_to_name[argument_name] = argument_name
        for alias in add_parser_kwargs.get("aliases", []):
            alias_to_name[alias] = argument_name

        # noinspection PyProtectedMember
        argument._fill_parser()

    def _add_argument(self, argument, argument_name=_not_named_argument):

        # noinspection PyProtectedMember
        argument_kwargs = argument._get_kwargs()

        if argument_name is not _not_named_argument:
            argument_kwargs["dest"] = argument_name

        if argument.group is None:
            add_argument_function = self._parser.add_argument
        else:
            if argument.group not in self._group_to_group_parser:
                if isinstance(argument.group, ArgumentGroup):
                    group_parser = self._parser.add_argument_group(
                        title=argument.group.title, description=argument.group.description)
                elif isinstance(argument.group, MutuallyExclusiveGroup):
                    group_parser = self._parser.add_mutually_exclusive_group(
                        required=argument.group.required)
                else:
                    raise ValueError("Unsupported type '%s' in group argument" % type(argument.group))

                self._group_to_group_parser[argument.group] = group_parser

            add_argument_function = self._group_to_group_parser[argument.group].add_argument

        # noinspection PyNoneFunctionAssignment
        argument = add_argument_function(*argument.flags, **argument_kwargs)
        # noinspection PyTypeChecker
        _argument_call_patch(argument, self._namespace)

    def set_default(self, name, value):

        if name not in dir(self):
            raise AttributeError("class '%s' has not attribute named '%s'" % (type(self), name))

        self._parser.set_defaults(**{name: value})

    def set_defaults(self, **kwargs):

        for name, value in six.viewitems(kwargs):
            self.set_default(name=name, value=value)

    def get_default(self, name):
        return self._parser.get_default(dest=name)

    def parse_args(self, args=None):
        self._fill_parser()
        self._parser.parse_args(args=args)
        return self

    def parse_known_args(self, args=None):
        self._fill_parser()
        _, remainder = self._parser.parse_known_args(args=args)
        return self, remainder

    def format_usage(self):
        return self._parser.format_usage()

    def format_help(self):
        return self._parser.format_help()

    def print_usage(self, file=None):
        return self._parser.print_usage(file=file)

    def print_help(self, file=None):
        return self._parser.print_help(file=file)

    def exit_(self, status=0, message=None):
        return self._parser.exit(status=status, message=message)

    def error_(self, message=None):
        return self._parser.error(message=message)
