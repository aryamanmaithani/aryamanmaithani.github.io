---
layout: page
title: Responses
subtitle: My responses to some of the anonymous feedback sent
image:
---

> "doubt regarding theorem on pg 135 of Churchill-Brown reference book:i think i understand from  the theorem that if there is a function f continuous on a domain(any domain; no restrictions about simple connectedness were given) having an antiderivative on the same domain(the antiderivative just has to exist) would give 0 as the result of an integral along a contour lying entirely in the domain. they even proceed to show the application for f(z)=1/(z^2) on |z|>0. the slides seem to state sth different: requiring the function to be holomorphic on a simply connected domain at least, not to mention additional constraints on the contour of integration. please elaborate on the same. p.s.:thank you"  
> \- doubtful existence  
> 01/09/2020, 21:03

TL;DR - If you happen to know that $$f$$ has an antiderivative, then you need not care about the domain.  
However, given just $$f$$, the existence of antiderivative in not guaranteed. In the event that the domain is simply-connected, we have hope and can conclude that integral around closed loops is zero.

Full answer -  
Hey, thanks for an actual math question. Here's the point:  
__If__ $$f:\Omega \to \mathbb{C}$$ has an antiderivative $$F:\Omega \to \mathbb{C}$$ (i.e., $$F' = f$$), __then__ it is true that

$$\int_\gamma f = 0$$

for _any_ __closed__ path $$\gamma$$ in $$F$$. (Here, you do need the constraint that $$\gamma$$ is closed. Otherwise, even the example of $$z^{-2}$$ will give a counterexample. For example, take the path $$\gamma:[0, 1] \to \mathbb{C}\setminus\{0\}$$ given as $$\gamma(t) = e^{\iota\pi t/2}$$.)

Moreover, we restrict ourselves to the case of $$\gamma$$ being (piecewise) smooth so that we can _define_ the integral as

$$\int_{a}^b f(\gamma(t))\gamma'(t){\mathrm{d}}t.$$

Note that even Churchill has the following assumption in the definition of contour:  
  
> A contour, or piecewise smooth arc, is an arc consisting of a finite number of smooth  arcs joined end to  end.

With just these constraints on $$\gamma$$, it _is_ true that 

$$\int_\gamma f = 0.$$

However, note that this is under the assumption that __$$f$$ has an antiderivative $$F$$ on $$\Omega$$__.

The issue arises precisely because we don't know that a holomorphic function has an antiderivative on the same domain. For example, consider the holomorphic function

$$f:\mathbb{C}\setminus\{0\} \to \mathbb{C}$$

defined as

$$f(z) = \dfrac{1}{z}.$$

This is indeed holomorphic but

$$\int_\gamma f = 2\pi\iota,$$

where $$\gamma$$ is the unit circle centered at $$0$$ oriented counterclockwise.   
  
So, what went wrong? Well, it's precisely that $$f$$ has no antiderivative on the given domain. (The above computation is a proof of that! This is similar to how integrating in MA 105 let us conclude that a certain vector field is not the grad of anything, even though its curl was zero.)  
And indeed, our domain was _not_ simply-connected!

If you do want the (holomorphic) function to have integral zero about every closed loop, then you need to make further assumptions about the "shape" (read: topology) of the domain, which is why the slides had the further assumptions.

By the way, what you say as "additional constraints on the contour of integration", I guess you mean the stuff after the piece-wise smoothness. Note that that was actually _weakening_ the conditions on $$\gamma$$, requiring it to be just rectifiable and so forth. So, to summarise - the slides did not state anything weaker.