from egzP9btesty import runtests
from copy import deepcopy
import sys


# Increase the recursion limit
sys.setrecursionlimit(50000)



def combineGraph(G,R):
	n=len(G)
	for i in range(n):
		for v in R[i]:
			G[i].remove(v)
                     


def EulerCycle(G):
	def DFSvisit(G,u):
		nonlocal cycle
		while  len(G[u])!=0: 
				v=G[u].pop()
				DFSvisit(G,v)
		cycle.append(u)
	n=len(G) 
	cycle=[]
	DFSvisit(G,0)
	cycle.reverse()                                              
	return cycle


def dyrektor( G, R ):
	G2=deepcopy(G)        
	combineGraph(G2,R)
	cycle=EulerCycle(G2)
	return cycle
	
runtests(dyrektor, all_tests=True)
