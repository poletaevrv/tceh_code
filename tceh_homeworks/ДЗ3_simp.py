#1
import random
s = [ValueError, TypeError, RuntimeError]

def rand_error_select(value):
    return(random.choice(value))

try: 
    raise rand_error_select(s) 
except ValueError: 
    print('Ошибка! ValueError') 
except TypeError: 
    print('Ошибка! TypeError') 
except RuntimeError: 
    print('Ошибка! RuntimeError') 

# либо:
import random

def rand_error_select():
    return(random.choice([ValueError, TypeError, RuntimeError]))

try: 
    raise rand_error_select() 
except ValueError: 
    print('Ошибка! ValueError') 
except TypeError: 
    print('Ошибка! TypeError') 
except RuntimeError: 
    print('Ошибка! RuntimeError') 

# 2
#Написать функцию, которая принимает на вход список, если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError 
def sort_list(value): 
    return_list = [] 
    try: 
        for i in value: 
            i = int(i) 
            return_list.append(i) 
        return_list.sort() 
        return return_list 
    except ValueError: 
        print('ValueError: список содержит не числовой элемент') 
 
a = [1,2,5,7,3,4,'qwerty'] 
sort_list(a) 

# 3
# Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь

def key_to_string(value): 
    new_dict_inf = {}
    for key, value in value.items(): 
        new_dict_inf.update({str(key):value})
    return new_dict_inf

my_dict = {1 : 4, 'd' : 'er', 2 : 'rr'}
new_dict = key_to_string(my_dict)

# 4
# Написать функцию, которая принимает список чисел и возвращает их произведение

def mult_list(value): 
    x = 1
    for i in value:
        x *= i 
    return print(x) # можно без print конечно

list_num = (1, 4, 2)
mult_list(list_num)

# 5
# Написать три функции: do_work, handle_success, handle_error. do_word(my_list, success_callback, error_callback) принимает на вход три аргумента: список, функцию 
# для обработки успеха и функцию для обработки ошибки. Ее задача проверить, что все значения в списке идут по-возрастанию. 
#Если все верно: вызываем success_callback, иначе: error_callback. 
# Функция handle_success пишет в консоль информацию об успешном выполнении. Функция handle_error выбрасывает ValueError

def handle_success(): 
    print('Проверка прошла успешно') 
 
def handle_error(): 
    try: 
        raise ValueError() 
    except ValueError:
        print('ValueError - Ошибка в значениях, список должен быть задан по возрастанию')
 
def do_work(my_list, success_callback, error_callback): 
    d_w = my_list[0]
    for i in my_list:
        if d_w < i + 1:
            d_w = i #+ 1
            success_callback() 
            
        else:
            error_callback()
            break  
    	 
#do_work((1,2,3,4,5,6), handle_success, handle_error) 
do_work([13,21,3,40,600,50], handle_success, handle_error) 

#5" После консультации с преподавателем)))

def handle_success(): 
    print('Проверка прошла успешно') 
 
def handle_error(): 
    raise ValueError('ValueError - Ошибка в значениях, список должен быть задан по возрастанию') 
        
def do_work(my_list, success_callback, error_callback): 
    d_w = my_list[0]
    for i in my_list:
        if d_w < i + 1:
            d_w = i #+ 1
        else:
            error_callback()
    success_callback()
    
        
    
	 
do_work((1,2,3,4,5,6), handle_success, handle_error) 
#do_work([13,21,3,40,600,50], handle_success, handle_error) 