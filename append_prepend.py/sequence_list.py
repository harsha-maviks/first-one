class Sequence:
    def __init__(self):
        self._items = []

    # Requirement 1: support multiple datatypes (duplicates allowed)
    def add(self, item):
        """Adds an item to the sequence, allowing duplicates."""
        self._items.append(item)

    def get(self, index):
        """Retrieves the item at the specified 0-based index."""
        return self._items[index]

    def count(self, item):
        """Returns the total number of occurrences of the given item."""
        return self._items.count(item)

    def __len__(self):
        """Enables len(seq) syntax to return the total count of items."""
        return len(self._items)

    # Requirement 2: front and back insertion
    def append(self, item):
        """Appends an item to the end (back insertion)."""
        self._items.append(item)

    def prepend(self, item):
        """Inserts an item at the beginning (front insertion)."""
        self._items.append(None)                      # make room at the end
        for i in range(len(self._items) - 1, 0, -1):  # shift items one place right
            self._items[i] = self._items[i - 1]
        self._items[0] = item                         # put the new item at the front