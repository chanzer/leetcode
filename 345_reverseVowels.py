"""
Reverse Vowels of a String
题目描述：
	Write a function that takes a string as input and reverse
only the vowels of a string.

Example 1:
	Input: "hello"
	Output:"holle"

Example 2:
	Input: "leetcode"
	Output:"leotcede""
"""
class Solution:
    def reverseVowels(self, s):
        s= list(s)
        vows = 'aeiouAEIOU'
        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and s[l] not in vows: l += 1
            while l <= r and s[r] not in vows: r -= 1
            if l > r: break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)
