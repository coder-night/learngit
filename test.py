#!/usr/bin/env python3
#coding=utf-8




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
