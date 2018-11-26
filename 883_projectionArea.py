"""
Projection Area of 3D Shapes
题目描述：
	On a N * N grid, we place some 1 * 1 * 1 cubes that are
axis-aligned with the x, y, and z axes.
	Each value v = grid[i][j] represents a tower of v cubes
placed on top of grid cell (i, j).
	Now we view the projection of these cubes onto the xy, yz,
and zx planes.
	A projection is like a shadow, that maps our 3 dimensional
figure to a 2 dimensional plane.
	Here, we are viewing the "shadow" when looking at the cubes
from the top, the front, and the side.
	Return the total area of all three projections.


Example 1:
	Input: [[2]]
	Output: 5

Example 2:
	Input:  [[1,2],[3,4]]
	Output: 17


Note: 1. 1 <= grid.length = grid[0].length <= 50
	  2. 0 <= grid[i][j] <= 50
"""
# 方法一
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        up = sum([sum([1 for i in N if i!=0]) for N in grid])
        left = sum([max(N) for N in grid])
        front = sum([max(N) for N in zip(*grid)])
        return up+left+front


# 方法二
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0

        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]:
                    ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col

        return ans
