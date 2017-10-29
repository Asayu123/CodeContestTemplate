import sys


def main(*args):

    # Receive arguments.
    arg1 = args[0]
    arg2 = args[1]

    # Write main logic here.
    output = arg1 + arg2

    # Export result in correct way.
    _export_result(output)


def _input_args():
    # Comment-out appropriate pattern depends on subject.

    # arguments = sys.argv[1:]  # ptn1: get args from command line option
    arguments = input().split()  # ptn2: get args from 1 line prompt with space separated.

    # for multi-line input, use this.
    # arguments = _get_args_from_multiple_lines(end_of_lines_char=[''])

    # Cast elements If you need.
    # arguments = map(int, arguments)  # cast elements to int for example.

    return arguments


def _get_args_from_multiple_lines(end_of_lines_char=['']):
    """Get arguments from multiple lines standard input.

    :param end_of_lines_char: Strings that indicate the end of lines.
    :type end_of_lines_char: list of str
    :return: args
    :rtype list of str
    """
    args = []
    while True:
        try:
            arg = input()
            if arg in end_of_lines_char:
                break
            args.append(arg)
        except EOFError:  # Supported for EOF Style. (Very Rare case)
            break
    return args


def _export_result(output):
    # Comment-out appropriate output pattern depends on subject.

    # sys.stdout.write(output)  # No Line Feed, and arg must be string. for single value output.
    # print(output)  # Output automatically evaluated and cast to strings. LF at the end. for single value output.
    print(output, end='')  # No Line Feed version of above. for single value output.
    # print(','.join(map(str, output)))  # Print array elements as comma separated strings. for multi-value.
    # print('{}, {}'.format(output[0], output[1], end=''))  # Same results, but more versatile. for multi-value.


if __name__ == '__main__':

    arguments = _input_args()
    # Execute main Logic.
    main(*arguments)
