
class orderedSequence:
    def __init__(self):
        self._items = []

    # Requirement 1: support multiple datatypes (duplicates allowed)
    def add(self, item):
        """Adds an item to the end, allowing duplicates."""
        self._items.append(item)

    def get(self, index):
        """Retrieves the item at the specified 0-based index."""
        return self._items[index]

    def count(self, item):
        """Returns the number of occurrences of the given item."""
        return self._items.count(item)

    def __len__(self):
        return len(self._items)

    # Requirement 2: front and back insertion
    def append(self, item):
        self._items.append(item)

    def prepend(self, item):
        self._items.insert(0, item)

    # Requirement: mutable
    def set_at(self, index, value):
        self._items[index] = value

    # Requirement 5: ordered sequence
    def to_list(self):
        """Returns a copy of the items in their current order."""
        return list(self._items)
