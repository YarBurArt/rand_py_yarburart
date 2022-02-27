import random
alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ineg = int(input('Seed шифровки: '))
random.seed(ineg)
smeshenie = random.randint(0, 10)
message = input("Сообщение для ДЕ/шифровки: ").upper()
itog = ''
lang = input('Выберите язык RU/EU: ')
cf = input('Шифровка или дешифровка 1/2:')
if cf == '1':
    # Алгоритм для дешифрования сообщения
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto - smeshenie
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto - smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
if cf == '2':
    # Алгоритм для шифрования сообщения         
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)   # Алгоритм для шифрования сообщения на русском 
            new_mesto = mesto + smeshenie
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EU.find(i)      # Алгоритм для шифрования сообщения на английском 
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
print (itog)