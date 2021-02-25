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
    update = print("4- Update script")
    inp = input("$ ")
    if inp == "3":
        os.system("clear")
        os.system("apt install metasploit-framework sqlmap hash-identifier uniscan weevely backdoor-factory burpsuite armitage websploit john johnny xsser wireshark set aircrack-ng masscan wpscan jsql beef-xss nmap -y")
        os.system("apt install git -y && git clone git://git.kali.org/packages/gr-scan.git")
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
        elif option == "0":
            os.system("clear")
            os.system("python3 toolsr.py")
toolsr()





