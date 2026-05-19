HEAD
# CodeAlpha Basic Network Sniffer



&#x20;CodeAlpha\_BasicNetworkSniffer



A Python-based network packet sniffer developed for the CodeAlpha Cybersecurity Internship. This tool captures live network traffic, parses packet headers (IP, TCP/UDP), and extracts payload data for security analysis.



&#x20;Features

\- Captures real-time packets using scapy.

\- Parses Layer 3 (IP) source and destination addresses.

\- Identifies Layer 4 (TCP/UDP) protocols.

\- Extracts and decodes raw packet payloads into human-readable text.



&#x20;Prerequisites

\- Python 3.x

\- scapy library



&#x20;Installation



1\. Clone this repository:

&#x20;  bash

&#x20;  git clone \[https://github.com/YOUR\_USERNAME/CodeAlpha\_BasicNetworkSniffer.git](https://github.com/YOUR\_USERNAME/CodeAlpha\_BasicNetworkSniffer.git)

&#x20;  cd CodeAlpha\_BasicNetworkSniffer

# CodeAlpha_Basic_Network_Sniffer-

## Introduction

You can't defend what you can't see. In cybersecurity, having complete visibility into your network traffic is the difference between stopping an attack and reading about your company's data breach in the news.

Developed during my cybersecurity internship at **Code Alpha**, this project is a practical, hands-on build of a **Basic Network Sniffer**. Operating inside a modern Windows 11 environment, this Python-powered tool intercepts raw network frames and slices them open to reveal how data moves under the hood. By parsing essential components like Source/Destination IPs, protocols, and raw payloads, this sniffer shines a light on the hidden conversations happening across a local network.



##  Objectives

The goals for this project were straightforward but critical to mastering network security fundamentals:

* **Real-Time Capture:** Build a stable Python script that intercepts live network packets on the fly.
* **Protocol Decoding:** Pull apart network traffic to read and categorize core protocols like TCP, UDP, and ICMP.
* **Security Auditing:** Inspect packet payloads to spot dangerous, unencrypted cleartext data transmissions.
* **Environment Mastery:** Navigate and configure low-level network drivers (`Npcap`) to bypass security restrictions on Windows 11.
* **Professional Delivery:** Document and publish the project using clean version control standards that match industry expectations.



##  Tools Used

Building this required a mix of low-level system access, a robust development environment, and clean version control:

* **Command Prompt (CMD) / PowerShell (Admin Mode):** Windows 11 doesn't just let any program spy on network traffic. Running CMD as an Administrator was essential to grant the Python script permission to force the Network Interface Card (NIC) into promiscuous mode.
* **Visual Studio 2022:** My primary workspace. VS 2022 provided a fantastic Python environment, seamless debugging tools, and syntax highlighting that made managing the `scapy` library straightforward and efficient.
* **GitHub:** The command center for version control. Used to track code changes, manage project history, and host this public repository (`CodeAlpha_ProjectName`) for peer review and submission.



##  Skills Gained

Stepping out of theory and into raw packet capturing helped me develop several crucial security skills:

* **Packet-Level Analysis:** I moved past looking at network diagrams and actually saw the OSI and TCP/IP models in action, watching how data encapsulates layer by layer.
* **Python for Cyber Automation:** Learned how to utilize the `scapy` library to interact directly with hardware-level network traffic.
* **Windows System Troubleshooting:** Figured out how to handle Windows 11 security constraints, User Account Control (UAC), and driver dependencies without breaking the OS.
* **The Defensive Mindset:** Seeing how easily an attacker can sniff unencrypted traffic made me realize why strong encryption protocols (like HTTPS or SSH) are non-negotiable.



##  Importance to an Organisation

A network sniffer isn't just a fun project; it represents a foundational pillar of corporate security and infrastructure health:

* **Threat Hunting & Incident Response:** Security teams use sniffers to catch malicious anomalies early like malware attempting to whisper back to a Command-and-Control (C2) server or unauthorized data exfiltration.
* **Vulnerability Management:** Sniffers act as an internal audit tool, ensuring employees and apps aren't accidentally sending sensitive data or corporate credentials over the network in plaintext.
* **Keeping the Lights On:** When things break, network admins rely on packet-level analysis to pinpoint routing loops, packet loss, or configuration errors, saving the company hours of costly downtime.



## Steps

* 1. Installed  Scapy on my Wondows 11 by running the following command:  pip install scapy

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1f146cb0-5d48-4c53-a3e7-5d3fbe8ca0c9" />

* 2. On cmd , I created the folder named "CodeAlpha_BasicNetworkSniffer" using the command : mkdir CodeAlpha_BasicNetworkSniffer
  
* 3. Inside the CodeAlpha_BasicNetworkSniffer, i created anothor folder names sniffer.py using visual studio and wrote the packet capture code using python

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/38ec0ee1-d9a8-4046-8044-2452ae04c417" />

* 4. To capture a live traffic, I had to ping google.com using the ping command
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/59e82723-c92b-427b-8fc8-1dda718875f4" />

* 5. I then ran the cmd as an administrator and navigated to the CodeAlpa_BasicNetworkSniffer to run the sniffer.py by using the command python sniffer.py

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ed3a3893-4d40-40e0-8b18-17fcf3e74547" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/90f4f4c2-30d2-4090-9f2f-86f5cc92ac48" />


## Executive Summary


This project successfully demonstrates how to design, configure, and execute a localized Basic Network Sniffer on a Windows 11 platform. By bridging Python with the scapy packet manipulation engine and the Npcap driver, the application successfully intercepted live network traffic, isolated key transport protocols (TCP, UDP, ICMP), and displayed data payloads in real time.

All code assets have been securely deployed via GitHub in accordance with Code Alpha's strict internship standards, with a live presentation published to LinkedIn for professional validation. Ultimately, this project underlines a core truth in cybersecurity: packet-level visibility is an organization's first line of defense in identifying unencrypted vulnerabilities and neutralizing advanced digital threats.




>>>>>>> be0077d78eeb9c72ecd170166beb27e2797cb034

