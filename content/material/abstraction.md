# What is good design?

In this chapter we try to answer the fundamental question: What is good design? How can it be described? And what questions do we need to ask ourselfs during development that will lead to good design?

## Easy To Change

It is difficult to break "good design" down into a single value. But Andrew Hunt and Dave Thomas did a great job in the book [Pragramatic Programmer](./literature.md). They stated: **"Good design is easier to change than bad design"**. 

That's it. That is the ETC princple: *Easier to change. ETC*. 

A system has a better design if it is easy to change. If it is difficult to change, than the design is worse.

Keep the ETC value in your head during the proceeding of this course. Ask yourself during the development: "Will this implementation make my system easier or harder to change in the future?".

At this point you should have implemented a TCP network connection to receive books in the json format over network. Ask yourself: "Is it easy for a me to change to another network framework? Is it easy for me to change the transmission protocol to UDP?".

If your answer is "yes", it is more likely that your design is good. 

Most design principles, patterns and akronyms are closly related to the ETC value. We will talk about simplicity and readability now, but there is more to come during the course.

## Simplicity
A good design is simple and easy to understand. If we understand it well, we can change it more easily. So this property directly pays into the **ETC** property.

If you have the same functionality in two systems (system *A* and *B*) and system *A* is way simpler (e.g. less code, less classes, little inheritance hierarchie), than the simpler system *A* is more likely to be the better system.

There is this tale about a country paying thousands of dollers to a company which should delevope a ball pen that can write in space without gravity. Another country just uses a lead pencil in space. I don't know if this story is true, but it gets the point very well. You have more or less the same functionality, but one is way simpler so the solution is superior.  

## Readability
 Source code is written once and maybe changed one time on a later point while refactoring. But it is read way more often. So if we can understand the source code quite well, we can change it more easily. That's why readability is also a supporting metric to ETC. 

# How do we want to change the system?
If we need to change our system, e.g. we get a new requirement from our customers that we need to implement, than the question arises: *How* do we want to change the system?

We can implement new features by **changing existing code** or by **adding new code**. The **open-close-principle** (originated by Bertrand Meyer in the 1980s) states, that a system is easier to change, if we can implement a new requirement by adding new code, rather than changing existing code (Open for extension, closed for modification).

Let's have a look at this example:

![](images/NetworkServer.png)

The above picture shows an UML class diagram. A client (this can be simply another class) has a dependency to an abstract `NetworkServer`. This `NetworkServer` has two implementations: a `TCPNetworkServer` and an `UDPNetworkServer`.

Because we already have the right abstractions (in this case the interface `NetworkServer`) it is very easy for us to implement a different kind of network server by adding a new class that will inherit from NetworkServer. 

We have fullfilled the open-close-principle (OCP). Due to this principle we also fulfill the value *easy to change* (ETC) and so we can consider our design as good.

# How can we find the right abstractions in our system?
We want to anticipate what will change in the future. If we think it is likely that it will change in the future than we define an abstraction for that. 

# Abstractions and Layers
We can see an abstraction as a layer. We can swap out the things under the layer and everything will still work. 

# Too much abstraction
We make our system harder to change if we make it too abstract. As always it is a tradeoff. Abstractions make our system more complex, but it allows us to change it more easily. It's like a tradeoff between computational complexity and disc space. We can save computational ressources if we store precalculated values on disc. But this leads to more occupied disk space. So it is a tradeoff. 
