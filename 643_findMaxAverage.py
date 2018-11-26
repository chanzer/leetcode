"""
Maximum Average Subarray I
题目描述：
		Given an array consisting of n integers, find the
contiguous subarray of given length k that has the maximum
average value. And you need to output the maximum average
value.
Example 1:
	Input: [1,12,-5,-6,50,3],k=4
	Output:12.75
	Explanation:Maximum average is(12-5-6+50)/4=12.75

Note:
	1.1 <= k <= n <= 30,000.
	2.Elements of the given array will be in the range
	  [-10,000, 10,000].
"""
class Solution:
	def findMaxAverage(self,nums,k):
		"""
		:type nums:List[int]
		:type k:int
		:rtype : float
		"""
		sums = [0]
		tmp = 0
		if len(nums) <= k:
			return sum(nums)/len(nums)
		for i in range(len(nums)):
			tmp += nums[i]
			sums.append(tmp)
		return max([sums[i] - sums[i-k]for i in range(k,len(nums)+1)])/k
# 速度更快
class Solution:
	def findMaxAverage(self,nums,k):
		maxSum = tmp = sum(nums[:k])

		for i in range(k,len(nums)):
			tmp += nums[i] - nums[i -k]
			if maxSum <tmp :maxSum = tmp

		return maxSum/k

