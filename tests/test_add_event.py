#!/usr/bin/python3
# -*- coding: utf8 -*-
import unittest
from input_parser import InputParser


class TestInputParser(unittest.TestCase):

    def test_entry_is_string(self):

        content = "today we had events going on here"

        parser = InputParser()
        parser.parse()

    def test_entry_is_url(self):
        pass
