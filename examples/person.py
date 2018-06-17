from enum import Enum, auto, unique

from xargparse import Arg, ParserHolder, ActionName, ArgumentGroup, MutuallyExclusiveGroup


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


questions = ArgumentGroup(title="questions", description="Questions about you")
apples_group = MutuallyExclusiveGroup(required=False)


# noinspection PyCompatibility
class PersonInfo(ParserHolder):

    name: str = Arg(help="Your name")
    family: str = Arg(help="Your family name")
    age: int = Arg(help="Your age", type=int)
    gender: Gender = Arg(type=Gender.__getitem__, choices=Gender,
                         help="The closest thing to your Gender")
    is_human: bool = Arg("--not-human", "--alien", "-a", action=ActionName.store_false, group=questions,
                         help="Tell us if you are an alien!")
    is_zombie: bool = Arg("--zombie", action=ActionName.store_true, group=questions,
                          help="Tell us if you are a zombie!")
    is_sane: bool = MutuallyExclusiveGroup(required=False, arguments=[
        Arg("--insane", action=ActionName.store_false, help="You are insane!"),
        Arg("--sane", action=ActionName.store_true, help="You are sane!"),
    ], arguments_default=True)


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


# noinspection PyCompatibility
class SubCommand1(ParserHolder):

    bla: str = Arg(help="bla??")


# noinspection PyCompatibility
class SubCommand2(ParserHolder):

    yada: str = Arg(help="bla??")


# noinspection PyCompatibility
class Person(PersonInfo, PropertyInfo):

    _description = "Person Class"

    sub1 = SubCommand1()
    sub2 = SubCommand2()

    _version = "v1.0.0.0"
    _help = "Super help message!!!"


if __name__ == "__main__":

    args = Person()
    try:
        print(args.has_cats)
    except AttributeError:
        pass
    args.parse_args(["leon", "vaiman", "29", "male", "gorodisky", "--no-cats", "--one-apple", "sub1", "1"])
    print(args.has_cats)
    print(args)
