#1

my_list = [10, 'Alla', True, None, (1, False, 'cat')]

for el in my_list:
    print(f'Тип {el} - {type(el)}')

#2

user_list = input('Enter elements separated by commas: ').split(',')
for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(user_list)


#3

#list
months = ['зима', 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень']
month = months.pop(int(input('Введите месяц в формате числа')) + 1)
print(month)

#dict
months = {
    1: ['Январь', ' зима'],
    2: ['Февраль', ' зима'],
    3: ['Март', ' весна'],
    4: ['Апрель', ' весна'],
    5: ['Май', ' весна'],
    6: ['Июнь', ' лето'],
    7: ['Июль', ' лето'],
    8: ['Август', ' лето'],
    9: ['Сентябрь', ' осень'],
    10: ['Октябрь', ' осень'],
    11: ['Ноябрь', ' осень'],
    12: ['Декабрь', ' зима']
}

key = int(input('Enter a month'))
print(','.join(months[key]))


#4

user_str = input('Enter a sentence separated by spaces: ')
user_list = user_str.split()

n = 0
for el in user_list:
    n += 1
    print(n, el[:10])

#5

my_list = [1, 2, 4, 3, 3, 8]
usr = int(input('Enter a number'))

my_list.append(usr)

new_list = sorted(my_list)
new_list.reverse()
print(new_list)




#6
count_items = int(input('Введите количество товаров'))
list_items = []

i = 1
while i <= count_items:
    name = input('Введите название товара')
    price = input('Введите цену товара')
    n = input('Введите количество товара')
    unit = input('Введите единицу измерения')

    dict = {'название': name, "цена": price, "количество": n, "ед": unit}
    tuple = (i, dict)
    list_items.append(tuple)
    i += 1

print(list_items)

print({
    'название': dict.get('название')
})