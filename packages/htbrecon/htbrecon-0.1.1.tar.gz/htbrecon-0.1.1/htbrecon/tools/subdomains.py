import ipaddress
import subprocess

from colorama import init, Fore, Style
from PyInquirer import prompt, Separator
import state
SUBDOMAINS = "Subdomains"

def subdomains():
    questions = [
        {
            'type': 'input',
            'name': 'url',
            'message': 'Enter url:',
        }
    ]
    answers = prompt(questions)
    url = answers['url']

    print(Fore.YELLOW + "Creating dummy subdomains file to dry run for specifying filters.")
    with open("/tmp/dummy_subdomains.txt", 'w') as f:
        f.write("test\ntest2\ntest3\ntest4\n")
    print(Fore.GREEN + "Done")

    print(Fore.YELLOW + "Dry run for specific filter...")
    domain = url.split("//")[-1]
    params = ["ffuf", '-w', '/tmp/dummy_subdomains.txt', '-u', url, '-H', f'Host: FUZZ.{domain}']
    process = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    words = []
    for line in process.stdout:
        if line == '\n': continue
        splitted = line.split(" ")
        cleared = [x for x in splitted if x != '']
        words.append(cleared[6].replace(",", ""))

    # might be wrong, but I am leaving this here for now
    params = ["ffuf",
              '-w', '/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt',
              '-u', url,
              '-H', f'Host: FUZZ.{domain}',
              '-fw', words[0]
              ]
    print(Fore.GREEN + f"Running ffuf with params: {params}")
    process = subprocess.Popen( params, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    state.processes.append({
        "name": "Subdomains",
        "process": process
    })