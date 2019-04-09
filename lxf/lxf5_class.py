class Student:

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('qi', 100)
bart._Student__name = 'dfdsf'
# bart.set_score(120)
bart.print_score()
print(bart.get_score())


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')



print(isinstance(bart, Student))


class Animal:
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

def run_twice(ccc):
    ccc.run()
    ccc.run()

dog = Dog()
print(isinstance(dog, Animal))
run_twice(Dog())


class Timer:
    def run(self):
        print('Start...')


run_twice(Timer())
print(type(dog))


a = Animal()
d = Dog()
print(isinstance(d, Animal))
print(dir(a))

class Myobject:
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Myobject()


class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

Student('aaa')
Student('bbb')
print(Student.count)

