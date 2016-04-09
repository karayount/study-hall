""" Implement a queue using two stacks
"""

class Stack(object):

    def __init__(self):
        self._stack_list = []

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self._stack_list[-1]

    def push(self, value):
        self._stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self._stack_list.pop()
            return value

    def is_empty(self):
        return len(self._stack_list) == 0


class doubleStackQueue(object):

    def __init__(self):
        self._stack_A = Stack()
        self._stack_B = Stack()

    def enqueue(self, item):
        self._stack_A.push(item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            while not self._stack_A.is_empty():
                self._stack_B.push(self._stack_A.pop())
            value = self._stack_B.pop()
            while not self._stack_B.is_empty():
                self._stack_A.push(self._stack_B.pop())
            return value

    def peek(self):
        if self.is_empty():
            return None
        else:
            while not self._stack_A.is_empty():
                self._stack_B.push(self._stack_A.pop())
            value = self._stack_B.peek()
            while not self._stack_B.is_empty():
                self._stack_A.push(self._stack_B.pop())
            return value

    def is_empty(self):
        return self._stack_A.is_empty()


test_queue = doubleStackQueue()
test_queue.enqueue(7)
test_queue.enqueue(8)
test_queue.enqueue(9)
test_queue.enqueue(10)
test_queue.enqueue(11)
test_queue.enqueue(12)
test_queue.enqueue(13)
test_queue.enqueue(14)
test_queue.enqueue(15)

print test_queue.dequeue()
print test_queue.dequeue()
print test_queue.dequeue()
print test_queue.peek()