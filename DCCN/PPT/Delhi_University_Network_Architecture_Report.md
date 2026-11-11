# Delhi University Network Architecture Report

## 1. Introduction

This report describes the existing and proposed network architecture of the University of Delhi (DU) based on the document **“Bid for Campus Network.”** The document describes DU's campus-wide LAN, its three-tier architecture, connectivity through the Delhi University Computer Centre (DUCC), existing network equipment, the North and South Campus Internet architecture, and a proposed network layout.


## 2. University of Delhi Computer Centre and Campus Connectivity

The document states that the University of Delhi uses a **star topology network**, with the **Delhi University Computer Centre (DUCC)** acting as the nodal centre for both internal and external connectivity.

Departments, centres, hostels, residences and colleges are connected to DUCC through a **fiber-optic campus-wide LAN**. The document reports **67,000+ wired/wireless nodes** operating across departments, centres, hostels and colleges.

Internet and inter-campus connectivity described in the document includes:

- **10 Gbps Internet bandwidth from NKN, New Delhi for each campus**.
- Colleges connected through **250 Mbps fiber links via MPLS**.
- Campuses connected with **10 Gbps links from RailTel**.

## 3. Three-Tier Campus LAN Architecture

The campus LAN is described as a **three-tier architecture** consisting of:

1. **Access Layer**
2. **Distribution Layer**
3. **Core Layer**

Access locations connect directly to, or are aggregated toward, nearby distribution points. Distribution switches then connect toward the core switches located at DUCC.

The architecture is described as having **physical ring and logical redundancy at each layer**.

### 3.1 Design Principles

The document identifies four major design principles:

| Principle | Purpose stated in the document |
|---|---|
| Hierarchical | Clarifies device roles, simplifies deployment/operation/management, and reduces fault domains. |
| Modularity | Allows the network to grow on demand. |
| Resiliency | Supports high availability of network services. |
| Flexibility | Enables intelligent traffic load sharing using network resources. |

## 4. Access Layer

The access layer is the network edge where traffic enters or exits the campus network. Its primary purpose is to provide network access to users and endpoints.

According to the document, access switches connect upward to distribution switches, which connect to the core.

Important technologies and practices include:

- Limiting VLANs to a single closet wherever possible.
- Using **Rapid PVST+** to avoid Layer 2 loops.
- Using secure **VTP with MD5** to distribute VLAN configuration.
- Configuring trunks without negotiation and pruning unused VLANs.
- Applying **QoS** and per-port **MAC-address-based security**.
- Supporting different endpoint types and future voice, video and data requirements.

## 5. Distribution Layer

The distribution layer forms the interface between the access and core layers.

Its documented functions include:

- Aggregating and terminating Layer 2 broadcast domains from access switches.
- Running Rapid PVST+.
- Using secure VTP with MD5.
- Configuring trunks and pruning unused VLANs.
- Aggregating Layer 3 routing boundaries.
- Running **EIGRP** for fast convergence and equal-cost path sharing.
- Providing switching, routing and network-access policy functions.

## 6. Core Layer

The core layer acts as the backbone of the campus LAN. It connects the campus layers and provides connectivity between end devices, computing and storage services.

The document describes the core as an aggregator for campus blocks.

Its functions include:

- Aggregating and terminating Layer 2 broadcast domains from server-access switches.
- Running Rapid PVST+.
- Using secure VTP with MD5.
- Configuring trunks and pruning unused VLANs.
- Providing Layer 3 routing between distribution layers.
- Running EIGRP for fast convergence and equal-cost path sharing.
- Providing switching, routing and network-access policy functions.
- Supporting Layer 2/Layer 3 troubleshooting and traceroute capabilities.

## 7. Existing Network Equipment

The document lists the following existing equipment:

| Functionality | Model | Quantity | Location / Notes | Status |
|---|---|---:|---|---|
| Core Switch | Cisco Nexus 9K | 4 | 2 at DU North + 2 at DU South | Working; warranty |
| Distribution Switches | Cisco 2960 | 120 | Campus network | Working; warranty |
| Edge | 3Com, D-Link, Digisol, etc. | 300 | Various locations | Working; mixed warranty/AMC |
| Firewall | Sophos XGS6500 | 4 | 2 at North + 2 at South | Warranty |
| Wireless LAN Controller | Cisco 8540 | 2 | 1 at North + 1 at South | Working; not under warranty/AMC |
| Wireless Access Gateway | Mikrotik RB4011 | 25 | 20 North + 5 South | Working; warranty |
| Wireless Access Points | HFCL ion4xi | 1000 | North and South campuses | Working; warranty |
| Wireless Access Points | Cisco 3600/2800/1800 | 600 | Both campuses | Working; not under warranty/AMC |

## 8. Existing North and South Campus Architecture

The **Existing Network Layout diagram on page 10** shows a two-campus design.

### North Campus

The diagram shows:

**NKN → Juniper MX80 Router → UTM/Firewall → Dual Nexus 9K / Core → L3 Switching / VLANs**

The North Campus has a **10 Gbps connection to NKN**.

### South Campus

The diagram shows:

**NKN → Juniper M10i Router → UTM/Firewall → Dual Nexus 9K / Core → L2 Switching / VLANs**

The South Campus also has a **10 Gbps connection to NKN**.

The two campus core areas are shown with **Dual Nexus 9K for failover**. The diagram also indicates **100 Mbps MPLS-VPN connectivity to 52 off-campus colleges**.

## 9. Proposed Network Layout

