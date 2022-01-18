# Implementation pt. 1
At this point you should have an empty project in your prefered programming language. There is a separate repository for the project and every group member should have access to it. If not, follow along the [preparation steps](./preparation.md).

## Network connection
The RCP systems needs to process json files via network. Start your implementation by creating a TCP socket. o

To test your implementation you can use the program `rcp_send.py`. 

# Questions for reflection
1) Where is the interface and port of your network socket configured? Is it hard coded in source code or changable via a configuration file?

2) Do you have any tests for your system? How can your system be tested? How does the network retrieval of data over network affect your ability to test your system?
