"""
把数组排成最小的数

题目描述：
	输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的
	所有数字中最小的一个。例如输入{3,32,321}，则打印出这三个数字能排成的最
	小数字为321323.

解疑： 关于lmb = lambda x,y:int(str(x)+str(y))-int(str(y)+str(x))

"""
#方法一(python2.x版)：python2.x版本有cmp参数，在python3.x中没有此功能
class Solution:
	def PrintMinNumber(self,numbers):
		if not numbers:
			return  ''
		lmb = lambda n1,n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
		array = sorted(numbers,cmp = lmb)
		return ''.join([str(i) for i in array])

#方法二(python3.x)：

from functools import cmp_to_key
class Solution:
	def PrintMinNumber(self,numbers):
		cmp2key = cmp_to_key(lambda x,y :int(str(x)+str(y))-int(str(y)+str(x)))
		return ''.join(sorted(map(str,numbers),key = cmp2key))









lista = [5,4,3,2,1]
lmb = cmp_to_key(lambda x,y:int(str(x)+str(y))-int(str(y)+str(x)))

x = sorted(map(str,lista),key = lmb)
print(''.join(x))
print(lista)
print(x)
