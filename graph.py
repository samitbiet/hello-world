import networkx as nx 
import numpy as np 

def Draw_Graph(A):
  G = nx.from_numpy_matrix(np.array(A))
  layout = nx.spring_layout(G)
  nx.draw(G, with_labels=True)
  
