# Плюсы:
# Быстрые push и pop O(1), тк обращаемся только к концу.
# Предсказуемая память, тк нет выделения нового и не перемещаются объекты внутри.
# Минусы:
# Нельзя динамически расширять размер.

class RingBufferArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, value):
        if self.size == self.capacity:
            raise OverflowError("Buffer full")

        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Buffer empty")

        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value
    
    def get(self):
        return self.buffer[self.head]
    
    def get_size(self):
        return self.size

# Плюсы:
# Тоже быстрый тк deque реализован на C
# Удобнее при написании и использлованиии
# Минусы:
# Меньше контроля над внутренней структурой 

from collections import deque

class RingBufferDeque:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def push(self, value):
        if len(self.buffer) == self.capacity:
            raise OverflowError("Buffer full")
        self.buffer.append(value)

    def pop(self):
        if not self.buffer:
            raise IndexError("Buffer empty")
        return self.buffer.popleft()
    
    def get(self):
        return self.buffer[len(self.buffer)-1]
    
    def get_size(self):
        return self.capacity


def CheckRingBufferArray():
    print("Array buffer:")
    buf = RingBufferArray(5)
    buf.push(1)
    buf.push(2)
    print("Size:", buf.get_size())
    buf.push(3)
    buf.push(4)
    print(buf.get())
    print(buf.pop())
    print("Size:", buf.get_size())
    print(buf.get())

def CheckRingBufferDeque():
    print("\nDeque buffer:")
    buf = RingBufferDeque(5)
    buf.push(1)
    buf.push(2)
    print("Size:", buf.get_size())
    buf.push(3)
    buf.push(4)
    print(buf.get())
    print(buf.pop())
    print("Size:", buf.get_size())
    print(buf.get())

CheckRingBufferArray()
CheckRingBufferDeque()