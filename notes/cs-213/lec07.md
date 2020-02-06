---
layout: page
title: CS 213
subtitle: Lecture 7
image:
---
Main theme of today: Linked lists. Examples and motivations later.  
More specifically, we'll get into _Singly link list_.  
## Linked lists
Collection of elements → dynamic.  
We start with an empty collection.  
We can add one or more elements.  
Similarly, we may delete one or more elements.  

#### Visual feel - how does it go?
You start with an empty rectangle.  
Then, you add one more element. The original rectangle stores the address of the next.  
In general, you get a sequence of rectangles with each storing some value as well as the next address.  
To get till the 5th guy, you need to hop from one to the other.  
Thus, it's $$O(n)$$. This is different compared to array, where the look up was $$O(1)$$.  
  
Note - header doesn't store any value. Just the address. The later ones store a value and the address of the next guy.  

To delete some element, we just "short circuit" the list.

#### What do we require?
1. Heterogeneous collection → we're storing addresses and values.
    This is done using `class`/`struct`.  
    Also, the values themselves can be of different types.  
2. Addresses of memory addresses as a data type.
    `*` operator helps us.
3. Ask or surrender memory chunks at runtime.
    We don't know how much memory we require at compile time.

#### Semantics
`new( )` → in the `( )` part, we put the data type and we get memory based on that.  
`delete( )` → in the `( )` part, we put the address.  
  
`T* name`. Here, `T` can be of any type. (User or predefined.)  
Any pointer has size 8 bytes. (This 8 depends on the architecture, assume 64 bits.)  
Then, `name` will be a pointer to an object of type `T`.  

Example.  
```C++
int a = 10;  
int * p = &a;
```

`p` will store the address of the `int` object `a`.  
The following would've given an error:
```C++
float pi = 3.14;  
int * p = &pi;
```

`p` can only store the address of an `int` object.

Consider the following code:
```C++
int *p;  
cout << p << &p << *p << endl;
```

We should get: `garbage address ??` where `??` could either be segmentation fault (if lucky) or some random value.  
`p` will give us the random garbage that's in the location of `p` originally.  
`&p` will give us the address of `p`.  
`*p` will give us the value stored at the address which was stored in `p`. (the original garbage.) This could be any random memory location anywhere.

## Defining class
```C++
class list
{
    int value;
    node * next;
}
```

This is just a class by itself, not doing anything.  
Now, we put the empty rectangle (box) mentioned earlier.  

`node * header = 0` does that.  
Now, we want to make new boxes.  
We use the `new` keyword.  

```C++
while(...)
{
    node * p = new node;    // sanity check 
        //check whether you do have the memory
    p -> value = 1;  
    p -> next = 0;          // these are just example values
} 
```
Normally, we'll put something like `p -> next = head` for inserting.

#### Different operations on lists
* `create()`
* `isempty()`
* `number of elements in the linked list()`
* `insert()` (at the head/beginning)
* `append()` (at the end)
* could also want to insert somewhere in between
* `delete()`
* `remove()` (first occurrence only)
* `concatenate()` (two lists)
* `display()`

We want to create a good enough class `list` such that we could do operations such as:
```C++
int main(){
    list l1, l2, l3;  
    while(in >> val) l1 = l1 + val;  
    while(in >> val) l2 = l2 & val;  
    l3 = l1 + l2;  
    cout << l1 << l2 << l3 << endl;
}
```

We will redefine the operators so that we can use `+` for `insert`, `&` for `append`, et cetera.  
  
```C++
list.operator+(val){
    // list inserted with val as first element
}  
list.operator&(val){
    // list with val at the end
}
list.operator+(list){
    // concatenate
}
```

Note that we've defined `+` twice. However, we have different argument types. So, the compiler will know what to do.  
We also want to overload `<<` to print lists directly.  
Thus, we want to make a good definition in `class list{};` so that we can use all these operations.

`insert` is $$O(1)$$. (Refer the code of list given by professor.)

##### [Prev](/notes/cs-213/lec06) | [Next](/notes/cs-213/lec08)
#### [CS 213](/notes/cs-213)