"""
search insert

题目描述：
	给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
	如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
"""

class Solution:
	def searchInsert(self,nums,target):

		nums[:] = [x for x in nums if x <target]
		return len(nums)
