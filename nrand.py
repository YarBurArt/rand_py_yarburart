print("[info] import module ...")
import colorama
from colorama import Fore, Back, Style
import random
import requests
import os
from PIL import Image
print(Fore.GREEN + "[done] \n" , Style.RESET_ALL)
"""
image_url = "http://static.maps.2gis.com/1.0?center=" + input("a:") +","+input("b:")+"&zoom=10&size=500,500"

img_data = requests.get(image_url).content
with open('rand.png', 'wb') as handler:
    handler.write(img_data)

os.startfile("rand.png")
"""
print(Fore.YELLOW + "[info]",Style.RESET_ALL," import random image ...")
rand_img = "nasa-curiosity/img_nasa_" + str(random.randint(0, 99)) + ".jpg"
img = Image.open(rand_img)
obj = img.load()
print(Fore.GREEN + "[done] \n" , Style.RESET_ALL)
print(Fore.YELLOW + "[info]",Style.RESET_ALL," randoming float ...")
r1 = obj[random.randint(0,432),random.randint(0,432)]
r2 = r1[0] + r1[1] + r1[2]
r3 = float(r2) / 3 
r4 = r3 / random.randint(1,10)
r5 = r4 * random.randint(-1000000, 1000000)
print(Fore.GREEN + "[done] \n" , Style.RESET_ALL)
print(Fore.MAGENTA + "[result]", Style.RESET_ALL,"pic color:",r1, "| medium color:",r3, "| result integer:",Fore.CYAN + str(r5), Style.RESET_ALL)