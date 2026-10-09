class MyList:
    def __init__(self):
        self._items = []

    # Requirement 3: add front / end / in-between
    def add_at(self, index, item):
        """Adds an item at the given index (0 = front, len = end)."""
        if not 0 <= index <= len(self._items):
            raise IndexError(f"Index {index} out of range (length {len(self._items)})")
        self._items.append(None)                          # make room at the end
        for i in range(len(self._items) - 1, index, -1):  # shift items right
            self._items[i] = self._items[i - 1]
        self._items[index] = item                         # place the new item

    def add_front(self, item):
        """Adds an item at the front."""
        self.add_at(0, item)

    def add_end(self, item):
        """Adds an item at the end."""
        self.add_at(len(self._items), item)

    def get(self, index):
        """Retrieves the item at the specified 0-based index."""
        return self._items[index]

    def __len__(self):
        return len(self._items)