class SimpleStack:
    def __init__(self, size: int):
        self.size = size
        self.stack = []

    def add(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            raise Exception("Stack is full")

    def display(self):
        return self.stack

    def delete(self):
        self.stack.pop()

    def update(self, old_item, new_item):
        if old_item in self.stack:
            index = self.stack.index(old_item)
            self.stack[index] = new_item
        else:
            raise Exception("Item not found in stack")

    def count(self):
        return len(self.stack)

    def search(self, item):
        return item in self.stack

    def sort(self):
        self.stack.sort()

    def isEmpty(self):
        return len(self.stack) == []
    
    def isFull(self):
        return len(self.stack) == self.size

def simp_stk(size: int = 5):
    return SimpleStack(size)