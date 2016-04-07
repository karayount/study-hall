"""Given a list_of_ints, find the highest_product you can get from
three of the integers.

The input list_of_ints will always have at least three integers.

>>> find_highest_product([1, 2, 3, 4, 5])
60

>>> find_highest_product([1, 2, 3, 2, 3, 2, 3, 4])
36

>>> find_highest_product([0, 1, 2])
0

>>> find_highest_product([-8, -1, 2, 0, 1])
16
"""

def find_highest_product_slow(arr):
    prod_seen = set()
    num_seen = set()
    max_prod = None
    for num in arr:
        if max_prod is None:
            max_prod = num
        for prod in prod_seen:
            possible_max = prod * num
            if possible_max > max_prod:
                max_prod = possible_max
        for seen in num_seen:
            prod_seen.add(seen*num)
        num_seen.add(num)
    return max_prod


def find_highest_product(arr):
    highest_seen_prod = None
    lowest_seen_prod = None

    
    max_prod = None
    for num in arr:
        if max_prod is None:
            max_prod = num
        for prod in prod_seen:
            possible_max = prod * num
            if possible_max > max_prod:
                max_prod = possible_max
        for seen in num_seen:
            prod_seen.add(seen*num)
        num_seen.add(num)
    return max_prod



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WE'RE WELL-MATCHED!\n"
