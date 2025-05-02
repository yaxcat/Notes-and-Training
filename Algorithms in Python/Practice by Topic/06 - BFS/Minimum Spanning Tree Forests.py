class UnionFind:
    # Initialize Union-Find data structure with an empty parent mapping.
    def __init__(self):
        # Dictionary to keep track of nodes in the union
        self.id = {}

    # Finds the root of a node with path compression to flatten the structure for future queries
    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    # Unites two disjoint sets by connecting their roots.
    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)

def mst_forest(trees: int, pairs: list[list[int]]) -> int:
    # sort list, make sure to define custom comparator class cmp to sort edge based on weight from lowest to highest
    pairs.sort(key=lambda pair: pair[2])
    dsu = UnionFind()
    ret = 0
    for a, b, d in pairs:
        # check if pairs belong to same set before merging and adding edge to mst
        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
            ret += d
    return ret

if __name__ == "__main__":
    trees = int(input())
    pairs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = mst_forest(trees, pairs)
    print(res)