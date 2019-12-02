---
layout: page
title: Groups of order p^2 are abelian
subtitle: 
image: group.jpg
---
Let $$p$$ be any prime number.  
Let $$G$$ be a group with order $$p^2$$. We show that $$G$$ is abelian.  

As $$G$$ has order of the form $$p^n,$$ we know that $$Z(G) \neq (1).$$ (See proof [here](/alg/groups/p-group-nontrivial-center).)  
Thus, $$|Z(G)| = p$$ or $$|Z(G)| = p^2.$$ In the latter case, we're done as $$Z(G) = G \implies G$$ is abelian.  

Assume $$|Z(G)| = p.$$ We shall arrive at a contradiction.  
Choose $$x \in G\setminus Z(G).$$ (This set is nonempty as $$Z(G)$$ has order strictly less than that of $$G.$$)  
Consider $$H = Z(x) = \{g \in G : gx = xg\},$$ the set of all elements in $$G$$ that commute with $$x.$$  
It is easy to check that $$H$$ is a subgroup of $$G.$$

Claim 1: $$Z(G) \lneq H$$  
_Proof._ The (improper) containment follows immediately by definition.  
To see that it's proper, observe that $$x \in Z(x)$$ but $$x \notin Z(G),$$ by our choice of $$x.$$

Claim 2: $$H \lneq G$$  
_Proof._ Once again, the proper containment is immediate, by definition of $$H.$$  
To see the proper containment, suppose $$H = G.$$ In that case, $$x$$ commutes with every element of $$G.$$ However, then we get that $$x \in Z(G),$$ a contradiction.

Thus, by the above two claims, we get that $$Z(G) \lneq H \lneq G.$$  
This leads to a contradiction as we get that the order of $$H$$ is strictly between $$p$$ and $$p^2$$ but also divides $$p^2.$$  

To summarise, we get that the only possibility is that $$Z(G) = G$$ which gives us that the groups is abelian as every element commutes with every other.