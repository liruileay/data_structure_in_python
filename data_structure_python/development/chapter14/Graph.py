class Graph(object):
	class Vertex:
		"""表示图上面的每一个节点"""
		__slots__ = '_element'
		
		def __init__(self, x):
			self._element = x
		
		def element(self):
			return self._element
		
		def __hash__(self):
			return hash(id(self))
		
		def __str__(self):
			return str(self._element)
	
	class Edge:
		"""用于表示图上面的边"""
		__slots__ = '_origin', '_destination', '_element'
		
		def __init__(self, u, v, x):
			self._origin = u
			self._destination = v
			self._element = x
		
		def endpoints(self):
			"""返回一个元组(u,v)u是边的起点v是边的终点"""
			return (self._origin, self._destination)
		
		def opposite(self, v):
			"""假设v是一个边的一个端点那么返回边的另一个端点"""
			return self._destination if v is self._origin else self._origin
		
		def element(self):
			"""返回边上面的元素值"""
			return self._element
		
		def __hash__(self):
			return hash((self._origin, self._destination))
		
		def __str__(self):
			return '({0}{1}{2})'.format(self._origin, self._destination, self._element)
	
	def __init__(self, directed=False):
		"""定义进入和出去的逻辑和初始化方式"""
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing
	
	def is_directed(self):
		return self._incoming is not self._outgoing
	
	def vertex_count(self):
		"""返回图的顶点的数目"""
		return len(self._outgoing)
	
	def vertices(self):
		"""返回图中所有的顶点"""
		return self._outgoing.keys()
	
	def edge_count(self):
		"""返回图的边的数目"""
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		return total if self.is_directed() else total // 2
	
	def edges(self):
		"""返回图的所有的边"""
		result = set()
		for secondary_map in self._outgoing.values():
			result.update(secondary_map.values())
		return result
	
	def get_edge(self, u, v):
		"""返回从顶点u到v的边，如果其中一个存在就返回不存在就返回Bone"""
		return self._outgoing[u].get(v)
	
	def degree(self, v, outgoing=True):
		"""对于一个无向图返回返回边入射到顶点的数目，对于一个有向图返回入射到顶点v的输出变得数目"""
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v])
	
	def incident_edges(self, v, outgoing=True):
		"""返回所有边入射到顶点v的迭代循环，在有向图的情况下，通过默认报告输出边，如果可选参数设置为false则报告输入边"""
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge
	
	def insert_vertex(self, x=None):
		"""创建和返回一个新的元素x的Vertex"""
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming[v] = {}
		return v
	
	def insert_edge(self, u, v, x=None):
		"""创建并且返回一个新的从顶点u到顶点v的存储元素的x的Edge"""
		e = self.Edge(u, v, x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e
