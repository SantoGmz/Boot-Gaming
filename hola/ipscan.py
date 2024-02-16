#pip install scapy

import scapy.all as scapy

def escanear(ip):
    try:
        scapy.arping(ip)
    except Exception as e:
        print(f"Se produjo un error: {e}")

escanear("192.168.0.1/24")