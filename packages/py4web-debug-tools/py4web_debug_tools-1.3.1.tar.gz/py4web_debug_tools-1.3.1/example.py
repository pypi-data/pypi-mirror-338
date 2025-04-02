import py4web_debug
from py4web_debug import dbg


def handle(_): ...


def my_decorator(fn):
    return fn


@my_decorator
def some_func(arg):
    return dbg("hello")


dbg("hi")
y = dbg("hi")
py4web_debug.dbg("hi")
z = py4web_debug.dbg("hi")

handle(dbg("hi"))
handle(py4web_debug.dbg("hi"))

some_long_expression = " 3 + 123"

handle(dbg((some_long_expression + some_long_expression)))

some_func(arg=dbg("arg1"))
