import unittest

from src.bin.main import _main


class TestMain(unittest.TestCase):

    def test_main(self):
        """Test for Main Logic.
        Warning: This test doesn't ensure whether input delivered to _main correctly.
        Also, it doesn't ensure whether result exported as correct format.
        """

        args = ['1', '2']
        expected = ['11', '22']

        result = _main(args)

        self.assertEqual(expected, result)
        # if there are multiple output, stdout.getvalue returns combined one.
