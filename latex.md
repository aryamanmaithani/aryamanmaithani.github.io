---
layout: page
title: LaTeX
subtitle: Tutorial of sorts
image: img/latex.png
---

As you may have seen, I like $$\LaTeX$$. I encourage everyone to learn it.  
In my opinion, an efficient way of learning is to start making a document and googling the things along the way.  
To get started, I feel it's enough to just see one code and its output to get a sense of how it works. That's the point of this page.  
I would suggest you to first make an account (for free) on [Overleaf](https://www.overleaf.com/?r=6953fddc&rm=d&rs=b). (If you use this link, it counts as a referral for me.) Then, you may see [this](https://www.overleaf.com/read/smxvxtpbvjht) file of mine.  
I think that that contains more or less everything basic needed to get started.   
After familiarising yourself with LaTeX on Overleaf, you may move to an offline medium. For example, I use Sublime Text for all my LaTeX documents. One of the benefits of this (other than internet independency) is the setup of many shortcuts. The packages that I have installed on Sublime Text for LaTeX uses are LaTeXTools and LaTeXYZ.

Lastly, almost every LaTeX'd PDF on my repositories/website also has the source code uploaded. Simply changing the .pdf to .tex in the URL would do the job.  

Some more links:
* [DeTeXify](http://detexify.kirelabs.org/) - draw a symbol and it gives you the command
* [List of Mathematical Symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols) - exactly what it sounds like

Some things to keep in mind:
1. Don't put spaces before commas.
2. Use `\cdots`, `\ldots`, `\vdots` instead of manually making dots.
3. While we're on this topic, use   `\cdots` when putting dots between operators. For example, $$a_1 + \cdots + a_n.$$ Use `\ldots` when listing something. For example, $$S = \{a_1, \ldots, a_n\}.$$
4. My personal suggestion for proof-writing: try to use words rather than making it concise using $$\exists$$ and stuff. It improves readability. 
5. Similarly, use the environment `align*` if you don't need equation numbers. Only number those which you will refer to, later on.
6. Try to use display math `$$ ... $$` for important equations. This avoids clutter within sentences.
7. Very important - If you refer to a function or a variable, ALWAYS use the `$...$` environment even if it's not "necessary". $f$ and f look very different and that, in my opinion, is a sign of amateur writing.
8. Conversely, when you use functions like max, sup, min, write `\max`, `\sup`, `\min` while in math mode. These are recognised commands. If it's something not recognised, use `\text{...}` or `\operatorname{...}`.
9. Use `\displaystyle` to keep the limits formatted nicely. This is difference between $$\lim_{n\to \infty}$$ (`\lim_{n\to \infty}`) and $$\displaystyle\lim_{n\to \infty}$$ (`$$\displaystyle\lim_{n\to \infty}$$`).
10. Use `\|` instead of `||`.