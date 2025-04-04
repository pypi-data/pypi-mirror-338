from __future__ import annotations

from collections.abc import Iterable
from typing import Literal

# Color names for termcolor
TextColor = Literal[
    "black",
    "grey",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
    "white",
]

# Color attributes for termcolor
TextStyle = Iterable[
    Literal[
        "bold",
        "dark",
        "underline",
        "blink",
        "reverse",
        "concealed",
    ]
]


# Translation table for smart quotes replacement
SMART_QUOTES_TABLE = str.maketrans({
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
})
