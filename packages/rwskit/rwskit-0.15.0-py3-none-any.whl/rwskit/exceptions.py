"""Utilities related to exceptions."""

# Standard Library
from typing import Type


def raise_exception(msg: str, exception_type: Type[Exception] = ValueError):
    """Always raises the given ``exception_type` with the supplied ``msg``.

    Parameters
    ----------
    msg : str
        The message for the exception.
    exception_type : Type[Exception], default = ``ValueError``
        The type of exception to raise.

    Raises
    ------
    exception_type
    """
    raise exception_type(msg)
