from ordered_list import OrderedList

def test_append_and_prepend():
    collection = OrderedList()

    # Append to the back
    collection.add(10)
    collection.append("world")  # [10, "world"]

    # Prepend to the front
    collection.prepend("hello") # ["hello", 10, "world"]

    # Verify positions after insertions
    assert collection.get(0) == "hello"
    assert collection.get(1) == 10
    assert collection.get(2) == "world"
    assert len(collection) == 3

if __name__ == "__main__":
    test_append_and_prepend()
    print("Requirement 2 (Append & Prepend Elements) passed successfully!")