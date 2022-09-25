[Back (Implementation I)](../impl_2/impl_2.md) | [Next (The End)](../impl_3/end.md)

# Implementation part III

In this chapter we will provide an interface for our end users. 

## Status Quo:
At this point the RCP should be able to receive json files over network and can persist the information in a database. 

## Providing an interface
There are many interface technologies and frameworks to provide data to an enduser. In our use case a REST API is very well suited for our application. 

But first things first: What is an API?

### Application Programming Interface
An API defines a kind of contract between two or more parties. The content of the contract highly depends on the specified API and is described in the API specification. 

Let's say our API has two parties: the content provider (our RCP) and the information receiver (a client, e.g. a mobile app or another system).

In our API description we provide information about what information the client can request, how the information can be requested and how does the answer to the request look like. This information is typically provided in the API description. 

You can read more about APIs on [this](https://en.wikipedia.org/wiki/API) wiki page.

### What is REST?

REST stands for Representational State Transfer and is a common API for web services. By using a REST API data gets delivered using URIs and the HTTP protocol. The data transfered from the data provider to the client is typically structured in the well known JSON format, but also other formats like XML or plain text are a valid alternative. 

A REST API is *stateless*, that means each request is separated from other requests and no prior actions need to take place before requesting and receiving the data. 

REST ist mostly used in machine-to-machine communication. 

# What information should our API provide?
1) Request a book based on author and title
2) Request all books with a given title
3) Request all books from an author

Is there more that makes sense?

## Possible frameworks to use
If you are using Python as a programming language, you can use FastAPI or Flask as an REST framework. You will find an overview over Python REST API Frameworks [here](https://rapidapi.com/blog/best-python-api-frameworks/). 

If you are using Java as a programming language, you can use Spring Boot for your REST interface. 

# Questions for reflection
1) Our API makes use of a principle called **information hiding**. What information is exactly hidden by our API?

2) What is the *Open API Specification* and how can it be used?

3) Did this requirement change your overall system architecture? Where is the source code for your API requests located? In a existing class, in a new class, in a new module, in a new application?

4) How scalable is your current design and implementation? Can you handle way more requests than you initially specified? What design can improve the scalability?

5) What other technologies instead of REST could be used for our API?

[Back (Implementation I)](../impl_2/impl_2.md) | [Next (The End)](../impl_3/end.md)

