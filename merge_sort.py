def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst)/2
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    result = []
    while lst1 or lst2:
        if lst1 == []:
            result.append(lst2.pop(0))
        elif lst2 == []:
            result.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    return result


print merge_sort([45, 67, 12, 3, 46, 57, 9, 99, 6, 32])