class TicTacToe(object):
	'''棋局游戏'''
	def __init__(self):
		'''初始化一个3*3的二维数组'''
		self._board = [[' '] * 3 for i in range(3)]
		self._player = "X"
	
	def mark(self, i, j):
		'''判读该那个走并且是否符合规范'''
		if not (0 <= i <= 2 and 0 <= j <= 2):
			raise ValueError("超出边界")
		if self._board[i][j] != ' ':
			raise ValueError("已经走过了不要重复走")
		if self.winner() is not None:
			raise ValueError("Game is already complete")
		self._board[i][j] = self._player
		if self._player == "X":
			self._player = "O"
		else:
			self._player = "X"
	
	def _is_win(self, mark):
		'''判断是否赢棋'''
		board = self._board
		return (mark == board[0][0] == board[0][1] == board[0][2] or
		        mark == board[1][0] == board[1][1] == board[1][2] or
		        mark == board[2][0] == board[2][1] == board[2][2] or
		        mark == board[0][0] == board[1][0] == board[2][0] or
		        mark == board[0][1] == board[1][1] == board[2][1] or
		        mark == board[0][2] == board[1][2] == board[2][2] or
		        mark == board[0][0] == board[1][1] == board[2][2] or
		        mark == board[0][2] == board[1][1] == board[2][0]
		        )
	
	def winner(self):
		'''判断是否有人赢棋'''
		for mark in "XO":
			if self._is_win(mark):
				return mark
		return None
	
	def __str__(self):
		rows = ['|'.join(self._board[r]) for r in range(3)]
		return '\n--------\n'.join(rows)
