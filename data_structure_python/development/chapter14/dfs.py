"""图的深度优先搜索"""


def DFS(g, u, discovered):
	"""已制定的顶点开始图的深度优先搜索的递归是实现"""
	for e in g.incident_edge(u):
		v = e.opposite(u)
		if v not in discovered:
			discovered[v] = e
			DFS(g, v, discovered)


def construct_path(u, v, discovered):
	"""重建u到v的u有向路径的函数给出DFS的发现的踪迹"""
	path = []
	if v in discovered:
		path.append(v)
		walk = v
		while walk is not u:
			e = discovered[walk]
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		path.reverse()
	return path


def DFS_complate(g):
	"""返回全部图的DFS森林的高级函数"""
	forest = {}
	for u in g.vertices():
		if u not in forest:
			forest[u] = None
			DFS(g, u, forest)
	return forest
