"""
First Unique Charcater in a String
题目描述：
		Given a string, find the first non-repeating character
in it and return it's index. If it doesn't exist, return -1.

Example :
		s = "leetcode"
		return 0.

		s = "loveleetcode",
		return 2.

Notes:You may assume the string contain only lowercase
	  letters.
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters ='abcdefghijklmnopqrstuvwxyz'
        index = [s.index(i) for i in letters if s.count(i) == 1]
        return min(index) if len(index) >0 else -1
