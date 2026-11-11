# Assignment - 2

> Name : Gaurang Tyagi

> Roll No. : 16

---

# Task 1 : Analyze an ARP Request and Reply

1. Identify the ARP request and record its frame number and timestamp.
```
Frame: 11
Timestamp: 17.522291
Info: Who has 192.168.1.105? Tell 192.168.1.1
```
2. Identify the corresponding ARP reply and record its frame number and timestamp.
```
Frame: 35
Timestamp: 19.068723
Info: 192.168.1.105 is at 08:00:27:5e:01:7c
```
3. What is the sender IP address in the ARP request?
```
192.168.1.1
```

4. What is the target IP address being resolved?
```
192.168.1.105
```
5. What is the sender MAC address in the ARP request?
```
08:00:27:5e:01:7c
```
6. What is the target MAC address specified in the ARP request?
```
Since the sender doesn't yet know the MAC address of 192.168.1.105, the target MAC is:
00:00:00:00:00:00
```
7. What is the opcode of the ARP request?
```
Opcode of the ARP request : 1
Opcode 1 means ARP request.
```
8. What are the Hardware Type and Protocol Type?
```
Hardware Type: 1 — Ethernet
Protocol Type: 0x0800 — IPv4
```
9. In the corresponding ARP reply, what MAC address is associated with the requested IP address?
```
The reply says: 192.168.1.105 is at 08:00:27:5e:01:7c
Therefore: 08:00:27:5e:01:7c
```
10. Calculate the time difference between the ARP request and the corresponding ARP reply.
```
The reply says: 192.168.1.105 is at 08:00:27:5e:01:7c
Therefore: 08:00:27:5e:01:7c
```
11. Explain how the request and reply together establish an IP-to-MAC address mapping.
```
The client at 192.168.1.1 broadcasts an ARP request asking:

Who has 192.168.1.105?

The device owning 192.168.1.105 responds with its MAC address:

192.168.1.105 → 08:00:27:5e:01:7c

The sender can then store this association in its ARP cache and use the MAC address to send Ethernet frames to 192.168.1.105.
```