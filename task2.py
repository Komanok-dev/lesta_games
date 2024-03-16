# FIFO (first in first out) queue

from collections import deque


# Time Complexity O(1)
# Space Complexity O(1)
class Fifo_deque():
    def __init__(self) -> None:
        '''Initialize empty queue.'''
        self.queue = deque()
    
    def push(self, value) -> None:
        '''Push value to queue.'''
        self.queue.append(value)

    def pop(self) -> any:
        '''Release value from queue. If stack is empty returns None.'''
        return self.queue.popleft() if len(self.queue) > 0 else None


# Time Complexity O(1)
# Space Complexity O(n)
class Fifo_standard():
    def __init__(self) -> None:
        '''Initialize empty queue.'''
        self.queue = []
    
    def push(self, value) -> None:
        '''Push value to queue.'''
        self.queue.append(value)

    def pop(self) -> any:
        '''Release value from queue. If stack is empty returns None.'''
        return self.queue.pop(0) if len(self.queue) > 0 else None


'''
The deque implemented as a doubly-linked list,
which allows to insert and removing elements
from both ends of the queue at constant time O(1)

When you use standard list.pop(0) it takes first element,
but then it shifts all other elements to the left one by one,
it takes O(n) time


1 2 3 4 5  |  _ 2 3 4 5  |  2 3 4 5
^          |    < < < <  |

'''
