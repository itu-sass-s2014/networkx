# -*- coding: utf-8 -*-

from heapq import heappush, heappop
from networkx import NetworkXError
import networkx as nx

__author__ = "\n".join(["Christian Olsson <chro@itu.dk>",
                        "Jan Aagaard Meier <jmei@itu.dk>",
                        "Henrik Haugbølle <hhau@itu.dk>"])
__all__ = ['min_degree']

def min_degree(G):
	""" Takes the nodes with minimum degree first, and assigns those a color.
	To reverse the algorith, so that it will take nodes with maximum degree first, simply apply *-1 to the priority of the heapqueue (based on degree)
	"""

	# G
	# sortér nodes efter degree (min/max)
	# vælg node fra liste
	# check om den har farvede naboer / find næste farvede
	# farv node
	# repeat
	# når listen er tom -> done

	queue = []
	assigned = dict()

	for n in G.nodes():
		heappush(queue, (len(G.neighbors(n) * -1), n))

	while len(queue):
		(priority, node) = heappop(queue) # node with least degree

		neighbourColors = dict()

		for neighbor in G.neighbors(node):
			if neighbor in assigned:
				neighbourColors[assigned[neighbor]] = 1 # doesnt matter, we're using the dict as a set

		i = 0
		color = -1
		while color == -1:
			if i in neighbourColors.keys():
				i = i + 1
			else:
				color = i

		assigned[node] = color

	print assigned
	asd()

	return assigned
