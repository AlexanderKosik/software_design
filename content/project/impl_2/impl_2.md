[Back (Implementation I)](../impl_1/impl_1.md) | [Next (Implementation III)](../impl_3/impl_3.md)

# Implementation part II
In this chapter the received JSON files will be persistently stored. If the number of objects to be saved is small, saving to a file (without a database) might be sufficient. But in our case we expect the number books (respectively JSON files) to be high enough to justify using a database. 

## Status Quo:
At this point the RCP should be able to receive JSON files over network and have an internal representation for the JSON content. 

## Storing to a database
The decision to store the JSON files to a database was made. The next steps are: 

1) Start searching for a file-based database for your programming language. Check what the requirements are to use the database. An example for a commonly used file based database is `sqlite`.

2) If you are using a relational database, create a draft for the database schema without coding.
   You need to consider:

    - The tables you need and the relations between the tables
    - Primary keys of the database
    - Field types of the database

3) Implement the database connection and storage of JSON files to the database.

# Multiple ways of database implementation

There are multiple ways of implementing the database connection in your project. 

## The manual way

The manual way uses raw SQL queries. These queries must be packed into a suitable object structure. For example, one object for each query or one object for each table. The dataset is manipulated via an `insert`, `update` and `delete` query. 

The manual approach means less overhead, no dependencies to existing libraries have to be added. However, depending on the situation, the approach can be more extensive and is more likely to introduce errors in the implementation.

## Object Relational Mapping (ORM)
Object Relational Mapping presents a method of associating classes with database tables. Database tables are implicitly described by the objects that need to be stored. Every row in a table is associated to an object, where as every attribute of the object is a column in the table. 

ORM simplifies object oriented programming with a database in the background. Common frameworks are `Hibernate` for `Java` and `SQLAlchemy` for `python`. 

## NoSQL

Another approach is to implement the requirements with a `NoSQL database`. A commonly used NoSQL database is `MongoDB`. NoSQL databases are predestined to work with data like JSON files. 

If you have never heard about NoSQL databases, have a look at this description of advantages of NoSQL databases like MongoDB: [link (mongodb.com)](https://www.mongodb.com/advantages-of-mongodb)

If you take this approach, you can set up a free MongoDB in the cloud (AWS, Microsoft Azure, Google Cloud) via the [MongoDB Atlas](https://www.mongodb.com/atlas/database). You can create a free test instance with your google account. 

# Questions for reflection
1) What are the right abstractions to use to implement the database connection? Consider the ETC principle. Can you swap out the database implementation easily?

2) Where did the creation of the database occure? In source code, by script, manually?

3) Where are your connection properties stored? Are they hard coded or configurable with a configuration file?

4) How can you test your implementation? 

# Further readings

- [The database is a detail](../../material/database_detail.md)

[Back (Implementation I)](../impl_1/impl_1.md) | [Next (Implementation III)](../impl_3/impl_3.md)
