""" Given an input list that has some breaking point, and would be sorted if the
slice of the list before the breaking point were removed and appended to the
end, find the index of a number in the list.
Assume all values in array are unique.

"""

# binary search to find breaking point, store that
# compare number searching for to first array element, to determine whether
# to search before breaking point or after
# use breaking point as start/end and search that "half" of array for num
sample = [7, 8, 1, 2, 3]
another = [10, 14, 16, 18, 21, 2, 5, 6, 8]


def find_num(num, lst):
    lowest = find_break(num, lst)
    if num < lst[0]:
        start = lowest
        end = len(lst)
    else:
        start = 0
        end = lowest
    result = find_index(num, start, end, lst)
    return result


def find_break(num, lst):
    """ find index of first element after break point
    :param num: number to search for
    :param lst: input list to search
    :return: index of lowest value in list
    """
    first = lst[0]
    start = 0
    end = len(lst)
    mid = end/2
    while start < end:
        if lst[mid] < lst[mid-1]:
            return mid
        elif lst[mid] < first:
            end = mid
            mid = (start+end)/2
        else:
            start = mid + 1
            mid = (start+end)/2
    return mid


def find_index(num, start_index, end_index, lst):
    """ find the index of
    :param num: element to find
    :param start: first index of subarray
    :param end: last index of subarray
    :param lst: input list to search
    :return: index of num
    """
    start = start_index
    end = end_index
    mid = (start+end)/2
    while start < end:
        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            start = mid + 1
            mid = (start+end)/2
        else:
            end = mid
            mid = (start+end)/2

    return "Number not in list"


print find_num(3, sample)
print find_num(3, another)