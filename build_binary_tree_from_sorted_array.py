""" Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""

class BSTNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return "<BSTNode data=%s>" % self.data


def build_BST(arr):
    start = 0
    end = len(arr)
    root = help_build_BST(arr, start, end)
    return root


def help_build_BST(arr, start, end):
    if end == start:
        return
    mid = (start+end)/2
    left_start = start
    left_end = mid
    right_start = mid + 1
    right_end = end
    current = arr[mid]

    node = BSTNode(current,
                   help_build_BST(arr, left_start, left_end),
                   help_build_BST(arr, right_start, right_end))

    return node


my_array = [1, 3, 7, 14, 22, 30, 42]
root = build_BST(my_array)
print root