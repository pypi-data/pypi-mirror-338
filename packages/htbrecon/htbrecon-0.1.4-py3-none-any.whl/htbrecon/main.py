from InquirerPy import prompt
from colorama import init, Fore
import sys
from htbrecon import banner
from htbrecon.tools.gobuster import GOBUSTER, gobuster

from htbrecon.tools.hosts import add_to_etc_hosts, ADD_ETC_HOSTS
from htbrecon.tools.nmap import nmap, NMAP
from htbrecon import state
from htbrecon.tools.subdomains import SUBDOMAINS, subdomains

init(autoreset=True)

CONFIGURE = 'Configure'
EXIT = "Exit"
def main_menu():
    questions = [
        {
            'type': 'list',
            'name': 'main_choice',
            'message': "Please select an option:",
            'choices': [
                state.STATUS,
                ADD_ETC_HOSTS,
                NMAP,
                GOBUSTER,
                SUBDOMAINS,
                EXIT
            ]
        }
    ]
    answer = prompt(questions)
    return answer['main_choice']

def run():
    banner.display()
    while True:
        try:
            choice = main_menu()
            if choice == ADD_ETC_HOSTS:
                add_to_etc_hosts()
            if choice == NMAP:
                nmap()
            if choice == state.STATUS:
                state.check_status()
            if choice == GOBUSTER:
                gobuster()
            if choice == SUBDOMAINS:
                subdomains()
            elif choice == 'Exit':
                print(Fore.RED + 'Exiting. Goodbye!')
                sys.exit()
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")





if __name__ == '__main__':
    run()