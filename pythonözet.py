metin = "Python Programlama"

# İndeksleme (Sıfırdan başlar)
print(metin[0])   # 'P'
print(metin[-1])  # 'a' (Son eleman)

# Dilimleme (Slicing) -> [başlangıç : bitiş(dahil değil) : adım]
print(metin[0:6])   # 'Python'
print(metin[::-1])  # 'amalmargorP nohtyP' (Metni tersine çevirir)

# En Çok Kullanılan Metotlar
ornek = "  bilişim sistemleri  "
print(ornek.strip())      # "bilişim sistemleri" -> Baş ve sondaki boşlukları siler
print(ornek.upper())      # "  BILIŞIM SISTEMLERI  " -> Büyük harfe çevirir
print(ornek.split(" "))   # ['', '', 'bilişim', 'sistemleri', '', ''] -> Belirtilen karakterden böler, liste yapar

programlar = ["Python", "C", "JavaScript"]

# Eleman Manipülasyonu
programlar.append("SQL")       # Sonuna ekler -> ["Python", "C", "JavaScript", "SQL"]
programlar.insert(1, "Java")   # 1. indekse araya ekler -> ["Python", "Java", "C", ...]
programlar.remove("C")         # Değere göre siler
silinen = programlar.pop(0)    # İndekse göre siler ve silinen elemanı döndürür

# Matematiksel Fonksiyonlar
sayilar = [10, 20, 30, 40]
print(len(sayilar))  # 4 (Eleman sayısı)
print(sum(sayilar))  # 100 (Elemanların toplamı)

# !!! KRİTİK TUZAK: Referans Ataması vs Gerçek Kopyalama
liste_a = [1, 2, 3]
liste_b = liste_a         # Hatalı: Aynı hafıza adresini paylaşırlar! One değişirse diğeri de değişir.
liste_c = liste_a.copy()  # Doğru: Hafızada tamamen bağımsız yeni bir liste açar.

# Tanımlama
gunler = ("Pazartesi", "Salı", "Çarşamba")

# !!! KRİTİK TUZAK: Tek elemanlı tuple tanımlarken SONUNA VİRGÜL KOYMALISIN!
tek_elemanli_hata = ("Python")  # Bu bir String olur!
tek_elemanli_dogru = ("Python",) # Bu bir Tuple olur.

# Tuple değiştirilemez, eleman eklenip silinemez. Sadece + ile yeni tuple birleştirilebilir:
yeni_gunler = gunler + ("Perşembe",)

# Tanımlama ve Tekrarları Engelleme
Veri = [1, 2, 2, 3, 3, 3]
benzersiz_veri = set(veri) # {1, 2, 3} -> Tekrarlar otomatik silindi!

# Eleman Ekleme/Silme
benzersiz_veri.add(4)
benzersiz_veri.remove(2)

# Küme Matematiği (Kesişim ve Birleşim)
kume_a = {1, 2, 3}
kume_b = {3, 4, 5}

print(kume_a & kume_b)  # {3} -> Kesişim (Intersection)
print(kume_a | kume_b)  # {1, 2, 3, 4, 5} -> Birleşim (Union)

ogrenci = {
    "isim": "Yasemin",
    "bolum": "Bilişim Sistemleri Mühendisliği",
    "gpa": 3.85
}

# Veri Çekme ve Güncelleme
print(ogrenci["isim"])  # "Yasemin"
ogrenci["gpa"] = 3.90   # Değeri güncelleme
ogrenci["sinif"] = 1    # Yeni anahtar-değer ekleme

# !!! KRİTİK TUZAK: Olmayan anahtara erişim
# print(ogrenci["yas"])  # KeyError fırlatır ve program ÇÖKER!
print(ogrenci.get("yas", "Kayıt Bulunamadı")) # Güvenli erişim: Çökmez, "Kayıt Bulunamadı" döner.

# Sözlük Metotları
print(list(ogrenci.keys()))   # ['isim', 'bolum', 'gpa', 'sinif'] -> Sadece anahtarlar
print(list(ogrenci.values())) # ['Yasemin', 'Bilişim Sistemleri...', 3.90, 1] -> Sadece değerler
ogrenci.pop("sinif")          # Belirtilen anahtarı ve değerini siler

