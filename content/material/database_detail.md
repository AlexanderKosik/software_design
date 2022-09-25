# The database is a detail

If you have chosen the right abstraction, the actual database to use can be a detail. This means, you can swap the actual database to use easily (this does not affect the dataset!). Where needs the abstraction to be in this case? Think about the Open-Close-Principle (OCP).

If not already familiar, familiarize yourself with the "Factory Pattern" and also with the "Abstract Factory Design Pattern". If you use the Factory Design Pattern for creating the database connection, using another database might just be a change in a configuration file. The complexity of the implemenation is in that case "pulled down", this means only in the actual implementation of the class. Pulling complexity down is a common way of simplifying a design. 

- [Back](../../content/project/impl_2/impl_2.md)
