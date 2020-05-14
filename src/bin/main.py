import sys


def main(*args, **kwargs):
    """Write Codes for contest here."""
    pass


def _input_args():
    # Comment-out appropriate pattern depends on subject.

    # arguments = sys.argv[1:]  # ptn1: get args from script parameters.
    arguments = input().split()  # ptn2: get args from 1 line console prompt with space separated.

    # for multi-line console input, use this.
    # arguments = _get_args_from_multiple_lines(end_of_lines_char=[''], limit=10000000)

    # Cast elements If you need.
    # arguments = list(map(int, arguments))  # cast elements to int for example.

    return arguments  # This will be array.


def _get_args_from_multiple_lines(end_of_lines_char=[''], limit=10000000):
    """Get arguments from multiple lines standard input.

    :param end_of_lines_char: Strings that indicate the end of lines.
    :type end_of_lines_char: list of str
    :param limit: If a number of the input line are certain, you can use this param to close prompt immediately.
    :type limit: int
    :return: args
    :rtype list of str
    """
    args = []
    for i in range(limit):
        try:
            arg = input()
            if arg in end_of_lines_char:
                break
            args.append(arg)
        except (EOFError, StopIteration):  # Supports EOF Style. (Very Rare case), StopIteration for mock.
            break
    return args


def _output_result(result):
    # Comment-out appropriate output pattern depends on subject.

    # sys.stdout.write(result)  # No Line Feed, and an result must be string (not useful). for single value output.
    # print(result)  # The result will cast to strings. Line feed will be appended to the end. for single value output.
    # print(result, end='')  # Same as above except Line Feed won't be appended. for single value output.
    # print(','.join(map(str, result)))  # Print array elements as comma separated strings. for multi-value.
    print('{}'.format(str(result)))  # Same as above, but more versatile.


if __name__ == '__main__':
    main()
