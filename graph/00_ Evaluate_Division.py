'''https://leetcode.com/problems/evaluate-division/

[["a","b"],["b","c"]]
[2.0,3.0]
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
[["a","b"],["b","c"],["bc","cd"]]
[1.5,2.5,5.0]
[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
[["a","b"]]
[0.5]
[["a","b"],["b","a"],["a","c"],["x","y"]]
[["a","b"], ["a","c"], ["c","h"],["b","k"]]
[0.5, 3, 4, 5]
[["a","k"]]
[["a","b"],["c","d"]]
[1.0,1.0]
[["a","c"],["b","d"],["b","a"],["d","c"]]
[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
[3.0,4.0,5.0,6.0]
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
'''
import collections
class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		
		# create graph
		graph = collections.defaultdict(list)
		k = 0 
		for u,v in equations:  # a -> b | b -> a 
			graph[u].append( (v, values[k]) )
			graph[v].append( (u, 1/values[k]) )
			k+=1
		
		# calculate
		ans =  []
		# print(graph)
		def f(x, y ):
			if x in visited : return None
			if x not in graph or y not in graph: return -1
			if x==y: return 1
			visited[x] = True
			if y in graph[x]: 
				for item in graph[x]:
					if item[0] == y: return item[1]
				
			for neighbour in graph[x]:
				# print('here root',  x, y)
				rst = f( neighbour[0],  y)
				# print('here', rst, x, y)
				if rst and rst !=-1: return neighbour[1] *  rst
			return -1
			
			
			
			
			
		for u,v in queries:
			visited = {}
			ans.append(  f(u,v) )
		return ans