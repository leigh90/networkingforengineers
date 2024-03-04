4. TRANSPORT LAYER

The transport layer takes messages to and from the relevant application on the end-system. It is found on end-systems. 

### Responsibilities of the transport layer 
1. **Logical application-to-application delivery** - Allows applications to to address other applications on other end-systems directly. 

2. **Data segmentation** - The transport layer also divides the data into manageable pieces called segments or datagrams 

3. **Can allow multiple conversations**  - tracks each application to app connection or conversation separately thus allow multiple conversations to occur at once. 

4. **Multiplexes & de-multiplexes data**  ensuring that the data reaches the relevant application within an end-system. so that multiple packets end up in the correct application


#### Transport Layer Protocols 
Uses two protocols: 
- Transmission Control Protocol(TCP) 
- User datagram protocol (UDP)

#### TCP 
- Delivers messages/segments in order 
- Detects modifications to packets and corrects them 
- Handles the data volume by only sending the appropriate amount of data. 
- Used by apps like HTTP, E-mail, File transfers 

#### UDP 
- Does not ensure in-order delivery of messages/datagrams 
- Detects modifications to packets but cannot fix them.
- Does not ensure reliable delivery 
- Faster than TCP since it doesn't check for corruption of packets.
- Used by apps like DNS, live-streaming and Voice over IP


#### Multiplexing 

Allows for sending messages to be sent to more than one destination host via a single medium. 

Lets say you have multiple packages from one house destined for various destinations 
#### De-multiplexing

The process of delivering the correct packets to the correct application from once stream (figuring out which house to delver the mail to at the post office)

The transport layer labels packets with the port number of the application a message is from and the one it is addressed to. 
 
#### Multiplexing & De-multiplexing in UDP
#### Ports

When a datagram is sent out from an app, the port no of the associated source and destination app is appended to it in the UDP protocol header. 

When the datagram is received at the receiving host it sends the datagram off to the relevant app's socket based on the port number. 

If the source port and source IP address of the two datagrams are different but the destination port and IP address are the same, the datagram will still get sent to the same application. 

![[Screenshot from 2024-02-02 17-11-07.png]]


#### Congestion control 

This happens when there are more packets than the network has bandwidth for and  some of them start getting dropped and others get delayed. 

Physically congestion happens in the network layer but it's mainly caused by the transport layer sending too much at once. So this is the best place to handle it. 

Congestion control is mostly congestion avoidance. By: 
 - Slow down the rate at which packets come in.
 - Keep track in the traffic also kept track of. 

#### Bandwidth Allocation Principles

Bandwidth location is better done per connection as opposed to per host. 

This is because not all hosts are created equal some need more bandwidth than others. 

Additionally traffic tends to happen in bursts as opposed to in a continuous stream.  
Transmission threshold - the number of packets drastically drops past a certain threshold of the transmission rate despite the fact that the threshold is less than the capacity. Transmission rate increases exponentially when the packet transmission rate increases beyond a certain threshold and since the delay will never be infinite the packets eventually will just be dropped. 






### The User Datagram Protocol


Is a transport layer protocol that works over the Internet protocol. 

##### How it works
It doesn't involve initial handshaking like TCP hence its called a connectionless protocol. This means that there are no established 'connections' between hosts.




UDP  adds information about the source port(where the message is coming from) and destination port (where the message is going) to the beginning of the data received from an application. This info is used to correctly direct messages through the network. Once this header is added UDP passes the message to the internet protocol for delivery. 


IP does not guarantee message delivery, order or integrity of messages 

#### UDP Structure 

#### Header 
UDP prepends 4 2-byte header fields to the data from the application layer. 

The included fields are:
	1. *Source*  port number
	2. *Destination*  port number
	3. *Length* of the datagram(header and data in bytes)
	4. *Checksum*  to detect if errors have been introduced into the message.

#### Data

The body of a datagram can be 65528 bytes. thats about 2 to the power of 16 2^16


![[Screenshot from 2024-02-19 09-25-16.png]]



#### UDP Checksum Calculation & UDP

Why UDP

1. UDP is fast
2. YOu can build reliability on top of UDP. TCP ensures that every message is sent by handling the re-sending it if necessary. However you can do this with the app instead. 
3. UDP gives finer control over what message is sent and when it's sent. this allows developers to decide which messages are important and which aren't and dont need concrete reliability. 
4. UDP allows custom protocols to be built on top of it. e.g google's transport layer protocol (Quick UDP Internet Connections) is an experimental transport layer network protocol is built on top of UDP and is designed by google with  the goal of reducing latency to and from chrome web browsers
5. A smaller header makes UDP faster in terms of reduced transmission overhead and quicker transmission times 

UDP is also used by DNS which makes web browsing significantly faster. 
UDP is also used for network management and networking is done using a protocol called the Simple Network Management Protocol


