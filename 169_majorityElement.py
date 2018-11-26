"""
Majority Element
题目描述：
		Given an array of size n, find the majority element.
		The majority element is the element that appears
		more than ⌊ n/2 ⌋ times.
		You may assume that the array is non-empty and the
		majority element always exist in the array.
Example 1:
	Input:[3,2,3]
	Output:3
Example 2:
	Input:[2,2,1,1,1,2,2]
	Output:2
"""
class Solution:
	def majorityElement(self,nums):
		"""
		:type nums:List[int]
		:rtype :int
		"""
		#set会去除相同的元素
		L = set(nums)
		c = list(L)
		n = len(nums)
		for i in c:
			if nums.count(i) > int(n/2):
				element = i
				return element

class Solution:
	def majorityElement(self,nums):
		nums.sort()
		return nums[len(nums)//2]
