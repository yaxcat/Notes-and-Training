# TC: O(N)
# SC: O(N)
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        # Initialize the parents dict.  Set the parent of every node to itself by default.  We will assign
        # real parentage later.
        for v in vertices:
            self.parent[v] = v
        # This allows us to keep track of which node represents the set.  We assign a 0 rank to all nodes
        # by default
        self.rank = dict.fromkeys(vertices, 0) 

    def find(self, item):
        # If the node we've passed in is the current dictionary item, we've found what we're looking for
        if self.parent[item] == item:
            return item
        # If not, recursively call the function until we find it
        else:
            return self.find(self.parent[item])
        
    def union(self, x, y):
        # First, find the elements we want to merge
        xroot = self.find(x)
        yroot = self.find(y)

        # Next, assign parentage
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        # If both nodes have the same rank, just make xroot the parent since it was first.
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

vertices = ["A", "B", "C", "D", "E"]
ds = DisjointSet(vertices)
print("Initial Condition")
print("Parentage: ", ds.parent)
print("Rank: ", ds.rank)
print("")

ds.union("A", "B")
ds.union("A", "C")
print("Parentage: ", ds.parent)
print("Rank: ", ds.rank)
print("Find: ", ds.find("A"))
print("")

ds.union("D", "A")
print("Parentage: ", ds.parent)
print("Rank: ", ds.rank)
print("Find: ", ds.find("A"))