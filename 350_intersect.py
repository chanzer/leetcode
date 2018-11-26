"""
Intersection of Two Arrays II
题目描述：
		Given two arrays, write a function to compute
		their intersection.

Example 1:
	Input:  nums1 = [1,2,2,1], nums2 = [2,2]
	Output: [2,2]
Example 2:
	Input:   nums1 = [4,9,5], nums2 = [9,4,9,8,4]
	Output: [4,9]
Notes:
	1.Each element in the result should appear as
	  many times as it shows in both arrays.
	2.The result can be in any order.
"""
import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        result = []
        for n in c1:
            if n in c2:
                result += [n] * min(c1[n], c2[n])
        return result
