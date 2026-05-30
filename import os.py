import os
import numpy as np
import pandas as pd

class Kullanici:
    def __init__(self, kullanici_adi, rol):
        self.kullanici_adi = kullanici_adi
        self.rol = rol

    def bilgileri_goster(self):
        print(f"\n[ Aktif Kullanıcı: {self.kullanici_adi} | Rol: {self.rol} ]")


class Admin(Kullanici):
    def __init__(self, kullanici_adi):
        super().__init__(kullanici_adi, rol="Admin")

    def menuyu_guncelle(self, restoran_sistemi):
        print("\n--- RESTORAN MENÜSÜNÜ GÜNCELLEME ---")
        yeni_urun = input("Eklenecek/Güncellenecek Ürün Adı: ").strip()
        try:
            yeni_fiyat = float(input(f"{yeni_urun} için fiyat girin (TL): "))
            if yeni_fiyat <= 0:
                print("Fiyat 0'dan büyük olmalıdır!")
                return
            
            restoran_sistemi.menu[yeni_urun] = yeni_fiyat
            print(f"-> {yeni_urun} başarıyla {yeni_fiyat} TL olarak güncellendi.")
        except ValueError:
            print("Hata: Lütfen geçerli bir fiyat sayısı girin!")

    def dosyadan_rapor_oku(self, dosya_adi="adisyonlar.txt"):
        print("\n" + "="*10 + " GÜN SONU RAPOR ANALİZİ " + "="*10)
        
        if not os.path.exists(dosya_adi):
            print("Henüz kaydedilmiş bir adisyon dosyası bulunamadı.")
            return

        tutar_listesi = []
        
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            for satir in dosya:
                if "Hesap Toplamı:" in satir:
                    parcalar = satir.split(":")
                    tutar_metni = parcalar[1].strip()
                    tutar_listesi.append(float(tutar_metni))

        if len(tutar_listesi) == 0:
            print("Dosyada okunacak adisyon kaydı bulunamadı.")
            return

        veri_sozlugu = {"Adisyon Tutar": tutar_listesi}
        df = pd.DataFrame(veri_sozlugu)
        print(df)

        np_dizisi = np.array(tutar_listesi)
        print(f"Toplam Ciro (np.sum)     : {np.sum(np_dizisi)} TL")
        print(f"Ortalama Hesap (np.mean)  : {np.mean(np_dizisi)} TL")
        print(f"En Yüksek Hesap (np.max)  : {np.max(np_dizisi)} TL")
        print("="*45)


class Musteri(Kullanici):
    def __init__(self, masa_no):
        super().__init__(kullanici_adi=f"Masa-{masa_no}", rol="Müşteri")
        self.masa_no = masa_no
        self.sepet = {} 

    def siparis_ekle(self, urun, adet):
        if urun in self.sepet:
            self.sepet[urun] = self.sepet[urun] + adet
        else:
            self.sepet[urun] = adet
        print(f"-> {adet} adet {urun} sepetinize eklendi.")

    def hesabi_ode_ve_kapat(self, menu_sozlugu, dosya_adi="adisyonlar.txt"):
        print(f"\n--- MASA {self.masa_no} HESAP ÖZETİ ---")
        if not self.sepet:
            print("Sepetiniz boş.")
            return True

        toplam_hesap = 0
        dosya_metni = f"=== Masa {self.masa_no} Adisyonu ===\n"

        for urun, adet in self.sepet.items():
            fiyat = menu_sozlugu[urun]
            ara_toplam = fiyat * adet
            toplam_hesap = toplam_hesap + ara_toplam
            
            satir = f" - {urun} x {adet} adet = {ara_toplam} TL\n"
            print(satir.strip())
            dosya_metni = dosya_metni + satir

        print(f"Toplam Ödenecek Tutar: {toplam_hesap} TL")
        dosya_metni = dosya_metni + f"Hesap Toplamı: {toplam_hesap}\n"
        dosya_metni = dosya_metni + "---------------------------\n"

        onay = input("Ödeme alındı mı? (E/H): ").strip().upper()
        if onay == "E":
            with open(dosya_adi, "a", encoding="utf-8") as dosya:
                dosya.write(dosya_metni)
            print("Ödeme alındı. Masa kapatıldı ve veriler dosyaya kaydedildi.")
            self.sepet.clear()
            return True
        else:
            print("Ödeme onaylanmadı, masa açık kaldı.")
            return False


