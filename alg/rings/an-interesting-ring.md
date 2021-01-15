---
layout: page
title: An interesting ring
---

$$\newcommand{\Spec}{\operatorname{Spec}}$$

Consider the following ring

$$R = \prod_{i = 1}^{\infty}\mathbb{Z}/2\mathbb{Z}.$$

I will now show that this is an interesting ring, a ring you should care about.

## Not Noetherian

Recall that a ring is said to be Noetherian if every increasing chain of ideals

$$I_1 \subset I_2 \subset I_3 \subset \cdots$$

_stabilises,_ that is, there exists $$n \in \mathbb{N}$$ such that $$I_{n + i} = I_n$$ for all $$i \ge 1$$.

Letting $$e_i \in R$$ denote the element which is non-zero precisely at the $$i$$-th component, we see

$$\langle e_1\rangle \subsetneq \langle e_1, e_2\rangle \subsetneq \langle e_1, e_2, e_3\rangle \subsetneq \cdots.$$

Thus, $$R$$ is not Noetherian. $$\blacksquare$$

## Every prime ideal is maximal

Let $$\mathfrak{p} \in \Spec(R).$$ (Recall that $$\Spec(R)$$ is the collection of all prime ideals of $$R$$. More on this later.)

We show that $$\mathfrak{p}$$ is maximal. 

First, we note that $$x^2 = x$$ for all $$x \in R$$. Let $$S = R/\mathfrak{p}$$. Since $$\mathfrak{p}$$ is prime, $$S$$ is an integral domain. Moreover, $$y^2 = y$$ holds for all $$y \in S$$ as well.  
However, $$S$$ is an integral domain. Thus, $$y^2 = y$$ forces that $$y = 0, 1$$. Thus, $$S$$ has exactly two elements. ("At most" is clear. "At least" follows since primes are proper.)

Thus, we conclude that $$S \cong \mathbb{Z}/2\mathbb{Z}$$. However, since this is a field, we conclude that $$\mathfrak{p}$$ is maximal. $$\blacksquare$$

## The poset $$\Spec(R)$$ has the Noetherian property

To be more precise, any increasing chain of prime ideals

$$\mathfrak{p}_1 \subset \mathfrak{p}_2 \subset \mathfrak{p}_3 \subset \cdots$$

stabilises.

However, this is clear at once because every prime is maximal.

## The topological space $$\Spec(R)$$ is not Noetherian

Recall that a topological space $$X$$ is said to be Noetherian if every increasing chain

$$U_1 \subset U_2 \subset U_3 \subset \cdots$$

of open subsets of $$X$$ stabilises. Equivalently, every decreasing chain of closed subsets must stabilise.

Also recall that $$\Spec(R)$$ is a topological space in the [Zariski topology](https://en.wikipedia.org/wiki/Spectrum_of_a_ring#Zariski_topology). (We shall use the same notation as in the link.)

Consider the following ideals in $$R$$: 

\begin{aligned}
	I_1 &= \mathbb{Z}/2\mathbb{Z} \oplus 0 \oplus 0 \oplus \cdots\\  
	I_2 &= \mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z} \oplus 0 \oplus \cdots\\  
	&\vdots\\  
	I_n &= \underbrace{\mathbb{Z}/2\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/2\mathbb{Z}}_{n} \oplus 0 \oplus \cdots
\end{aligned}

We have

$$I_1 \subset I_2 \subset \cdots$$

which gives us a decreasing chain of closed sets

$$V(I_1) \supset V(I_2) \supset \cdots.$$

We show that the inclusions are strict. It suffices to show that for each $$n$$, there exists a prime ideal $$\mathfrak{p}_n$$ containing $$I_n$$ and not $$I_{n+1}$$.

It can be verified that

$$\mathfrak{p}_n = \underbrace{\mathbb{Z}/2\mathbb{Z} \times \cdots \times \mathbb{Z}/2\mathbb{Z}}_{n} \times 0 \times \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \times \cdots$$

is an ideal in $$R$$ which contains $$I_n$$ and not $$I_{n+1}$$. To see that it is prime, note that $$R/\mathfrak{p}_n \cong \mathbb{Z}/2\mathbb{Z}$$.