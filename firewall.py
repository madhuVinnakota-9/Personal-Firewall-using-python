
from scapy.all import *
from datetime import datetime

BLOCKED_IPS = [
	"192.168.100.100"
]
BLOCKED_PORTS = [
	21,
	23
]
def log_event(message):
	with open("logs.txt", "a") as log:
		log.write(
			f"{datetime.now()} : {message}\n"
		)
def firewall(packet):
	if packet.haslayer(IP):
		src = packet[IP].src
		dst = packet[IP].dst
		
		if src in BLOCKED_IPS:
			msg = f"BLOCKED IP {src}"
			
			print(msg)
			
			log_event(msg)
			
			return
		if packet.haslayer(TCP):
			port = packet[TCP].dport
			
			if port in BLOCKED_PORTS:
				msg = f"BLOCKED PORT {port}"
				
				print(msg)
				
				log_event(msg)
				
				return
		msg = f"ALLOWED {src} -> {dst}"
		
		print(msg)
		
		log_event(msg)
print("FIREWALL ACTIVE")
	
sniff(
		prn=firewall,
		store=False
)

