# -*- coding: utf-8 -*-
import unittest
from unittest import skip
from test.support import captured_stdout

from src.bin.main import main, _main
from unittest.mock import MagicMock, patch


class TestMain(unittest.TestCase):

    @staticmethod
    def mock_of_inputs():  # Use this mock if a contest requires interactive input.
        stdin_lines = MagicMock()
        stdin_lines.side_effect = ['0 3',  # you can emulate standard input lines by using this list.
                                   '1',
                                   '2',
                                   '3'
                                   ]
        return stdin_lines

    @staticmethod
    def get_last_stdout_line(stdout):  # This method sometimes useful when you print results to stdout.
        return stdout.getvalue().split('\n')[-2]

    def test_main(self):
        """Test Whole things, including standard Input/Output by using input mocking.
        Use this test if the contest requires input from stdin, and requires export result to stdout.
        """
        expected = 'ans=6'

        with patch(target='src.bin.main._input', new=self.mock_of_inputs()):  # emulate inputs by mock
            with captured_stdout() as stdout:
                main()
                result = self.get_last_stdout_line(stdout)

        self.assertEqual(expected, result)
        # if there are multiple output, stdout.getvalue returns combined one.

    @skip
    def test__main(self):
        """Test for Main Logic Only.
        Use This test if the contest only evaluates method level Input/Output and not interactive.
        """

        args = ['1', '2']
        expected = ['11', '22']

        result = _main(args)

        self.assertEqual(expected, result)
