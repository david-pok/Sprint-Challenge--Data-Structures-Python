class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def __repr__(self):
        return f'STORAGE>> {self.storage}'

    def append(self, item):
        if self.current >= self.capacity:
            self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):
        return [x for x in self.storage if x is not None]


rb = RingBuffer(5)
print(rb)
