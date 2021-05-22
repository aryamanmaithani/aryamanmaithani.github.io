---
layout: page
title: Order p^2q
subtitle: 
image: /img/simple.png
image-link: /alg/groups/simple
comments: true
---
Let $$p$$ and $$q$$ be distinct prime numbers.  
Let $$G$$ be a group with order $$p^2q$$. We show that $$G$$ is not simple.  
#### Case 1. p > q
Then, by Sylow Theorem (3), we know that $$n_p \mid q$$ and $$n_p \equiv 1 \mod p$$.  
This gives us that that $$n_p = 1$$ or $$n_p = q$$. However, $$q < p$$ and thus $$q \not\equiv 1 \mod p$$. Thus, $$n_p = 1$$.  
This gives us that $$G$$ is not simple.  
#### Case 2. p < q
Using Sylow Theorem (3) again gives us that $$n_q \in \{1, p, p^2\}$$. If $$n_q = 1$$, then we are done. As $$p < q$$, we again get that $$n_q \neq p$$. Now, we consider the case $$n_q = p^2$$.  
Thus, there are $$p^2$$ Sylow-$$q$$ subgroups of $$G$$. Now, note that each such Sylow-$$q$$ subgroup has order $$q$$, a prime and thus, the intersection of two distinct Sylow-$$q$$ subgroups must be trivial, id est, $$(1)$$.  
Thus, the union of these Sylow-$$q$$ subgroups contains $$d = p^2(q-1)$$ elements, after removing the identity.  
All of these elements have order $$q$$. Now, we are left with $$d' = p^2q - d = p^2$$ elements. Now, we know that $$n_p \ge 1$$ and none of the $$d$$ elements counted above can be a part of a Sylow-$$p$$ subgroup. Thus, the remaining $$d'$$ must form the unique Sylow-$$p$$ subgroup and we get that $$n_p = 1$$.  
Thus, $$G$$ is not simple!