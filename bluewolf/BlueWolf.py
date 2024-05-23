from colorama import Fore, Style
import os, socket, sys, requests, pywhatkit, pyshorteners, base64, qrcode, sqlite3, platform
from faker import Faker  
from random import sample
import PyPDF2

faker = Faker()  

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

class color:
    RED = Fore.RED + Style.BRIGHT
    BLUE = Fore.BLUE + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

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
    print(color.WHITE + f'\n[&]: Inexpected error in {color.BLUE}BlueWolf{color.WHITE}')
    ret()

def get_ip():
    print(color.WHITE + '\n[&]: Your IP adress is: ' + color.BLUE + ip)
    ret()

def verify():
    try:
        res = requests.get('https://www.google.com')
        print(color.WHITE + f'\n[&]: You are {color.BLUE}connected{color.WHITE} to Internet')
    except:
        print(color.WHITE + f"\n[&]: You {color.BLUE}aren't connected{color.WHITE} to Internet")
    ret()

def send_discord():
    try:
        webhook = input(color.WHITE + '\n[&]: Enter the URL of your server WebHook: ')
        message = input(color.WHITE + '[&]: Enter the message to send: ')
        requests.post(webhook, json={'username': 'BlueWolf', 'content': message})
        print(color.WHITE + f'[&]: Message {color.BLUE}sended{color.WHITE} successfully')

    except:
        error()

def gen_ip():
    false_ip = faker.ipv4() 
    print(color.WHITE + '\n[&]: The false IP address is: ' + color.BLUE + false_ip)
    ret()

def gen_phone():
    false_phone = faker.phone_number()
    print(color.WHITE + '\n[&]: The false phone number is: ' + color.BLUE + false_phone)
    ret()

def send_whatsapp():
    try:
        choice = input(color.WHITE + '\n[&]: Enter the phone number to send the message: ')
        message = input(color.WHITE + '[&]: Enter the message to send: ')
        pywhatkit.sendwhatmsg_instantly(choice, message)
        
        print(f'\n[&]: Message {color.BLUE}sended{color.WHITE} successfully')
        
    except:
        error()

    ret()

def binary():
    choice = input(color.WHITE + '\n[&]: Enter the plain text to convert: ')
    binary = ' '.join(format(ord(caracter), '08b') for caracter in choice)
    print(color.WHITE + '[&]: The binary code generated is: ' + color.BLUE + binary)
    ret()

def parrot():
    try:
        os.system('curl parrot.live')

    except KeyboardInterrupt:
        print(color.WHITE + f'\n\n[&]: Operation {color.BLUE}interrupted')
    
    except:
        error()

    ret()

def info():
    choice = f'''
[&]: BlueWolf By {color.BLUE}ZombieGeeK0
{color.WHITE}[&]: GitHub: {color.BLUE}https://github.com/ZombieGeeK0/BlueWolf
{color.WHITE}[&]: {color.BLUE}©2024{color.WHITE} By ZombieGeeK0
{color.WHITE}[&]: BlueTiger is a multitool make with only {color.BLUE}ethical purposes. 
'''
    print(color.WHITE + choice)
    ret()

def get_public():
    res = requests.get('https://api.ipify.org?format=json')
    public_ip = res.json()['ip']

    print(color.WHITE + f'\n[&]: The public IP adress is: ' + color.BLUE + public_ip)
    ret()

def generate_pass():   
    measure = int(input(color.WHITE + '\n[&]: Enter the measure in characters of your password: '))

    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = abc_lower.upper() 
    
    numbers = "0123456789"
    characters = "{}[]()*;/,_-"
    
    sequence = abc_lower + abc_upper + numbers + characters
    password = sample(sequence, measure)
    

    password_result = "".join(password)
    print(color.WHITE + '[&]: The result password is: ' + color.BLUE + password_result)
    ret()

def read_pdf():
    choice = input(color.WHITE + '\n[&] Enter the path or the name of the PDF file to read: ')
    reader = PyPDF2.PdfReader(choice)

    print(color.WHITE + '[&]: The PDF have ' + color.BLUE + str(len(reader.pages)) + color.WHITE + 'pages')
    print(color.WHITE + '[&]: The text of the PDF file is: \n' + color.BLUE + reader.pages[0].extract_text())

    ret()

def mask_url():
    s = pyshorteners.Shortener()
    choice = input(color.WHITE + '\n[&]: Enter the URL to mask: ')
    try:
        ey = s.isgd.short(choice)
        mod = input(color.WHITE + '[&] Enter the domain you want to supplant (eg. https://google.com): ')
        word = input(color.WHITE + '[&] Enter the social engineering words separated by "-" (eg. free-gems): ')
        ey = ey.replace("https://", "")
        print(color.WHITE + f'[&]: The masked URL: {color.BLUE}{mod}-{word}@{ey}')

    except:
        error()

    ret()

