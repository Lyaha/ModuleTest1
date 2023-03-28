
def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)

if __name__ == '__main__':
    file_path = 'sample_text.txt'
    word_count = count_words(file_path)
    print(f'Total words: {word_count}')