class CustomSequence:
    """
    Mutable, ordered sequence collection supporting mixed data types and duplicates.
    """
    def __init__(self):
        self._items = []

    def add(self, item):
        """
        [Requirement 1 & 2]: Append an item of any type to the collection.
        Duplicate values are explicitly permitted and stored at new indices.
        """
        self._items.append(item)

    def get(self, index: int):
        """Retrieve element by index."""
        if index < 0 or index >= len(self._items):
            raise IndexError("Index out of bounds")
        return self._items[index]

    def count(self, value) -> int:
        """Return the number of times a specific value appears in the collection."""
        return self._items.count(value)

    def __len__(self) -> int:
        return len(self._items)