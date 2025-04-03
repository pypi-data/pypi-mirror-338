import ipaddress
import subprocess
from PyInquirer import prompt, Separator
from colorama import init, Fore, Style
import state
NMAP = "Nmap"

QUICK_SCAN = "Quick Scan"
FULL_SCAN = "Full Scan (fast)"
SPECIFIC_PORT_SCAN = "Specific Port Scan"
UDP_SCAN = "UDP Scan (slow)"
GO_BACK = "Go back"
def nmap_menu():
    questions = [
        {
            'type': 'list',
            'name': 'nmap_main_menu',
            'message': 'What would you like to do?',
            'choices': [
                QUICK_SCAN,
                FULL_SCAN,
                SPECIFIC_PORT_SCAN,
                UDP_SCAN,
                Separator(),
                GO_BACK
            ]
        }
    ]
    answer = prompt(questions)
    return answer['nmap_main_menu']

def nmap():
    while True:
        choice = nmap_menu()

        if choice == QUICK_SCAN:
            quick_scan()
        elif choice == FULL_SCAN:
            full_scan()
        elif choice == SPECIFIC_PORT_SCAN:
            specific_port_scan()
        elif choice == UDP_SCAN:
            print("UDP scan")
        elif choice == GO_BACK:
            return


def quick_scan():
    questions = [
        {
            'type': 'input',
            'name': 'ip',
            'message': 'Enter ip:',
        }
    ]
    answer = prompt(questions)
    ip = answer['ip']

    try:
        ipaddress.ip_address(ip)
    except:
        print(Fore.RED + f"Invalid IP address: {ip}")
        return

    print(Fore.GREEN+ f"Running quick scan on {ip}...")
    process = subprocess.Popen(
        ['nmap', '-sC', '-sV', '-oN', 'quick_scan.txt', ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    state.processes.append({
        "name": "Quick Scan",
        "process": process
    })

def full_scan():
    questions = [
        {
            'type': 'input',
            'name': 'ip',
            'message': 'Enter ip:',
        }
    ]
    answer = prompt(questions)
    ip = answer['ip']

    try:
        ipaddress.ip_address(ip)
    except:
        print(Fore.RED + f"Invalid IP address: {ip}")
        return

    print(Fore.GREEN+ f"Running full scan on {ip}...")
    process = subprocess.Popen(
        ['nmap', '-p-', '--min-rate=1000', 'full_scan.txt', ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    state.processes.append({
        "name": "Full Scan",
        "process": process
    })

def specific_port_scan():
    questions = [
        {
            'type': 'input',
            'name': 'ip',
            'message': 'Enter ip:',
        },
        {
            'type': 'input',
            'name': 'ports',
            'message': 'Enter comma separated ports:',
        }
    ]
    answer = prompt(questions)
    ip, ports = answer['ip'], answer['ports']

    try:
        ipaddress.ip_address(ip)
    except:
        print(Fore.RED + f"Invalid IP address: {ip}")
        return

    print(Fore.GREEN+ f"Running specific ports scan on {ip}...")
    process = subprocess.Popen(
        ['nmap', '-sC', '-sV', '-p', str(ports), '-oN', 'specific_port_scan.txt', ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    state.processes.append({
        "name": "Specific Port Scan",
        "process": process
    })