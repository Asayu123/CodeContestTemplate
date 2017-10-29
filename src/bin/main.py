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

    # Cast elements If you need.
    # arguments = map(int, arguments)  # cast elements to int for example.

    return arguments


def _export_result(output):
    # Comment-out appropriate output pattern depends on subject.

    # sys.stdout.write(output)  # No Line Feed, and arg must be string. for single value output.
    # print(output)  # With Line Feed, and automatically eval and cast args. for single value output.
    print(output, end='')  # No Line Feed version of above. for single value output.
    # print(','.join(map(str, array_to_output))) # Print array elements with comma separated. for multi value.
    # print('{}, {}'.format(arg1, arg2, end=''))  # Same results, but more versatile. for multi value.


if __name__ == '__main__':

    arguments = _input_args()
    # Execute main Logic.
    main(*arguments)
