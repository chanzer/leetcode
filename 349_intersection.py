"""
Intersection of Two Arrays
题目描述：
		Given two arrays, write a function to compute
		their intersection.

Example 1:
	Input:  nums1 = [1,2,2,1], nums2 = [2,2]
	Output: [2]
Example 2:
	Input:   nums1 = [4,9,5], nums2 = [9,4,9,8,4]
	Output: [9,4]
Notes:
	1.Each element in the result must be unique.,
	2.The result can be in any order.
"""
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        dict = {}
        result = []
        for n in nums1:
            dict[n] = n
        for n in set(nums2):
            if dict.get(n) != None:
                result.append(dict[n])
        return result

