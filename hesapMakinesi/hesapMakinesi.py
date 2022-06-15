x1=0
x2=0
sonuc=0
secim=0

def toplama(x1,x2):
    global sonuc
    sonuc=x1+x2
    return sonuc

def cıkarma(x1,x2):
    global sonuc
    sonuc=x1-x2
    return sonuc

def carpma(x1,x2):
    global sonuc
    sonuc=x1*x2
    return sonuc

def bolme(x1,x2):
    global sonuc
    sonuc=x1/x2
    return sonuc

while True:
    print("Toplama islemi icin '1'\nÇıkarma islemi icin '2'\nÇarpma islemi icin '3'\nBolme islemi icin '4'\nCikis icin '-1'")
    secim = int(input("Yapmak istediginiz islemi seciniz: "))

    if(secim == -1):
        print("Cikis yaptınız.")
        break

    elif(secim == 1):
        x1 = int(input("1. Sayiyi giriniz:"))
        x2 = int(input("2. Sayiyi giriniz:"))
        print("Sonuc="+str(toplama(x1,x2))+"\n")


    elif (secim == 2):
        x1 = int(input("1. Sayiyi giriniz:"))
        x2 = int(input("2. Sayiyi giriniz:"))
        print("Sonuc="+str(cıkarma(x1,x2))+"\n")

    elif (secim == 3):
        x1 = int(input("1. Sayiyi giriniz:"))
        x2 = int(input("2. Sayiyi giriniz:"))
        print("Sonuc="+str(carpma(x1,x2))+"\n")

    elif (secim == 4):
        x1 = int(input("1. Sayiyi giriniz:"))
        x2 = int(input("2. Sayiyi giriniz:"))
        print("Sonuc=" + str(bolme(x1, x2)) + "\n")

    else:
        print("Yanlis deger girdiniz.\n")