import os
from time import *
import networkx as nx
from cdlib import algorithms
from node2vec import Node2Vec

def read(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  G = nx.MultiGraph(name = file)
  nodes = {}
  with open(os.path.join(path, file + '.net'), 'r') as file:
    for line in file:
      if line.startswith('*vertices'):
        continue
      elif line.startswith('*edges') or line.startswith('*arcs'):
        break
      else:
        node = line.strip().split('"')
        nodes[node[0].strip()] = node[1]
        G.add_node(node[1], cluster = int(node[2]) if len(node[2]) > 0 else 0)
    for line in file:
      edge = line.strip().split(' ')
      G.add_edge(nodes[edge[0]], nodes[edge[1]])
  return G

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
  print("{0:>15s} | {1:,d} ({2:,d})".format('Nodes', G.number_of_nodes(), nx.number_of_isolates(G)))
  print("{0:>15s} | {1:,d} ({2:,d})".format('Edges', G.number_of_edges(), nx.number_of_selfloops(G)))
  ks = [k for _, k in G.degree()]
  print("{0:>15s} | {1:.1f} ({2:,d}, {3:,d})".format('Degree', 2.0 * G.number_of_edges() / G.number_of_nodes(), min(ks), max(ks)))
  CCs = sorted(nx.connected_components(G), key = len, reverse = True)
  print("{0:>15s} | {1:.1f}% ({2:,d})".format('Components', 100.0 * len(CCs[0]) / G.number_of_nodes(), len(CCs)))
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

tic = time()

for name in ['karate', 'java']:

  # Constructs a graph of real network

  G = read(name)
  G = nx.Graph(G)

  # Prints out statistics of real network

  info(G)

  # Computes node centralities of real network

  degrees = nx.degree_centrality(G)
  pageranks = nx.pagerank(G)
  
  clusterings = nx.clustering(G)
  
  closenesses = nx.closeness_centrality(G)
  betweennesses = nx.betweenness_centrality(G)

  # Finds community structure of real network

  leiden = {}
  for c, comm in enumerate(algorithms.leiden(G).communities):
    for i in comm:
      leiden[i] = c
      
  infomap = {}
  for c, comm in enumerate(algorithms.infomap(G).communities):
    for i in comm:
      infomap[i] = c

  # Writes node features to tab-separated file

  with open(os.path.join('.', name + '-features.tab'), 'w') as file:
    file.write("m#node\tC#degree\tC#pagerank\tC#clustering\tC#closeness\tC#betweenness\tD#leiden\tD#infomap\tcD#class\n")
    for node in G.nodes(data = True):
      i, c = node[0], node[1]['cluster']
      file.write("{:s}\t{:f}\t{:f}\t{:f}\t{:f}\t{:f}\t{:d}\t{:d}\t{:d}\n".format(i, degrees[i], pageranks[i], clusterings[i], closenesses[i], betweennesses[i], leiden[i], infomap[i], c))
  
  # Computes node embeddings using node2vec

  dims = 32
  node2vec = Node2Vec(G, dimensions = dims, workers = 8, quiet = True)
  node2vec = node2vec.fit().wv
  
  # Writes node embeddings to tab-separated file

  with open(os.path.join('.', name + '-node2vec.tab'), 'w') as file:
    file.write("m#node\t" + "\t".join(["C#node2vec-" + str(i) for i in range(dims)]) + "\tcD#class\n")
    for node in G.nodes(data = True):
      i, c = node[0], node[1]['cluster']
      file.write(i + "\t" + "\t".join([str(x) for x in node2vec[i]]) + "\t" + str(c) + "\n")

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
