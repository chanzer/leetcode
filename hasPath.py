"""
矩阵中的路径

题目描述：
		请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串
		所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可
		以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经
		过了矩阵中的某一个格子，则之后不能再次进入这个格子。
		例如 a b c e
		     s f c s
		     a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的
		路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符
		b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""
class Solution:
    def hasPath(self, board, row, col, word):
        self.col, self.row = col, row
        board = [list(board[col * i:col * i + col]) for i in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    self.b = False
                    self.search(board, word[1:], [(i, j)], i, j)
                    if self.b:
                        return True
        return False

    def search(self, board, word, dict, i, j):
        if word == "":
            self.b = True
            return
        if j != 0 and (i, j - 1) not in dict and board[i][j - 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j - 1)], i, j - 1)
        if i != 0 and (i - 1, j) not in dict and board[i - 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i - 1, j)], i - 1, j)
        if j != self.col - 1 and (i, j + 1) not in dict and board[i][j + 1] == word[0]:
            self.search(board, word[1:], dict + [(i, j + 1)], i, j + 1)
        if i != self.row - 1 and (i + 1, j) not in dict and board[i + 1][j] == word[0]:
            self.search(board, word[1:], dict + [(i + 1, j)], i + 1, j)
