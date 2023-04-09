# Data Strucutres
In computer science, data structures refer to the way of organizing and storing data in a computer so that it can be efficiently accessed and manipulated. It involves defining data types, organizing data in a way that enables efficient access and modification, and designing algorithms that operate on these data structures.

Examples of common data structures include arrays, linked lists, stacks, queues, trees, and graphs. Each data structure has its own unique strengths and weaknesses, making them suitable for different tasks and scenarios.

Data structures play a crucial role in computer programming, as they help developers write efficient and optimized code. By choosing the appropriate data structure for a given task, programmers can reduce the time and resources required to perform complex operations, resulting in faster and more responsive applications and we will learn more about them together :

## Array

- A collection of elements of the same data type.
- Elements are stored in contiguous memory locations.
- Access time is constant time O(1) if the index is known.
- Insertion and deletion time is O(n) as all the elements may need to be shifted.

## Linked List

- A collection of nodes, where each node has a value and a reference to the next node.
- Elements are not stored in contiguous memory locations.
- Access time is O(n) as we need to traverse the list to find the node.
- Insertion and deletion time is constant time O(1) as we only need to update the references.

## Stack

- A collection of elements that follow Last-In-First-Out (LIFO) order.
- Operations include push (adds an element to the top) and pop (removes the top element).
- Implemented using an array or a linked list.
- Access time for the top element is constant time O(1).

## Queue

- A collection of elements that follow First-In-First-Out (FIFO) order.
- Operations include enqueue (adds an element to the end) and dequeue (removes the first element).
- Implemented using an array or a linked list.
- Access time for the first element is constant time O(1).

## Tree

- A collection of nodes where each node has a value and references to its child nodes.
- Nodes have a parent-child relationship.
- Root node has no parent and leaf nodes have no children.
- Binary trees have at most two children per node.
- Traversal can be pre-order, in-order, or post-order.

## Hash Table

- A data structure that stores data in key-value pairs.
- Implemented using an array and a hash function that maps keys to array indices.
- Access time is constant time O(1) on average for insertion, deletion, and search operations.

## Graph

- A collection of nodes and edges that connect them.
- Nodes can have multiple edges to other nodes.
- Can be directed or undirected.
- Traversal can be breadth-first search (BFS) or depth-first search (DFS).