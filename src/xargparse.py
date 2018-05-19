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
# mutually exclusive groups
# append_const
# sub command

# help, version common code refactor

# docstrings
# readme
# fix documentation about not supporting set_defaults and get_defaults, and other changes
# pypi
# tests (copy from standard library and add some of our own..)
# should we somehow separate the Argument result class from the parser class (can we?)
# is there a better way to do argument groups?

# changes list
# 1) sane defaults...
# 2) No set_defaults and get_defaults
# 3) No parents argument for parser, inheritance is a perfect and working replacement

# tests:
# 1) Inherit twice from two classes with different orders, output strings should differ
# 2) 

_keep_default = object()


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
        self.instance_index = Arg._index_counter


class _KwargsHolder(object):
    """
    An inner class used to hold keyword arguments for functions and classes that we don't want to immediately evaluate
    """

    _kwarg_names = ()

    def get_kwargs(self, name_prefix=""):
        all_kwarg_pairs = ((k, getattr(self, name_prefix + k)) for k in self._kwarg_names)
        return {k: v for k, v in all_kwarg_pairs if v is not _keep_default}


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


class Arg(_Sortable, _KwargsHolder):

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


class ArgumentGroup(object):

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description


class _ParserHolderMeta(type, _KwargsHolder):
    """
    We use this meta class for two reasons:
    1) To give our classes the _sorted_arguments variable that allows to get only the _Sortable variables defined in
       the class (and not in the parents). We use __new__ to do that and it allows us to easily implement proper
       ArgumentParser.parents behaviour in our __init__ method
    2) To define all the parser variables in a way that is only accessible to the class and not to the instance.
       this will allow the

    """

    _kwarg_names = (
        "description", "prog", "usage", "epilog", "formatter_class", "prefix_chars", "fromfile_prefix_chars",
        "argument_default", "conflict_handler", "add_help"
    )

    def __new__(mcs, name, bases, attrs):

        _sortable_arguments = ((k, v) for k, v in attrs.items() if isinstance(v, Arg))
        attrs["_sorted_arguments"] = list(sorted(_sortable_arguments, key=lambda kv: kv[1].instance_index))

        return super(_ParserHolderMeta, mcs).__new__(mcs, name, bases, attrs)


_not_named_argument = object()


@six.add_metaclass(_ParserHolderMeta)
class ParserHolder(object):

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

    def __init__(self):

        # We never call super __init__, this choice escapes the MRO which is usually not a good idea, but in our
        # case the MRO will not function for the most simple (and probably common) usage of parents that we try to
        # emulate.
        # If we have a class with two parents that provide arguments, depending on when we call super (at the start or
        # at the end) Arguments order will happen:
        # 1) The first arguments will come from the child class and then from the parents left to right
        # 2) The first arguments will come from the parents right to left and from the child class and then
        # While the behaviour in the argparse library is parent left to right first and then the child arguments
        self._parser = self._get_argument_parser(add_help=self._add_help)

    @classmethod
    def _get_parent_argument_parsers(cls):

        # There is no super call here, see why in the comment in the __init__ function
        for base in cls.__bases__:
            try:
                # noinspection PyUnresolvedReferences,PyProtectedMember
                yield base._get_argument_parser(add_help=False)
            except AttributeError:
                pass

    @classmethod
    def _get_base_argument_parser(cls, add_help):

        if cls._argument_default == SUPPRESS:
            raise SuppressError()

        if cls._help is not None and add_help is _keep_default:
            add_help = False

        parser_kwargs = cls.get_kwargs(name_prefix="_")

        parser_kwargs["add_help"] = add_help

        allow_abbrev = cls._allow_abbrev
        if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 5):
            allow_abbrev = _keep_default
        if allow_abbrev is not _keep_default:
            parser_kwargs["allow_abbrev"] = allow_abbrev

        parser_kwargs["parents"] = cls._get_parent_argument_parsers()

        return cls._parser_class(**parser_kwargs)

    @classmethod
    def _add_argument(cls, parser, group_to_group_parser, argument, argument_name=_not_named_argument):

        argument_kwargs = argument.get_kwargs()

        if argument_name is not _not_named_argument:
            argument_kwargs["dest"] = argument_name

        if argument.group is None:
            add_argument_function = parser.add_argument
        else:
            if argument.group not in cls.__group_to_group_parser:
                group_to_group_parser[argument.group] = parser.add_argument_group(
                    title=argument.group.title, description=argument.group.description)
            add_argument_function = group_to_group_parser[argument.group].add_argument

        add_argument_function(*argument.flags, **argument_kwargs)

    @classmethod
    def _get_argument_parser(cls, add_help):

        parser = cls._get_base_argument_parser(add_help=add_help)

        group_to_group_parser = {}

        for argument_name, argument in cls._sorted_arguments:
            cls._add_argument(parser=parser, group_to_group_parser=group_to_group_parser,
                              argument=argument, argument_name=argument_name)

        if cls._help is not None:
            if isinstance(cls._help, six.string_types):
                help_argument = HelpArg(
                    *[a.format(p=parser.prefix_chars) for a in ("{p}{p}help", "{p}h")],
                    help=cls._help)
            else:
                help_argument = cls._help

            cls._add_argument(parser=parser, group_to_group_parser=group_to_group_parser, argument=help_argument)

        if cls._version is not None:
            if isinstance(cls._version, six.string_types):
                version_argument = VersionArg(
                    *[a.format(p=parser.prefix_chars) for a in ("{p}{p}version", "{p}v")],
                    version=cls._version)
            else:
                version_argument = cls._version

            cls._add_argument(parser=parser, group_to_group_parser=group_to_group_parser, argument=version_argument)

        return parser

    @property
    def parser(self):
        """
        Exposes the inner parser object

        Dangerous: Can easily break stuff, only use it if what you want to do can't be achieved otherwise
        and you understand both the relevant code in xargparse and argparse.
        """
        return self._parser

    def parse_args(self, args=None):
        parsed_dict = vars(self._parser.parse_args(args=args))
        self.__dict__.update(**parsed_dict)
        return self

    def parse_known_args(self, args=None):
        result, remainder = self._parser.parse_known_args(args=args)
        parsed_dict = vars(result)
        self.__dict__.update(**parsed_dict)
        return self, remainder

    def format_usage(self):
        return self.parser.format_usage()

    def format_help(self):
        return self.parser.format_help()

    def print_usage(self, file=None):
        return self.parser.print_usage(file=file)

    def print_help(self, file=None):
        return self.parser.print_help(file=file)

    def exit(self, status=0, message=None):
        return self.parser.exit(status=status, message=message)

    def error(self, message=None):
        return self.parser.error(message=message)

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, {n: getattr(self, n) for n in self.__argument_names})
