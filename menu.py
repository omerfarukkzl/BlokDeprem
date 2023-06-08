import pandas as pd


# Sistemde kayıtlı kullanıcılar
kullanicilar = {}

# Excel dosyasını okuma ve kullanıcı bilgilerini güncelleme
def load_user_data():
    try:
        df = pd.read_excel('login_bilgileri.xlsx')
        for index, row in df.iterrows():
            kullanici_adi = row['Kullanıcı Adı']
            sifre = row['Şifre']
            kullanicilar[kullanici_adi] = sifre
            print(df)
    except FileNotFoundError:
        print("Excel dosyası bulunamadı!")


# Kullanıcı yetkileri
kullanici_yetkileri = {"Sisteme Üye Ol": True,
"Sisteme Giriş Yap": True,
"Şifremi Unuttum": True,
"Kullanıcı Sil": False,
"Çıkış Yap": True}


# Admin yetkileri
admin_yetkileri = {"Sisteme Üye Ol": True,
"Sisteme Giriş Yap": True,
"Şifremi Unuttum": True,
"Kullanıcı Sil": True,
"Çıkış Yap": True}

# Sisteme üye olma işlemi
def uye_ol():
    print("Sisteme kayıt işlemi")
    kullanici_adi = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    kullanicilar[kullanici_adi] = sifre
    print("Kayıt işlemi başarıyla tamamlandı!\n")

# Sisteme giriş yapma işlemi
def giris_yap():
    global kullanici_adi # kullanıcı adını global değişken olarak tanımla
    print("Sisteme giriş işlemi")
    kullanici_adi = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == sifre:
        print("Giriş başarılı!\n")
        return True # giriş başarılı ise True döndür
    else:
        print("Kullanıcı adı veya şifre yanlış!\n")
        return False # giriş başarısız ise False döndür

# Şifremi unuttum işlemi
def sifre_unuttum():
    print("Şifremi unuttum işlemi")
    kullanici_adi = input("Kullanıcı adı: ")
    if kullanici_adi in kullanicilar:
        yeni_sifre = input("Yeni şifre: ")
        kullanicilar[kullanici_adi] = yeni_sifre
        print("Şifreniz başarıyla güncellendi!\n")
    else:
        print("Kullanıcı adı bulunamadı!\n")
        
# Kullanıcı silme işlemi
def kullanici_sil():
    print("Kullanıcı silme işlemi")
    silinecek_kullanici = input("Silinecek kullanıcı adı: ")
    if silinecek_kullanici in kullanicilar:
        kullanicilar.pop(silinecek_kullanici) # sözlükten pop metodu ile sil
        print(f"{silinecek_kullanici} isimli kullanıcı silindi.\n")
    else:
        print("Kullanıcı adı bulunamadı!\n")

#Çıkış Yap işlemi       
def programi_kapat():
    print("Program kapatılıyor...")
    raise SystemExit

# Menü seçenekleri için tuple ve listeler
menu_options = (
    "Sisteme Üye Ol",
    "Sisteme Giriş Yap",
    "Şifremi Unuttum",
    "Kullanıcı Sil",
    "Çıkış Yap"
)
menu_functions = (
    uye_ol,
    giris_yap,
    sifre_unuttum,
    kullanici_sil,
    programi_kapat,
)

# Ana menü
def main_menu():
    
    giris_durumu = False # giriş durumunu takip etmek için bir değişken
    
    while True:
        print("Ana Menü")
        
        if giris_durumu: # eğer giriş yapıldıysa
            if kullanici_adi == "admin": # eğer kullanıcı admin ise
                yetki_sozlugu = admin_yetkileri # yetki sözlüğünü admin yetkileri olarak belirle
            else: # eğer kullanıcı admin değilse
                yetki_sozlugu = kullanici_yetkileri # yetki sözlüğünü kullanıcı yetkileri olarak belirle
        else: # eğer giriş yapılmadıysa
            yetki_sozlugu = kullanici_yetkileri # yetki sözlüğünü kullanıcı yetkileri olarak belirle
        
        for i, option in enumerate(menu_options):
            if yetki_sozlugu[option]: # eğer seçenek yetki sözlüğünde True ise
                print(f"{i+1}. {option}") # seçeneği göster
        choice = input("İşlem seçiniz: ")
        try:
            choice = int(choice)
            if choice > 0 and choice <= len(menu_options):
                if yetki_sozlugu[menu_options[choice-1]]: # eğer seçilen işlem yetki sözlüğünde True ise
                    if menu_functions[choice-1]() == True: # eğer seçilen işlem giriş yapma ise ve başarılı ise
                        giris_durumu = True # giriş durumunu True yap
                else: # eğer seçilen işlem yetki sözlüğünde False ise
                    print("Bu işlem için yetkiniz yok!\n") # uyarı ver
            else:
                raise ValueError
        except ValueError:
            print("Hatalı seçim yaptınız!\n")

# Programı çalıştırma

main_menu()
