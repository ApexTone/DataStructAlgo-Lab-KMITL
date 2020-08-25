class Stack:
    def __init__(self, items=None, cap=50):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.cap = cap

    def push(self, value):
        if not self.is_full():
            self.items.append(value)
        else:
            print('Stack is full')

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print('Stack is empty')
            return -1

    def peek(self):
        if not self.is_empty():
            return self.items[self.size()-1]
        else:
            print('Stack is empty')
            return -1

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() <= 0

    def is_full(self):
        return self.size() >= self.cap

    def __str__(self):
        return str(self.items)


