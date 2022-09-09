[Back](../project/rcp.md) 

# JSON

JSON stands for `JavaScript Object Notation`. In JavaScript objects are simple containers with key-value pairs. The key is a simple string, whereas the value can be a string, a number, a function or another object. 

The advantages of JSON are, that it is easier to read for humans (compared to e.g. `XML`), being less verbose while being identical easy to parse by a machine. 

A simple JSON file looks like this:

```json
{
    "id": 42
    "name": { "first": "Alexander", "last": "Kosik"}
    "programming_languages": [
        { "language": "C++" },
        { "language": "Python" },
        { "language": "Java" }    
    ]
}
```

JSON is nowadays a standard format for exchanging data over networks, like the web. But in the mean time JSON files are used in many use cases like:

- Application configuration files
- Logging
- APIs

Every modern programming language has support for JSON files. 

[Back](../project/rcp.md) 
