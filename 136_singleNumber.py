"""
Single Number
题目描述：
		Given a non-empty array of integers, every element
appears twice except for one. Find that single one.

Note:
		Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
	Input:  [2,2,1]
	Output: 1

Example 2:
	Input: [4,1,2,1,2]
	Output: 4
"""
#方法一：笨方法
class Solution:
	def singleNumber(self,nums):
		"""
		:type nums:List[int]
		:rtype :int
		"""
		res = []
		for i in nums:
			if i not in res:
				res.append(i)
			else:
				res.remove(i)
		return res.pop()

#方法二：异或的巧妙用法：与同一个数异或两次等于原始
#		速度最快，时间最短
class Solution:
	def singleNumber(self,nums):
		"""
		:type nums:List[int]
		:rtype :int
		"""
		res = 0
		for i in nums:
			res = res ^i
		return res

#方法三：数学之美：2*(a+b+c) - (a+a+b+b+c) = c
class Solution:
	def singleNumber(self,nums):
		"""
		:type nums:List[int]
		:rtype :int
		"""
		new_nums = list(set(nums))
		res = 2*sum(new_nums) - sum(nums)
		return res
