from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse





def process_pkt(pkt):
    global iPkt
    print(f"Ho ricevutto un package  {iPkt} lungo {pkt[IP].len}")


sniff(iface="en0", filter="tcp", prn=process_pkt)


