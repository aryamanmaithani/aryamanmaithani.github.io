---
layout: page
title: Sylow exercises
subtitle: 
image: /img/group.png
---

Uh, this is an incomplete set of solutions for Exercise 4.5 of Dummit Foote. Maybe I shall update them someday.

---

General stuff:  
Whenever we write $${\vert}G{\vert} = p^\alpha m$$, it is understood that $$p \nmid m$$.  
$$n_p$$ will denote the number of Sylow $$p$$-subgroups of $$G$$.  

We shall use the representation of $$D_{2n}$$ as used in the book, that is,

$$D_{2n} = \langle r, s \mid r^n = s^2 = 1,\ rs = sr^{-1}\rangle$$

and thus, every element can be written (uniquely) as $$s^ir^j$$ for some $$0 \le i < 2$$ and $$0 \le j \le n$$.  
We also recall that every element of $$D_{2n}$$ which is not a power of $$r$$ has order 2.

---

1. Prove that if $$P \in Syl_P(G)$$ and $$H$$ is a subgroup of $$G$$ containing $$P$$, then $$P \in Syl_P(H)$$. Give an example to show that, in general, a Sylow $$p$$-subgroup of a subgroup of $$G$$ need not be a Sylow $$p$$-subgroup of $$G$$.  

    __Solution:__ We are given $$P \le H \le G$$ with $${\vert}P{\vert} = p^\alpha$$ and $${\vert}G{\vert} = p^\alpha m$$ such that $$p \nmid m$$.  
    As $${\vert}P{\vert} \mid {\vert}H{\vert}$$, we get that $${\vert}H{\vert} = p^\alpha k$$ for some $$k \in \mathbb{N}$$.  
    Moreover, $${\vert}H{\vert} \mid {\vert}G{\vert}$$ and thus, $$k \mid m$$. As $$p \nmid m$$, we get that $$p \nmid k$$.  
    Thus, $$P$$ is a Sylow $$p$$-subgroup of $$H$$.  
      
    For the second part, consider $$G = \mathbb{Z}_4$$ and $$H = \{\bar{0}, \bar{2}\}$$. Then $$P = H$$ is a Sylow $$2$$-subgroup of $$H$$ but not one of $$G$$.

    ---

2. Prove that if $$H$$ is a subgroup of $$G$$ and $$Q \in Syl_p(H)$$ then $$gQg^{-1} \in Syl_p(gHg^{-1})$$ for all $$g \in G$$.  

    __Solution:__ We first note that $$gQg^{-1}$$ is indeed a subgroup of $$gHg^{-1}$$.  
    The assertion follows from the fact that $${\vert}gQq^{-1}{\vert} = {\vert}Q{\vert}$$ and $${\vert}gHg^{-1}{\vert} = {\vert}H{\vert}$$.

    ---

3. Use Sylow's theorem to prove Cauchy's theorem.  

    __Solution:__ Recall that Cauchy's theorem says that if $$G$$ is a finite group such that $$p \mid {\vert}G{\vert}$$ for some prime $$p$$, then $$G$$ has an element of order $$p$$.  
    To prove this, let $$G$$ and $$p$$ be as above and $$P$$ be a Sylow $$p$$-subgroup of $$G$$. (Existence of $$P$$ is given by the Sylow theorems.)  
    Let $$G = p^\alpha m$$ with usual meanings. Then, $${\vert}P{\vert} = p^\alpha.$$  
    Consider $$x \in P$$ such that $$x \neq 1$$. Then, the order of $$x$$ is $$x^\beta$$ for some $$1 \le \beta \le \alpha$$.  
    Consider $$y = x^{p^{\beta - 1}}.$$ Then, order of $$y$$ is $$p$$. (How? It is clear that $$y^p = 1$$. Thus, the only other possibility for the order is $$1$$ but that is not possible since $$y \neq 1$$ as $$p^{\beta - 1} < p^{\beta}$$, the order of $$x$$.)

    ---

4. Exhibit all Sylow 2-subgroups and Sylow 3-subgroups of $$D_{12}$$ and $$S_3 \times S_3$$.  

    __Solution:__   
    $$D_{12}$$:  
    Note that $${\vert}D_{12}{\vert} = 12 = 2^{2}\cdot3$$. Thus, the Sylow 2-subgroup(s) will have order 4 and Sylow 3-subgroup(s) will have order 3.  

    Sylow 3:  
    Note that a Sylow 3-subgroup must necessarily be isomorphic to $$\mathbb{Z}_3$$. Since all elements not of the form $$r^k$$ have order 2, we just find powers of $$r$$ which have order 3. These turn out to be $$r^2$$ and $$r^4$$. As $$\langle r^2\rangle = \langle r^4\rangle$$, we have a unique Sylow 3-subgroup:

    $$\langle r^2\rangle.$$

    Sylow 2:  
    Note that no element of $$D_{12}$$ has order 4. (Any such element would have to be a power of $$r$$ but 4 does not divide 6, the order of $$r$$.)  
    Thus, any Sylow 2-subgroup must be isomorphic to $$\mathbb{Z}_2 \times \mathbb{Z}_2$$.  
    Every element of this group must have order 2. $$r^3$$ is the only power of $$r$$ which has order 2. Thus, the other two elements must be of the form $$sr^{k}$$. Noting that the multiplication of two such elements is:

    $$sr^{k} \cdot sr^{k'} = r^{k' - k},$$

    we get that $${\vert}k - k'{\vert} = 3$$. This gives us three such groups which are all the Sylow 2-subgroups:

    $$\langle s, sr^3\rangle,\ \langle sr, sr^4\rangle,\ \langle sr^2, sr^5\rangle.$$

    (It can be checked that all of these are distinct subgroups.)

    $$S_3 \times S_3$$:  
    The order of the group is $$36 = 2^2\cdot 3^2$$. Thus, the Sylow 2-subgroup(s) will have order 4 and Sylow 3-subgroup(s) will have order 9.  

    Sylow 2:  
    Note that there are three subgroups of order 2 of $$S_3$$: $$\langle (12)\rangle,\ \langle (13)\rangle,\ \langle 23\rangle.$$ Let these be $$H_1, H_2, H_3$$. (Note that these are indeed distinct.)  
    Then, the nine products:  
      
    $$H_i \times H_j \quad i, j \in \{1, 2, 3\}$$

    are subgroups of $$S_3 \times S_3$$ have order 4. This gives us nine Sylow 2-subgroups. However, by the Sylow theorems, $$n_2 \mid 9$$ and thus, there can't be any more.

    Sylow 3:  
    Let $$P$$ be a Sylow 3-subgroup. Note that no element of $$S_3 \times S_3$$ has order 9. Thus, every non-identity element of $$P$$ must have order 3. Now, note that the order of an element $$(\sigma, \tau) \in S_3 \times S_3$$ is the lcm of the orders of $$\sigma$$ and $$\tau$$. This gives us that there are 8 elements of order 3. These elements together with the identity do form a subgroup and moreover, there can't be any other. Thus, there is a unique Sylow 3-subgroup which is:

    $$\langle (123)\rangle \times \langle (123)\rangle.$$

    ---

