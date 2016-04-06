# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
#
# For example, given:
#
#   [1, 7, 3, 4]
#
# your function would return:
#
#   [84, 12, 28, 21]

def naive_get_products_of_all_ints_except_at_index(lst):

    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [0]
    count_zeroes = 0
    result = []
    max_prod = 1
    for i in range(len(lst)):
        if lst[i] == 0:
            count_zeroes += 1
        else:
            max_prod *= lst[i]
    for num in lst:
        if count_zeroes > 1:
            result.append(0)
        elif count_zeroes == 1:
            if num == 0:
                result.append(max_prod)
            else:
                result.append(0)
        else:
            result.append(max_prod/num)

    return result


def naive_no_division(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [0]
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            if i != j:
                product *= lst[j]
        result.append(product)
    return result


def get_products_of_all_ints_except_at_index(lst):

    # greedy approach
    result = [None] * len(lst)
    running_product = 1
    for i in range(len(lst)):
        result[i] = running_product
        running_product *= lst[i]
    running_prod = 1
    for i in range(len(lst)-1, -1, -1):
        result[i] *= running_prod
        running_prod *= lst[i]

    return result


test_input = [1, 7, 3, 4]
test_zero = [3, 0, 5, 6]
test_zeroes = [0, 0, 4, 5, 8]
print naive_no_division(test_input)
print naive_no_division(test_zero)
print naive_no_division(test_zeroes)

print get_products_of_all_ints_except_at_index(test_input)
print get_products_of_all_ints_except_at_index(test_zero)
print get_products_of_all_ints_except_at_index(test_zeroes)
