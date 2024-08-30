class SimpleQueue:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def Enqueue(self, item):
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            raise Exception("Queue is full")

    def display(self):
        return self.queue

    def Dequeue(self):
        del self.queue[0]

    def update(self, old_item, new_item):
        if old_item in self.queue:
            index = self.queue.index(old_item)
            self.queue[index] = new_item
        else:
            raise Exception("Item not found in queue")

    def count(self):
        return len(self.queue)

    def peak(self, item):
        return item in self.queue

    def sort(self):
        self.queue.sort()

    def IsEmpty(self):
        return len(self.queue) == []
    
    def IsFull(self):
        return len(self.queue) == self.size

def simp_que(size: int = 5):
    return SimpleQueue(size)