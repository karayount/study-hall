class Stack(object):
    """ stack """

    def __init__(self, starting_list=None):
        if starting_list is None:
            self._list = []
        else:
            self._list = starting_list

    def push(self, data):
        """ Adds input data to top of stack
        :param data: thing to push to stack
        :return: none
        """

        self._list.append(data)

    def pop(self):
        """ Removes and returns item from top of stack
        :return: item from top of stack
        """

        popped = self._list.pop()
        return popped


class Queue(object):
    """ queue """

