"""
Class based extension to argparse: https://docs.python.org/3/library/argparse.html
"""
import argparse


# todo:
# Sane defaults for append, nargs (*) and count
# nargs
# append_const
# sub command
# argument groups
# mutually exclusive groups
# pass the argument parser class to our Namespace class
# help argument
# version argument
# allow_abbrev option in Action on python 2 and 3
# tests
# rename to something better
# expose the formatter classes RawDescriptionHelpFormatter RawTextHelpFormatter ArgumentDefaultsHelpFormatter
#                              MetavarTypeHelpFormatter
# expose the Action class as well
# handle argparse.SUPPRESS in defaults and _argument_default
# Make sure that we work with multi inheritance in a sane way
# verbose nargs names (like we did with the Action class) and/or handle argparse.REMAINDER
# add documentation about not supporting set_defaults and get_defaults (makes no sense)
# should we support the printing and exiting methods? print_usage print_help format_usage format_help exit error
# partial parsing
# docstring
# readme
# pypi


_keep_default = object()


def _get_none_default_kwargs(containing_object, key_names, key_prefix=""):

    all_kwarg_pairs = ((k, getattr(containing_object, key_prefix + k)) for k in key_names)
    return {k: v for k, v in all_kwarg_pairs if v is not _keep_default}


class Action(object):
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

    # We do not support those since they won't work well with the intention of the library, but i think a similar
    # functionality can be attained using class inheritance
    parsers = "parsers"


class Arg(object):

    __index_counter = 0

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
    ):

        if action == Action.parsers:
            raise ValueError(
                "Action %s is not supported, you can try to achieve what you want with inheritance" % action)

        # No need to protect from racing access, since in a case of a "race" it will happen with two different classes
        # and so both will raise the counter and will have the same index value, but internally the class arguments will
        # still have sorted different indexes..
        Arg.__index_counter += 1
        self.index = Arg.__index_counter

        self.flags = flags
        self.action = action
        self.nargs = nargs
        self.const = const
        self.default = default
        self.type = type
        self.choices = choices
        self.required = required
        self.help = help
        self.metavar = metavar


class Namespace(object):

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

    __argument_parser_kwarg_names = (
        "prog", "usage", "description", "epilog", "parents", "formatter_class", "prefix_chars",
        "fromfile_prefix_chars", "argument_default", "conflict_handler", "add_help"
    )

    __argument_kwarg_names = (
        "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar",
    )

    def __init__(self, args=None):

        parser_kwargs = _get_none_default_kwargs(self, self.__argument_parser_kwarg_names, key_prefix="_")
        parser = argparse.ArgumentParser(**parser_kwargs)

        argument_variables_unfiltered = ((k, getattr(self, k)) for k in dir(self))
        argument_variables_unsorted = ((k, v) for k, v in argument_variables_unfiltered if isinstance(v, Arg))
        argument_variables = sorted(argument_variables_unsorted, key=lambda kv: kv[1].index)
        self.__argument_names = [k for k, v in argument_variables]

        for argument_name, argument in argument_variables:

            argument_kwargs = _get_none_default_kwargs(argument, self.__argument_kwarg_names)
            argument_kwargs["dest"] = argument_name

            # # Doing default None on append is horrible
            # if argument.action == Action.append and "default" not in argument_kwargs:
            #     argument_kwargs["default"] = []

            parser.add_argument(*argument.flags, **argument_kwargs)

        parsed_dict = vars(parser.parse_args(args=args))
        self.__dict__.update(** parsed_dict)

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, {n: getattr(self, n) for n in self.__argument_names})
