#!/usr/bin/env python3
#coding=utf-8

#python内置函数
#https://docs.python.org/3/library/functions.html

def test():
	test15('jackie', 30)


#高级特性  

#切片




#函数  常用内置函数和自定义函数

#函数的参数 位置参数、默认参数（放在后边）、可变参数、关键字参数

#关键字参数  extra = {'city': 'beijing', 'job':journaliste}  test15('jim', 40, **extra)
def test15(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

#可变参数 参数的传入值为list 或tuple ，
def test13(numbers):
	pass
def test14(*numbers):
	pass
#默认参数 ***定义默认参数，默认参数必须指向不变对象，由于默认参数在定义时，就已经被计算出来,每次调用,内部改变其值，下次内容会改变
def test12(L = None):
	if L is None:
		L = []
	L.append("end")
	print(L)




def test11(age):
	#参数检查
	#isinstance(objc,(class1, class2)) 检查某个对象是否为类或其子类的对象
	#issubclass(sub, super) 检查某个类是否为super的派生类
	if not isinstance(age, (int, float)):
		raise TypeError("类型不为int或float")

	if age > 10:
		pass #占位符，什么都不做
		print("hello")
	else:
		print("world")

def abs(num):
	if num >= 0:
		return num
	else:
		return -num


def test10():
	#绝对值
	print(abs(100), abs(-100), abs(0) )
	print(max(1,0,100,-5,20))
	print(min(1,0,100,-5,20))

	#数据类型转换
	print(int(True), int(False), int('0'))
	print(bool(0), bool(''), bool(1))
	print(float(0), float('0'))


#dict {} 'Thomas' #in {} 判断key是否在dict中#  #dict.get("name") 获取value值
#set
def test9():
	name = {'arvin':18, 'frank':19, 'jim':['30', '60kg']}
	
	print(len(name))

	for i in name:
		if i in name:
			print("dict[%s]",i, name[i], i in name, name.get(i))

	for (k, v) in name.items():
		print(k, v)

	# for (k,v) in name.iteritems():
	# 	print(k, v)

	# for (k, v) in zip(name.iterkeys(), name.iteritems()):
	# 	print(k, v)

	s = set([1,3,4,5,6,5,5])
	for k in s:
		print(k)

#循环 for in list or tuple            for index in list(rang())      while
def test8():
	index = [1,2,5,4]
	for i in index:
		print(i)

	n = len(index)
	while n > 0:
		n = n - 1
		print(index[n])

	sum = 0
	for i in list(range(101)):
		sum = i + sum
		
	print(sum)

#分支  bool判断 非零.非空字符串。非空list等

def test7():
	h = input('input your weight:') #返回字符串
	height = int(h) #将字符串转化为整型
	if height > 170:
		print("高")
	elif height == 170:
		print("中")
	elif height < 170:
		print("低")


#数据结构
#list 可变数组：[]  tuple不可变数组 (,) 在只有一个元素的情况下，为了与小括号区分，加一个逗号

#tuple 不可变数组()
def test6():
	index = (1,2,[4, 5])

	index[2][0] = 8
	index[2].pop()
	print(index, len(index))

#list 可变数组
def test5():
	index = [1, 2, 3, 4]
	index.append(9)
	index.insert(0, 0)
	index.pop(1)
	index.pop()
	print(index[0], index[1], index[2], index[3])
	index[0] = [3, 4]
	print(index[0], index[0][1])



# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#网络传输用的是byte的类型数据
def test4():
	x = b'ABC' #1个字符只占一个字节
	x1 = 'ABC' #一个字符多个字节，前边补0
	x2 = 'ABC'.encode('ascii')
	x3 = '你好'.encode('utf-8')
	print(x, x1, x2, x3)

#接受的网络数据是以byte形式接受

#ASCII码与字符的相互转换
# print( ord('A'), ord('人'), ord('民'), chr(66), chr(44), chr(20154))
def test3():
	y = x.decode('ascii')
	y2 = x2.decode('utf-8')
	y3 = x3.decode('utf-8')
	print(y, y2, y3, len(y), len(y2), len(y3))

#second
def test2():
	name = input("输入名字:") #输入数字：input()   raw_input 字符串
	print(name)

#first 
def test1():
	print("hello,world")



test()
