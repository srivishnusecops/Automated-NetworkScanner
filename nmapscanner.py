import subprocess
import os
from voice import talk

# Function to run nmap scan
def run_nmap(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e.stderr}")
        return None

# Function to check if file is created in the current directory
def check_file_created(filename):
    if os.path.exists(filename):
        print(f"File {filename} created successfully!")
    else:
        print(f"Error: {filename} not created!")

# Scan Definitions
def host_alive(target):
    talk("Performing host alive check")
    filename = 'nmap_hostalive_report.json'
    command = ['nmap', '-sn', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def ping_scan(target):
    talk("Performing Ping scan")
    filename = 'nmap_pingscan_report.json'
    command = ['nmap', '-Pn', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def syn_ping(target):
    talk("Performing syn ping")
    filename = 'nmap_synping_report.json'
    command = ['nmap', '-PS', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def syn_scan(target):
    talk("Performing syn scan")
    filename = 'nmap_synscan_report.json'
    command = ['nmap', '-sS', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def tcp_scan(target):
    talk("Performing tcp scan")
    filename = 'nmap_tcpscan_report.json'
    command = ['nmap', '-sT', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def udp_scan(target):
    talk("Performing udp scan")
    filename = 'nmap_udpscan_report.json'
    command = ['nmap', '-sU', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def tcp_ack_scan(target):
    talk("Performing tcp ack scan")
    filename = 'nmap_tcpack_scan.json'
    command = ['nmap', '-sA', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def fastscan(target):
    talk("Performing fastscan")
    filename = 'nmap_fastscan_report.json'
    command = ['nmap', '-F', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    print(result)

def topscan(target):
    talk("Performing top scan")
    filename = 'nmap_topscan_report.json'
    command = ['nmap', '--top-ports', '50', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def syn_powerscan(target):
    talk("performing syn_powerscan")
    filename = 'nmap_synpowerscan.json'
    command = ['nmap', '-sS', '-sV', '-O', '-p-', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def null_powerscan(target):
    talk("Performing null powerscan")
    filename = 'nmap_nullpowerscan.json'
    command = ['nmap', '-sN', '-sV', '-O', '-p-', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def xmas_powerscan(target):
    talk("performing xmas powerscan")
    filename = 'nmap_xmaspowerscan.json'
    command = ['nmap', '-sX', '-sV', '-O', '-p-', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def ip_spoof_synpowerscan(target):
    talk("Performing syn powerscan with IP Spoofing")
    filename = 'nmap_ip_spoof_synpowerscan.json'
    command = ['nmap', '-D', 'RND:50', '-sS', '-e', 'eth0', '-A', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def vuln_scan_powerscan(target):
    talk("Performing vulnerability scan")
    filename = 'nmap_vuln_scan_powerscan.json'
    command = ['nmap', '--script=vuln', '-sS', '-A', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def cookie_powerscan(target):
    talk("Performing cookie powerscan")
    filename = 'nmap_cookie_powerscan.json'
    command = ['nmap', '-sZ', '-sS', '-A', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def protocol_powerscan(target):
    talk("Performing protocol analyze powerscan")
    filename = 'nmap_protocol_powerscan.json'
    command = ['nmap', '-sO', '-sS', '-A', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result

def default_script_powerscan(target):
    talk("Performing default script powerscan")
    filename = 'nmap_default_script_powerscan.json'
    command = ['nmap', '--script', 'default,safe', '--script=vuln', '--version-all', '-sS', '-oJ', filename, target]
    result = run_nmap(command)
    check_file_created(filename)
    return result


# Main Program: Command Selection
commands_list = """1. host_alive scan
2. ping_scan
3. syn_ping scan
4. syn scan
5. tcp scan
6. udp scan
7. tcp_ack scan
8. fast scan
9. top scan
10. syn_powerscan
11. null_powerscan
12. xmas_powerscan
13. ip_spoof_synpowerscan
14. vuln_scan_powerscan
15. cookie_powerscan
16. protocol_powerscan
17. default_script_powerscan"""

print(commands_list)

# Input Target IP
talk("Enter the target ip address")
target = input("Enter the target IP: ")

# Input choice and perform the corresponding scan
talk("enter the choice number")
choice = input("Enter the scan type (number): ")

if choice == '1':
    print(host_alive(target))
elif choice == '2':
    print(ping_scan(target))
elif choice == '3':
    print(syn_ping(target))
elif choice == '4':
    print(syn_scan(target))
elif choice == '5':
    print(tcp_scan(target))
elif choice == '6':
    print(udp_scan(target))
elif choice == '7':
    print(tcp_ack_scan(target))
elif choice == '8':
    print(fastscan(target))
elif choice == '9':
    print(topscan(target))
elif choice == '10':
    print(syn_powerscan(target))
elif choice == '11':
    print(null_powerscan(target))
elif choice == '12':
    print(xmas_powerscan(target))
elif choice == '13':
    print(ip_spoof_synpowerscan(target))
elif choice == '14':
    print(vuln_scan_powerscan(target))
elif choice == '15':
    print(cookie_powerscan(target))
elif choice == '16':
    print(protocol_powerscan(target))
elif choice == '17':
    print(default_script_powerscan(target))
else:
    print("Invalid choice.")
