from unittest.mock import MagicMock
from unittest.mock import patch
from test.support import captured_stdout


class StdInOutTestCase(object):
    """This class implements basic test cases.
    Only you need to do is mix in this class with unittest.TestCase in a subclass, and override class attributes.
    This mixin assumes that all input values are given from stdin, and all result is dumped to the last several lines of stdout.
    """
    # Override following params in your TestCase.
    target_method = None  # Define a target method that needs to be tested.
    input_cases = None  # Must be a list of a list of strings.
    expected_outputs = None  # Must be a list of a list of strings.

    # Examples
    # module =
    # input_cases = [
    #             ['0 3', '1', '2', '3'],  # One list corresponds to a one test case.
    #             ['0 2', '1', '2'],  # One Element of the list corresponds to a one line
    #             ['0 1', '1']
    #         ]
    # expected_outputs = [
    #             ['6'],
    #             ['3'],
    #             ['1']
    #         ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert self.target_method, "Please override 'target_method' class attribute in a subclass of TestBase"
        assert self.input_cases, "Please override 'input_cases' class attribute in a subclass of TestBase"
        assert self.expected_outputs, "Please override 'expected_outputs' class attribute in a subclass of TestBase"

    @staticmethod
    def get_input_mock(inputs=None):  # Use this mock if a contest requires interactive input.
        """Get Mock that emulate standard input. You won't use this function directly.

        :param inputs: Define standard inputs that you want to emulate. One element corresponds to one line.
         example: ['0 3', '1', '2', '3']
        :type inputs: list of str
        :return: stdin_lines
        :rtype MagicMock
            Caution, MagicMock raises StopIteration error
             when you call input function more than the length of 'inputs' in main.py
        """
        stdin_mock = MagicMock()
        stdin_mock.side_effect = inputs  # You can emulate standard input lines by using this list.
        return stdin_mock

    @staticmethod
    def get_stdout_line(stdout, bottom=1):
        """This method captures stdout lines and converts it to the list of strings.
        By Default, with no 'bottom' specified, only returns the last line as a list that length is 1.

        :param stdout: test.support.captured_stdout context
        :param bottom: A number of lines you want to capture from the bottom.
        :type bottom: int
        :rtype: list of str
        """
        # If there are multiple outputs, stdout.getvalue returns combined one. so we need split to get a specific line.
        return stdout.getvalue().split('\n')[-(bottom + 1):-1]

    def test_e2e(self):
        """Test Whole things, including standard Input/Output by using input mocking.
        Use this test if the contest requires input from stdin, and requires the export result to stdout.
        """

        for input_lines, expected_result in zip(self.__class__.input_cases, self.__class__.expected_outputs):  # extract params for sub_test.
            # Execute sub_test for each test cases.
            with self.subTest(input=input_lines, output=expected_result):

                # Emulate input_lines by mock
                with patch(target='builtins.input', new=self.get_input_mock(inputs=input_lines)):

                    # Execute main logic with capturing standard output.
                    with captured_stdout() as stdout:
                        self.__class__.target_method()  # If mock raises StopIteration here, it means that the input method has been called more than the number of supplied lines by Mock.
                        actual_result = self.get_stdout_line(stdout=stdout, bottom=len(expected_result))

                        self.assertEqual(expected_result, actual_result)
