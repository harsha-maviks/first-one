from sequence import CustomSequence

def test_allow_duplicates():
    seq = CustomSequence()

    # Add duplicate integers and strings
    seq.add(10)
    seq.add("apple")
    seq.add(10)        # Duplicate integer
    seq.add("apple")    # Duplicate string
    seq.add(10)        # Third duplicate integer

    # Verify total length reflects all duplicates
    assert len(seq) == 5

    # Verify items exist at separate indices
    assert seq.get(0) == 10
    assert seq.get(2) == 10
    assert seq.get(4) == 10
    assert seq.get(1) == "apple"
    assert seq.get(3) == "apple"

    # Verify duplicate count helper
    assert seq.count(10) == 3
    assert seq.count("apple") == 2

if __name__ == "__main__":
    test_allow_duplicates()
    print("Requirement 2 (Allow Duplicates) passed successfully!")