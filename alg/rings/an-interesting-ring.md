---
layout: page
title: An interesting ring
---

$$\newcommand{\Spec}{\operatorname{Spec}}$$

Consider the following ring

$$R = \prod_{i = 1}^{\infty}\mathbb{Z}/2\mathbb{Z}.$$

I will now show that this is an interesting ring, a ring you should care about.

<!-- MarkdownTOC autolink="true" -->

- [Not Noetherian](#not-noetherian)
- [Every prime ideal is maximal](#every-prime-ideal-is-maximal)
- [The poset Spec\(R\) has the Noetherian property](#the-poset-specr-has-the-noetherian-property)
- [The topological space Spec\(R\) is not Noetherian](#the-topological-space-specr-is-not-noetherian)
- [R\_p is Noetherian for every prime p](#r_p-is-noetherian-for-every-prime-p)

<!-- /MarkdownTOC -->

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

## The poset Spec(R) has the Noetherian property

To be more precise, any increasing chain of prime ideals

$$\mathfrak{p}_1 \subset \mathfrak{p}_2 \subset \mathfrak{p}_3 \subset \cdots$$

stabilises.

However, this is clear at once because every prime is maximal.

## The topological space Spec(R) is not Noetherian

Recall that a topological space $$X$$ is said to be Noetherian if every increasing chain

$$U_1 \subset U_2 \subset U_3 \subset \cdots$$

of open subsets of $$X$$ stabilises. Equivalently, every decreasing chain of closed subsets must stabilise.

Also recall that $$\Spec(R)$$ is a topological space in the [Zariski topology](https://en.wikipedia.org/wiki/Spectrum_of_a_ring#Zariski_topology). (We shall use the same notation as in the link.)

Consider the following ideals in $$R$$: 

$$I_n = \underbrace{\mathbb{Z}/2\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/2\mathbb{Z}}_{n} \oplus 0 \oplus \cdots$$

for $$n \in \mathbb{N}$$.

We have

$$I_1 \subset I_2 \subset \cdots$$

which gives us a decreasing chain of closed sets

$$V(I_1) \supset V(I_2) \supset \cdots.$$

We show that the inclusions are strict. It suffices to show that for each $$n$$, there exists a prime ideal $$\mathfrak{p}_n$$ containing $$I_n$$ and not $$I_{n+1}$$.

It can be verified that

$$\mathfrak{p}_n = \underbrace{\mathbb{Z}/2\mathbb{Z} \times \cdots \times \mathbb{Z}/2\mathbb{Z}}_{n} \times 0 \times \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \times \cdots$$

is an ideal in $$R$$ which contains $$I_n$$ and not $$I_{n+1}$$. To see that it is prime, note that $$R/\mathfrak{p}_n \cong \mathbb{Z}/2\mathbb{Z}$$. $$\blacksquare$$

## R\_p is Noetherian for every prime p

Note that this is interesting because this shows that being Noetherian is not a "local" property.

To prove this, we recall that we have the following bijection

$$\Spec(R_{\mathfrak{p}}) \longleftrightarrow \{\mathfrak{q} \in \Spec(R) : \mathfrak{q} \subset \mathfrak{p}\}.$$

Since every prime ideal in $$R$$ is maximal, we get that the only element in the right set is $$\mathfrak{p}$$. Thus, $$\Spec(R_{\mathfrak{p}})$$ is a singleton. Moreover, $$\mathfrak{p}_{\mathfrak{p}}$$ is the unique maximal ideal of $$R_{\mathfrak{p}}$$. We show that $$\mathfrak{p}_{\mathfrak{p}} = 0$$ and conclude that $$R_{\mathfrak{p}}$$ is a field. This would show that $$R_{\mathfrak{p}}$$ is Noetherian.

Now, recall that the intersection of all prime ideals gives us the nilradical (the ideal of all nilpotent elements) of the ring. Since $$\Spec(R_{\mathfrak{p}})$$ is a singleton, we see

$$\mathcal{N}(R_{\mathfrak{p}}) = \mathfrak{p}_{\mathfrak{p}}.$$

We contend that there are no non-zero elements in the nilradical. Indeed, suppose that $$\frac{x}{a} \in R_{\mathfrak{p}}$$ is nilpotent. This would imply that $$\frac{x}{1}$$ is nilpotent. However, for any $$n \in \mathbb{N}$$, note that

$$\left(\frac{x}{1}\right)^n = \frac{x^n}{1^n} = \frac{x}{1}$$

since every element of $$R$$ is idempotent. Thus, there are no nonzero nilpotents in $$R_{\mathfrak{p}}$$ and thus,

$$\mathfrak{p}_{\mathfrak{p}} = \mathcal{N}(R_{\mathfrak{p}}) = 0,$$

as desired. $$\blacksquare$$