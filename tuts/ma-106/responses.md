---
layout: page
title: Responses
subtitle: My responses to some of the anonymous feedback sent
image:
---
> "This is rather a very plain, basic message/question. It used to be more strategic approach to questions, now its more and more of understanding "stuff", which I am sort of failing at. But when I see your approach (and most of the students in my group) to questions, I don't think I can ever be so detailed at solving math, considering all the given conditions and stuff (specially, proving things), I sort of never know where to start from and even if I do, I never know how to continue. Does this mean, I've got to refer to books and practice (a lot :/) to develop my understanding in more of a *mathematical* way (because at this point, I'm just-- sort of clueless)? 
> 
> (P.S. It went too lengthy, sorry. XD)"  
> \- [NAME REDACTED]  
> 24/02/2020, 13:58

Hey,  
I guess it _is_ true that you'd have to put in efforts. One nice thing to do would be to find another person who's also interested and just run your proof/ideas past them and ask them to find flaws. Conversely, you do the same for them.  
This will help in strengthening your thought process. A lot of problem that people face in "writing proofs" just comes from lack of logical reasoning from one step to the other. Mathematical arguments rely mainly on the definitions and axioms, that is, having some starting set of rules and seeing what you can logically deduce from those.  
In the end, have fun!

---

> "how can we prove the cayley hamilton theorem for a general square matrix? I was able to prove it for diagonalizable matrix but can't generalize the result."  
> \- [NAME REDACTED]  
> 21/02/2020, 13:21

I don't think the responses page is really a good place to get an answer for something like this as the proof does get a bit involved.  
The idea is the following:  
Suppose $$T: V \to V$$ is a linear transform. Let $$p_T(x)$$ denote its characteristic polynomial. We want to show that $$p_T(T)$$ is the zero function.  
First prove this: Given any subspace $$W \subset V$$ such that $$T(W) \subset W$$, we have that the characteristic polynomial of $$T|_W$$ divides $$p_T(x)$$.  
Then, you show that given any $$v \in V$$, the space $$W = \operatorname{span}\{v, T(v), T^2(v), \ldots\}$$ has the property that $$T(W) \subset W$$. ($$T^2(v) = T(T(v))$$ and so on.)  

Conclude that $$p_T(T)v = 0$$. As this will be true for all $$v \in V$$, you get that $$p_T(T)$$ is the zero operator.

---


> "Firstly, thanks for all your help with MA105. I've never personally(or anonymously) asked you a question before, but your doubt clearing on the Whatsapp groups and the tut solutions saved my ass and got me a good grade.  
>  
>I am once again asking for your academic support.  
>  
>Please, upload the solutions of the practice problems of just tut sheet 3; nothing more, nothing less. The proofs are either too trivial-seeming or too difficult for me (and my friends) to prove."  
> \- Bernie  
> 16/02/2020, 21:19

Hello, Bernie. I'm happy to know that I could (indirectly) help you out during MA 105.  
Either you haven't seen this page or you've chosen to ignore the other response where I said that I won't upload solutions/hints of the practice problems.  
However, I really enjoyed reading your response. So, [here](https://github.com/aryamanmaithani/ma-106-tut/blob/master/Hints/tut-3-extra.pdf) you go.  

---

> "If we are able to understand lecture slides, would you still recommend reading Gilbert Strang/ solving problems from it? "  
> \- x  
> 02/02/2020, 18:49

Well, this depends mainly on what the purpose of asking this question.  
If you want to know from the point of view of exams/grades, then I guess it's fine even if you don't read anything extra.  
If it's from the perspective of learning more, then well, it never hurts.

---

> "I am a bit confused about the properties of the rank of matrices, particularly those where we take the product of two matrices. It would of great help if you list some properties with a little explanation"  
> \- Charlie Harper  
> 02/02/2020, 16:16

I'm not very sure as to what your confusion is.  
Tutorial 3 question 4 does address the relation between ranks of matrices and their product.  
Moreover, using question 1 you can recover also get more information.  
If there's something more particular that you want, you may drop another comment. Meanwhile, if I can think of something useful to post, I shall do so.

---

> "can you please upload ma106 tut solutions including the extra questions it would be really helpful"  
> \- ~  
> 28/01/2020, 21:40

I can but I won't. We have been told to not give solutions. I do upload hints for the tutorial questions, though.
I will not do that for extra questions as it'll be too time consuming for me as well. Plus, you should attempt them yourself and ask your TA (or mail me) if you have doubts.

---

> "Hey, can you post a document on introduction to infinite vector spaces at some point?"  
> \- Axiom of Choice  
> 28/01/2020, 11:57

You're my new favourite person. I shall post something as soon as I can.

---
> "we wanted you as our ta again"  
> \- d1 t5 nibba  
> 27/01/2020, 18:45

oof, sori.  
Although, I don't think you speak for *everyone*. 👀

---

> "So glad you are a TA for 106 and 108(hopefully) as well."  
> \- Every freshie  
> 18/01/2020, 20:59

I'm glad too and I hope so too!