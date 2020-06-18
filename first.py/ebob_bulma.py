print(""" ***********************
ebob bulma prg.
en büyük ortak bölenini
********************""")
sayi1 = int(input("sayi1 giriniz :"))
sayi2 = int(input("sayi2 giriniz :"))


def ebob_bulma(sayi1,sayi2):
    ebob = 0
    i = 1
    while (sayi1 >= i) and (sayi2 >= i):
        if (sayi1 % i == 0) and (sayi2 % i == 0):
            ebob = i
        i+=1
    return ebob

print("{} ve {} nin ebob u {} dur".format(sayi1,sayi2,ebob_bulma(sayi1,sayi2)))
