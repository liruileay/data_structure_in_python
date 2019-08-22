class GameEntry(object):
	"""为游戏存储最高分"""
	
	def __init__(self, name, score):
		self._name = name
		self._score = score
	
	def get_name(self):
		return self._name
	
	def get_score(self):
		return self._score
	
	def __str__(self):
		return "{0},{1}".format(self._name, self._score)


class Scoreboard(object):
	"""按照分数降序的顺序将列表中的对象排列"""
	
	def __init__(self, capacity):
		'''初始化一个列表'''
		self._board = [None] * capacity
		self._n = 0
	
	def __getitem__(self, k):
		return self._board[k]
	
	def __str__(self):
		return "\n".join(str(self._board[j] for j in range(self._n)))
	
	def add(self, entry: GameEntry):
		'''列表中的元素按照降序排列'''
		score = entry.get_score()
		if self._n < len(self._board) or self._board[-1] < score:
			if self._n < len(self._board):
				self._n += 1
			j = self._n - 1
			while j > 0 and self._board[j].get_score() < score:
				self._board[j] = self._board[j - 1]
				j -= 1
			self._board[j] = entry
