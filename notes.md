# Network Simulator

The network is made of Node objects.

Nodes are identified by a unique identifier.

Each node can have multiple network interfaces.

Each interface has its own set of addresses.

Each node is connected to other nodes via Link objects.

Each link is a triple associating 2 ports/addresses with a communication channel.

The channel can represents the physical link between 2 nodes. 

The physical link is modelled with the propagation delay (queue) and the bit error rate/packet error rate.

The set of nodes connected by links is a network graph.

Each node keeps its time/clock.

Each node has a protocol stack.

Each layer of the stack implements a set of services.

Each service implements a protocol.

Each service communicate to other services with ports. 

Service ports are numbered. 
