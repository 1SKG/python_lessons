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
# срез с приминением обратной инексации

my_slice = my_list[-2:-5:-1]

# Переворот списка 

my_slice = my_list [::-1]

# len() вовзращают длину (количество элементов) коллекция

# print(len(my_list))

# print(my_list)
# print(my_slice)

# * кортеж (tuple)**

# неизменяемая (imutable) коллекция

# Создание кортежа

my_tuple = (10, 20, 30, 40, 50)


# my_tuple[0] = 100


# print(my_tuple)

# Чтение значения элементов кортежей
# print(my_tuple[0])

# Срез 
# print(my_tuple[2:1])

# Словарь (мутабельный)

#  Пара "Ключ значение"
#  {Ключ_1:значение_1, ключ_2:Значение_2}

my_dict = {10:3.14, "abc":[1,2,3]}


# print(my_dict)

# Чтение значений 

# print(my_dict[10])
# print(my_dict["abc"])

# data0 = {"name":"John", "age":34, "id":123.5}
# data1 = {"name":"Luk",  "age":32, "id":123.2}
# data2 = {"name":"Rock", "age":31, "id":121.2}

# total_data ={"p0":data0, "p1":data1, "p2":data2}

# print(total_data ["p2"]["id"] )

# Изменение значений
my_dict["abc"] = "string"


# Особенность словаря ,при присвоеннием нового значения по не существующему ключу
# Сохдается новая пара 
my_dict['A'] = 777

# удаление пары (элемента)
del my_dict[10]

# print(my_dict)
# Обновление данных
data0 = {"name":"John", "age":34, "id":123.4}

data0.update ({"age":35, "id":300, "w":140.5})

# Множетсво (set)

# Особенности 
#  Неупорядочный тип коллекции (Обьекта)
#  Автоматом удаляет дублирующие обьекты

# Создание пустого множества

my_set =  set()

# Создание наполненного множетсва
my_set = {10, 20, 30}

# Добавление элемента
my_set.add(123)

# Когда добавляется значение, которо уже есть во множетсве, то оно удаляется либо не добавляется

my_set.add(30)

# удаленеи элемента
my_set.remove(20)
# my_set.remove(40)

my_set.discard(123)

#  Дано Два множества 

w = {"a", "b", "c", 'd'}

z = {'b', 'c', 'q'}

#  Обьединение 

f = w.union(z)
f = w | z

#  Пересечение 
f = w.intersection(z)
f = w & z

# Разность 

f = w.difference(z)
f = z.difference(w)
f = w.symmetric_difference(z)
#  коротакая запись difference
f = w - z
#  самостоятольно по изучать оставшийся методы
#  Рассмотреть модуль collections
print(f)


