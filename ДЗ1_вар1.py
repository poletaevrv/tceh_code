score = 0
while True:
		q1 = str.lower(input('Как называется, изучаемый язык программирования?: '))
		if q1 == 'python' or q1 == 'питон':
		    print('Это правильный ответ!')
		    score = score + 1
		    break
		else:
		    print('"%s" не правильный ответ. Попробуйте еще раз' % q1)
		    continue
while True:
		q2 = str.lower(input('Год последнего обновления Python 2.7?: '))
		if q2 == '2015':
		    print('Это правильный ответ!')   
		    score = score + 1
		    break
		else:
		    print('"%s" не правильный ответ. Попробуйте еще раз' % q2)
		    continue
print(score)