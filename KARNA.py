from pyfiglet import figlet_format
from colorama import Fore, Style
import os

print(Fore.YELLOW + figlet_format("KARNA"))
print(Fore.RED + "[*] Created by Vizz\n" + Style.RESET_ALL)

def usb_history():
    print(Fore.CYAN + "[*] Listing USB device history..." + Style.RESET_ALL)
    os.system("reg query HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR /s")

usb_history()