# *** Функции ***

# встроеные функции ввода данных


# 1 Вариант. Функция, принимающая данные (Обладающая аргументами)

def func_1(arg_1): 
    s = arg_1 ** 2
    w = s + 10
    print(f"Результат: {w}")



 # Вызов функции

func_1(1000)

def func_2(a, b, c):
    res = a + b + c
    res += 200
    print(f"Вывод:  {res}")

#func_2(10, 5, 2)

 # Аргумент может иметь значение по умолчанию

def func_3(arg_1, arg_2=100):
    print(arg_1 *arg_2)

#func_3(20, 10)
#func_3(100)
#func_3(3.14)

# 2. вариант. Функция, возвращающая данные
def func_4(arg_1, arg_2):
    res = arg_1 + arg_2
    return res

#d = func_4(6, 5)
 
def func_5(x, y):
     res_1 = x * y
     res_2 = x / y
     return res_1, res_2, x
# Первый способ приема данных
d_1 = func_5(10, 2) 
# Второй способ приема данных
a, b, c = func_5(10, 2)

#print(d_1)
#print(d_1[0])

#print(a, b, c)
#print(b)



# Безымянные функции
# - Всегда обладают аргументами 
# - Всегда возвращает результат

# Пример 1. Лямбда внутри генератора списка
my_list =[(lambda arg_1: arg_1.upper())(i) for i in "Hello"]

# Привер 2. Словарь лямда вырожений
my_lamdas = {
    "*": lambda arg_1, arg_2: arg_1 * arg_2, 
    "+": lambda w, z,: w + z 
}
#print(my_list)
print(my_lamdas["+"](5, 2))
print(my_lamdas["*"](5, 2))
