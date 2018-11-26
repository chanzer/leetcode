"""

Pascal Triangle II

题目描述：
		Given a non-negative index k where k ≤ 33, return
		the kth index row of the Pascal's triangle.
Note:
	In Pascal's triangle, each number is the sum of
	the two numbers directly above it.
Example:
	Input:3
	Output:[1,3,3,1]


		[
			    [1],
			   [1,1],
			  [1,2,1],
			 [1,3,3,1],
			[1,4,6,4,1]
		]
"""
class Solution:
	def getRow(self,rowIndex):
		# 生成一个numRows行的矩阵
		pascal = [[1]*(i+1) for i in range(34)]
		for i in range(34):
			for j in range(1,i):
				pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
		return pascal[rowIndex]
# 方法二(更简洁，无需建立整个矩阵)：
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        #  _ 表示临时变量，仅用一次，后面无需用到
        for _ in range(rowIndex):
        	#zip() 函数用于将可迭代的对象作为参数，将对象中对应的
        	#元素打包成一个个元组，然后返回由这些元组组成的列表。
        	#如果各个迭代器的元素个数不一致，则返回列表长度与最短
        	#的对象相同，利用 * 号操作符，可以将元组解压为列表。
        	#a = [1,2,3]   b = [4,5,6]
        	#c = zip(a,b)
        	# list(c) = [(1, 4), (2, 5), (3, 6)]
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row




