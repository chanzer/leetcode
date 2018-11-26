"""
X of a Kind in a Deck of Cards
题目描述：
		In a deck of cards, each card has an integer written
on it.

		Return true if and only if you can choose X >= 2 such
that it is possible to split the entire deck into 1 or more
groups of cards, where:
		1. Each group has exactly X cards.
		2. All the cards in each group have the same integer.
Example 1:
	Input:  [1,2,3,4,4,3,2,1]
	Output: true
	Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:
	Input: [1,1,1,2,2,2,3,3]
	Output: false
	Explanation: No possible partition.
"""
import collections
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            if a < b: a, b = b, a
            if b == 0: return a
            return gcd(b,  a % b)

        d = collections.Counter(deck)
        res = len(deck)
        for v in d.values():
            res = gcd(res, v)
        return res >= 2

