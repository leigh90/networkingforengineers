# 2. Network Infrastructure - The OSI Model
### A.  Open Systems Interconnection Model
#### Application Layer 
1. Almost always implemented in software
2. End users interact with the application layer 
3. The application layer is where most end-user applications such as web browsing and email live 
#### Presentation Layer 
1. Presents data in a way it can be easily understood by the application layer. 
	- This is done by encoding the data from the underneath layers
	- Encryption - presentation layer encrypts the data
	- Abstraction - assumes the user session is being handled by lower layers so it transforms the content to suit the application
	- End-to-end compression - The presentation layer might also implement end to end compression. 
#### Session Layer 
Builds on the transport layer services and builds a service on top of it that manages user sessions. 
	- Transports the session layer messages across the network to the destination. The session layer must manage the mapping of messages delivered by the transport layer to the sessions
	- Abstraction: assumes that connections establishment and packet transportation is handled by the layers below it. 

#### Transport Layer 
- Responsible for segmenting the data into smaller chunks. These chunks are called datagrams or segments depending on the protocol. 
- This layer also adds additional information that allows the datagram to be transmitted reliably. For example the checksum that ensures that the message was not corrupted in transit. This info is placed int the header. 

#### Network Layer

Network layer messages are called packets
The network layer facilitates movement of packets from one end system to another and determine the best route for the packet to take. 

Routing protocols are applications that run on the network layer and exchange messages with each other to develop info that helps them route transport layer messages. It uses routing algorithms to determine the most efficient path for each packet to take, considering factors like network congestion, topology and routing policies. (*Routing is the process of selecting what path in a network to send traffic along, it's typically done by routers that use routing protocols to learn about the network and make routing decisions*)

Load balancing - there are many links (copper wire, optical fiber, wireless ) in a given network and its the job of the network layer to keep them equally utilized otherwise an imbalance is expensive.

#### Data Link Layer 
Ensures that the two hosts connected on a shared physical medium are able to exchange data in an efficient and accurate way to minimize data loss or corruption.

The data link layer enables devices connected to each other on a share physical medium to communicate. 

This is done by 
1) flow control - managing the pace of data exchange. This ensures that a sender doesn't overwhelm a receiver with data transfer faster than it can be processed. This is key especially when the capacities of the receiver and sender differ. 
2)  error detection/correction - identifying and fixing errors in the transmitted data. It uses things like checksum, cyclic redundancy and hamming to detect errors. For correction it may use protocols like ARQ (automatic repeat request) to transmit data that was received with errors. 
So what does the data link layer do?

- Ensures packets are prepared with the necessary formatting and control info to be transmitted over a direct connection - this essentially means wrapping the data from the network layer into frames adding headers and trailers that include control info to manage the transmission
- Resolves transmission conflicts e.g when 2 end systems send a message at the same time across a singular link
- Handles addressing ensuring that the data frames are sent to the correct device on the network. In a broadcast  medium where multiple devices share a communication channel it ensures that the right message is delivered to the right device by using addresses. 
- Multiplexing - it's the process of combining multiple signals or data streams into one, sharing a common channel to increase the efficiency of a resource by carrying multiple transmissions simultaneously. So you combine several physical or logical connections to achieve a higher bandwidth link to make it more efficient as it's shared across multiple connections. 
- De-multiplexing - Take one physical data link, split it logically into multiple virtual links so each virtual link behaves like its a separate physical link so you can send data simultaneously and independently so you can manage and secure it separately. 

#### Physical layer 

Consists largely of hardware. 
Provides a solid electrical and mechanical medium to transmit data 
Transmits bits, not logical packets, datagrams or segments.
Also deals with the mechanical specifications for the cables and connectors. 

### Transmission Control Protocol /Internet Protocol

TCP.IP model differes from the OSI model in 2 key ways.

1. TCP/IP is used practically while the OSI model is a theoretical model.
2. TCP/IP has 5 layers while OSI has 7 

In TCP/IP  the application layer is made up of the 3 layers of the OSI model ie, the application, presentation and session layer. 

Otherwise the rest of the layers function in the same way.



  
 
 
