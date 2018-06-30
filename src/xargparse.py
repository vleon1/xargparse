# Copyright (c) 2018 Leon Vaiman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Class based extension to argparse
"""
import os
import sys

# Exposing all argparse here so that users don't have to import it as well.
import argparse
from argparse import *  # pylint: disable=wildcard-import,unused-wildcard-import


# pylint: disable=too-many-lines


# A little trick to make sure we don't really try to import typing unless we need them
if "mypy" in os.environ:
    # pylint: disable=unused-import,import-error
    from typing import Dict, Any, List, Optional, Union, Callable, Iterable, Tuple, Set


# =============================
# Compatibility: This section contains code that is needed for this library to work with both
# python 2 and python 3 the code itself was stolen from the six library (with minor alternations).
# I didn't use the library directly to avoid any external dependencies for this library.
# =============================


# I stole this code from the six library, Since I wanted fro users of this package to be able to
# just copy the source file to their project, without an extra dependency.
if sys.version_info.major >= 3:
    # noinspection PyUnresolvedReferences,PyCompatibility
    _viewkeys = dict.keys  # type: ignore # pylint: disable=invalid-name,no-member,undefined-variable
    # noinspection PyUnresolvedReferences,PyCompatibility
    _viewitems = dict.items  # type: ignore # pylint: disable=invalid-name,no-member,undefined-variable
    # noinspection PyUnresolvedReferences,PyCompatibility
    _string_types = (str,)  # type: ignore # pylint: disable=invalid-name,no-member,undefined-variable
else:  # python 2
    # noinspection PyUnresolvedReferences,PyCompatibility
    _viewkeys = dict.viewkeys  # type: ignore # pylint: disable=invalid-name,no-member,undefined-variable
    # noinspection PyUnresolvedReferences,PyCompatibility
    _viewitems = dict.viewitems  # type: ignore # pylint: disable=invalid-name,no-member,undefined-variable
    # noinspection PyUnresolvedReferences,PyCompatibility
    _string_types = (basestring,)  # type: ignore # pylint: disable=invalid-name,no-member,undefined-variable


def _add_metaclass(metaclass):
    # type: (Any) -> Any
    """ This is also stolen from the six library """
    def wrapper(cls):
        # type: (Any) -> Any
        """ Recreates the class using the supplied metaclass """
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

def _action_call_patch(action, class_parser):
    # type: (argparse.Action, ClassParser) -> None
    """
    A hack function that allows us to patch argparse action.__call__ to use our ClassParser
    objects as a namespace instead of the provided one. This is ugly, but considering all the
    other alternatives I think it is the best choice.
    It allows us to support all existing Action classes in argparse and any user created sub-classes
    without the need to change anything, or add tons of subclasses.
    The downside is that if a user have an Action subclass that does something with the namespace
    that shouldn't be done on our ClassParser object, unexpected things might happen that are
    difficult to debug.
    But from the user's point of view the ClassParser is the namespace, and the library doesn't
    allow to supply a custom namespace argument anyway, so hopefully these cases should be rare
    enough.
    """

    parent = type(action)

    class Replacer(parent):  # type: ignore # pylint: disable=too-few-public-methods
        """ Replaces the original class to overwrite __call__ """

        def __call__(self, parser, namespace, values, option_string=None):
            # type: (argparse.ArgumentParser, ClassParser, List[str], Optional[str]) -> None
            del namespace
            # noinspection PyTypeChecker
            return super(Replacer, self).__call__(parser, class_parser, values, option_string)

    Replacer.__name__ = parent.__name__
    action.__class__ = Replacer


# noinspection PyProtectedMember
def _subparser_action_call_patch(action, class_parser, subparser_mappers):
    # type: (argparse._SubParsersAction, ClassParser, List[Tuple[str, SubParserMapper]]) -> None
    """ Same hack as _action_call_patch but with extra logic for subparsers """

    parent = type(action)

    class Replacer(parent):  # type: ignore # pylint: disable=too-few-public-methods
        """ Replaces the original class to overwrite __call__ """

        def __call__(self, parser, namespace, values, option_string=None):
            # type: (argparse.ArgumentParser, ClassParser, List[str], Optional[str]) -> None

            alias = values[0]
            alias_to_name = getattr(self, "__alias_to_name")  # type: Dict[str, str]
            name_to_namespace = getattr(self, "__name_to_namespace")  # type: Dict[str, ClassParser]

            # Set all parsers to None, only the one that was chosen will get overwritten
            for name in _viewkeys(name_to_namespace):
                setattr(class_parser, name, None)

            name = alias_to_name[alias]
            setattr(class_parser, name, name_to_namespace[name])

            for mapper_name, mapper in subparser_mappers:
                value = mapper.map.get(name, None)
                setattr(class_parser, mapper_name, value)

            # noinspection PyTypeChecker,PyUnresolvedReferences
            return super(Replacer, self).__call__(parser, namespace, values, option_string)

    Replacer.__name__ = parent.__name__
    action.__class__ = Replacer


# =============================
# Exceptions: All exceptions are defined here
# =============================

class SuppressError(ValueError):
    """
    An exception thrown in case the user tries to use the argparse.SUPPRESS as a value, since not
    setting an argument goes against the whole logic and idea of this library.
    """
    def __init__(self):
        # type: () -> None
        super(SuppressError, self).__init__(
            "SUPPRESS is not supported for argument "
            "defaults since it makes no sense in class context"
        )


class UnparsedArgumentAccess(AttributeError):
    """
    Raised when we try to access a ClassParser attribute before parse_args or parse_known_args was
    called.
    """
    def __init__(self):
        # type: () -> None
        super(UnparsedArgumentAccess, self).__init__("Tried to access an unparsed argument")


class ArgumentForDefaultValueDoesntExist(AttributeError):
    """
    Raised when trying to set a default value for an attribute that doesn't exist
    """
    def __init__(self, class_parser, attribute_name):
        # type: (ClassParser, str) -> None
        super(ArgumentForDefaultValueDoesntExist, self).__init__(
            "class '%s' has no attribute named '%s'" % (type(class_parser), attribute_name)
        )


class NoArgumentInParser(AttributeError):
    """
    Raised when trying to set a value to an argument of a parser, but the parser didn't define this
    argument
    """

    def __init__(self, class_parser, dest):
        # type: (ClassParser, str) -> None
        super(NoArgumentInParser, self).__init__(
            "class '%s' doesn't have the attribute '%s'" % (type(class_parser), dest)
        )


class UnexpectedArgumentsInInit(AttributeError):
    """
    Raised when one of the classes with a dynamic kwargs init gets an unexpected argument.

    Due to python 2 compatibility we had to use dynamic kwargs in some of the classes.
    """

    def __init__(self, instance, arguments):
        # type: (Any, Iterable[str]) -> None
        super(UnexpectedArgumentsInInit, self).__init__(
            "Class '%s' got unexpected arguments in __init__: '%s'" %
            (type(instance), ", ".join(arguments))
        )


class UnsupportedType(TypeError):
    """
    Generic base exception raised when an argument of a wrong type is used in the wrong place
    """
    message_template = ""

    def __init__(self, argument):
        # type: (Any) -> None
        super(UnsupportedType, self).__init__(self.message_template % type(argument))


class UnsupportedGroupType(UnsupportedType):
    """
    Raised when a group parameter in an Argument is not a sub-class of one of the supported group
    types
    """
    message_template = "Unsupported type '%s' in group argument"

    def __init__(self, group):
        # type: (Any) -> None
        super(UnsupportedGroupType, self).__init__(argument=group)


class UnsupportedSubParserConfigType(UnsupportedType):
    """
    Raised when a subparser config object is not of the SubParserConfig type
    """
    message_template = "Unsupported type '%s' for subparser"

    def __init__(self, subparser_config):
        # type: (Any) -> None
        super(UnsupportedSubParserConfigType, self).__init__(argument=subparser_config)


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
    def __init__(self, subparser_name):
        # type: (str) -> None
        super(MissingSubParserKeyInMapper, self).__init__(
            "SubParserMapper is missing a key for the SubParser '%s'" % subparser_name
        )


class NoSubParserForKeyInMapper(KeyError):
    """  Raised when a SubParserMapper contains a key with noe SubParser to map to """
    def __init__(self, subparser_name):
        # type: (str) -> None
        super(NoSubParserForKeyInMapper, self).__init__(
            "SubParserMapper maps to a none existing SubParser '%s'" % subparser_name
        )


# =============================
# Globals: Global definitions used int the library
# =============================


# When default is not set the argparse would use None instead of [] or 0 in places where these value
# are far more logical (a.k.a sane) if this is set to True we overwrite this "insane" behaviour.
#
# There was a dilemma of whether this change should be added or not, since we usually want to work
# as a one to one wrapper to argparse.
# But our goal is to achieve easy type friendly arguments, and with the old defaults it breaks that.
# The user can still define the argument with default=None if he wants that specific behaviour, but
# when nothing is defined the new behaviour is used.
#
# This variable allows us to change the behaviour of this library to be more strict in that matter,
# we can also add an overwrite in a class and/or in an instance level of ClassParser, but I see no
# reason to do so right now.
USE_SANE_DEFAULTS = True


# Used internally to indicate that an argument should not be passed as part of an argument dict
# (In other words the receiving function should use its own default value for the argument)
_KEEP_DEFAULT = object()


# Used internally for the version and help arguments to avoid setting a dest on these parameters
_NOT_NAMED_ARGUMENT = object()


# =============================
# Name classes: Helper enum like classes used to replace string usage with class variable usage
# =============================

class ActionName(object):  # pylint: disable=too-few-public-methods
    """
    Use this for string actions, because named variables get auto completion and strings don't...
    """

    # This just stores the argument's value. This is the default action.
    store = "store"

    # This stores the value specified by the const keyword argument.
    # The 'store_const' action is most commonly used with optional arguments that specify some sort
    # of flag.
    store_const = "store_const"

    # A special cases of 'store_const' used for storing the value True.
    # In addition, it creates a default value of False.
    store_true = "store_true"

    # A special cases of 'store_const' used for storing the value False.
    # In addition, it creates a default value of True.
    store_false = "store_false"

    # This stores a list, and appends each argument value to the list.
    # This is useful to allow an option to be specified multiple times.
    append = "append"

    # This stores a list, and appends the value specified by the const keyword argument to the list.
    # (Note that the const keyword argument defaults to None.)
    # The 'append_const' action is typically useful when multiple arguments need to store constants
    # to the same list using an Args object.
    append_const = "append_const"

    # This counts the number of times a keyword argument occurs.
    # For example, this is useful for increasing verbosity levels.
    count = "count"

    # This prints a complete help message for all the options in the current parser and then exits.
    # By default a help action is automatically added to the parser.
    # See ClassParser for details of how the output is created.
    help = "help"

    # This expects a version= keyword argument in the Arg class,
    # and prints version information and exits when invoked.
    version = "version"


class ConflictHandlerName(object):  # pylint: disable=too-few-public-methods
    """
    Use this when setting _conflict_handler in the ClassParser instead of relying on strings
    """

    # The default conflict handler, Any duplicates will create an error.
    error = "error"

    # Overwrites duplicates
    resolve = "resolve"


class NArgName(object):  # pylint: disable=too-few-public-methods
    """
    Use this instead of the strings '?', '+' etc.. for nargs, you can also directly use the globals
    in argparse
    """

    # One argument will be consumed from the command line if possible, and produced as a single
    # item.
    # If no command-line argument is present, the value from default will be produced.
    # Note that for optional arguments, there is an additional case -
    # the option string is present but not followed by a command-line argument.
    # In this case the value from const will be produced.
    # One of the more common uses of nargs=optional is to allow optional input and output files.
    optional = argparse.OPTIONAL  # ?

    # All command-line arguments present are gathered into a list.
    # Note that it generally doesn't make much sense to have more than one positional argument
    # with nargs=zero_or_more, but multiple optional arguments with nargs=zero_or_more is
    # possible.
    zero_or_more = argparse.ZERO_OR_MORE  # *

    # Just like zero_or_more, all command-line args present are gathered into a list.
    # Additionally, an error message will be generated if there wasn't at least one
    # command-line argument present.
    one_or_more = argparse.ONE_OR_MORE  # +

    # All the remaining command-line arguments are gathered into a list.
    # This is commonly useful for command line utilities that dispatch to other command line
    # utilities.
    remainder = argparse.REMAINDER  # ...


# =============================
# Base and Meta classes: Classes used to provide all the magic functionality of the library, these
# classes are considered very low level and thus they are all private.
# =============================


class _Sortable(object):  # pylint: disable=too-few-public-methods
    """
    Any class inheriting this one will have instances that can be sorted against each other by the
    order of declaration. They use the _instance_index variable to do that, and it is guaranteed
    that if two instances of _Sortable where declared one after another in the same class, the
    second one will have a higher index.
    This is also the only thing guaranteed about _instance_index.
    """

    _global_index_counter = 0

    def __init__(self):
        # type: () -> None

        # No need to protect from racing access, since in a case of a "race" it will happen with
        # two different classes and so both will raise the counter and will have the same index
        # value, but internally the class arguments will still have sorted different indexes..
        _Sortable._global_index_counter += 1
        self._instance_index = _Sortable._global_index_counter

        super(_Sortable, self).__init__()


class _KwargsHolder(object):  # pylint: disable=too-few-public-methods
    """
    An inner class used to hold keyword arguments for functions and classes that we don't want to
    immediately evaluate.
    """

    _kwarg_names = []  # type: List[str]
    _kwargs_name_prefix = ""

    def _get_kwargs(self):
        # type: () -> Dict[str, Any]
        class_ = type(self)
        all_kwarg_pairs = (
            (k, getattr(self, class_._kwargs_name_prefix + k))  # pylint: disable=protected-access
            for k in class_._kwarg_names  # pylint: disable=protected-access
        )
        return {k: v for k, v in all_kwarg_pairs if v is not _KEEP_DEFAULT}


class _ParsedProperty(object):
    """
    Implements __get__ and __set__ methods that make sure that we don't access an instance of this
    class that wasn't parsed (aka __set__) first..
    """

    def __init__(self):
        # type: () -> None

        self._instance_to_value = {}  # type: Dict[_ParsedProperty, Any]

        super(_ParsedProperty, self).__init__()

    def __get__(self, instance, owner):
        # type: (_ParsedProperty, Any) -> None
        del owner

        if instance not in self._instance_to_value:
            raise UnparsedArgumentAccess()

        return self._instance_to_value[instance]

    def __set__(self, instance, value):
        # type: (_ParsedProperty, Any) -> None
        self._instance_to_value[instance] = value


class _BaseArg(_Sortable, _ParsedProperty, _KwargsHolder):  # pylint: disable=too-few-public-methods
    """
    All classes that can be used as arguments inherit this class, and we use this class to store a
    sorted list of such argument in our ClassParser class.
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
        arguments = ", ".join(
            "%s=%r" % (n, v) for n, v in sorted(name_and_values, key=lambda nv: nv[0])
        )
        return "%s(%s)" % (type(self).__name__, arguments)


