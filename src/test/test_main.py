# -*- coding: utf-8 -*-
import unittest
from unittest import skip
from test.support import captured_stdout

from src.bin.main import main, _main
from unittest.mock import MagicMock, patch


class TestMain(unittest.TestCase):

    @staticmethod
    def generate_subtest_case():
        """This function creates sub_test case for parameterized test.
        PLEASE define INPUT and OUTPUT Value HERE for test.
        :return: input_list, expected_list
        :rtype list of list, list of str
        """

        input_list = [
            ['0 3', '1', '2', '3'],
            ['0 2', '1', '2'],
            ['0 1', '1']
        ]

        expected_list = [
            'ans=6',
            'ans=3',
            'ans=1'
        ]

        return input_list, expected_list

    @staticmethod
    def get_input_mock(inputs=None):  # Use this mock if a contest requires interactive input.
        """Get Mock that emulate standard input. You won't use this function directly.

        :param inputs: Define standard inputs that you want emulate. one element one input.
         example: ['0 3', '1', '2', '3']
        :type inputs: list of str
        :return: stdin_lines
        :rtype MagicMock
            Caution, MagicMock raises StopIteration error when you call input function more than length of 'inputs'
            in main.py
        """
        stdin_mock = MagicMock()
        stdin_mock.side_effect = inputs  # you can emulate standard input lines by using this list.
        return stdin_mock

    @staticmethod
    def get_last_stdout_line(stdout):  # This method sometimes useful when you print results to stdout.
        # If there are multiple outputs, stdout.getvalue returns combined one. so we need split to get a specific line.
        return stdout.getvalue().split('\n')[-2]

    def test_main(self):
        """Test Whole things, including standard Input/Output by using input mocking.
        Use this test if the contest requires input from stdin, and requires export result to stdout.
        """

        input_list, expected_list = self.generate_subtest_case() # Get test parameters.

        for input_lines, expected_result in zip(input_list, expected_list):  # extract params for sub_test.
            # Execute sub_test for each params.
            with self.subTest(input=input_lines, output=expected_result):

                # Emulate input_lines by mock
                with patch(target='src.bin.main._input', new=self.get_input_mock(inputs=input_lines)):

                    # Execute main logic with capturing standard output.
                    with captured_stdout() as stdout:
                        main()
                        actual_result = self.get_last_stdout_line(stdout)

                        self.assertEqual(expected_result, actual_result)

    @skip
    def test__main(self):
        """Test for Main Logic Only.
        Use This test if the contest only evaluates method level Input/Output and not interactive.
        """

        args = ['1', '2']
        expected = ['11', '22']

        result = _main(args)

        self.assertEqual(expected, result)
