"""
Missing Number
题目描述：
		Given an array containing n distinct numbers taken
		from 0, 1, 2, ..., n, find the one that is missing
		from the array.
Example 1:
	Input: [3,0,1]
	Output:2
Example 2:
	Input:[9,6,4,2,3,5,7,0,1]
	Output:8
"""
class Solution:
	def missingNumber(self,nums):
		"""
		:type nums: List[int]
		:rtype : int
		"""
		nums_set = set(nums)
		for i in range(len(nums)+1):
			if  i not in nums_set:
				return i
#求和相减
class Solution:
	def missingNumber(self,nums):
		return sum(range(1,len(nums)+1)) - sum(nums)
