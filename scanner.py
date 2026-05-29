import nmap

def scan_network(target):
    nm = nmap.PortScanner()
    print(f"🔍 Scanning target: {target}")
    nm.scan(hosts=target, arguments='-sV')

    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                service = nm[host][proto][port]
                print(f"Port: {port}\tState: {service['state']}\tService: {service['name']}")

if __name__ == "__main__":
    # Example: scan local subnet
    target_subnet = "192.168.1.0/24"
    scan_network(target_subnet)
