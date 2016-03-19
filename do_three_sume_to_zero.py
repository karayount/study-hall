""" Write a function to determine if any 3 integers in an array sum to 0.
If so, return true, else false.
Example: [1, -1, 3, 5, 2, -2] --> True
"""

def three_sum_to_zero(lst):
    seen = set()
    prev_sums = set()
    for num in lst:
        match = 0 - num
        if match in prev_sums:
            return True
        else:
            for prev in seen:
                new_sum = prev + num
                prev_sums.add(new_sum)
            seen.add(num)
    return False


num_list = [1, -1, 3, 5, 2, -2]
print three_sum_to_zero(num_list)