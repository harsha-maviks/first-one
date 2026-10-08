from sequence import CustomSequence  # ✅ Correct import

def test_support_multiple_datatypes():
    """Requirement 1 Test"""
    collection = CustomSequence()

    collection.add(10)
    collection.add("hello")
    collection.add(3.14)
    collection.add(True)

    assert collection.get(0) == 10
    assert collection.get(1) == "hello"
    assert collection.get(2) == 3.14
    assert collection.get(3) is True

def test_append_and_prepend():
    """Requirement 2 Test: Front & Back Insertion"""
    collection = CustomSequence()

    # Back insertion using add and append
    collection.add(10)           # List: [10]
    collection.append("hello")   # List: [10, "hello"]

    # Front insertion using prepend
    collection.prepend(3.14)     # List: [3.14, 10, "hello"]
    collection.prepend(True)     # List: [True, 3.14, 10, "hello"]

    # Verify indices after front/back insertions
    assert collection.get(0) is True
    assert collection.get(1) == 3.14
    assert collection.get(2) == 10
    assert collection.get(3) == "hello"
    assert len(collection) == 4

if __name__ == "__main__":
    test_support_multiple_datatypes()
    test_append_and_prepend()
    print("All requirements passed successfully!")