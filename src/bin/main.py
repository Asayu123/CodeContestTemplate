import sys


def main():

    # Get Args
    args = _input_args()  # get arguments as an array from console/script parameters.

    # Call main Logic
    result = _main(args)

    # Export a result in a correct way.
    _export_result(result)


def _main(args):
    """Write Main Logic here for the contest.

    :param args: arguments
    :type args: list
    :return: result
    :rtype: depends on your logic.
    """
    N = int(args[0])
    Q = int(args[1])

    alphabets = list((chr(ord('A') + i) for i in range(N)))
    result = merge_sort(array=alphabets)
    return result


def merge_sort(array):

    if len(array) <= 1:  # You can't sort if the array length is less than or equal to 1.
        return array

    # Define variables for array index.
    head = 0
    end = len(array) - 1
    center = int(head+end/2)

    # Divide original array to partial arrays.
    array_part1 = array[head:center + 1]  # Contains array[0] ... array[center]
    array_part2 = array[center + 1:end + 1]  # Contains array[center + 1] ... array[end]

    # Do sort in partial arrays recursively.
    sorted_partial_array_1 = merge_sort(array_part1)
    sorted_partial_array_2 = merge_sort(array_part2)

    # Merge two sorted arrays.
    merged_array = _merge_partial_arrays(sorted_partial_array_1, sorted_partial_array_2)
    return merged_array


def _merge_partial_arrays(array1, array2):
    """Merge two partial arrays to one sorted array.
    Compare each array heads and pop smaller one and append it to result array.
    If either array becomes empty, append the rest of array elements to the result array.

    BOTH PARTIAL ARRAYS MUST HAVE BEEN SORTED.
    """
    result = []
    head = 0  # Define index number in order not to implement magic number to the source code.

    while len(array1) != 0 and len(array2) != 0:  # While either of arrays is not empty,
        if _is_elem1_smaller(elem1=array1[head], elem2=array2[head]):  # Compare both heads and pop smaller one to a new array.
            result.append(array1.pop(head))
        else:
            result.append(array2.pop(head))

    # Append the rest of array elements. Either array1 or array2 is empty.
    result.extend(array1)
    result.extend(array2)

    return result


def _is_elem1_smaller(elem1, elem2):
    print('? {} {}'.format(elem1, elem2))
    char = _input()
    if char == '<':
        return True
    else:
        return False


# def _main(args):  # bubble sort
#     """Write Main Logic here for the contest.
#
#     :param args: arguments
#     :type args: list
#     :return: result
#     :rtype: depends on your logic.
#     """
#     # Extract arguments.
#     N = int(args[0])
#     Q = int(args[1])
#
#     alphabets = list((chr(ord('A') + i) for i in range(N)))
#
#     for i in range(0, len(alphabets)-1):
#         for j in range(0, len(alphabets)-1-i):
#             print('? {} {}'.format(alphabets[j], alphabets[j+1]))
#
#             comp_result = _input()
#             if comp_result == '<':
#                 pass
#             elif comp_result == '>':
#                 alphabets[j], alphabets[j+1] = alphabets[j+1], alphabets[j]
#             else:
#                 raise ValueError('input should either of "<" ">"')
#
#     # Write main logic here.
#     result = alphabets
#
#     # Return something.
#     return result

def _input_args():
    # Comment-out appropriate pattern depends on subject.

    # arguments = sys.argv[1:]  # ptn1: get args from script parameters.
    arguments = _input().split()  # ptn2: get args from 1 line console prompt with space separated.

    # for multi-line console input, use this.
    # arguments = _get_args_from_multiple_lines(end_of_lines_char=[''])

    # Cast elements If you need.
    # arguments = list(map(int, arguments))  # cast elements to int for example.

    return arguments  # This will be array.


def _input():
    # If Subject requires interactive input, use this and patch mock in unittest.
    return input()  # Change if necessary.


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
        except EOFError:  # Supports EOF Style. (Very Rare case)
            break
    return args


def _export_result(result):
    # Comment-out appropriate output pattern depends on subject.

    # sys.stdout.write(result)  # No Line Feed, and an result must be string (not useful). for single value output.
    # print(result)  # The result will cast to strings. Line feed will be appended to the end. for single value output.
    # print(result, end='')  # Same as above except Line Feed won't be appended. for single value output.
    print('! '+ ''.join(map(str, result)))  # Print array elements as comma separated strings. for multi-value.
    # print('! {}'.format(str(result)))  # Same as above, but more versatile. for multi-value.


if __name__ == '__main__':
    main()
