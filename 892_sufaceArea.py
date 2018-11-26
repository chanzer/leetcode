"""
Surface Area of 3D Shapes
题目描述：
	On a N * N grid, we place some 1 * 1 * 1 cubes.
	Each value v = grid[i][j] represents a tower of v cubes
placed on top of grid cell (i, j).
	Return the total surface area of the resulting shapes.


Example 1:
	Input: [[2]]
	Output: 10

Example 2:
	Input:  [[1,2],[3,4]]
	Output: 34


Note: 1. 1 <= N <= 50
	  2. 0 <= grid[i][j] <= 50
"""
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        result = 0
        for i in range(n):
            row = grid[i]
            for j in range(n):
                v = row[j]
                v1 = grid[j][i]
                if v:
                    result += 2
                if j == 0:
                    result += v + v1
                if j < n - 1:
                    result += abs(row[j + 1] - v)
                    result += abs(grid[j + 1][i] - v1)
                else:
                    result += v + v1
        return result

