# -*- coding: utf-8 -*-

"""Main code."""

__all__ = [
    "contract",
]

# mypy, optional static typing


def contract(uri: str, prefix_map: dict[str, str]) -> str:
    """Contract a URI into a CURIE given the prefix map.

    :param uri:
        A URL or URL to contract
    :param prefix_map:
        A mapping that has short prefixes as the keys and
        URI prefixes in the values
    :returns:
        A contracted URI as a CURIE if it can be contracted,
        otherwise return the original URI

    >>> prefix_map = {"chebi": "https://bioregistry.io/chebi:"}
    >>> contract("https://bioregistry.io/chebi:1234", prefix_map)
    'chebi:1234'
    """
    for key, value in prefix_map.items():
        if uri.startswith(value):
            return f"{key}:{uri.removeprefix(value)}"
    return uri
