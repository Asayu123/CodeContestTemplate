# -*- coding: utf-8 -*-
from unittest import TestCase

from src.bin.main import main  # Change this source based on what you want to test.
from src.test.base.mixins import StdInOutTestCase


class StdInOutTestCase(StdInOutTestCase, TestCase):
    # If the contest site uses Stdin and Stdout for evaluation, use this test case.
    # See the definition of the Mixin class to know the details of what class attributes you need to override.
    target_method = main
    input_cases = [
        ['0 3', '1', '2', '3'],
        ['0 2', '1', '2'],
        ['0 1', '1']
    ]

    expected_outputs = [
        ['6'],
        ['3'],
        ['1']
    ]


class MainRoutineTestCase(TestCase):
    # If the contest site uses return value for evaluation, use this test case.

    def test_main(self):
        """Test for Main Logic Only.
        Use This test if the contest only evaluates method level Input/Output and not interactive.
        """

        args = ['1', '2']
        expected = ['11', '22']

        result = main(*args)

        self.assertEqual(expected, result)