# Sözlük içinde Liste barındıran yapı
sistem = {
    "kullanicilar": ["eylul_b", "selen_k", "yasemin_d"],
    "aktif": True
}
# En içteki "yasemin_d" değerine ulaşmak:
# Önce sözlük anahtarı, sonra listenin indeksi
print(sistem["kullanicilar"][2])  # "yasemin_d"

# GELİŞMİŞ SENSÖR VERİ TOPLAMA SİMÜLASYONU
okunan_veriler = []
limit = 3

print("--- Güvenli Veri Giriş Modülü ---")
while len(okunan_veriler) < limit:
    ham_girdi = input(f"{len(okunan_veriler) + 1}. Sensör Değerini Giriniz (Örn: 23.4): ").strip()
    
    # 1. TEMİZLİK: Kullanıcı yanlışlıkla virgül girdiyse noktaya çeviriyoruz
    temiz_girdi = ham_girdi.replace(",", ".")
    
    # 2. DOĞRULAMA: Girdi sayısal bir float değer mi kontrolü (Noktayı geçici silerek bakıyoruz)
    if temiz_girdi.replace(".", "", 1).isdigit():
        veri = float(temiz_girdi)
        
        # Sınır Kontrolü (Boundary Check)
        if 0.0 <= veri <= 100.0:
            okunan_veriler.append(veri)
            print(f"-> Veri güvenli listeye eklendi: {veri}")
        else:
            print("⚠️ HATA: Değer 0 ile 100 arasında olmalıdır!")
    else:
        print("⚠️ HATA: Geçersiz sayı formatı! Tekrar deneyin.")

print(f"\nİşleme Hazır Sensör Havuzu: {okunan_veriler}")

# KAFETERYA STOK VE FİYAT YÖNETİM MATRİSİ
# Her anahtar bir ürünü, değerler ise o ürüne ait alt özellikleri (sözlüğü) temsil eder.
kafe_envanter = {
    "Mocha": {"fiyat": 55, "stok": 12, "kategori": "Kahve"},
    "Espresso": {"fiyat": 42, "stok": 0, "kategori": "Kahve"},
    "Cheesecake": {"fiyat": 75, "stok": 5, "kategori": "Tatlı"},
    "Filtre Kahve": {"fiyat": 45, "stok": 20, "kategori": "Kahve"}
}

print("--- Kritik Stok ve Satış Analizi ---")
# .items() metodu bize hem anahtarı (urun_adi) hem de içindeki sözlüğü (detay) aynı anda verir.
for urun_adi, detay in kafe_envanter.items():
    # İç sözlükteki verilere anahtarlarla erişiyoruz
    fiyat = detay["fiyat"]
    stok = detay["stok"]
    
    # Kritik Stok Kontrolü
    if stok == 0:
        print(f"🚨 KRİTİK: {urun_adi} tükenmiştir! Satış yapılamaz.")
    elif stok < 8:
        print(f"⚠️ UYARI: {urun_adi} stoku azalıyor! Kalan: {stok}. Güncel Fiyat: {fiyat} TL")
    else:
        print(f"✅ Güvenli: {urun_adi} stoku yeterli ({stok} adet).")

# SENARYO: Ham veri havuzundaki sıcaklıkları al, anomalileri ayıkla, fahrenheit'a çevir ve raporla.

# 1. Fonksiyon: Sadece filtreleme yapar (Data Filtering)
def anomalileri_süz(ham_liste):
    temiz_veri = []
    for deger in ham_liste:
        # 10 ile 45 derece dışındaki uç değerleri eliyoruz
        if 10 <= deger <= 45:
            temiz_veri.append(deger)
    return temiz_veri

# 2. Fonksiyon: Sadece matematiksel dönüşüm yapar (Data Transformation)
def celcius_to_fahrenheit(celcius_listesi):
    fahrenheit_listesi = []
    for c in celcius_listesi:
        f = (c * 9/5) + 32
        fahrenheit_listesi.append(f)
    return fahrenheit_listesi

# 3. Fonksiyon: Gelen verileri analiz edip çoklu return yapar (Data Aggregation)
def istatistik_ozet(nihai_liste):
    if not nihai_liste: # Liste boşsa hatayı engelle
        return 0, 0
        
    toplam = 0
    en_yuksek = nihai_liste[0]
    
    for deger in nihai_liste:
        toplam += deger
        if deger > en_yuksek:
            en_yuksek = deger
            
    ortalama = toplam / len(nihai_liste)
    return ortalama, en_yuksek # Çift return (Unpacking için)

