---
layout: page
title: Order p^n
subtitle: 
image: /img/simple.png
image-link: /alg/groups/simple
comments: true
---
Let $$p$$ be any prime number and let $$n \ge 2$$ be an integer.  
Let $$G$$ be a group with order $$p^n$$. We show that $$G$$ is not simple.  
As $$G$$ is a $$p$$-group, $$Z(G) \neq (1)$$. (See [here](/alg/groups/p-group-nontrivial-center) for proof.)  
If $$Z(G) \neq G$$, then $$Z(G)$$ is a proper nontrivial normal subgroup of $$G$$ and thus, $$G$$ is not simple.  
Now, assume $$Z(G) = G$$. (This means that $$G$$ is abelian.)  
Let $$1 \neq x \in G$$. Then, ord$$(x) = p^m$$ for some $$1 \le m \le n$$.  
Choose $$y = x^{p^{m-1}}$$. Then ord$$(y)=p$$. (How?)  
Let $$H = \langle y \rangle$$. Then, $$H$$ is a proper nontrivial subgroup of $$G$$ which is normal as $$G$$ is abelian.