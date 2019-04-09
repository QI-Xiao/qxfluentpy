class Student111:
    __slots__ = ('name', 'age', 'set_age')
    pass

s = Student111()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# def set_score(self, score):
#     self.score = score
#
# Student111.set_score = set_score
# s.set_score(100)
# print(s.score)


class Student(object):

    @property
    def score(self):
         return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s = Student()
s.score = 60
print(s.score)
s.birth = 2013
print(s.age)

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._height * self._width

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 各种动物:
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, ):
    pass

class Ostrich(Bird):
    pass


class Fib:
    def __init__(self):
        self.a , self.b = 0,1

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        print(item)
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a,b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L


for n in Fib():
    print(n)

f = Fib()
print(f[4])
print(f[:10])
print(f[:10:2])


class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item=='score':
            return 99
        if item=='aaavvv':
            return lambda: 25
        raise AttributeError('has no attribute: %s' % item)

    def __call__(self):
        print('my name is %s' % self.name)

s = Student()
print(s.name)
print(s.score)
print(s.aaavvv)
# print(s.aab)
s()
print(callable(Student()))
print(callable(max))
print(callable([1,2,3]))

class Chain:

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.status.list)

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb'))
for name,member in Month.__members__.items():
    print(name, member, member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(day1 == Weekday.Mon)



class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')