# --- ANA SİSTEM HATTI (PIPELINE) ---
fabrika_ham_verileri = [22.5, -5.0, 30.2, 85.0, 19.8, 40.0]

# Adım 1: Ham veriyi temizle
temiz_celcius = anomalileri_süz(fabrika_ham_verileri) 
# temiz_celcius artık: [22.5, 30.2, 19.8, 40.0]

# Adım 2: Temiz veriyi dönüştür
donusmus_fahrenheit = celcius_to_fahrenheit(temiz_celcius)

# Adım 3: İstatistikleri çıkar ve Unpacking ile değişkenlere yükle
ort_sicaklik, maks_sicaklik = istatistik_ozet(donusmus_fahrenheit)

print("--- Fabrika Sistem Raporu ---")
print(f"İşlem Gören Dönüştürülmüş Veriler (F): {donusmus_fahrenheit}")
print(f"Sistem Ortalama Sıcaklığı: {ort_sicaklik:.2f} F")
print(f"Sistem Tepe Sıcaklığı: {maks_sicaklik} F")


# SENARYO: Bir sistemde yasaklı kelimeler veya siber tehdit unsurları aranıyor.
def tehdit_analizi(log_mesajlari, kritik_kelimeler):
    # Bu fonksiyon iç içe döngülerle tüm metinleri tarar
    for log in log_mesajlari:
        # Log mesajını kelimelerine ayırıp küçük harfe çekiyoruz
        kelimeler = log.lower().split()
        
        for kelime in kelimeler:
            if kelime in kritik_kelimeler:
                # KRİTİK: Tehdit bulunduğu an fonksiyon ALT DÖNGÜLERİ BEKLEMEDEN anında True döner ve kapanır!
                return True 
                
    # Eğer tüm loglar ve kelimeler hatasız tarandıysa ve yukarıdaki return tetiklenmediyse:
    # Bu satır en dıştaki 'for' döngüsünün BİTİŞ hizasındadır.
    return False

# Test Yapısı
sistem_loglari = [
    "Sistem basariyla baslatildi",
    "Kullanici girisi hatali deneme",
    "Veritabanina yetkisiz malware saldirisi tespit edildi"
]
tehditler = ["malware", "virus", "hack", "ransomware"]

if threat_found := threat_analysis(system_logs, threats): # Python 3.8+ walrus operatörü ile doğrudan atama ve kontrol
    print("🚨 ACİL DURUM: Sistemde siber tehdit unsuru bulundu!")
else:
    print("✅ GÜVENLİ: Temiz sistem logları.")


# =============================================================================
# 1. ADIM: VERİ SANİTASYON MODÜLÜ (String Temizleme)
# =============================================================================
def veri_sanitize(barkod):
    # Gelen metni tamamen küçük harfe çeviriyoruz (Örn: "Şeftali" -> "şeftali")
    temiz_metin = barkod.lower()
    
    # Türkçe karakterleri İngilizce karşılıklarıyla değiştiriyoruz
    # .replace() metodu zincirleme (peş peşe) kullanılabilir
    temiz_metin = temiz_metin.replace("ş", "s")
    temiz_metin = temiz_metin.replace("ç", "c")
    temiz_metin = temiz_metin.replace("ı", "i")
    temiz_metin = temiz_metin.replace("ğ", "g")
    temiz_metin = temiz_metin.replace("ü", "u")
    temiz_metin = temiz_metin.replace("ö", "o")
    
    return temiz_metin


