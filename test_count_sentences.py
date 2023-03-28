import pytest
from main import count_sentences

def test_count_sentences():
    filename = "test_file2.txt"
    with open(filename, "w") as file:
        file.write("Hello world!")

    assert count_sentences(filename) == 1

    with open(filename, "a") as file:
        file.write(" This is a sample text file.")

    assert count_sentences(filename) == 2