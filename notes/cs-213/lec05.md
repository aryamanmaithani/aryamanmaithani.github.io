---
layout: page
title: CS 213
subtitle: Lecture 5
image:
---
# Topics for next 4 lectures
* Strings in C++ problems, solving with strings
* Divide and conquer algorithms design, analysis + examples  
* Linked list data structure, problems for illustration  
	Create out own implementation, analysis
* Hash table organisation, applications, analysis  

Somewhere in between → tutorial and quiz (post dinner some day, Wed/Friday)

# Strings in C++
Many important stuff happen in text.  
WhatsApp, reviews of restaurants, et cetera  

Given a passage, tell the theme of the passage.  
Passage → Important words (using some frequency analysis probably) → Top ten words → give a title

### What is a string?
(Definition should be independent of programming language)  
Alphabet $$\Sigma$$ → (finite) set of symbols  
String over $$\Sigma$$: 
Empty string $$\epsilon$$ → length 0  
$$\Sigma^* = \Sigma \cup \Sigma^1 \cup \Sigma^2 \cup ... $$ 

Assume $$|\Sigma| = 100$$.  
Then, the set of words of length $$\le 100$$ has cardinality $$1 + 100 + \cdots + 100^{100} = (100^{101} - 1)/99$$  

> Q. What is the largest string length in (standard) C++? Experiment.  

## Code
```C++
include <string>  
using namespace std;  
string s1, s2;
```
s1, s2 → empty strings, can check it using:  
`s1.length()` returns length of the string  
In general, we can do `stringboject.method()`.  

Can use `==` and `!=`; e.g., `s1 == s2` will return true if they're both empty. (Like at the time of initialisation.)

Can make arrays also. `string name[100]`, thus it's a *proper* data type.  
Can use `+` for concatenation.  

Search or find → strings can be accessed as if an array of characters.  

Given a path, how many directories? Count the number of non-contiguous colons.  
Can also ask what the deepest directory is.

`$ cat $PATH` displays the content on the screen. Example - `cat randinp`

> Question: Take last 100 emails.  
> How many people have written to you?  
> The dates and times.  

# Divide and conquer
Binary search: $$T(n) = T(n/2) + 3$$

In general, we may divide the problem into $$a$$ parts, each of size $$n/b$$. ($$b = a$$ is not necessary, maybe not disjoint.)  
Then, $$T(n) = aT(n/b) + g(n).$$  
(In the case of binary sort, we didn't have to analyse both parts.)

$$T(n) = a(aT(n/b^2) + g(n/b)) + g(n) = a^2T(n/b^2) + a g(n/b) + g(n) = ...$$  

If $$g(n)$$ is polynomial, say $$n^d$$, then we know the complexity $$T(n)$$ as a function of $$n$$. (Master's Theorem)

##### [Prev](/notes/cs-213/lec04) | [Next](/notes/cs-213/lec06)
#### [CS 213](/notes/cs-213)