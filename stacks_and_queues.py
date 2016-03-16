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

    def __init__(self, starting_list=[]):

        working_list = []
        for item in starting_list:
            node = DLLNode(item)
            working_list.append(node)

        if len(working_list) > 0:

            self.head = working_list[0]
            self.tail = working_list[-1]
            if len(working_list) > 1:
                self.head.next = working_list[1]
                self.tail.prev = working_list[-2]

            for i in range(1, len(working_list)-1):
                working_list[i].prev = working_list[i-1]
                working_list[i].next = working_list[i+1]

    def print_Q(self):

        current = self.head
        print current.data
        while current.next != None:
            current = current.next
            print current.data

    def enqueue(self, node):

        new_item = DLLNode(node)
        self.tail.next = new_item
        new_item.prev = self.tail
        new_item.next = None
        self.tail = new_item


    def dequeue(self):

        dequeued_item = self.head
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head
        return dequeued_item

    def peek(self):

        return self.head

    def is_empty(self):

        return self.head is None


class DLLNode(object):
    """ node of a doubly linked list """

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


consolis = DLLQueue(["Kara", "Kevin", "Kyla", "Chris", "Nick", "Ali", "Dana"])