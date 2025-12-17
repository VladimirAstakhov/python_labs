# Лабораторная работа №10 по Python

## Структуры данных: Stack, Queue, Linked List и бенчмарки

## Краткая теоритическая справка
## Stack
```
Стек — линейная структура данных, работающая по принципу LIFO
(последний добавленный элемент извлекается первым).

Операции:
push — O(1)
pop — O(1)
peek — O(1)
```
## Queue
```
Очередь — линейная структура данных, работающая по принципу FIFO
(первый добавленный элемент извлекается первым).

Операции (на базе deque):
enqueue — O(1)
dequeue — O(1)
peek — O(1)

```
## Node
```
Node — элемент связного списка, содержащий значение и ссылку
на следующий узел.

Доступ к значению — O(1)
Переход к следующему узлу — O(1)

```
## Linked list
```
Односвязный список — структура данных, состоящая из узлов,
связанных ссылками.

Операции:
append — O(1)
prepend — O(1)
insert — O(n)
доступ по индексу — O(n)

```

## Задание A - Stack, Queue

## Код в structures.py

```
При попытке вернуть/удалить элемент из пустой структуры возращается None
```

```python
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
```



## Задание B - Linked List

```
В Node добавлено поле tail (последний элемент)
```


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        self.tail = None

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self._size += 1
            if self.tail is None:
                self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):

        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

```

## Простые тесты работы структур

## Код в src/lab10/test.py

```python
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList, Node


print("Стек")
stack = Stack()
for i in range(10):
    stack.push(i)

while not stack.is_empty():
    print("peek =", stack.peek(), "pop =", stack.pop())

print("Очередь")

queue = Queue()
for i in range(10):
    queue.enqueue(i)

while not queue.is_empty():
    print("peek =", queue.peek(), "dequeue =", queue.dequeue())

print("Односвязный список")

lst = SinglyLinkedList()

# append
for i in range(3):
    lst.append(i)
print("after append:", list(lst))

# prepend
lst.prepend(-1)
print("after prepend:", list(lst))

# insert
lst.insert(2, 99)
print("after insert:", list(lst))

# insert at edges
lst.insert(0, -2)
lst.insert(len(lst), 3)
print("after edge inserts:", list(lst))

# checks
print("size:", len(lst))
print("head:", lst.head.value)
print("tail:", lst.tail.value)


```
<img width="691" height="890" alt="test" src="https://github.com/user-attachments/assets/394e2931-a371-40ea-93be-0bb9b9d76cb7" />



## Benchmark

## Код в src/lab10/benchmark.py 

```python
import time
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList, Node
import random
N = 10000

# Stack
start = time.perf_counter()
s = Stack()
for i in range(N):
    s.push(i)
for i in range(N):
    s.pop()
print("Stack:", time.perf_counter() - start)

# Queue
start = time.perf_counter()
q = Queue()
for i in range(N):
    q.enqueue(i)
for i in range(N):
    q.dequeue()
print("Queue:", time.perf_counter() - start)

# Linked list append
start = time.perf_counter()
lst = SinglyLinkedList()
for i in range(N):
    lst.append(i)
print("LinkedList append:", time.perf_counter() - start)

# Linked list insert
start = time.perf_counter()
lst = SinglyLinkedList()
for i in range(N):
    lst.insert(i//2,i)
print("LinkedList insert:", time.perf_counter() - start)


```
<img width="461" height="199" alt="benchmark" src="https://github.com/user-attachments/assets/e9a8d274-bf6b-4e4f-b678-bc444ea7f422" />


```
Есть смысл сравнивать append в linked list и аналогичные операции в stack и queue.
Мы видим, что в stack и queue эти операции работают быстрее, тк:
1) узлы односвязного списка хранятся в памяти разрозненно, что увеличивает время
2) list и deque (на которых реализованы stack и queue) реализованы на C, что увеличивает оптимизацию

Операция insert в linked list работает сильно дольше из-за асимптоики O(n)
```



