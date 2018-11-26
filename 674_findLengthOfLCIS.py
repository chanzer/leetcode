"""
Longest Continuous Increasing Subsequence
题目描述：
		Given an unsorted array of integers, find the
length of longest continuous increasing subsequence.
Example 1:
	Input:  [1,3,5,4,7]
	Output: 3
Example 2:
	Input:  [2,2,2,2,2]
	Output: 1
	Explanation:The longest continuous increasing
	            subsequence is [2], its length is 1.
Note:
	 Length of the array will not exceed 10,000.
"""
class Solution:
	def findLengthOfLCIS(self,nums):
		"""
		:type nums:List[int]
		:rtype : int
		"""
		if not nums:
			return 0
		max_len = 1
		cur_len = 1
		for i in range(1,len(nums)):
			if nums[i] > nums[i-1]:
				cur_len += 1
				max_len = cur_len if cur_len >max_len else max_len
			else:
				cur_len = 1
		return max_len
