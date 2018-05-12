from enum import Enum, auto, unique

from xargparse import XArg, XNamespace, XAction, XHelpArg


# noinspection PyCompatibility
@unique
class Gender(Enum):

    male = auto()
    female = auto()
    both = auto()
    neither = auto()
    other = auto()

    def __str__(self):
        return self.name


# noinspection PyCompatibility
class Arguments(XNamespace):

    _version = "v1.0.0.0"
    _help = "Super help message!!!"

    name: str = XArg(help="Your name")
    family: str = XArg(help="Your family name")
    age: int = XArg(help="Your age", type=int)
    gender: Gender = XArg(type=Gender.__getitem__, choices=Gender,
                          help="The closest thing to your Gender")
    is_human: bool = XArg("--not-human", "--alien", "-a", action=XAction.store_false,
                          help="Tell us if you are an alien!")
    is_zombie: bool = XArg("--zombie", action=XAction.store_true, help="Tell us if you are a zombie!")
    has_cats: bool = XArg("--no-cats", default=True, action=XAction.store_const, const=False,
                          help="Tell us if you have no cats")
    cat_names: str = XArg("--cat-name", action=XAction.append, help="Add the name of one of your cats")

    coin_tosses: int = XArg("--toss", default=0, action=XAction.count, help="Toss a coin")


if __name__ == "__main__":

    args = Arguments().parse_args()

    print(args)
