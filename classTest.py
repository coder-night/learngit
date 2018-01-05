#!/usr/bin/env python3
#coding=utf-8

#面向对象编程

#__author__ Frank

#class 有着相同方法和不同数据的元素的集合

import types

from types import MethodType #用于给实例绑定方法

def test():
	test4()


#@property 使用
class Screen():
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		if not isinstance(width, float) and not isinstance(width, int):
			raise ValueError('width must be float or int')
		elif width <= 0:
			raise ValueError('width must bigger than zero')
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if not isinstance(height, float) and not isinstance(height, int):
			raise ValueError('height must be float or int')
		elif height <= 0:
			raise ValueError('height must bigger than zero')

		self._height = height

	@property #只读
	def resolution(self):
		return self._resolution

def test4():
	screen = Screen()
	screen.width = 2
	print(screen.width)

	screen.height = 3
	print(screen.height)

	screen.resolution = 5
	print(screen.resolution)






#使用__slots__  限制某个类的实例的属性
class Person():
	__slot__ = {'name', 'age'} #限制实例额外绑定的成员变量，使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

	def __init__(self, name, age, sex):
		self.name = name
		self.age = age

		self.sex = sex


def test3():
	first = Person('jake', 24, 'male')
	first.name = "jakie" #给一个实例动态添加属性
	print(first.name)

	def set_age(self, age):
		self.age = age
	#给一个实例动态添加方法
	# first.set_age = MethodType(set_age, first) 
	# print(first.set_age(10))
	# print(first.age)

	#给一个实例添加的方法，只对 一个实例有效
	#如果要给所有的实例绑定同一个方法，需要对类绑定方法
	# Person.set_age = set_age
	# first.set_age(10)
	# print(first.age)

	# second = Person()
	# second.set_age(20)
	# print(second.age)


#继承  多态
class Animal(object):

	name = 'animal' #类属性
	def run(self):
		print('animal is running')
class Dog(Animal):
	count = 0
	name = 'dog'
	def __init__(self):
		Dog.count = Dog.count + 1

	def run(self):
		print('dog is running')
class Cat(Animal):
	def run(self):
		print('cat is running')

def test2():

	def run_twice(animal):
		animal.run()
		animal.run()
	animal = Animal()
	
	dog = Dog()
	print(dog.name)
	print(dog.count)
	dog1 = Dog()
	print(dog1.count)
	dog2 = Dog()
	print(dog2.count)
	dog3 = Dog()
	print(dog3.count)

	print(Dog.count)

	cat = Cat()
	print(cat.name)

	run_twice(animal)
	run_twice(dog)
	run_twice(cat)

	print(isinstance(animal, Animal))
	print(isinstance(dog, Animal))

	#获取对象信息

	#获取对象类型
	print(type(animal))
	print(type(dog))

	print(type(animal) == Animal)

	#判断某个对象是否是函数
	print(type(run_twice) == types.FunctionType)
	print(type(abs)==types.BuiltinFunctionType)
	print(type(lambda x: x)==types.LambdaType)
	print(type((x for x in range(10)))==types.GeneratorType)


	#获取对象的所有属性和方法  dir()  返回一个list
	print(dir(animal))

	#hasattr(obj, 'x') #对象是否有属性x

	#getattr(obj, 'z', 404) #获取属性z，如果不存在返回404





class Student(object):
	#类的函数，第一个参数必须为self, 在使用该函数时，不需要传递self参数
	def __init__(self,name,age):
		self.name = name
		self.age = age

		#访问限制
		self.__name = name #name为一个私有变量， 内部吧__name变为——Student__name
		self._name = name #_name可以从外部访问到，但是一般不要访问


	def printNameAndAge(self):
		print(self.name, self.age)
def test1():
	jack = Student("jack", 18)
	jack.printNameAndAge()

#模板  类名：大写字母开头
# class Student(object):
# 	pass

#实例  Student()

test()