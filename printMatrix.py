"""
顺时针打印矩阵
题目描述：
	输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
	1  2  3  4
	5  6  7  8
	9  10 11 12
	13 14 15 16
	输出： 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""
class Solution:
	def printMatrix(self,matrix):
		res = []
		while matrix:
			res += matrix.pop(0)
			if matrix and matrix[0]:
				for row in matrix:
					res.append(row.pop())
			if matrix:
				res += matrix.pop()[::-1]
			if matrix and matrix[0]:
				for row in matrix[::-1]:
					res.append(row.pop(0))
		return res
