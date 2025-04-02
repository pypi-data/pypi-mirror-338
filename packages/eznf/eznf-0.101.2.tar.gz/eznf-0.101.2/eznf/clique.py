import modeler
import itertools
import random

def encode(G):
    enc = modeler.Modeler()
    for i in range(len(G)):
        enc.add_var(f"x_{i}")
        
    for triple in itertools.combinations(range(len(G)), 3):
        i, j, k = triple
        if G[i][j] and G[j][k] and G[i][k]:
            enc.add_clause([f"x_{i}", f"x_{j}", f"x_{k}"])
        if not G[i][j] and not G[j][k] and not G[i][k]:
            enc.add_clause([f"-x_{i}", f"-x_{j}", f"-x_{k}"])
        
    return enc


def random_graph(n, p):
    adj = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                adj[i][j] = True
                adj[j][i] = True
    return adj
                
def decode(model):
    n = len(model)
    ans = []
    for i in range(n):
        if model[f"x_{i}"]:
            ans.append(i)
    print(ans)
    return ans
            
                
graphs = [random_graph(6, 0.5) for _ in range(10)]

for graph in graphs:

    encoding = encode(graph)
    n = len(graph)
    encoding.solve_and_decode(decode)
    
# encoding.serialize(f"formulas/clique-is-k-6.cnf")
