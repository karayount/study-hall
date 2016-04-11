"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31


As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


def find_survivor(num_people, kill_every):
    people_left = []
    for i in range(num_people):
        people_left.append(i+1)
    index = kill_every-1
    survivor_count = num_people
    while survivor_count > 1:
        people_left[index] = 0
        survivor_count -= 1
        index = find_next_index(index, people_left, kill_every)
    return people_left[index]


def find_next_index(start, lst, increment):
    steps = increment
    index = start
    count = 0
    while count < steps:
        index += 1
        if index > len(lst)-1:
            next_one = index % (len(lst))
            index = next_one
        while lst[index] == 0:
            index += 1
            if index > len(lst)-1:
                index = index % (len(lst)+1)
        count += 1
    return index

def find_survivor(num_people, kill_every):
    



class LinkedList(object):
    """ Linked list, pointers to head, tail"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def print_list(self):
        """ displays entire list with print statements
        :return: none
        """

        current = self.head
        while current != None:
            print current
            current = current.next

    def find(self, data):
        """ finds Node in LL with input data.
        :param data: data attribute of Node sought
        :return: Node sought
        """

        if self.head:
            current = self.head
            while current is not None:
                if current.data == data:
                    return current
                current = current.next

    def add_in_order(self, data, after):
        """ Adds new node with data, after input node.
        :param data: content of node, after: node before new node
        :return: none
        """

        if self.head:
            current = self.head
            while current is not None:
                if current.data == after:
                    new_node = LLNode(data)
                    new_node.next = current.next
                    current.next = new_node
                    if self.tail == current:
                        self.tail = new_node
                    return
                current = current.next

    def remove(self, data):
        """ Finds Node in LL with input data and removes from LL
        :param data: data attribute of Node to be removed
        :return: none
        """

        # account for empty list
        if self.head and self.head.data == data:
            # account for case where data sought is head of list
                self.head = self.head.next
                return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                    current.next = current.next.next
                    return
                current.next = current.next.next
                return
            else:
                current = current.next


class LLNode(object):
    """ node of a linked list, pointer to next"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """ make it pretty
        :return: string
        """

        return "<LLNode data=%s>" % (self.data)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