The **Proposed Network Layout diagram on page 11** shows a more structured access/distribution/core arrangement.

At the top is a pair of **Core Switches**. Below them are distribution switches labelled:

- DS-1
- DS-2
- DS-3
- DS-13

The diagram shows multiple **10G SM (single-mode fiber) connections** between the core and distribution switches and between distribution elements.

The distribution layer connects to **24-port PoE+ switches**, which then provide **1G copper** connectivity to endpoints such as wireless access points and client devices.

The proposed diagram also shows an upper-right services area containing:

- VM Controller
- Orchestration Tool
- NMS
- AAA

This indicates a management/virtualization-oriented services component alongside the switching infrastructure.

## 10. End-to-End Traffic Flow

A simplified representation of the architecture is:

```text
                    Internet / External Networks
                              |
                             NKN
                              |
                   10 Gbps per campus
                              |
                    Router / Firewall
                              |
                       Core Layer
                  (Nexus 9K, redundant)
                              |
                    Distribution Layer
                (10G fiber interconnects)
                              |
                       Access Layer
                   (PoE+ access switches)
                              |
                    1G copper / Wi-Fi
                              |
                  Users and End Devices
```

For colleges, the document additionally describes MPLS-based connectivity, including the 100 Mbps MPLS-VPN connection shown in the existing network diagram.

## 11. Redundancy and Resilience

Resilience is a major theme of the architecture.

The document explicitly describes:

- Physical ring and logical redundancy at each layer.
- Dual core switches / Nexus 9K infrastructure.
- Failover capability in the North and South Campus design.
- EIGRP for fast convergence and equal-cost path sharing.
- Rapid PVST+ for Layer 2 loop avoidance.
- Modular hierarchical design to reduce fault domains and support growth.

These mechanisms are intended to maintain availability and provide alternative paths when network components or links fail.

## 12. Network Management and Security Features

The document identifies several operational and security-related mechanisms:

### VLAN and Layer 2 control
- VLAN segmentation.
- Rapid PVST+.
- Secure VTP with MD5.
- Trunk configuration and VLAN pruning.

### Access security
- Per-port MAC-address-based security.
- Network-access policy functions.

### Traffic management
- QoS at the access layer.
- Intelligent traffic load sharing.
- Routing through EIGRP at the distribution/core layers.

### Troubleshooting
- Layer 2 and Layer 3 traceroute.
- Layer 2 debugging.
- Compatibility with protocols used by the existing campus LAN.

## 13. Architectural Interpretation

Based strictly on the supplied document, DU's architecture can be understood as a **hierarchical, redundant campus network**.

The architecture separates responsibilities:

- **Access**: endpoint connectivity and edge controls.
- **Distribution**: aggregation, routing boundaries and policy.
- **Core**: high-speed backbone and campus-wide interconnection.
- **External connectivity**: NKN and RailTel/MPLS links.
- **Security boundary**: UTM/firewall components between external connectivity and campus switching.
- **Wireless infrastructure**: wireless controllers, gateways and access points.
- **Management/services**: the proposed design shows NMS, AAA, orchestration and VM-controller components.

## 14. Existing vs Proposed Architecture

| Aspect | Existing architecture | Proposed architecture |
|---|---|---|
| Core | Dual Nexus 9K at North/South campuses | Redundant core switches shown centrally |
| Distribution | Cisco 2960 distribution layer | Multiple dedicated distribution switches |
| Access | Mixed edge/access equipment | 24-port PoE+ access switches |
| Uplinks | Campus/core links and MPLS connectivity | Multiple 10G single-mode fiber uplinks |
| Wireless | Cisco WLC, Mikrotik gateways and multiple AP generations | APs/endpoints connected through PoE+ access |
| Management | Existing campus network management functions | VM controller, orchestration, NMS and AAA explicitly shown |
| Redundancy | Dual Nexus 9K and failover | Multiple cross-connected core/distribution paths |

## 15. Key Observations and Limitations of the Source

The supplied document provides a strong high-level view of the architecture, but it does not provide every implementation detail. In particular, the report should not assume details that are not explicitly shown.

The document does not fully specify:

- IP addressing and subnet allocation.
- Exact VLAN IDs and VLAN-to-department mapping.
- Exact routing tables or EIGRP areas/parameters.
- Firewall rule sets.
- Detailed NKN/Internet edge security policies.
- Exact physical fiber routes between every building.
- Detailed wireless SSID and authentication configuration.
- Exact specifications of every proposed switch.
- Detailed configuration of the VM controller, NMS, orchestration or AAA systems.

Therefore, those details would require additional DU network documentation or configuration records.

## 16. Conclusion

The University of Delhi campus network described in the supplied *Bid for Campus Network* document is a large-scale fiber-based campus network centered on DUCC. It uses a hierarchical **three-tier Core–Distribution–Access architecture**, with redundancy and modularity built into the design.

The existing infrastructure includes high-end Cisco Nexus 9K core switches, Cisco 2960 distribution switches, heterogeneous edge switches, Sophos firewalls, wireless LAN controllers, gateways and a large wireless access-point deployment. The North and South Campus architecture uses NKN connectivity at 10 Gbps per campus, with additional MPLS/RailTel connectivity described for colleges and campuses.

The proposed architecture further emphasizes redundant core/distribution connectivity, 10G single-mode fiber uplinks, PoE+ access switching, and centralized services such as NMS, AAA, orchestration and VM management.

**Primary source:** University of Delhi, *Bid for Campus Network*, supplied document, pages 6–11.
