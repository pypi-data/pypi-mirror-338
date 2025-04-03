import ipaddress
import subprocess
from colorama import init, Fore
from InquirerPy import inquirer
from htbrecon import state

SUBDOMAINS = "Subdomains"

def subdomains():
    url = inquirer.text(message="Enter URL (e.g., http://target.htb):").execute()

    print(Fore.YELLOW + "[*] Creating dummy subdomains file for dry run filter test...")
    dummy_file = "/tmp/dummy_subdomains.txt"
    with open(dummy_file, 'w') as f:
        f.write("test\ntest2\ntest3\ntest4\n")
    print(Fore.GREEN + "[+] Dummy file written.")

    domain = url.split("//")[-1].strip("/")

    print(Fore.YELLOW + "[*] Running dry run ffuf to determine filter word count...")
    dry_params = [
        "ffuf",
        "-w", dummy_file,
        "-u", url,
        "-H", f"Host: FUZZ.{domain}"
    ]

    process = subprocess.Popen(dry_params, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    words = []
    for line in process.stdout:
        if line.strip() == "":
            continue
        splitted = line.split(" ")
        cleared = [x for x in splitted if x != '']
        if len(cleared) >= 7:
            words.append(cleared[6].replace(",", ""))

    if not words:
        print(Fore.RED + "[!] Could not detect filter word count. Check if ffuf output is correct.")
        return

    print(Fore.GREEN + f"[+] Using filter word count: -fw {words[0]}")

    with open("subdomains.txt", "w") as f:
        real_params = [
            "ffuf",
            "-w", "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt",
            "-u", url,
            "-H", f"Host: FUZZ.{domain}",
            "-fw", words[0]
        ]

        print(Fore.GREEN + f"[+] Running ffuf.")
        process = subprocess.Popen(real_params, stdout=f, stderr=subprocess.DEVNULL)

        state.processes.append({
            "name": "Subdomains",
            "process": process
        })