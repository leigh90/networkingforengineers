### A. Definitions 
- A network is a group or a system of interconnected people or items. E.g a road network, a rail network, a people network etc
- Networks allow us to ==**communicate**== and ==**share resources**==
- The internet is essentially a network of computer networks 

### B. Access Networks 

#### 1. Edge of the internet: End systems 

Each network is made of devices called end systems connected to each other with communication links. 
End systems are essentially ==the devices that are connected to the internet==. For example phones, laptops, servers, IOT devices etc 
They are called edge systems because they are at the edge of the internet since they dont relay data from one device to another like routers would. 

#### 2. The network edge

The collection of end-systems that we use daily
Devices that relay messages like routers are not part of the edge of the internet. 

#### 3. Access Networks

The media through which end systems physically connect. 
They physically connect end systems to the first router( also called an edge router).
The type of access network depends on the physical media involved. 
Common access networks include WIFI, Satellite, DIal-up, FibreToTheHome(FTTH), Cable internet, Digital Subscriber Line(DSL).

End systems have a piece of hardware called a ==network interface adapter ==(basically a network card) (NIA)that enables the computer to attach to a network. They are the ==physical gateways that connect devices== to the internet. 

Since there's different types of networks the adapter is used so the user can install one to suit the network they want to attach to.
NIAs have an address associated with them, on machine can have multiple interfaces. Most machines have external ports which network cables can be plugged into. The type of access network depends on the physical media involved. 

#### 4. Network Speed 
The rate at which data is transmitted from one point to another in a network is called the transmission rate. 

Transmission rates are measured in units of bits/sec and multiples of bits like mb, gb, kb
Data flows though end systems in 2 ways 
To an end system  - download rate 
From an end system - upload rate 
Some networks have varying upload and download transmission rates called asymmetric transmission rates, this is useful because traffic going out from end hosts consists of smaller requests which solicit comparatively much larger responses. 


### C. Types of Access Networks

DSL - Digital Subscriber Line uses the existing groundwork of telephone lines for an internet connection. 

An ISP is the company that provides end users with an internet connection. e.h zuku, safaricom 

DSL modem modulates the digital signals that a computer outputs into high-frequency analog audio signals that are out of the human voice and hearing range.

The telephone wire's frequency spectrum is divided into 3 parts 
	- A downstream channel(receives data) : in the 50KHz - 1MHz
	- An upstream channel (sends data) uses the 4kHz to 50kHz
	- Regular channel used for telephone conversations using the 0 - 4kHz range

These signals are then carried by telephone  wires over to the ISP. Then these high frequency analog signals are converted back to digital signals using a device at the ISPs end called a DSLAM. Then the signal are then forwarded to the end system that it was  meant to reach


### D. TYPES OF COMPUTER NETWORKS BY: PHYSICAL MEDIA

Data needs to be transmitted over a certain medium from one end system to another. 
There are two kinds of media. 
- Guided - when signals are transported on a confined pathway
- Unguided - when signals aren't confined to a specific pathway like radio waves

Guided Media 
- Twisted copper wire 
- Coaxial cable 
- Fiber optics - Carry light instead of electrical signals. 
	- This is actually really nice since unlike metal which is susceptible to electrical noise and interference which light isn't affected by
	- Additionally fiber optic cables avoid interference from other light sources by having an opaque covering around the optic fiber cable 
	- These cables have very fast transmission rates and can be stretched over long distances like over 1km 
	- There are 2 main types of optical fibers 
		- Multimode - used LED to send signals, cheaper than multimode, works over tens of KMs, multiple light signals. Multiple light signals travels throuh the same optic fiber while reflecting off the edges of the fiber at different angles
		- Monomode - uses laser for transmissions, more expensive than multimode, can only work over a few kilometers. 
	
Unguided Media

- Radio waves encompass a certain band of the electromagenetic spectrum. 
- There are 3 kinds of terrestrial radio channels: 
	- Bluetooth - operate over short distances  
	- WiFi - operate over hundreds of meters
	- 3G,4G, LTE, 5G - Operate over a range of kilometers 
	- 


### E. TYPES OF COMPUTER NETWORKS BY: GEOGRAPHICAL DISTANCE

LAN
Ethernet 
WiFi 
MAN - 
WAN

### F. TYPES OF COMPUTER NETWORKS BY: TOPOLOGY

Bus - all the computers are computers are connected to a main line 
Ring - end systems communicate with each other through each other in a unidirectional way 
Star - All end systems talk to each other through one central device such as a router or switch. 
Tree - Essentially a bunch of stars connected by a large bus
Mesh  - Every end system is directly connected to every other end system 
