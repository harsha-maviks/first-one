class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class OrderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def get(self, index):
        for i, value in enumerate(self):
            if i == index:
                return value
        raise IndexError("index out of range")

    def count(self, value):
        return sum(1 for item in self if item == value)

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
