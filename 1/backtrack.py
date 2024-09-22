from itertools import combinations
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        self.visited = False

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def size(self):
        if len(self.children) == 0:
            return 1
        return 1 + sum([child.size() for child in self.children])

    def dfs_print(self, depth):
        str_ = "   "*depth + f"{self.value}\n"
        for i in self.children:
            str_ += i.dfs_print(depth+1)
        return str_

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.node2.add_child(self.node1)

class Tree:
    def __init__(self, root, k, nodes):
        self.root = root
        self.k = k
        self.nodes = nodes

    def size(self):
        return self.root.size()

    def dfs_print(self):
        for i in self.nodes:
            if i.parent is None:
                print(i.dfs_print(0))

def create_tree(n,k,edges):
    nodes = [Node(i+1) for i in range(n)]
    for i,j in edges:
        Edge(nodes[i-1],nodes[j-1])
    return Tree(nodes[0],k, nodes)

def is_valid_combination(edges_cut, edges, k, nodes):
    #create a new tree without the edges cut
    new_edges = [edges[i] for i in range(len(edges)) if (i+1) not in edges_cut]
    new_tree = create_tree(nodes,k,new_edges)

    for i in new_tree.nodes:
        if i.parent is None and i.size() == k:
            return True, new_tree

    return False, new_tree

def calc_size(tree):
    size = -1
    for i in tree.nodes:
        if i.parent is None:
            size += 1
    return size

def backtrack_solve(n,k,edges):
    #all combinations of all sizes of edges
    all_combinations = []
    for i in range(1,n+1):
        all_combinations.extend(combinations(range(1,n),i))

    if n == 1:
        return 0,[]

    if n == k:
        return 0,[]

    min_size = float('inf')
    edges_cut = []

    for i in all_combinations:
        valid, new_tree = is_valid_combination(i,edges,k,n)
        if valid:
            # new_tree.dfs_print()
            size = len(i)
            if size < min_size:
                min_size = size
                edges_cut = i

    if min_size == 0 or min_size == float('inf'):
        return 0,[]

    return min_size,edges_cut









