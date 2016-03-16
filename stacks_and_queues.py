class Stack(object):
    """ stack """

    def __init__(self, starting_list=None):
        """ Create a new Stack """

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


    def peek(self):
        """ show item at top of stack """




class Queue(object):
    """ queue """

    def __init__(self, starting_list=None):
        """ create a new Queue """
        if starting_list:
            self._list = starting_list
        else:
            self._list = []

    def enqueue(self, item):
        """ add an item to the end of the queue """

        self._list.append(item)

    def dequeue(self):
        """ remove and item from the beginning of the queue
        :return: removed item
        """

        if len(self._list) > 0:
            popped = self._list.pop(0)
            return popped
        else:
            return "Cannot dequeue and empty queue."

    def peek(self):
        """ show first item in queue """

        first = self._list[0]
        return first

    def is_empty(self):
        """ return boolean of whether queue is empty
        :return: boolean
        """

        return len(self._list) == 0

    def __repr__(self):
        """ nice representation of object """

        return "Queue with %d items" % (len(self._list))



class DLLQueue(object):
    """ queue built on doubly linked list """

    pass


class DLL(object):
    """ doubly linked list """

    pass


class DLLNode(object):
    """ node of a doubly linked list """


