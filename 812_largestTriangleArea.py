"""
Largest Triangle Area
题目描述：
	You have a list of points in the plane. Return the area of
the largest triangle that can be formed by any 3 of the points..


Example:
	Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
	Output: 2
	Explanation:The five points are show in the figure below.
The red triangle is the largest.

"""
import itertools
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
		# itertools.combinations(x, n) :从x中选n个元素去重排列组合
        return max(f(a, b, c) for a, b, c in itertools.combinations(points, 3))

