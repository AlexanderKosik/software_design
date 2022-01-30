[Back (Implementation I)](../impl_1/impl_1.md) | [Next (Implementation III)](../impl_3/impl_3.md)

# Implementation part II
In this chapter the received json files will be stored in a database. 

## Status Quo:
At this point the RCP should be able to receive json files over network and have an internal representation for the json content. 

## Storing to a database
The received json files must now be stored to a database. 

1) Start searching for a file-based database for your programming language. Check what the requirements are to use the database. An example for a commonly used file based database is `sqlite`.

2) If you are using a relational database, create a draft for the database schema without coding.
   You need to consider:

    - The tables you need and the relations between the tables
    - Primary keys of the database
    - Field types of the database

3) Implement the database connection and storage of json files to the database.

# Multiple ways of database implementation

There are multiple ways of implementing the database connection in your project. 

## The manual way

TBD

## Object Relational Mapping (ORM)
Object Relational Mapping presents a method of associating classes with database tables. Database tables are implicitly described by the objects that need to be stored. Every row in a table is associated to an object, where as every attribute of the object is a column in the table. 

ORM simplifies object oriented programming with a database in the background. Common frameworks are `Hibernate` for `Java` and `SQLAlchemy` for `python`. 

## NoSQL

Another approach is to implement the requirements with a `NoSQL database`. A commonly used NoSQL database is `MongoDB`. NoSQL databases are predestined to work with data like JSON files. 

If you have never heared about NoSQL databases, have a look at this description of advantages of NoSQL databases like MongoDB: [link (mongodb.com)](https://www.mongodb.com/advantages-of-mongodb)

If you take this approach, you can set up a free MongoDB in the cloud (AWS, Microsoft Azure, Google Cloud) via the [MongoDB Atlas](https://www.mongodb.com/atlas/database). You can create a free test instance with your google account. 

# Questions for reflection
1) What are the right abstractions to use? Consider the ETC principle. Can you swap out the database implementation easily?

2) Where did the creation of the database occure? In source code, by script, manually, ...?

3) Where are your connection properties stored? Are they hard coded?

4) How can you test your implementation? 

# Further readings

- [The database is a detail](../../material/database_detail.md)

[Back (Implementation I)](../impl_1/impl_1.md) | [Next (Implementation III)](../impl_3/impl_3.md)