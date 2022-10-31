# Задача 1

name = input("Введите ваше имя")
age = int(input("Введите ваш возраст"))

print("Имя:", name, "Возраст:", age)



# Задача 2

time = int(input("Введите время в секундах"))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")



# Задача 3

n = input("Введите целое число")
n_1 = int(n)
n_2 = int(n + n)
n_3 = int(n + n + n)
sum = int(n_1 + n_2 + n_3)
print(sum)

# Или

n = input("Введите целое число")
print(int(n) + int(n + n) + int(n + n + n))



# Задача 4

number_init = int(input("Введите целое число"))
max_digit = 0
num = number_init

while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num = num // 10

print(f"Наибольшая цифра в числе {number_init}: {max_digit}")



# Задача 5,6

revenue = float(input("Введите выручку"))
expenses = float(input("Введите издержки"))
profit = revenue - expenses

if profit > 0:
    print(f"Прибыль: {profit}")
    print(f"Рентабельность {profit / revenue * 100:.1f}%")
    empl = int(input("Введите численность сотрудников фирмы"))
    profit_empl = profit//empl
    print(f"Прибыль на одного сотрудника: {profit_empl}")
elif profit == 0:
    print("Прибыль = 0")
else:
    print(f"Убыток: {profit}")



# Задача 7

a = float(input("Сколько км вы пробежали?"))
b = float(input("Ваш желаемый результат в км"))
n = 1

while a < b:
    print(f"{n}-й день: {a:.2f}")
    a = a + (a * 10 / 100)
    n = n + 1
    if a == b:
        break
print(f"На {n}-й день спортсмен достигнет результата - не менее {b}")
