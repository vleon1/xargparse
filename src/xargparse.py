"""
Class based extension to argparse: https://docs.python.org/3/library/argparse.html
"""
import argparse

# Exposing all argparse here so that users don't have to import it as well.
import sys

# noinspection PyUnresolvedReferences
from argparse import *


# todo:
# help argument
# version argument

# append_const
# sub command
# parents
# argument groups
# mutually exclusive groups
# Make sure that we work with multi inheritance in a sane way

# docstring
# readme
# add documentation about not supporting set_defaults and get_defaults
# pypi
# tests


_keep_default = object()


def _get_none_default_kwargs(containing_object, key_names, key_prefix=""):

    all_kwarg_pairs = ((k, getattr(containing_object, key_prefix + k)) for k in key_names)
    return {k: v for k, v in all_kwarg_pairs if v is not _keep_default}


class SuppressError(ValueError):
    def __init__(self):
        super(SuppressError, self).__init__(
            "SUPPRESS is not supported for argument defaults since it makes no sense in class context"
        )


class XAction(object):
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


class _XargBase(object):

    _index_counter = 0

    def __init__(self):

        # No need to protect from racing access, since in a case of a "race" it will happen with two different classes
        # and so both will raise the counter and will have the same index value, but internally the class arguments will
        # still have sorted different indexes..
        _XargBase._index_counter += 1
        self.__instance_index__ = XArg._index_counter


USE_SANE_DEFAULTS = True


class XArg(_XargBase):

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
            allow_abbrev=_keep_default,
    ):

        if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 5):
            allow_abbrev = _keep_default

        super(XArg, self).__init__()

        self.flags = flags
        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices = choices
        self.required = required
        self.help = help
        self.metavar = metavar
        self.allow_abbrev = allow_abbrev

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

            if self.action == XAction.append or self.nargs == "*" or self.nargs == "+" or self.nargs == REMAINDER:
                self.default = []

            if self.action == XAction.count:
                self.default = 0


class XNamespace(_XargBase):

    _description = _keep_default

    # All these have sane auto values
    _prog = _keep_default
    _usage = _keep_default
    _epilog = _keep_default
    _parents = _keep_default
    _formatter_class = _keep_default
    _prefix_chars = _keep_default
    _fromfile_prefix_chars = _keep_default
    _argument_default = _keep_default
    _conflict_handler = _keep_default
    _add_help = _keep_default

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
        "prog", "usage", "description", "epilog", "parents", "formatter_class", "prefix_chars",
        "fromfile_prefix_chars", "argument_default", "conflict_handler", "add_help"
    )

    __argument_kwarg_names = (
        "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar", "allow_abbrev"
    )

    def __init__(self):

        if self._argument_default == SUPPRESS:
            raise SuppressError()

        super(XNamespace, self).__init__()

        parser_kwargs = _get_none_default_kwargs(self, self.__argument_parser_kwarg_names, key_prefix="_")
        self._parser = self._parser_class(**parser_kwargs)

        argument_variables_unfiltered = ((k, getattr(self, k)) for k in dir(self))
        argument_variables_unsorted = ((k, v) for k, v in argument_variables_unfiltered if isinstance(v, _XargBase))
        argument_variables = sorted(argument_variables_unsorted, key=lambda kv: kv[1].index)
        self.__argument_names = [k for k, v in argument_variables]

        for argument_name, argument in argument_variables:

            if isinstance(argument, XArg):

                if self._use_sane_defaults:
                    argument.make_default_argument_sane()

                argument_kwargs = _get_none_default_kwargs(argument, self.__argument_kwarg_names)
                argument_kwargs["dest"] = argument_name

                self.parser.add_argument(*argument.flags, **argument_kwargs)

        if self._help is not None:
            argument_kwargs = _get_none_default_kwargs(self._help, self.__argument_kwarg_names)
            argument_kwargs["dest"] = SUPPRESS

            self.parser.add_argument(**argument_kwargs)

        if self._version is not None:
            argument_kwargs = _get_none_default_kwargs(self._version, self.__argument_kwarg_names)
            argument_kwargs["dest"] = SUPPRESS

            self.parser.add_argument(**argument_kwargs)

    @property
    def parser(self):
        """
        Exposes the inner parser object

        Dangerous: Can easily break stuff, only use it if what you want to do can't be achieved otherwise
        and you understand both the relevant code in xargparse and argparse.
        """
        return self._parser

    def set_defaults(self, **kwargs):
        raise AttributeError("This method is not supported as it goes against the philosophy of the library")

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
