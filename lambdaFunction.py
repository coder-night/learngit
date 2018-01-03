#!/usr/bin/env python3
#coding=utf-8

#函数式编程
import os
import sys
from functools import reduce
def test():
    test6()


#filter 参数为一个函数和一个序列，函数依次作用于序列的每一个元素，根据返回值是true或者fale决定是否丢弃该元素

#计算素数
def test6():
    def _odd_iter():
        n = 1
        print(n)
        while True:
            n = n + 2
            print(n)
            yield n
    _odd_iter()
	# num = [2, 3, 5, 7]
	# def findPrime(n):
	# 	if n == 10000:
	# 		return

	# 	return findPrime(n + 1)
	# findPrime(2)

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
