# Project RCP: Recommerce Platform

In this project we create a recommerce platform. A recommerce platform is a software platform that manages used media items such as books.

We start this project from scratch. For that we need some requirements.

The numer of requirements will increase over time. In the beginning we start quite simple. So our first set of requirements for our project are as followed:

## Requirements

### Book Meta Data
Our system must accept meta data about books. This meta data will be transmitted over network. The format of the meta data is `json`. 

The `json` format looks as followed:

```json
```
This json book meta data can be validated in the RCP using a json schema file.

### Data storage
The book meta data needs to be persistently stored by the RCP.

### Data requests
Clients must be able to query the book inventory over the RCP. In the first RCP version the client needs to be able to query a book by author and book title over network. 

[Back (Preparation)](./preparation.md)|[Next (Implementation I)](./impl_1.md)
