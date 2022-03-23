[Back (Preparation)](./preparation.md) | [Next (Implementation I)](./impl_1/impl_1.md)

# System overview

We now know our three main requirements that we need to implement:

- Processing book information as JSON files over network
- Persistance of information
- Providing an interface to request information about available books

We can assume, that the requirements will not be final and will be extended or changed during the lifetime of our system.

## System context
Let's give an overview over our system and the communication partners/clients of our system.

![](../material/images/system_overview.png)

The overview shows a client using a program `json file transmitter` to send book information to our platform. 

The RCP itself consists of three parts. Each part is responsible for a specific requirement. The components may consist of other part, but this is not specific at the moment. 

## Quality scenario

When we design and implement our system, we can do this regarding specific quality attributes.  [ISO 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010) gives an overview over quality attributes, as seen in the following picture.

![](../material/images/iso25010.png)

# Exercise

1) What are important qualities we need to consider in our system design and implementation?

2) Try to discribe quality scenarios for your identified quality attributes. Examples for 
quality scenarios are the following: 

    1) *"Time behaviour: The platform must be able to import at least 15 books per second over the network interface"*

    2) *"Resource Utilization: The platform must be able to store at least 50.000 books"*

    3) ...

[Back (Preparation)](./preparation.md) | [Next (Implementation I)](./impl_1/impl_1.md)