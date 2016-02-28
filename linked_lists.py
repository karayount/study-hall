class LinkedList(object):
    """ Linked list, pointers to head, tail"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def show_whole_list(self):
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
            while current != None:
                if current.data == data:
                    return current
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

consolis = LinkedList()
kara = LLNode("Kara")
consolis.head = kara
kevin = LLNode("Kevin")
kara.next = kevin
kyla = LLNode("Kyla")
kevin.next = kyla
chris = LLNode("Christina")
kyla.next = chris
nick = LLNode("Nicholas")
chris.next = nick
alison = LLNode("Alison")
nick.next = alison
dana = LLNode("Dana")
alison.next = dana
consolis.tail = dana



class DoublyLinkedList(object):
    """ linked list with head and tail """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def show_whole_list(self):
        """ displays entire list with print statements
        :return: none
        """

        current = self.head
        while current != None:
            print current
            current = current.next


class DLLNode(object):
    """ node of a doubly linked list, pointers to next and previous """

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        """ make it pretty
        :return: string
        """

        return "<DLLNode data=%s>" % (self.data)


younts = DoublyLinkedList()
steffen = DLLNode("Steffen")
doug = DLLNode("Doug")
sonja = DLLNode("Sonja")
kara = DLLNode("Kara")
anja = DLLNode("Anja")
younts.head = steffen
younts.tail = anja
steffen.next = doug
doug.prev = steffen
doug.next = sonja
sonja.prev = doug
sonja.next = kara
kara.prev = sonja
kara.next = anja
anja.prev = kara
