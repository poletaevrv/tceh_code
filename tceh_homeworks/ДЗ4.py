# 1
# Реализовать класс Person, у которого должно быть два публичных поля: age и name. Также у него 
# должен быть следующий набор методов: know(person), который позволяет добавить другого человека в список знакомых. 
# И метод is_known(person), который возвращает знает ли знакомы ли два человека
class Person(object):
    pers_in_frlist = ()
	
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def is_known(self, person):
        if person.name in self.pers_in_frlist:
            return True
        else:
            return False
    def know(self, person):
        if person.name in self.pers_in_frlist:
    	    print('{} and {} are friends'.format(self.name, person.name))
        else:
            self.pers_in_frlist = self.pers_in_frlist + (person.name,)
            
			
person1 = Person(12, 'Bobby')
person2 = Person(13, 'Jimmy') 
person3 = Person(14, 'Buddy')
person1.know(person2)
person1.know(person3)
person1.is_known(person2)
person1.know(person2)

# 2
# Есть класс, который выводи информацию в консоль: 
#`Printer`, у него есть метод: log(*values). Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *
class Printer(object):
    log_list = list()
    def __init__(self):
    	print(self)
    def log(self, *values):
        for t in values:
            self.log_list.append(t)
class Formatted(Printer):
    def star_print(self, *values):
        #self.values = values
        for j in values:
	        print('**{}**'.format(j)) 

a = Formatted()
b = Formatted()
a.log(1, 'asd', 123)
a.star_print(1, 'asd', 123)
b.log(4, '2asd', 32123)

	def log(self, *values):
		self.values = values ()
class Formatted(Printer):
	print('**()**'.format(self.values))

a = Formatted(1, 'asd', 123)

# 3
# Написать класс Animal и Human, сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые). 
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Animal(object):
	
	def __init__(self, name, danger):
		self.name = name
		self.danger = danger
#		animal_list = [name, danger]
	def is_dangerous (self, name):
#		self.danger = danger
		if self.danger == True:
			print ('Human be aware!')
		else:
		    print('OK!')
class Human(Animal):
	def __init__(self, name, sex):
	    pass

a = Animal('lion', True)
b = Human('Paul', 'male')
c = Animal('cat', False)
a.is_dangerous(b)
c.is_dangerous(b)