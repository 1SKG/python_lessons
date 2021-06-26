# Коллекции (контейнеры ) 
#  Класс обьекта:

#1. Список (list)

# Создание пустого списка 

my_list = []
my_list = list()

# Добавлени я обьекта (элемента) в список 
my_list.append(100)
my_list.append(3.14)
my_list.append("string")
my_list.append([10, 20, 30])

# print(my_list)

# Чтение значений элемента
# Прямая индесакция (положительная)
# Обратная индесакция
#  В квадратную скобу указываем индекс элемента
el = my_list[3]
el = my_list[3][1]

el = my_list[-1]
# Замена значение элемента 

my_list[0] = 2000

#  Удаление элемениа по значанию 
# my_list.remove(3.14)

# Удаление по индексу
del my_list[-1]

# Срез списка

s = "hello, world"
my_list = list(s)

my_slice = my_list[2:]
my_slice = my_list [2:5]

print(my_list)
print(my_slice)