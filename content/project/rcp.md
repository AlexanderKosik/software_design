[Back (Preparation)](./preparation.md) | [Next (Implementation I)](./impl_1.md)

# Project RCP: Recommerce Platform

In this project we create a recommerce platform (the *RCP*). A recommerce platform is a software platform that manages used media items such as books.

We start with very few requirements in the beginning. The numer of requirements will increase over time. This increase in requirements simulates demanding customers, when they get in first contact with the commissioned software project.

# Requirements

Our first set of requirements for our project are these:

## 1) Book Meta Data
Our system must accept meta data about books. This meta data will be transmitted over network. The format of the meta data is `json`. 

The `json` format looks as followed:

```json
{
   "title": "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
   "author": "James Clear",
   "isbn-10": "0735211299",
   "quality": "very good",
   "language": "english",
   "publication_date": "2018/010/16",
   "type": "hardcover",
   "purchase_price": 2.90
}
```
You will find further json example files in the directory `./impl_1/json`.

## 2) Data storage
The book meta data needs to be persistently stored by the RCP.

## 3) Data requests
Clients must be able to query the book inventory over the RCP. In the first RCP version the client needs to be able to query a book by author and book title over network. 

# Further readings

If you need more information about json, feel free to have a look at these descriptions:

- [Introduction to JSON](https://javaee.github.io/tutorial/jsonp001.html)
- [Libraries to parse JSON](https://www.json.org/json-en.html)

[Back (Preparation)](./preparation.md) | [Next (Implementation I)](./impl_1/impl_1.md)
