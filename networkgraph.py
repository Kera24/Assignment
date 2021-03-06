# -*- coding: utf-8 -*-
"""NetworkGraph.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hteECKZ_7y3qCSPlIEdGggccITzPf8IH
"""

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('matrix.csv')

data.index = data['Unnamed: 0']

data.drop('Unnamed: 0',
  axis='columns', inplace=True)

label= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
edge = []
for i in range(len(data)):
  row = data.iloc[i,:]
  
  for j in range(len(row)):
    if row[j]==1:
      edge.append((data.index[i],label[j]))

def plot_graph(label,edge):
  G = nx.Graph()
  G.add_nodes_from(label)
  G.add_edges_from(edge)
  nx.draw(G, with_labels=1)

plot_graph(label,edge)

