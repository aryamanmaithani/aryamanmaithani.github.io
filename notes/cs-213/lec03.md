---
layout: page
title: CS 213
subtitle: Lecture 3
image:
---
# Analyse Code

| Work   			| Cost		     									|
|-------------------|---------------------------------------------------|	
| Assignment		| 1 unit 											|
| Operation 		| 1 unit   											|
| Array reference	| 2 units 											|
| Comparison	 	| 1 unit 											|
| if-then-else 		| cost(condition) + cost(then) + cost(else) + 2 	|
| 	 				| [2 for jumps]										|
| for loop	 		| body once = 3 + cost(body)						|
| function call 	| cost(body) + 10									|
| 	 				| [10 for calling and returning]					|

Note that we're only looking at time, so we've ignored declarations (space).

# Example
```C++
unsigned short search(int a[], unsigned short size, int elt){  
	unsigned short pos = -1;			// cost 1  
	for(unsigned short i = 0; i < size; i++)	//3  
		if(a[i] == elt)				//2 + 1, array + comparison  
			return pos = i;			//6  
	return pos;  
}		
```

Execution of search over an array of n elements: $$9n + 1 \sim c_1n + c_2$$

# Big-O Notation

Let $$f, g: \mathbb{Z} \to \mathbb{R}$$.  
The function $$f(x)$$ is said to be of $$O(g(x))$$ if there are constants $$C$$ and $$k$$ such that $$|f(x)| \le C|g(x)|$$ for all $$x > k$$.  

The constants $$C$$ and $$k$$ are called *witnesses* to the relationship of $$f(x)$$ being of $$O(g(x))$$.

E.g. $$f(x) = 9x + 1$$, $$g(x) = 10$$  
$$C = 1$$, $$k = 1$$ works and thus, $$f(x)$$ is of $$O(10x)$$ and also of $$O(x)$$.

E.g. $$f_1(x) = log_2(x)$$, $$f_2(x) = \sqrt{x}$$  
Have to find $$C$$ and $$k$$ to claim $$f_1(x)$$ is of $$O(f_2(x))$$.  

## Results
$$f(x) = \sum_{i = 0}^{i = n}a_ix^i$$, then $$f(x) = O(x^n)$$. (Assuming $$a_n \neq 0$$.)  
$$n! = O(n^n)$$  
$$\log n! = O(n \log n)$$  

# Numerical application
## Polynomial = p(x) = $$\sum_{i = 0}^{n} a_i x^i$$
Given a polynomial, the following are natural operations to do with it.    
* Evaluate it at a point, $$P(x_0)$$  
* Find the roots  
* Extrema in domain  
* $$P_1(x) + P_2(x)$$, $$P_1(x)P_2(x)$$, $$P_1(x) \% P_2(x)$$  
* Given roots (data), construct *the* polynomial satisfying that stuff. (Clearly, something is missing. Maybe assume monic.)  

How do you represent a polynomial?  
* Array, possibly. $$4x^5 - 3x^3 + x^2 + 250 \to [250, 0, 1, -3, 0, 4]$$
** Not good for *sparse* polynomials like $$9x^{200} - 5x^{100} + 10$$  
	$$\{10, 0\},\; \{-5, 100\},\; \{9, 200\}$$
	But this is not v good for the cases where we have contiguous exponents.

Evaluating at a point. Cost?  
* Blind way: $$a_0 + a_1 x + ... + a_n x^n$$, do every operation  
	$$n$$ additions  
	$$1 + 2 + \cdots + n$$ multiplications = $$n(n+1)/2$$ multiplications  
	~ $$O(n^2)$$  

	$$4x^5 - 3x^3 + x^2 + 250 = ((4x^2 - 3)x + 1)x^2 + 250$$  
	~ $$O(n)$$

Can we do better than $$O(n)$$?  
No. In worst case scenario, we have $$n$$ different coefficients (as input) and we do need to look at them at least once.

## Matrix: $$n^2$$ elements  
A * B  
Output: $$n^2$$ elements 
Should expect algorithm of $$O(n^2)$$. → No one has gotten close to this.  
However, we don't have a better (proven) lower bound.  
Has gotten down to $$O(n^{2.49})$$.  
In class, we'll look at one algorithm of complexity $$O(n^3)$$.  

## All roots of a polynomial of degree $$n$$  
* Newton Raphsson
* Interval half
* Graephe's Root square -> Gives all n roots (approx, of course) simultaneously

##### [Next](/notes/cs-213/lec04)
#### [CS 213](/notes/cs-213)