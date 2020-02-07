---
layout: page
title: CS 213
subtitle: Lecture 8
image:
---
Some notes: the programs/algorithms given in the slides aren't necessarily the best. We could be expected to find an algorithm better than the one given, during the exams.  
Today, we learn hash tables.  

Need: Storage and retrieval.  
Before we go on, a question.  

> Q. How many distinct variable names can you create in C++?  
> Are there any limitations in the length of a variable name?  
> If we put a cap on that, of say, 100 characters, it's a very big number. ~ $$53\cdot63^{99}$$.

Thus, the _population_ is quite big.  
In practicality, we will work with a smaller set.  

## Hash function
A hash function $$h$$ takes a value and returns an integer, called index. That is, $$h(\operatorname{key}) = \operatorname{index}$$.  
This integer index is in some range $$[0, \max]$$.  

#### Example of hash function
Let $$p$$ be a prime. Then, $$\max = p - 1$$.  
Assume any $$\operatorname{key}$$ is an integer. Then $$h(\operatorname{key}) = \operatorname{key} \mod p$$ is a hash function.  
Note that is possible (in this case, it's definitely happening) that two different keys go to the same index → called a collision.  

#### Characteristics
In general, a hash function should have the two properties:
1. Easily computable. No matter the size of the key.
2. The output should distribute uniformly over the space (Previously,$$[0, p-1]$$).

Suppose number of keys ~ 10,000  
Then, choose a prime around 1000.  
We shouldn't get more than 10 values (indices) corresponding to the same key. (In uniform distribution, it should happen.)

1. Store in hash table
2. Retrieve a key  

Our aim is that even for a big set of values, we should get uniformly distributed values. → hopefully no bias, that is, many values shouldn't clutter in just one key but spread out equally

We want $$h(\operatorname{key)} \equiv O(1)$$.  

In linked lists, searching is $$O(n)$$ in worst case. Have to go through all. Even if ordered, we don't know the middle pointer.

We don't want any bias, that is, the value should be _reasonably independent_ of the key entered.

## Hash table
Implementation?  
An array of headers.  
Each header will have an `int` `n` and a `list *`. The `n` will keep track of how many collides have happened corresponding to that key.  
The list pointer will point to a linked list having the values corresponding to that.

##### [Prev](/notes/cs-213/lec07) | [Next](/notes/cs-213/lec09)
#### [CS 213](/notes/cs-213)