"""Задание 2 [Python]
У вас есть список my_list с разным набором слов.
Также имеется словарь my_dict с категориями fruit (фрукты) и
vegetables (овощи).
Задача - заменить в списке my_list все овощи и фрукты на альтернативные
из словаря (в соответствии с их принадлежностью
определенной категории).
Причем фрукт/овощь не может быть заменен на такой же (например если
вы замените apple на apple - это будет не правильно)

Например, список ['apple', 'tomato', 'car'], должен быть заменен
на нечто вроде ['blueberry', 'potato', 'car']. Обратите внимание
что car ни на что не заменилось, т.к. не относится
ни к одной из категорий словаря myDict.

my_dict = {"fruit" : ["apple", "blueberry", "pineapple"], "vegetable" :
["broccoli", "potato", "tomato"]}

my_list = ["maya", "apple", "potato", "blueberry", "laptop", "icecream",
"tomato", "candy"]
"""

import random


def change_food(my_dict, my_list):
    for i in range(len(my_list)):
        for d in my_dict.values():
            if my_list[i] in d:
                local_d = list(d)
                local_d.remove(my_list[i])
                my_list[i] = random.choice(local_d)

    print(my_list)


my_dict = {"fruit": ["apple", "blueberry", "pineapple"],
           "vegetable": ["broccoli", "potato", "tomato"]}

my_list = ["maya", "apple", "potato", "blueberry",
           "laptop", "icecream", "tomato", "candy"]

print(my_list)
change_food(my_dict, my_list)