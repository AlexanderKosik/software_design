# Implementation part III

In this chapter we will provide an interface for our end users. 

## Status Quo:
At this point the RCP should be able to receive json files over network and can persist the information in a database. 

## Providing an interface
There are many interface technologies and frameworks to provide data to an enduser. In our case a REST api is very well suited for our application. 

First, what is an API?

### Application Programming Interface
An API defines a kind of contract between two or more parties. The content of the contract highly depends on the specified API. Let's say our API the content provider is our RCP and the information receiver is a client (e.g. a mobile app or another system).

In our API description we provide information about what information the client can request from us, how the information can be requested and how does the answer to the request look like.

### What is REST?

REST ist mostly used in machine-to-machine communication. 

If you are using Python as a programming language, you can use FastAPI or Flask as an REST framework. You will find an overview over Python REST API Frameworks [here](https://rapidapi.com/blog/best-python-api-frameworks/). 
