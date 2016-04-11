""" Given a binary tree, return whether it meets criteria for binary
search tree.

Assume values of nodes are in range (-500, 500)
"""

class BTreeNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return "<BTreeNode data=%s>" % self.data


def build_btree_from_array(arr):
    start = 0
    end = len(arr)
    root = help_build_btree(arr, start, end)
    return root


def help_build_btree(arr, start, end):
    if end == start:
        return
    mid = (start+end)/2
    left_start = start
    left_end = mid
    right_start = mid + 1
    right_end = end
    current = arr[mid]

    node = BTreeNode(current,
                   help_build_btree(arr, left_start, left_end),
                   help_build_btree(arr, right_start, right_end))

    return node


def is_btree_a_BST(node, low=-501, high=501):
    """ Determine whether a given binary tree is a binary search tree
    :param node: root of binary tree
    :param low: lower bound of valid values
    :param high: upper bound of valid values
    :return: boolean

    This function's default values assume binary tree nodes have values in
    range (-500, 500).
    """
    if node is None:
        return True
    else:
        value = node.data
        in_range = False
        if value >= low and value <=high:
            in_range = True
        left_child = is_btree_a_BST(node.left, low, value)
        right_child = is_btree_a_BST(node.right, value, high)
        return in_range and left_child and right_child


my_sorted_array = [1, 3, 7, 14, 22, 30, 42, 90, 105, 245, 337]
my_array = [-6, 7, 5, -10, 16, 17, 99, -345, 262]
true_root = build_btree_from_array(my_sorted_array)
false_root = build_btree_from_array(my_array)
print is_btree_a_BST(true_root)
print is_btree_a_BST(false_root)

