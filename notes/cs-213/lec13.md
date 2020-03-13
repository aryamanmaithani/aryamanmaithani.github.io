---
layout: page
title: CS 213
subtitle: Lecture 13
image:
---

### Application of trees

> Q. Where have you seen trees?

* Someone: circuit diagram  
* Famous example: family tree. Could start with myself as root and branches are parents and so on. Can do it the other way around as well. Start with two important people like King X and Queen Y, then write their offsprings.  
* Decision tree. Flowchart of decisions. Helps in taking actions.  
* Game tree. 
    - Tournaments → leagues, semi-finals, finals. 
    - Chess, Tic-Tac-Toe, et cetera. AI uses this. (Making best possible decision.)  
* File system in Linux/Ubuntu. Tree or not?
    - In a tree, every node should have a unique parent. [Pic](/notes/cs-213/files-tree.png)
        + However, if we allow file sharing, the same file can come in two directories → then, it's not a tree. [Pic](/notes/cs-213/files-tree-sharing.png)
        + Linux _does_ allow you to share, though. So, not a tree. (`ln` command helps you link.) Then, it's called a directed acyclic graph.
            * Side tangent: sharing of directories is more constrained. This might create a cycle and thus, has to be done with care.
* Expression tree. We saw earlier how to go from the infix `a + b * c - d % e + f` to postfix to evaluation. (Using stacks.) However, now I don't want that. I want to go to the tree. Prof explained. I couldn't keep up with the diagrams using Paint. :(
    - dot → tool from open source Graphviz → powerful tool for drawing graphs

### Traversal of trees
3 ordered traversals  
Left:  
```C++  
inorder(T){  
    inorder(left(T))  
    val(T)  
    inorder(right(T))  
}
```
The above traversal of [this example](/notes/cs-213/bst-trav.png) will give the output: 11, 32, 33, 35, 42, 50, 60  
In general, a left traversal will give in ascending order.  

Another one:  
```C++  
preorder(T){  
    val(T)  
    preorder(left(T))  
    preorder(right(T))  
}
```

### Another Application
* ATC schedules landing/takeoff of aircrafts and one runway
* Scheduling of tasks which have priority

Scheduling requirements:
* highest priority event is to be picked up and scheduled
* events can join whenever they arrive along with their priority value
* operations:
    - `findmax()` → find highest priority element and delete it
    - `insert()` → add a new element to the collection

Let us look at a traditional implementation before creating a new DS.
#### Array

(i) Unordered collection of $$n$$ elements.  
Suppose originally we have array as: |25|31|62|5|2|...|  
After `findmax()` → |25|31|5|2|...|  
This will have to be $$O(n)$$.  
`insert()` → can cheaply add the end since we don't care about order  

(ii) Order collection.  
`findmax()` → $$O(1)$$  
`insert()` → $$O(n)$$: note that bin search could give you the location in $$\log n$$ but you might need to shift a lot of elements → takes time  
If we do $$n$$ such operations, we get $$O(n^2)$$ in total.

Now, people wanted to create a data structure which does the above two operations well. We call it a __priority queue__.  
(Note that it isn't a queue. The FIFO isn't there.)  

## Priority Queue
  
> Q. How do we implement this?

Example: 20, 5, 62, 55, 1, 19, 5, 12  
Complete binary tree: A binary tree which is is completely filled, i.e., at level $$l$$, we have $$2^l$$ nodes.  
Thus, total number of nodes will be $$2^{\text{something}} - 1$$. In particular, these will be odd. (Unless empty tree.)  

Heap  
→ fill up levels from top to bottom  
→ last level: left to right  

Maxheap property → every node is greater than everything in its sub-tree. [Pic](/notes/cs-213/maxheap.png)  
It is easy to find max and delete it.  
But then we have to patch up the children. For this, we have to traverse till the bottom-most node in worst case. → $$\log n$$ by construction.

##### [Prev](/notes/cs-213/lec12) | [Next](/notes/cs-213/lec14)
#### [CS 213](/notes/cs-213)