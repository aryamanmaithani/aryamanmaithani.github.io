---
layout: page
title: Cyclic quotient by center
subtitle: 
image: /img/group.png
---

> Let $$G$$ be a group such that the quotient $$G/Z(G)$$ is cyclic. Then $$G$$ is abelian.  

__Proof:__ Let $$x, y \in G$$.   
Let $$gZ(G)$$ be a generator of $$G/Z(G)$$.  
Then, $$xZ(G) = g^aZ(G)$$ and $$yZ(G) = g^bZ(G)$$ for some $$a, b \in \mathbb{Z}$$.  
Note that $$x \in xZ(G) = g^aZ(G)$$ and thus, $$x = g^az$$ for some $$z \in Z(G)$$. Similarly, $$y = g^bz'$$ for some $$z' \in Z(G)$$.  
  
Now, noting that $$z$$ and $$z'$$ commute with $$g$$ and each other, we get that

$$xy = g^azg^bz' = g^{a+b}zz' = g^{b+a}z'z = g^bz'g^az = yx.$$