from typing import Annotated, Dict, Optional

from attrs import define, field

from cyclopts import Parameter


@define
class Outfit:
    body: str
    head: str


@define
class User:
    id: int
    name: str = "John Doe"
    tastes: Dict[str, int] = field(factory=dict)
    outfit: Optional[Outfit] = None


def test_bind_attrs(app, assert_parse_args):
    @app.command
    def foo(user: User):
        pass

    assert_parse_args(
        foo,
        "foo --user.id=123 --user.tastes.wine=9 --user.tastes.cheese=7 --user.tastes.cabbage=1 --user.outfit.body=t-shirt --user.outfit.head=baseball-cap",
        User(id=123, tastes={"wine": 9, "cheese": 7, "cabbage": 1}, outfit=Outfit(body="t-shirt", head="baseball-cap")),
    )


def test_bind_attrs_accepts_keys_false(app, assert_parse_args):
    @define
    class SimpleClass:
        value: int

    @app.command
    def foo(example: Annotated[SimpleClass, Parameter(accepts_keys=False)]):
        pass

    assert_parse_args(foo, "foo 5", SimpleClass(5))
    assert_parse_args(foo, "foo --example=5", SimpleClass(5))
