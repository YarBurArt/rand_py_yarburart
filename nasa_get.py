import requests
import os
from numba import njit, prange

api_key = None
set_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=" + api_key

idat = requests.get(set_url)
print(idat.text)
print("\n")
print(idat.headers)
print("\n")
jdat = idat.json()
photos = jdat["photos"]


for i in prange(len(photos)):
    xc = photos[i]["img_src"]
    print(xc)
    img_data = requests.get(str(photos[i]["img_src"])).content
    nstr = "nasa-curiosity/img_nasa_" + str(i) + ".jpg"
    with open(nstr, 'wb') as handler:
        handler.write(img_data)
    if i == 99:
        break
print(f"Найдено {len(photos)} фотографий.")