"""
Задание 3 [Python]
Используя любой из известных вам методов, найдите все элементы в списке,
удовлетворяющие следующим условиям:

Первая буква должна быть заглавной, за которой следует нижнее подчеркивание
Где-то в середине слова должно присутствовать одно из трех car, или bus,
или truck
Заканчиваться слово должно подчеркиванием и тремя любыми цифрами.
Например: A_super_bus_driver_001 или B_sport_car_091

"""

import re


def search_value_elements(my_list):
    pattern = (r'[A-Z][_].*(car|bus|truck).*[_]\d{3}')
    new_list = []
    for element in my_list:
        if re.fullmatch(pattern, element):
            new_list.append(element)
    print(new_list)


my_list = ['A_super_bus_driver_001', 'B_sport_truck_091', 'gfвалf',
           'sd', 'car', 'acara', 'B_sport_csar_091', 'Bsport_car_093d1',
           'B_sport_car_091', '55ddd']

search_value_elements(my_list)