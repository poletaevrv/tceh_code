# import tkinter
score = 0
count = 0
while True:
        q1 = str.lower(input('Как называется, изучаемый язык программирования?: '))
        if q1 == 'python' or q1 == 'питон':
            print('Это правильный ответ!')
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q1)
            count = count + 1
            break
while True:
        q2 = str.lower(input('Год последнего обновления Python 2.7?: '))
        if q2 == '2015':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q2)
            count = count + 1
            break
            # continue
while True:
        q3 = str.lower(input('Год выхода Python 3?: '))
        if q3 == '2008':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q3)
            count = count + 1
            break
while True:
        q4 = str.lower(input('Специальный тип данных для обозначения "ничего","пустоты"?: '))
        if q4 == 'none':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q4)
            count = count + 1
            break
while True:
        q5 = str.lower(input('Cтандарт кодирования символов, позволяющий представить знаки почти всех письменных языков в виде числовых кодов.?: '))
        if q5 == 'unicode':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q5)
            count = count + 1
            break
while True:
        q6 = str.lower(input('Как обозначается цикл с предусловием?: '))
        if q6 == 'while':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q6)
            count = count + 1
            break
while True:
        q7 = str.lower(input('Как обозначается перебирающие циклы?: '))
        if q7 == 'for':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q7)
            count = count + 1
            break
while True:
        q8 = str.lower(input('Как в Python обозначается истина?: '))
        if q8 == 'true':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q8)
            count = count + 1
            break
while True:
        q9 = str.lower(input('Как в Python обозначается ложь?: '))
        if q9 == 'false':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q9)
            count = count + 1
            break
while True:
        q10 = str.lower(input('Как зовут преподавателя?: '))
        if q10 == 'никита':
            print('Это правильный ответ!')   
            count = count + 1
            score = score + 1
            break
        else:
            print('"%s" не правильный ответ.' % q10)
            count = count + 1
            break
print('Вы ответили правильно на {} из {} вопросов.' .format (score, count))
