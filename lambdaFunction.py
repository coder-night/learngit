#!/usr/bin/env python3
#coding=utf-8

#函数式编程
import os
import sys
import math
from functools import reduce

import functools  #
def test():
    # count1, count2, count3 = test9()
    # print( count1(), count2(), count3())
    test11()

#偏函数 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
def test11():
    print(int('1234556', base = 8))
    int2 = functools.partial(int, base=2)

#装饰器（decorator）  在函数运行期间，动态的更改函数的增加功能

def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def test10():
    print('hello,world')


#闭包
@log
def test9():
    def c(i):
        def calc():
            return i * i
        return calc

    l = []
    for i in range(1,4):
        l.append( c(i))
    return l

def test8():
    l = []
    for i in range(1,4):
        def calc():
            return i * i
        l.append(calc)
    return l



#返回函数
def test7(*args):
    
    def sum():
        n = 0
        for k in args:
            n = n + k
        return n
    return sum




#filter 参数为一个函数和一个序列，函数依次作用于序列的每一个元素，根据返回值是true或者fale决定是否丢弃该元素

#计算素数
def test6():
	#生成一个所有素数的生成器
    # def _odd_iter(): 
    # 	n = 1
    # 	while True:
    # 		n = n + 2
    # 		yield n
    # def _not_divisible(n):

    #     return lambda x: x % n > 0

    # def primes():

    # 	yield 2
    # 	it = _odd_iter()
    # 	while True:
    # 		n = next(it)
    # 		yield n
    # 		it = filter( _not_divisible(n), it)

    # for k in primes():
    # 	if k < 1000:
    # 	    print(k)
    # 	else:
    # 		break


    #回数的筛选
    def _nums():
    	n = 0
    	while True:
    		n = n + 1
    		yield n


    def findHuiNum(n):
    	ls = str(n)
    	invert = ls[::-1]

    	if ls == invert:
    		print(n)

    for k in _nums():
    	if k < 10000:
    		findHuiNum(k)
    	else:
    		break

    # def _odd_iter():
    #     n = 1
    #     while True:
    #         n = n + 2
    #         yield n

    # def _not_divisible(n):
    #     return lambda x: x % n > 0
  
    # def primes():
    #     yield 2
    #     it = _odd_iter()
    #     while True:
    #         n = next(it)
    #         yield n
    #         it = filter(_not_divisible(n), it)

    # for n in primes():
    # 	if n < 1000:
    # 		print(n)
    # 	else:
    # 		break


#map reduce

#map 两个参数，第一个参数是函数，第二个参数是iterable类型数据， map将第二个参数的每一个值放到第一个参数中执行
def test1():
	def power(x):
	    return x * x
	def turnToStr(x):
		return str(x)
	l = [1, 3, 5, 7, 9]
	l1 = map(power, l)
	l2 = map(turnToStr,l)
	print(list(l1))
	print(list(l2))
	print(list(map(str,l)))


#reduce
def test2():
	def plus(x, y):
		return x * 10 + y
	print(reduce(plus, [1,2,3,4,5]))

#complex
def test3():
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fn(s):
        return DIGITS[s]
    def two(x, y):
        return x * 10 + y
    print(reduce(two, map(fn, "12345")))

def test4():
	DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	print( reduce( lambda x, y: x * 10 + y, map(lambda s: DIGITS[s], "12345" ) ))

def test5():
    ex = ["dfsjd", "DadfD", "aDDdf"]
    print(ex[1].upper())
    print(ex[0].lower())
    print(list(map(lambda s: s[0].upper() + s[1:].lower() , ex)))


test()
