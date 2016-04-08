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

    def pop(self):
        """ Removes and returns smallest item in heap.
        Heapifies remaining elements.

        Returns None if heap is empty. """

        if self._size < 1:
            return
        smallest = self._heap_list[1]
        # move end item to root
        # perc_down(root)
        return smallest

    def push(self, value):
        pass

    def peek(self):
        """ returns value of smallest item in heap, None if empty"""
        if self._size < 1:
            return
        else:
            return self._heap_list[1]

    def current_size(self):
        return self._size

    def _perc_up(self):
        pass

    def _perc_down(self):
        # find smallest child
        # while this is larger than smallest child, swap
        pass


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
                high_scores.pop()
                high_scores.push(score)

    # build list of high scores from heap
    how_many_high_scores = high_scores.current_size()
    top_scores_list = [None] * how_many_high_scores
    last = how_many_high_scores - 1
    for i in range(last, -1, -1):
        score = high_scores.pop()
        top_scores_list[i] = score

    return top_scores_list

