AGH UST Course of Date Structures and Algorithms
=============================================== 
This repository contains the materials for the course of Data Structures and Algorithms at the AGH University of Science and Technology,
algorithms learned in this course and exercises solved during the course.
All the code is written in Python 3.

## Algorithms Overview

This section provides descriptions of all algorithms implemented in the `Algorytmy/` directory, organized by category.

### Dynamic Programming (dynamiczne/)
Dynamic programming algorithms that solve optimization problems by breaking them down into subproblems:

- **Fibonacci** (`fib.py`) - Classic Fibonacci sequence calculation using dynamic programming
- **Knapsack Problem** (`knapsack.py`, `knapsack2d.py`) - 0/1 knapsack problem variations
- **Longest Increasing Subsequence** (`LIS.py`, `LisNlogN.py`) - Finding LIS with O(n²) and O(n log n) approaches
- **Subset Sum** (`SumaPodzbioru.py`) - Determining if a subset with given sum exists
- **Coins Problem** (`coins.py`) - Minimum coins needed to make change
- **Traveling Salesman Problem** (`TSP.py`, `TSPbitonic.py`) - TSP solutions including bitonic variant
- **Independent Set Problem** (`ProblemZbioruNiezależnego.py`) - Maximum weight independent set
- **Block Tower** (`wiezaKlockow.py`) - Optimal block stacking problem
- **Ferry Problem** (`ferry.py`) - Vehicle loading optimization
- **Frog Problem** (`zaba.py`) - Path optimization for frog jumps
- **Chessboard** (`szachownica.py`) - Chessboard path problems
- **Black Forest** (`blackforest.py`) - Forest traversal optimization
- **Connecting Ranges** (`ConnectingRanges.py`) - Range connection optimization
- **Two Table Series** (`twoTableSeries.py`) - Series optimization across two tables

### Graph Algorithms (grafowe/)
Algorithms for graph traversal, shortest paths, and graph properties:

**Traversal:**
- **Breadth-First Search** (`BFS.py`, `BFSMatrix.py`) - BFS for adjacency list and matrix
- **Depth-First Search** (`DFS.py`, `DFSMatrix.py`) - DFS for adjacency list and matrix

**Shortest Paths:**
- **Dijkstra's Algorithm** (`Dijkstra.py`) - Single-source shortest paths for non-negative weights
- **Bellman-Ford Algorithm** (`Bellman-Ford.py`) - Single-source shortest paths with negative edges
- **Floyd-Warshall Algorithm** (`Floyd-Warshall.py`) - All-pairs shortest paths

**Minimum Spanning Tree:**
- **Kruskal's Algorithm** (`MSTKruskalClass.py`, `MSTKruskalTables.py`) - MST using union-find
- **Prim's Algorithm** (`MSTPrima.py`) - MST using priority queue

**Graph Properties:**
- **Topological Sorting** (`SortowanieTopologiczne.py`) - Ordering of directed acyclic graphs
- **Strongly Connected Components** (`silnieSpojneSkladowe.py`) - Finding SCCs
- **Bipartiteness Check** (`dwudzeilnosc.py`, `dwudzielnoscDFS.py`) - Testing if graph is bipartite
- **Bridges** (`mosty.py`) - Finding bridges in graphs
- **Articulation Points** (`punktyArtykulacji.py`) - Finding cut vertices
- **Euler Cycle** (`CyklEulera.py`) - Finding Eulerian cycles
- **Connectivity** (`spojnosc.py`) - Graph connectivity algorithms

**Flow Networks:**
- **Edmonds-Karp Algorithm** (`Ford-Fulkerson/Edmond-Karp.py`) - Maximum flow using BFS

**Utility:**
- **Graph Conversion** (`konwersjaGrafów.py`) - Converting between graph representations
- **4-Cycle Detection** (`cykl4.py`) - Detecting 4-cycles in graphs

### Sorting Algorithms (Sorotowanie/)
Various sorting algorithms with different time complexities:

- **Quick Sort** (`quicksort1.py`, `quicksort2.py`, `quicksortHoare.py`, `quicksortLomuto.py`) - Quick sort variants
- **Iterative Quick Sort** (`quicksortIterHoare.py`, `quicksortIterLomuto.py`) - Non-recursive implementations
- **Merge Sort** (`mergesort1.py`, `mergesortLinkedList1.py`, `meargesortLinkedList2.py`) - Merge sort for arrays and linked lists
- **Heap Sort** (`heapsort1.py`, `heapsortLinkList.py`) - Heap sort for arrays and linked lists
- **Insertion Sort** (`insertionSort.py`) - Simple insertion sort algorithm
- **Counting Sort** (`countigsort.py`) - Linear time sorting for integers
- **Radix Sort** (`radixSort.py`, `radixSortNum.py`) - Digit-based sorting
- **Bucket Sort** (`bucketSort.py`) - Distribution-based sorting

### Search Algorithms (wyszukiwanie/)
Algorithms for finding elements and selecting order statistics:

- **Binary Search** (`findBin.py`) - Standard binary search
- **Binary Search Variants** (`findBinFirst.py`, `findBinLast.py`) - Finding first/last occurrence
- **Quick Select** (`quickselect1.py`) - Finding k-th order statistic

### Data Structures (strukturyDanych/)
Implementation of fundamental data structures:

- **Binary Search Tree** (`BST.py`, `BSTTees.py`) - BST implementations
- **Hash Table** (`hashTable.py`) - Hash table with collision handling
- **Range Queries** (`przedziały.py`, `sumyPrzedzialow.py`) - Range sum and interval queries
- **Blocks** (`klocki.py`) - Block-based data structure problems

### Selection Algorithms (mediana/)
Algorithms for finding medians and order statistics:

- **Magic Fives** (`magicFives.py`) - Median of medians algorithm
- **Two Heaps** (`TwoHeaps.py`) - Finding running median using two heaps

### Greedy Algorithms (zachłanne/)
Greedy approach algorithms that make locally optimal choices:

- **Knapsack Variants** (`knapsack.py`, `knapsackLiquid.py`) - Greedy knapsack solutions
- **Task Selection** (`ProblemWyboruZadan.py`) - Activity selection problem
- **Huffman Coding** (`KodyHuffmana.py`) - Optimal prefix-free coding
- **Deadline Scheduling** (`deadliny.py`) - Task scheduling with deadlines
- **Tractor Problem** (`traktor.py`, `traktor-HP_Wojciech.py`) - Resource allocation optimization

