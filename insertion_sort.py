def insertion_sort(lst):

    for i in range(1, len(lst)):
        position = i
        current = lst[i]
        while position > 0 and current < lst[position-1]:
            lst[position] = lst[position-1]
            position -= 1
        lst[position] = current

    return lst


a_list = [67, 89, 12, 34, 42, 52, 6, 55, 76, 1, 10, 15, 71, 17]
print insertion_sort(a_list)