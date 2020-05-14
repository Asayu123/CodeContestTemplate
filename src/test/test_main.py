# -*- coding: utf-8 -*-
from unittest import TestCase

from src.bin.main import main  # Change this source based on what you want to test.
from src.test.base.mixins import StdInOutTestMixin


class StdInOutTestCase(StdInOutTestMixin, TestCase):
    # If the contest site uses Stdin and Stdout for evaluation, use this test case.
    # See the definition of the Mixin class to know the details of what class attributes you need to override.
    target_method = main
    input_cases = [  # Format: [testCase[inputLine]]
        ['0 3', '1', '2', '3'],
        ['0 2', '1', '2'],
        ['0 1', '1']
    ]

    expected_outputs = [  # Format: [testCase[outputLine]]
        ['6'],  # The order needs to correspond to that of input_cases.
        ['3'],
        ['1']
    ]


class MainRoutineTestCase(TestCase):
    # If the contest site uses return value for evaluation, use this test case.

    def test_main(self):
        """Test Return value."""

        test_cases = [  # Format: [testCase[positional argument]]
            [1, 2],  # Positional arguments per a test case.
        ]

        expected_return_values = [  # Format: [testCase[expectedReturnValue]]
            11,  # return value/values per a test case.
        ]

        for args, expected_return_value in zip(test_cases, expected_return_values):
            with self.subTest(args=args):
                result = main(*args)
                self.assertEqual(result, expected_return_value)
