#1 Позиционные аргументы

def division(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        result = round(num_1/num_2, 2)
    except ValueError:
        return 'Введено некорректное значение!'
    except ZeroDivisionError:
        return 'Деление на ноль запрещено!'
    return result

print(division(input('Введите первое число: '), input('Введите второе число: ')))


#1.2 На мой взгляд данная конструкция работает эффективнее, т.к. исключения срабатывают сразу после введения некорректного значения,
# а не после введения двух значений

def division():
    try:
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе число: '))
        result = round(num_1/num_2, 2)
    except ValueError:
        return 'Введено некорректное значение!'
    except ZeroDivisionError:
        return 'Деление на ноль запрещено!'
    return result

print(division())


#2.1

def user(first_name, last_name, year_of_birth, city, email, phone_number):
    print(f'Имя: {first_name}, Фамилия: {last_name}, Год рождения: {year_of_birth}, '
          f'Город проживания: {city}, Email: {email}, Телефон: {phone_number}')

user(first_name='Kate', last_name='Jons',
     year_of_birth=1993, city='London',
     email='kate@gmail.com', phone_number=7876943)

#2.2

def user(**kwargs):
    return ' '.join(kwargs.values())

print(user(first_name=input('Имя: '), last_name=input('Фамилия: '),
     year_of_birth=input('Дата рождения: '), city=input('Город проживания: '),
     email=input('email: '), phone_number=input('Телефон: ')))


#3

def my_func(arg_1, arg_2, arg_3):
    my_list = list(map(float, [arg_1, arg_2, arg_3]))
    max_num_1 = max(my_list)
    my_list.remove(max_num_1)
    max_num_2 = max(my_list)
    return max_num_1 + max_num_2

print(my_func(input(), input(), input()))


#4.1

def my_func(x, y):
    return x ** y

print(my_func(x, y))


#4.2

def my_func(x, y):
    n = 1
    x_1 = 1
    while n <= abs(y):
        x_1 = x_1 * x
        print(x_1)
        n += 1
    return 1/x_1

print(my_func(0.5, -2))

#5

total_sum = 0

while True:
    user_str = input('Введите числа через пробел: ')
    user_str_as_list = user_str.split(' ')
    number_list = []
    for el in user_str_as_list:
        int_el = int(el)
        number_list.append(int_el)
    print(number_list)

    if input('Нажмите Enter, чтобы посчитать сумму чисел') != '':
        break
    number_list_sum = sum(number_list)
    print(f'Cумма чисел на текущей итерации: {number_list_sum}')
    total_sum += number_list_sum


    if input('Если хотите завершить программу, введите stop и посчитать общую сумму') == 'stop':
        break

print(f'Общая сумма: {total_sum}')



#Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.



#6

def my_func(text):
    return(text.capitalize())

print(my_func())


#7.1

def my_func(user_str):
    return user_str.title()

print(my_func(input('Введите слова через пробел')))


#7.2

def my_func(user_str):
    user_str_as_list = user_str.split(' ')
    new_list = []
    for el in user_str_as_list:
        el_cap = el.capitalize()
        new_list.append(el_cap)
        cap_words = (' '.join(new_list))
    return cap_words

print(my_func(input('Введите слова через пробел')))
