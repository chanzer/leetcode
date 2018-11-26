"""
Missing Number
题目描述：
		Given an array nums, write a function to move all
		0's to the end of it while maintaining the relative
		order of the non-zero elements.
Example:
	Input: [0,1,0,3,12]
	Output:[1,3,12,0,0]
Note:
	1.You must do this in-place without making a copy of
	  the array.
	2.Minimize the total number of operations.
"""
class Solution:
	def moveZeroes(self,nums):
		"""
		:type nums:List[int]
		:rtype:void do not return anything,
			   modify nums in-place instead.
		"""
		i = 0
		count = 0
		while 0 in nums:
			if nums[i] == 0:
				nums.pop(i)
				count += 1
			else:
				i += 1
		nums += ([0] * count)

class Solution:
	def moveZeroes(self,nums):
		for i in range(len(nums))[::-1]:
			if nums[i] == 0:
				nums.append(nums.pop(i))

