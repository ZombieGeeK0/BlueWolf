from colorama import Fore, Style
import os, socket, sys

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

class color:
    RED = Fore.RED + Style.BRIGHT
    BLUE = Fore.BLUE + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def reset_color():
    print(color.RESET)

def exit():
    reset_color()
    clear()
    sys.exit()

def ret():
    choice = input(color.WHITE + '[&]: Press any key to return to the menu: ')
    main()

def error():
    print(color.WHITE + '\n[&]: Error: Comand not found')
    ret()

def get_ip():
    print(color.WHITE + '\n[&] Your IP adress is: ' + color.BLUE + ip)
    ret()

def change_ip():
    options = '''
[00]: Salir
[01]: Volver al menú
[02]: Change IP in Linux
[02]: Change IP in Windows
'''
    print(color.WHITE + '\n' + options)

    print(color.BLUE + f'┌── <{hostname}@BlueWolf> ─ [~]')
    choice = input('└──╼ $ ')

    if choice == '00':
        exit()

    elif choice == '01':
        ret()

    elif choice == '03' and os.name == 'nt':
        options = '''
[00]: Exit the program
[01]: Back to the menu
[02]: Change IP with netsh
[03]: Change IP with ipconfig
'''
    print(color.WHITE + '\n' + options)

    print(color.BLUE + f'┌── <{hostname}@BlueWolf> ─ [~]')
    choice = input('└──╼ $ ')

    if choice == '00':
        exit()

    elif choice == '01':
        ret()

    elif choice == '02':
        pass
        #netsh
    
    elif choice == '03':
        print(color.WHITE + '\n[&]: Changing IP...\n')
        os.system('ipconfig /release & ipconfig /renew')
        print(color.WHITE + '\n[&]: The IP was changed')
        ret()

    else:
        error()

    elif choice == '02' and not os.name == 'nt':
        choice = input(color.WHITE + '\n[&]: Enter the IP address to change: ')
        os.system(f'sudo ifconfig eth0 {ip} netmask 255.255.255.0 && sudo ifdown eth0 && sudo ifup eth0')
        print(color.WHITE + '\n[&]: The IP was changed')
        ret()  

    else:
        error()



def main():
    clear()
    title = '''
 ▄▄▄▄    ██▓     █    ██ ▓█████  █     █░ ▒█████   ██▓      █████▒
▓█████▄ ▓██▒     ██  ▓██▒▓█   ▀ ▓█░ █ ░█░▒██▒  ██▒▓██▒    ▓██   ▒ 
▒██▒ ▄██▒██░    ▓██  ▒██░▒███   ▒█░ █ ░█ ▒██░  ██▒▒██░    ▒████ ░ 
▒██░█▀  ▒██░    ▓▓█  ░██░▒▓█  ▄ ░█░ █ ░█ ▒██   ██░▒██░    ░▓█▒  ░ 
░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▒░░██▒██▓ ░ ████▓▒░░██████▒░▒█░    
░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒ ░    
▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░  ▒ ░ ░    ░ ▒ ▒░ ░ ░ ▒  ░ ░      
 ░    ░   ░ ░    ░░░ ░ ░    ░     ░   ░  ░ ░ ░ ▒    ░ ░    ░ ░    
 ░          ░  ░   ░        ░  ░    ░        ░ ░      ░  ░        
      ░                                                  
          [&]: BlueWolf By ZombieGeeK0 
          [&]: GitHub: https://github.com/ZombieGeeK0        
'''
    print(color.BLUE + title)
    options = '''
[00]: Exit the program
[01]: Get my IP
[02]: Change my IP
'''
    print(color.WHITE + options)

    print(color.BLUE + f'┌── <{hostname}@BlueWolf> ─ [~]')
    choice = input('└──╼ $ ')

    if choice == '00':
        exit()

    elif choice == '01':
        get_ip()

    elif choice == '02':
        change_ip()

    else:
        error


main()


# poner bien los if tipo if algo: break
