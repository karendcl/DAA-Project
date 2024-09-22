import random
from solution import solve
from backtrack import backtrack_solve
def generate():
    #n,k : nodes, subtree with k nodes
    # i,j : i is connected to j
    # must be a tree

    n = random.randint(2, 15)
    k = random.randint(1, n-1)
    #generate edges of the tree
    edges = []
    for i in range(2,n+1):
        edges.append((i,random.randint(1,i-1)))
    # edges.insert(0,(2,1))

    return n,k,edges

def trying():
    for i in range(100):
        n, k, edges = generate()
        sol1 = solve(n, k, edges)
        sol2, ed = backtrack_solve(n, k, edges)
        assert sol1 == sol2


if __name__ == "__main__":
    trying()