class RestoranSistemi:
    def __init__(self):
        self.menu = {
            "Burger": 180.0,
            "Pizza": 220.0,
            "Kola": 45.0,
            "Ayran": 30.0,
            "Sufle": 90.0
        }
        self.kategoriler = ("Yiyecekler", "İçecekler", "Tatlılar")
        self.aktif_masalar = {}

    def menuyu_goster(self):
        print("\n" + "-"*10 + " GÜNCEL MENÜ " + "-"*10)
        for urun, fiyat in self.menu.items():
            print(f" * {urun:<12} : {fiyat} TL")
        print("-"*26)


def ana_program():
    sistem = RestoranSistemi()
    admin_paneli = Admin("Yasemin")
    
    masa_listesi = [1, 2, 3, 4, 5]

    while True:
        print("\n=== DİJİTAL GARSON OTOMASYON SİSTEMİ ===")
        print("1. Müşteri Girişi")
        print("2. Yönetici Girişi")
        print("3. Sistemden Çıkış")
        
        secim = input("Lütfen bir işlem seçin (1-3): ").strip()

        if secim == "1":
            print(f"\nKullanılabilir Masalar: {masa_listesi}")
            try:
                m_no = int(input("Masa numaranızı girin: "))
                if m_no not in masa_listesi:
                    print("Geçersiz masa numarası!")
                    continue
            except ValueError:
                print("Lütfen sadece sayı giriniz!")
                continue

            if m_no not in sistem.aktif_masalar:
                sistem.aktif_masalar[m_no] = Musteri(m_no)
            
            musteri = sistem.aktif_masalar[m_no]

            while True:
                musteri.bilgileri_goster()
                print("1. Menüyü Listele")
                print("2. Sipariş Ver")
                print("3. Hesap İste & Masayı Kapat")
                print("4. Üst Menüye Dön")
                
                m_secim = input("İşleminiz: ").strip()

                if m_secim == "1":
                    sistem.menuyu_goster()
                elif m_secim == "2":
                    sistem.menuyu_goster()
                    secilen_urun = input("İstediğiniz ürünün adını aynen yazın: ").strip()
                    
                    if secilen_urun not in sistem.menu:
                        print("Menüde böyle bir ürün yok!")
                        continue
                    
                    try:
                        adet = int(input("Kaç adet istiyorsunuz?: "))
                        if adet <= 0:
                            print("Adet en az 1 olmalıdır!")
                            continue
                    except ValueError:
                        print("Geçersiz adet!")
                        continue
                    
                    musteri.siparis_ekle(secilen_urun, adet)

                elif m_secim == "3":
                    kapandi_mi = musteri.hesabi_ode_ve_kapat(sistem.menu)
                    if kapandi_mi:
                        del sistem.aktif_masalar[m_no]
                        break
                elif m_secim == "4":
                    break

        elif secim == "2":
            while True:
                admin_paneli.bilgileri_goster()
                print("1. Restoran Menüsünü Göster")
                print("2. Menüyü Güncelle (Ürün Ekle/Fiyat Değiştir)")
                print("3. Dosyadan Satış Raporunu Oku")
                print("4. Sabit Kategorileri Göster")
                print("5. Üst Menüye Dön")
                
                a_secim = input("İşleminiz: ").strip()

                if a_secim == "1":
                    sistem.menuyu_goster()
                elif a_secim == "2":
                    admin_paneli.menuyu_guncelle(sistem)
                elif a_secim == "3":
                    admin_paneli.dosyadan_rapor_oku()
                elif a_secim == "4":
                    print(sistem.kategoriler)
                elif a_secim == "5":
                    break

        elif secim == "3":
            print("\nSistem kapatılıyor. İyi çalışmalar!")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    ana_program()