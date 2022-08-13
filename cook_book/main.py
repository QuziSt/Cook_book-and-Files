# def start():
#     dishes = input('Введите названия блюд через пробел: ').split()
#     persons = input('Сколько человек?: ')
#     return dishes, persons
from pprint import pprint
def cook_dict():
    with open('recipes.txt', encoding='utf-8') as recipes:
        cook_book = {}
        while True:
            try:
                cook_book.setdefault(recipes.readline().strip(), [{'ingredient_name': stat[0],
                                                                   'quantity': int(stat[1]),
                                                                   'measure': stat[2].strip()}
                                                                  for stat in [recipes.readline().split(' | ')
                                                                  for _ in range(int(recipes.readline()))]])
                recipes.readline()
            except:
                break

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        if dish in cook_dict().keys():
            for i in cook_dict()[dish]:
                if i['ingredient_name'] in all_ingredients.keys():
                    all_ingredients[i['ingredient_name']]['quantity'] += i['quantity']*person_count
                else:
                    all_ingredients.setdefault(i['ingredient_name'], {'measure': i['measure'], 'quantity': i['quantity']*person_count})

    return all_ingredients


def start():
    dishes = input('Введите названия блюд через пробел: ').split()
    persons = int(input('Сколько человек?: '))
    get_shop_list_by_dishes(dishes, persons)


start()

