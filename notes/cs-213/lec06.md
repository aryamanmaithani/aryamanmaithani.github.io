---
layout: page
title: CS 213
subtitle: Lecture 6
image:
---
## Binary Search
```C++
int binary_search(int a[SIZE], int elm, int low, int high)  
{  
    //test if array is empty  
    int mid;  
    if(high < low)  
        return -1;  
    else  
    {  
        //calculate midpoint to cut set in half  
        if(a[mid] > elm)  
            return binary_search(a, elm, low, mid-1);  
        else if(a[mid] < elm)  
            return binary_search(a, elm, mid+1, high);  
    };  
    return mid;  
}  
```

#### Complexity
$$T(n) = T(n/2) + c$$

---

## Largest contiguous positive sum in an array of reals
(Check code in slides)  
`max2left`, `max2right`, and `maxcrossing` are the main deals.

#### Complexity
$$T(n) = 2T(n/2) + c n$$  

$$2T(n/2)$$ → two recursive calls  
$$c n$$ → from the two loops of $$n/2$$  

---
---

## Merge sort
Divided the array into two arrays of (approximately) same size, sort them and them interleave them together.  

#### Complexity
$$T(n) = 2T(n/2) + n-1$$

If we have two (sorted) arrays of n elements, what is the cost of making the sorted interleaved array?  
$$A = \{a_1, a_2, ..., a_n\}$$, sorted  
$$B = \{b_1, b_2, ..., b_n\}$$, sorted  

To make interleaved $$S$$, we first compare $$a_1$$ and $$b_1$$. Make the smaller one first, then compare $$a_2$$ with $$b_1$$ or $$a_1$$ with $$b_2$$, as the case may be.  
Continue this.  
This will require ~ $$n$$ comparisons. Will take $$c n$$.  
The divide part is $$2T(n/2)$$.

---

## Fast multiplication of integers
Let $$a$$ and $$b$$ be two $$2n$$$-bits integers, $$a = (a_{2n-1}, a_{2n-2}, ..., a_1, a_0)_2$$ and $$b = (b_{2n-1}, b_{2n-2}, ..., b_1, b_0)_2$$.  

$$A_1 := (a_{2n-1}, a_{2n-2}, ..., a_n)_{2}$$  
$$A_2 := (a_{n-1}, a_{n-2}, ..., a_0)_{2}$$  
$$B_1 := (b_{2n-1}, b_{2n-2}, ..., b_n)_{2}$$  
$$B_2 := (b_{n-1}, b_{n-2}, ..., b_0)_{2}$$  

$$A = 2^nA_1 + A_2$$  
$$B = 2^nB_1 + B_2$$  

$$AB = 2^{2n}A_1B_1 + 2^n(A_1B_2 + A_2B_1) + A_2B_2  \qquad(*)$$  

Now we have __four multiplications__ of n-bit integers, __three additions__ of n-bit integers and __two shift__ operations. (The multiplication with the powers of 2. Multiplying by $$2^n$$ is the same as shifting (<<) $$n$$ bits. Cheap as hecc.)  

Using $$(*)$$ as the divide and conquer strategy, we get:  
$$f(2n) = 4f(n) + 5n$$ or equivalently, $$f(n) = 4 f(n/2) + 5(n/2)$$.  

---

## Matrix multiplication

Assume that $$A$$ and $$B$$ are square matrices of size $$2^n$$.  
Write them as:

$$ A = \begin{bmatrix}
A_1 & A_2 \\  
A_3 & A_4 \\
\end{bmatrix} \text{ and }
B = \begin{bmatrix}
B_1 & B_2 \\  
B_3 & B_4 \\
\end{bmatrix}.
$$ 

Where $$A_i$$ and $$B_i$$ are the submatrices of size $$2^{n-1}$$.

Their product is:

$$
\begin{bmatrix}
A_1B_1 + A_2B_3 & A_1B_2 + A_2B_4\\  
A_3B_1 + A_4B_3 & A_3B_2 + A_4B_4
\end{bmatrix}
$$

Thus, we have reduced (divided) the multiplication problem into multiplication of smaller submatrices.
#### Complexity

$$T(n) = T(n/2) + O(n^2)$$ 
$$O(n^2)$$ is for additions.  

---

