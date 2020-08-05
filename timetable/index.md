---
layout: page
title: LaTeX Timetable
subtitle: Tutorial of sorts
image: img/latex.png
---

Note that this is made for IITB timetables, customised to the slots here.  

# Part I: Getting the LaTeX code generated

## If you have Python installed

1. Download [this text file](/timetable.txt).
2. Download [this python file](/timetable.py) __in the same folder.__
3. Modify the text file as per the instructions below. (Save the modified changes in the same file. The filename should be `timetable.txt` in the same folder as the python code.)
4. Compile the python code.

## If you don't have python installed

1. Open any online service that lets you compile python online while also accepting input. (For example, [this](https://www.tutorialspoint.com/execute_python_online.php).)
2. Open [this text file](/timetable.txt) and copy the content in the input area.
3. Open [this text file](/timetable-online-code.txt) which contains the Python code customised for online purposes. Copy the content into the code area.
4. Modify the content in the input area as per the instructions below.
5. Compile the code.

# Part II: Generating the table

1. Download [this tex file](/timetable.tex). (If you don't have a local LaTeX compiler, you can use some online service like [Overleaf](https://www.overleaf.com/).)
2. You can can modify the title on line 25. (Alternately, search for the phrase "MODIFY TITLE" in the file.)
3. Copy the output of the python code and replace the comment "% INSERT CODE HERE" (on line 32) with the output.
4. Compile.

# Instructions

So, here's how you should modify the .txt file:

The main lines of the .txt file follow the following format:  

`slot>>x>>x`  

(Do __not__ change the `>>`s!)

Do not modify the `slot`. You can modify the next two `x`s. Typically, you'd want to make the first `x` the course code and the second `x` the location. (Hopefully, in-campus classes have started.)  
This is up to you.  
Note that you _can_ put a space in course code and locations. For example, `MA 105` and `LA 101` are fine.  
However, __maintain__ the two `>` in between.  

The thing to keep in mind is that when the code is compiled, each cell will have two lines: the top line will be the first `x` and the second line will be the second `x`.

The nice thing is that if you leave an `x` as it is, then the code will ignore it. That is, you don't _have_ to modify it. (In particular, if you don't have anything in slot 6, you don't have to make any changes.)

Now, you may observe that there's slot 1 and also 1A, 1B, 1C.  
If you have the same course (and location) in all the three sub-slots, you only need to fill information in slot 1 and leave the rest blank.  
However, if you do fill 1A, then the information of 1A will be given priority over 1.  
If you fill 1 and 1A but not the rest, then 1B and 1C will follow whatever you've filled for 1.  

As an example, you can see [this](/example.txt) file.  
(Since there's no point of location this semester, I've used the second `x` for course name. I also haven't exploited the sub-slots feature.)

### Extra hacks
If you do know LaTeX yourself, then you can add some input additional stuff using your knowledge. For example if you want to add three lines to slot 5A, you can do the following:  
`5A>>CS 101>>LA 101\\(9:30 - 10:55)`

Since LaTeX reads `\\` as a newline, you'd be done.  
You can even get funkier and use math commands (within math mode, of course). Up to you. (Note to modify the file to import the relevant packages.)

# Feedback
If there are any errors or if you want to suggest something, you can either [mail me](mailto:aryamanmaithani@gmail.com) or drop a message [here]({{ site.anon-form }}){:target="_blank"}.