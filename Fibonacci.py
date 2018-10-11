"""
斐波那契数列

题目描述：
	现在要求输入一个整数n,请你输出斐波那契数列的第n项
	(从0开始，第0项为0)
"""
#方法一：（通过测试用例）
class Solution:
	def Fibonacci(self,n):
	res =[0,1,1,2]
	while  len(res)<= n:
		res.append(res[-1]+res[-2])
	return res[n]

#方法二：递归（上传测试不通过，本地没问题）
def Fibonacci(n):
	if n == 0:
		return 0
	elif n ==1 or n ==2:
		return 1
	else:
		return (Fibonacci(n-1)+Fibonacci(n-2))
print(Fibonacci(0))


