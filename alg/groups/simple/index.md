---
layout: page
title: Simplicity of Groups
subtitle: 
image: /img/simple.png
image-link: /alg/groups/simple
comments: true
---
Here is something I plan on doing over the winter of 2019 - show groups of order $$n$$ are (not) simple for as many values of $$n$$ as I can.  
## Sylow Theorems
We shall constantly be appealing to the Sylow Theorems and be using the relevant notations.  
Notations: Let $$G$$ be a group with order $$p^nm$$ where $$p$$ is a prime, $$n$$ is a positive integer, and $$p\not\mid m$$.  
Syl$$_p(G) = \{H \le G : |H| = p^n\} = $$ set of subgroups of $$G$$ that have order $$p^n$$.  
An element of Syl$$_p(G)$$ is called a Sylow-$$p$$ subgroup of $$G$$.  
$$n_p := |\operatorname{Syl}_p(G)|$$, the number of Sylow-$$p$$ subgroups of $$G$$.  

Now, we list the Sylow theorems:  
(1) $$n_p \ge 1$$.  
(2) (i) All Sylow-$$p$$ subgroups are conjugates.  
    (ii) If $$H \le G$$ and $$|H| = p^m$$ for some $$1 \le m \le n$$, then $$H$$ is contained in a Sylow-$$p$$ subgroup.  
(3) $$n_p \mid m$$ and $$n_p \equiv 1 \mod p$$.  

#### Corollary of (2) (i) 
Keeping the same notations as before, suppose $$m > 1$$ and $$n_p = 1$$, then $$G$$ is not simple.  
To see this, let $$H$$ be the unique Sylow-$$p$$ subgroup of $$G$$. (This is unique because $$n_p = 1$$.)  
This is clearly a nontrivial proper subgroup of $$G$$. Moreover, let $$g \in G$$. Then, $$gHg^{-1}$$ is also a Sylow-$$p$$ subgroup of $$G$$. By uniqueness, it follows that $$gHg^{-1} = H$$. Thus, $$H$$ is normal and we are done.  

This corollary will be used frequently in concluding that a group is not simple.

### Broad classifications
The letters $$p,$$ $$q,$$ and $$r$$ are used for primes. Moreover, they are assumed to be distinct. $$n$$ is a positive integer.  
* [Order $$p$$](p)
* [Order $$p^n$$](pn) with $$n > 1$$
* [Order $$mp^n$$](pnm) where $$p \not\mid m$$ and $$m < p$$.
* [Order $$p^2q$$](ppq)
* [Order $$pqr$$](pqr)
* [Order $$2^n\cdot3$$](2n3) with $$n > 1$$
* [Order $$3^n\cdot4$$](3n4) with $$n > 1$$

[Here](sieve) is the list of all order $$\le 200$$ that are taken care of, by the above classifications.

### Specific Orders
* [40](40)
* [56](56)
* [60](60) - actually, there does exist a simple group of order 60! (exclamation)
* [72](72)
* [80](80)
* [84](84)
* [90](90)
* [112](112)
* [120](120)
* [126](126)
* [132](132)
* [135](135)
* [140](140)
* [144](144)
* [150](150)
* [160](160)
* [168](168) - actually, there does exist a simple group of order 168! (exclamation)
* [176](176)
* [180](180)
* [189](189)
* [198](198)
* [200](200)