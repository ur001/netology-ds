# coding: utf8
"""
Найти все слова которые можно составить из слова «ростелеком»
python match_words.py [слово] [словарь]
python match_words.py ростелеком sociation_org.txt
Доступные словари: sociation_org.txt, efremova_cleaned.txt
"""

def get_dict_iterator(file_name, min_length=2):
    """
    Возвращает итератор по файловому словарю. 
    Формат: на каждой строчке по слову
    """
    with open(file_name, 'r') as dict_file:
        for word in dict_file:
            word = word.strip().lower()
            if len(word) >= min_length:
                yield word


def get_word_matcher(word):
    """
    Возвращает функцию для проверки можно ли составить тестовое слово test_word 
    из букв указанного слова word

    >>> matcher = get_word_matcher('тест')
    >>> matcher('сет')
    True
    """
    from collections import Counter
    _letter_couner = Counter(word.lower())

    def match(test_word):
        letter_couner = _letter_couner.copy()
        for letter in test_word:
            if letter_couner[letter] > 0:
                letter_couner[letter] -= 1
            else:
                return False
        return True

    return match


if __name__ == "__main__":
    import sys
    word = sys.argv[1] if len(sys.argv) > 1 else 'ростелеком'
    dict_file_name = sys.argv[2] if len(sys.argv) > 2 else 'sociation_org.txt'

    word_matcher = get_word_matcher(word)
    dict_iterator = get_dict_iterator(dict_file_name, 3) 

    for word in filter(word_matcher, dict_iterator):
        print(word)