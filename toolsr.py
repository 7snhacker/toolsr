def toolsr():
    import os
    os.system("clear")
    print("""████████╗ ██████╗  ██████╗ ██╗     ███████╗██████╗ 
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝██╔══██╗
   ██║   ██║   ██║██║   ██║██║     ███████╗██████╔╝
   ██║   ██║   ██║██║   ██║██║     ╚════██║██╔══██╗
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                   """)
    pkgs = print("1- install Packages")
    tools = print("2- Show tools")
    toolsr = print("3- install all tools")
    reinstall = print("4- Reinstall script ( Update )")
    inp = input("$ ")
    if inp == "3":
        os.system("clear")
        os.system("apt install metasploit-framework sqlmap hash-identifier uniscan weevely backdoor-factory burpsuite armitage websploit john johnny xsser wireshark set aircrack-ng masscan wpscan jsql beef-xss nmap acccheck enum4linux exploitdb p0f parsero sfuzz sqlninja ghost-phisher mdk3 hydra-gtk -y")
        os.system("apt install git -y && git clone git://git.kali.org/packages/gr-scan.git")
        os.system("apt install git && git clone https://github.com/hangetzzu/saycheese.git")
        os.system("apt install git && git clone https://github.com/suljot/shellphish.git")
        os.system("apt install git && git clone https://github.com/DarkSecDevelopers/HiddenEye-Legacy.git")
        os.system("apt install git && git clone https://github.com/wifiphisher/wifiphisher.git")
        os.system("apt install git && git clone https://github.com/UndeadSec/SocialFish.git")
        os.system("apt install git && git clone https://github.com/htr-tech/zphisher.git")
        os.system("apt install git && git clone https://github.com/Cyb0r9/SocialBox.git")
        os.system("apt install git && git clone https://github.com/Mebus/cupp.git")
        os.system("apt install git && git clone https://github.com/the-robot/sqliv.git")
        os.system("clear")
        os.system("ls")
    elif inp == "4":
        os.system("git clone https://github.com/7snhacker/toolsr.git")
        os.system("rm toolsr.py")
        os.system("rm README.md")
        os.system("ls")
    elif inp == "1":
         os.system("clear")
         os.system("apt install python python2 ruby git php perl bash wget unzip curl -y")
         os.system("python3 toolsr.py")
    elif inp == "2":
        os.system("clear")
        c = print('''
        0- back
        1- nmap
        2- sqlmap
        3- metasploit
        4- jsql
        5- masscan
        6- Aircrack-ng
        7- gr-scan
        8- setoolkit
        9- Wireshark
        10- WPScan
        11- XSSer
        12- Burp Suite
        13- Weevely
        14- BeEF
        15- hash-identifier
        16- John the Ripper
        17- Johnny
        18- Armitage
        29- Uniscan
        20- websploit
        21- Backdoor Factory
        22- acccheck
        23- enum4linux
        24- exploitdb
        25- p0f
        26- parsero
        27- sfuzz
        28- sqlninja
        29- ghost-phisher
        30- mdk3
        31- saycheese
        32- shellphish
        33- HiddenEye
        34- wifiphisher
        35- SocialFish
        36- zphisher
        37- SocialBox
        38- cupp
        39- hydra
        40- sqliv
        ''')
        option = input("$ ")
        if option == "1":
            os.system("clear")
            os.system("apt install nmap -y")
            os.system("python3 toolsr.py")
        elif option == "2":
              os.system("clear")
              os.system("apt install sqlmap -y")
              os.system("python3 toolsr.py")
        elif option == "3":
            os.system("clear")
            os.system("apt install metasploit-framework -y")
            os.system("python3 toolsr.py")
        elif option == "4":
            os.system("clear")
            os.system("apt install jsql -y")
            os.system("python3 toolsr.py")
        elif option == "5":
            os.system("clear")
            os.system("apt install masscan -y")
            os.system("python3 toolsr.py")
        elif option == "6":
            os.system("clear")
            os.system("apt install aircrack-ng -y")
            os.system("python3 toolsr.py")
        elif option == "7":
            os.system("clear")
            os.system("apt install git -y && git clone git://git.kali.org/packages/gr-scan.git")
            os.system("python3 toolsr.py")
        elif option == "8":
            os.system("clear")
            os.system("apt install set -y")
            os.system("python3 toolsr.py")
        elif option == "9":
            os.system("clear")
            os.system("apt install wireshark -y")
            os.system("python3 toolsr.py")
        elif option == "10":
            os.system("clear")
            os.system("apt install wpscan -y")
            os.system("python3 toolsr.py")
        elif option == "11":
            os.system("clear")
            os.system("apt install xsser -y")
            os.system("python3 toolsr.py")
        elif option == "12":
            os.system("clear")
            os.system("apt install burpsuite -y")
            os.system("python3 toolsr.py")
        elif option == "13":
            os.system("clear")
            os.system("apt install weevely -y")
            os.system("clear")
            os.system("python3 toolsr.py")
        elif option == "14":
            os.system("clear")
            os.system("apt install beef-xss -y")
            os.system("python3 toolsr.py")
        elif option == "15":
            os.system("clear")
            os.system("apt install hash-identifier -y")
            os.system("python3 toolsr.py")
        elif option == "16":
            os.system("clear")
            os.system("apt install john -y")
            os.system("python3 toolsr.py")
        elif option == "17":
            os.system("clear")
            os.system("apt install johnny -y")
            os.system("python3 toolsr.py")
        elif option == "18":
            os.system("clear")
            os.system("apt install armitage -y")
            os.system("python3 toolsr.py")
        elif option == "19":
            os.system("clear")
            os.system("apt install uniscan -y")
            os.system("python3 toolsr.py")
        elif option == "20":
            os.system("clear")
            os.system("apt install websploit -y")
            os.system("python3 toolsr.py")
        elif option == "21":
            os.system("clear")
            os.system("apt install backdoor-factory -y")
            os.system("python3 toolsr.py")
        elif option == "22":
            os.system("clear")
            os.system("apt install acccheck -y")
            os.system("python3 toolsr.py")
        elif option == "23":
            os.system("clear")
            os.system("apt install enum4linux -y")
            os.system("python3 toolsr.py")
        elif option == "24":
            os.system("clear")
            os.system("apt install exploitdb -y")
            os.system("python3 toolsr.py")
        elif option == "25":
            os.system("clear")
            os.system("apt install p0f -y")
            os.system("python3 toolsr.py")
        elif option == "26":
            os.system("clear")
            os.system("apt install parsero -y")
            os.system("python3 toolsr.py")
        elif option == "27":
            os.system("clear")
            os.system("apt install sfuzz -y")
            os.system("python3 toolsr.py")
        elif option == "28":
            os.system("clear")
            os.system("apt install sqlninja -y")
            os.system("python3 toolsr.py")
        elif option == "29":
            os.system("clear")
            os.system("apt install ghost-phisher -y")
            os.system("python3 toolsr.py")
        elif option == "30":
            os.system("clear")
            os.system("apt install mdk3 -y")
            os.system("python3 toolsr.py")
        elif option == "31":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/hangetzzu/saycheese.git")
            os.system("python3 toolsr.py")
        elif option == "32":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/suljot/shellphish.git")
            os.system("python3 toolsr.py")
        elif option == "33":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/DarkSecDevelopers/HiddenEye-Legacy.git")
            os.system("python3 toolsr.py")
        elif option == "34":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/wifiphisher/wifiphisher.git")
            os.system("python3 toolsr.py")
        elif option == "35":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/UndeadSec/SocialFish.git")
            os.system("python3 toolsr.py")
        elif option == "36":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/htr-tech/zphisher.git")
            os.system("python3 toolsr.py")
        elif option == "37":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/Cyb0r9/SocialBox.git")
            os.system("python3 toolsr.py")
        elif option == "38":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/Mebus/cupp.git")
            os.system("python3 toolsr.py")
        elif option == "39":
            os.system("clear")
            os.system("apt install hydra-gtk")
            os.system("python3 toolsr.py")
        elif option == "40":
            os.system("clear")
            os.system("apt install git && git clone https://github.com/the-robot/sqliv.git")
            os.system("python3 toolsr.py")
        elif option == "0":
            os.system("clear")
            os.system("python3 toolsr.py")
toolsr()




