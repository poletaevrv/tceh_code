# Задача 1
n1 = input('Введите число: ') 
p2 = input('Введите степень: ') 
print (int(n1) ** int(p2))

# Задача 1(2)
n1 = int(input('Введите число: ')) 
p2 = int(input('Введите степень: ')) 
 
 
def func_1(x, y): 
    return x ** y 

print(func_1(n1, p1)) 

# Задача 2
# Функция принимает от пользователя два значения и ищет их НОК 
 
 
def nok(a, b):
	m = a * b
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return m // (a + b)

while 1:
	try:
		x = int(input('a='))
		y = int(input('b='))
		print ('NOK: ', nok(x, y))
	except:
		break


# Задача 3
# Написать функцию, которая принимает список, и возвращает словарь в формате: "тип данных: количество объектов" count_types([1, 4, 'd']) -> {<class 'int'>: 2, <class 'str'>: 1}

list1 = [1, 'xcxcc', 3, 4.13, ]
def list_to_dict(list1): 
    dict_type = {} 
    for item in list1: 
        if type(item) not in dict_type: 
            dict_type[type(item)] = list1.count(item)
    return dict_type 
print('Типы данных в списке {}: '.format(list1)) 

 
print(list_to_dict(list1)) 

# Задача 4
# Написать функцию, которая принимает два словаря, сравнивает их ключи, выдает в консоль сколько у них общих ключей
dict_1 = {1: 'ываы', 2: 'rty', 3: 'sr'} 
dict_2 = {4: 'sr', 7: 'ываы', 3: 789} 
 
 
print('Сколько общих ключей в словарях:') 
print(dict_1) 
print(dict_2) 

 
def count_keys(dict_1, dict_2): 
	count = 0 
	for key1 in dict_1: 
		for key2 in dict_2: 
			if key1 == key2: 
				count += 1 
	return count 

 
print('Общих ключей - {}'.format (count_keys(dict_1, dict_2))) 

# Задача 5
# Написать функцию, которая принимает любое количество аргументов, 
# должна вернуть список типов, принятых аргументов find_types(1, 's', []) -> [<class 'int'>, <class 'str'>, <class 'list'>]

def find_types(*n): 
 	list_types = [] 
 	for i in n: 
 		list_types.append(type(i)) 
 	return list_types 
 	 
print('Список типов:') 
print(find_types(1, 2, 5, 'adfd', [1, 3, 4], {'d': 'd', 'f': 'f'}, 5, 6)) 



# Задача 6
# Написать функцию, которая принимает на вход список списков (матрицу)  
# и выводит ее в виде матрицы (один ряд на одной строке) в консоль 

matrix1 = [ 
[1, 2, 3, 4], 
['a', 'b', 'c', 'd'], 
[66, 77, 88, 99] 
 ] 

 
def matrix_print(matrix): 
	for row in matrix: 
		print(row) 
 
print('Матрица:') 
matrix_print(matrix1) 

# Задача 7 
# Написать функцию, которая принимает любое количество  
# аргументов - списков, она должна возвращать 
# список из всех объектов списков, но каждый объект  
# должен быть уникальным  

# join_lists([1, 2], ['a', 2], ['c', 1]) -> [1, 2, 'a', 'c'] 
 
l1 = [1, 2] 
l2 = ['a', 2] 
l3 = ['c', 1] 

def join_lists(*lists): 
	common_list = [] 
	for raw in lists: 
		for element in raw: 
			common_list.append(element)
	return list(set(common_list))
	 
print('Уникальные объекты:') 
print(join_lists(l1, l2, l3)) 
























