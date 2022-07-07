# Coding Concepts 

## Data Types

- Primitive data types 
    - Python : int, float, str, and bool
- User defined data types

### Data Structures

**Definition**: a particular way of storying and organizing data in order to be used efficiently

1) *Linear data structures* - elements are accessed in sequential order, however the data does not need to be stored sequentially

    Examples:

    - Linked Lists
    - Stacks
    - Queues

2) *Non-linear data structures* - element are stored and accesssed in non-linear order

    Examples:

    - Trees
    - Graphs

### Abstract Data Types (ADT)
**Definition**: Class for an object whose behavior is defined by a set of data and a set of operations.

Feature
- *Abstraction*: Implemenation of the data structure is not know ot user
- *Conceptualization*: ADT give us a better conceptualization of the real world 


## Algorithms
**Definition**: Step-by-step instructions to solve a given problem

### Algorithm Analysis

Resources to consider

1) Time complexity - number of steps alogrithm takes given the input size

2) Space complexity - number of storage locations used by algorithm

| Complexity | Name | Example |
| :--------: | :--: | :-----: |
| O(1) | Constant | Adding element to front/end of a linked list |
| O(log(n)) | Logrithmic | Binary search | 
| O(n) | Linear | Linear search |
| O(nlog(n)) | Linear Logarithmic | Merge sort |
| O(n^2) | Quadratic | Shortest path between two nodes in a graph | 
| O(2^n) | Exponential | The Towers of Hanoi problem |


### Recursion

**Definition**: Solves a problem by calling a itself to work on a smaller subset of the problem 

- Terminates when *base case* is reached
- Calls itself in a *cursive case* to perform operation on subset of the problem
- Each recursive call requires stack space and will cause stack overflow, if infinite rescurion occurs
- Useful in cases where iterative solutions are not clear even though iterative solutions are more efficient in most cases

Examples:

- Fibonacci Series
- Factoral
- Merge Sort
- Quick Sort
- Binary Search
- Tree Traversal (InOrder, PreOrder, PostOrder)
- Graph Traversal (DFS - Depth First Search and BFS - Breadth First Search)
- Towers of Hanoi

#### Backtracking

**Definition**: Use of recursion to explore all possibilities until goal state is reached

- Subset of recursion 
- Used in problems that require trying all possibilities 

Examples:

- Generating All Possible Binary Strings (for given length)
- Generating k-ary Strings
- The Knapsack Problem
- Hamiltonian Cycles

### Linked List

**Definition**: data structure used for storing collections of data 

- Successive elements are connected by pointers
- Last element points to NULL
- Can grow until memory is exhausted (memory limited by system)
- Extra memory used to store pointer information

Operations:

- Insert
- Delete
- Delete List
- Count
- Find nth node from end of list


### Stack

**Definition**: one-ended linear data structure that models a real world stack
- LIFO - Last In First Out

Operations:

- Push - insert element onto stack
- Pop - removes and returns the most recently inserted element from the stack
- Top - returns the most recently inserted element
- Size - returns the number of elements on the stack
- IsEmptyStack - returns boolean indicating if stack is empty
- IsFullStack - returns boolean indicating if stack is full

Applications:

- Balancing of symbols
- Infix-to-postfix conversion
- Evaluation of postfix expression
- Implementing function calls 
- Finding of spans
- Page-visted history in Web browser
- Undo sequeence in text editor

### Queue

**Definition**: linear data structure which models real world queues (check-out line)
- FIFO - First In First Out

Operations:

- Enqueue - Inserts element at the end of the queue
- Dequeue - Removes and returns the element at the front of the list

Applications:

- Simulate real-world queues
- Asynchronous data transfers
- Waiting times of customer call center

### Priority Queue

**Definition**: operates similar to a queue, but elements are removed based on priority

Operations:

- Enqueue - Inserts element into the queue
- Dequeue - Removes and returns element with the highest priorty from the queue
- Peek - Returns element with the highest priority from the queue

Applications:

- Operating system schedule jobs with equal priority
- Graph algorithms (Dijkstra's shortest path, Prim's miniumum spanning tree, etc)
- Data compresssion in Huffman code

Implementations:

- Array
- Linked List
- Heap 
- Binary Search Tree

### Tree

**Definition**: non-linear data structure with each node pointing to a number of nodes

- Root - node with no parents and each tree can only contain one
- Edge - the link between parent and children nods
- Leaf node - node with no children
- Siblings - nodes that have the same parent
- Depth - Number of nodes required to reach node from root node

#### Binary Tree
 
Operations:

- Inserting an element
- Deleting an element 
- Searching for an element 
- Traversing the tree
- Size of tree
- Height of tree
- Least common ancestor (LCA)

Applications:

- Expression trees (compilers)
- Huffman coding trees (data compression)
- Binary search tree
- Priority Queue

### Graph

**Definition**: non-linear collection of nodes that contain data and are connected to other nodes

Operations:
- Add vertex - adds a vertex to the graph
- Add edge - adds an edge between two vertices of the graph
- Display vertex - displays a vertex of the graph

Applications:
- Representing relationships between components in electronic circuits
- Transportation networks (Highway/Flights)
- Computer networks
- Databases (Entity Relationship)

Implementations:
- Adjacency matrix
- Adjacency list
- Adjancency set