class Solution(object):
    def __init__(self):
        self.board = []
        self.col = []
        self.diag = set()
        self.reverse_diag = set()
        self.n = 0
        self.ans = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans.clear()
        self.board = [-1] * n
        self.col = [False] * n
        self.n = n
        self.back_track(0)
        return self.ans

    def back_track(self, row):
        # Done
        if row == self.n:
            self.ans.append(self.generate_board())

        for i in range(self.n):
            # Check the board
            diagonal = row - i
            rev_diagonal = row + i
            if self.col[i]:
                continue
            if diagonal in self.diag:
                continue
            if rev_diagonal in self.reverse_diag:
                continue

            # Set a queen
            self.board[row] = i
            self.col[i] = True
            self.diag.add(diagonal)
            self.reverse_diag.add(rev_diagonal)

            # Go for the next column
            self.back_track(row + 1)

            # Remove this queen
            self.board[row] = -1
            self.col[i] = False
            self.diag.remove(diagonal)
            self.reverse_diag.remove(rev_diagonal)

    def generate_board(self):  # Based on self.board
        str_board = []
        for col in self.board:
            row = ""
            for i in range(self.n):
                if i == col:
                    row += 'Q'
                else:
                    row += '.'
            str_board.append(row)
        return str_board


def main():
    s = Solution()
    for i in range(1, 10):
        print(s.solveNQueens(i))


if __name__ == "__main__":
    main()
