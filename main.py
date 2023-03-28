import re
def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)

def count_sentences(filename):
    with open(filename, "r") as file:
        text = file.read()
        sentences = re.split(r'[.!?]+|\?', text)
        if sentences[-1] == '':
            sentences = sentences[:-1]
        return len(sentences)

if __name__ == '__main__':
    file_path = 'sample_text.txt'
    word_count = count_words(file_path)
    sentences_count = count_sentences(file_path)
    print(f'Total words: {word_count}')
    print(f'Total sentences: {sentences_count}')
