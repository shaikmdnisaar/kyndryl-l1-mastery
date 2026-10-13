# 🚀 Kyndryl L1 Network Operations Center — CCNA v1.1 Mastery Platform

[![Deploy to GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Deployment-success?style=for-the-badge&logo=github)](https://shaikmdnisaar.github.io/kyndryl-l1-mastery/)
[![Cisco CCNA v1.1](https://img.shields.io/badge/Cisco-CCNA%20200--301%20v1.1-blue?style=for-the-badge&logo=cisco)](https://www.linkedin.com/learning/cisco-certified-network-associate-ccna-v1-1-200-301-cert-prep/diving-into-the-course?u=76281980)
[![Kyndryl L1 NOC Ready](https://img.shields.io/badge/Kyndryl-L1%20Network%20Engineer-red?style=for-the-badge)](https://shaikmdnisaar.github.io/kyndryl-l1-mastery/)

An interactive, enterprise-grade Network Operations Center (NOC) training platform and CCNA v1.1 tracker tailored specifically for the **L1 Network Engineer role at Kyndryl**.

🔗 **Live Application URL:** **[https://shaikmdnisaar.github.io/kyndryl-l1-mastery/](https://shaikmdnisaar.github.io/kyndryl-l1-mastery/)**

---

## 🌟 Key Features

### 1. 🎬 CCNA v1.1 Course Tracker (201 Lessons)
- Complete coverage of Kevin Wallace's **Cisco Certified Network Associate (CCNA) v1.1 (200-301)** curriculum.
- **Direct One-Click Watch Links** with Toronto Public Library SSO tokens (`?u=76281980`).
- **Interactive Checkboxes** with persistent browser progress tracking (`localStorage`).
- **Module Collapsing/Expanding** and full-text keyword search across all 201 video lessons.

### 2. ⭐ Kyndryl L1 Priority Track (66 High-Yield Lessons)
- Instant toggle filter that reduces study overhead by ~65% while covering 100% of L1 NOC alert scenarios:
  - Switching loops & Spanning Tree (STP/RSTP/PortFast/BPDU Guard)
  - 802.1Q Trunks, Native VLANs & Voice VLANs
  - DHCP DORA & `ip helper-address` relay
  - OSPF neighbor adjacencies, MTU mismatches & DR/BDR elections
  - HSRP Gateway Redundancy & Virtual IPs
  - Port Security & Err-Disabled recovery
  - IPv4 Subnetting & Wildcard Masks

### 3. 💻 Multi-Device Interactive Cisco Terminal Simulator
Simulate troubleshooting across an end-to-end enterprise network topology with authentic CLI responses:
- **🔀 Core Switch (`KYNDRYL-CORE-SW01`):** Catalyst 9300-24T (IOS-XE 17.9.4a) — Inter-VLAN, HSRP, OSPF, STP
- **🔌 Access Switch (`KYNDRYL-ACC-SW02`):** Catalyst 9200L-48P (IOS-XE 17.9.3) — PoE+ power draw, 802.1X, Port Security
- **🌐 WAN Edge Router (`KYNDRYL-EDGE-RTR01`):** Cisco ISR 4451-X (IOS-XE 17.6.5) — BGP multi-homing, NAT Overload, Azure IPsec VPN
- **🛡️ Perimeter Firewall (`KYNDRYL-FW01`):** Cisco ASA 5516-X (Software 9.16(2)) — Stateful inspection, DMZ NAT, Failover HA
- **📶 Wireless Controller (`KYNDRYL-WLC01`):** Catalyst 9800-CL (IOS-XE 17.9.2) — SSIDs, CAPWAP APs, CleanAir RF
- **💻 Diagnostic Host PC (`NOC-ADMIN-PC`):** Windows 11 / PowerShell 7 — `ipconfig /all`, `ping`, `tracert`, `nslookup`, `arp -a`, `netstat`

Features:
- **Clickable Data Path Topology Pipeline Strip**
- **Dynamic Quick Presets** that swap automatically per device
- **Independent Scrollback Buffers** for each node
- **Command History Recall** using Up/Down arrow keys (`↑` / `↓`)
- **Fuzzy Shortcut Resolution** (`sh ip int br`, `sh run`, `sh vlan`, etc.)

### 4. ⚡ Mental Subnetting Speed Trainer
- Random IPv4 CIDR generator (`/25` through `/30`).
- Tests mental calculation of Network ID, First Usable IP, Last Usable IP, Broadcast Address, and Host Count.
- Instant validation and streak tracking for sub-10-second NOC triage speed.

### 5. 🚨 Kyndryl Incident War Room & SOP Playbooks
- Real-world triage workflows with diagnostic sequences:
  - **P1 Critical (INC098231):** Branch Office STP Loop & High CPU Storm
  - **P2 High (INC098402):** VLAN 30 APIPA Address Failure & DHCP Helper Relay
  - **P3 Medium (INC098555):** Conference Room Port Security `err-disable` Violation
- Copyable **Kyndryl ServiceNow Worklog Templates** ready for shift handover.

### 6. 📖 Top 25 Cisco CLI Reference
- Categorized cheatsheet with one-click clipboard copy for interfaces, switching, routing, NAT, security, and diagnostics.

### 7. 🎯 Kyndryl L1 Technical Interview Flashcards
- High-yield scenario questions covering duplex mismatches, DHCP DORA, STP BPDU Guard, routing tie-breakers, and OSPF ExStart states.

---

## 🔑 Toronto Public Library (TPL) Access Quick Reference

| Parameter | Value |
| :--- | :--- |
| **Partner Portal** | Toronto Public Library (`tpl`) |
| **Organization ID** | `76281980` |
| **Access Card Number** | `29100701939436` |
| **PIN** | `1234` |
| **Direct Login URL** | [LinkedIn Learning TPL Auth](https://www.linkedin.com/checkpoint/enterprise/login/76281980?pathWildcard=76281980&application=learning) |

---

## 🛠️ Tech Stack & Architecture
- **Frontend:** Vanilla HTML5, CSS3 (NOC Glassmorphism & Plus Jakarta Sans / JetBrains Mono typography), Vanilla ES6 JavaScript.
- **Storage:** Client-side persistent state via `localStorage`.
- **Hosting:** GitHub Pages via branch `main`.
