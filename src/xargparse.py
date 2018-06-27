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
    from typing import Dict, Any, List, Optional, Union, Callable, Iterable, Tuple


# todo:

# Names:
# * change namespace, parser-holder and parser class-parser (ClassParser)
# * add_argument to Arg
# * argparse to xargparse
# * think about names

# Other:
# * named calls

# changes list:
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

# Docs focus:
# * single file code

# tests:
# * Inherit twice from two classes with different orders, output strings should differ
# * Make sure we see Set and see Description

# Final stuff:
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
    # type: (argparse._SubParsersAction, ParserHolder, List[Tuple[str, SubParserMapper]]) -> None
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

    """
    This just stores the argument’s value. This is the default action.
    """
    store = "store"

    """
    This stores the value specified by the const keyword argument. 
    The 'store_const' action is most commonly used with optional arguments that specify some sort of flag.
    """
    store_const = "store_const"

    """
    A special cases of 'store_const' used for storing the value True. 
    In addition, it creates a default value of False.
    """
    store_true = "store_true"

    """
    A special cases of 'store_const' used for storing the value False. 
    In addition, it creates a default value of True.
    """
    store_false = "store_false"

    """
    This stores a list, and appends each argument value to the list. 
    This is useful to allow an option to be specified multiple times.
    """
    append = "append"

    """
    This stores a list, and appends the value specified by the const keyword argument to the list.
    (Note that the const keyword argument defaults to None.)
    The 'append_const' action is typically useful when multiple arguments need to store constants to the same list
    using an Args object.
    """
    append_const = "append_const"

    """
    This counts the number of times a keyword argument occurs. 
    For example, this is useful for increasing verbosity levels.
    """
    count = "count"

    """
    This prints a complete help message for all the options in the current parser and then exits.
    By default a help action is automatically added to the parser. 
    See ParserHolder for details of how the output is created.
    """
    help = "help"

    """
    This expects a version= keyword argument in the add_argument() call,
    and prints version information and exits when invoked.
    """
    version = "version"


class ConflictHandlerName(object):
    """ Use this when setting _conflict_handler in the ParserHolder instead of relying on strings """

    error = "error"
    resolve = "resolve"


