# What is good design?

A good design is easy to understand. 

That is very important. But even more import is, that a good design is easy to change

As Andrew Hunt and Dave Thomas stated it in Pragramatic Programmer, a good measurement for a good design is "How easy is the system to change"?

This is one of the core messages of this complete course. A good design is easier to change than a bad design. 

We can use this question to ask ourself during the development, will this implementation make my system easier or harder to change?

If we think about our network connection. How hard will it be if we want to process UDP datagrams instead of tcp packets? Which parts of our system need to be changed

# How do we want to change the system?

Open Close Principle. The O of the SOLID Pattern by Robert C. Martin. 
We want the system to be changed by writing new code. That there are already the right abstractions there for us. 
We don't need to change the abstractions to implement a new feature. We can simply create a new class with the needed functionality and plug it in, like a usb device and everything works. 

# How can we find the right abstractions in our system?
We want to anticipate what will change in the future. If we think it is likely that it will change in the future than we define an abstraction for that. 

# Abstractions and Layers
We can see an abstraction as a layer. We can swap out the things under the layer and everything will still work. 

# Too much abstraction
We make our system harder to change if we make it too abstract. As always it is a tradeoff. Abstractions make our system more complex, but it allows us to change it more easily. It's like a tradeoff between computational complexity and disc space. We can save computational ressources if we store precalculated values on disc. But this leads to more occupied disk space. So it is a tradeoff. 
