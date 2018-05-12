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


_keep_default = object()


def _get_none_default_kwargs(containing_object, key_names, key_prefix=""):

    all_kwarg_pairs = ((k, getattr(containing_object, key_prefix + k)) for k in key_names)
    return {k: v for k, v in all_kwarg_pairs if v is not _keep_default}


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
        self.__instance_index__ = Arg._index_counter


USE_SANE_DEFAULTS = True


class Arg(_Sortable):

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
        self.default = default  # Keep at the end since the setter does sensitization that depends on the other values

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

    def make_default_argument_sane(self):

        if self.default is _keep_default:

            if self.action == ActionName.append or self.nargs == "*" or self.nargs == "+" or self.nargs == REMAINDER:
                self.default = []

            if self.action == ActionName.count:
                self.default = 0


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


class ParserHolder(_Sortable):

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

    """ Overwrite to add a help argument manually """
    _help = None

    """ Overwrite to add a version argument manually """
    _version = None

    """
    When default is not set the argparse would use None instead of [] or 0 in places where these value are far more
    logical (a.k.a sane) if this is set to True we overwrite this insane behaviour..
    """
    _use_sane_defaults = USE_SANE_DEFAULTS

    __argument_parser_kwarg_names = (
        "prog", "usage", "description", "epilog", "formatter_class", "prefix_chars", "fromfile_prefix_chars",
        "argument_default", "conflict_handler", "add_help", "allow_abbrev"
    )

    __argument_kwarg_names = (
        "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar", "version"
    )

    def __init__(self):

        if self._argument_default == SUPPRESS:
            raise SuppressError()

        if self._help is not None and self._add_help is _keep_default:
            self._add_help = False

        super(ParserHolder, self).__init__()

        if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 5):
            self._allow_abbrev = _keep_default

        parser_kwargs = _get_none_default_kwargs(self, self.__argument_parser_kwarg_names, key_prefix="_")
        self._parser = self._parser_class(**parser_kwargs)

        argument_variables_unfiltered = ((k, getattr(self, k)) for k in dir(self))
        argument_variables_unsorted = (
            (k, v) for k, v in argument_variables_unfiltered if isinstance(v, _Sortable) and not k.startswith("_"))
        argument_variables = sorted(argument_variables_unsorted, key=lambda kv: kv[1].__instance_index__)
        self.__argument_names = [k for k, v in argument_variables]

        group_to_group_parser = {}

        for argument_name, argument in argument_variables:

            if isinstance(argument, Arg):

                if self._use_sane_defaults:
                    argument.make_default_argument_sane()

                argument_kwargs = _get_none_default_kwargs(argument, self.__argument_kwarg_names)
                argument_kwargs["dest"] = argument_name

                if argument.group is None:
                    add_argument_function = self.parser.add_argument
                else:
                    if argument.group not in group_to_group_parser:
                        group_to_group_parser[argument.group] = self.parser.add_argument_group(
                            title=argument.group.title, description=argument.group.description)
                    add_argument_function = group_to_group_parser[argument.group].add_argument

                add_argument_function(*argument.flags, **argument_kwargs)

        if self._help is not None:
            if isinstance(self._help, six.string_types):
                self._help = HelpArg(
                    *[a.format(p=self.parser.prefix_chars) for a in ("{p}{p}help", "{p}h")],
                    help=self._help)

            argument_kwargs = _get_none_default_kwargs(self._help, self.__argument_kwarg_names)
            argument_kwargs["dest"] = SUPPRESS

            self.parser.add_argument(*self._help.flags, **argument_kwargs)

        if self._version is not None:
            if isinstance(self._version, six.string_types):
                self._version = VersionArg(
                    *[a.format(p=self.parser.prefix_chars) for a in ("{p}{p}version", "{p}v")],
                    version=self._version)

            argument_kwargs = _get_none_default_kwargs(self._version, self.__argument_kwarg_names)
            argument_kwargs["dest"] = SUPPRESS

            self.parser.add_argument(*self._version.flags, **argument_kwargs)

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
