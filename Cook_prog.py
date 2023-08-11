# ЗАДАНИЕ 1

cook_book = {}
ingredients = []
ingr_dict = {}

with open ("Cook_book.txt", encoding = 'utf-8') as f:
    for line in f:
        dish = line.strip()
        count = int(f.readline())
        for ingr_line in range(count):
            ingr_name, quan, meas = f.readline().strip().split('|')
            ingredients.append({'product': ingr_name, 'quantity': quan, 'measure': meas})
            recipe = {dish : ingredients}
        blank_line = f.readline()
        cook_book.update(recipe)
    print(f'cook_book = {cook_book}')

# ЗАДАНИЕ 2


with open ("cook_book.txt", 'rt', encoding = 'utf-8') as f:
    for line in f:
        dish = line.strip()
        ingr_count = f.readline()
        for item in range(int(ingr_count)):
            mean = f.readline()
            prod, quan, meas = mean.strip().split('|')
            ingredients.append({'ingredient_name': prod, 'quantity': quan, 'measure': meas})
            dict = {dish: ingredients}
        lineread = f.readline()
        cook_book.update(dict)
    print(cook_book)
    def get_shop_list_by_dishes(person_count: int, dishes: list):
        shop_list = {}
        for dish in dishes:
            if dish in cook_book:
                for exist in cook_book[dish]:
                    if exist['ingredient_name'] in shop_list:
                        shop_list[exist['ingredient_name']]['quantity'] += (exist['quantity'] * person_count)
                    else:
                        shop_list[exist['ingredient_name']] = {'measure': exist['measure'],'quantity': (exist['quantity'] * person_count)}

get_shop_list_by_dishes(2, ['Сырники', 'Омлет'])