def enc_base64():
    choice = input(color.WHITE + '\n[&]: Enter the plain text to encode: ')

    text_bytes = choice.encode('utf-8')
    encrypted_text = base64.b64encode(text_bytes)

    print(color.WHITE + '[&]: The text encrypted in base64 is: ' + color.BLUE + str(encrypted_text.decode("utf-8")))
    ret()

def get_size():
    choice = input(color.WHITE + '\n[&] Enter the file or path to the file to view size: ')

    sizefile = os.stat(choice).st_size
    print(color.WHITE + '[&]: The size of the file is: ' + color.BLUE + str(sizefile) + color.WHITE + ' bytes')
    ret()

def qr_code():
    try:
        choice = input(color.WHITE + '\n[&] Enter the URL or text to generate in the QR Code: ')
        arch = input(color.WHITE + '[&]: Enter the archive name to save the QR Code (the .png is auto completed): ')

        img = qrcode.make(choice)
        f = open(arch + '.png', "wb")
        img.save(f)
        f.close()

        print(color.WHITE + '\n[&]: The QR Code is generated in the file ' + color.BLUE + arch)

    except:
        error()

    ret()  

def clear_chrome_history():
    if platform.system() == 'Windows':
        history_path = os.path.expanduser('~') + r'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
    elif platform.system() == 'Linux':
        history_path = os.path.expanduser('~') + '/.config/google-chrome/Default/History'
    else:
        print(color.WHITE + f'[&]: System {color.BLUE}not supported{color.WHITE} for Chrome')
        return
    
    if os.path.exists(history_path):
        conn = sqlite3.connect(history_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM urls")
        conn.commit()

        cursor.close()
        conn.close()

        print(color.WHITE + f'[&]: Chrome history {color.BLUE}deleted{color.WHITE} successfully')
    else:
        print(color.WHITE + f"[&]: Chrome historial archive " + color.BLUE + 'not found')

def clear_firefox_history():
    if platform.system() == "Windows":
        profiles_path = os.path.expanduser('~') + r"\AppData\Roaming\Mozilla\Firefox\Profiles"
    elif platform.system() == "Linux":
        profiles_path = os.path.expanduser('~') + "/.mozilla/firefox/"
    else:
        print(color.WHITE + f'[&] System {color.BLUE}not supported{color.WHITE} for Firefox')
        return

    for root, dirs, files in os.walk(profiles_path):
        for dir in dirs:
            profile_path = os.path.join(root, dir)
            places_path = os.path.join(profile_path, "places.sqlite")
            if os.path.exists(places_path):
                conn = sqlite3.connect(places_path)
                cursor = conn.cursor()

                cursor.execute("DELETE FROM moz_historyvisits")
                cursor.execute("DELETE FROM moz_places")
                conn.commit()

                cursor.close()
                conn.close()

                print(color.WHITE + f'[&] Firefox history {color.BLUE}deleted{color.WHITE} successfully')
                return

    print(color.WHITE + f"[&] Firefox historial archive " + color.BLUE + 'not found')

def clear_browser_history():
    browsers = {
        "Chrome": clear_chrome_history,
        "Firefox": clear_firefox_history,
    }

    for browser, clear_func in browsers.items():
        try:
            clear_func()
        except Exception as e:
            error()

def history():
    print(color.WHITE + '\n[&] Cleaning history...')
    try:
        clear_browser_history()
        ret()

    except:
        error()

    ret()

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
[00]: Exit the program                                [11]: Generate a sure password
[01]: Get my IP address                               [12]: Read PDF file
[02]: Verify the Internet connection                  [13]: Mask an URL
[03]: Send Discord message                            [14]: Encrypt plain text with base64
[04]: Generate false IP address                       [15]: Obtener el espacio que ocupa un archivo
[05]: Generate false phone number                     [16]: Generate the QR Code of a URL
[06]: Send WhatsApp message                           [17]: Clear the browser history
[07]: Convert a plain text message in binary code
[08]: View parrot.live
[09]: Credits and info about this proyect
[10]: Get my public IP address
'''
    print(color.WHITE + options)

    print(color.BLUE + f'┌── <{hostname}@BlueWolf> ─ [~]')
    choice = input('└──╼ $ ')

    if choice == '00': exit()
    elif choice == '01': get_ip()
    elif choice == '02': verify()
    elif choice == '03': send_discord()
    elif choice == '04': gen_ip()
    elif choice == '05': gen_phone()
    elif choice == '06': send_whatsapp()
    elif choice == '07': binary()
    elif choice == '08': parrot()
    elif choice == '09': info()
    elif choice == '10': get_public()
    elif choice == '11': generate_pass()
    elif choice == '12': read_pdf()
    elif choice == '13': mask_url()
    elif choice == '14': enc_base64()
    elif choice == '15': get_size()
    elif choice == '16': qr_code()
    elif choice == '17': history()
    else: error()

main()
