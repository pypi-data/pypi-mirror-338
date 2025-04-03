from InquirerPy import prompt
from colorama import Fore

from tools.nmap import GO_BACK
import subprocess

import state
GOBUSTER = "Gobuster"

COMMON = "Common"
MEDIUM = "Medium"
LARGE = "Large"
def gobuster_menu():
    questions = [
        {
            'type': 'list',
            'name': 'gobuster',
            'message': 'What would you like to do?',
            'choices': [
                COMMON,
                MEDIUM,
                LARGE,
                GO_BACK
            ]
        }
    ]
    answer = prompt(questions)
    return answer['gobuster']

def gobuster():
    while True:
        choice = gobuster_menu()

        if choice == COMMON:
            common()
        elif choice == MEDIUM:
            medium()
        elif choice == LARGE:
            large()
        elif choice == GO_BACK:
            return


def common():
    path = "/usr/share/wordlists/seclists/Discovery/Web-Content/common.txt"
    questions = [
        {
            'type': 'input',
            'name': 'url',
            'message': 'Enter url:',
        },
        {
            'type': 'input',
            'name': 'ext',
            'message': 'Enter extension:',
        }
    ]
    answer = prompt(questions)
    url = answer['url']
    ext = answer.get('ext')

    params = ['gobuster', 'dir', '-u', url, '-w', path, '-o', 'gobuster_common.txt']

    if ext:
        params.extend(ext.split(" "))

    print(Fore.GREEN, "Running common scan on", url)
    process = subprocess.Popen(params, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    state.processes.append({
        "name": "Full Scan",
        "process": process
    })

def medium():
    path = "/usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt"
    questions = [
        {
            'type': 'input',
            'name': 'url',
            'message': 'Enter url:',
        },
        {
            'type': 'input',
            'name': 'ext',
            'message': 'Enter extension:',
        }
    ]
    answer = prompt(questions)
    url = answer['url']
    ext = answer.get('ext')

    params = ['gobuster', 'dir', '-u', url, '-w', path, '-o', 'gobuster_common.txt']

    if ext:
        params.extend(ext.split(" "))

    print(Fore.GREEN, "Running medium scan on", url)
    process = subprocess.Popen(params, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    state.processes.append({
        "name": "Full Scan",
        "process": process
    })

def large():
    path = "/usr/share/wordlists/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt"
    questions = [
        {
            'type': 'input',
            'name': 'url',
            'message': 'Enter url:',
        },
        {
            'type': 'input',
            'name': 'ext',
            'message': 'Enter extension:',
        }
    ]
    answer = prompt(questions)
    url = answer['url']
    ext = answer.get('ext')

    params = ['gobuster', 'dir', '-u', url, '-w', path, '-o', 'gobuster_common.txt']

    if ext:
        params.extend(ext.split(" "))

    print(Fore.GREEN, "Running medium scan on", url)
    process = subprocess.Popen(params, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    state.processes.append({
        "name": "Full Scan",
        "process": process
    })