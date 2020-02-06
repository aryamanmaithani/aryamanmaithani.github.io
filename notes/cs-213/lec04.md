---
layout: page
title: CS 213
subtitle: Lecture 4
image:
---
# Writing programs
* Choosing appropriate data types → min memory, can store all values required  
* Global/static/local variables → should select one in a justified manner
								→ pro/cons for taking a decision
* Functions to write your programs, main() should be very small
	→ type of arguments → our choice from C++. Value, reference, pointer? Justify  
	→ overloading  
	→ template functions  

# Numerical algorithms
* Linear equations  
* Polynomial roots  
* Numerical integration  
* Solving ODE/PDE  

Use numerical algorithms when we can't solve analytically. Don't use it for roots of quadratic/cubic/quartic. Same when we can actually integrate or solve PDEs.  
Use numerical algorithms when no closed form.

## Interval halving
We need to first find two points between which the function changes its sign.  
Suppose we have a polynomial, can we use the coefficients to find a suitable interval?  

## Newton Raphson
$$x_{n+1} = x_n - f(x_n)/f'(x_n)$$  

Polynomial can be evaluated at any point.  
Construct $$p'(x)$$ given $$p(x)$$.  

$$e_{n+1} = ce_n^2$$, $$e_n$$ is the error at $$n$$-th step.  
Using this, justify how many times we should run a while loop.

NR shows different behaviour if we have repeated roots.  


Polynomial: Suppose we have distinct roots which are reasonably separated.  
$$P(x)$$ : roots are 1, 2, 3, 4, 5  
Suppose we can create a polynomial with square roots  
$$P_1(x)$$ : roots are 1, 4, 9, 16, 25   
And then, $$P_2(x)$$ - 1, 16, 81, 256, 625  

coeff of $$x^4$$ in the last polynomial: 625 + 256 + 81 + 16 + 1  ~ 625 → take fourth roots (this is the spirit)
In reality, the sum is 979 → 5.59...  
Then find the next by looking at $$x^3$$  

Programming part - find the coefficients of $$P_1$$, $$P_2$$  
Need a method to do that without knowing the roots.  
> Hint: Consider $$P(x)P(-x)$$

##### [Prev](/notes/cs-213/lec03) | [Next](/notes/cs-213/lec05)
#### [CS 213](/notes/cs-213)