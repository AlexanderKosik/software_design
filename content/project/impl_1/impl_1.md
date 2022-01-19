[Back (preparation)](./preparation.md) | [Next (Implementation II)](./impl_2.md)

# Implementation pt. 1
At this point you should have an empty project in your prefered programming language. There is a separate repository for the project and every group member should have access to it. If not, follow along the [preparation steps](./preparation.md).

## Network connection
The RCP systems needs to process json files via network. Start your implementation by creating a TCP socket.

To test your implementation you can use the program `rcp_send.py` in the directory `content/project/impl_1`. With this application you can send json files to your RCP. To run the application you need a python installation. If you have no python interpreter installed, you can get some [here (python.org)](www.python.org).

The script can be used as followed:

# Help

If you have never heard about the json format, you can read about it TBD

# Questions for reflection
1) Where is the interface and port of your network socket configured? Is it hard coded in source code or changable via a configuration file?

2) What is the difference between TCP and UDP? Why is TCP the appropriate transmission protocol for this use case?

2) Do you have any tests for your system? How can your system be tested? How does the network retrieval of data over network affect your ability to test your system?