#### Capturing UDP Packets 
tcpdump 


```
tcpdump -w filename.txt 
tcpdump -w output.pcap
```

Count packets with -c
This flag makes tcpdump captured a defined number of packets. 
`tcpdump -w output.pcap -c 10`

Printing PCAP files with -r 

	 tcpdump -w output.pcap


Capture UDP Packet headers
Capturing one UDP packet - sample output
`tcpdump udp -X -c 1  

```
[sudo] password for leigh: 
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on veth83715ad, link-type EN10MB (Ethernet), capture size 262144 bytes
10:14:44.280892 IP leigh-ThinkPad-X13-Gen-2i.56315 > 239.255.255.250.1900: UDP, length 173
	0x0000:  4500 00c9 ff06 4000 0111 de0f ac12 0001  E.....@.........
	0x0010:  efff fffa dbfb 076c 00b5 9cd4 4d2d 5345  .......l....M-SE
	0x0020:  4152 4348 202a 2048 5454 502f 312e 310d  ARCH.*.HTTP/1.1.
	0x0030:  0a48 4f53 543a 2032 3339 2e32 3535 2e32  .HOST:.239.255.2
	0x0040:  3535 2e32 3530 3a31 3930 300d 0a4d 414e  55.250:1900..MAN
	0x0050:  3a20 2273 7364 703a 6469 7363 6f76 6572  :."ssdp:discover
	0x0060:  220d 0a4d 583a 2031 0d0a 5354 3a20 7572  "..MX:.1..ST:.ur
	0x0070:  6e3a 6469 616c 2d6d 756c 7469 7363 7265  n:dial-multiscre
	0x0080:  656e 2d6f 7267 3a73 6572 7669 6365 3a64  en-org:service:d
	0x0090:  6961 6c3a 310d 0a55 5345 522d 4147 454e  ial:1..USER-AGEN
	0x00a0:  543a 2047 6f6f 676c 6520 4368 726f 6d65  T:.Google.Chrome
	0x00b0:  2f31 3230 2e30 2e36 3039 392e 3139 3920  /120.0.6099.199.
	0x00c0:  4c69 6e75 780d 0a0d 0a                   Linux....
1 packet captured
1 packet received by filter
0 packets dropped by kernel

