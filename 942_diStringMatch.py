"""
DI String Match
题目描述：
	Given a string S that only contains "I" (increase) or
"D" (decrease), let N = S.length.
	Return any permutation A of [0, 1, ..., N] such that
for all i = 0, ..., N-1:
	If S[i] == "I", then A[i] < A[i+1]
	If S[i] == "D", then A[i] > A[i+1]


Example 1:
	Input:  "IDID"
	Output: [0,4,1,3,2]

Example 2:
	Input:  "III"
	Output: [0,1,2,3]


Note: 1. 1 <= S.length <= 1000
	  2. S only contains characters "I" or "D".
"""
class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low, high = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1

        return ans + [low]