class _ClassParserMeta(type, _KwargsHolder):
    """
    We use this meta class for two reasons:
    1) To give our classes the _sorted_arguments variable that allows us to get only the _BaseArg
       arguments defined in the class (and not in the parents). We use __new__ to do that and it
       allows us to easily implement proper ArgumentParser.parents behaviour in our __init__ method
    2) To supply the _get_kwargs method for the ClassParser class (if ClassParser were to inherit
       _KwargsHolder it would have been an instance method and that is useless to us..)
    """

    _kwarg_names = [
        "description", "prog", "usage", "epilog", "formatter_class", "prefix_chars",
        "fromfile_prefix_chars", "argument_default", "conflict_handler", "add_help",
    ]
    _kwargs_name_prefix = "_"

    def __new__(mcs, name, bases, attrs):
        # type: (Any, str, List[Any], Dict[str, Any]) -> None

        _sortable_arguments = ((k, v) for k, v in attrs.items() if isinstance(v, _BaseArg))
        # noinspection PyProtectedMember
        attrs["_sorted_arguments"] = sorted(
            _sortable_arguments,
            key=lambda kv: kv[1]._instance_index  # pylint: disable=protected-access
        )

        return super(_ClassParserMeta, mcs).__new__(mcs, name, bases, attrs)  # type: ignore


