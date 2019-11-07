---
layout: page
title: Responses
subtitle: My responses to some of the anonymous feedback sent
image:
---
> "Hey! Can you help me solve Q9(b) Sheet 14? And yes, please reply Bruce."  
> \- Natasha Romanoff

Consider $$ \psi = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2}$$.  
Note that the outwards unit normal $$\mathbf{n}$$ at any point $$\mathbf{r} = (x, y, z)$$ on the ellipsoid is in the same direction as $$\nabla \psi$$ and one also has $$p = \mathbf{r}\cdot\mathbf{n}$$. Also note that $$\mathbf{r}\cdot\nabla\psi=2$$. I will use these facts in the following equations. It is your task to see where I've used what and how.  
$$\displaystyle\iint_S\frac{1}{p}dS$$  
$$ = \displaystyle\iint_S\frac{1}{\mathbf{r}\cdot\mathbf{n}}dS$$  
$$ = \displaystyle\iint_S\frac{\mathbf{n}\cdot\mathbf{n}}{\mathbf{r}\cdot\mathbf{n}}dS$$  
$$ = \displaystyle\iint_S\left(\frac{\mathbf{n}}{\mathbf{r}\cdot\mathbf{n}}\right)\cdot\mathbf{n}dS$$  
$$ = \displaystyle\iint_S\left(\frac{\nabla\psi}{\mathbf{r}\cdot\nabla\psi}\right)\cdot\mathbf{n}dS$$  
$$ = \displaystyle\iint_S\left(\frac{\nabla\psi}{2}\right)\cdot\mathbf{n}dS$$  
$$ = \displaystyle\iiint_W\frac{\nabla^2\psi}{2}dV$$  
$$ = \displaystyle\left(\frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2}\right)\iiint_W 1dV$$   
$$ = \displaystyle\frac{4}{3}abc\left(\frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2}\right).$$  
Note that I have used Gauss' divergence theorem and the fact that the volume of $$W$$, the solid ellipsoid, is what it is. 

---

> "Can u explain in brief or post something about the alternative formulations of greens theorem."  
> \- Green

Could you be more specific as to what you want? The alternate formulations are there in slides and I'm not sure as to what more I can tell about that.

---

> "Q9 Sheet 12 is making me turn green. Please help!"  
> \- Bruce Banner

Here's an outline of what to do. Hopefully you can complete it.  
The hemisphere satisfies $$z = \sqrt{1 - x^2 - y^2}$$ and $$x^2 + y^2 \le 1$$.  
Using the fact that $$\mathbf{n}dS = (-z_x, -z_y, 1)d(x, y)$$.  
In this case, $$z_x = -x/z$$ and $$z_y = -y/z$$.  
Thus, $$\mathbf{F}\cdot\mathbf{n}dS = \frac{1 - 2xy - 2y^2}{z}d(x, y).$$  
(Note that both the above equations involving $$dS$$ are just written in differential notation. I'm not treating $$dS$$ as a real number or any such thing.)  
Now the mass blah blah blah stuff asked is just the flux which equals:  
$$\displaystyle\iint_S\mathbf{F}\cdot\mathbf{n}dS = \iint_D{1 - 2xy - 2y^2}{\sqrt{1 - x^2 - y^2}}d(x, y)$$.  
Where $$D = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 \le 1\}$$. The above can be solved using polar coordinates.

---

> "You could have quoted The Daily Bugle.  
I check this page every day, once in the evening and once before going to bed.  
I must admit that I envy and appreciate your math skills. Any tips?"  
> \- Peter Parker

Ah, looks like I don't remember it well enough to quote that.  
I guess just be patient and practice.

---

> "Parametization was the problem indeed.  
Speaking of revealing my identity, did you even watch my latest movie (till the very end)?"  
> \- Peter Parker

Oh, good to know that I solved your doubt then.  
Yes, I had, I was thinking of making a Mysterio reference but couldn't think of a nice one.  
P.S.: How often do you refresh this page to reply quickly enough?

---

> "My Spidey Sense tells me that Q7 Sheet 10 is a threat. Can you help me fight it?"  
> \- Peter Parker

Good job giving away your identity.  
I'm not sure what exactly is the problem with this question, though. I guess you had a problem finding a parameterisation for the curve $$C$$ because it's quite straightforward otherwise.  
Note that the cylinder is given by $$\left(x-\frac{a}{2}\right)^{2}+y^{2}=\frac{a^{2}}{4}$$.  
The equation of the sphere tells us that the points lying on the intersection, that is, the points of $$C$$ satisfy: $$z^2 = a^2 - ax$$.  
The first equation leads to the natural parameterisation of $$x = \frac{a}{2} + \frac{a}{2}\cos\theta$$ and $$y = \frac{a}{2}\sin\theta$$ where $$\theta \in [0, 2\pi]$$.  
Also, substituting this value of $$x$$ in the second equation and noting that $$z \ge 0$$ gives us that $$z = a\sin\frac{\theta}{2}$$.  
Thus, we now have a parameterisation for the curve and can (hopefully) easily solve it now.  
You just need to compute the integral $$\oint_C \mathbf{F}\cdot d\mathbf{r}$$. Check the solutions for the similar tutorial problems if you don't get it.

