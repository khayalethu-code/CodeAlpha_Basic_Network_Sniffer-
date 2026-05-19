from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    """
    This function is called for every packet that is captured.
    It extracts and displays IP addresses, protocols, and payloads.
    """
    # 1. Check if the packet contains an IP Layer (Network Layer)
    if packet.haslayer(IP):
        ip_src = packet[IP].src      # Source IP Address
        ip_dst = packet[IP].dst      # Destination IP Address
        proto = packet[IP].proto     # Protocol Number (e.g., 6 for TCP, 17 for UDP)

        # Convert protocol numbers to human-readable strings
        protocol_name = "Other"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"

        print(f"\n[+] Packet Captured: {ip_src} ----({protocol_name})----> {ip_dst}")

        # 2. Check if the packet has a Raw Payload (Data Layer)
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            # Print the first 100 characters of the payload, filtering out unreadable bytes
            print(f"    [Payload Data]: {str(payload)[:100]}")

def main():
    print("="*60)
    print("        CODE ALPHA - BASIC NETWORK SNIFFER (WINDOWS 11)        ")
    print("="*60)
    print("[*] Initializing sniffer... Press Ctrl+C to stop.")
    
    # Start sniffing. 
    # store=False keeps Scapy from loading every packet into RAM (prevents crashes).
    # prn sends every captured packet to our callback function.
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()