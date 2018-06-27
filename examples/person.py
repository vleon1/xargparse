from enum import Enum, auto, unique
from typing import List

from xargparse import Arg, ParserHolder, ActionName, ArgumentGroup, MutuallyExclusiveGroup, Args, SubParserMapper


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
@unique
class Color(Enum):

    red = auto()
    green = auto()
    blue = auto()
    brown = auto()

    def __str__(self):
        return self.name


questions = ArgumentGroup(title="questions", description="Questions about you")
apples_group = MutuallyExclusiveGroup(required=False)


# noinspection PyCompatibility
class PersonInfo(ParserHolder):

    name: str = Arg(help="Your name")
    family: str = Arg(help="Your family name")
    age: int = Arg(help="Your age", type=int)
    # noinspection PyTypeChecker
    gender: Gender = Arg(type=Gender.__getitem__, choices=Gender,
                         help="The closest thing to your Gender")
    is_human: bool = Arg("--not-human", "--alien", "-a", action=ActionName.store_false, group=questions,
                         help="Tell us if you are an alien!")
    is_zombie: bool = Arg("--zombie", action=ActionName.store_true, group=questions,
                          help="Tell us if you are a zombie!")
    is_sane: bool = MutuallyExclusiveGroup(required=False, args=[
        Arg("--insane", action=ActionName.store_false, help="You are insane!"),
        Arg("--sane", action=ActionName.store_true, help="You are sane!"),
    ], args_default=True)


# noinspection PyCompatibility
class PropertyInfo(ParserHolder):

    street: str = Arg(help="Where do you live")

    has_cats: bool = Arg("--no-cats", default=True, action=ActionName.store_const, const=False,
                         group=questions,
                         help="Tell us if you have no cats")
    cat_names: str = Arg("--cat-name", action=ActionName.append, help="Add the name of one of your cats")

    coin_tosses: int = Arg("--toss", default=0, action=ActionName.count, help="Toss a coin")

    one_apple: bool = Arg("--one-apple", action=ActionName.store_true, group=apples_group)
    two_apples: bool = Arg("--two-apples", action=ActionName.store_true, group=apples_group)

    colors: List[Color] = Args(args=[
        Arg("--red", action=ActionName.append_const, const=Color.red),
        Arg("--green", action=ActionName.append_const, const=Color.green),
        Arg("--blue", action=ActionName.append_const, const=Color.blue),
        Arg("--brown", action=ActionName.append_const, const=Color.brown),
    ], args_default=[])


# noinspection PyCompatibility
class SubCommand1(ParserHolder):

    bla: str = Arg(help="bla??")


# noinspection PyCompatibility
class SubCommand2(ParserHolder):

    yada: str = Arg(help="bla??")


# noinspection PyCompatibility
class Person(PersonInfo, PropertyInfo):

    _description = "Person Class Example Program"

    sub1 = SubCommand1(aliases=["sub"])
    sub2 = SubCommand2()

    parser_name: str = SubParserMapper(sub1="sub1", sub2="sub2")

    bio = "No bio"

    _version = "v1.0.0.0"
    _help = "Super help message!!!"


if __name__ == "__main__":

    args = Person()

    try:
        print(args.has_cats)
    except AttributeError:
        pass

    try:
        args.set_default("bio1", "He was born in 2088")
    except AttributeError:
        pass

    args.set_default("bio", "He was born in 1988")

    print(args.get_default("bio1"))
    print(args.get_default("bio"))

    args.parse_args(["leon", "vaiman", "29", "male", "gorodisky",
                     "--no-cats", "--one-apple", "--one-apple", "--green", "--green", "--blue",
                     "sub2", "2"])
    print(args.has_cats)
    print(args)
    print(args.parser_name)
