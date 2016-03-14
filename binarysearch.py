"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> binary_search(100) < 8
    True

    >>> max([binary_search(i) for i in range(1, 100)])
    7
"""

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0
    min = 1
    max = 100
    mid = (min + max)/2
    while min <= max:
        num_guesses += 1
        if mid == val:
            break
        elif val < mid:
            max = mid
            mid = (min + max)/2
        else:
            min = mid + 1
            mid = (min + max)/2

    return num_guesses

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"
