import pickle

from time import time
from datetime import datetime

import functools

class BufferIsEmpty(Exception):
    pass

class BufferIsFull(Exception):
    pass

class CircularBuffer:

    def __init__(self, capacity=10):

        self.capacity = capacity
        self.buf = [None] * capacity

        self.head = -1
        self.tail = capacity

        self.size = 0

        self._index = 0
        self._elem = None

    def __len__(self):

        if self.tail >= self.head:
            return self.tail - self.head

        return self.capacity - self.head - self.tail

    def __iter__(self):

        self._elem = self.tail 

        return self

    def __next__(self):

        if self._index == self.capacity:
            self._index = 0
            self._elem = None

            raise StopIteration

        ret = self.buf[self._elem]
        self._elem = (self._elem + 1) % self.capacity

        self._index += 1

        return ret

    def push_front(self, val):

        if self.size == self.capacity:
            raise BufferIsFull
        
        self.head = (self.head + 1) % self.capacity
        self.buf[self.head] = val

        if self.size < self.capacity:
            self.size += 1

    def push_back(self, val):

        if self.size == self.capacity:
            raise BufferIsFull

        self.tail = (self.tail - 1) % self.capacity
        self.buf[self.tail] = val
        
        if self.size < self.capacity:
            self.size += 1

    def pop_front(self):

        if self.size == 0:
            raise BufferIsEmpty

        ret = self.front()
        
        self.buf[self.head] = None

        self.head = (self.head - 1) % self.capacity
        self.size -= 1

        return ret

    def pop_back(self):

        if self.size == 0:
            raise BufferIsEmpty

        ret = self.back()
        
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1

        return ret

    def front(self):

        return self.buf[self.head]

    def back(self):

        return self.buf[self.tail]

def timer(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):

        t1 = time()
        ret = func(*args, **kwargs)
        t2 = time() - t1

        print(f"{func.__name__} has elapsed in: {t2:.3f} seconds")

        return ret

    return wrapped

def log(depth):
        
    def _log(func):

        @functools.wraps(func)
        def wrapped(*args, **kwargs):

            ret = func(*args, **kwargs)
            if depth == 1:
                print(f"{func.__name__} is called: \n\t"
                    f"{datetime.now():%A, %d.%m.%Y, %H.%M.%S} \n")

            if depth == 2:
                print(f"{func.__name__} is called: \n\t"
                    f"{datetime.now():%A, %d.%m.%Y, %H.%M.%S}")
                print(f"\twith args:\n\t\t{args} \n")
                print(f"\twith kwargs:\n\t\t{kwargs}")
                print(f"\twith ret:\n\t\t{ret}")

            return ret

        return wrapped

    return _log

@timer
def load_buffer():
    with open("data.pickle", "rb") as f:

        data = pickle.load(f)
        return data

@timer
def save_buffer(buf):
    with open("data.pickle", "wb") as f:

        pickle.dump(buf, f)

def printBuf(buf):

    for i in buf:
        print(i)

def main():

    buf = CircullarBuffer(4)

    buf.push_front(1)
    buf.push_back(2)
    buf.push_front(3)
    buf.push_front(4)
    printBuf(buf)

    save_buffer(buf)

    new_buf = load_buffer()

    printBuf(new_buf)

if __name__ == "__main__":
    main()
