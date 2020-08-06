---
layout: page
title: Special groups of order pq
subtitle: 
image: /img/group.png
---
> Let $$p$$, $$q$$ be primes such that $$p < q$$ such that $$p \nmid q - 1$$.  
> Let $$G$$ be a group of order $$pq$$. Then, $$G$$ is cyclic.  

_Remark:_ The case $$p = q$$ is covered by [this](/alg/groups/p2-groups-abelian) fact.  

__Proof:__ By the Sylow Theorems, $$n_p = n_q = 1$$ is forced. This is because $$p \not\equiv 1 \mod q$$ and $$q \not\equiv 1 \mod p$$.  

Let $$H$$ and $$K$$ be the unique Sylow subgroups of order $$p$$ and $$q$$, respectively. Both of them are normal in $$G$$. (As they are the only Sylow subgroups of that order.)  
Moreover, $$H \cap K = (1)$$, by Lagrange's theorem. Also, every element of $$H$$ commutes with every element of $$K$$. To see this, let $$h \in H$$ and $$k \in K$$. Normality of $$H$$ and $$K$$ tells us that $$hkh^{-1}k^{-1} \in H \cap K = (1)$$.
Thus, 

$$G \cong H \times K \cong \mathbb{Z}_p \times \mathbb{Z}_q \cong \mathbb{Z}_{pq},$$ 

where the last isomorphism follows from the fact that $$p$$ and $$q$$ are relatively prime.