class NArgName(object):
    """
    Use this instead of the strings '?', '+' etc.. for nargs, you can also directly use the globals in argparse
    """

    """
    One argument will be consumed from the command line if possible, and produced as a single item. 
    If no command-line argument is present, the value from default will be produced. 
    Note that for optional arguments, there is an additional case - 
    the option string is present but not followed by a command-line argument. 
    In this case the value from const will be produced.
    One of the more common uses of nargs=optional is to allow optional input and output files.
    """
    optional = argparse.OPTIONAL  # ?

    """
    All command-line arguments present are gathered into a list. 
    Note that it generally doesn’t make much sense to have more than one positional argument with 
    nargs=zero_or_more, but multiple optional arguments with nargs=zero_or_more is possible.
    """
    zero_or_more = argparse.ZERO_OR_MORE  # *

    """
    Just like zero_or_more, all command-line args present are gathered into a list. 
    Additionally, an error message will be generated if there wasn’t at least one 
    command-line argument present.
    """
    one_or_more = argparse.ONE_OR_MORE  # +

    """
    All the remaining command-line arguments are gathered into a list. 
    This is commonly useful for command line utilities that dispatch to other command line utilities.
    """
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
        # type: (...) -> None
        """
        :param flags: A flag or a list of flags for optional arguments (This will turn this argument into an optional one..)

        :param action: ParserHolder objects associate command-line arguments with actions.
        These actions can do just about anything with the command-line arguments associated with them,
        though most actions simply add an attribute to the object returned by parse_args().
        The action keyword argument specifies how the command-line arguments should be handled
        see ActionName class for a list of provided actions.

        You may also specify an arbitrary action by passing an Action subclass or other object
        that implements the same interface.
        The recommended way to do this is to extend Action, overriding the __call__ method
        and optionally the __init__ method.

        :param nargs: ArgumentParser objects usually associate a single command-line argument with a single action to be taken.
        The nargs keyword argument associates a different number of command-line arguments with a single action.
        The supported values are a number or the values in the NArgName class.

        When a number N is supplied. N arguments from the command line will be gathered together into a list
        Note that nargs=1 produces a list of one item. This is different from the default,
        in which the item is produced by itself.

        If the nargs keyword argument is not provided, the number of arguments consumed is determined by the action.
        Generally this means a single command-line argument will be consumed and a single item (not a list) will be produced.

        :param const: The const argument of add_argument() is used to hold constant values that are not read from the
        command line but are required for the various ArgumentParser actions. The two most common uses of it are:

        * When add_argument() is called with action=store_const or action=append_const.
        These actions add the const value to one of the attributes of the object returned
        by parse_args(). See the action description for examples.
        * When add_argument() is called with option strings (like -f or --foo) and nargs=optional.
        This creates an optional argument that can be followed by zero or one command-line arguments.
        When parsing the command line, if the option string is encountered with no command-line argument following it,
        the value of const will be assumed instead. See the nargs description for examples.

        With the store_const and append_const actions, the const keyword argument must be given.
        For other actions, it defaults to None.

        :param default: All optional arguments and some positional arguments may be omitted at the command line.
        The default keyword argument of add_argument(), whose value defaults to None,
        specifies what value should be used if the command-line argument is not present.
        For optional arguments, the default value is used when the option string was not present at the command line.

        If the default value is a string, the parser parses the value as if it were a command-line argument.
        In particular, the parser applies any type conversion argument, if provided,
        before setting the attribute on the ParserHolder return value. Otherwise, the parser uses the value as is.

        For positional arguments with nargs equal to optional or zero_or_more, the default value is used when
        no command-line argument was present.

        :param type: By default, ArgumentParser objects read command-line arguments in as simple strings.
        However, quite often the command-line string should instead be interpreted as another type,
        like a float or int.
        The type keyword argument of add_argument() allows any necessary type-checking and type conversions to be performed.
        Common built-in types and functions can be used directly as the value of the type argument.

        See the section on the default keyword argument for information on when the type argument is applied to default arguments.

        To ease the use of various types of files, the argparse module provides the factory FileType which
        takes the mode=, bufsize=, encoding= and errors= arguments of the open() function.
        For example, FileType('w') can be used to create a writable file.

        type= can take any callable that takes a single string argument and returns the converted value.

        The choices keyword argument may be more convenient for type checkers that simply check against a range of values.
        See the choices section for more details.

        :param choices: Some command-line arguments should be selected from a restricted set of values.
        These can be handled by passing a container object as the choices keyword argument to Arg.
        When the command line is parsed, argument values will be checked,
        and an error message will be displayed if the argument was not one of the acceptable values.

        Note that inclusion in the choices container is checked after any type conversions have been performed,
        so the type of the objects in the choices container should match the type specified.

        ny object that supports the in operator can be passed as the choices value, so dict objects,
        set objects, custom containers, etc. are all supported.

        :param required: In general, the argparse module assumes that flags like -f and --bar indicate optional arguments,
        which can always be omitted at the command line. To make an option required,
        True can be specified for the required= keyword argument to Arg

        Note: Required options are generally considered bad form because users expect options to be optional,
        and thus they should be avoided when possible.

        :param help: The help value is a string containing a brief description of the argument.
        When a user requests help (usually by using -h or --help at the command line),
        these help descriptions will be displayed with each argument.

        The help strings can include various format specifiers to avoid repetition of things like the program name
        or the argument default.
        The available specifiers include the program name, %(prog)s and most keyword arguments
        to Arg, e.g. %(default)s, %(type)s, etc.

        As the help string supports %-formatting, if you want a literal % to appear in the help string,
        you must escape it as %%.

        xargparse supports silencing the help entry for certain options,
        by setting the help value to xargparse.SUPPRESS.

        :param metavar: When ParserHolder generates help messages, it needs some way to refer to each expected argument.
        By default, ParserHolder objects uses the name of the argument.

        An alternative name can be specified with metavar.

        Note that metavar only changes the displayed name.

        Different values of nargs may cause the metavar to be used multiple times.
        Providing a tuple to metavar specifies a different display for each of the arguments.

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
        # type: (...) -> None
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
        # type: (...) -> None
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
        # type: (bool, Optional[List[Arg]], Optional[Any]) -> None
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
        # type: (...) -> None
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
    Use this class to get a commandline argument, it is a parallel to argparse.ArgumentParser except that
    ArgumentParser is also used internally.

    You use this class by subclassing it, you replace the add_argument calls you would do with ArgumentParser
    with adding Arg objects to the sub-class (In the same order you would have called add_argument).
    """

    """
    The name of the program (default: sys.argv[0])
    """
    _prog = _keep_default

    """
    The string describing the program usage (default: generated from arguments added to parser)
    """
    _usage = _keep_default

    """
    Text to display before the argument help (default: none)
    """
    _description = _keep_default

    """
    Text to display after the argument help (default: none)
    """
    _epilog = _keep_default

    """
    A class for customizing the help output
    """
    _formatter_class = _keep_default

    """
    The set of characters that prefix optional arguments (default: ‘-‘)
    """
    _prefix_chars = _keep_default

    """
    The set of characters that prefix files from which additional arguments should be read (default: None)
    """
    _fromfile_prefix_chars = _keep_default

    """
    The global default value for arguments (default: None)
    """
    _argument_default = _keep_default

    """
    The strategy for resolving conflicting optionals (usually unnecessary)
    """
    _conflict_handler = _keep_default

    """
    Add a -h/--help option to the parser (default: True)
    """
    _add_help = _keep_default

    """
    Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)
    Supported only in python>=3.5 on other versions it is silently ignored
    """
    _allow_abbrev = _keep_default

    """
    Change the parser class
    """
    _parser_class = argparse.ArgumentParser

    """ 
    Overwrite to add a help argument manually
    Set it to a string to get a default HelpArg with the help parameter set to this string
    Set it to a HelpArg for more control
    You can also use Arg but that is less comfortable, more error prone and should not be necessary since HelpArg
    is built in a way that is supposed to let you achieve everything that is possible with this type of arguments
    
    Setting this and _add_help to anything that evaluates to True will probably create a conflict
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

    """ Used internally when the parser is used as a subparser """
    _kwarg_names = ("prog", "aliases", "help")
    _kwargs_name_prefix = "__"

    # noinspection PyShadowingBuiltins
    def __init__(
            self,
            prog=_keep_default,  # type: Optional[str]
            aliases=_keep_default,  # type: Optional[List[str]]
            help=_keep_default,  # type: Optional[str]
            _add_help=None,  # type: Optional[bool]
            _namespace=None  # type: Optional[ParserHolder]
    ):
        # type: (...) -> None
        """
        If you overwrite the __init__ method, DO NOT call super since that will break parents usage.

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

        if _add_help is None:
            _add_help = self._add_help

        if _namespace is None:
            _namespace = self
        self._namespace = _namespace

        # The parser is not exposed since the name might be used for an argument and since direct usage will most likely
        # break things.
        # But if there is a missing feature in this implementation, or a bug that is possible to overcome by directly
        # using _parser, then nothing stops you from doing so.
        # Do note that you most likely can achieve what you want by implementing it in a subclass, instead of accessing
        # the instance's "_parser" variable.
        #
        # Note that in subparser mode this parameter will be overwritten, but add it in init to make auto completion
        # and type checking work better.
        self._parser_kwargs = self._get_parser_kwargs(add_help=_add_help)
        self._parser = self._parser_class(**self._parser_kwargs)

        # noinspection PyProtectedMember
        self._group_to_group_parser = {}  # type: Dict[Union[ArgumentGroup, MutuallyExclusiveGroup], argparse._ArgumentGroup]
        # noinspection PyProtectedMember
        self._subparser_action = None  # type: Optional[argparse._SubParsersAction]

    def _get_parser_kwargs(self, add_help):
        # type: (Optional[bool]) -> Dict[str, Any]

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
        # type: () -> Iterable[ParserHolder]

        # We never call super __init__, this choice escapes the MRO which is usually not a good idea, but in our
        # case the MRO will not function for the most simple (and probably common) usage of parents that we try to
        # emulate.
        # If we have a class with two parents that provide arguments, depending on when we call super (at the start or
        # at the end) Arguments order will happen:
        # 1) The first arguments will come from the child class and then from the parents left to right
        # 2) The first arguments will come from the parents right to left and from the child class and then
        # While the behaviour in the argparse library is parent left to right first and then the child arguments
        for base in self.__class__.__bases__:
            if issubclass(base, ParserHolder):
                parent_holder = base(_add_help=False, _namespace=self._namespace)
                # noinspection PyProtectedMember
                parent_holder._fill_parser()

                # noinspection PyProtectedMember
                yield parent_holder._parser

    def _fill_parser(self):
        # type: () -> None

        self._fill_parser_defaults()

        self._fill_parser_regular_arguments()

        self._fill_parser_special_arguments()

    def _fill_parser_defaults(self):
        # type: () -> None

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

    def _fill_parser_regular_arguments(self):
        # type: () -> None

        sorted_arguments = self._sorted_arguments  # type: List[Tuple[str, _BaseArg]]
        subparser_names = {n for n, a in sorted_arguments if isinstance(a, ParserHolder)}
        subparser_mappers = list((n, a) for n, a in sorted_arguments if isinstance(a, SubParserMapper))

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
        # type: (ParserHolder, str, List[Tuple[str, SubParserMapper]]) -> None

        if self._subparser_action is None:
            self._add_subparser_action(subparser_mappers=subparser_mappers)

        # noinspection PyProtectedMember
        add_parser_kwargs = dict(argument._parser_kwargs)
        # noinspection PyProtectedMember
        add_parser_kwargs.update(argument._get_kwargs())

        argument._parser = self._subparser_action.add_parser(argument_name, **add_parser_kwargs)

        alias_to_name = getattr(self._subparser_action, "__alias_to_name")  # type: Dict[str, str]
        name_to_namespace = getattr(self._subparser_action, "__name_to_namespace")  # type: Dict[str, ParserHolder]
        name_to_namespace[argument_name] = argument
        alias_to_name[argument_name] = argument_name
        for alias in add_parser_kwargs.get("aliases", []):
            alias_to_name[alias] = argument_name

        # noinspection PyProtectedMember
        argument._fill_parser()

    def _add_subparser_action(self, subparser_mappers):
        # type: (List[Tuple[str, SubParserMapper]]) -> None

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

    def _add_argument(self, argument, argument_name):
        # type: (Arg, Union[str, _not_named_argument]) -> None

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
        # type: (str, Any) -> None
        """
        Most of the time, the attributes of the object returned by parse_args() will be fully determined
        by inspecting the command-line arguments and the argument actions.
        set_defaults() allows some additional attributes that are determined without any inspection of
        the command line to be added.

        Note that parser-level defaults always override argument-level defaults.
        """

        if name not in dir(self):
            raise ArgumentForDefaultValueDoesntExist(parser=self, attribute_name=name)

        self._parser.set_defaults(**{name: value})

    def set_defaults(self, **kwargs):
        # type: (Dict[str, Any]) -> None
        """
        Most of the time, the attributes of the object returned by parse_args() will be fully determined
        by inspecting the command-line arguments and the argument actions.
        set_defaults() allows some additional attributes that are determined without any inspection of
        the command line to be added.

        Note that parser-level defaults always override argument-level defaults.
        """

        for name, value in _viewitems(kwargs):
            self.set_default(name=name, value=value)

    def get_default(self, name):
        # type: (str) -> Any
        """
        Get the default value for an attribute, as set by either add_argument() or by adding through Arg.
        """
        return self._parser.get_default(dest=name)

    def parse_args(self, args=None):
        # type: (Optional[List[str]]) -> ParserHolder
        """
        Convert argument strings to objects and assign them as attributes of the Parser. Return the Parser.
        Args set in the Parser subclass determine exactly what objects are parsed.
        See the documentation for Arg for details.

        :param args: List of strings to parse. The default is taken from sys.argv.
        """

        self._fill_parser()
        self._parser.parse_args(args=args)
        return self

    def parse_known_args(self, args=None):
        # type: (Optional[List[str]]) -> Tuple[ParserHolder, List[str]]
        """
        Sometimes a script may only parse a few of the command-line arguments,
        passing the remaining arguments on to another script or program.
        In these cases, the parse_known_args() method can be useful.
        It works much like parse_args() except that it does not produce an error
        when extra arguments are present.
        Instead, it returns a two item tuple containing the populated namespace
        and the list of remaining argument strings.
        """

        self._fill_parser()
        _, remainder = self._parser.parse_known_args(args=args)
        return self, remainder

    def format_usage(self):
        # type: () -> str
        """
        Return a string containing a brief description of how the ArgumentParser should be
        invoked on the command line.
        """
        return self._parser.format_usage()

    def format_help(self):
        # type: () -> str
        """
        Return a string containing a help message, including the program usage and information
        about the arguments registered with the ArgumentParser.
        """
        return self._parser.format_help()

    def print_usage(self, file=None):
        # type: (Optional[file]) -> None
        """
        Print a brief description of how the ArgumentParser should be invoked on the command line.
        If file is None, sys.stdout is assumed.
        """
        return self._parser.print_usage(file=file)

    def print_help(self, file=None):
        # type: (Optional[file]) -> None
        """
        Print a help message, including the program usage and information about the arguments
        registered with the ArgumentParser. If file is None, sys.stdout is assumed.
        """
        return self._parser.print_help(file=file)

    def exit_(self, status=0, message=None):
        # type: (int, Optional[str]) -> None
        """
        This method terminates the program, exiting with the specified status and, if given,
        it prints a message before that.
        """
        return self._parser.exit(status=status, message=message)

    def error_(self, message=None):
        # type: (Optional[str]) -> None
        """
        This method prints a usage message including the message to the standard error and
        terminates the program with a status code of 2.
        """
        return self._parser.error(message=message)
