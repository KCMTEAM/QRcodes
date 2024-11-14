import os
import pyqrcode
from PIL import Image
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
MAGENTA = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"
RESET = "\033[0m"

BANNER = (
    f"{RESET}°{RED}████████████████████████████████████████████████ \n"
    f" {RED}█─▄▄▄─██▄─▄▄▀██─▄▄▄─██─▄▄─██▄─▄▄▀██▄─▄▄─██─▄▄▄▄█ \n"
    f" {WHITE}█─██▀─███─▄─▄██─███▀██─██─███─██─███─▄█▀██▄▄▄▄─█ \n"
    f" ▀───▄▄▀▀▄▄▀▄▄▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▄▄▀ \n"
    f" {CYAN}___________________{RED}[ {GREEN}HAIFIL{RED} ]{CYAN}___________________{RESET}"
)

print(BANNER)
def startQr():
  os.system('clear')
  print(BANNER)
  print("")
  linkInput = input(f"{YELLOW}INPUT LINK HERE TO GENERATE{WHITE}:{GREEN} ")
  qrcode = pyqrcode.create(linkInput)
  qrcode.png("QRCode.png", scale=5)
  print(f"""
{YELLOW}GENERATE SUCCESSFULL {GREEN}✓""")
startQr()