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


## TODO
- Linked List
    - Implement insert by position
    - Implement circular linked list