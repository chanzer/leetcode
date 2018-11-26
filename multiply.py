"""
构建乘积数组

题目描述：
	给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
	其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
	不能使用除法。

思路：
	将数组A写成一个方针，并把对角线上的元素赋值为1
	然后每一行的乘积对应B中的各个元素值。

"""
class Solution:
	def multiply(self,A):
		B = []
		for i in range(len(A)):
			temp = A[i]
			b = 1
			for j in range(len(A)):
				A[i] = 1
				b *= A[j]
			B.append(b)
			A[i] = temp
		return B

