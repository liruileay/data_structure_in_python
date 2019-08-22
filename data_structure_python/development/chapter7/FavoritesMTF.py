from development.chapter7.FavoritesList import FavoritesList
from development.chapter7.PositionalList import PositionalList


class FavoritestListMTF(FavoritesList):
	
	def _move_to(self, p):
		"""不对元素进行排序将要访问的元素放在第一个"""
		if p != self._data.first():
			self._data.add_first(self._data.delete(p))
	
	def top(self, k):
		"""返回访问两排名前k个的节点元素"""
		temp = PositionalList()
		for item in self._data:
			temp.add_last(item)
		for j in range(k):
			highPos = temp.first()
			walk = temp.after(highPos)
			while walk is not None:
				if walk.element()._count > highPos.element()._count:
					highPos = walk
				walk = temp.after(walk)
			yield highPos.element()._value
			temp.delete(highPos)

if __name__ == '__main__':
	fav = FavoritestListMTF()
	for c in 'hello. this is a test of mtf':
		fav.access(c)
	for k in fav.top(10):
		print(k)
	print(fav)