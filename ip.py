import ipaddress

# Beispiel-IP-Adressen
ip_addresses = ['192.168.0.1', '10.0.0.1', '8.8.8.8', '2001:0db8:85a3:0000:0000:8a2e:0370:7334']

# Überprüfen, ob jede IP-Adresse gültig ist und grundlegende Informationen ausgeben
for ip in ip_addresses:
    try:
        ip_obj = ipaddress.ip_address(ip)
        print(f"Die IP-Adresse {ip} ist gültig.")
        print(f"Version: IPv{ip_obj.version}")  # IPv4 oder IPv6
        print(f"Netzwerk: {ip_obj.is_private}")  # Private oder öffentliche IP
        print(f"Reverse-DNS: {ip_obj.reverse_pointer}")  # Reverse DNS-Lookup
        print("---------------------------")
    except ValueError:
        print(f"Die IP-Adresse {ip} ist ungültig.")
        print("---------------------------")
