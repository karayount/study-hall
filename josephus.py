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


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def remove(self, node):
        if not self.head:
            return
        if node == self.head:
            self.head = None
            return
        current = self.head
        while current.next != node:

            current = current.next




class LLNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
