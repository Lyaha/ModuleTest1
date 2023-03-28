import pytest
from main import count_words

def test_count_words():
    filename = "test_file.txt"
    with open(filename, "w") as file:
        file.write("Hello world!")

    assert count_words(filename) == 2

    with open(filename, "w") as file:
        file.write(
            "Hello world! This is a sample text file.")

    assert count_words(filename) == 8