The other thing is what has been put in slides.  

---

Aim (expectation) of lecture: Skill to formulate the recursive relation for a given algorithm.  

Solving is what will come next. (Maybe not full solution in class. :/)  

---
---

## Solving recursive

$$f(n) = a f(n/b) + g(n)$$  

$$a$$ → Number of subproblems  
$$n/b$$ → size of each subproblem  
$$g(n)$$ → conquer step

$$f(n) = a^2 f(n/b^2) + a g(n/b) + g(n)$$  
.  
.  
.  
$$f(n) = a^k f(n/b^k) + \displaystyle\sum_{i=0}^{k-1} a^i g(n/b^i)$$

Assume $$n = b^k$$. (Can work around this.)  
Then, we get  
$$f(n) = a^kf(1) + \displaystyle\sum_{i=0}^{k-1} a^i g(n/b^i)$$  
The last summation is usually a pain to deal with.  

#### Special case
$$g(n) = c$$ (constant)  

Also assume that $$a = 1$$ (Binary search type.)  
Then, $$f(n) = f(1) + c k$$  
Recall that $$k = \log_b n$$. Thus,

> $$f(n) = O(\log n).$$

---

Now, let us assume $$a > 1$$. ($$g$$ still constant)  

Then, $$f(n) = a^kf(1) + c\left(\dfrac{a^k - 1}{a - 1}\right) = c_1a^k + c_2 \sim a^k.$$
Note that $$a^k = a^{\log_b n}$$ and thus,  
> $$f(n) = O(n^{\log_ba}).$$

#### Case that g is linear
$$f(n) = af(n/b) + cn$$  
$$f(n) = a^kf(1) + cn\left(1 + \left(\frac{a}{b}\right) + \cdots + \left(\frac{a}{b}\right)^{k-1} \right)$$

Let us take the case that a = b = 2.
$$f(n) = c_12^k + c_2kn \sim c_1'n + c_2kn$$  
Both the terms have an n term. k will dominate the whole thing giving
> $$f(n) = O(n \log n).$$

## Master Theorem
Let f be an increasing function satisfying
$$f(n) = af(n/b) + cn^d$$  
where $$a \ge 1$$, $$b > 1$$, $$c > 0$$ and $$d \ge 0$$.  
Then the time complexity is given by:  

$$O(n^d) \; ; \; a < b^d$$  
$$O(n^d\log_b n) \; ; \; a = b^d$$  
$$O(n^{\log_b a}) \; ; \; a > b^d$$  

---

Strassen's scheme for matrix multiplication:  
$$T(n) = 7T(n/2) + c n^2.$$  
Thus, $$T(n) = O(n^{\log_27}).$$

---
---

## Linked List
This is the next thing to do.  
We'll do pointers.  

#### Motivation
Consider $$p(x) = a_1x^{200} + a_2a^{100} + a_3 $$.  
Very few nonzero coefficients but degree high.  
If we use the _dense representation_, then it is quite bad. (Storing _all_ the coefficients in an array of 201 elements.)  

We'll now describe the polynomial using a collection of tuples.  
[$$a_1$$, 200], [$$a_2$$, 100], [$$a_3$$, 0]  

Note that in dense, we didn't have to pair up the degree as that was done implicitly.  

---

Now, if I have to add, subtract, yada yada, what will we do in sparse representation?  
Linked lists will help us here!  
We don't need to know a priori what the size of polynomial is. In fact, the coefficients need not even be given in order.  

We need the following stuff:  
→ `new()`  `delete()`  
→ pointers  
Note that the data stored here need not be contiguous  
→ `class` (keeps track of where's the next data)

We should be able to define a class in C++. Not as professional as SQL classes maybe but still nice.

---

---

### Words from Samad:  
→ Most of us have done fine. (In regards to tutorial 1.)  
→ He wants us to focus on time analysis.  
→ We shouldn't care about how small stuff. Take every constant stuff as 1 unit. Care only asymptotic stuff.  
→ Assignment 1 today evening. Next week deadline.  
→ Easy to copy from Internet but easy to catch also. :(  
→ Don't copy. You won't be able to get away.  
→ We'll get caught in the end. People got screwed in ICPC for plagiarism.  
→ Prof: "I care only about your effort, not clean code."
