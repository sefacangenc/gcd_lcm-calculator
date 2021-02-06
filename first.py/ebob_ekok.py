sayi1 = int(input("sayi1 :"))
sayi2 = int(input("sayi2 :")) 
def gcd(sayi1,sayi2):#ebob
    while sayi2 > 0:
        sayi1,sayi2 = sayi2,sayi1 % sayi2
    return sayi1
    

def lcm(sayi1,sayi2):#ekok
    return (sayi1*sayi2)/gcd(sayi1,sayi2)

while True:
    secim = input("2 sayinin ekok unun mu ebob unun mu bulmak istersinniz")
    if secim == "ekok":
        print("{} ve {} nin ekok u {} dur".format(sayi1,sayi2,lcm(sayi1,sayi2)))
        break
    elif secim == "ebob":
        print("{} ve {} nin ebob u {} dur".format(sayi1,sayi2,gcd(sayi1,sayi2)))
        break
    else:
        print("lütfen geçerli bir işlem seçiniz")
