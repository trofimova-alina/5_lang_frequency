import re
from collections import Counter

WORDS_COUNT = 10


def load_data(filepath):
    with open(filepath, 'r') as raw_content:
        data = raw_content.read()
    return data


def get_most_frequent_words(text):
    wordlist = re.findall(r'\w+', text.lower())
    return Counter(wordlist).most_common(WORDS_COUNT)


if __name__ == '__main__':
    data = load_data('test.txt')
    print(get_most_frequent_words(data))
