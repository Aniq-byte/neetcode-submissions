class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        i_set = self.find(i)
        j_set = self.find(j)

        self.parent[i_set] = j_set

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        out = n

        for edge in edges:
            a,b = edge[0],edge[1]
            if uf.find(a) != uf.find(b):
                uf.union(a,b)
                out -= 1
                   
        return out

            
        