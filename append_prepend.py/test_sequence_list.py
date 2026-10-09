from maintain_order import orderedSequence


def test_support_multiple_datatypes():
    """Requirement 1 Test"""
    collection = orderedSequence()

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
    collection = orderedSequence()

    collection.add(10)           # [10]
    collection.append("hello")   # [10, "hello"]

    collection.prepend(3.14)     # [3.14, 10, "hello"]
    collection.prepend(True)     # [True, 3.14, 10, "hello"]

    assert collection.get(0) is True
    assert collection.get(1) == 3.14
    assert collection.get(2) == 10
    assert collection.get(3) == "hello"
    assert len(collection) == 4


if __name__ == "__main__":
    test_support_multiple_datatypes()
    test_append_and_prepend()
    print("All requirements passed successfully")