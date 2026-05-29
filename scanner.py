import nmap
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def scan_network(target):
    nm = nmap.PortScanner()
    print(f"{Fore.CYAN}🔍 Scanning target: {target}{Style.RESET_ALL}")
    nm.scan(hosts=target, arguments='-sV')

    for host in nm.all_hosts():
        print(f"\n{Fore.YELLOW}Host: {host} ({nm[host].hostname()}){Style.RESET_ALL}")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                service = nm[host][proto][port]
                # Highlight open ports in green, closed in red
                if service['state'] == 'open':
                    color = Fore.GREEN
                else:
                    color = Fore.RED
                print(f"Port: {port}\tState: {color}{service['state']}{Style.RESET_ALL}\tService: {service['name']}")

if __name__ == "__main__":
    target_subnet = "192.168.1.0/24"
    scan_network(target_subnet)