# =============================
# Argument Objects: All the argument related objects are defined here
# =============================

class Arg(_BaseArg):  # pylint: disable=too-few-public-methods,too-many-instance-attributes
    """
    Define how a single command-line argument should be parsed.
    """

    _kwarg_names = [
        "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar",
        "version",
    ]

    def __init__(self, *flags, **kwargs):
        # type: (...) -> None
        """
        :param flags: A flag or a list of flags for optional arguments (This will turn this argument
        into an optional one..)
        :param action: The basic type of action to be taken when this argument is encountered at the
        command line.
        :param nargs: The number of command-line arguments that should be consumed.
        :param const: A constant value required by some action and nargs selections.
        :param default: The value produced if the argument is absent from the command line.
        :param type: The type to which the command-line argument should be converted.
        :param choices: A container of the allowable values for the argument.
        :param required: Whether or not the command-line option may be omitted (optionals only).
        :param help: A brief description of what the argument does.
        :param metavar: A name for the argument in usage messages.
        :param version: Only used in version args, an optional string containing the version of the
        application.
        :param group: Used to associate the argument with the provided group
        """

        super(Arg, self).__init__()

        self.flags = flags
        self.action = kwargs.pop(
            "action", _KEEP_DEFAULT)  # type: Union[None, str, argparse.Action, object]
        self.nargs = kwargs.pop("nargs", _KEEP_DEFAULT)  # type: Union[None, str, int, object]
        self.const = kwargs.pop("const", _KEEP_DEFAULT)  # type: Any
        self.type = kwargs.pop("type", _KEEP_DEFAULT)  # type: Any
        self.choices = kwargs.pop("choices", _KEEP_DEFAULT)  # type: Union[List[Any], object]
        self.required = kwargs.pop("required", _KEEP_DEFAULT)  # type: Union[bool, object]

        self.help = kwargs.pop("help", _KEEP_DEFAULT)  # type: Union[None, str, object]
        self.metavar = kwargs.pop("metavar", _KEEP_DEFAULT)  # type: Union[None, str, object]
        self.version = kwargs.pop("version", _KEEP_DEFAULT)  # type: Union[None, str, object]

        self.group = kwargs.pop(
            "group", None)  # type: Union[None, ArgumentGroup, MutuallyExclusiveGroup]
        # This is overwritten by the next line, and is only set to make the ide happy.
        self._default = kwargs.pop("default", _KEEP_DEFAULT)  # type: Any
        # Keep at the end since the setter does checks that can depend on the other values
        self.default = self._default

        if kwargs:
            raise UnexpectedArgumentsInInit(instance=self, arguments=_viewkeys(kwargs))

    @property
    def default(self):
        # type: () -> Any
        """
        Get the default value of an argument
        """
        return self._default

    @default.setter
    def default(self, value):
        # type: (Any) -> None
        """
        make sure that we don't set illegal values to to an arguments, and makes better defaults
        when needed.
        """

        # we also make sure SUPPRESS is not used here
        if value == SUPPRESS:
            raise SuppressError()

        if USE_SANE_DEFAULTS and value is _KEEP_DEFAULT:

            list_default = (
                self.action == ActionName.append or
                self.nargs == "*" or
                self.nargs == "+" or
                self.nargs == REMAINDER
            )
            if list_default:
                value = []

            if self.action == ActionName.count:
                value = 0

        self._default = value


