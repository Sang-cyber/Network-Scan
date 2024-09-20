from scapy.all import srp  # type: ignore
from scapy.layers.l2 import Ether, ARP  # type: ignore

target_ip = "192.168.1.1/24"

print("Started scanning...")

# Create ARP packet
arp = ARP(pdst=target_ip)

# Create the Ether broadcast packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Stack them
packet = ether / arp

# Send the packet and get the response
result = srp(packet, timeout=3, verbose=0)[0]

# A list of clients
clients = []

for sent, received in result:
    # For each response, append IP and MAC address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# Print clients
print("Available devices in the network:")
print("IP" + " "*18 + "MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
