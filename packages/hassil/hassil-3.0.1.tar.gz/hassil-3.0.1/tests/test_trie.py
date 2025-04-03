from hassil.trie import Trie


def test_insert_find() -> None:
    """Test inserting and finding values in the trie."""
    trie = Trie()
    trie.insert("1", 1)
    trie.insert("two", 2)
    trie.insert("10", 10)
    trie.insert("twenty two", 22)

    text = "set to 10"
    results = list(trie.find(text))
    assert results == [(8, "1", 1), (9, "10", 10)]
    for end_pos, number_text, number_value in results:
        start_pos = end_pos - len(number_text)
        assert text[start_pos:end_pos] == number_text
        assert int(number_text) == number_value

    assert list(trie.find("set to 1, then *two*, then finally twenty two please!")) == [
        (8, "1", 1),
        (19, "two", 2),
        (45, "twenty two", 22),
    ]

    # Without unique, *[two]* and twenty [two] will return 2
    assert list(
        trie.find("set to 1, then *two*, then finally twenty two please!", unique=False)
    ) == [
        (8, "1", 1),
        (19, "two", 2),
        (45, "two", 2),
        (45, "twenty two", 22),
    ]

    # Test a character in between
    assert not list(trie.find("tw|o"))

    # Test non-existent value
    assert not list(trie.find("three"))

    # Test empty string
    assert not list(trie.find(""))


def test_multiple_values() -> None:
    """Test that we can insert multiple values for the same string."""
    trie = Trie()
    trie.insert("test", 1)
    trie.insert("test", 2)

    assert list(trie.find("this is a test")) == [(14, "test", 1), (14, "test", 2)]