# =============================================================================
# 2. ADIM: KALİTE VE FİYAT KONTROL MODÜLÜ (Sözlük ve Şart Blokları)
# =============================================================================
def kalite_ve_fiyat_kontrol(urun_adi, agirlik):
    # Tesisin kalite ve birim fiyat kriterlerini tutan iç içe sözlük (Global/Yerel Veri)
    urun_kriterleri = {
        "zeytin": {"birim_fiyat": 60, "min_agirlik": 10.0},
        "seftali": {"birim_fiyat": 45, "min_agirlik": 15.0},
        "incir": {"birim_fiyat": 80, "min_agirlik": 8.0}
    }
    
    # Kural 1: Ürün sözlükte tanımlı mı?
    if urun_adi not in urun_kriterleri:
        print(f"❌ Reddedildi: '{urun_adi}' tanımsız bir üründür.")
        return False, 0  # Unpacking için çift değer döndürüyoruz
        
    # Sözlükten o ürüne ait alt özellikleri çekiyoruz
    kriter = urun_kriterleri[urun_adi]
    min_kabul_agirligi = kriter["min_agirlik"]
    birim_fiyati = kriter["birim_fiyat"]
    
    # Kural 2: Ağırlık kalite standardına uygun mu?
    if agirlik < min_kabul_agirligi:
        print(f"❌ Reddedildi: '{urun_adi}' düşük kalite/eksik ağırlık. (Mevcut: {agirlik} kg, Gerekli: {min_kabul_agirligi} kg)")
        return False, 0
        
    # Kural 3: Şartlar sağlanıyorsa bütçe hesabı yapılıyor
    toplam_tutar = agirlik * birim_fiyati
    print(f"✅ Kabul Edildi: '{urun_adi}' ({agirlik} kg) -> Tutar: {toplam_tutar} TL")
    return True, toplam_tutar


# =============================================================================
# 3. ADIM: LOJİSTİK DAĞITIM VE PIPELINE MODÜLÜ (Ana İş Motoru)
# =============================================================================
def lojistik_dagitim(depo_girdileri):
    kamyon_A = []  # Hafif/Ucuz Sevkiyat (Tutar <= 800)
    kamyon_B = []  # Ağır/Pahalı Sevkiyat (Tutar > 800)
    
    print("--- 🚜 TARIM TESİSİ GİRİŞ DENETİMİ BAŞLADI 🚜 ---\n")
    
    for kasa in depo_girdileri:
        ham_barkod = kasa[0]
        agirlik = kasa[1]
        
        # 1. VERİ PARÇALAMA: "Şeftali_Kasa_1" metnini "_" işaretinden bölüp ilk parçayı alıyoruz
        # .split("_") bize ["Şeftali", "Kasa", "1"] listesini verir, [0] ile ilk elemanı seçeriz.
        ham_urun_adi = ham_barkod.split("_")[0]
        
        # 2. VERİ TEMİZLEME: İlk yazdığımız fonksiyonu çağırıp ismi temizliyoruz
        temiz_urun_adi = veri_sanitize(ham_urun_adi)
        
        # 3. KALİTE KONTROL: Temiz ismi ve ağırlığı kalite kontrol fonksiyonuna gönderiyoruz
        # Fonksiyondan dönen iki değeri UNPACKING yöntemiyle onay ve kasa_tutari değişkenlerine yıkıyoruz
        onay, kasa_tutari = kalite_ve_fiyat_kontrol(temiz_urun_adi, agirlik)
        
        # 4. LOJİSTİK ROTALAMA: Onay durumuna ve bütçeye göre kamyon seçimi
        if onay == True:
            if kasa_tutari <= 800:
                kamyon_A.append([temiz_urun_adi, kasa_tutari])
            else:
                kamyon_B.append([temiz_urun_adi, kasa_tutari])
                
    print("\n--- 🚜 DENETİM BİTTİ, LOJİSTİK ARAÇLAR SEVKE HAZIR 🚜 ---")
    return kamyon_A, kamyon_B


# =============================================================================
# 4. ADIM: ANA PROGRAM (Sistemin Çalıştırılması)
# =============================================================================

# Sınavda verilen ham test verisi
gelen_kasalar = [
    ["Şeftali_Kasa_1", 20.0],  # Temizlenecek seftali olacak, 20*45=900 TL > Kamyon B
    ["Zeytin_Kasa_2", 5.0],    # Temizlenecek zeytin olacak, min_agirlik 10 altı > ELENECEK
    ["İncir_Kasa_A", 12.0],    # Temizlenecek incir olacak, 12*80=960 TL > Kamyon B
    ["Mango_Kasa_X", 15.0]     # Sözlükte yok > ELENECEK
]

# Dağıtım motorunu çalıştırıp dönen araç listelerini teslim alıyoruz
kamyon_marmara_ici, kamyon_marmara_disi = lojistik_dagitim(gelen_kasalar)

# Final Raporunu Ekrana Basıyoruz
print("\n================ FINAL LOJİSTİK RAPORU ================")
print(f"🚛 KAMYON A (Marmara İçi / Hafif Sevkiyat): {kamyon_marmara_ici}")
print(f"🚛 KAMYON B (Marmara Dışı / Ağır Sevkiyat) : {kamyon_marmara_disi}")
print("=======================================================")