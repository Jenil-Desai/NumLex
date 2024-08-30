class CircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.cnt = 0

    def add(self, item):
        if self.count == self.size:
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.cnt += 1

    def display(self):
        elements = []
        for _ in range(self.cnt):
            elements.append(self.queue[self.front])
            self.front = (self.front + 1) % self.size
        self.front = (self.front - self.cnt) % self.size
        return elements

    def delete(self):
        if self.cnt == 0:
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.cnt -= 1
        return item

    def update(self, old_item, new_item):
        for i in range(self.size):
            if self.queue[i] == old_item:
                self.queue[i] = new_item
                return
        raise Exception("Item not found in queue")

    def count(self):
        return self.cnt

    def search(self, item):
        for i in range(self.size):
            if self.queue[i] == item:
                return True
        return False

    def sort(self):
        sorted_queue = sorted(self.queue)
        self.queue = sorted_queue

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

def circ_que(size: int = 5):
    return CircularQueue(size)