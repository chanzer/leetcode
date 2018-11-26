"""
Self Dividing Numbers
题目描述：
	A self-dividing number is a number that is divisible by
every digit it contains.
	For example, 128 is a self-dividing number because
128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
	Also, a self-dividing number is not allowed to contain
the digit zero.
	Given a lower and upper number bound, output a list of
every possible self dividing number, including the bounds
if possible.

Example :
	Input:	left = 1, right = 22
	Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
	The boundaries of each input argument are
	1 <= left <= right <= 10000.
"""
# 方法一
class Solution:
	def selfDividingNumbers(self,left,right):
		"""
		:type left:int
		:type right:int
		:rtype : List[int]
		"""
		ans = []
		for i in range(left,right+1):
			flag = True
			n = i
			while n > 0:
				# :   %	取模 - 返回除法的余数
				t = n % 10
				# :   //取整除 - 返回商的整数部分（向下取整）
				n = n // 10
				if t == 0 or i % t != 0:
					flag = False
					break
			if flag:
				ans.append(i)
		return ans

# 方法二
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [x for x in range(left, right+1) if all([int(i) != 0 and x % int(i)==0 for i in str(x)])]
