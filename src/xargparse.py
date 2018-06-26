"""
Class based extension to argparse: https://docs.python.org/3/library/argparse.html
"""
import argparse
import os
import sys
from argparse import *  # Exposing all argparse here so that users don't have to import it as well.


"""
A little trick to make sure we don't really try to import typing unless we need them
"""
if "mypy" in os.environ:
    from typing import Dict, Any, List, Optional, Union, Callable


# todo:

# * help, version common code refactor
# * Can we find a better name than ParserHolder (ClassParser)
# * change namespace, and parser-holder to parser or class parser
# * think about names

# * named calls
# * types
# * docstrings
# * figure out if references like https://docs.python.org/3.6/library/argparse.html#metavar are good, and if we can change the
#   version part to be dynamic..

# changes list
# * USE_SANE_DEFAULTS
# * No parents argument for parser, inheritance is a perfect and working replacement
# * added set_default, they must overwrite something that exist, not recommended to use
# * SubCommand has a sub item that holds stuff instead of setting the parent, SubParserMapper, SubParserConfig
# * Args type to allow multi args setting
# * New Exceptions (SuppressError)
# * added ActionName
# * The way we set parser properties (like _description) and the HelpArg and versionArg
# * The way we handle ArgumentGroup and MutuallyExclusiveGroup
# * No namespace
# * exit = exit_ and error = error_

# Docs focus
# * single file code

# tests:
# * Inherit twice from two classes with different orders, output strings should differ
# * Make sure we see Set and see Description

# * readme
# * license
# * pypi
# * delete the pass statement...
pass


# =============================
# Compatibility: This section contains code that is needed for this library to work with both python 2 and python 3
# the code itself was stolen from the six library (with minor alternations).
# I didn't use the library directly to avoid any external dependencies for this library.
# =============================

"""
I stole this code from the six library, Since I wanted fro users of this package to be able to just copy the source file
to their project, without an extra dependency.
"""
if sys.version_info.major >= 3:
    # noinspection PyUnresolvedReferences
    _viewkeys = dict.keys
    # noinspection PyUnresolvedReferences
    _viewitems = dict.items
    # noinspection PyUnresolvedReferences
    _string_types = str,
else:  # python 2
    # noinspection PyUnresolvedReferences
    _viewkeys = dict.viewkeys
    # noinspection PyUnresolvedReferences
    _viewitems = dict.viewitems
    # noinspection PyUnresolvedReferences
    _string_types = basestring,


def _add_metaclass(metaclass):
    # type: (Any) -> Any
    """ This is also stolen from the six library """
    def wrapper(cls):
        # type: (Any) -> Any
        original_variables = cls.__dict__.copy()
        slots = original_variables.get("__slots__")
        if slots is not None:
            if isinstance(slots, str):
                slots = [slots]
            for slots_variable in slots:
                original_variables.pop(slots_variable)
        original_variables.pop("__dict__", None)
        original_variables.pop("__weakref__", None)
        return metaclass(cls.__name__, cls.__bases__, original_variables)
    return wrapper


# =============================
# Hacks: This section contains the hack code needed for this library to work
# =============================

def _action_call_patch(action_instance, argument_holder):
    # type: (argparse.Action, ParserHolder) -> None
    """
    A hack function that allows us to patch argparse action.__call__ to use our ParserHolder
    objects as a namespace instead of the provided one. This is ugly, but considering all the
    other alternatives I think it is the best choice.
    It allows us to support all existing Action classes in argparse and any user created subclasses without the need to change
    anything, or add tons of subclasses.
    The downside is that if a user have an Action subclass that does something with the namespace that shouldn't be done on our
    ParserHolder object, unexpected things might happen that are difficult to debug.
    But from the user's point of view the ParserHolder is the namespace, and the library doesn't allow to supply a custom
    namespace argument anyway, so hopefully these cases should be rare enough.
    """

    parent = type(action_instance)

    class Replacer(parent):

        def __call__(self, parser, namespace, values, option_string=None):
            # type: (argparse.ArgumentParser, ParserHolder, List[str], Optional[str]) -> None
            del namespace
            # noinspection PyTypeChecker
            return super(Replacer, self).__call__(parser, argument_holder, values, option_string)

    Replacer.__name__ = parent.__name__
    action_instance.__class__ = Replacer


