"""
Reach a Numer
题目描述：
		You are standing at position 0 on an infinite number
line. There is a goal at position target.
		On each move, you can either go left or right. During the
n-th move (starting from 1), you take n steps.
		Return the minimum number of steps required to reach the
destination.


Example 1:
	Input: target = 3
	Output: 3
	Explanation:
		On the first move we step from 0 to 1.
		On the second step we step from 1 to 3.

Example 2:
	Input:  target = 2
	Output: 3
	Explanation:
		On the first move we step from 0 to 1.
		On the second move we step  from 1 to -1.
		On the third move we step from -1 to 2.

"""
class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target=abs(target)
        if target<2: return target
        l,r=0,target
        while l+1<r:
            m=(l+r)//2
            if m*(m+1)//2<target:
            	l=m
            else:
            	r=m
        while (r*(r+1)//2)%2!=target%2:
        	r+=1
        return r
