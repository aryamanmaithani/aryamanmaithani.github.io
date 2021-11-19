---
layout: page
title: Order p^n(p + 1)
subtitle: 
image: /img/simple.png
image-link: /alg/groups/simple
comments: true
---

Let $$p$$ be a prime and $$n \ge 1.$$ Then, any group with order $$p^n(p + 1)$$ is not simple.

Indeed, let $$G$$ be such a group. For the sake of contradiction, assume that $$G$$ is simple.  
Note $$n_p \equiv 1 \pmod{p}$$ and $$n_p \mid (p + 1)$$ forces $$n_p \in \{1, p + 1\}$$.  
Since $$G$$ is simple, $$n_p \neq 1$$ and hence, $$n_p = p + 1$$.

Let $$S$$ be the set of Sylow-$$p$$ subgroups of $$G$$. Then, $$|S| = p + 1$$ and $$G$$ acts on $$S$$, giving us a homomorphism $$m : G \to S_{p + 1}$$.  
Since this action is transitive, in view of Sylow theorem (2), we see that $$\ker(m) \neq G$$. Thus, $$\ker(m) = 1$$ since kernels are normal and $$G$$ is simple.

