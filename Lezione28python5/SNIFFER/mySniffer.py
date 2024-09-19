from scapy.all import *
from scapy.layers.inet import IP,TCP
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse
from datetime import datetime
import csv



iPkt=0

def process_pkt(pkt):
    global iPkt
    iPkt+=1
    if pkt.haslayer(TCP) and (pkt[TCP].dport in [80, 443] or pkt[TCP].sport in [80, 443]):        
        dataOra=datetime.now().strftime("%Y-%m-%d %H: %M:%S")
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
        tcp_src=pkt[TCP].sport
        tcp_dst=pkt[TCP].dport
        host= ""

        
        if pkt.haslayer(HTTPRequest):
            if pkt[HTTPRequest].Host:
             host = pkt[HTTPRequest].Host.decode()
                
        
        if 443 in [tcp_src,tcp_dst]:
            protocol= "HTTPS"
        else:
           protocol= "HTTP"


        with open("file.csv","a", newline="") as file:
           writer=csv.writer(file)
           writer.writerow([f"{dataOra}|,{ip_src}|,{ip_dst}|,{tcp_src}|,{tcp_dst},{host}"])




with open("file.csv","w", newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["dataOra|","ip_src|","ip_dst|","tcp_src|","tcp_dst|","host"])

           
           


sniff(iface="eth0", filter="tcp", prn=process_pkt)





