# -*- coding=utf-8 -*-
from __future__ import absolute_import, print_function

import os
import sys
import threading
import time
from io import StringIO

import pipenv.vendor.colorama as colorama
import pipenv.vendor.six as six

from .compat import IS_TYPE_CHECKING, to_native_string
from .cursor import hide_cursor, show_cursor
from .misc import decode_for_output, to_text

if IS_TYPE_CHECKING:
    from typing import (
        Any,
        Callable,
        ContextManager,
        Dict,
        IO,
        Optional,
        Text,
        Type,
        TypeVar,
        Union,
    )

    TSignalMap = Dict[
        Type[signal.SIGINT],
        Callable[..., int, str, Union["DummySpinner", "VistirSpinner"]],
    ]
    _T = TypeVar("_T", covariant=True)

try:
    import pipenv.vendor.yaspin as yaspin
except ImportError:  # pragma: no cover
    yaspin = None
    Spinners = None
    SpinBase = None
else:  # pragma: no cover



