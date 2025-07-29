from colorama import init, Fore, Style
init()
import random

devam = True

while devam:
    print(Fore.YELLOW + Style.BRIGHT + "********** SAYI TAHMİN ETME OYUNUNA HOŞGELDİNİZ **********" + Style.RESET_ALL)
    min_sayi = 1
    max_sayi = 100
    while True:
        hak = int(input("Kaç deneme hakkınız olsun? (0-100 aralığında): "))
        if 1<=hak<=100:
            break
        else:
            print("Lütfen geçerli bir aralık giriniz!")
    sayi = random.randint(1,100)
    deneme = hak

    while deneme != 0:
        tahmin = int(input("Tahminizi giriniz: "))
        if sayi == tahmin:
            print(Fore.GREEN + f"Doğru tahmin! Oyunu {(hak+1)-deneme} denemede bitirdiniz ve puanınız {100-(int(100/hak)*((hak+1)-deneme))}." + Style.RESET_ALL)
            karar = input("Tekrar oynamak ister misiniz? (E/H): ")
            if karar.upper() == "H":
                devam = False
            break

        elif tahmin<sayi:
            deneme -=1
            min_sayi = tahmin+1
            if deneme == 0:
                print(Fore.YELLOW + Style.BRIGHT + f"Haklarınız bitmiştir. Kaybettiniz :( Puanınız : 0 Doğru cevap : {sayi}" + Style.RESET_ALL)
                karar = input("Tekrar oynamak ister misiniz? (E/H): ")
                if karar.upper() == "H":
                    devam = False
            else:
                print(Fore.RED + f"Yanlış tahmin, YUKARI! Kalan hakkınız: {deneme} ve tahmin aralığınız {min_sayi}-{max_sayi}." + Style.RESET_ALL)

        elif tahmin>sayi:
            deneme -=1
            max_sayi = tahmin-1
            if deneme == 0:
                print(Fore.YELLOW + Style.BRIGHT + f"Haklarınız bitmiştir. Kaybettiniz :( Puanınız : 0 Doğru cevap : {sayi}" + Style.RESET_ALL)
                karar = input("Tekrar oynamak ister misiniz? (E/H): ")
                if karar.upper() == "H":
                    devam = False
            else:
                print(Fore.RED + f"Yanlış tahmin, AŞAĞI! Kalan hakkınız: {deneme} ve tahmin aralığınız {min_sayi}-{max_sayi}." + Style.RESET_ALL)

print(Fore.BLUE + Style.BRIGHT + "OYUN BİTMİŞTİR." + Style.RESET_ALL)
