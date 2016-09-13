import re


def load_data(filepath):
    with open(filepath, 'r') as raw_content:
        data = raw_content.read()
    return data


def get_most_frequent_words(text):
    wordlist = re.findall(r'\w+', text)
    dict_of_words = {}
    for current_word in wordlist:
        if current_word in dict_of_words.keys():
            continue
        else:
            dict_of_words[current_word] = wordlist.count(current_word)
    return dict_of_words


if __name__ == '__main__':
    data = load_data('test.txt')
    list_of_words = list(get_most_frequent_words(data).items())
    list_of_words.sort(key=lambda item: item[1], reverse=True)
    for i in range(0, 10):
        print(list_of_words[i])
