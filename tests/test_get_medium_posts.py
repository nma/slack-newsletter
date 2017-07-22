#!/usr/bin/python3
# -*- coding: utf8 -*-
import unittest

from medium_scraper import MediumReader


class TestMediumDataRetriever(unittest.TestCase):

    def test_get_posts(self):
        medium = MediumReader(user='ifme')
        result = medium.get_posts()

        self.assertIsNotNone(result, 'result can\'t be none!')
        self.assertEqual(type(result), type({}), 'result is not a dict object!')

