print (""""
********

TEKIN FAKTORIYEL BULMA PROGRAMINA HOSGELDINIZ

Cikmak isterseniz 'm' ye basiniz.

********
""")

while True:
    sayi = raw_input("Hesaplamak isteginiz sayi:")
    if sayi == "m":
        print("Programdan cikiliyor...\n Gorusmek Uzere")
        break
    else :
        sayi=int(sayi)
        faktoriyel=1

        for i in range(2,sayi +1):
            faktoriyel *= i
        print("Faktoriyel",faktoriyel)