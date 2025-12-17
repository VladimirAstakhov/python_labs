from collections import deque
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:

        if not self._data:
            return True
        return False

class Queue:
    def __init__(self):

        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            return None
        return self._data.popleft()

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data