class HelpArg(Arg):  # pylint: disable=too-few-public-methods
    """
    A convenience subclass for help arguments
    """

    def __init__(self, *flags, **kwargs):
        # type: (...) -> None
        """
        :param flags: Flags for the help argument, when not specified -h and --help are used
        :param help: The help string
        """

        if not flags:
            flags = ["--help", "-h"]  # type: ignore

        action = ActionName.help
        help_ = kwargs.pop("help", _KEEP_DEFAULT)  # type: Union[None, str, object]

        if kwargs:
            raise UnexpectedArgumentsInInit(instance=self, arguments=_viewkeys(kwargs))

        super(HelpArg, self).__init__(*flags, action=action, help=help_)


class VersionArg(Arg):  # pylint: disable=too-few-public-methods
    """ A convenience subclass for version arguments """

    def __init__(self, *flags, **kwargs):
        # type: (...) -> None
        """
        :param flags: Flags for the version argument, when not specified -v and --version are used
        :param version: The version string
        :param help: A help message for the version argument
        """

        if not flags:
            flags = ["--version", "-v"]  # type: ignore

        action = ActionName.version
        help_ = kwargs.pop("help", _KEEP_DEFAULT)  # type: Union[None, str, object]
        version = kwargs.pop("version", None)  # type: Optional[str]

        if kwargs:
            raise UnexpectedArgumentsInInit(instance=self, arguments=_viewkeys(kwargs))

        super(VersionArg, self).__init__(*flags, action=action, help=help_, version=version)


class Args(_BaseArg):  # pylint: disable=too-few-public-methods
    """
    Lets a couple of args set a value to the same destination, useful for example with set_const
    where each arg sets a different constant value.
    """

    def __init__(self, args=None, args_default=None):
        # type: (Optional[List[Arg]], Optional[Any]) -> None
        """
        :param args: A list of Arg objects
        :param args_default: A default value to set when none of args was invoked
        """

        super(Args, self).__init__()

        if args is None:
            args = []

        self.args = args
        self.args_default = args_default


