"""
Задание 1 [Python]
Разработайте программный код, предназначенный для выявления
слова с максимальной длиной из предоставленного набора.
Реализуйте функцию, способную принимать переменное число
аргументов (слов для анализа).
Следуйте предложенному ниже шаблону.

def find_max_word( {words} ):
    result = None

    # сравнить длину всех слов
    # найти слово с максимальной длиной
    # вернуть это слово

    return result

max_word = find_max_word("pineapple", "polinomial", "equation")
"""


def find_max_word(*args):
    result = ''
    for arg in args:
        if len(arg) > len(result):
            result = arg

    return result


max_word = find_max_word("pineapple", "polinomial", "equation")

print(max_word)