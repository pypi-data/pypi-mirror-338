import itertools
from typing import Any

from skabelon.filter.common import join_newline


def markdown_heading(value: str, level: int = 1) -> str:
    """Transform a string into a Markdown heading of a given level"""
    return f"{'#' * level} {value}"


def markdown_list(value: list[Any]) -> str:
    """Transform a list of values into a Markdown list"""
    return join_newline([f"- {x}" for x in value])


def markdown_enumeration(value: list[Any]) -> str:
    """Transform a list of values into a Markdown enumeration"""
    return join_newline([f"{idx}. {x}" for idx, x in enumerate(value, start=1)])


def markdown_monospace(value: str) -> str:
    """Wrap a string with Markdown monospace formatting"""
    return f"`{value}`"


def markdown_codeblock(value: list[str] | str, language: str | None = None) -> str:
    """Wrap a string or list of strings in Markdown code block formatting"""
    prefix = f"```{language}" if language else "```"
    suffix = "```"

    components = [prefix, *(value if isinstance(value, list) else [value]), suffix]

    return join_newline(components)


def markdown_table_row(value: list[Any]) -> str:
    """Wrap a list of strings as a Markdown table row"""
    return f"| {' | '.join(value)} |"


def markdown_table(
    value: list[list[Any]], header: list[str] | None = None, fill_values: bool = False
) -> str:
    """Wrap a list of strings in Markdown table formatting"""
    body = []
    empty = ""

    value = list(value)
    element_count = max(map(len, value))

    if header:
        header = header[0:element_count]
        body.append(markdown_table_row(value=header))
        body.append(markdown_table_row(["---"] * element_count))

    # Optionally fill missing body values up to maximum line length
    if fill_values and any([len(x) < element_count for x in value]):
        value = [
            [
                v
                for _, v in itertools.zip_longest(
                    [empty] * element_count, x, fillvalue=empty
                )
            ]
            for x in value
        ]

    body.extend(list(map(markdown_table_row, value)))

    return join_newline(body)
