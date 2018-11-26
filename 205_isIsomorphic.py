"""
Isomorphic Strings
题目描述：
		Given two strings s and t, determine if they are
isomorphic.
		Two strings are isomorphic if the characters in s can
be replaced to get t.
		All occurrences of a character must be replaced with
another character while preserving the order of characters.
No two characters may map to the same character but a character
may map to itself.

Example 1:
	Input:  s = "egg", t = "add"
	Output: true

Example 2:
	Input:  s = "foo", t = "bar"
	Output: false

Example 3:
	Input:  s = "paper", t = "title"
	Output: true

Note:You may assume both s and t have the same length.
"""

#方法一：
class Solution:
	def isIsomorphic(self,s,t):
		"""
		:type s:str
		:type t:str
		:rtype :bool
		"""
		res = {}
		if len(s) != len(t) or len(set(s)) != len(set(t)):
			return False

		for a,b in zip(s,t):
			if a not in res:
				res[a] = b
			elif b != res[a]:
				return False
		return True

#方法二：
class Solution:
	def isIsomorphic(self,s,t):
		return len(set(s)) == len(set(t)) == len(set(zip(s,t)))

