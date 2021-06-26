# Логические операции
#  Операции  сравнения

z = 3
w = 2

#  Операция "Равно"
# Мы спрашиваем " значение z равно значению w?"
# ответ будет присоен переменной result
result = z == w

# Операция -не равно 

result = z != w

#   Операция меньше

result = z < w

#  Операция больше
result = z > w

# Операция меньше либо равно 

result = z <= w

# Операция больше либо равно

result = z >= w

# 



# чистые логические операции



var_1 = True
var_2 = False

# Оператор не - not, инвервция 

result = not var_1

# Оператор И (AND)
# Возвращает True только тогда ,когда обе переменных True

result = var_1 and var_2

# Оператор Или -OR
# Возвращает False только тогда, обе переменых являются False

result = var_1 or var_2


# print(result)

# Условные Операторы

# Оператор if если
# if False:
#     w = "Hello"
#     print(w)

# z = 10

# if z < 3:
#     print("menshe")
# else:
#     print("ne menshe")

# оператор elif

v = 'D'

if  v == 'B':
    res = "literal B"
elif v == 'A':
    res = "Literal A"
elif v == 'D':
    res = "Literal D"
elif v == 'W':
    res = "literal W"
else: 
    res = "neponytnhu* mne slovo:("

# print(res)

# *Пример (Термостас) *
# Текущая температура помещения 
current_temp = 25

# Заданое значение диапозон температур 
min_temp = 10
max_temp = 25

# параметр "Ludi est /net"
h = True

# Logiga termostata
if current_temp <min_temp and  not h:
    print(f"vkluchon nagrev do {min_temp}")
elif current_temp <max_temp and h:
    print(f"vluchen nagrev do {max_temp}")
    
else:
    print("nagrev vukluchen")


