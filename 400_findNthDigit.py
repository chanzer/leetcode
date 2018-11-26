"""
Nth Digit
题目描述：
	Find the n-th digit of the infinite integer sequence
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
	n is positive and will fit within the range of a
32-bit signed integer (n < 2^31).

Example 1:
	Input:  3
	Output: 3

Example 2:
	Input: 11
	Output:0
	Explanation:
	The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7,
8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
class Solution:
	def findNthDigit(self,n):
		"""
		:type n :int
		:rtype: int
		"""
		if n <= 9:
			return n
		i,p = 1,9
		while True:
			n += p
			p = p * 10 + 9
			i += 1
			if n < p * i:
				return int(str(int((n+i-1)//i))[(n+i-1)%i])

