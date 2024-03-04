The main job of the application layer is to facilitate access to the internet through a number of applications. Provide the interface and protocols necessary for users to interact with the network through application. It translates user actions into network operations and presents the data from the network in a way that users can understand and use.

1. Format the data to conform to the standards of a specific network protocol before sending it over the network. This ensures that the data can be correctly interpreted and used by the receiving system. 
2. Receiving input from the user e.g text commands and processing them according to the user request.
3. Development of software that serves users 
4. Error handling

The application layer is the taking the package to the post office part of sending a letter. 
The application layer lives entirely on end-systems e.g phones, laptops, fridges


#### Network Application Architectures

1. Client-server architecture - Client processes use the Internet to consume content and use the services. Client processes almost always initiate connections to servers, while server processes wait for requests from clients.
2. Data center - Data centers are buildings that house servers.
3. Peer to peer -  applications on end-systems called ‘peers’ communicate with each other. No dedicated server or large data center is involved. Peers mostly reside on PCs like laptops and desktops in homes,
4. Hybrid 

#### Quantitative comparison of P2P with client-server

Server upload speed in bits per second
No of clients - N 
Size of the file - S 
Upload rate of server - up
Number of bits to be uploaded is = NS 
Speed to upload NS to all clients = NS/up

client with slowest download rate (dwn = min(dwn.i)) will take atleast S/dwn.min



$$
max{NS/UPs, S/dwnmin}
$$


### How Processes communicate

**Program** - an executable file. An application such as MS Word is one example

**Process** - Any currently running instance of a program. It contains the program code and the current activity A program can have several copies running at once. say multiple windows of chrome or MS Word. Each window represents a separate process. 
In computing a process represents a single sequence of execution in a computing environment. with it's own memory space and system resources. Each process is kept isolated from other processes so they don't interfere with one another. When a program is started the OS creates a new process for it. 

The OS will schedule their execution, allocates resources such as CPU time, memory and I/O and handles their lifecycles from creation to termination. Processes can communicate with each other through mechanisms like pipes, sockets, shared memory or message passing. 

**Thread** - The smallest unit of processing that can be scheduled by an OS. It's a single sequence of instructions within a process. that can execute independently but shares resources like memory with other threads within the same process. 

a lightweight process - a process can have multiple running threads. A thread does a single job. It's lightweight because it shares the same memory space and resources of its parent process. Threads can run concurrently enabling parallel processing within a single process. For example in MS Word a thread could be spell checking or auto-saving or updating the display without needing to start a separate process for each task. 


![[Screenshot from 2024-01-28 22-59-29 1.png]]

#### SOCKETS

A socket is a software endpoint that allows processes to send and receive data through the network using protocols like TCP or UDP. 
It's a gateway for network communication between processes running on different systems. Each socket is associated with a specific protocol, IP address and port number. 

TCP Sockets - Provide a reliable, connection-oriented stream of data between processes. They ensure that data is delivered in order and without being duplicated. 

UDP Sockets - Provide connection-less unreliable service for sending messages(datagrams)
It's faster but it doesn't guarantee delivery or the order of the messages. 

Processes direct their messages to sockets. 

#### Addressing 

Port numbers are used to address packets to a specific applications. Its like an apartment number for apartments that share a single street address( IP address)

Ephemeral ports - Port numbers that are dynamically generated for each instance of an application, and then freed when the app is done. 
Typically server processes have well-defined and fixed port numbers so that clients can connect to them in a systematic and predictable way. Clients don't need to have reserved ports instead they just use ephemeral ports in addition to reserved ones. So a client makes the initial connection to the server on a well-known port and the rest of the communication is carried by connecting to an ephemeral port. 


HTTP (Hyper Text Transfer Protocol)

Web pages are essentially objects that consist of other objects
An object can be a HTML file, PNG file, MP3 file etc
Each object has a URL 
The base object of a web page is often a HTML referencing other objects

Anatomy of a URL 
URL - Uniform resource locator

A url has the following parts 
- Protocol
- Hostname 
- Location of the file
- Arguments

![[Screenshot from 2024-02-02 04-48-40.png]]

HTTP is a stateless protocol meaning no information about the client is stored
so if a client requests a resource multiple times the server wouldn't know that it was the same client.


**HTTP requires lower layer reliability**
Application layer protocols rely on underlying transport layer protocols called UDP(User Datagram Protocol) and TCP (Transmission Control Protocol)
HTTP uses TCP because it always ensures messages are always delivered and in order.
TCP is connection-oriented a connection has to be initiated with servers using a series of starting messages, and ended with ending messages

**Anatomy of HTTP header lines **

1. The host 
2. The type of http connection
3. User-agent - the client 
4. Accept-language - header  specifies  the user's preffered language
5. Accept - defines the sort of response to accept. Could be HTML files, images, audio, video


![[Screenshot from 2024-02-02 14-40-26.png]]

**HTTP responses**

![[Screenshot from 2024-02-02 14-48-30.png]]

The header lines 

1. Connection type - the server will close the TCP connection after it sends the response
2. Date - the date when the response was generated
3. Server - Gives software specs of the server that generated the message. For example apache
4. Last-modified - The date the object being sent was last modified
5. Content-length  - the length of the object being sent in 8-bit bytes
6. Content-Type - The type of content, the type of the file is not determined by the file extension
#### Cookies 
String identifiers stored on the client's browser
These can be set by the server through HTTP headers when the client first navigates to the website. 
After the cookie is set its sent along with other HTTP requests to the same server which allows the server to know who is contacting it and hence serve the content accordingly 

When a server wants to set a cookie it includes the Set-cookie value in its response to the client which is then appended to the cookie file stored on the browser
The file contains the 
- website domain
- string value of the cookie
- date that the cookie expires 

#### SMTP 


#### DNS (Domain Name Server)

A protocol that translates hostnames on the internet to IP addresses. 
DNS is also a distributed database of names that map to IP addresses

#### DNS namespaces

Parts of a url roughly map to DNS servers. These servers manage the abstract space of domains. These server exist in a hierarchy

![[Screenshot from 2024-02-02 15-24-14.png]]


Root DNS servers 

First point of contact for a DNS query after the local cache. so for educatiove.io would return the IP address of a server for the top level domain, io 

Top level servers - server in the top level domain hold mappings to DNS servers for certain domains. e.g .com, org, edu, mil, net, org. 

Local DNS servers - usually the next point of content after the client checks its local cache. These servers are hosted by the ISP. 

`host` is a DNS lookup utility. It is normally used to map hostnames to IP addresses.

The syntax of the command above, for instance, is
```
host -t ns hostname.com
```
- `host` invokes the host command
- `-t` is the `type` flag. It is used to specify the type of the command. Check out [host’s manpage](https://linux.die.net/man/1/host) for a list of all the types available.
- `ns` specifies the type. It stands for the name server in this case.
- `hostname.com` can be any website of your choice.
