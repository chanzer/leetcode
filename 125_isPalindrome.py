"""
Valid Palindrome
题目描述：
	Given a string, determine if it is a palindrome, considering
only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as
valid palindrome.

Example 1:
	Input: "A man, a plan, a canal: Panama"
	Output:true

Example 2:
	Input: "race a car"
	Output:false
"""
# 方法一
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i =[i.lower() for i in s if i.lower() in'abcdefghijklmnopqrstuvwxyz0123456789']
        return i == i[::-1]


# 方法二
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''
        for char in s:
        	# str.isalnum()如果 string 至少有一个字符并且所有字符
        	#              都是字母或数字则返回 True,否则返回 False
            if char.isalnum():
                res += char.lower()
        return res == res[::-1]
