try: 
    print("[info] import module ...")
    from colorama import Fore, Back, Style
    from random import randint
    from randomgen import ExtendedGenerator, Xoshiro512
    from PIL import Image
    from PIL.Image import Image as ImageObj
    print(Fore.GREEN + "[done] \n" , Style.RESET_ALL)

except ImportError as e:
    print("[error] import module: " + e)
    
def load_image() -> ImageObj:
    print(Fore.YELLOW + "[info]",Style.RESET_ALL," load random image ...")
    rand_img:str = "nasa-curiosity/img_nasa_" + str(randint(0, 99)) + ".jpg"
    img = Image.open(rand_img)

    if obj := img.load():
        print(Fore.GREEN + "[done] \n" , Style.RESET_ALL)
        return obj

def get_rand(obj: ImageObj) -> int:
    print(Fore.YELLOW + "[info]", Style.RESET_ALL, " randoming float ...")
    r1:list = obj[randint(0,432), randint(0,432)]
    r2:int = r1[0] + r1[1] + r1[2]
    r3:float = float(r2) / 3 
    r4:float = r3 / randint(1, 10)
    r5:float = r4 * randint(-1000000, 1000000)
    rg = ExtendedGenerator(Xoshiro512())
    r5 = rg.random()
    print(Fore.YELLOW+ "[data] ", Style.RESET_ALL,"pic color:", r1, "| medium color:", r3, "| seed:", r4 , Style.RESET_ALL)
    print(Fore.GREEN + "[done] \n" , Style.RESET_ALL)
    return r5
    

if __name__ == "__main__":
    obj = load_image()
    result = get_rand(obj)
    print(Fore.MAGENTA + "[result] ", Fore.CYAN + str(result), Style.RESET_ALL)    
    