# noinspection PyProtectedMember
def _subparser_action_call_patch(action_instance, argument_holder, subparser_mappers):
    # type: (argparse._SubParsersAction, ParserHolder, List[SubParserMapper]) -> None
    """ Same hack as _action_call_patch but with extra logic for subparsers """

    parent = type(action_instance)

    class Replacer(parent):

        def __call__(self, parser, namespace, values, option_string=None):
            # type: (argparse.ArgumentParser, ParserHolder, List[str], Optional[str]) -> None

            alias = values[0]
            alias_to_name = getattr(self, "__alias_to_name")  # type: Dict[str, str]
            name_to_namespace = getattr(self, "__name_to_namespace")  # type: Dict[str, ParserHolder]

            # Set all parsers to None, only the one that was chosen will get overwritten
            for name in _viewkeys(name_to_namespace):
                setattr(argument_holder, name, None)

            name = alias_to_name[alias]
            setattr(argument_holder, name, name_to_namespace[name])

            for mapper_name, mapper in subparser_mappers:
                value = mapper.map.get(name, None)
                setattr(argument_holder, mapper_name, value)

            # noinspection PyTypeChecker,PyUnresolvedReferences
            return super(Replacer, self).__call__(parser, namespace, values, option_string)

    Replacer.__name__ = parent.__name__
    action_instance.__class__ = Replacer


# =============================
# Exceptions: All exceptions are defined here
# =============================

class SuppressError(ValueError):
    """
    An exception thrown in case the user tries to use the argparse.SUPPRESS as a value, since not setting
    an argument goes against the whole logic and idea of this library.
    """
    def __init__(self):
        # type: () -> None
        super(SuppressError, self).__init__(
            "SUPPRESS is not supported for argument defaults since it makes no sense in class context"
        )


class UnparsedArgumentAccess(AttributeError):
    """ Raised when we try to access a parser attribute before parse_args or parse_known_args was called"""
    def __init__(self):
        # type: () -> None
        super(UnparsedArgumentAccess, self).__init__("Tried to access an unparsed argument")


class ArgumentForDefaultValueDoesntExist(AttributeError):
    """ Raised when trying to set a default value for an attribute that doesn't exist """
    def __init__(self, parser, attribute_name):
        # type: (ParserHolder, str) -> None
        super(ArgumentForDefaultValueDoesntExist, self).__init__(
            "class '%s' has not attribute named '%s'" % (type(parser), attribute_name)
        )


class NoArgumentInParser(AttributeError):
    """ Raised when trying to set a value to an argument of a parser, but the parser didn't define this argument """

    def __init__(self, parser, dest):
        # type: (ParserHolder, str) -> None
        super(NoArgumentInParser, self).__init__(
            "class '%s' doesn't have the attribute '%s'" % (type(parser), dest)
        )


class UnsupportedType(TypeError):
    """ Generic base exception raised when an argument of a wrong type is used in the wrong place """
    message_template = ""

    def __init__(self, argument):
        # type: (Any) -> None
        super(UnsupportedType, self).__init__(self.message_template % type(argument))


class UnsupportedGroupType(UnsupportedType):
    """ Raised when a group parameter in an Argument is not a subclass of one of the supported group types """
    message_template = "Unsupported type '%s' in group argument"

    def __init__(self, group):
        # type: (Any) -> None
        super(UnsupportedGroupType, self).__init__(argument=group)


class UnsupportedArgumentType(UnsupportedType):
    """
    Raised when an argument is not an instance of one of the supported types for arguments
    This can only happen if you subclass _BaseArg instead of one of its subclasses,
    and then use this subclass as an argument.
    """
    message_template = "Unsupported argument type '%s'"


class UnsupportedHelpArgumentType(UnsupportedType):
    """ Raised when the _help argument is of an unsupported type """
    message_template = "Unsupported help argument type '%s'"


class UnsupportedVersionArgumentType(UnsupportedType):
    """ Raised when the _version argument is of an unsupported type """
    message_template = "Unsupported version argument type '%s'"


class UnsupportedArgumentTypeInArgs(UnsupportedType):
    """ Raised when we use an Args object with arguments that don't subclass Arg """
    message_template = "Unsupported argument type '%s' in an Args class"


