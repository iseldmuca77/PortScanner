import socket

def scan(targets, port):
    print("\n" + " Duke Startuar Skanimin Per: " + str(targets))
    for port in range(1,port):
        scan_port(targets,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+]" + str(port) + " Port E Hapur")
        sock.close()
    except:
        pass
        
targets = input("[*] Vendosni Targets Per Te Skanuar(Ndaji me ,): ")
ports = int(input("[*] Sa Port Doni Te Skanoni: "))
if ',' in targets:
    print("[*] Duke Skanuar Shume Targets")
    for ip_addr in targets.split(','):  
            scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports)
