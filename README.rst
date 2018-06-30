Class based extension to argparse


# todo:

# Final stuff:
# * docs
# * tests
# * readme
# * pypi

# Docs position:
# * parents

# Docs changes list:
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
# * no convert_arg_line_to_args to overwrite, provide a _parser_class with the overwritten method instead..

# Docs focus:
# * single file code

# Docs faq:
# * Name choice and why not classparse

# Addon Tests:
# * Inherit twice from two classes with different orders, output strings should differ
# * Make sure we see Set and see Description
# * Defaults when unset should work
# * Subparser with unset optional arg
