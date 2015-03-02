#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import datetime
import unittest


# Import user libs
import task_01


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    def test_get_current_data(self):
        """Tests that the get_current_date() function returns today()"""
        curdate = datetime.date.today()
        self.assertEqual(task_01.get_current_date(), curdate)

    def test_curdate(self):
        """Tests that CURDATE is initially set as None"""
        self.assertIsNone(task_01.CURDATE)


if __name__ == '__main__':
    unittest.main()
