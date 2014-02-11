#!/usr/bin/env python
from nose.tools import *
import networkx as nx
from random import random, choice

class TestMinDegree:

    def setUp(self):
        print "test setup"

    def test_random_graph(self):
    	print "test random graph"

    	G = nx.Graph()

    	G.add_node(11)
    	G.add_node(12)
    	G.add_node(13)

    	G.add_edge(11,12)
    	G.add_edge(11,13)
    	# G.add_edge(2,3)

    	nx.min_degree(G)
