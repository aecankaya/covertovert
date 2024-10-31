from scapy.all import ICMP, sniff

# Implement your ICMP receiver here

def receive_icmp(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 8: 
        packet.show()

# Wait first ICMP packet
if __name__ == "__main__":
    sniff(filter="icmp", prn=receive_icmp, count=1)
