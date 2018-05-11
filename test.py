from enum import Enum, auto, unique

from argparse3 import Arg, Namespace, Action


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
class Arguments(Namespace):

    name: str = Arg(help="Your name")
    family: str = Arg(help="Your family name")
    age: int = Arg(help="Your age", type=int)
    gender: Gender = Arg(type=Gender.__getitem__, choices=Gender,
                         help="The closest thing to your Gender")
    is_human: bool = Arg("--not-human", "--alien", "-a", action=Action.store_false, help="Tell us if you are an alien!")
    is_zombie: bool = Arg("--zombie", action=Action.store_true, help="Tell us if you are a zombie!")
    has_cats: bool = Arg("--no-cats", default=True, action=Action.store_const, const=False,
                         help="Tell us if you have no cats")
    cat_names: str = Arg("--cat-name", action=Action.append, help="Add the name of one of your cats")

    coin_tosses: int = Arg("--toss", default=0, action=Action.count, help="Toss a coin")


if __name__ == "__main__":

    args = Arguments()

    print(args)
