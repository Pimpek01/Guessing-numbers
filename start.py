import random
import time
while True:
    passwrod = str(input("Wpisz Liczbe od 0 do 9999: "))
    los = " "
    while los != passwrod:
        los = str(random.randint(0, 9999))
        print(">>>" + los)
        if (los == passwrod):
            print("Liczba to: " + passwrod)
            time.sleep(4)
            random
