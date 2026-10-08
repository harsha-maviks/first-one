class OrderedList:
    def __init__(self):
        self.items = []

    def add(self, value):
        """Appends an element to the end (back insertion)."""
        self.items.append(value)

    def prepend(self, value):
        """Inserts an element at the beginning (front insertion)."""
        self.items.insert(0, value)

    def append(self, value):
        """Alias for add(); appends an element to the end."""
        self.items.append(value)

    def get(self, index):
        """Retrieves an element by its 0-based index."""
        return self.items[index]

    def __len__(self):
        """Returns the total number of elements in the list."""
        return len(self.items)