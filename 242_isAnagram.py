"""
Valid Anagram
题目描述：
		Given two strings s and t , write a function to
determine if t is an anagram of s.

Example 1:
	Input:  s = "anagram", t = "nagaram"
	Output: true

Example 2:
	Input:  s = "rat", t = "car"
	Output: false

Note:You may assume the string contains only lowercase alphabets.
"""
# 方法一：
class Solution:
	def isAnagram(self,s,t):
		"""
		:type s:str
		:type t:str
		:rtype :bool
		"""
		for i in range(26):
			#遍历26个小写字母
			character = chr(ord('a')+i)

			if s.count(character) != t.count(character):
				return False
		return True
#方法二：与方法一原理相同，统计每个字母出现地次数
from collections import Counter
class Solution:
	def isAnagram(self,s,t):
		return Counter(s) == Counter(t)

#方法三：笨方法，比较长度，比较两个元素列表是否相同
class Solution:
	def isAnagram(self,s,t):
		if len(s) != len(t) or len(set(s)) != len(set(t)):
			return False
		return sorted(list(s)) == sorted(list(t))
