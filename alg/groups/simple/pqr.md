---
layout: page
title: Order pqr
subtitle: 
image: /img/simple.png
image-link: /alg/groups/simple
comments: true
---
Let $$p$$, $$q$$, and $$r$$ be distinct prime numbers.  
WLOG, we may assume that $$p < q < r$$.  
Let $$G$$ be a group with order $$pqr$$.  
We shall be appealing to the Sylow theorems without mentioning it explicitly.  
If any of $$n_p$$, $$n_q$$, or $$n_r$$ is equal to $$1$$, then we know that $$G$$ is not simple.  
For sake of contradiction assume that each of the above is strictly greater than $$1$$.  
As $$n_r \mid pq$$ and $$p, q < r$$, we get that $$n_r = pq$$. (Since we have assumed that $$n_r > 1$$.)  
Thus, there are $$pq$$ Sylow-$$r$$ subgroups of $$G$$. Now, note that each such Sylow-$$r$$ subgroup has order $$r$$, a prime and thus, the intersection of two distinct Sylow-$$r$$ subgroups must be trivial, id est, $$(1)$$. Thus, the number of elements having order $$r$$ equals $$o_r = pq(r-1)$$.  
Now, $$n_q > 1$$ and $$n_q \mid pr$$. Thus, $$n_q \in \{p, r, pr\}$$. However, $$n_q \equiv 1 \mod q$$ and thus, $$n_q \neq p$$. This gives us that $$n_q \ge r$$. Thus, the number of elements having order $$q$$ equals $$o_q \ge r(q-1)$$.  
Lastly, similar argument as earlier gives us that $$o_p \ge q(p-1)$$.  
Note that $$o_r$$, $$o_q$$, and $$o_p$$ are counting distinct non-identity elements and thus,  
$$|G| \ge o_r + o_q + o_p + 1 \ge pq(r-1) + r(q-1) + q(p-1)$$  
$$\implies |G| \ge pqr + rq - r - q + 1 = pqr + \underbrace{(r-1)(q-1)}_{>0} > pqr$$.  
Thus, we have a contradiction as $$|G| = pqr$$ and we are done!