import random
def adamas():

    kelimeler = random.choice(["bulut", "gece", "gökyüzü", "araba", "telefon", "konforlu", "kütüphane", "yıldız", "orion", "kulaklık", "deniz", "şelale", "gölet", "okyanus", "olasılık", "defter", "matara", "kahve", "yasemin", "orkide", "lavanta", "kedi", "bilgisayar", "manzara", "hayat", "okul", "çanta", "matematik", "fizik", "kimya", "biyoloji", "türkçe", "yazılım"])
    gecerliHarfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
    toplamHak = 9
    yapilanTahmin = ''

    while len(kelimeler) > 0:
        asilKelime = ""
        hataliTahminSayisi = 0

        for harf in kelimeler:
            if harf in yapilanTahmin:
                asilKelime = asilKelime + harf
            else:
                asilKelime = asilKelime + "_" + " "
        if asilKelime == kelimeler:
            print(asilKelime)
            print("Tebrikler kazandınız!")
            break

        print("Harf girin:" , asilKelime)
        tahmin = input()

        if tahmin in gecerliHarfler:
            yapilanTahmin = yapilanTahmin + tahmin
        else:
            print("girdiğiniz harfi kontrol edin")
            tahmin = input()
        if tahmin not in kelimeler:
            toplamHak = toplamHak - 1
            if toplamHak == 8:
                print("8 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
            if toplamHak == 7:
                print("7 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if toplamHak == 6:
                print("6 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if toplamHak == 5:
                print("5 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 4:
                print("4 hakkınız kaldı")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 3:
                print("3 hakkınız kaldı")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 2:
                print("2 hakkınız kaldı")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 1:
                print("1 hakkınız kaldı")
                print("Dikkatli kullanın")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if toplamHak == 0:
                print("Oyun bitti")
                print("bilemediniz ve kaybettiniz")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


print("Kelimeyi bulabilmek için 9 hakkınız var")
adamas()
print()