class ArgumentGroup(object):  # pylint: disable=too-few-public-methods
    """
    By default, ClassParser groups command-line arguments into "positional arguments"
    and "optional arguments" when displaying help messages.
    When there is a better conceptual grouping of arguments than this default one,
    appropriate groups can be created using the ArgumentGroup class, and added as the group
    parameter of the Arg objects.
    """

    def __init__(self, title=None, description=None):
        # type: (Optional[str], Optional[str]) -> None
        self.title = title
        self.description = description


class MutuallyExclusiveGroup(Args):  # pylint: disable=too-few-public-methods
    """
    Create a mutually exclusive group. xargparse will make sure that only one of the arguments in
    the mutually exclusive group was present on the command line.

    Can be used in two ways:
    1) Like ArgumentGroup supplied as the group parameter of an Arg object
    2) Used like the Args object
    In both cases all associated arguments will be mutually exclusive as expected, Usage as an Args
    object is more recommended, the Group like usage is added in case it doesn't cover all use
    cases.
    """

    def __init__(self, required=False, args=None, args_default=None):
        # type: (bool, Optional[List[Arg]], Optional[Any]) -> None
        """
        :param required: Makes sure that at least of argument in the group should be set
        :param args: When used as an argument, this list of arguments will be added to the group
        with their result put in the groups variable name.
        :param args_default: when used as an argument and required is set to false, this will be
        used when none of the grouped argument is selected
        """
        super(MutuallyExclusiveGroup, self).__init__(args=args, args_default=args_default)

        self.required = required


class SubParserConfig(_KwargsHolder):  # pylint: disable=too-few-public-methods,too-many-instance-attributes
    """
    Many programs split up their functionality into a number of sub-commands,
    for example, the svn program can invoke sub-commands like svn checkout, svn update, and svn
    commit.
    Splitting up functionality this way can be a particularly good idea when a program performs
    several different functions which require different kinds of command-line arguments.
    ClassParser supports the creation of such sub-commands by having ClassParser arguments that
    represent them.
    To control how sub-parsers are created for the provided ClassParser object we use the
    SubParserConfig class.
    """

    _kwarg_names = [
        "title", "description", "prog", "parser_class", "action", "option_string", "help",
        "metavar",
    ]

    # noinspection PyShadowingBuiltins
    def __init__(  # type: ignore # pylint: disable=too-many-arguments
            self,
            title=_KEEP_DEFAULT,  # type: Optional[str]
            description=_KEEP_DEFAULT,  # type: Optional[str]
            prog=_KEEP_DEFAULT,  # type: Optional[str]
            parser_class=_KEEP_DEFAULT,  # type: Optional[argparse.ArgumentParser]
            action=_KEEP_DEFAULT,  # type: Union[None, str, argparse.Action]
            option_string=_KEEP_DEFAULT,  # type: Optional[str]
            help=_KEEP_DEFAULT,  # type: Optional[str]  # pylint: disable=redefined-builtin
            metavar=_KEEP_DEFAULT,  # type: Optional[str]
    ):
        # type: (...) -> None
        """

        :param title: title for the subparser group in help output; by default "subcommands"
        if description is provided, otherwise uses title for positional arguments
        :param description: description for the subparser group in help output, by default None
        :param prog: usage information that will be displayed with sub-command help, by default
        the name of the program and any positional arguments before the subparser argument
        :param parser_class: class which will be used to create subparser instances, by default
        the class of the current parser (e.g. ArgumentParser)
        :param action: the basic type of action to be taken when this argument is encountered at
        the command line
        :param option_string: Mentioned in the signature of add_subparsers in the documentations
        and only there, I am not sure if and how it is used, and I left it here just in case it
        is needed for someone.
        :param help: help for subparser group in help output, by default None
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


class SubParserMapper(_BaseArg):  # pylint: disable=too-few-public-methods
    """
    A mapper of subparser name to anything that we want to set when the subparser is chosen.
    Not set parsers are not allowed in this implementation (explicit is better than implicit)
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

