---
layout: page
title: CS 213
subtitle: Lecture 11
image:
---
## Announcements
Mid-semester syllabus  
* stacks → complete
* programming in C++  

Tutorial/problem solving session → Friday 9:30 - 11:00 hours in SIC 301, KR Building  

## Operator properties
Let $$\alpha, \beta, \gamma$$ be some arbitrary binary operators in some hypothetical language.  
Suppose $$\alpha$$ → left associative, $$\beta$$ → right and $$\gamma$$ → non-associative.  
One may have an expression like $$x \alpha y \beta z \gamma u$$. In this case, we don't care about associativity. Only precedence is enough.  
OTOH, we may have something like $$x \alpha y \alpha z \alpha u.$$  
This has one possible interpretation as: $$((x \alpha y) \alpha z) \alpha u$$. If this is the meaning desired, then $$\alpha$$ would be called a left associative operator.  
In the case of right associative, this would be reversed.  
Non-associative means that we cannot write an expression like $$x \gamma y \gamma z$$. It would give an error.  
In C++, there are no non-associative operators. For example, writing something like `x <= y <= z` will not give an error. (However, this will not act in the way you might want it to.)

## Stacks
We can implement it mainly in two ways → arrays and linked lists. (You may think of a new one.)  
#### Array
Data members: an array (static) and a `top` variable. (Note that even though we have an array, we aren't allowed to traverse through it.)  
We have to implement the following methods:  
* `create()`
* `isempty()`
* `isfull()`
* `push()`
* `pop()`
* `peek()`

One may even keep the array and `top` private, so that we can't access them. However, we may use the public methods to make changes.  

#### Linked lists
The `top` here will point to the first guy of the linked list, which will be our stack. This is simple.  

Note that each implementation has its difference in the amount of time it takes. Thus, we should choose implementation based on required usage.

#### Balanced parenthesis problem
We want to check if an expression is well-formed. `(()` is not well formed.  
To check this, we can implement a stack. While we keep reading `(`, we put it in the stack. If we read a `)`, there are two possibilities:  
1. Stack is empty. In this case, it's an ill formed expression.
2. Stack is not empty. In this case, pop the last guy.  
Keep doing this. Then, after the expression is finished reading, we have two options:  
1. Stack is empty. In this case, it's a balanced expression.
2. Stack is not empty. In this case, it's an ill formed expression.  
Then, we accordingly return `true` or `false`.  

We may make a program that tells us more as well. For example, in the case of a bad expression, it tells us the first point of unbalance. In this case of a balanced expression, it tells us which brackets pair up.  

This has some applications → checking some code or something.  

## Function calls and definitions "Recursion"
Stacks are required to permit things like recursive calls.  
Not just recursion, but function calls in general.  
Recursion may also lead to segmentation faults.  
Example:  
```pseudo-code
factorial(n):  
    return n*factorial(n-1)

```
This will not terminate. This will lead to a segmentation as the stack will keep growing. The system gives a certain fixed memory to the program. It won't let it exceed that.

## Data type faults
Professor showed an example that exploits the float representation via program.  
The program doesn't terminate in some cases if we just keep `start != end`. Thus, we should keep something like `start < end`.  

Moral: Every data type has its issues. Be careful when implementing.  
This is not a C++ problem. A problem with float representation itself.

---
  
Another example: reading files. We open two files but the second file is not read. Why?  
We didn't put an `in.close()`.  
We should always check for errors.

## Index sorting 
We are given a list of roll numbers, mobile numbers, hostel numbers and names.  
Suppose we want to display them according to hostel numbers.  
Sorting the whole array will be very costly as we would have to make many swaps.  
Instead, we somehow make a new array that stores the indices in order of the hostels. Then, we print using that.

## Template functions
Template function → use the same function for different templates.  
However, it may not work for some particular templates. Then, we may have to hard-code a function for it differently.  
For example, a function like sorting can work for most templates. It more or less relies on `<`. This will fail if we have a template which does not have a comparison operator. (Like that majority question in the quiz.)  

## Problem solving
* "How to solve" by G. Polya
* Understand the problem by reading the problem carefully and figuring out all the constraints. 
    - If the terrain is unknown, don't jump to write an algorithms.  
    - Work for small instances first. Make observations.
    - Can you prove some of these in general. (Intuitively.)
    - These will give an idea about how to solve.
    - Now, professor demonstrates this for the majority question.

##### [Prev](/notes/cs-213/lec10) | [Next](/notes/cs-213/lec12)
#### [CS 213](/notes/cs-213)