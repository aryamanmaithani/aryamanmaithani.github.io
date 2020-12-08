---
layout: page
title: Collection of rings
subtitle: Some useful rings
---

$$\newcommand{\Max}{\operatorname{Max}}$$
$$\newcommand{\Spec}{\operatorname{Spec}}$$

Given a commutative ring $$R$$, $$\Max(R)$$ denotes the set of its maximal ideals and $$\Spec(R)$$ its prime ideals.  
The $$0$$ ring is neither considered an integral domain nor a field.

# $$\mathbb{Z}$$
* Integral domain
* Euclidean domain
* PID
* UFD

### Ideals
* All ideals are of the form $$\langle n\rangle$$ for some $$n \in \mathbb{Z}$$
* $$\Max(\mathbb{Z})$$ $$=\{\langle p\rangle : p \text{ is prime}\}\cup\{\langle 0\rangle\}$$
* $$\Spec(\mathbb{Z})$$ $$=\Max(\mathbb{Z})\cup\{\langle 0\rangle\}$$

### Special elements
* Nilpotents: only $$0$$
* Zero divisors: only $$0$$
* Units: $$\pm 1$$

---

# $$\mathbb{Z}/n\mathbb{Z}$$
* An integral domain iff $$n$$ is prime or $$0$$
* A field iff $$n$$ is prime
* All ideals are principal

### Ideals
* Ideals are of the form $$m\mathbb{Z}/n\mathbb{Z}$$ where $$m \mid n$$.

### Special elements
* Nilpotents: $$\bar{m}$$ such that $$m$$ is divisible by every prime that divides $$n$$
* Zero divisors: $$\bar{m}$$ such that $$(m, n) \neq 1$$
* Units: $$\bar{m}$$ such that $$(m, n) = 1$$

---

# $$\Bbbk[x]$$
$$\Bbbk$$ is a field
* Integral domain
* Euclidean domain
* PID
* UFD

### Ideals
* All ideals are of the form $$\langle p(x)\rangle$$ for some $$p(x) \in \Bbbk[x]$$
* $$\Max(\Bbbk[x])$$ $$= \{\langle p(x)\rangle : p(x) \text{ is irreducible}\}\cup\{\langle 0\rangle\}$$
* $$\Spec(\Bbbk[x])$$ $$=\Max(\Bbbk[x])\cup\{\langle 0\rangle\}$$

### Special elements
* Nilpotents: only $$0$$
* Zero divisors: only $$0$$
* Units: nonzero constant polynomials

---

# $$\Bbbk [\![x]\!]$$
$$\Bbbk$$ is a field
* Integral domain
* Euclidean domain
* PID
* UFD

### Ideals
* Ideals are precisely of the following type: $$\langle 0\rangle, \langle 1\rangle$$, or $$\langle x^n\rangle$$ for some $$n \ge 1$$
* $$\Max(\Bbbk[\![x]\!])$$ $$=\{\langle x\rangle\} $$
* $$\Spec(\Bbbk[\![x]\!])$$ $$=\{\langle x\rangle, \langle 0\rangle\}$$

### Special elements
* Nilpotents: only $$0$$
* Zero divisors: only $$0$$
* Units: power series with nonzero constant term

---

# $$\mathbb{Z}[\sqrt{-5}]$$

* Integral domain
* Not Euclidean
* Not PID
* Not UFD
