import random
import os
import json

FILE_NAME = "C:\\Users\\gokce\\OneDrive\\Masaüstü\\Code\\alistirmalar\\sifre\\sifreler.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump({}, file)


def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
def main():
    veriler = load_data()
    while True:
        print("\n-----Menü-----")
        print("1 - Yeni giriş")
        print("2 - Şifre değiştir")
        print("3 - Hesap sil")
        print("4 - Çıkış")
        choice = input("Seçim yapınız: ")

        if choice == "1":
            kullanici_adi = input("Kullanıcı Adı giriniz: ")
            sifre = input("Şifre giriniz: ")
            veriler[kullanici_adi] = sifre
            save_data(veriler)
        elif choice == "2":
                print("\n-----Şifre Değiştirme-----")
                check_user = input("Kullanıcı Adı giriniz: ")
                if check_user in veriler:
                    check_pass = input(f"{check_user} adlı hesabın mevcut şifresini girin: ")
                    if veriler[check_user] == check_pass:
                        yeni_sifre = input("Yeni şifreyi giriniz: ")
                        veriler[check_user] = yeni_sifre
                        save_data(veriler)
                        print(f"\n{check_user} için şifre değiştirilmiştir")
                    else:
                            print("Yanlış Şifre")
                else:
                    print("Yanlış kullanıcı adı ")
        elif choice == "3":
                print("\n-----Hesap Silme-----")    
                check_account = input("Kullanıcı Adı giriniz: ")
                if check_account in veriler:
                    del veriler[check_account]
                    save_data(veriler)
                else:
                    print("Yanlış kullanıcı adı")
        elif choice == "4":
            break


main()

