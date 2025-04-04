from __future__ import annotations

import functools
import inspect
import os
import re
from typing import Awaitable, Callable, TypeVar, cast

from ._typing_extensions import ParamSpec, TypeGuard

# --------------------------------------------------------------------
# wrap_async() and is_async_callable() was copied from shiny/_utils.py
# --------------------------------------------------------------------

R = TypeVar("R")  # Return type
P = ParamSpec("P")


def wrap_async(
    fn: Callable[P, R] | Callable[P, Awaitable[R]],
) -> Callable[P, Awaitable[R]]:
    """
    Given a synchronous function that returns R, return an async function that wraps the
    original function. If the input function is already async, then return it unchanged.
    """

    if is_async_callable(fn):
        return fn

    fn = cast(Callable[P, R], fn)

    @functools.wraps(fn)
    async def fn_async(*args: P.args, **kwargs: P.kwargs) -> R:
        return fn(*args, **kwargs)

    return fn_async


def is_async_callable(
    obj: Callable[P, R] | Callable[P, Awaitable[R]],
) -> TypeGuard[Callable[P, Awaitable[R]]]:
    """
    Determine if an object is an async function.

    This is a more general version of `inspect.iscoroutinefunction()`, which only works
    on functions. This function works on any object that has a `__call__` method, such
    as a class instance.

    Returns
    -------
    :
        Returns True if `obj` is an `async def` function, or if it's an object with a
        `__call__` method which is an `async def` function.
    """
    if inspect.iscoroutinefunction(obj):
        return True
    if hasattr(obj, "__call__"):  # noqa: B004
        if inspect.iscoroutinefunction(obj.__call__):  # type: ignore
            return True

    return False


T = TypeVar("T")


def drop_none(x: dict[str, T | None]) -> dict[str, T]:
    return {k: v for k, v in x.items() if v is not None}


# https://docs.pytest.org/en/latest/example/simple.html#pytest-current-test-environment-variable
def is_testing():
    return os.environ.get("PYTEST_CURRENT_TEST", None) is not None


class MISSING_TYPE:
    """
    A singleton representing a missing value.
    """

    pass


MISSING = MISSING_TYPE()


# --------------------------------------------------------------------
# html_escape was copied from htmltools/_utils.py
# --------------------------------------------------------------------


HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    ">": "&gt;",
    "<": "&lt;",
}

HTML_ATTRS_ESCAPE_TABLE = {
    **HTML_ESCAPE_TABLE,
    '"': "&quot;",
    "'": "&apos;",
    "\r": "&#13;",
    "\n": "&#10;",
}


def html_escape(text: str, attr: bool = True) -> str:
    table = HTML_ATTRS_ESCAPE_TABLE if attr else HTML_ESCAPE_TABLE
    if not re.search("|".join(table), text):
        return text
    for key, value in table.items():
        text = text.replace(key, value)
    return text