@_add_metaclass(_ClassParserMeta)
class ClassParser(_BaseArg):
    """
    Use this class to get a commandline argument, it is a parallel to argparse.ArgumentParser
    except that ArgumentParser is also used internally.

    You use this class by subclassing it, you replace the add_argument calls you would do with
    ArgumentParser with adding Arg objects to the sub-class (In the same order you would have
    called add_argument).
    """

    # The name of the program (default: sys.argv[0])
    _prog = _KEEP_DEFAULT

    # The string describing the program usage (default: generated from arguments added to parser)
    _usage = _KEEP_DEFAULT

    # Text to display before the argument help (default: none)
    _description = _KEEP_DEFAULT

    # Text to display after the argument help (default: none)
    _epilog = _KEEP_DEFAULT

    # A class for customizing the help output
    _formatter_class = _KEEP_DEFAULT

    # The set of characters that prefix optional arguments (default: '-')
    _prefix_chars = _KEEP_DEFAULT

    # The set of characters that prefix files from which additional arguments should be read
    # (default: None)
    _fromfile_prefix_chars = _KEEP_DEFAULT

    # The global default value for arguments (default: None)
    _argument_default = _KEEP_DEFAULT

    # The strategy for resolving conflicting optionals (usually unnecessary)
    _conflict_handler = _KEEP_DEFAULT

    # Add a -h/--help option to the parser (default: True)
    _add_help = _KEEP_DEFAULT

    # Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)
    # Supported only in python>=3.5 on other versions it is silently ignored
    _allow_abbrev = _KEEP_DEFAULT

    # Change the parser class
    _parser_class = argparse.ArgumentParser

    # Overwrite to add a help argument manually
    # Set it to a string to get a default HelpArg with the help parameter set to this string
    # Set it to a HelpArg for more control
    # You can also use Arg but that is less comfortable, more error prone and should not be
    # necessary since HelpArg is built in a way that is supposed to let you achieve everything
    # that is possible with this type of arguments
    #
    # Setting this and _add_help to anything that evaluates to True will probably create a conflict
    _help = None

    # Overwrite to add a version argument manually
    # Set it to a string to get a default VersionArg with the version parameter set to this string
    # Set it to a VersionArg for more control
    # You can also use Arg but that is less comfortable, more error prone and should not be
    # necessary since VersionArg is built in a way that is supposed to let you achieve everything
    # that is possible with this type of arguments
    _version = None

    # Set this property to configure the subparser used for sub-commands (It accepts the same
    # parameters as the add_subparsers that you would have used with ArgumentParser.
    # There is no need to supply this argument when you use sub-parsers, but if left empty the
    # add_subparsers will be called without arguments.
    # You should only supply a SubParser argument here, or leave it as None.
    _subparser_config = None

    # Used internally when the parser is used as a subparser
    _kwarg_names = ["prog", "aliases", "help"]
    _kwargs_name_prefix = "__"

    # noinspection PyShadowingBuiltins
    def __init__(  # type: ignore
            self,
            prog=_KEEP_DEFAULT,  # type: Optional[str]
            aliases=_KEEP_DEFAULT,  # type: Optional[List[str]]
            help=_KEEP_DEFAULT,  # type: Optional[str]  # pylint: disable=redefined-builtin
            _add_help=None,  # type: Optional[bool]
            _namespace=None  # type: Optional[ClassParser]
    ):
        # type: (...) -> None
        """
        If you overwrite the __init__ method, DO NOT call super since that will break parents usage.

        :param prog: When initiated as a subparser it is used to set the prog argument, ignored
        otherwise
        :param aliases: When initiated as a subparser it is used to set the aliases argument,
        ignored otherwise
        :param help: When initiated as a subparser it is used to set the help argument, ignored
        otherwise
        :param _add_help: Used internally, Setting this will overwrite the class parameter but
        using this parameter like that should be avoided.
        :param _namespace: Used internally, we pass self to parent class using this argument to
        make sure they add parameters to this object, and not to the temporary parent instance.
        """

        super(ClassParser, self).__init__()

        # noinspection PyProtectedMember
        setattr(self, "__prog", prog)
        setattr(self, "__aliases", aliases)
        setattr(self, "__help", help)

        if _add_help is None:
            _add_help = self._add_help  # type: ignore

        if _namespace is None:
            _namespace = self
        self._namespace = _namespace

        # The parser is not exposed since the name might be used for an argument and since direct
        # usage will most likely break things.
        # But if there is a missing feature in this implementation, or a bug that is possible to
        # overcome by directly using _parser, then nothing stops you from doing so.
        # Do note that you most likely can achieve what you want by implementing it in a subclass,
        # instead of accessing the instance's "_parser" variable.
        #
        # Note that in subparser mode this parameter will be overwritten, but add it in init to
        # make auto completion and type checking work better.
        self._parser_kwargs = self._get_parser_kwargs(add_help=_add_help)
        self._parser = self._parser_class(**self._parser_kwargs)

        # noinspection PyProtectedMember
        self._group_to_group_parser = {
        }  # type: Dict[Union[ArgumentGroup, MutuallyExclusiveGroup], argparse._ArgumentGroup]
        # noinspection PyProtectedMember
        self._subparser_action = None  # type: Optional[argparse._SubParsersAction]

    def _get_parser_kwargs(self, add_help):
        # type: (Optional[bool]) -> Dict[str, Any]

        if self._argument_default == SUPPRESS:
            raise SuppressError()

        class_ = type(self)
        # noinspection PyProtectedMember,PyCallByClass,PyTypeChecker
        parser_kwargs = class_._get_kwargs(class_)  # type: ignore # pylint: disable=protected-access

        if self._help is not None and add_help is _KEEP_DEFAULT:
            add_help = False
        if add_help is not _KEEP_DEFAULT:
            parser_kwargs["add_help"] = add_help

        allow_abbrev = self._allow_abbrev
        allow_abbrev_supported = sys.version_info.major >= 3 and sys.version_info.minor >= 5
        if not allow_abbrev_supported:
            allow_abbrev = _KEEP_DEFAULT
        if allow_abbrev is not _KEEP_DEFAULT:
            parser_kwargs["allow_abbrev"] = allow_abbrev

        parser_kwargs["parents"] = list(self._get_parent_argument_parsers())

        return parser_kwargs

    def _get_parent_argument_parsers(self):
        # type: () -> Iterable[ClassParser]

        # We never call super __init__, this choice escapes the MRO which is usually not a good
        # idea, but in our case the MRO will not function for the most simple (and probably common)
        # usage of parents that we try to emulate.
        # If we have a class with two parents that provide arguments, depending on when we call
        # super (at the start or at the end) Arguments order will happen:
        # 1) The first arguments will come from the child class and then from the parents left to
        # right
        # 2) The first arguments will come from the parents right to left and and then from the
        # child class
        # While the behaviour in the argparse library is parent left to right first and then the
        # child arguments
        for base in self.__class__.__bases__:
            if issubclass(base, ClassParser):
                parent_class_parser = base(  # pylint: disable=unexpected-keyword-arg
                    _add_help=False, _namespace=self._namespace)
                # noinspection PyProtectedMember
                parent_class_parser._fill_parser()  # pylint: disable=protected-access,no-member

                # noinspection PyProtectedMember
                yield parent_class_parser._parser  # pylint: disable=protected-access,no-member

    def _fill_parser(self):
        # type: () -> None

        self._fill_parser_defaults()

        self._fill_parser_regular_arguments()

        self._fill_parser_special_arguments()

    def _fill_parser_defaults(self):
        # type: () -> None

        # noinspection PyProtectedMember,PyUnresolvedReferences
        for action in self._parser._actions:  # pylint: disable=protected-access
            if action.dest is not SUPPRESS and action.default is not SUPPRESS:
                if action.dest not in dir(self._namespace):
                    # I think if that happens we have a bug
                    raise NoArgumentInParser(  # type: ignore
                        class_parser=self._namespace, dest=action.dest)
                setattr(self._namespace, action.dest, action.default)

        # noinspection PyProtectedMember,PyUnresolvedReferences
        for dest, value in self._parser._defaults.items():  # pylint: disable=protected-access
            if dest not in dir(self._namespace):
                # I think if that happens we have a bug
                raise NoArgumentInParser(  # type: ignore
                    class_parser=self._namespace, dest=dest)
            setattr(self._namespace, dest, value)

    def _fill_parser_regular_arguments(self):
        # type: () -> None

        sorted_arguments = getattr(self, "_sorted_arguments")  # type: List[Tuple[str, _BaseArg]]  # pylint: disable=no-member
        subparser_names = {n for n, a in sorted_arguments if isinstance(a, ClassParser)}
        subparser_mappers = list(
            (n, a) for n, a in sorted_arguments if isinstance(a, SubParserMapper)
        )

        for argument_name, argument in sorted_arguments:

            if isinstance(argument, Arg):
                self._add_argument(argument=argument, argument_name=argument_name)

            elif isinstance(argument, Args):
                self._add_sub_arguments(
                    args=argument, args_name=argument_name)

            elif isinstance(argument, ClassParser):
                self._add_subparser(
                    subparser=argument,
                    subparser_name=argument_name,
                    subparser_mappers=subparser_mappers
                )

            elif isinstance(argument, SubParserMapper):
                self._validate_subparser_mapper(
                    subparser_mapper=argument, subparser_names=subparser_names)
                for name in _viewkeys(argument.map):
                    if name not in subparser_names:
                        raise NoSubParserForKeyInMapper(subparser_name=name)
                # noinspection PyProtectedMember
                if argument._must_set_all_parsers:  # pylint: disable=protected-access
                    for name in subparser_names:
                        if name not in argument.map:
                            raise MissingSubParserKeyInMapper(subparser_name=name)
            else:
                raise UnsupportedArgumentType(argument=argument)

    def _fill_parser_special_arguments(self):
        # type: () -> None

        if self._help is not None:
            if isinstance(self._help, _string_types):
                help_argument = HelpArg(
                    *[a.format(p=self._parser.prefix_chars) for a in ("{p}{p}help", "{p}h")],
                    help=self._help)
            elif isinstance(self._help, Arg):
                help_argument = self._help
            else:
                raise UnsupportedHelpArgumentType(argument=self._help)

            self._add_argument(argument=help_argument, argument_name=_NOT_NAMED_ARGUMENT)

        if self._version is not None:
            if isinstance(self._version, _string_types):
                version_argument = VersionArg(
                    *[a.format(p=self._parser.prefix_chars) for a in ("{p}{p}version", "{p}v")],
                    version=self._version)
            elif isinstance(self._version, Arg):
                version_argument = self._version
            else:
                raise UnsupportedVersionArgumentType(argument=self._version)

            self._add_argument(argument=version_argument, argument_name=_NOT_NAMED_ARGUMENT)

    def _add_argument(self, argument, argument_name):
        # type: (Arg, Union[str, object]) -> None

        # noinspection PyProtectedMember
        argument_kwargs = argument._get_kwargs()  # pylint: disable=protected-access

        if argument_name is not _NOT_NAMED_ARGUMENT:
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
        action = add_argument_function(*argument.flags, **argument_kwargs)  # type: ignore
        # noinspection PyTypeChecker
        _action_call_patch(action=action, class_parser=self._namespace)  # type: ignore

    def _add_sub_arguments(self, args, args_name):
        # type: (Args, str) -> None

        for sub_argument in args.args:
            if not isinstance(sub_argument, Arg):
                raise UnsupportedArgumentTypeInArgs(argument=sub_argument)
            # We use the group logic inside _add_argument to make sure the mutually
            # exclusiveness works
            if isinstance(args, MutuallyExclusiveGroup):
                sub_argument.group = args
            self._add_argument(argument=sub_argument, argument_name=args_name)
        self.set_defaults(**{args_name: args.args_default})  # type: ignore

    def _add_subparser(self, subparser, subparser_name, subparser_mappers):
        # type: (ClassParser, str, List[Tuple[str, SubParserMapper]]) -> None

        if self._subparser_action is None:
            self._add_subparser_action(subparser_mappers=subparser_mappers)

        # noinspection PyProtectedMember
        add_parser_kwargs = dict(subparser._parser_kwargs)  # pylint: disable=protected-access
        # noinspection PyProtectedMember
        add_parser_kwargs.update(subparser._get_kwargs())  # pylint: disable=protected-access

        subparser._parser = self._subparser_action.add_parser(  # type: ignore # pylint: disable=protected-access
            name=subparser_name, **add_parser_kwargs)

        alias_to_name = getattr(self._subparser_action, "__alias_to_name")  # type: Dict[str, str]
        name_to_namespace = getattr(
            self._subparser_action, "__name_to_namespace")  # type: Dict[str, ClassParser]
        name_to_namespace[subparser_name] = subparser
        alias_to_name[subparser_name] = subparser_name
        for alias in add_parser_kwargs.get("aliases", []):
            alias_to_name[alias] = subparser_name

        # noinspection PyProtectedMember
        subparser._fill_parser()  # pylint: disable=protected-access

    def _add_subparser_action(self, subparser_mappers):
        # type: (List[Tuple[str, SubParserMapper]]) -> None

        if self._subparser_config is None:
            subparser_config = SubParserConfig()
        elif isinstance(self._subparser_config, SubParserConfig):
            subparser_config = self._subparser_config
        else:
            raise UnsupportedSubParserConfigType(subparser_config=self._subparser_config)
        # noinspection PyProtectedMember
        subparser_config_kwargs = subparser_config._get_kwargs()  # pylint: disable=protected-access
        self._subparser_action = self._parser.add_subparsers(**subparser_config_kwargs)

        setattr(self._subparser_action, "__alias_to_name", {})
        setattr(self._subparser_action, "__name_to_namespace", {})

        _subparser_action_call_patch(  # type: ignore
            action=self._subparser_action,
            class_parser=self._namespace,
            subparser_mappers=subparser_mappers
        )

    @staticmethod
    def _validate_subparser_mapper(subparser_mapper, subparser_names):
        # type: (SubParserMapper, Set[str]) -> None

        for name in _viewkeys(subparser_mapper.map):
            if name not in subparser_names:
                raise NoSubParserForKeyInMapper(subparser_name=name)
        # noinspection PyProtectedMember
        if subparser_mapper._must_set_all_parsers:  # pylint: disable=protected-access
            for name in subparser_names:
                if name not in subparser_mapper.map:
                    raise MissingSubParserKeyInMapper(subparser_name=name)

    def set_default(self, name, value):
        # type: (str, Any) -> None
        """
        Most of the time, the attributes of the object returned by parse_args() will be fully
        determined by inspecting the command-line arguments and the argument actions.
        set_defaults() allows some additional attributes that are determined without any inspection
        of the command line to be added.

        Note that parser-level defaults always override argument-level defaults.
        """

        if name not in dir(self):
            raise ArgumentForDefaultValueDoesntExist(class_parser=self, attribute_name=name)

        self._parser.set_defaults(**{name: value})

    def set_defaults(self, **kwargs):
        # type: (Dict[str, Any]) -> None
        """
        Most of the time, the attributes of the object returned by parse_args() will be fully
        determined by inspecting the command-line arguments and the argument actions.
        set_defaults() allows some additional attributes that are determined without any inspection
        of the command line to be added.

        Note that parser-level defaults always override argument-level defaults.
        """

        for name, value in _viewitems(kwargs):
            self.set_default(name=name, value=value)

    def get_default(self, name):
        # type: (str) -> Any
        """
        Get the default value for an attribute, as set by either adding an Arg or by using
        set_default or set_defaults.
        """
        return self._parser.get_default(dest=name)

    def parse_args(self, args=None):
        # type: (Optional[List[str]]) -> ClassParser
        """
        Convert argument strings to objects and assign them as attributes of the ClassParser.
        Return the ClassParser.
        Arg objects set in the ClassParser subclass determine exactly what objects are parsed.
        See the documentation for Arg for details.

        :param args: List of strings to parse. The default is taken from sys.argv.
        """

        self._fill_parser()
        self._parser.parse_args(args=args)
        return self

    def parse_known_args(self, args=None):
        # type: (Optional[List[str]]) -> Tuple[ClassParser, List[str]]
        """
        Sometimes a script may only parse a few of the command-line arguments,
        passing the remaining arguments on to another script or program.
        In these cases, the parse_known_args() method can be useful.
        It works much like parse_args() except that it does not produce an error
        when extra arguments are present.
        Instead, it returns a two item tuple containing the parsed ClassParser
        and the list of remaining argument strings.
        """

        self._fill_parser()
        _, remainder = self._parser.parse_known_args(args=args)
        return self, remainder

    def format_usage(self):
        # type: () -> str
        """
        Return a string containing a brief description of how the ClassParser should be
        invoked on the command line.
        """
        return self._parser.format_usage()

    def format_help(self):
        # type: () -> str
        """
        Return a string containing a help message, including the program usage and information
        about the arguments registered with the ClassParser.
        """
        return self._parser.format_help()

    # noinspection PyShadowingBuiltins
    def print_usage(self, file=None):  # pylint: disable=redefined-builtin
        # type: (Optional[Any]) -> None
        """
        Print a brief description of how the ClassParser should be invoked on the command line.
        If file is None, sys.stdout is assumed.
        """
        return self._parser.print_usage(file=file)

    # noinspection PyShadowingBuiltins
    def print_help(self, file=None):  # pylint: disable=redefined-builtin
        # type: (Optional[Any]) -> None
        """
        Print a help message, including the program usage and information about the arguments
        registered with the ClassParser. If file is None, sys.stdout is assumed.
        """
        return self._parser.print_help(file=file)

    def exit_(self, status=0, message=None):
        # type: (int, Optional[str]) -> None
        """
        This method terminates the program, exiting with the specified status and, if given,
        it prints a message before that.
        """
        self._parser.exit(status=status, message=message)

    def error_(self, message=None):
        # type: (Optional[str]) -> None
        """
        This method prints a usage message including the message to the standard error and
        terminates the program with a status code of 2.
        """
        self._parser.error(message=message)  # type: ignore