class MissingSubParserKeyInMapper(KeyError):
    """
    Raised when a SubParserMapper with _must_set_all_parsers=True
    is missing a mapping for one of the subparsers
    """
    def __init__(self, name):
        # type: (str) -> None
        super(MissingSubParserKeyInMapper, self).__init__(
            "SubParserMapper is missing a key for the SubParser '%s'" % name
        )


class NoSubParserForKeyInMapper(KeyError):
    """  Raised when a SubParserMapper contains a key with noe SubParser to map to """
    def __init__(self, name):
        # type: (str) -> None
        super(NoSubParserForKeyInMapper, self).__init__(
            "SubParserMapper maps to a none existing SubParser '%s'" % name
        )


# =============================
# Globals: Global definitions used int the library
# =============================

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


"""
Used internally to indicate that an argument should not be passed as part of an argument dict
(In other words the receiving function should use its own default value for the argument)
"""
_keep_default = object()


"""
Used internally for the version and help arguments to avoid setting a dest on these parameters
"""
_not_named_argument = object()


# =============================
# Name classes: Helper enum like classes used to replace string usage with class variable usage
# =============================

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

    # This one should not be used directly
    parsers = "parsers"


class ConflictHandlerName(object):
    """ Use this when setting _conflict_handler in the ParserHolder instead of relying on strings """

    error = "error"
    resolve = "resolve"


class NArgName(object):
    """ Use this instead of the strings '?', '+' etc.. for nargs, you can also directly use the globals in argparse """
    optional = argparse.OPTIONAL  # ?
    zero_or_more = argparse.ZERO_OR_MORE  # *
    one_or_more = argparse.ONE_OR_MORE  # +
    remainder = argparse.REMAINDER  # ...


# =============================
# Base and Meta classes: Classes used to provide all the magic functionality of the library, these classes are considered
# very low level and thus they are all private.
# =============================


class _Sortable(object):
    """
    Any class inheriting this one will have instances that can be sorted against each other by the order of declaration.
    They use the _instance_index variable to do that, and it is guaranteed that if two instances of _Sortable where declared one
    after another in the same class, the second one will have a higher index.
    This is also the only thing guaranteed about _instance_index.
    """

    _index_counter = 0

    def __init__(self):
        # type: () -> None

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

    _kwarg_names = ()  # type: List[str]
    _kwargs_name_prefix = ""
    _kwargs_name_postfix = ""

    def _get_kwargs(self):
        # type: () -> Dict[str, Any]
        class_ = type(self)
        all_kwarg_pairs = ((k, getattr(self, class_._kwargs_name_prefix + k)) for k in class_._kwarg_names)
        return {k: v for k, v in all_kwarg_pairs if v is not _keep_default}


class _ParsedProperty(object):
    """
    Implements __get__ and __set__ methods that make sure that we don't access an instance of this class
    that wasn't parsed (aka __set__) first..
    """

    def __init__(self):
        # type: () -> None

        self._instance_to_value = {}  # type: Dict[_BaseArg, Any]

        super(_ParsedProperty, self).__init__()

    def __get__(self, instance, owner):
        # type: (_BaseArg, Any) -> None
        del owner

        if instance not in self._instance_to_value:
            raise UnparsedArgumentAccess()

        return self._instance_to_value[instance]

    def __set__(self, instance, value):
        # type: (_BaseArg, Any) -> None
        self._instance_to_value[instance] = value


class _BaseArg(_Sortable, _ParsedProperty, _KwargsHolder):
    """
    All classes that can be used as arguments inherit this class, and we use this class to store a sorted list
    of such argument in our ParserHolder class.
    """

    def __repr__(self):
        # type: () -> str
        """
        An extra helper repr function that we use for debugging mostly.

        We can do better here, but for now its enough..
        """
        names = (n for n in dir(self) if not n.startswith("_"))
        name_and_values_full = ((n, getattr(self, n, "NOT PARSED")) for n in names)
        name_and_values = ((n, v) for n, v in name_and_values_full if not callable(v))
        variables = ", ".join("%s=%r" % (n, v) for n, v in sorted(name_and_values, key=lambda nv: nv[0]))
        return "%s(%s)" % (type(self).__name__, variables)


