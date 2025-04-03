import ipaddress
from colorama import init, Fore, Style
from PyInquirer import prompt, Separator

ADD_ETC_HOSTS = "Add to /etc/hosts"

def add_to_etc_hosts():
    questions = [
        {
            'type': 'input',
            'name': 'ip',
            'message': 'Enter ip:',
        },
        {
            'type': 'input',
            'name': 'domain',
            'message': 'Enter domain name',
        }
    ]
    answers = prompt(questions)
    ip, domain = answers['ip'], answers['domain']
    try:
        ipaddress.ip_address(ip)
    except:
        print(Fore.RED + f"Invalid IP address: {ip}")
        return

    print(Fore.YELLOW + f"Adding {ip} {domain} to /etc/hosts...")

    with open('/etc/hosts', 'r') as f:
        lines = f.readlines()

    print("Checking if entry already exists...")
    updated = False
    for i, line in enumerate(lines):
        if ip in line and domain in line:
            line = line.replace('\n', '')
            print(Fore.YELLOW + f"Entry already exists: {line}, nothing to do...")
            return

        if ip in line and not domain in line:
            print(Fore.YELLOW + f"Entry already exists with different domain: {line}, adding missing...")
            line = line.replace('\n', '')
            lines[i] = line + f" {domain}\n"
            updated = True
            break

    if not updated:
        lines.append(f"{ip} {domain}\n")

    with open("/etc/hosts", 'w') as f:
        f.writelines(lines)

    print(Fore.GREEN + f"Added {ip} {domain} to /etc/hosts.")