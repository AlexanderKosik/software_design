[Back (Implementation I)](../impl_1/impl_1.md) | [Next (Implementation III)](../impl_3/impl_3.md)

# Implementation part II
In this chapter the received json files will be stored in a database. 

## Status Quo:
At this point the RCP should be able to receive json files over network and have an internal representation for the json content. 

## Storing to a database
The received json files must now be stored to a database. 

1) Start by searching for a simple file-based database for your programming language. An example would be `sqlite`. 

2) If you are using a relation database, create a draft for the database schema without coding.
   You need to consider:

    - The tables you need and the relations between the tables
    - Primary keys of the database
    - Field types of the database

3) Implement the database connection and storage of json files to the database.


# Questions for reflection
1) What are the right abstractions to use? Consider the ETC principle. Can you swap out the database implementation easily?

2) Where are your connection properties stored? Are they hard coded?

3) Can you test your implementation effortless? 

# Further readings

- [The database is a detail](../../material/database_detail.md)

[Back (Implementation I)](../impl_1/impl_1.md) | [Next (Implementation III)](../impl_3/impl_3.md)