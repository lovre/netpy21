import os
from time import *
import networkx as nx
from random import sample

def read(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  G = nx.read_pajek(os.path.join(path, file + '.net'))
  G.name = file
  return G

#def dists(G, n = 100):
#  """
#  Compute approximate average distance and diameter of undirected multigraph G.
#  """
#  ds = []
#  for i in G.nodes() if len(G) <= n else sample(G.nodes(), n):
#    ds.extend([d for d in nx.shortest_path_length(G, source = i).values() if d > 0])
#  return sum(ds) / len(ds), max(ds)

def info(G):
  """
  Compute and print out standard statistics of undirected multigraph G.
  """
  tic = time()
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  multi = False
  for edge in G.edges():
    if G.number_of_edges(edge[0], edge[1]) > 1:
      multi = True
      break
  print("{0:>15s} | '{1:s}'".format('Type', '===' if multi else '---'))
  print("{0:>15s} | {1:,d}".format('Nodes', G.number_of_nodes()))
  print("{0:>15s} | {1:,d}".format('Edges', G.number_of_edges()))
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

tic = time()

# Constructs small toy graph

G = nx.MultiGraph(name = 'toy')
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

# Prints out statistics of toy graph

info(G)

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
