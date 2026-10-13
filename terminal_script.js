    // Multi-Device Terminal Simulation Database
    const deviceConfigs = {
      "core-sw": {
        name: "KYNDRYL-CORE-SW01",
        title: "KYNDRYL-CORE-SW01# (Cisco Catalyst 9300-24T IOS-XE 17.09.04a)",
        badge: "Layer 3 Distribution & Core Gateway",
        prompt: "KYNDRYL-CORE-SW01#",
        promptColor: "#10b981",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-CORE-SW01
Cisco IOS XE Software, Version 17.09.04a [Amsterdam] - Catalyst 9300-24T
IP Address: 10.10.1.2/24 (Uplink), 10.10.10.1/24 (VLAN 10 Default Gateway)
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show ip int br", cmd: "show ip interface brief" },
          { label: "show vlan br", cmd: "show vlan brief" },
          { label: "show int trunk", cmd: "show interfaces trunk" },
          { label: "show spanning-tree", cmd: "show spanning-tree" },
          { label: "show standby br", cmd: "show standby brief" },
          { label: "show ip route", cmd: "show ip route" },
          { label: "show errdisabled", cmd: "show interface status err-disabled" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-CORE-SW01:
  show ip interface brief       - Display IP addresses and status on all ports & SVIs
  show vlan brief               - Display active VLANs and assigned physical ports
  show interfaces trunk         - Display active 802.1Q trunk links, allowed VLANs
  show mac address-table        - Display dynamically learned Layer 2 MAC addresses
  show spanning-tree            - Display STP RSTP topology, root bridge, port roles
  show standby brief            - Display HSRP First Hop Redundancy gateway state
  show ip route                 - Display core Layer 3 routing table
  show ip ospf neighbor         - Display OSPF neighbor adjacencies with Edge Router
  show etherchannel summary     - Display bundled port-channels and member ports
  show interface status err-disabled - Display ports shutdown by STP or port security
  show cdp neighbors            - Display directly connected Cisco neighbors
  show version                  - Display IOS-XE version and uptime
  show logging                  - Display syslog buffer and interface flap alerts
  show tech-support             - Dump standard Kyndryl escalation diagnostic logs
  ping 10.10.1.1                - Test ICMP reachability to Edge Router
  traceroute 10.50.0.1          - Trace route to wireless gateway
  clear                         - Clear terminal window`,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1/0/1   unassigned      YES unset  up                    up      
GigabitEthernet1/0/2   unassigned      YES unset  up                    up      
GigabitEthernet1/0/3   unassigned      YES unset  down                  down    
GigabitEthernet1/0/4   unassigned      YES unset  down                  down    
GigabitEthernet1/0/23  unassigned      YES unset  up                    up      
GigabitEthernet1/0/24  10.10.1.2       YES manual up                    up      
TenGigabitEthernet1/1/1 unassigned     YES unset  up                    up      
TenGigabitEthernet1/1/2 unassigned     YES unset  up                    up      
Vlan1                  unassigned      YES unset  administratively down down    
Vlan10                 10.10.10.1      YES manual up                    up      
Vlan20                 10.10.20.1      YES manual up                    up      
Vlan30                 10.10.30.1      YES manual up                    up      
Vlan50                 10.10.50.1      YES manual up                    up      
Vlan99                 10.10.99.1      YES manual up                    up      `,

          "show vlan brief": `VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/5, Gi1/0/6, Gi1/0/7
10   DATA_USERS                       active    Gi1/0/8, Gi1/0/9, Gi1/0/10
20   VOICE_PHONES                     active    Gi1/0/11, Gi1/0/12, Gi1/0/13
30   SERVERS_DC                       active    Gi1/0/14, Gi1/0/15
50   WIRELESS_USERS                   active    Gi1/0/16, Gi1/0/17
99   MANAGEMENT                       active    Gi1/0/24`,

          "show interfaces trunk": `Port        Mode             Encapsulation  Status        Native vlan
Te1/1/1     on               802.1q         trunking      99
Te1/1/2     on               802.1q         trunking      99
Gi1/0/23    on               802.1q         trunking      99

Port        Vlans allowed on trunk
Te1/1/1     1-4094
Te1/1/2     1-4094
Gi1/0/23    10,20,30,50,99

Port        Vlans in spanning tree forwarding state and not pruned
Te1/1/1     1,10,20,30,50,99
Te1/1/2     1,10,20,30,50,99
Gi1/0/23    10,20,99`,

          "show spanning-tree": `VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    24586
             Address     0019.06e7.6480
             Cost        4
             Port        Te1/1/1 (TenGigabitEthernet1/1/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     70ea.1ae4.3300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Te1/1/1             Root FWD 4         128.53   P2p 
Te1/1/2             Altn BLK 4         128.54   P2p 
Gi1/0/23            Desg FWD 19        128.23   P2p `,

          "show standby brief": `Interface   Grp  Pri P State   Active          Standby         Virtual IP
Vl10        10   110 P Active  local           10.10.10.2      10.10.10.254
Vl20        20   90    Standby 10.10.20.2      local           10.10.20.254
Vl50        50   110 P Active  local           10.10.50.2      10.10.50.254`,

          "show ip route": `Gateway of last resort is 10.10.1.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 10.10.1.1, GigabitEthernet1/0/24
C     10.10.10.0/24 is directly connected, Vlan10
L     10.10.10.1/32 is directly connected, Vlan10
C     10.10.20.0/24 is directly connected, Vlan20
L     10.10.20.1/32 is directly connected, Vlan20
C     10.10.30.0/24 is directly connected, Vlan30
L     10.10.30.1/32 is directly connected, Vlan30
C     10.10.50.0/24 is directly connected, Vlan50
O     172.16.0.0/16 [110/11] via 10.10.1.1, 05:22:18, GigabitEthernet1/0/24
O     192.168.100.0/24 [110/20] via 10.10.1.1, 05:22:18, GigabitEthernet1/0/24`,

          "show ip ospf neighbor": `Neighbor ID     Pri   State           Dead Time   Address         Interface
198.51.100.2      1   FULL/BDR        00:00:36    10.10.1.1       GigabitEthernet1/0/24`,

          "show mac address-table": `          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    0050.56a1.2b3c    DYNAMIC     Gi1/0/23
  10    0050.56a1.9f12    DYNAMIC     Gi1/0/23
  20    0004.f211.bb44    DYNAMIC     Gi1/0/23
  30    d46d.50e1.77aa    DYNAMIC     Gi1/0/14
  99    0000.0c07.ac01    DYNAMIC     Te1/1/1
Total Mac Addresses for this criterion: 5`,

          "show etherchannel summary": `Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP      Te1/1/1(P)    Te1/1/2(P)`,

          "show interface status err-disabled": `Port      Name               Status       Reason               Err-disabled Vlans
Gi1/0/14  CONF_ROOM_JACK     err-disabled psecure-violation
Gi1/0/22  FLOOR_3_DROP       err-disabled bpduguard`,

          "show cdp neighbors": `Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
KYNDRYL-EDGE-RTR01 Gi 1/0/24       162        R B         ISR4451   Gi 0/0/2
KYNDRYL-ACC-SW02   Gi 1/0/23       148        S I         C9200L    Gi 1/0/23`,

          "show version": `Cisco IOS XE Software, Version 17.09.04a [Amsterdam]
cisco C9300-24T (X86) processor with 1813437K/6147K bytes of memory.
Processor board ID FOC2419L1AB
Switch Ports Model              SW Version        SW Image              Mode   
*    1 28    C9300-24T          17.09.04a         CAT9K_IOSXE           INSTALL
Configuration register is 0x102`,

          "show logging": `Syslog logging: enabled (0 messages dropped, 3 flushes, 0 overruns)
    Console logging: level debugging, 1823 messages logged
*Oct 13 18:22:10.412: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/24, changed state to up
*Oct 13 18:22:11.413: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/24, changed state to up
*Oct 13 18:22:15.981: %OSPF-5-ADJCHG: Process 1, Nbr 198.51.100.2 on GigabitEthernet1/0/24 from LOADING to FULL, Loading Done`,

          "show tech-support": `------------------ show version ------------------
Cisco IOS XE Software, Version 17.09.04a
System image file is "bootflash:packages.conf"
cisco C9300-24T (X86) processor with 1813437K/6147K bytes of memory.
Uptime for this switch is 18 weeks, 4 days, 12 hours, 14 minutes.
Configuration register is 0x102
[LOG BUFFER ATTACHED FOR KYNDRYL L2/L3 ESCALATION TICKET]`,

          "ping 10.10.1.1": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms`,

          "traceroute 10.50.0.1": `Type escape sequence to abort.
Tracing the route to 10.50.0.1
VRF info: (default VRF)
  1 10.10.1.1 1 msec 1 msec 2 msec
  2 10.50.0.1 2 msec 2 msec 3 msec`
        }
      },

      "acc-sw": {
        name: "KYNDRYL-ACC-SW02",
        title: "KYNDRYL-ACC-SW02# (Cisco Catalyst 9200L-48P-4G IOS-XE 17.09.03)",
        badge: "Floor 3 Access Switch / PoE+ & 802.1X",
        prompt: "KYNDRYL-ACC-SW02#",
        promptColor: "#38bdf8",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-ACC-SW02
Cisco IOS XE Software, Version 17.09.03 [Amsterdam] - Catalyst 9200L-48P-4G
Management IP: 10.10.99.2/24 (VLAN 99), Uplink: Gi1/0/23 -> CORE-SW01
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show int status", cmd: "show interfaces status" },
          { label: "show port-sec", cmd: "show port-security interface gi1/0/14" },
          { label: "show power inline", cmd: "show power inline" },
          { label: "show vlan br", cmd: "show vlan brief" },
          { label: "show errdisabled", cmd: "show interface status err-disabled" },
          { label: "show cdp neighbors", cmd: "show cdp neighbors" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-ACC-SW02:
  show interfaces status        - Display connected state, VLAN, duplex, speed of ports
  show port-security interface <id> - Check port security violations & shutdown state
  show port-security address    - Display secure sticky MAC address table
  show power inline             - Display PoE budget and power draw (IP Phones & APs)
  show vlan brief               - Display active VLANs on access switch
  show ip interface brief       - Display management SVI and port states
  show interface status err-disabled - Check errdisabled ports (e.g. psecure-violation)
  show spanning-tree vlan 10    - Display STP port state (Root, Designated, Edge)
  show mac address-table        - Display learned MAC addresses from desk drops
  show ip dhcp snooping binding - Display DHCP snooping table (IP-to-MAC leases)
  show cdp neighbors            - Display connected Core Switch, IP Phones, APs
  show version                  - Display Catalyst 9200 switch model and software
  ping 10.10.99.1               - Test reachability to Core Switch SVI gateway
  clear                         - Clear terminal window`,

          "show interfaces status": `Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/1   PC_DESK_301        connected    10         a-full a-1000 10/100/1000BaseTX
Gi1/0/2   PC_DESK_302        connected    10         a-full a-1000 10/100/1000BaseTX
Gi1/0/3   PC_DESK_303        notconnect   10           auto   auto 10/100/1000BaseTX
Gi1/0/11  IP_PHONE_301       connected    10,20      a-full a-1000 10/100/1000BaseTX
Gi1/0/14  CONF_ROOM_JACK     err-disabled 10           auto   auto 10/100/1000BaseTX
Gi1/0/15  AP_FLOOR_3_EAST    connected    50,trunk   a-full a-1000 10/100/1000BaseTX
Gi1/0/23  UPLINK_CORE-SW01   connected    trunk      a-full a-1000 10/100/1000BaseTX`,

          "show port-security interface gi1/0/14": `Port Security              : Enabled
Port Status                : Secure-shutdown
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 0
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 0050.56b2.88e1:10
Security Violation Count   : 1`,

          "show port-security address": `               Secure Mac Address Table
-------------------------------------------------------------------
Vlan    Mac Address       Type                    Ports   Remaining Age
                                                             (mins)
----    -----------       ----                    -----   -------------
  10    0050.56a1.2b3c    SecureConfigured        Gi1/0/1      -
  10    0050.56a1.9f12    SecureSticky            Gi1/0/2      -
Total Addresses: 2`,

          "show power inline": `Available: 740.0(w)  Used: 124.6(w)  Remaining: 615.4(w)

Interface Admin  Oper       Power(Watts) Device              Class Max
--------- ------ ---------- ----------- ------------------- ----- ----
Gi1/0/11  auto   on         12.0        IP Phone 8845       3     15.4
Gi1/0/12  auto   on         12.0        IP Phone 8845       3     15.4
Gi1/0/15  auto   on         25.5        C9120AXI-B Access Pt 4     30.0
Gi1/0/16  auto   on         25.5        C9120AXI-B Access Pt 4     30.0`,

          "show vlan brief": `VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/4, Gi1/0/5, Gi1/0/6
10   DATA_USERS                       active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/11
20   VOICE_PHONES                     active    Gi1/0/11, Gi1/0/12
50   WIRELESS_AP                      active    Gi1/0/15, Gi1/0/16
99   MANAGEMENT                       active    `,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
Vlan99                 10.10.99.2      YES manual up                    up      
GigabitEthernet1/0/1   unassigned      YES unset  up                    up      
GigabitEthernet1/0/2   unassigned      YES unset  up                    up      
GigabitEthernet1/0/14  unassigned      YES unset  down                  down    
GigabitEthernet1/0/23  unassigned      YES unset  up                    up      `,

          "show interface status err-disabled": `Port      Name               Status       Reason               Err-disabled Vlans
Gi1/0/14  CONF_ROOM_JACK     err-disabled psecure-violation`,

          "show spanning-tree vlan 10": `VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    24586
             Address     0019.06e7.6480
             Cost        19
             Port        Gi1/0/23 (GigabitEthernet1/0/23)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     ac44.f288.1900
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi1/0/1             Desg FWD 19        128.1    P2p Edge 
Gi1/0/2             Desg FWD 19        128.2    P2p Edge 
Gi1/0/11            Desg FWD 19        128.11   P2p Edge 
Gi1/0/23            Root FWD 19        128.23   P2p `,

          "show mac address-table": `          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    0050.56a1.2b3c    STATIC      Gi1/0/1
  10    0050.56a1.9f12    STATIC      Gi1/0/2
  20    0004.f211.bb44    DYNAMIC     Gi1/0/11
  50    4c77.6d22.ea10    DYNAMIC     Gi1/0/15
  99    70ea.1ae4.3300    DYNAMIC     Gi1/0/23
Total Mac Addresses for this criterion: 5`,

          "show ip dhcp snooping binding": `MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:50:56:A1:2B:3C   10.10.10.85      86400       dhcp-snooping   10   GigabitEthernet1/0/1
00:50:56:A1:9F:12   10.10.10.86      86400       dhcp-snooping   10   GigabitEthernet1/0/2
00:04:F2:11:BB:44   10.10.20.101     86400       dhcp-snooping   20   GigabitEthernet1/0/11
Total number of bindings: 3`,

          "show cdp neighbors": `Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
KYNDRYL-CORE-SW01 Gi 1/0/23        174        S I         C9300-24T Gi 1/0/23
SEP0004F211BB44  Gi 1/0/11        132        H P         IP Phone  Port 1
AP-FL3-EAST      Gi 1/0/15        155        T           C9120AXI  Gig 0`,

          "show version": `Cisco IOS XE Software, Version 17.09.03 [Amsterdam]
cisco C9200L-48P-4G (ARM) processor with 2097152K bytes of memory.
Processor board ID JAE254807ZZ
Switch Ports Model              SW Version        SW Image              Mode   
*    1 52    C9200L-48P-4G      17.09.03          CAT9K_LITE_IOSXE      INSTALL
Configuration register is 0x102`,

          "ping 10.10.99.1": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.99.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms`
        }
      },

      "edge-rtr": {
        name: "KYNDRYL-EDGE-RTR01",
        title: "KYNDRYL-EDGE-RTR01# (Cisco ISR 4451-X/K9 IOS-XE 17.06.05)",
        badge: "Enterprise WAN Edge / BGP & IPsec Gateway",
        prompt: "KYNDRYL-EDGE-RTR01#",
        promptColor: "#6366f1",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-EDGE-RTR01
Cisco IOS XE Software, Version 17.06.05 - Cisco ISR4451-X/K9
WAN Public IP: 198.51.100.2 (ISP1), LAN Gateway: 10.10.1.1/24 (Core Uplink)
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show ip int br", cmd: "show ip interface brief" },
          { label: "show ip route", cmd: "show ip route" },
          { label: "show ip ospf neighbor", cmd: "show ip ospf neighbor" },
          { label: "show ip bgp summary", cmd: "show ip bgp summary" },
          { label: "show ip nat translations", cmd: "show ip nat translations" },
          { label: "show access-lists", cmd: "show access-lists" },
          { label: "show crypto session", cmd: "show crypto session" },
          { label: "ping 8.8.8.8", cmd: "ping 8.8.8.8" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-EDGE-RTR01:
  show ip interface brief       - Display WAN, LAN, and Tunnel IP interface statuses
  show ip route                 - Display entire BGP, OSPF, and Static routing table
  show ip ospf neighbor         - Display internal OSPF neighbor state with Core Switch
  show ip bgp summary           - Display ISP BGP peer status (AS 15169 / AS 209)
  show ip nat translations      - Display active dynamic NAT/PAT translation sessions
  show ip nat statistics        - Display NAT hit/miss counters and pool exhaustion
  show access-lists             - Display ACL packet match counters
  show crypto session           - Display IPsec VPN tunnel state to Microsoft Azure
  show ip arp                   - Display ARP IP-to-MAC resolution table
  show version                  - Display ISR 4451 hardware and IOS-XE version
  ping 8.8.8.8                  - Test public Internet DNS reachability
  traceroute 8.8.8.8            - Trace WAN hops across ISP Autonomous Systems
  clear                         - Clear terminal window`,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   198.51.100.2    YES manual up                    up      
GigabitEthernet0/0/1   203.0.113.2     YES manual up                    up      
GigabitEthernet0/0/2   10.10.1.1       YES manual up                    up      
Tunnel1                172.16.254.2    YES manual up                    up      
Loopback0              198.51.100.254  YES manual up                    up      `,

          "show ip route": `Gateway of last resort is 198.51.100.1 to network 0.0.0.0

B*    0.0.0.0/0 [20/0] via 198.51.100.1, 42w2d
C     10.10.1.0/24 is directly connected, GigabitEthernet0/0/2
L     10.10.1.1/32 is directly connected, GigabitEthernet0/0/2
O     10.10.10.0/24 [110/2] via 10.10.1.2, 05:42:11, GigabitEthernet0/0/2
O     10.10.20.0/24 [110/2] via 10.10.1.2, 05:42:11, GigabitEthernet0/0/2
O     10.10.50.0/24 [110/2] via 10.10.1.2, 05:42:11, GigabitEthernet0/0/2
S     172.16.0.0/16 [1/0] via 172.16.254.1, Tunnel1
C     198.51.100.0/29 is directly connected, GigabitEthernet0/0/0
L     198.51.100.2/32 is directly connected, GigabitEthernet0/0/0
C     203.0.113.0/29 is directly connected, GigabitEthernet0/0/1`,

          "show ip ospf neighbor": `Neighbor ID     Pri   State           Dead Time   Address         Interface
10.10.10.1        1   FULL/DR         00:00:32    10.10.1.2       GigabitEthernet0/0/2`,

          "show ip bgp summary": `BGP router identifier 198.51.100.2, local AS number 65000
BGP table version is 9124401, main routing table version 9124401

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
198.51.100.1    4        15169 1240182  941209  9124401    0    0 42w2d               1
203.0.113.1     4          209  981204  782103  9124401    0    0 18w5d               1`,

          "show ip nat translations": `Pro Inside global         Inside local          Outside local         Outside global
tcp 198.51.100.2:49821    10.10.10.85:49821     52.96.166.130:443     52.96.166.130:443
tcp 198.51.100.2:51402    10.10.10.85:51402     142.250.224.46:443    142.250.224.46:443
udp 198.51.100.2:58102    10.10.20.101:5060     104.244.42.1:5060     104.244.42.1:5060
icmp 198.51.100.2:12      10.10.10.85:12        8.8.8.8:12            8.8.8.8:12`,

          "show ip nat statistics": `Total active translations: 3,428 (0 static, 3428 dynamic; 3428 extended)
Outside interfaces: GigabitEthernet0/0/0, GigabitEthernet0/0/1
Inside interfaces: GigabitEthernet0/0/2
Hits: 28914022  Misses: 3428
CEF Translated packets: 28910594, CEF Punted packets: 3428
Expired translations: 1842109
Dynamic mappings:
-- Inside Source
 [Id: 1] access-list NAT_USERS pool OVERLOAD refcount 3428`,

          "show access-lists": `Extended IP access list WAN_INSPECT
    10 permit ospf any any (142010 matches)
    20 permit tcp any any established (18442100 matches)
    30 permit udp any any eq domain (894012 matches)
    40 permit icmp any any echo-reply (31024 matches)
    50 deny ip any any log (41209 matches)
Standard IP access list NAT_USERS
    10 permit 10.10.0.0, wildcard bits 0.0.255.255 (28914022 matches)`,

          "show crypto session": `Crypto session current status

Interface: Tunnel1
Session status: UP-ACTIVE
Peer: 20.42.118.90 port 500
  Session ID: 4108
  IKEv2 SA: local 198.51.100.2/500 remote 20.42.118.90/500 Active
  IPSEC FLOW: permit ip 10.10.0.0/16 172.16.0.0/16
        Active SAs: 2, origin: crypto map
        Inbound Pkts: 7991440, Outbound Pkts: 8421902`,

          "show ip arp": `Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.10.1.1               -   001b.d45a.1102  ARPA   GigabitEthernet0/0/2
Internet  10.10.1.2               4   70ea.1ae4.3324  ARPA   GigabitEthernet0/0/2
Internet  198.51.100.1            1   0008.e3ff.fd90  ARPA   GigabitEthernet0/0/0
Internet  198.51.100.2            -   001b.d45a.1100  ARPA   GigabitEthernet0/0/0`,

          "show version": `Cisco IOS XE Software, Version 17.06.05
Cisco ISR4451-X/K9 (quad-core) processor with 3816567K/6147K bytes of memory.
Router operating mode: Autonomous
4 Gigabit Ethernet interfaces
System image file is "bootflash:isr4400-universalk9.17.06.05.SPA.bin"
Uptime for this router is 42 weeks, 2 days, 8 hours, 19 minutes.`,

          "ping 8.8.8.8": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 14/16/21 ms`,

          "traceroute 8.8.8.8": `Type escape sequence to abort.
Tracing the route to 8.8.8.8
VRF info: (default VRF)
  1 198.51.100.1 [AS 15169] 2 msec 1 msec 2 msec
  2 72.14.214.1 [AS 15169] 8 msec 7 msec 9 msec
  3 142.250.224.1 [AS 15169] 12 msec 13 msec 12 msec
  4 8.8.8.8 [AS 15169] 15 msec 16 msec 15 msec`
        }
      },

      "fw": {
        name: "KYNDRYL-FW01",
        title: "KYNDRYL-FW01# (Cisco ASA 5516-X Software Version 9.16(2))",
        badge: "Perimeter Security & Stateful Firewall",
        prompt: "KYNDRYL-FW01#",
        promptColor: "#f43f5e",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-FW01
Cisco Adaptive Security Appliance Software Version 9.16(2) - ASA 5516-X
Security Context: System / Multi-Zone (Inside, Outside, DMZ)
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show int ip br", cmd: "show interface ip brief" },
          { label: "show conn count", cmd: "show conn count" },
          { label: "show access-list", cmd: "show access-list" },
          { label: "show nat", cmd: "show nat" },
          { label: "show vpn-sessiondb l2l", cmd: "show vpn-sessiondb l2l" },
          { label: "show failover", cmd: "show failover" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-FW01 (Cisco ASA):
  show interface ip brief       - Display IP addresses and status of firewall zones
  show conn count               - Display current active stateful TCP/UDP connections
  show conn                     - Display active connection table details
  show access-list              - Display ASA Access Control Entries with hit counts
  show nat                      - Display Object and Manual NAT policy statistics
  show vpn-sessiondb l2l        - Display active Site-to-Site IPsec VPN tunnels
  show failover                 - Display High Availability (Active/Standby) status
  show xlate count              - Display active address translation slots
  show version                  - Display ASA software version and hardware spec
  ping 10.10.1.1                - Test reachability to Edge Router inside interface
  clear                         - Clear terminal window`,

          "show interface ip brief": `Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0         198.51.100.1    YES manual up                    up      
GigabitEthernet0/1         10.10.1.254     YES manual up                    up      
GigabitEthernet0/2         172.16.10.1     YES manual up                    up      
Management0/0              10.10.99.254    YES manual up                    up      `,

          "show conn count": `4821 in use, 14290 most used`,

          "show conn": `TCP outside 13.107.42.16:443 inside 10.10.10.85:51221, idle 0:00:04, bytes 192842, flags UIO
TCP outside 52.96.166.130:443 inside 10.10.10.85:49821, idle 0:00:01, bytes 849102, flags UIO
UDP outside 8.8.8.8:53 inside 10.10.10.85:61204, idle 0:00:12, bytes 184, flags -
TCP dmz 172.16.10.50:443 outside 198.51.100.88:39102, idle 0:00:08, bytes 42890, flags UIO`,

          "show access-list": `access-list OUTSIDE_IN; 4 elements; name hash: 0x8a91bc12
  line 1 extended permit icmp any any echo-reply (hitcnt=14201)
  line 2 extended permit tcp any host 172.16.10.50 eq https (hitcnt=892100)
  line 3 extended permit esp any any (hitcnt=498112)
  line 4 extended deny ip any any (hitcnt=68219)
access-list INSIDE_OUT; 2 elements; name hash: 0x4f12dc88
  line 1 extended permit ip 10.10.0.0 255.255.0.0 any (hitcnt=9412081)
  line 2 extended deny ip any any (hitcnt=0)`,

          "show nat": `Manual NAT Policies (Section 1)
1 (inside,outside) to (outside,inside)
    source dynamic OBJ-CORP-LAN interface
    translate_hits = 9412081, untranslate_hits = 8912440
Auto NAT Policies (Section 2)
1 (dmz,outside) to (outside,dmz)
    source static OBJ-WEB-SERVER 198.51.100.50 service tcp 443 443
    translate_hits = 892100, untranslate_hits = 892100`,

          "show vpn-sessiondb l2l": `---------------------------------------------------------------------------
VPN Session Summary
---------------------------------------------------------------------------
Active : 2   Cumulative : 184   Peak : 6

---------------------------------------------------------------------------
Connection-specific data:
---------------------------------------------------------------------------
Connection   : Azure-East-US-Tunnel
Index        : 14                IP Addr     : 20.42.118.90
Protocol     : IKEv2 IPsec       Encryption  : AES-GCM-256
Hashing      : SHA384            Bytes Tx    : 842190204
Bytes Rx     : 799144012         Login Time  : 04:12:18 UTC Oct 01 2026
Duration     : 12d 14h 22m

Connection   : AWS-Transit-Gateway
Index        : 15                IP Addr     : 3.120.44.12
Protocol     : IKEv2 IPsec       Encryption  : AES-GCM-256
Duration     : 38d 02h 11m`,

          "show failover": `Failover On 
Failover unit Primary
Failover LAN Interface: FO-LINK GigabitEthernet0/3 (up)
Unit Poll frequency 1 seconds, holdtime 15 seconds
Interface outside (198.51.100.1): Normal (Monitored)
Interface inside (10.10.1.254): Normal (Monitored)
Interface dmz (172.16.10.1): Normal (Monitored)
  This host: Primary - Active 
             Active time: 8941200 (sec)
  Other host: Secondary - Standby Ready 
             Active time: 0 (sec)`,

          "show version": `Cisco Adaptive Security Appliance Software Version 9.16(2)
SSP Operating System Version 9.16(2)
Device Type: ASA 5516-X with FirePOWER Services
Hardware:   ASA5516, 8192 MB RAM, CPU Atom C2000 series 2400 MHz
Uptime:     103 days 11 hours 42 mins
Configuration register is 0x1`,

          "ping 10.10.1.1": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms`
        }
      },

      "wlc": {
        name: "KYNDRYL-WLC01",
        title: "KYNDRYL-WLC01# (Cisco Catalyst 9800-CL WLC IOS-XE 17.09.02)",
        badge: "Enterprise Wireless LAN Controller",
        prompt: "KYNDRYL-WLC01#",
        promptColor: "#f59e0b",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-WLC01
Cisco IOS XE Software, Version 17.09.02 - Catalyst 9800-CL Wireless Controller
Management IP: 10.10.50.10/24 (VLAN 50), Active APs: 4, Associated Clients: 142
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show ap summary", cmd: "show ap summary" },
          { label: "show wlan summary", cmd: "show wlan summary" },
          { label: "show client summary", cmd: "show wireless client summary" },
          { label: "show ap 5ghz", cmd: "show ap dot11 5ghz summary" },
          { label: "show mobility summary", cmd: "show mobility summary" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-WLC01:
  show ap summary               - Display all registered lightweight APs, model, IP, status
  show wlan summary             - Display broadcasted SSIDs and security profiles
  show wireless client summary  - Display active associated Wi-Fi stations & speeds
  show ap dot11 5ghz summary    - Display 5GHz RF channels, power levels, utilization
  show mobility summary         - Display mobility tunnel peering with remote controllers
  show ip interface brief       - Display controller management and CAPWAP interfaces
  show version                  - Display Catalyst 9800-CL WLC system information
  clear                         - Clear terminal window`,

          "show ap summary": `Number of APs: 4

AP Name          Slots    AP Model       Ethernet MAC    Radio MAC       Location             State
---------------------------------------------------------------------------------------------------
AP-FL3-EAST        2      C9120AXI-B     4c77.6d22.ea10  4c77.6d22.ea20  Floor-3-Wing-A       Registered
AP-FL3-WEST        2      C9120AXI-B     4c77.6d22.eb10  4c77.6d22.eb20  Floor-3-Wing-B       Registered
AP-CONF-01         2      C9130AXI-B     7069.5a11.9010  7069.5a11.9020  Exec-Boardroom       Registered
AP-EXEC-02         2      C9130AXI-B     7069.5a11.9110  7069.5a11.9120  Floor-4-Exec-Suite   Registered`,

          "show wlan summary": `Number of WLANs: 3

WLAN ID   WLAN Profile Name       SSID                    Status   Security
--------------------------------------------------------------------------------
1         Kyndryl-Corp-Profile    Kyndryl-Corporate       UP       [WPA3-Enterprise] 802.1x
2         Kyndryl-Guest-Profile   Kyndryl-Guest           UP       [Open] WebAuth-Portal
3         Kyndryl-IoT-Profile     Kyndryl-Warehouse-IoT   UP       [WPA2-PSK] AES`,

          "show wireless client summary": `Number of Local Clients: 142

MAC Address    AP Name          WLAN  State            Protocol  Method   Role
--------------------------------------------------------------------------------
0050.56a1.2b3c AP-FL3-EAST      1     Run              11ax(5G)  Dot1x    Local
0004.f211.bb44 AP-FL3-WEST      1     Run              11ac(5G)  Dot1x    Local
784f.43a2.1190 AP-CONF-01       2     Webauth Pending  11ax(2.4G)None     Guest
d46d.50e1.77aa AP-EXEC-02       1     Run              11ax(5G)  Dot1x    Local`,

          "show ap dot11 5ghz summary": `AP Name          Radio MAC       Channel       Pwr-Lvl CleanAir  Channel-Utilization
------------------------------------------------------------------------------------
AP-FL3-EAST      4c77.6d22.ea20  36, (80MHz)   2       Enabled   18%
AP-FL3-WEST      4c77.6d22.eb20  52, (80MHz)*  2       Enabled   22%
AP-CONF-01       7069.5a11.9020  100,(80MHz)*  1       Enabled   14%
AP-EXEC-02       7069.5a11.9120  149,(80MHz)   2       Enabled   12%
*DFS Channel`,

          "show mobility summary": `Mobility Protocol: 802.11r / CAPWAP
Mobility Group Name: KYNDRYL-CORP-MOBILITY
Public IP: 198.51.100.50

Peer IP          State           Data Path   Control Path
---------------------------------------------------------
10.10.50.11      Up              Encrypted   Encrypted`,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
Vlan50                 10.10.50.10     YES manual up                    up      
GigabitEthernet1       unassigned      YES unset  up                    up      
GigabitEthernet2       unassigned      YES unset  up                    up      `,

          "show version": `Cisco IOS XE Software, Version 17.09.02 [Amsterdam]
cisco C9800-CL Software (X86_64_LINUX_IOSD-UNIVERSALK9-M)
Processor board ID 90K9W800CL1
Uptime for this controller is 64 days, 18 hours, 44 minutes.`
        }
      },

      "host-pc": {
        name: "NOC-ADMIN-PC",
        title: "NOC-ADMIN-PC (Windows 11 Enterprise PowerShell 7.4)",
        badge: "Diagnostic End-User Host / Workstation",
        prompt: "PS C:\\Users\\Kyndryl-NOC> ",
        promptColor: "#a78bfa",
        banner: `Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Host Name: NOC-ADMIN-PC (Kyndryl Network Operations Operations Center)
Assigned IP: 10.10.10.85/24 (VLAN 10 Data), Gateway: 10.10.10.1
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "ipconfig /all", cmd: "ipconfig /all" },
          { label: "ping gateway", cmd: "ping 10.10.10.1" },
          { label: "ping internet", cmd: "ping 8.8.8.8" },
          { label: "tracert 8.8.8.8", cmd: "tracert 8.8.8.8" },
          { label: "nslookup", cmd: "nslookup portal.kyndryl.com" },
          { label: "arp -a", cmd: "arp -a" },
          { label: "netstat -ano", cmd: "netstat -ano" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available diagnostic commands on NOC-ADMIN-PC:
  ipconfig /all                 - Display full TCP/IP configuration, DHCP lease & DNS
  ping 10.10.10.1               - Test ICMP echo to Local Default Gateway (Core Switch)
  ping 8.8.8.8                  - Test ICMP echo across WAN edge to Public Internet
  tracert 8.8.8.8               - Trace complete hop path from PC to Internet
  nslookup portal.kyndryl.com   - Test internal corporate DNS record resolution
  arp -a                        - Display local ARP table and Gateway MAC address
  netstat -ano                  - Display active TCP socket connections and PIDs
  curl -I https://portal.kyndryl.com - Send HTTP HEAD request to verify Web server
  route print                   - Display local Windows IPv4 routing table
  clear                         - Clear terminal window`,

          "ipconfig /all": `Windows IP Configuration

   Host Name . . . . . . . . . . . . : NOC-ADMIN-PC
   Primary Dns Suffix  . . . . . . . : corp.kyndryl.com
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : corp.kyndryl.com

Ethernet adapter vEthernet (Corporate LAN):

   Connection-specific DNS Suffix  . : corp.kyndryl.com
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection (7) I219-LM
   Physical Address. . . . . . . . . : 00-50-56-A1-2B-3C
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 10.10.10.85(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Tuesday, October 13, 2026 8:00:00 AM
   Lease Expires . . . . . . . . . . : Wednesday, October 14, 2026 8:00:00 AM
   Default Gateway . . . . . . . . . : 10.10.10.1
   DHCP Server . . . . . . . . . . . : 10.100.1.50
   DNS Servers . . . . . . . . . . . : 10.100.1.10
                                       10.100.1.11`,

          "ping 10.10.10.1": `Pinging 10.10.10.1 with 32 bytes of data:
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255

Ping statistics for 10.10.10.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms`,

          "ping 8.8.8.8": `Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117
Reply from 8.8.8.8: bytes=32 time=15ms TTL=117
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 14ms, Maximum = 15ms, Average = 14ms`,

          "tracert 8.8.8.8": `Tracing route to dns.google [8.8.8.8]
over a maximum of 30 hops:

  1    <1 ms    <1 ms    <1 ms  KYNDRYL-CORE-SW01 [10.10.10.1]
  2     1 ms     1 ms     1 ms  KYNDRYL-EDGE-RTR01 [10.10.1.1]
  3     2 ms     2 ms     2 ms  KYNDRYL-FW01 [198.51.100.1]
  4     8 ms     8 ms     9 ms  core2-chi.isp1.net [72.14.214.1]
  5    12 ms    12 ms    12 ms  142.250.224.1
  6    14 ms    14 ms    15 ms  dns.google [8.8.8.8]

Trace complete.`,

          "nslookup portal.kyndryl.com": `Server:  dc01.corp.kyndryl.com
Address:  10.100.1.10

Non-authoritative answer:
Name:    portal.kyndryl.com
Address:  10.100.25.105
Aliases:  intranet.kyndryl.com`,

          "arp -a": `Interface: 10.10.10.85 --- 0x12
  Internet Address      Physical Address      Type
  10.10.10.1            70-ea-1a-e4-33-00     dynamic (CORE-SW01 SVI)
  10.10.10.254          00-00-0c-07-ac-0a     dynamic (HSRP Virtual IP)
  10.10.10.86           00-50-56-a1-9f-12     dynamic (Peer Workstation)
  10.10.10.255          ff-ff-ff-ff-ff-ff     static`,

          "netstat -ano": `Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    10.10.10.85:49821      52.96.166.130:443      ESTABLISHED     4812
  TCP    10.10.10.85:51221      13.107.42.16:443       ESTABLISHED     4812
  TCP    10.10.10.85:58900      10.100.1.10:88         ESTABLISHED     824
  UDP    10.10.10.85:61204      10.100.1.10:53                         1102`,

          "curl -I https://portal.kyndryl.com": `HTTP/2 200 
content-type: text/html; charset=utf-8
server: Kyndryl-Cloud-Edge/2.4
date: Tue, 13 Oct 2026 18:25:00 GMT
strict-transport-security: max-age=31536000; includeSubDomains
x-frame-options: DENY
x-content-type-options: nosniff
content-length: 48921`,

          "route print": `===========================================================================
IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0       10.10.10.1     10.10.10.85      25
       10.10.10.0    255.255.255.0         On-link      10.10.10.85     281
      10.10.10.85  255.255.255.255         On-link      10.10.10.85     281
     10.10.10.255  255.255.255.255         On-link      10.10.10.85     281
        127.0.0.1  255.255.255.255         On-link        127.0.0.1     331
===========================================================================`
        }
      }
    };

    let activeDeviceId = "core-sw";
    const terminalSessionBuffers = {};
    const commandHistories = { "core-sw": [], "acc-sw": [], "edge-rtr": [], "fw": [], "wlc": [], "host-pc": [] };
    const historyIndices = { "core-sw": -1, "acc-sw": -1, "edge-rtr": -1, "fw": -1, "wlc": -1, "host-pc": -1 };

    function initTerminalUI() {
      // Initialize buffers with welcome banners
      for (const devId in deviceConfigs) {
        terminalSessionBuffers[devId] = `<div class="terminal-output">${deviceConfigs[devId].banner}</div>`;
      }
      renderActiveDeviceUI();
    }

    function switchDevice(devId) {
      if (!deviceConfigs[devId]) return;
      
      // Save current terminal body
      terminalSessionBuffers[activeDeviceId] = document.getElementById('termBody').innerHTML;

      // Update active ID
      activeDeviceId = devId;
      
      renderActiveDeviceUI();
    }

    function renderActiveDeviceUI() {
      const dev = deviceConfigs[activeDeviceId];

      // Update Device buttons
      document.querySelectorAll('.device-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById(`devBtn-${activeDeviceId}`);
      if (activeBtn) activeBtn.classList.add('active');

      // Update Topology Nodes
      document.querySelectorAll('.topo-node').forEach(node => node.classList.remove('active'));
      const activeTopo = document.getElementById(`topoNode-${activeDeviceId}`);
      if (activeTopo) activeTopo.classList.add('active');

      // Update Window Header
      document.getElementById('terminalTitle').innerText = dev.title;
      document.getElementById('terminalBadge').innerText = dev.badge;

      // Update Prompt
      const promptEl = document.getElementById('terminalPrompt');
      promptEl.innerText = dev.prompt;
      promptEl.style.color = dev.promptColor;

      // Update Presets
      const presetsEl = document.getElementById('terminalPresets');
      presetsEl.innerHTML = "";
      dev.presets.forEach(p => {
        const btn = document.createElement('button');
        btn.className = "btn-sm";
        btn.innerText = p.label;
        btn.onclick = () => runPreset(p.cmd);
        presetsEl.appendChild(btn);
      });

      // Restore terminal output
      const termBody = document.getElementById('termBody');
      termBody.innerHTML = terminalSessionBuffers[activeDeviceId] || `<div class="terminal-output">${dev.banner}</div>`;
      termBody.scrollTop = termBody.scrollHeight;

      // Focus input
      const inputEl = document.getElementById('termInput');
      inputEl.value = "";
      inputEl.placeholder = activeDeviceId === 'host-pc' ? "Type PowerShell command (e.g. ipconfig /all, ping, tracert)..." : "Type Cisco command (e.g. show ip int br, show ip route)...";
      inputEl.focus();
    }

    function executeCurrentInput() {
      const input = document.getElementById('termInput');
      const rawCmd = input.value.trim();
      if (!rawCmd) return;

      // Record in history
      const history = commandHistories[activeDeviceId];
      history.push(rawCmd);
      historyIndices[activeDeviceId] = history.length;

      printTerminalCommand(rawCmd);
      input.value = "";
    }

    function handleTerminalKey(e) {
      const history = commandHistories[activeDeviceId];
      if (e.key === 'Enter') {
        executeCurrentInput();
      } else if (e.key === 'ArrowUp') {
        if (history.length > 0 && historyIndices[activeDeviceId] > 0) {
          historyIndices[activeDeviceId]--;
          document.getElementById('termInput').value = history[historyIndices[activeDeviceId]];
        }
      } else if (e.key === 'ArrowDown') {
        if (historyIndices[activeDeviceId] < history.length - 1) {
          historyIndices[activeDeviceId]++;
          document.getElementById('termInput').value = history[historyIndices[activeDeviceId]];
        } else {
          historyIndices[activeDeviceId] = history.length;
          document.getElementById('termInput').value = "";
        }
      }
    }

    function runPreset(cmd) {
      printTerminalCommand(cmd);
    }

    function printTerminalCommand(cmd) {
      const term = document.getElementById('termBody');
      const dev = deviceConfigs[activeDeviceId];
      const lower = cmd.toLowerCase().trim();

      if (lower === 'clear' || lower === 'cls') {
        term.innerHTML = "";
        terminalSessionBuffers[activeDeviceId] = "";
        return;
      }

      let response = dev.commands[lower];

      // Fuzzy shortcut resolution
      if (!response) {
        for (let key in dev.commands) {
          if (key === lower) {
            response = dev.commands[key];
            break;
          }
          // Handle common Cisco abbreviations: sh -> show, int -> interface, br -> brief, neigh -> neighbor
          let normalizedKey = key.replace(/interface/g, 'int').replace(/brief/g, 'br').replace(/neighbor/g, 'neigh').replace(/show/g, 'sh');
          let normalizedInput = lower.replace(/interface/g, 'int').replace(/brief/g, 'br').replace(/neighbor/g, 'neigh').replace(/show/g, 'sh');
          if (normalizedKey === normalizedInput || key.startsWith(lower) || normalizedKey.startsWith(normalizedInput)) {
            response = dev.commands[key];
            break;
          }
        }
      }

      if (!response) {
        if (activeDeviceId === 'host-pc') {
          response = `'${cmd}' is not recognized as the name of a cmdlet, function, script file, or operable program. Type 'help' to see available commands.`;
        } else if (activeDeviceId === 'fw') {
          response = `% [ERROR] Command '${cmd}' not recognized in current context. Type 'help' for valid ASA commands.`;
        } else {
          response = `% Invalid command: "${cmd}". Type 'help' to see valid commands for ${dev.name}.`;
        }
      }

      const block = document.createElement('div');
      block.innerHTML = `
        <div style="color: #ffffff; margin-top: 10px; font-weight:600;">
          <span style="color: ${dev.promptColor};">${dev.prompt}</span> <span style="color: #38bdf8;">${cmd}</span>
        </div>
        <div class="terminal-output">${response}</div>
      `;
      term.appendChild(block);
      term.scrollTop = term.scrollHeight;
      terminalSessionBuffers[activeDeviceId] = term.innerHTML;
    }
