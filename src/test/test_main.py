import unittest
from test.support import captured_stdout, captured_stderr

from src.bin.main import main


class TestMain(unittest.TestCase):

    def test_main(self):
        """Test for Main Logic.
        Warning: This test doesn't ensure whether input correctly delivered to main.
        """
        expected = 'HelloWorld'  # if there are multiple output, combine it with \n.
        args = ['Hello', 'World']

        with captured_stdout() as stdout, captured_stderr() as stderr:
            main(*args)

        self.assertEqual(expected, stdout.getvalue())
        # if there are multiple output, stdout.getvalue returns combined one.