class _ParserHolderMeta(type, _KwargsHolder):
    """
    We use this meta class for two reasons:
    1) To give our classes the _sorted_arguments variable that allows to get only the _BaseArg variables defined in
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
        # type: (Any, str, List[Any], Dict[str, Any]) -> None

        _sortable_arguments = ((k, v) for k, v in attrs.items() if isinstance(v, _BaseArg))
        # noinspection PyProtectedMember
        attrs["_sorted_arguments"] = sorted(_sortable_arguments, key=lambda kv: kv[1]._instance_index)

        return super(_ParserHolderMeta, mcs).__new__(mcs, name, bases, attrs)


# =============================
# Argument Objects: All the argument related objects are defined here
# =============================

class Arg(_BaseArg):
    """ A class that we use as a parallel to ArgumentParser.add_argument """

    _kwarg_names = (
        "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar", "version"
    )

    # noinspection PyShadowingBuiltins
    def __init__(
            self,
            *flags,  # type: Union[str, List[str]]
            action=_keep_default,  # type: Union[None, str, argparse.Action]
            nargs=_keep_default,  # type: Union[None, str, int]
            const=_keep_default,  # type: Any
            default=_keep_default,  # type: Any
            type=_keep_default,  # type: Union[None, str, Callable[[str], Any]]
            choices=_keep_default,  # type: List[Any]
            required=_keep_default,  # type: bool
            help=_keep_default,  # type: Optional[str]
            metavar=_keep_default,  # type: Optional[str]
            version=_keep_default,  # type: Optional[str]
            group=None,  # type: Union[None, ArgumentGroup, MutuallyExclusiveGroup]
    ):
        """
        :param flags: A flag or a list of flags for optional arguments (This will turn this argument into an optional one..)
        see info about flags in https://docs.python.org/3.6/library/argparse.html#name-or-flags
        :param action: https://docs.python.org/3.6/library/argparse.html#action
        :param nargs: https://docs.python.org/3.6/library/argparse.html#nargs
        :param const: https://docs.python.org/3.6/library/argparse.html#const
        :param default: https://docs.python.org/3.6/library/argparse.html#default
        :param type: https://docs.python.org/3.6/library/argparse.html#type
        :param choices: https://docs.python.org/3.6/library/argparse.html#choices
        :param required: https://docs.python.org/3.6/library/argparse.html#required
        :param help: https://docs.python.org/3.6/library/argparse.html#help
        :param metavar: https://docs.python.org/3.6/library/argparse.html#metavar
        :param version: Only used in version args, an optional string containing the version of the application.
        :param group: Used to associate the argument with the provided group
        """

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
        # type: () -> Any
        """ An alternative to ArgumentParser.get_default """
        return self._default

    @default.setter
    def default(self, value):
        # type: (Any) -> None
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
            *flags,  # type: Union[str, List[str]]
            help=_keep_default,  # type: Optional[str]
    ):
        """
        :param flags: Flags for the help argument, when not specified -h and --help are used
        :param help: The help string
        """

        if not flags:
            flags = ["--help", "-h"]

        super(HelpArg, self).__init__(*flags, help=help, action=ActionName.help)


class VersionArg(Arg):

    # noinspection PyShadowingBuiltins
    def __init__(
            self,
            *flags,  # type: Union[str, List[str]]
            version=None,  # type: Optional[str]
            help=_keep_default,  # type: Optional[str]
    ):
        """
        :param flags: Flags for the version argument, when not specified -v and --version are used
        :param version: The version string
        :param help: A help message for the version argument
        """

        if not flags:
            flags = ["--version", "-v"]

        super(VersionArg, self).__init__(*flags, version=version, help=help, action=ActionName.version)


class Args(_BaseArg):
    """
    Lets a couple of args set a value to the same destination, useful for example with set_const
    where each arg sets a different constant value.
    """

    def __init__(self, args=None, args_default=None):
        # type: (Optional[List[Arg], Optional[Any]]) -> None
        """
        :param args: A list of Arg objects
        :param args_default: A default value to set when none of args was invoked
        """

        super(Args, self).__init__()

        if args is None:
            args = []

        self.args = args
        self.args_default = args_default


class ArgumentGroup(object):
    """
    A parallel to ArgumentParser.add_argument_group, used as the group argument of an Arg object
    """

    def __init__(self, title=None, description=None):
        # type: (Optional[str], Optional[str]) -> None
        self.title = title
        self.description = description


class MutuallyExclusiveGroup(Args):
    """
    A parallel to ArgumentParser.add_mutually_exclusive_group, can be used in two ways:
    1) Like ArgumentGroup supplied as the group parameter of an Arg object
    2) Used like the Args object
    In both cases all associated arguments will be mutually exclusive as expected, Usage as an Args object is more
    recommended, the Group like usage is added in case it doesn't cover all use cases.
    """

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
    """
    A parallel to the ArgumentParser.add_subparsers call, we set this up in the ParserHolder._subparser_config
    property to control the the creation of the subparser action
    """

    _kwarg_names = (
        "title", "description", "prog", "parser_class", "action", "option_string", "help", "metavar",
    )

    # noinspection PyShadowingBuiltins
    def __init__(
            self,
            title=_keep_default,  # type: Optional[str]
            description=_keep_default,  # type: Optional[str]
            prog=_keep_default,  # type: Optional[str]
            parser_class=_keep_default,  # type: Optional[argparse.ArgumentParser]
            action=_keep_default,  # type: Union[None, str, argparse.Action]
            option_string=_keep_default,  # type: Optional[str]
            help=_keep_default,  # type: Optional[str]
            metavar=_keep_default,  # type: Optional[str]
    ):
        """

        :param title: title for the sub-parser group in help output; by default “subcommands”
        if description is provided, otherwise uses title for positional arguments
        :param description: description for the sub-parser group in help output, by default None
        :param prog: usage information that will be displayed with sub-command help, by default
        the name of the program and any positional arguments before the subparser argument
        :param parser_class: class which will be used to create sub-parser instances, by default
        the class of the current parser (e.g. ArgumentParser)
        :param action: the basic type of action to be taken when this argument is encountered at
        the command line
        :param option_string: Mentioned in the signature of add_subparsers in the documentations
        and only there, I am not sure if and how it is used, and I left it here just in case it
        is needed for someone.
        :param help: help for sub-parser group in help output, by default None
        :param metavar: string presenting available sub-commands in help; by default it is None
        and presents sub-commands in form {cmd1, cmd2, ..}
        """
        self.title = title
        self.description = description
        self.prog = prog
        self.parser_class = parser_class
        self.action = action
        self.option_string = option_string
        self.help = help
        self.metavar = metavar


class SubParserMapper(_BaseArg):
    """
    A mapper of subparser name to anything that we want to set when the subparser is chosen
    None set parsers are not allowed in this implementation (explicit better than implicit)
    But you can subclass this parser and change _must_set_all_parsers to False to overwrite this.
    """

    # Subclass with a False value (or change in the instance you create, to allow unset parsers.
    _must_set_all_parsers = True

    def __init__(self, **kwargs):
        # type: (Dict[str, Any]) -> None
        super(SubParserMapper, self).__init__()
        self.map = kwargs


# =============================
# The parser class: The main class of this library.
# =============================

@_add_metaclass(_ParserHolderMeta)
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
        Do note that you most likely can achieve what you want by implementing it in a subclass, instead of accessing
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
        self._subparser_action = None

    def _get_parser_kwargs(self, add_help):

        if self._argument_default == SUPPRESS:
            raise SuppressError()

        class_ = type(self)
        # noinspection PyProtectedMember,PyCallByClass,PyTypeChecker
        parser_kwargs = class_._get_kwargs(class_)

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
                    raise NoArgumentInParser(parser=self._namespace, dest=action.dest)
                setattr(self._namespace, action.dest, action.default)

        # noinspection PyProtectedMember,PyUnresolvedReferences
        for dest, value in self._parser._defaults.items():
            if dest not in dir(self._namespace):
                # I think if that happens we have a bug
                raise NoArgumentInParser(parser=self._namespace, dest=dest)
            setattr(self._namespace, dest, value)

        subparser_names = {n for n, a in self._sorted_arguments if isinstance(a, ParserHolder)}
        subparser_mappers = list((n, a) for n, a in self._sorted_arguments if isinstance(a, SubParserMapper))

        for argument_name, argument in self._sorted_arguments:
            if isinstance(argument, ParserHolder):
                self._add_subparser(argument=argument, argument_name=argument_name, subparser_mappers=subparser_mappers)
            elif isinstance(argument, Args):
                for group_argument in argument.args:
                    if not isinstance(group_argument, Arg):
                        raise UnsupportedArgumentTypeInArgs(argument=group_argument)

                    if isinstance(argument, MutuallyExclusiveGroup):
                        group_argument.group = argument
                    self._add_argument(argument=group_argument, argument_name=argument_name)
                self._parser.set_defaults(**{argument_name: argument.args_default})
            elif isinstance(argument, Arg):
                self._add_argument(argument=argument, argument_name=argument_name)
            elif isinstance(argument, SubParserMapper):
                for name in _viewkeys(argument.map):
                    if name not in subparser_names:
                        raise NoSubParserForKeyInMapper(name=name)
                # noinspection PyProtectedMember
                if argument._must_set_all_parsers:
                    for name in subparser_names:
                        if name not in argument.map:
                            raise MissingSubParserKeyInMapper(name=name)
            else:
                raise UnsupportedArgumentType(argument=argument)

        if self._help is not None:
            if isinstance(self._help, _string_types):
                help_argument = HelpArg(
                    *[a.format(p=self._parser.prefix_chars) for a in ("{p}{p}help", "{p}h")],
                    help=self._help)
            elif isinstance(self._help, Arg):
                help_argument = self._help
            else:
                raise UnsupportedHelpArgumentType(argument=self._help)

            self._add_argument(argument=help_argument, argument_name=_not_named_argument)

        if self._version is not None:
            if isinstance(self._version, _string_types):
                version_argument = VersionArg(
                    *[a.format(p=self._parser.prefix_chars) for a in ("{p}{p}version", "{p}v")],
                    version=self._version)
            elif isinstance(self._version, Arg):
                version_argument = self._version
            else:
                raise UnsupportedVersionArgumentType(argument=self._version)

            self._add_argument(argument=version_argument, argument_name=_not_named_argument)

    def _add_subparser(self, argument, argument_name, subparser_mappers):

        if self._subparser_action is None:
            if self._subparser_config is None:
                subparser_config = SubParserConfig()
            else:
                subparser_config = self._subparser_config
            # noinspection PyProtectedMember
            subparser_config_kwargs = subparser_config._get_kwargs()
            self._subparser_action = self._parser.add_subparsers(**subparser_config_kwargs)

            setattr(self._subparser_action, "__alias_to_name", {})
            setattr(self._subparser_action, "__name_to_namespace", {})

            _subparser_action_call_patch(self._subparser_action, self._namespace, subparser_mappers)

        # noinspection PyProtectedMember
        add_parser_kwargs = dict(argument._parser_kwargs)
        # noinspection PyProtectedMember
        add_parser_kwargs.update(argument._get_kwargs())

        argument._parser = self._subparser_action.add_parser(argument_name, **add_parser_kwargs)

        alias_to_name = getattr(self._subparser_action, "__alias_to_name")
        name_to_namespace = getattr(self._subparser_action, "__name_to_namespace")
        name_to_namespace[argument_name] = argument
        alias_to_name[argument_name] = argument_name
        for alias in add_parser_kwargs.get("aliases", []):
            alias_to_name[alias] = argument_name

        # noinspection PyProtectedMember
        argument._fill_parser()

    def _add_argument(self, argument, argument_name):

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
                    raise UnsupportedGroupType(group=argument.group)

                self._group_to_group_parser[argument.group] = group_parser

            add_argument_function = self._group_to_group_parser[argument.group].add_argument

        # noinspection PyNoneFunctionAssignment
        action = add_argument_function(*argument.flags, **argument_kwargs)
        # noinspection PyTypeChecker
        _action_call_patch(action, self._namespace)

    def set_default(self, name, value):

        if name not in dir(self):
            raise ArgumentForDefaultValueDoesntExist(parser=self, attribute_name=name)

        self._parser.set_defaults(**{name: value})

    def set_defaults(self, **kwargs):

        for name, value in _viewitems(kwargs):
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
