import os

FILE_DIR = "/home/ates-isf/Scripts/.vpnstatus.txt"
EMAIL = "isfendiyar510@gmail.com"

if not os.path.exists(FILE_DIR):
    with open(FILE_DIR, "w") as file:
        file.write("0\n")

with open(FILE_DIR, "r") as file:
    status = int(file.readline()[0])
    
    if status == 1:
        isconnected = True
    else:
        isconnected = False

if isconnected == False:
    os.system("nm-applet > /dev/null 2>&1 &")
    os.system(f"protonvpn-cli login {EMAIL}")
    os.system("protonvpn-cli c -f")
    print("Run the script again to disconnect.")

    with open(FILE_DIR, "w") as file:
        file.write("1\n")

elif isconnected == True:
    os.system("protonvpn-cli d")
    os.system("killall nm-applet")

    with open(FILE_DIR, "w") as file:
        file.write("0\n")

