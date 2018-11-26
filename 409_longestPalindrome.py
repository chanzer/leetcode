"""
Longest Palindrome
题目描述：
		Given a string which consists of lowercase or
uppercase letters, find the length of the longest palindromes
that can be built with those letters.
		This is case sensitive, for example "Aa" is not
considered a palindrome here.

Example :
	Input: 'abccccdd'
	Output:7
	Explanation:One longest palindrome that can be built is
				"dccaccd", whose length is 7.
"""
from  collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s).values()
        l = sum([2 * (i//2) for i in cnt])
        if len(s) == l:
            return l
        else:
            return l+1