```


### Transmission Control Protocol

WHAT TCP DOES

1. Send data an an appropriate transmission rate - that should be fast enough to make full use of the available capacity but not fast enough to cause congestion.

2. Segment data - Data from the application layer is in a unsegmented stream of data so that there's no limit to how much data the application layer can give to the transport layer at once. the transport layer breaks it up into segments 

3. Flow control - Avoid overwhelming the receiver. The idea is to send data in a way the receiver can actually handle. 

4. Identify and retransmit messages - that don't get delivered.

5. Identify when messages are received out of order and reassemble them. 

WELL KNOWN APPS THAT USE TCP

File Transfer - FTP is built on TCP. It uses port 20 and 21. It uses TCP because of the you need reliable delivery and in the correct order of files. 

SSH Secure Shell - Allows a secure connection to a remote host over an unsecured network to execute operating system shell commands on remote servers that's why the application uses TCP because of the reliability. 

Email - All email protocols SMTP, IMAP, POP use TCP to ensure complete and reliable message delivery. 

Web Browsing 

#### Key Features of TCP

1. Connection-oriented - TCP creates a long term connection between hosts until a certain termination procedure is followed. 
2. Full duplex - both hosts on a TCP connection can send messages to each other simultaneously.
3. Point-to-point transmission - TCP connections have exactly 2 endpoints so you cant broadcast or multicast. 
4. Error control - can detect errors in segments and correct them. 
5. Flow control - TCP on the sending side controls the amount of data being sent at once based on the receiver's specified capacity to accept and process it. 
6. Congestion control - control congestion

#### TCP Segment Header
TCP Headers are crucial and are actually responsible for making it work. You can have TCP message that only has the header and that's absolutely valid. 

![[Screenshot from 2024-02-27 06-36-58.png]]

1. Source port (2-bytes) - port of the socket sending the segment. 
2. Destination port (2-bytes) - port of the socket of the receiving application.
3. Sequence number (4-bytes)  -Each byte of a TCP segment is labelled with a sequence number. This is the sequence number of the first byte of the data in the segment.  The initial sequence number is a randomly generated number between 00 and 232−1232−1.
4. Acknowledgement number (4-bytes) - Represents the sequence number of the next expected segment that the sender will send or the receiver will receive. Say the SN is 42849 and the data is 59bytes so the nest SN or the acknowledgement number would be 42908. This helps TCP Identify if a segment was missing or out of order. 
5. Header length (4bits) - Length of the TCP header is specified here this helps the receiving end to identify where the header ends and the data starts from. 
6. Reserved Field (4-bits) - Always set to 0. This field aligns the total header size to be in multiples of 4 (which is necessary for the header length to be processed) 
7. 8 Flags(8 bits) -  Are used in the establishment, maintainance, tear-down of  a TCP connection. 
	1. ACK - ==Acknowledge a segment that was received previously.== when a receiver wants to acknowledge some received data, it sends a TCP message with the ACK flag and the acknowledgement number field appropriately set. The flag is also used in connection establishment and termination as we will see in more detail later. 
	2. RST - Reset flag immediately ==terminates a connection,== this is sent when there's a confusion such as if the host doesnt recognize the connection. if the host has crashed or if the host refuses an attempt to open a connection.
	3. SYN - Synchronization flag initiates a connection establishment with a new host.
	4. FIN - Finish terminate or finish a connection with a host. 
	5. CWR & ECN - Congestion Window Reduced, Explicit Congestion Notification: Are used to handle congestion. The ==ECN flag is set by the receiver so that the sender knows that the congestion is occurring.== The ==sender sends the CWR flag in response to this so that the receiver knows that the sender has reduced its congestion window to compensate for congestion== and the sender is sending data at a slower rate. 
	6. PSH - If multiple small TCP segments were received the receiving TCP combines them before handing them to them over to the application layer. When the PSH flag is set ==the receiving end immediately flushes the data from its buffer to the application instead of waiting for the rest of it to arrive.== Typically used for Telnet where every keystroke is a command and is pushed. 
	7. URG - The urgent flag marks some data within a message as urgent. when the receiving host receives an URG flag the receiving host ==forwards the urgent data to the application with an indication that the data is marked as urgent.== This can be used when a large file is being transferred but the sender sends  a command to stop transfer so the command is sent to stop the file transfer.
8. Window Size (2-bytes) - Sent by the receiver to the sender in every TCP message and gets updated as the buffer fills and empties. ==If the window size reduces after a bit== the sender will know that it needs to reduce the amount of data being sent or give the receiver time to clear the buffer. Window size starts as the same size as the receiver sets it and as the receiver gets more data the window size decreases until it hands over the data to the application layer.
9. Checksum - calculated exactly like in UDP except it's mandatory in TCP. 
10. Urgent pointer - defines defines the byte to the of which the urgent data exists. This is coz a single segment can contain both parts of urgent and regular data. Only used when the URG flag is present.
11. Options and padding - provides upto an extra 40bytes to build extra activities that aren't covered by a regular header

![[Screenshot from 2024-02-29 03-08-58 1.png]]


![[Screenshot from 2024-02-29 03-12-05.png]]


### TCP CONNECTION ESTABLISHMENT

#### A. 3-Way handshake

1. The client sends a TCP segment with the SYN flag set and a random sequence number
	![[Screenshot from 2024-02-29 03-43-01.png]]
1. The server receives the segment and sets the ACK flag and the acknowledgement number is incremented by 1 mod ^23  because the SYN segment consumes 1 byte. This is done to indicate it has received all the segments including  the segments with the sequence number
![[Screenshot from 2024-02-29 03-43-18.png]]

1. When the client receives the SYN+ACK segment it replies with a segment with the ACK flag set and the scknowledgement number set to the sequence number of the received _SYN+ACK_ segment incremented by 1.
![[Screenshot from 2024-02-29 03-45-56.png]]


3. At this point the connection is open and the client and server can send TCP segments containing data. 

![[Screenshot from 2024-02-29 03-46-08.png]]


### Other TCP Connection Establishment methods

FSM - Finite State Machine

![[Screenshot from 2024-02-29 03-49-48.png]]

Client Side
1. Client starts init state
2. Sends a SYN segment and the enter SYN Sent state as it waits for the SYN+ACK segment
3. When the SYN+ACK segment is received in SYN Sent state, it replies with an ACK segment and enters the Established state where data can be exchanged. 

Server side
1. On the other hand, a server host starts in the **Init state**.
2. When a server process starts to listen to a destination port, the underlying TCP entity creates a TCP control block and a queue to process incoming _SYN_ segments. Upon reception of a _SYN_ segment, the server’s TCP entity replies with a _SYN+ACK_ and enters the **SYN RCVD** state.
3. It remains in this state until it receives an _ACK_ segment that acknowledges its _SYN+ACK_ segment, and with this it then enters the **Established** state.


Simultaneous Connection Establishment

when both the client and the server send a _SYN_ segment to open a TCP connection.

![[Screenshot from 2024-02-29 03-56-56.png]]

![[Screenshot from 2024-02-29 03-56-56 1.png]]


### When connection Establishment Fails: Syn Floods and Re-transmission


Hosts can refuse to open a TCP connection upon receipt of a SYN segment. For any no. of reasons.

- There may be no server process listening on the destination port of the SYN segment
- The server can always refuse connection establishments from a particular client
- The server may not have enough resources to accept a new TCP connection at that time.

Typically what will happen is that the server will respond with a RST flag set and a sequence number of the received SYN segment as its acknowledgement number.

##### SYN Flood Attacks

Essentially malicious actors would create a bunch of half open connections by opening a connection by sending  a SYN segment, receive and acknowledgement from the server which has created a TCB for the connection but never responding to it so the 3 way handshake isnt completed. When these half open connections reach the limit and fill the buffer the server is unable to accept any requests leading to a DOS (Denial of Service) attack. These segments would typically be sent with spoofed IP addresses to avoid being caught. 

TCB - Transmission Control Block - created when a TCP connection to contain the entire state of the connection including the local sequence number sent by the remote client. 
It includes 
- the local IP address
- the remote IP address
- the local TCP port number
- the remote TCP port number
- the current state of the TCP FSM
- the maximum segment size (MSS)

The way to solve this is to avoid opening a connection until the handshake is complete. 
**SYN Cookie** were introduced to solve this problem -it  use a function that uses some information from the client’s _SYN_ packet and some information from the server side to calculate a random initial sequence number. This number, say, y−1 is sent to the client in a _SYN + ACK_ message. If an _ACK_ packet is later received with a sequence number �y, using some packet header fields and some server side information, a reverse function can verify that the acknowledgement number is valid. If not, the connection is refused, otherwise a TCB is created and a connection is established.

Current TCP implementations start a re-transmission timer when the first SYN segment is sent. This timer is often set to 3 seconds for the first re-transmission. This timer is often set to three seconds for the first re-transmission, and then doubles after each re-transmission When the timer expires, the segment is re-transmitted. TCP implementations also enforce a maximum number of re-transmissions for the initial _SYN_ segment. Note that the same technique is used for all TCP segments, not just connection establishment segments.


### TCP Connection Release

There's 2 types

Graceful - connection isn't closed until both sides close the connection on their end
Abrupt - where either one user closes both directions of data transfer or one TCP entity is forced to close the connection. 

##### Abrupt connection release

An abrupt release is executed for a non-existing TCP connection
- A non SYN segment is received for a non-existing TCP connection
- Some implementations send and RST segment with an invalid-header is received on an open connection
- Some implementations send an RST segment to close an existing TCP connection where there aren't enough resources to support the connection or the remote host has stopped responding and is now un-reacheable. 

When a _RST_ segment is sent by a TCP entity, it should contain the current value of the sequence number for the connection (or 00 if it does not belong to any existing connection), and the acknowledgment number should be set to the next expected in-sequence sequence number on this connection.

#### Graceful connection release

Use the fin flag of the TCP header which allows the host to release its side of the connection individually. Utilization of the FIN flag in the TCP header consumes one sequence number. 


### Efficient Data Transmission with TCP


Nagle's algorithm 

![[Screenshot from 2024-02-29 05-26-27.png]]


Window Scaling 

Allowing the window size to be scaled up by including a factor that it can be scaled up to as needed

#### Measuring RTT with Ping


```
ping google.com
PING google.com (172.217.170.206) 56(84) bytes of data.
64 bytes from mba01s10-in-f14.1e100.net (172.217.170.206): icmp_seq=1 ttl=117 time=11.3 ms
64 bytes from mba01s10-in-f14.1e100.net (172.217.170.206): icmp_seq=2 ttl=117 time=11.4 ms
64 bytes from mba01s10-in-f14.1e100.net (172.217.170.206): icmp_seq=3 ttl=117 time=21.4 ms
64 bytes from mba01s10-in-f14.1e100.net (172.217.170.206): icmp_seq=4 ttl=117 time=16.3 ms

ping educative.io
PING educative.io (104.18.2.119) 56(84) bytes of data.
64 bytes from 104.18.2.119 (104.18.2.119): icmp_seq=1 ttl=54 time=203 ms
64 bytes from 104.18.2.119 (104.18.2.119): icmp_seq=2 ttl=54 time=236 ms
64 bytes from 104.18.2.119 (104.18.2.119): icmp_seq=3 ttl=54 time=248 ms
64 bytes from 104.18.2.119 (104.18.2.119): icmp_seq=4 ttl=54 time=272 ms
64 bytes from 104.18.2.119 (104.18.2.119): icmp_seq=5 ttl=54 time=193 ms
64 bytes from 104.18.2.119 (104.18.2.119): icmp_seq=6 ttl=54 time=214 ms


```

`64 bytes`  - Size of the packet
`104.18.2.119` - IP address of the domain we looked up
`icmp_seq=1ttl=54` - sequence number and TTL of the packet
`time=214 ms` - Round trip time


ttl - time to live in this case it can  jump 54 more hops before being discarded

each router or intermediary forwarding device decreases the TTL by 1.

TCP congestion control algorithm

