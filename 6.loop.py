# Циклы 

#  Оператор цикла while
#  Перевод как "пока"

# Бесконечный цикл 

# while True:
    # print("Hello")

# Инструкция прерывание цикла 
# По дополнительному условию
g = 10

while g > 0:
    print(f"hello {g}")
    if g == 5:
        break
    # g = g - 1
    # короткая запись
    g -= 1

# Оператор цикла for

# 1.Читает значения из итерируемых обьектов по порядку
# 2.Значение присваивается в свою переменную
# 3.Выполняет блок кода своего тела

# my_list = [10,20,30,40,50,]

# for i in my_list[::-1]:
#     print(i)

# Генератор списка 

# создание списка чисел в диапозоне от 10 до 100 с шагом 10

num_list =[num for num in range(10, 100, 10)]
print(num_list)
    