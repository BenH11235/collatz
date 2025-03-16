#! /usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

class CONST:
    DEFAULT_MAX_INITIAL_VAL : int = 20

def f(num: int) -> int:
    result = 3*num+1
    while result%2==0 : result//=2
    return result

def generate_graph(max_initial_val=CONST.DEFAULT_MAX_INITIAL_VAL) -> nx.DiGraph:
    G = nx.DiGraph()
    for i in range(1,max_initial_val,2):
        curr=i
        #explore "Collatz path" until back in charted territory
        while(curr not in G or G.out_degree()[curr]==0):
            G.add_node(curr)
            G.add_node(f(curr))
            G.add_edge(curr,f(curr))
            curr = f(curr)
    return G

def draw(max_initial_val: int, out_file: str) -> None:
    G = generate_graph(max_initial_val)
    nx.draw_circular(G)
    plt.savefig(out_file)
        
def test_graph_generate() -> None:
    G = generate_graph(max_initial_val=30)
    assert(all([len(G[node])==1 for node in G]))
    assert(17 in G[11])