--- 

> "There should be summary of all the content covered in the tutorial in the start as you have done in week1 sheet. It will be very helpful"  
> \- Harry Potter

I'm not quite sure as to what you're referring to as there was no summary at the beginning of the Week-1 slides. But I guess I can add the questions covered at the beginning for easier reference.

---  

> "Tony forgot to ask Q9(ii) Sheet11. Please provide a solution for that too."  
> \- Thor Odinson

I guess MA 105 questions are an Avengers' level threat, huh?  
However, question 9 is indeed a nice question in my opinion. So, [here](https://github.com/aryamanmaithani/ma-105-tut/blob/master/Additional%20solutions/S11-Q09.pdf) you have the solution for all parts.

---  

> "Iron man has a problem with the solution too! Shouldn't phi_x=xf(r) instead of xf(x) in the first slide??"  
> \- Iron man 

Iron man is indeed correct. The typo has been fixed.

---  

> "Please provide a solution for Sheet 10 Q11"  
> \- Iron man 

Surely Iron man shouldn't be having a problem with this.  
Anyway, [here's](https://github.com/aryamanmaithani/ma-105-tut/blob/master/Additional%20solutions/S10-Q11.pdf) the solution.

---  

> "Can you please give the solution to Q7 Sheet 8?"  
> \- Freshie 

I *can* and I shall.  
By symmetry, the given volume is 8 times the volume in the positive octant.  
In that octant the volume lies above the region $$Q := \{(x, y, 0) \in \mathbb{R}^3 :x \ge 0, y \ge 0, x^2 + y^2 \le a^2\}$$ and underneath the cylinder given by $$x^2 + z^2 = a^2$$.  
Therefore,  
$$V = 8\displaystyle\int_0^a\left(\int_0^{\sqrt{a^2-x^2}}\left(\int_0^{\sqrt{a^2-x^2}}1dz\right)dy\right)dx = \dfrac{16a^3}{3}$$.

---  

> "You are really helpful .I attended tsc class you took.And I really understand the concept .Thanking You"  
> \- Enthu Wala frieshie 

That's what I hoped to do. Glad to know I was successful :)

---  

> "Thanks for taking the efforts to actually write out the solutions, they are really helpful. Hope I can do the same for a future batch."  
> \- Random Guy

You're welcome!  
P.S.: Nothing is stopping you from making your own solutions for your own batch. I'm sure that there are plenty of subjects for which solutions aren't being made.

---  

> "Can a continuous function with bounded and open domain be. integrable "  
> \- A person who is going to revolutionize whole world 

Yes, it *can*. But it's not necessary. This is because a continuous function need not be bounded on a bounded and open domain. (Think of an example.)  
Hence, the function won't be integrable.

---  

> "The solutions are very helpful! Thanks!"  
> \- someoneNotFromD1T5  

Ayy, I'm glad you find them helpful!  
Also, thanks for not asking me for physics solutions, lol.

---  

> "What about question 7 of tut sheet 6? what do they mean by bounded in a disc?"  
> \- CuriousFreshie  

Hello, what the question means is that given any $$\epsilon > 0$$ and any $$M \in \mathbb{R}$$, there will be a point $$(x_0, y_0)$$ in the disc of radius $$\epsilon$$ centered at origin such that the value of $$\mid f_x(x_0, y_0)\mid$$ is greater than $$M$$. (This is what is means for the derivative to *not* be *bounded* in any disc around $$(0, 0)$$.)

---  

> The 'mail me at this address' on your website (the MA105 page) has aryamanmaithani@gmial.com instead of aryamanmaithani@gmail.com.  
> \- Aryaman Maithani

Thanks a lot for pointing this out. Nice name!

---

> Hey!! great help. thanx a lot. a request. is it possible for you to upload solutions for phy tuts as well. thanx  
> \- 

I'm glad you find it helpful. You're most welcome. No, I won't be uploading solutions for physics tuts. I don't have the time for an extra subject.

---

> You are amazing bro.  
> \- [hiding name to protect privacy]

Thank you!

---

> can you upload solutions of tutorial sheets??  
> \-

I'm not quite sure how you missed the solutions which are pretty much the highlight of the page.  

---

> This site is very helpful. It would be nice if you could provide solution for extra question.  
> \- 

Hey, I'm glad you find the site helpful. However, I won't be uploading the solutions for extra questions. That would defeat the purpose of the questions. (Purpose being - you must think about them.)

---

> Good job  
> \- God

Thanks, God.