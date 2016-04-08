""" Given an array of pinball scores, where each score is a positive integer,
return a list of the 10 highest scores from highest to lowest. If there are
less than ten scores, return the complete list, from highest to lowest.
"""

# build minHeap to store highest scores. minHeap used rather than maxHeap, so
#   peek can compare to 10th highest (quickly) and see if we need to add
#   current score in array (as we loop over it) to the high scores

class minHeap(object):
    def __init__(self):
        self._heap_list = [0]
        self._size = 0

    def get_min(self):
        """ Removes and returns smallest item in heap.
        Heapifies remaining elements.

        Returns None if heap is empty. """

        if self._size < 1:
            return None

        smallest = self._heap_list[1]
        max = self._size

        # move end item to root
        self._heap_list[1] = self._heap_list[max]
        self._heap_list.pop()
        self._size = max-1
        self._perc_down(1)

        return smallest


    def push(self, value):
        self._heap_list.append(value)
        self._size += 1
        self._perc_up(self._size)

    def peek(self):
        """ returns value of smallest item in heap, None if empty"""
        if self._size < 1:
            return None
        else:
            return self._heap_list[1]

    def current_size(self):
        return self._size

    def _perc_up(self, index):
        i = index
        while i / 2 > 0:
            if self._heap_list[i] < self._heap_list[i/2]:
                temp = self._heap_list[i/2]
                self._heap_list[i/2] = self._heap_list[i]
                self._heap_list[i] = temp
            i = i/2


    def _perc_down(self, index):
        i = index
        sc = self._find_smaller_child(i)
        while sc <= self._size:
            if self._heap_list[i] > self._heap_list[sc]:
                temp = self._heap_list[sc]
                self._heap_list[sc] = self._heap_list[i]
                self._heap_list[i] = temp
            i = sc
            sc = self._find_smaller_child(i)


    def _find_smaller_child(self, i):
        """ find the smaller of node's children, if any children exist
        :param i: index of node
        :return: index of smaller of node's children
        """

        left_child_index = 2*i
        right_child_index = (2*i)+1
        if self._size < right_child_index:
            return left_child_index
        if self._heap_list[left_child_index] < self._heap_list[right_child_index]:
            return left_child_index
        else:
            return right_child_index


def find_top_ten(scores_list):
    """ from a list of pinball scores, return the 10 highest
    :param scores_list: array of positive integer pinball scores
    :return: list of 10 highest scores, descending order, or full list if input
    list had less than 10 items
    """

    # build heap with 10 highest scores
    high_scores = minHeap()
    for score in scores_list:
        if high_scores.current_size() < 10:
            high_scores.push(score)
        else:
            tenth_highest = high_scores.peek()
            if score > tenth_highest:
                high_scores.get_min()
                high_scores.push(score)

    # build list of high scores from heap
    how_many_high_scores = high_scores.current_size()
    top_scores_list = [None] * how_many_high_scores
    last = how_many_high_scores - 1
    for i in range(last, -1, -1):
        score = high_scores.get_min()
        top_scores_list[i] = score

    return top_scores_list


scores1 = [1, 4, 100, 62, 7, 48, 15, 66, 92, 45, 53, 56, 18, 27, 40]
scores2 = [10, 14, 16, 17, 18]
print find_top_ten(scores1)
print find_top_ten(scores2)