5. Show that a Sylow $$p$$-subgroup of $$D_{2n}$$ is cyclic and normal for every odd prime $$p$$.

    __Solution:__ Let $$2n = p^\alpha m$$ as usual. As $$p$$ is odd and $$2n$$ is even, we must have that $$m = 2m'$$ for some $$m \in \mathbb{N}$$. Thus, $$n = p^\alpha m'$$ with $$p \nmid m'$$.  
    Note that $$r$$ has order $$n$$ and hence, $$r^{m'}$$ has order $$p^\alpha$$. Hence, $$\langle r^{m'}\rangle$$ is Sylow p-subgroup of $$D_{2n}$$.  
      
    We now show that is normal. To do this, it is enough to work with the generators of $$D_{2n}$$. Clearly, $$r(r^{m'})r^{-1} \in \langle r^{m'}\rangle$$. Also, $$s(r^{m'})s^{-1} = s^2r^{-m'} = r^{-m'} \in \langle r^{m'}\rangle$$.  
    Thus, $$\langle r^{m'}\rangle$$ is normal.  
      
    As all Sylow p-subgroups are conjugates, we get that the above Sylow p-subgroup is the unique Sylow p-subgroup. As it is cyclic and normal, we are done.

    ---

6. Exhibit all Sylow 3-subgroups of $$A_4$$ and all Sylow 3-subgroups of $$S_4$$.

    __Solution:__ $$A_4$$: Clearly, $$n_3 \mid 4$$. We exhibit 4 such Sylow 3-subgroups now:

    $$\langle (123)\rangle,\ \langle (124)\rangle,\ \langle (134)\rangle, \ \langle (234)\rangle.$$

    (Note that these are indeed distinct subgroups.)  
    These were easy to find as a Sylow 3-subgroup must have order 3 and thus, must be isomorphic to $$\mathbb{Z}_3$$. It was then a matter of finding elements of order 3.

    $$S_4$$: Same as earlier. Note that there are 8 elements of order 3. If we consider all the 8 subgroups generated by them, we see that we get only four distinct ones, listed above.

    ---

7. Exhibit all Sylow 2-subgroups of $$S_4$$ and find elements of $$S_4$$ which conjugate one of these into each of the others.

    __Solution:__ A little bit of experimenting with elements of order 2 and 4 gives the following subgroups:

    $$\langle (1234), (13)\rangle, \ \langle (1243), (14)\rangle, \ \langle (1324), (12)\rangle.$$

    It can be verified that these are distinct. (For example, the 2 cycles listed in the generators don't appear in any of the other subgroups.) It can also be verified that all of these have order 8. Moreover, there can't be any more as $$n_2 \mid 3$$.  
    
    As for the conjugation question, $$(34)$$ conjugates the first to the second and $$(24)$$ the second to the third.

    ---

8. Exhibit two distinct Sylow 2-subgroups of $$S_5$$ and an element of $$S_5$$ that conjugates one into the other.

    __Solution:__ Note that $${\vert}S_5{\vert} = 2^3 \cdot 15$$ and thus, any two of the Sylow 3-subgroups listed earlier will work again. (With the understanding that the elements are now elements of $$S_5$$.)

    ---

9. Exhibit all Sylow 3-subgroups of $$SL_2(\mathbb{F}_3).$$

    __Solution:__ Note that the order of $$GL_2(\mathbb{F}_3)$$ is $$(3^2 - 1)(3^2 - 3) = 48$$. It can be easily shown that the order of $$SL_2$$ is half of that.  
    Thus, $$n_3 = 1$$ or $$4$$. Also, note that any Sylow 3-subgroup will have order 3 and hence, is isomorphic to $$\mathbb{Z}_3$$.  
    It is easy to find two distinct subgroups of order 3 by observing the following matrices to have order 3:

    $$\begin{pmatrix}
        1 & 1\\
        0 & 1
    \end{pmatrix},\ 
    \begin{pmatrix}
        1 & 0\\
        1 & 1
    \end{pmatrix}$$

    Also, these matrices generate distinct subgroups. Thus, $$n_3 > 1$$ which forces $$n_3 = 4$$.  
    We may now conjugate the above matrices to get the other two. In any case, we are left with the following:

    $$\left\langle \begin{pmatrix}
        1 & 1\\
        0 & 1\\
    \end{pmatrix} \right\rangle, \ 
    \left\langle \begin{pmatrix}
        0 & 1\\
        1 & 1\\
    \end{pmatrix} \right\rangle, \ 
    \left\langle \begin{pmatrix}
        0 & 1\\
        2 & 2\\
    \end{pmatrix} \right\rangle, \ 
    \left\langle \begin{pmatrix}
        2 & 1\\
        2 & 0\\
    \end{pmatrix} \right\rangle.$$

    ---

10. Prove that the subgroup of $$SL_2(\mathbb{F}_3)$$ generated by $$\begin{pmatrix}
    0 & -1\\
    1 & 0\\
\end{pmatrix}$$ and $$\begin{pmatrix}
    1 & 1\\
    1 & -1\\
\end{pmatrix}$$ is the unique Sylow 2-subgroup of $$SL_2(\mathbb{F}_3)$$.  
  
    __Solution:__ Hmm.

    ---

11. Show that the center of $$SL_2(\mathbb{F}_3)$$ is the group of order 2 consisting of $$\pm I$$, where $$I$$ is the identity matrix. Prove that $$SL_2(\mathbb{F}_3)/Z(SL_2(\mathbb{F}_3)) \cong A_4$$. 

    __Solution:__ Let $$M \in Z(SL_2(\mathbb{F}_3))$$. Then, $$AM = MA$$ and $$BM = MB$$ where

    $$A = \begin{pmatrix}
        1 & 1\\
        0 & 1\\
    \end{pmatrix} \text{ and } B = \begin{pmatrix}
        1 & 0\\
        1 & 1\\
    \end{pmatrix}.$$

    A straightforward calculation shows that this forces $$M = cI$$ for some $$c \in \mathbb{F}_3$$. As $$M \in SL_2(\mathbb{F}_3)$$, $$c \neq 0$$.  
    This just leaves $$c = -1, 1$$. It can be verified that $$\pm I$$ do indeed commute with every other element of $$SL_2(\mathbb{F}_3)$$. (And that they do belong to this group.)

    ---

12. Let $$2n = 2^ak$$ where $$k$$ is odd. Prove that the number of Sylow 2-subgroups of $$D_{2n}$$ is $$k$$.  
  
    __Solution:__ Hmm.

    ---

13. Prove that a group of order 56 has a normal Sylow $$p$$-subgroup for some prime $$p$$ dividing its order.

    __Solution:__ The proof [here](/alg/groups/simple/56) works.

    ---

14. Prove that a group of order 312 has a normal Sylow $$p$$-subgroup for some prime $$p$$ dividing its order.

    __Solution:__ Note that $$312 = 13\cdot 24$$. By the Sylow theorems, $$n_{13} \mid 24$$ and $$n_{13} \equiv 1$$ mod 13. This forces $$n_{13} = 1$$ and we are done.

    ---

15. Prove that a group $$G$$ of order 351 has a normal Sylow $$p$$-subgroup for some prime $$p$$ dividing its order.

    __Solution:__ Note that $$312 = 3^3\cdot13$$. By the Sylow theorems, $$n_{13} \mid 27$$ and $$n_{13} \equiv 1$$ mod 13. This forces $$n_{13} = 1, 27$$. If $$n_{13} = 1$$, then we are done. Let us assume that $$n_{13}\neq 1$$. Thus, $$n_{13} = 27$$.  
      
    Thus, there are 27 Sylow 13-subgroups of $$G$$. As 13 is a prime, this forces the intersection of two distinct Sylow 13-subgroups to be trivial. Thus, the number of elements having order 13 equals $$27(13-1) = 3^3(12).$$  
    This leaves us with $$3^3$$ remaining elements which are not part of any Sylow 13-subgroup.  
    Now, by Sylow Theorems, we know that $$n_3 \ge 1$$. However, no non-identity element can be part of a Sylow 3 as well as a Sylow 13-subgroup. Thus, the remaining $$3^3$$ elements form the unique Sylow 3-subgroup which gives us that $$n_3 = 1$$ and thus, we are done.

    ---

16. Let $${\vert}G{\vert} = pqr$$, where $$p$$, $$q$$, and $$r$$ are primes with $$p < q < r$$. Prove that G has a normal Sylow subgroup for either p, q or r.

    __Solution:__ See [this](/alg/groups/simple/pqr).

    ---

17. Prove that if $${\vert}G{\vert} = 105$$, then $$G$$ has a normal Sylow 5-subgroup and a normal Sylow 7-subgroup.

    __Solution:__ Assume not. Then, $$n_5 > 1$$ and $$n_7 > 1$$.  
    Note that $$105 = 3 \cdot 5 \cdot 7$$. The Sylow theorems force $$n_5 = 21$$ and $$n_7 = 15$$.  
    Note that the intersection of any two of these $$21 + 15$$ Sylow subgroups must be trivial (by Lagrange's Theorem). Thus, their union contains exactly 

    $$21(5 - 1) + 15(7 - 1) + 1 = 175 \text{ elements.}$$

    This is clearly a contradiction. (As 175 > 105.)

    ---

18. Prove that a group of order 200 has a normal Sylow 5-subgroup.

    __Solution:__ $$n_5 \mid 8$$ and $$n_5 \equiv 1 \mod 5$$ forces $$n_5 = 1$$.

    ---

19. Prove that if $${\vert}G{\vert} = 6545$$ then $$G$$ is not simple.
    
    __Solution:__ Note that $$6545 = 5 \cdot 7 \cdot 11 \cdot 17$$. For the sake of contradiction, let us assume that $$G$$ is not simple. Thus, $$n_5$$, $$n_7$$, $$n_{11}$$, and $$n_{17}$$ are all strictly greater than 1.  
    Now, looking at the possibilities for each by considering the factors of the "complimentary part", we get that

    $$n_5= 11, n_7 = 85, n_{11} = 594, n_{17} = 35.$$

    Note that the intersection of any two of these Sylow subgroups must be trivial (by Lagrange's Theorem). Thus, their union contains exactly 

    $$11(5 - 1) + 85(7 - 1) + 594(11 - 1) + 35(17 - 1) + 1 = 7055 \text{ elements.}$$

    This is clearly a contradiction. (As 7055 > 6545.)

    ---

20. Prove that if $${\vert}G{\vert} = 1365$$ then $$G$$ is not simple.
    
    __Solution:__ Note that $$1365 = 3 \cdot 5 \cdot 7 \cdot 13$$. For the sake of contradiction, let us assume that $$G$$ is not simple. Thus, $$n_3$$, $$n_{7}$$, and $$n_{13}$$ are all strictly greater than 1.  
    Now, looking at the possibilities for each by considering the factors of the "complimentary part", we get that

    $$n_3 \ge 7, n_7 \ge 15, n_{13} = 105.$$

    Note that the intersection of any two of these Sylow subgroups must be trivial (by Lagrange's Theorem). Thus, their union contains at least 

    $$7(3 - 1) + 15(7 - 1) + 105(13 - 1) > 1365 \text{ elements.}$$

    This is clearly a contradiction.

    ---

21. Prove that if $${\vert}G{\vert} = 2907$$ then $$G$$ is not simple.

    __Solution:__ Same idea as earlier. We get that $$n_{17} = 171$$ and $$n_{19} = 153$$ in this case. (If we assume that neither is 1.)

    ---

22. Prove that if $${\vert}G{\vert} = 132$$ then $$G$$ is not simple.

    __Solution:__ See [here](/alg/groups/simple/132/).

    ---

23. Prove that if $${\vert}G{\vert} = 462$$ then $$G$$ is not simple.

    __Solution:__ Note that $$462 = 11 \cdot 42$$. Considering the factors of 42, we see that $$n_{11}$$ is forced to be 1.

    ---

24. Prove that if $$G$$ is a group of order 231 then $$Z(G)$$ contains a Sylow 11-subgroup of $$G$$ and a Sylow 7-subgroup is normal in $$G$$.

    __Solution:__ Note that $$231 = 3\cdot 7\cdot 11$$. The restrictions from Sylow Theorems force that $$n_7 = n_{11} = 1$$. In particular, this shows that $$G$$ has a (unique) Sylow 7-subgroup which is normal in it.  
    Now, we show that the Sylow 11-subgroup is contained in $$Z(G)$$. Let us denote this subgroup by $$P$$. Note that $$P$$ is normal. Consider the action of $$G$$ on $$P$$ given by conjugation, that is, $$(g, p) \mapsto gpg^{-1}$$.  
      
    This induces a homomorphism $$\Phi : G \to \operatorname{Aut}(P)$$. Note that $$P = (\mathbb{Z}/11\mathbb{Z})$$ is cyclic and thus, $$\operatorname{Aut}(P) = (\mathbb{Z}/11\mathbb{Z})^\times = (\mathbb{Z}/10\mathbb{Z})$$.  
    (The last equality may be manually verified by noting that $$\bar{2}$$ is a generator for $$(\mathbb{Z}/11\mathbb{Z})^\times$$ which has 10 elements.)  
      
    Thus, $$G/\ker\Phi$$ is isomorphic to a subgroup of $$\mathbb{Z}_{10}$$ (First Isomorphism Theorem). In particular, $${\vert}G/\ker\Phi{\vert} \mid 10$$. Looking at the divisors of $${\vert}G{\vert}$$, we see that this forces $${\vert}G/\ker\Phi{\vert} = 1$$ or $$G = \ker\Phi$$.

    This means that given any $$g \in G$$, the map $$\Phi(g)$$ is the identity map. In other words, $$\Phi(g)(p) = p$$ for all $$g \in G$$ and $$p \in P$$. The above is equivalent to $$gpg^{-1} = p$$ or $$gp = pg$$ for all $$g \in G$$ and $$p \in P$$. Thus, $$P \le Z(G)$$, by the definition of the center.

    _Remark._ We didn't really require the fact that $$\mathbb{Z}_{11}^\times \cong \mathbb{Z}_{10}$$. Only $${\vert}\mathbb{Z}_{11}^\times{\vert} = 10$$ would've been sufficient (which is more straightforward as well).

    ---

25. Prove that if $$G$$ is a group of order 385 then $$Z(G)$$ contains a Sylow 7-subgroup of $$G$$ and a Sylow 11-subgroup is normal in $$G$$.

    __Solution:__ Same as before. We once again get that $$n_7 = n_{11} = 1$$ is forced by the Sylow Theorems directly.  
    As before, we get a map $$\Phi:G \to \operatorname{Aut}(P)$$ where $$P$$ is the unique Sylow 7-subgroup. As $${\vert}\operatorname{Aut}(P){\vert} = 6$$, it is again forced that the above map is trivial.

    ---

26. Let $$G$$ be a group of order 105. Prove that if a Sylow 3-subgroup of $$G$$ is normal then $$G$$ is abelian.

    __Solution:__ Let $$N$$ be the Sylow 3-subgroup.  
    __Claim 1:__ $$N \le Z(G)$$.  
    Note that $${\vert}G/C_G(N){\vert}$$ must divide both $${\vert}\operatorname{Aut}(N){\vert} = 2$$ and $${\vert}G{\vert} = 105$$. This forces $$G = C_G(N)$$ or $$N \le Z(G).$$  
    (We have used the fact that $$N$$ is normal in the above by considering the $$\Phi$$ defined similarly in the previous exercise.)

    __Claim 2:__ $$G/N$$ is cyclic.  
    Note that $$G/N$$ has order $$35 = 5 \cdot 7$$. Noting that $$5 \nmid 6$$ proves the claim. (See [this](/alg/groups/pq-cyclic-group).)  
      
    __Claim 3:__ $$G/Z(G)$$ is cyclic.  
    By the third isomorphism theorem, we have that

    $$G/Z(G) \cong (G/N)/(Z(G)/N).$$

    (Note that Claim 1 (and the fact that $$N \lhd G$$) tells us that $$Z(G)/N$$ makes sense.)  
    By the previous claim, $$G/N$$ is cyclic. The claim follows as quotients of a cyclic group are cyclic.

    __Claim 4:__ $$G$$ is abelian.  
    This is a consequence of the above claim. (See [this](/alg/groups/GZ-cyclic-abelian).)

    ---

27. Let $$G$$ be a group of order 315 which has a normal Sylow 3-subgroup. Prove that $$Z(G)$$ contains a Sylow 3-subgroup of $$G$$ and deduce that $$G$$ is abelian.
    
    __Solution:__ Let $$N$$ be the normal Sylow 3-subgroup. (It must necessarily be unique.)  
    Consider the action of $$G$$ on $$N$$ given by conjugation. (This is an action as $$N$$ is normal.)  
    Consider the induced homomorphism $$\Phi:G \to \operatorname{Aut}(N)$$.  
      
    Now, note that $$N$$ is a group of order 9. Thus, it is isomorphic to either $$\mathbb{Z}_9$$ or $$\mathbb{Z}_3 \times \mathbb{Z}_3$$. Accordingly, $\operatorname{Aut}$ has order either 6 or 48.  
      
    As $$G/\ker\Phi \cong \Phi(G)$$ by the first isomorphism theorem, we get that $${\vert}G/\ker\Phi{\vert}$$ divides 48. (6 divides 48 anyway.)  
    Also, $${\vert}G/\ker\Phi{\vert} \mid {\vert}G{\vert}$$. Thus, $${\vert}G/\ker\Phi{\vert}$$ is either 1 or 3.  
    
    If $${\vert}G/\ker\Phi{\vert} = 3$$, then $${\vert}\ker\Phi{\vert} = 315/3 = 105$$. However, note that $$P \le \ker\Phi = C_G(P)$$ and hence $${\vert}P{\vert} \mid {\vert}C_G(P){\vert}$$ which is a contradiction as $$9 \nmid 105$$. Hence, we get that $$G/\ker\Phi = (1)$$ or $$G = \ker\Phi$$.  
      
    The above shows that the image of $$\Phi$$ is just the identity map. In other words, $$gpg^{-1} = p$$ for all $$p \in P$$ and $$g \in G$$. This is precisely what it means for $$P \le Z(G)$$.  
      
    The rest of the solution is now the same as the earlier one. We note that $$G/P$$ has order 35 and hence, is cyclic. (See [this](/alg/groups/pq-cyclic-group).)  
    We also have

    $$G/Z(G) \cong (G/P)/(Z(G)/P)$$

    and thus, $$G/Z(G)$$ is cyclic. This proves that $$G$$ is abelian. (See [this](/alg/groups/GZ-cyclic-abelian).)

    ---

28. Let $$G$$ be a group of order 1575. Prove that if a Sylow 3-subgroup of $$G$$ is normal then a Sylow 5-subgroup and a Sylow 7-subgroup are normal. In this situation prove that $$G$$ is abelian.
    
    __Solution:__ By the same arguments as earlier, we get that $$G$$ is abelian. Now, by the Sylow Theorems, there do exist Sylow 5 and 7-subgroups. As $$G$$ is abelian, they must be normal.

    _Remark:_ Admittedly, I have not followed the path that the authors wanted us to.

    ---

29. If $$G$$ is a non-abelian simple group of order $$< 100$$, prove that $$G \cong A_5$$. 

    __Solution:__ Let $${\vert}G{\vert} = n$$.   
    [This](/alg/groups/simple) shows that if $$n \neq 60$$ and if $$n$$ is not a prime, then $$G$$ is abelian. Now, if $$n$$ is a prime, then $$G$$ must be abelian. Thus, the only possibility left is that $$n = 60$$.  
    Now, the only simple group of order 60 (up to isomorphism) is $$A_5$$ and hence, we are done.

    ---

30. How many elements of order 7 must there be in a simple group of order 168?

    __Solution:__ Note that $$168 = 7\cdot 24$$. The Sylow Theorems force $$n_7$$ to be either 1 or 8.  
    If $$n_7 = 1$$, then there is a unique Sylow 7-subgroup which must be normal. This contradicts the assumption that the group is simple.  
    Thus, $$n_7 = 8$$. This means that every Sylow 7-subgroup is isomorphic to $$\mathbb{Z}_7$$. In particular, every non-identity has order 7.  
    Moreover, two distinct Sylow 7-subgroups can only intersect trivially, by Lagrange's theorem. Thus, the total number of order 7 elements contained in these Sylow subgroups is

    $$8(7 - 1) = 48.$$

    Now, we show that there are no more. That is, any order 7 element is contained in some Sylow 7-subgroup.  
    Let $$x$$ be any order 7 element. Then, $$\langle x\rangle$$ is a 7-group and thus, must be contained in some Sylow 7-subgroup, as desired. (In fact, $$\langle x\rangle$$ is itself a Sylow 7-subgroup.)

    ---

31. For $$p = 2$$, $$3$$, and $$5$$, find $$n_p(A_5)$$ and $$n_p(S_5)$$.

    __Solution:__  
    $$A_5$$:  
    Note that Sylow Theorems force $$n_3 \in \{1, 10\}$$ and $$n_5 \in \{1, 6\}$$.  
    As $$A_5$$ is simple, $$n_p$$ cannot be 1 for any $$p$$ and hence, $$n_3 = 10$$ and $$n_5 = 6$$.  

    Now, we show that $$n_2 = 5$$. Note that $$\langle (12)(34), (13)(24) \rangle$$ is a Sylow 2-subgroup. (The way I found this was by taking a Sylow 2-subgroup from Q8. and intersecting it with $$A_5$$.)  
    Note that its elements are

    $$\{1, (12)(34), (13)(24), (14)(23)\}.$$

    That is, identity along with all possible elements of the cycle type 1-2-2 formed using the numbers 1, 2, 3, 4.  
    Recalling that all Sylow 2-subgroups are conjugates and also recalling how conjugates in $$S_n$$ look, we see that any Sylow 2-subgroup is of this form:

    $$\{1, (ab)(cd), (ac)(bd), (ad)(bc)\}.$$

    (Where $$a, b, c, d$$ are distinct elements of $$\{1, 2, 3, 4, 5\}$$.)  
    This shows us that picking any four numbers from $$\{1,\ldots, 5\}$$ uniquely defines Sylow 2-subgroup. (In the sense, that there's no over-counting or under-counting.)
    Thus, the number of such subgroups is $$\dbinom{5}{4} = 5$$.  
    To conclude, we have, for $$A_5$$:

    $$n_2 = 5,\ n_3 = 10,\ n_5 = 6.$$

    $$S_5$$:  
    $${\vert}S_5{\vert} = 120 = 2^3\cdot3\cdot5$$.  
    For $$n_3$$, we have the possibilities 1, 10, and 40. Note that it can't be 1 as any Sylow 3-subgroup of $$A_5$$ is again a Sylow 3-subgroup of $$S_5$$ and we already had 10 there.  
    Now, if $$n_3$$ were 40, then there would be a total of 80 elements of order 3. However, it can be verified that only elements of the cycle type $$(abc)$$ have order 3 and there are only 20 of those. Thus, $$n_3 = 10$$.  
    For $$n_5$$, the discussion is even simpler as there are no new possibilities and we have $$n_5 = 6$$ as before.  
      
    As before, we have $$n_2 \le 15$$. We show that $$n_2 = 15$$ by demonstrating fifteen such subgroups. Let $$a, b, c, d \in \{1, 2, 3, 4, 5\}$$ be distinct. Assume that $$a$$ is the smallest amongst the four.  
    Consider the subgroup:

    $$\langle (abcd), (ac)\rangle.$$

    It can be verified that the above does have 8 elements. Moreover, to determine such a subgroup, we first need to pick 4 elements from $$\{1, \ldots, 5\}$$ and then from those 4, pick an element to be paired with the smallest.  
    It can be verified that different such pickings will give different subgroups. (Simply by writing explicitly the elements of the above subgroup.)  
    This gives us $$5 \times 3 = 15$$ different subgroups and hence, we are done.  
    To conclude, we have, for $$S_5$$:

    $$n_2 = 15,\ n_3 = 10,\ n_5 = 6.$$

    ---

32. Let $$P$$ be a Sylow $$p$$-subgroup of $$H$$ and let $$H$$ be a subgroup of $$K$$. If $$P \lhd H$$ and $$H \lhd K$$, prove that $$P$$ is normal in $$K$$. Deduce that if $$P \in Syl_p(G)$$ and $$H = N_G(P)$$, then $$N_G(H) = H$$.

    __Solution:__ We first show that $$P \lhd K$$. To see this, let $$k \in K$$ be arbitrary. Now, note that

    $$kPk^{-1} \le kHk^{-1} = H,$$

    where the last equality follows from that fact that $$H \lhd K$$. Now, note that $$kPk^{-1}$$ has the same order as $$P$$ and thus, it also a Sylow p-subgroup of $$H$$. However, since $$P$$ was normal, it must be the unique Sylow p-subgroup of $$H$$. Thus, $$kPk^{-1} = P$$ and thus, $$P \lhd K$$.  
      
    Second part: Let $$K = N_G(H)$$. Then, we have $$P \lhd H$$ and $$H \lhd K$$. (Note that a subgroup is always normal in its normaliser.)  
    By Q1., we know that $$P \in Syl_p(H)$$ and hence, by the previous part, we see that $$P \lhd K$$. However, note that $$N_G(P)$$ is the largest subgroup of $$G$$ in which $$P$$ is normal and hence, $$K \le H$$. As we already had $$H \le K$$, we get that $$H = K = N_G(H)$$, as desired.

    ---

33. Let $$P$$ be a normal Sylow $$p$$-subgroup of $$G$$ and let $$H$$ be any subgroup of $$G$$. Prove that $$P \cap H$$ is the unique Sylow $$p$$-subgroup of $$H$$.

    __Solution:__ Note that $$P \cap H$$ is normal in $$H$$. (Since $$P \lhd H$$.)  
    Thus, if $$P \cap H$$ is a Sylow $$p$$-subgroup of $$H$$, then it is indeed the unique one. The main task is to show that $$P\cap H \in Syl_p(H)$$.  
      
    Suppose not. Note that $$P \cap H$$ is a $$p$$-group and thus, there exists $$Q \in Syl_p(H)$$ such that $$P \cap H \lneq Q \le H$$.  
    In turn, note that $$Q$$ is a $$p$$-group as well and hence, is contained in some Sylow p-subgroup of $$G$$. As $$P \lhd G$$, it is forced that $$Q \le P$$. (Since $$P$$ is the unique Sylow p-subgroup of $$G$$.)  
    Thus, we have that $$Q \le H$$ and $$Q \le P$$. This implies that $$Q \le P \cap H$$, a contradiction.

    ---

34. Let $$P \in Syl_p(G)$$ and assume $$N \lhd G$$. Use the conjugacy part of Sylow's Theorem to prove that $$P \cap N$$ is a Sylow $$p$$-subgroup of N. Deduce that $$PN/N$$ is a Sylow $$p$$-subgroup of $$G/N$$.

    __Solution.__ We first note the following lemma:  
    _Lemma._ For any $$g \in G$$, we have $$g(P\cap N)g^{-1} = (gPg^{-1})\cap(gNg^{-1})$$.  
    This is a straightforward check.  
    
    We now prove that $$P\cap N \in Syl_p(N)$$. Note that $$P\cap N$$ is a $$p$$-group and thus, is contained in some $$Q \in Syl_p(N)$$, by the second Sylow Theorem. We now show that $$P \cap N = Q$$.  
    Since $$Q$$ is again a $$p$$-group, it is contained in $$gPg^{-1}$$ for some $$g \in G$$. (Conjugacy part of the Sylow theorem.)  
    
    Thus, we have $$Q \le gPg^{-1}$$ and $$Q \le N$$. This, in turn gives us that

    $$Q \le gPg^{-1} \cap N = (gPg^{-1}) \cap (gNg^{-1}).$$

    The last equality follows from the fact that $$N \lhd G$$. By the lemma, we see that $$Q \le g(P \cap N)g^{-1}$$. Thus, we get

    $$ P \cap N \le Q \le g(P \cap N)g^{-1}.$$

    Now, note that all the groups above are finite and $${\vert}P \cap N {\vert} = {\vert}g(P \cap N)g^{-1}{\vert}$$. Thus, we must have equality throughout, as desired.

    For the last deduction, we first note that $$PN/N$$ is indeed a subgroup of $$G/N$$. (Since $$N \lhd G$$, $$N \lhd PN \le G$$.)  
    Now, if $${\vert}G{\vert} = p^am$$ and $${\vert}N{\vert} = p^bm'$$, then the above shows that $$P\cap N = p^b$$. The result then follows from noting that $${\vert}G/N{\vert} = p^{a-b}(m/m')$$ and $${\vert}PN/N{\vert} = {\vert}P{\vert}/{\vert}P\cap N{\vert} = p^{a-b}$$.  
    (As usual, $$(m, p) = (m', p) = 1$$.)
    
    ---

35. Let $$P \in Syl_p(G)$$ and let $$H \le G$$. Prove that $$gPg^{-1} \cap H$$ is a Sylow $$p$$-subgroup of $$H$$ for some $$g \in G.$$ Give an explicit example showing that $$hPh^{-1} \cap H$$ is not necessarily a Sylow $$p$$-subgroup of $$H$$ for any $$h \in H$$.
    
    __Solution:__ Let $$Q$$ be a Sylow $$p$$-subgroup of $$H$$. (Which exists, by the first Sylow Theorem).  
    By the conjugacy part, we know that $$Q \le gPg^{-1}$$ for some $$g \in G$$.  
    As $$Q \le H$$, we have that $$Q \le gPg^{-1} \cap H$$.  
      
    Now, note that the order of the RHS is at most the GCD of that of $$gPg^{-1}$$ and $$H$$, which would precisely be the order of $$Q$$. Thus, equality follows, as desired.  
      
    Explicit example: Let $$G = S_3$$, $$p = 2$$, $$P = \langle (13)\rangle$$, and $$H = \langle (12)\rangle$$.

    ---

36. Prove that if $$N$$ is a normal subgroup of $$G$$ then $$n_p(G/N) \le n_p(G)$$.

    __Solution:__ Hmm.

    ---

37. Let $$R$$ be a normal $$p$$-subgroup of $$G$$ (not necessarily a Sylow subgroup).  

    (a) Prove that $$R$$ is contained in every Sylow $$p$$-subgroup of $$G$$.  
    
    __Solution:__ Let $$P \in Syl_p(G)$$. We show that $$R \le P$$.  
    As $$Q$$ is a $$p$$-subgroup, there exists $$g \in G$$ such that $$R \le gPg^{-1}$$.  
    This implies that $$g^{-1}Rg \le P$$. As $$R \lhd G$$, $$g^{-1}Rg = R$$ and thus, $$R \le P$$, as desired.

    (b) If $$S$$ is another normal $$p$$-subgroup of $$G$$, prove that $$RS$$ is also a normal $$p$$-subgroup of $$G$$.

    __Solution:__ First we show that $$RS$$ is normal. (That it is a subgroup follows from the fact that $$R$$ is normal.)  
    For any $$g \in G$$, note that

    $$gRSg^{-1} = (gRg^{-1})(gSg^{-1}) = RS.$$

    (The first equality follows from the fact that $$R, S \lhd G$$.)  
    Now, note that

    $${\vert}RS{\vert} = \dfrac{|R{\vert}{\vert}S|}{|R\cap S|}.$$

    Clearly, $$p$$ is the only prime divisor of the RHS and hence, $$RS$$ is a $$p$$-subgroup.

    (c) The subgroup $$O_p(G)$$ is defined to be the group generated by all normal $$p$$-subgroups of $$G$$. Prove that $$O_p(G)$$ is the unique largest normal $$p$$-subgroup of $$G$$ and $$O_p(G)$$ equals the intersection of all Sylow $$p$$-subgroups of $$G$$.

    __Solution:__ As $$G$$ is finite, the set of all normal $$p$$-subgroups is finite. Let this be set $$\{R_1, \ldots, R_n\}$$.  
    
    Define $$R := R_1R_2\cdots R_n$$. By the previous part, we see that $$R$$ is normal $$p$$-subgroup 

    __Claim 1.__ $$O_p(G) \subset R$$.  
    _Proof._ Note that $$R_i \le R$$ for all $$i \in \{1, \ldots, n\}$$. Thus, the claim follows by the definition of $$O_p(G)$$.  
      
    __Claim 2.__ $$R \subset O_p(G)$$.  
    _Proof._ Since $$R$$ is a normal $$p$$-subgroup, we see that $$R = R_i$$ for some $$i \in \{1, \ldots, n\}$$. Thus, the claim follows by the definition of $$O_p(G)$$.  

    __Claim 3.__ $$R = O_p(G)$$.  
    _Proof._ Follows from the earlier claims.  
      
    From this, it follows that $$O_p(G)$$ is the unique largest normal $$p$$-subgroup.  
      
    __Claim 4.__ $$R \subset \displaystyle\bigcap_{P \in Syl_p(G)}P$$.  
    _Proof._ Follows from part (a).

    __Claim 5.__ $$\displaystyle\bigcap_{P \in Syl_p(G)}P \subset R$$.  
    _Proof._ Let $$I = \displaystyle\bigcap_{P \in Syl_p(G)}P$$. It clear that $$I$$ is a $$p$$-subgroup. We show that $$I$$ is normal.  
    Let $$g \in G.$$ Observe that

    $$gIg^{-1} = g\left(\bigcap_{P \in Syl_p(G)}P\right)g^{-1} = \bigcap_{P \in Syl_p(G)}(gPg^{-1}) \subset \bigcap_{P \in Syl_p(G)}P = I.$$
    
    Where the last containment follows from the fact that the conjugate of a Sylow $$p$$-subgroup is once again a Sylow $$p$$-subgroup. Thus, $$I$$ is normal.  
      
    By the definition of $$R$$, we have $$I \le R$$, as desired.

    __Claim 6.__ $$R = \displaystyle\bigcap_{P \in Syl_p(G)}P$$.  
    _Proof._ Follows from the previous two claims.

    (d) Let $$G = G/O_p(G)$$. Prove that $$O_p(\bar{G}) = \bar{1}$$.

    __Solution:__ The above is equivalent to showing that $$\bar{G}$$ has no nontrivial $$p$$-subgroup.  
    Let $$\bar{R}$$ be a normal $$p$$-subgroup of $$\bar{G}$$. By the correspondence theorem, $$\bar{R} = R/N$$ for some $$O_p(G) \le R \lhd G$$. (This $$R$$ is not the same as part (c).)  
    
    Note that $$R$$ is again a normal $$p$$-subgroup and hence, $$R \le O_p(G)$$. Therefore, $$R = O_p(G)$$ and thus, $$\bar{R} = \bar{1}$$, as desired.

    ---

38. Use the method of proof in Sylow's Theorem to show that if $$n_p$$ is not congruent to l (mod $$p^2$$) then there are distinct Sylow $$p$$-subgroups $$P$$ and $$Q$$ of $$G$$ such that $${\vert}P : P \cap Q{\vert} = {\vert}Q : P \cap Q{\vert} = p$$.

    __Solution:__ We shall be using the following lemma from the book:  
    __Lemma.__ Let $$P \in Syl_p(G)$$. If $$Q$$ is any $$p$$-subgroup of $$G$$, then $$Q \cap N_G(P) = Q \cap P$$.  
    The $$\supset$$ containment is clear. The idea for the reverse is to show that $$P(Q \cap N_G(P))$$ is a $$p$$-subgroup containing $$P$$ and hence, must equal $$P$$ which gives $$Q \cap N_G(P) \subset P$$.  
      
    Now, consider the set $$\mathcal{S} = Syl_p(G) = \{P_1, \ldots, P_{n_p}\}$$. $$G$$ acts on $$\mathcal{S}$$ by conjugation and thus, so does $$P = P_1 \le G$$.  
    Under this action of $$P$$, $$\mathcal{S}$$ decomposes as

    $$\mathcal{S} = \mathcal{O}_1 \cup \cdots \cup \mathcal{O}_s.$$  
      
    We have that

    $$n_p = {\vert}\mathcal{O}_1{\vert} + \cdots + {\vert}\mathcal{O}_s{\vert}.$$

    Now, we note that $${\vert}\mathcal{O}_i{\vert} = P : N_{P}(P_i){\vert}$$. By definition, we have $$N_P(P_i) = P \cap N_G(P_i) = P \cap P_i$$, where the last equality to due to the above lemma.  
    Thus, $${\vert}\mathcal{O}_i{\vert} = {\vert}P : P \cap P_i$$.
      
    Now, note that $${\vert}\mathcal{O}_1{\vert} = 1$$ and $${\vert}\mathcal{O}_i > 1$$ for all $$2 \le i \le s$$.  
      
    However, notice that all $$P_i$$s are $$p$$-groups (and hence, so are their intersections, by Lagrange) and thus, $${\vert}\mathcal{O}_i{\vert} = p^{a_i}$$ for all $$2 \le i \le s$$ such that $$a_i \ge 1$$ for all such $$i$$.  
      
    Now, let us assume that $$a_i \neq 1$$ for all $$i \in \{2, \ldots, n\}$$. This means that $$a_i \ge 2$$ for all such $$i$$ or that $$p^2 \mid {\vert}\mathcal{O}_i$$ for all such $$i$$. Thus, we get

    $$n_p = {\vert}\mathcal{O}_1{\vert} + ({\vert}\mathcal{O}_2{\vert} + \cdots + {\vert}\mathcal{O}_{n_p}{\vert}) \equiv 1 \mod p^2,$$

    a contradiction. Thus, $$a_i = 1$$ for some $$i \in \{2, \ldots, n\}$$. Let $$Q = P_i$$.  
    Thus, we have

    $${\vert}P : P \cap Q = p.$$

    As $${\vert}P{\vert} = {\vert}Q{\vert}$$, we have that $${\vert}Q:P\cap Q{\vert} = p$$ as well.

    ---

39. Show that the subgroup of strictly upper triangular matrices in $$G = GL_n(\mathbb{F}_p)$$ is a Sylow $$p$$-subgroup of this finite group.

    __Solution:__ Note that

    $${\vert}G{\vert} = (p^n - 1)(p^n - p)\cdots(p^n - p^{n-1}) = p^{1 + \cdots + n-1}(p^n - 1)(p^{n-1} - 1)\cdots(p - 1).$$

    Let $$m = (p^n - 1)(p^{n-1} - 1)\cdots(p - 1)$$. Then, $${\vert}G{\vert} = p^{n(n-1)/2}m$$ with $$p \nmid m$$.  
    Now, for $$P$$ to be a Sylow $$p$$-subgroup, it must have order $$p^{n(n-1)/2}$$, by definition. One may check that the subgroup of strictly upper triangular matrices (that is, upper triangular matrices with $$1$$s along the diagonal) does have this order. (And that it is indeed a subgroup.)

    ---

40. Prove that the number of Sylow $$p$$-subgroups of $$GL_2(\mathbb{F}_p)$$ is $$p+1$$.

    __Solution:__ Note that $$n_p = {\vert}G:N_G(P){\vert}$$ for any $$P \in Syl_p(G)$$.  
    As noted in the previous question, the subgroup of upper triangular matrices is a Sylow $$p$$-subgroup. In this case, it has an easy representation. Namely, it is

    $$\left\langle \begin{pmatrix}
        1 & 1\\
        1 & 0
    \end{pmatrix}\right\rangle.$$

    Let $$X$$ denote the matrix above. Note that for $$M \in G$$ to belong to $$N_G(P)$$, we must have $$MXM^{-1} = X^n$$ for some $$n \in \{0, \ldots, p - 1\}$$. That is,

    $$MXM^{-1} = \begin{pmatrix}
        1 & n\\
        1 & 0
    \end{pmatrix}.$$

    Assume $$M = \begin{pmatrix}
        a & b\\
        c & d   
    \end{pmatrix}$$. Then, we have $$M^{-1} = \dfrac{1}{ad - bc}\begin{pmatrix}
        d & -b\\
        -c & a
    \end{pmatrix}$$.

    Thus, the product $$MXM^{-1}$$ is:  
      
    $$\dfrac{1}{ad - bc}\begin{pmatrix}
        ad - ac - bc & a^2\\
        -c^2 & -bc + ac + ad
    \end{pmatrix}.$$

    Thus, it forced that $$c = 0$$. The product then becomes:  
      
    $$\dfrac{1}{ad}\begin{pmatrix}
        ad & a^2\\
        0 & ad
    \end{pmatrix} = \begin{pmatrix}
        1 & ad^{-1}\\
        0 & 1
    \end{pmatrix}.$$

    (Note that $$d$$ must necessarily be nonzero as $$M \in G$$.)  
    Thus, we see that $$c = 0$$ is both necessary and sufficient. This gives us that

    $$N_G(P) = \left\{\begin{pmatrix}
        a & b\\
        0 & d
    \end{pmatrix} \in GL_2(\mathbb{F}_n) : a, b, d \in \mathbb{F}_n\right\}.$$

    Note that $$\det M = ad$$ must be nonzero. Thus, we have precisely $$(p - 1)$$ choices for each $$a$$ and $$d$$. For $$b$$, we have exactly $$p$$ choices. Thus, $${\vert}N_G(P){\vert} = p(p - 1)^2$$. This finally gives us

    $$n_p = {\vert}G:N_G(P){\vert} = \dfrac{p(p - 1)^2(p + 1)}{p(p - 1)^2} = p + 1.$$

    ---


41. Hmm.
42. Hmm.
43. Hmm.
44. Let $$p$$ be the smallest prime dividing the order of the finite group $$G$$. If $$P \in Syl_p(G)$$ and $$P$$ is cyclic prove that $$N_G(P) = C_G(P)$$.

    __Solution:__ Note that we already have $$C_G(P) \le N_G(P)$$. We just need to show that $$N_G(P) \subset C_G(P)$$.  
    Let $${\vert}G{\vert} = p^am$$ with $$p \nmid m$$. Then, $${\vert}P{\vert} = p^a$$.  
    Note that $$P \le N_G(p)$$ and thus, $${\vert}N{\vert} = p^am'$$ for some $$m' \in \mathbb{N}$$ such that $$p \nmid m' \mid m$$. Also note that if $$m' \neq 1$$, then $$m'$$ has prime factors, all of which are strictly greater than $$p$$. (Since $$p$$ is the smallest prime dividing $${\vert}G{\vert}$$.)  

    Consider the action of $$N_G(P)$$ on $$P$$ given conjugation. This induces a homomorphism $$\Phi:N_G(P) \to \operatorname{Aut}(P)$$. By the first isomorphism theorem, $$N_G(P)/\ker\Phi$$ is isomorphic to a subgroup of $$\operatorname{Aut}(P)$$. In particular, $${\vert}N_G(P)/\ker\Phi{\vert}$$ divides $${\vert}\operatorname{Aut}(P){\vert}$$.  
    As $$P$$ is cyclic with order $$p^a$$, the order of $$\operatorname{Aut}(P)$$ is $$\varphi(p^a) = p^{a-1}(p - 1)$$.  
    Moreover, $$P$$ is abelian (since it's cyclic) and thus, $$P \le \ker\Phi$$. This gives us that $${\vert}\ker\Phi{\vert} = p^am''$$ for some $$p \nmid m'' \mid m'$$.  
    Thus, we have

    $${\vert}N_G(P)/\ker\Phi{\vert} \mid p^{a-1}(p - 1)$$

    $$\implies \dfrac{m'}{m''} \mid p^{a-1}(p - 1).$$

    Note that if $$m' \neq m''$$, then all the prime factors of $$m'/m''$$ would be $$>p$$ and thus, could not divide the RHS. Hence, we must have $$m' = m''$$ or $$\ker\Phi = N_G(P)$$. This means that $$npn^{-1} = p$$ for all $$n \in N_G(P)$$ and $$p \in P$$. This precisely means that $$N_G(P) \subset C_G(P)$$, as desired.

    ---

45. Find generators for a Sylow $$p$$-subgroup of $$S_{2p}$$, where $$p$$ is an odd prime. Show that this is an abelian group of order $$p^2$$.
    
    __Solution:__ The exponent of $$p$$ in $$p^2!$$ can easily be calculated to be 2. (We use the fact that $$p > 2$$ here.) Thus, a Sylow $$p$$-subgroup must necessarily have order $$p^2$$. Note that this already proves that the group is abelian as all groups of order $$p^2$$ are abelian. (See [this](/alg/groups/p2-groups-abelian).) However, we shall explicitly see the group anyway.

    Note that the cycles $$(1\ 2 \ \ldots\ p)$$ and $$(p+1 \ p+2 \ \ldots\ 2p)$$ are distinct elements of order $$p$$ that commute with each other. This gives us the following Sylow $$p$$-subgroup:

    $$\langle (1\ 2 \ \ldots\ p),  (p+1 \ p+2 \ \ldots\ 2p)\rangle.$$

    Clearly, this is abelian.

    ---

46. Find generators for a Sylow $$p$$-subgroup of $$S_{p^2}$$, where $$p$$ is a prime. Show that this is a non-abelian group of order $$p^{p+1}$$.

    __Solution:__ The exponent of $$p$$ in $$p^2!$$ can easily be calculated to be $$p+1$$. Thus, a Sylow $$p$$-subgroup must necessarily have order $$p^{p+1}$$.

    First, note the following $$p$$-cycles: $$(1\ 2\ \ldots\ p)$$, $$(p+1\ p+2\ \ldots\ 2p)$$, $$\ldots$$, $$((p-1)p+1\ \ldots\ p^2)$$. All of these are $$p$$ distinct elements of order $$p$$ that commute with each other. Let $$H$$ be the group generated by these elements. Clearly, $$H$$ has order $$p^p$$.

    Now, consider the subgroup $$P$$ generated by $$H$$ along with the cycle $$\sigma = (1\ 2\ \ldots\ p^2)$$. We now prove the following claims about $$P$$:

    __Claim 1.__ Every non-identity element of $$P$$ has order $$p$$ or $$p^2$$.  
    _Proof._ One may verify that every element of $$P$$ is either a $$p^2$$-cycle or a product of disjoint $$p$$-cycles.

    __Claim 2.__ $$P$$ is a $$p$$-group.  
    _Proof._ $$H\le P$$ and thus, $$p^p$$ divides the order of $$p$$. If there were some other prime that divided $${\vert}P{\vert}$$, then we would have an element of that prime order (Cauchy's Theorem) but that is not possible, due to Claim 1.

    __Claim 3.__ $${\vert}P{\vert} = p^{p+1}$$.  
    _Proof._ By the earlier claim, $${\vert}P{\vert} = p^n$$ for some $$n \in \mathbb{N}$$.  
    As $$H \lneq P$$, we have $$n > p$$. However, $$n \le p+1$$ as that's the largest power of $$p$$ in $${\vert}S_{p^2}{\vert}$$. Thus, $$n = p+1$$, as desired.

    By the above claims, we have that $$P$$ is a Sylow $$p$$-subgroup, as desired. It is non-abelian as $$\sigma$$ does not commute with $$(1\ 2\ \ldots\ p)$$.

    ---

47. Write and execute a computer program which
    (i) gives each odd number $$n < 10,000$$ that is not a power of a prime and that has some prime divisor $$p$$ such that $$n_p$$ is not forced to be 1 for all groups of order $$n$$ by the congruence condition of Sylow's Theorem, and
    (ii) gives for each $$n$$ in (i) the factorization of $$n$$ into prime powers and gives the list of all permissible values of $$n_p$$ for all primes $$p$$ dividing $$n$$.

    __Solution:__ The code can be found [here](sylow.py) and the output [here](sylow-odd.txt).

    ---

48. Carry out the same process as in the preceding exercise for all even numbers less than 1000. Explain the relative lengths of the lists versus the number of integers tested.

    __Solution:__ The same code as earlier works with the values adjusted. The output can be found [here](sylow-even.txt).  
      
    Note that every even number which is not a power of 2 will appear because if it of the form $$2^am$$ for some odd $$m > 1$$, then $$n_p$$ always has at least 2 possibilities. Namely, $$1$$ and $$m$$.  
    Due to this, 491 of the 499 even numbers appear in this list. The 8 that don't are the powers of 2.  
      
    On the other hand, in the case of question 47, only 1714 of the 4998 numbers appear in the list. 

    ---

49. Prove that if $${\vert}G{\vert} = 2^nm$$ where $$m$$ is odd and $$G$$ has a cyclic Sylow 2-subgroup then $$G$$ has a normal subgroup of order $$m$$.

    __Solution:__ We shall be using the following proposition.  
    __Proposition.__ Let $$G$$ be a finite group and $$x \in G$$ be such that $${\vert}x{\vert}$$ is even and $$\frac{|G|}{|x|}$$ is odd. Then $$G$$ has a (normal) subgroup of index 2.  
    This proposition is a result of Exercises 11 and 12 of Section 4.2.  
      
    Let us fix the odd natural $$m$$ and prove the result via induction on $$n$$.  
    For $$n = 1$$, the result follows because there exists an element of order 2. The subgroup of index 2 given by the proposition has order $$m$$ and is necessarily normal.

    Assuming the result to be true for $$n-1$$, we now prove it for $$n \ge 2$$.

    Let $$x$$ be a generator for the cyclic Sylow 2-subgroup. Then, $$x$$ has order $$2^n$$ and hence, satisfies the hypothesis of the proposition. Thus, there is a normal subgroup $$K \lhd G$$ of order $$2^{n-1}m$$. Now, by the induction hypothesis, there exists $$N \lhd K$$ such that $${\vert}N{\vert} = m$$.  
    Now we show that $$N \lhd G$$.

    __Claim 1.__ $$N$$ is the unique subgroup of $$K$$ of order $$m$$.  
    _Proof._ Suppose $$N'$$ is a subgroup of $$K$$ of order $$m$$.  
    Note that $$NN'$$ is a subgroup of $$K$$ as $$N \lhd K$$. Let us calculate the order of this group.

    $$|NN'| = \dfrac{|N||N'|}{|N \cap N'|} = \dfrac{m^2}{|N \cap N'|}.$$

    Clearly, $${\vert}NN'{\vert}$$ is odd. However, note that $$m$$ is the greatest odd number that divides $${\vert}K{\vert}$$ and thus, for $${\vert}NN'$$ to divide $${\vert}K{\vert}$$, we must have $${\vert}N\cap N'{\vert} = m$$ which is possible iff $$N = N'$$, as desired.

    __Claim 2.__ $$N \lhd G$$.  
    _Proof._ Let $$g \in G$$ be arbitrary. Consider the automorphism $$\varphi_g:G \to G$$ given by $$\varphi_g(x) = gxg^{-1}$$.  
    As $$K \lhd G$$, we have $$gKg^{-1} = K$$. That is to say, the automorphism $$\varphi_g$$ of $$G$$ restricts to an automorphism of $$K$$.  
    Thus, $$\varphi_g(N)$$ is a subgroup of $$K$$ of order $$m$$. By Claim 1, it is forced that $$\varphi_g(N) = N$$ or $$gNg^{-1} = N$$.  
    This concludes the proof.

    ---

50. Prove that if $$U$$ and $$W$$ are normal subsets of a Sylow $$p$$-subgroup $$P$$ of $$G$$ then $$U$$ is conjugate to $$W$$ in $$G$$ if and only if $$U$$ is conjugate to $$W$$ in $$N_G(P)$$. Deduce that two elements in the
center of $$P$$ are conjugate in $$G$$ if and only if they are conjugate in $$N_G(P)$$.

    __Solution:__ It is clear that if $$U$$ and $$W$$ are conjugates in $$N_G(P)$$, then they are conjugates in $$G$$. (By definition, there must exist some $$g \in N_G(P)$$ such that $$gUg^{-1} = W$$. The same $$g$$ also belongs to $$G$$.)

    We now show the reverse. Let $$g \in G$$ be such that $$gUg^{-1} = W$$. Equivalently, $$g^{-1}Wg = U$$.

    __Claim 1.__ $$gPg^{-1} \subset N_G(W)$$.  
    _Proof._ Let $$x = gpg^{-1}$$ for some $$p \in P$$. Then, we have

    $$xWx^{-1} = gpg^{-1}Wgp^{-1}g^{-1} = gpUp^{-1}g^{-1} = gUg^{-1} = U.$$

    We used the fact that $$pUp^{-1} = U$$. ($$\because U \lhd P$$.)

    Now, note that $$gPg^{-1}$$ is a $$p$$-group. Moreover, normality of $$W$$ in $$P$$ implies that $$P \le N_G(W)$$. Thus, $$P$$ is a Sylow $$p$$-subgroup of $$N_G(W)$$ as well.  
    By the second Sylow Theorem, there exists $$x \in N_G(W)$$ such that $$xgPg^{-1}x^{-1} = P$$. This gives us that $$y = xg \in N_G(P)$$. We now show that $$y$$ conjugates $$U$$ to $$W$$, as desired.

    $$yUy^{-1} = xgUg^{-1}x^{-1} = xWx^{-1} = W,$$

    where the last equality follows since $$x \in N_G(W)$$.

    Deduction: Consider $$U = \{x\}$$ and $$W = \{y\}$$. (Note that $$U$$ and $$W$$ were just _subsets_ in the above. Not necessarily subgroups.)

    ---

51. Let $$P$$ be a Sylow $$p$$-subgroup of $$G$$ and let $$M$$ be any subgroup of $$G$$ which contains $$N_G(P)$$. Prove that $${\vert}G : M{\vert} \equiv \mod p$$.

    __Solution:__ Note that we have the following tower of subgroups

    $$P \le N_G(P) \le M \le G.$$

    __Claim 1.__ $$P$$ is a Sylow $$p$$-subgroup of $$M$$.  
    _Proof._ Trivial by consideration of orders of the groups given in the tower.

    __Claim 2.__ $$N_M(P) = N_G(P)$$.  
    _Proof._ $$(\subset)$$ Follows from the fact that $$M \subset G$$.  
    $$(\supset)$$ Follows from the fact that $$N_G(P) \subset M$$.

    __Claim 3.__ $${\vert}G:N_G(P){\vert} \equiv {\vert}M:N_M(P){\vert} \equiv 1 \mod p$$.  
    _Proof._ The quantities are $$n_p(G)$$ and $$n_p(M)$$, respectively.

    Now, observe that 

    $${\vert}G:M{\vert}{\vert}M:N_G(P){\vert} = {\vert}G:N_G(P){\vert} \equiv 1 \mod p$$

    $$\implies {\vert}G:M{\vert}{\vert}M:N_G(P){\vert}  \equiv 1 \mod p$$

    $$\implies {\vert}G:M{\vert}{\vert}M:N_M(P){\vert}  \equiv 1 \mod p$$

    $$\implies {\vert}G:M{\vert}\cdot1 \equiv 1 \mod p$$

    $$\implies {\vert}G:M{\vert} \equiv 1 \mod p.$$

    ---

52. Suppose $$G$$ is a finite simple group in which every proper subgroup is abelian. If $$M$$ and $$N$$ are distinct maximal subgroups of $$G$$ prove $$M \cap N = 1$$.

    __Solution:__ Let $$H = M \cap N$$ and $$K = N_G(H)$$.  
    As $$M$$ and $$N$$ are abelian (since a maximal subgroup is proper), we see that $$M \le K$$ and $$N \le K$$.  
    Since $$M \neq N$$, we must have $$G = K$$. (Else, maximality would force $$M = K = N$$.)  
    Thus, $$G = N_G(H)$$ or $$H \lhd G$$. As $$G$$ is simple, this forces $$H = 1$$. (Since $$H$$ is clearly not $$G$$.)

    ---

53. Use the preceding exercise to prove that if $$G$$ is any non-abelian group in which every proper subgroup is abelian then $$G$$ is not simple.

    __Solution:__ Let us assume that $$G$$ is simple. We show that this leads to a contradiction via a series of claims.  
    __Claim 1.__ $$G$$ equals the union of its maximal subgroups.  
    _Proof._ Given any $$x \in G$$, there is a maximal subgroup $$M \ge \langle x\rangle$$ and hence, $$x \in \bigcup_{M \le G\text{ is maximal}}M.$$ (Every subgroup of a finite group is contained in some maximal subgroup.)

    __Claim 2.__ Any conjugate of a maximal subgroup is maximal.  
    _Proof._ Let $$M$$ be a maximal subgroup of $$G$$ and $$g \in G$$. We show that $$gMg^{-1}$$ is maximal.  
    Suppose $$gMg^{-1} \le H$$. We wish to show that either $$H = gMg^{-1}$$ or $$H = G$$. That is to say, $$H \in \{gMg^{-1}, G\}$$.  
    
    $$gMg^{-1} \le H \implies M \le g^{-1}Hg \implies g^{-1}Hg \in \{M, G\},$$

    where the last implication follows since $$M$$ is maximal. The conclusion follows by noting $$gGg^{-1} = G$$.

    __Claim 3.__ $$\langle 1\rangle$$ is not a maximal subgroup of $$G$$.  
    _Proof._ We first note that $$G \neq \langle 1\rangle$$ as $$G$$ is non-abelian. Thus, there is some $$x \in G$$ such that $$x \neq 1$$. If $$\langle 1\rangle$$ were maximal, then $$\langle x\rangle$$ would be forced to be $$G$$. This would then imply that $$G$$ is abelian. A contradiction.

    __Claim 4.__ Given any maximal subgroup $$M$$, we have $$N_G(M) = M$$.  
    _Proof._ Note that $$M$$ is a proper subgroup of $$G$$ and hence, cannot be normal. ($$M \neq 1$$ by the previous claim.)  
    Thus, $$N_G(M) \neq G$$. However, $$M \le N_G(M)$$ and thus, maximality of $$M$$ forces $$M = N_G(M)$$.

    __Claim 5.__ There are at least two conjugacy classes of maximal subgroups.  
    _Proof._ Suppose not. Then, there is a maximal subgroup $$M \le G$$ such that given any maximal subgroup $$M' \le G$$, there is some $$g \in G$$ such that $$M' = gMg^{-1}$$. Conversely, by Claim 1, we know that all conjugates are indeed maximal subgroups.  
    Now, note that the number of conjugates of $$M$$ is $${\vert}G:N_G(M){\vert} = {\vert}G:M{\vert}$$. (Equality follows due to the previous claim.)  
    
    By the previous exercise, we see that that any two conjugates must intersect trivially. Thus, we get that the total number of non-identity elements in the union of all the conjugates is:

    $$({\vert}M{\vert} - 1){\vert}G:M{\vert} = {\vert}G{\vert} - {\vert}G:M{\vert},$$

    where the equality follows from Lagrange's theorem stating $${\vert}M{\vert}{\vert}G:M{\vert} = {\vert}G{\vert}$$.

    Thus, the _total_ number of elements contained in the union is 

    $${\vert}G{\vert} - {\vert}G:M{\vert} + 1 < {\vert}G{\vert},$$

    where the last equality follows due to the fact that $$M \neq G$$ and hence, $${\vert}G:M{\vert} > 1$$.

    However, this is a contradiction as the union of all the conjugates is the union of all maximal subgroups, which in turn, equals $$G$$, by the first claim.

    __Claim 6.__ $$G$$ contains more than $${\vert}G{\vert}$$ elements. (The contradiction.)  
    _Proof._ By the previous claim, there exist two non-conjugate maximal subgroups, $$M$$ and $$N$$.  
    By the same counting argument as in the above proof, we see that $$G$$ must contain at least

    $$({\vert}M{\vert} - 1){\vert}G:M{\vert} + ({\vert}N{\vert} - 1){\vert}G:N{\vert} + 1 \text{ elements}.$$

    Rearranging the above gives us

    $${\vert}G{\vert} + ({\vert}G{\vert} - {\vert}G:M{\vert} - {\vert}G:N{\vert}) + 1.$$

    We now focus on the term inside the bracket. First, note that by Claim 3, we have $${\vert}M{\vert} \ge 2$$ and $${\vert}N{\vert} \ge 2$$. This gives us that

    $$\dfrac{1}{|M|} + \dfrac{1}{|N|} \le 1.$$

    Thus, the terms in the bracket simplifies as

    $${\vert}G{\vert} - {\vert}G:M{\vert} - {\vert}G:N{\vert} = {\vert}G{\vert}\left(1 - \dfrac{1}{|M|} - \dfrac{1}{|N|}\right) \ge 0.$$

    Hence, we see that 

    $${\vert}G{\vert} + ({\vert}G{\vert} - {\vert}G:M{\vert} - {\vert}G:N{\vert}) + 1 > {\vert}G{\vert}.$$

    Thus, we are done.

    ---

54. Prove the following classification: if $$G$$ is a finite group of order $$p_1\cdots p_r$$ where the $$p_i$$s are distinct primes such that $$p_i$$ does not divide $$p_j - 1$$ for all $$i$$ and $$j$$, then $$G$$ is cyclic.

    __Solution.__ We prove this via induction on $$r$$. For $$r = 1$$, it is clear as the only group (up to isomorphism) of a prime order is the cyclic group of that order.  
    We now show that $$G$$ is abelian.  

    __Claim.__ $$G$$ is abelian.  
    _Proof._ Suppose that $$G$$ were not abelian. Then, by the previous exercise, $$G$$ is not simple. Let $$N$$ be a proper nontrivial subgroup of $$G$$.  
    Then, $$N$$ has order $$q_1\cdots q_s$$ where each $$q_i$$ belongs to $$\{p_1, \ldots, p_r\}$$ and all the $$q_i$$s are distinct. Moreover, we have $$1 \le s < r$$. Thus, by induction hypothesis, we have that $$N$$ is cyclic.

    As $$N$$ is normal in $$G$$, $$G$$ acts on $$N$$ by conjugation which induces a homomorphism $$\Phi:G \to \operatorname{Aut}(N)$$.  
    Now, note that $$N$$ being cyclic implies that $$\operatorname{Aut}(N)$$ has order $$\varphi(q_1\cdots q_s) = (q_1 - 1)\cdots(q_s - 1)$$.  
    Moreover, we must have that $${\vert}G/\ker\Phi{\vert} \mid (q_1 - 1)\cdots(q_s - 1)$$.  
    As none of the $$p_i$$s divide any of the $$(q_j - 1)$$s, we see that $$\ker\Phi = G$$. In other words, the action is trivial and $$gng^{-1} = n$$ for all $$n \in N$$ and $$g \in G$$.  
    This tells us that $$N \le Z(G)$$. In particular, $$Z(G)$$ is not trivial.  
    From this and the induction hypothesis, we deduce that $$G/Z(G)$$ is cyclic. This proves that the group is abelian. (See [this](/alg/groups/GZ-cyclic-abelian).)

    Now, that we know the group is abelian, we are almost done. We just need to prove the following claim:

    __Claim.__ For each $$i \in \{1, \ldots, r\}$$, there exists an element of order $$p_i$$.  
    _Proof._ This follows directly from Cauchy's theorem. (cf. Exercise 3.)  
    Alternately, one may see that each Sylow $$p_i$$-subgroup is of order $$p_i$$ and conclude.  
      
    For each $$i \in \{1, \ldots, r\}$$, let $$x_i$$ denote an element of order $$p_i$$. (Which exists, by the above claim and since everything is finite, no need to worry about Choice.)  
    Now, the element $$x = x_1\cdots x_r$$ has order $$p_1\cdots p_r = {\vert}G{\vert}$$ and thus, $$G$$ is cyclic.

    ---

55. Prove the converse to the preceding exercise: if $$n \ge 2$$ is an integer such that every group of order $$n$$ is cyclic, then $$n = p_1p_2\cdots p_r$$ is a product of distinct primes and $$p_i$$ does not divide $$p_j - 1$$ for all $$i$$, $$j$$.

    __Solution.__ Suppose not. We then show that there exists a non-cyclic group of order $$n$$.  
    
    __Case 1.__ The primes are not distinct. Then, $${\vert}G{\vert} = p^2n$$ for some prime $$p$$. ($$p$$ and $$n$$ not necessarily coprime.)  
    Consider the group $$G = \mathbb{Z}_p \times \mathbb{Z}_p \times \mathbb{Z}_n$$. Clearly, this has the desired order.  
    This is not cyclic as $$x^{pn} = 1$$ for all $$x \in G$$. In particular, $$G$$ has no element of order $$p^2n$$.

    __Case 2.__ $$p_i \mid (p_j - 1)$$ for some $$i$$, $$j$$. Then $${\vert}G{\vert} = pqn$$ for some primes $$p$$ and $$q$$ such that $$p \mid q - 1$$.  
    We first construct the following non-abelian group $$H$$ of order $$pq$$:  
    Let $$Q$$