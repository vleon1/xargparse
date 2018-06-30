from xargparse import *


class Arguments(ClassParser):

    _description = 'Process some integers.'

    integers = Arg(metavar='N', type=int, nargs=NArgName.one_or_more,
                   help='an integer for the accumulator')

    accumulate = Arg('--sum', action=ActionName.store_const, const=sum, default=max,
                     help='sum the integers (default: find the max)')


args = Arguments().parse_args()
print(args)
