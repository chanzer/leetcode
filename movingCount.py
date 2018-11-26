"""
机器人的运动范围

题目描述：
		地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移
		动，每一次只能向左，右，上，下四个方向移动一格，但是不能
		进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18
		时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
		但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
		请问该机器人能够达到多少个格子？

"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        self.row, self.col = rows, cols
        self.dict = set()
        self.search(threshold, 0, 0)
        return len(self.dict)

    def judge(self, threshold, i, j):
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold

    def search(self, threshold, i, j):
        if not self.judge(threshold, i, j) or (i, j) in self.dict:
            return
        self.dict.add((i, j))
        if i != self.row - 1:
            self.search(threshold, i + 1, j)
        if j != self.col - 1:
            self.search(threshold, i, j + 1)