# -*- coding: utf-8 -*-

"""Trivial version test."""

import unittest

from simple_resolver import contract
from simple_resolver.version import get_version


class TestContract(unittest.TestCase):
    def test_chebi(self):
        prefix_map = {"chebi": "https://bioregistry.io/chebi:"}
        result = contract("https://bioregistry.io/chebi:1234", prefix_map)
        self.assertEqual("chebi:1234", result)
        # assert 'chebi:1234' == result


class TestVersion(unittest.TestCase):
    """Trivially test a version."""

    def test_version_type(self):
        """Test the version is a string.

        This is only meant to be an example test.
        """
        version = get_version()
        assert isinstance(version, str)
        self.assertIsInstance(version, str)

    def test_something_else(self):
        pass
