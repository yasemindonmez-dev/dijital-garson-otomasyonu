"""pin_kodu="1802"
bakiye=5000
hak=3
while hak>0:
    girilen_pin=input("Pin kodunuzu giriniz:")

    if girilen_pin==pin_kodu:
        print("Hesabınıza giriş yapılıyor")
        break
    else:
        hak-=1
        if hak>0:
            print(f"Yanlış şifre girdiniz. Kalan hakkınız: {hak}")
        else:
            print("Yanlış şifre! Kartınız bloke ediliyor...")

if hak>0:
    while True:
        print("1-Bakiye Sorgula")
        print("2-Para Çek")
        print("3-Çıkış")

        secim=input("Yapmak istediğiniz işlemi seçiniz:")

        if secim=="1":
            print(f"Hesabınızdaki bakiye: {bakiye}")
        
        elif secim=="2":
            cekilecek_tutar=int(input("Çekmek istediğiniz tutarı giriniz:"))
            if cekilecek_tutar>bakiye:
                print("Yetersiz bakiye!")
            else:
                bakiye-=cekilecek_tutar
                print(f"İşlem başarılı. Çekilen tutar:{cekilecek_tutar}")
                print(f"Kalan para miktarı:{bakiye}TL")
        elif secim=="3":
            print("Güvenli çıkış yapılıyor...")
            break
        else:
            print("Geçersiz sayı girdiniz.Tekrar deneyin.")


def sifre_kontrol(sifre):
    uzunluk=False
    buyuk_harf=False
    rakam=False

    if len(sifre)>=8:
        uzunluk=True
    
    for karakter in sifre:
        if karakter.isupper():
            buyuk_harf=True
        if karakter.isdigit():
            rakam=True

    if uzunluk==True and buyuk_harf==True and rakam==True:
        return True
    else:
        return False
    
kullanici_sifresi=input("Bir şifre belirleyin:")
sonuc=sifre_kontrol(kullanici_sifresi)
if sonuc==True:
    print("Şifreniz kabul edildi.")
else:
    print("Şifreniz kabul edilmedi. Kurallara dikkat ediniz.")

menu = {"Filtre Kahve": 45, "Mocha": 55, "Espresso": 42}

def siparis_hesapla(sepet):
    toplam_tutar=0

    for urun in sepet:
        toplam_tutar+=menu[urun]
    
    return toplam_tutar

musterı_sepeti=[]

print("Dijital Kafemize Hoşgeldiniz!")
print("Menümüz:",list(menu.keys()))
print("Bitirmek için tamam yazın."),

while True:
    secim=input("Sepete eklemek istediğiniz ürünün adını yazınız:")

    if secim.lower()=="tamam":
        break

    if secim in menu:
        musterı_sepeti.append(secim)
        print(f"{secim} sepetinize eklendi.")
    else:
        print("Hatalı giriş. Bu ürün bulunmamaktadır.")

print(f"Satın aldığınız ürünler:{musterı_sepeti}")
toplam_hesap=siparis_hesapla(musterı_sepeti)

print(f"Toplam ödeyeceğiniz tutar:{toplam_hesap}TL")


sicakliklar = [22, 19, 45, 85, 23, 52, 30, -5]

def anomali_temizle(veri_listesi):
    temiz_liste=[]

    for i in veri_listesi:

        if i<20 or i>50:
            print("Hatalı veri.")
        else:
            temiz_liste.append(i)

    return temiz_liste

temiz_veri=anomali_temizle(sicakliklar)
print("Son liste:",temiz_veri)

def sezar_sifrele(metin,kaydirma_mikari):
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    sifreli_metin=""

    kucuk_metin=metin.lower()

    for karakter in kucuk_metin:

        if karakter==" ":
            sifreli_metin+=" "

        elif karakter in alfabe:
            mevcut_index=alfabe.index(karakter)
            yeni_index=(mevcut_index+kaydirma_mikari)%26
            sifreli_metin+=alfabe[yeni_index]
        else:
            sifreli_metin+=karakter
    return sifreli_metin

orijinal_mesaj=input("Şifrelenecek mesajı girin:")
adim_sayisi=int(input("Kaç adım kaydırılsın?"))

gizli_mesaj=sezar_sifrele(orijinal_mesaj,adim_sayisi)
print(f"Orijinal mesaj:{orijinal_mesaj}")
print(f"Kripto mesaj:{gizli_mesaj}")

def kargo_duzenle(paketler_listesi):
    hafif_arac=[]
    agir_arac=[]

    for paket in paketler_listesi:
        en=paket[0]
        boy=paket[1]
        yukseklik=paket[2]

        desi=(en*boy*yukseklik)/3000

        if desi <= 15:
            hafif_arac.append(paket)
        else:
            agir_arac.append(paket)
    
    return hafif_arac,agir_arac

gelen_paketler = [[20, 30, 40], [50, 60, 70], [10, 15, 20], [80, 80, 50]]
hafif_paketi_tasiyanlar,agir_paketi_tasiyanlar=kargo_duzenle(gelen_paketler)

print(f"Hafif dağıtım aracı paketleri:{hafif_paketi_tasiyanlar}")
print(f"Ağır dağıtım aracı paketleri:{agir_paketi_tasiyanlar}")

def harf_notu_hesapla(vize,final):
    ortalama=(vize*0.4)+(final*0.6) 

    if ortalama>=85:
        return "AA"
    elif ortalama>=70:
        return "BB"
    elif ortalama>=50:
        return "CC"
    else:
        return "FF"  

def sinif_analizi(ogrenci_notlari):
    kalanlar=0
    gecenler=0

    for ogrenci in ogrenci_notlari:
        v_not=ogrenci[0]
        f_not=ogrenci[1]

        ogrenci_harf_notu=harf_notu_hesapla(v_not,f_not)

        if ogrenci_harf_notu=="FF":
            kalanlar+=1
        else:
            gecenler+=1

    return kalanlar,gecenler


sinif_notlari = [[40, 45], [80, 90], [70, 65], [30, 50]]
kalan_sayisi,gecen_sayisi=sinif_analizi(sinif_notlari)

print(f"Dersten geçen öğrenci sayısı:{gecen_sayisi}")
print(f"Dersten kalan öğrenci sayısı:{kalan_sayisi}")

def mukemmel_sayi_mi(sayi):
    bolenler_toplami=0
    for i in range(1,sayi):
        if sayi%i==0:
            bolenler_toplami+=i
    if bolenler_toplami==sayi:
        return True
    else:
        return False
        
def listeyi_suz(ana_liste):
    mukemmel_sayilar=[]
    for i in ana_liste:
        if mukemmel_sayi_mi(i)==True:
            mukemmel_sayilar.append(i)
    return mukemmel_sayilar



sayi_havuzu = [6, 10, 28, 35, 496, 50, 12]

print(f"Mükemmel sayılar listesi:{listeyi_suz(sayi_havuzu)}")

def marmara_mi(sehir_ismi):
    marmara_sehirleri = ["bursa", "istanbul", "kocaeli", "balikesir", "canakkale"]
    temiz_sehir=sehir_ismi.lower()

    if temiz_sehir in marmara_sehirleri:
        return True
    else:
        return False
    
def siparisleri_ayristir(siparis_listesi):
    marmara_lojistik=[]
    dis_lojistik=[]

    for siparis in siparis_listesi:
        siparis_id=siparis[0]
        sehir=siparis[1]
        tutar=siparis[2]

        if marmara_mi(sehir)==True:
            marmara_lojistik.append([siparis_id,tutar])
        else:
            dis_lojistik.append([siparis_id,tutar])
    return marmara_lojistik,dis_lojistik


gelen_siparisler = [[101, "Bursa", 450], [102, "Ankara", 1200], [103, "Istanbul", 850], [104, "Izmir", 600]]
marmara_paketleri,dis_paketler=siparisleri_ayristir(gelen_siparisler)
print(f"Marmara Lojistik Firması (Sipariş ID, Tutar): {marmara_paketleri}")
print(f"Dış Lojistik Firması (Sipariş ID, Tutar)   : {dis_paketler}")

def sifre_guvenli_mi(sifre):
    uzunluk_tamam=False
    sayi_var=False
    ozel_karakter_var=False

    if len(sifre)>=6:
        uzunluk_tamam=True

    for karakter in sifre:
        if karakter.isdigit():
            sayi_var=True
        elif karakter in "*.-":
            ozel_karakter_var=True

    if uzunluk_tamam==True and sayi_var==True and ozel_karakter_var==True:
        return True
    else:
        return False

girilen_sifre=input("Bir şifre giriniz:")
if sifre_guvenli_mi(girilen_sifre)==True:
    print("Şifreniz güvenli.")
else:
    print("Güvenli değil. Tekrar deneyiniz.")"

def veri_sanitize(barkod):
    temiz_metin=barkod.lower()
    temiz_metin=temiz_metin.replace("ş","s")
    temiz_metin = temiz_metin.replace("ç", "c")
    temiz_metin = temiz_metin.replace("ı", "i")
    temiz_metin = temiz_metin.replace("ğ", "g")
    temiz_metin = temiz_metin.replace("ü", "u")
    temiz_metin = temiz_metin.replace("ö", "o")

    return temiz_metin

def kalite_fiyat_kontrol(urun_adi,agirlik):
    urun_kriterleri = {
    "zeytin": {"birim_fiyat": 60, "min_agirlik": 10.0},
    "seftali": {"birim_fiyat": 45, "min_agirlik": 15.0},
    "incir": {"birim_fiyat": 80, "min_agirlik": 8.0}}

    if urun_adi not in urun_kriterleri:
        print(f"Tanımsız ürün. {urun_adi} bulunamadı.")
        return False,0
    
    kriter=urun_kriterleri[urun_adi]
    min_kabul_agirligi=kriter["min_agirlik"]
    birimFiyat=kriter["birim_fiyat"]

    if agirlik<min_kabul_agirligi:
        print("Düşük kalite, eksik ağırlık.")
        return False,0
    
    toplam_tutar=agirlik*birimFiyat
    print(f"Kabul edildi.Toplam tutar:{toplam_tutar}")
    return True,toplam_tutar

def lojistik_dagitim(depo_girdileri):
    kamyon_A=[]
    kamyon_B=[]

    for kasa in depo_girdileri:
        ham_barkod=kasa[0]
        agirlik=kasa[1]

        ham_urun_adi=ham_barkod.split("_")[0]
        temiz_urun_adi=veri_sanitize(ham_urun_adi)

        onay,kasa_tutari=kalite_fiyat_kontrol(temiz_urun_adi,agirlik)

        if onay==True:
            if kasa_tutari<=800:
                kamyon_A.append([temiz_urun_adi,kasa_tutari])
            else:
                kamyon_B.append([temiz_urun_adi,kasa_tutari])

    return kamyon_A,kamyon_B


gelen_kasalar = [
    ["Şeftali_Kasa_1", 20.0],  # Temizlenecek seftali olacak, 20*45=900 TL > Kamyon B
    ["Zeytin_Kasa_2", 5.0],    # Temizlenecek zeytin olacak, min_agirlik 10 altı > ELENECEK
    ["İncir_Kasa_A", 12.0],    # Temizlenecek incir olacak, 12*80=960 TL > Kamyon B
    ["Mango_Kasa_X", 15.0]     # Sözlükte yok > ELENECEK
]

kamyon_marmara_ici,kamyon_marmara_disi=lojistik_dagitim(gelen_kasalar)
print(f"🚛 KAMYON A (Marmara İçi / Hafif Sevkiyat): {kamyon_marmara_ici}")
print(f"🚛 KAMYON B (Marmara Dışı / Ağır Sevkiyat) : {kamyon_marmara_disi}")

def kart_tipi_ve_ucret_bul(kart_kodu):
    tarifeler = {
    "ogrenci": 5.5,
    "tam": 14.0,
    "yasli": 0.0}

    temiz_kod=kart_kodu.lower()
    if temiz_kod in tarifeler:
        return tarifeler[temiz_kod]
    else:
        return -1
    

def istasyon_denetimi(yolcu_listesi):
    gecen_yolcular=[]
    reddedilen_yolcular=[]

    for yolcu in yolcu_listesi:

        ham_isim=yolcu[0]
        kart_tipi=yolcu[1]
        mevcut_bakiye=yolcu[2]

        temiz_isim=ham_isim.strip()
        gecis_ucreti=kart_tipi_ve_ucret_bul(kart_tipi)

        if gecis_ucreti==-1:
            print(f"❌ Turnike Açılmadı: {temiz_isim} -> Nedeni: Geçersiz Kart Tipi ('{kart_tipi}')")
            reddedilen_yolcular.append([temiz_isim,"Geçersiz Kart"])
        elif mevcut_bakiye<gecis_ucreti:
            print(f"❌ Turnike Açılmadı: {temiz_isim} -> Nedeni: Yetersiz Bakiye (Mevcut: {mevcut_bakiye} TL, Gerekli: {gecis_ucreti} TL)")
            reddedilen_yolcular.append([temiz_isim,"Yetersiz Bakiye"])
        else:
            yeni_bakiye = mevcut_bakiye - gecis_ucreti
            print((f"✅ Turnike Açıldı: {temiz_isim} -> Geçiş Türü: {kart_tipi.upper()} (Kalan Bakiye: {yeni_bakiye} TL)"))
            gecen_yolcular.append([temiz_isim,yeni_bakiye])

    return gecen_yolcular,reddedilen_yolcular

turnike_kuyrugu = [
    ["  Yasemin Donmez  ", "ogrenci", 50.0],  # Boşluklar silinecek, bakiye düşecek, geçecek
    ["Eylul Yilmaz", "tam", 10.0],             # Bakiyesi 14 TL'den az, yetersiz bakiyeden reddedilecek
    [" Selen Kaya ", "yasli", 5.0],            # Ücretsiz geçecek (0 TL), bakiyesi değişmeyecek
    ["Melis Demir", "misafir", 100.0]          # Sözlükte yok, geçersiz karttan reddedilecek
]

onaylananlar,reddedilenler=istasyon_denetimi(turnike_kuyrugu)
print(f"🟢 GEÇEN YOLCULAR (İsim, Kalan Bakiye): {onaylananlar}")
print(f"🔴 REDDEDİLEN YOLCULAR (İsim, Gerekçe): {reddedilenler}")

def temiz_kod_bul(ham_kod):
    parcalar=ham_kod.split("_")
    temiz_kod=f"{parcalar[1]}_{parcalar[2]}".lower()
    return temiz_kod

def depo_stok_guncelle(talep_listesi):
    onaylanan_talepler=[]
    tedarik_talepleri=[]

    depo_stoklari = {
    "vida_12": 150,
    "somun_08": 80,
    "rulman_05": 30}

    for talep in talep_listesi:
        ham_kod=talep[0]
        talep_edilen_miktar=talep[1]

        temiz_kod=temiz_kod_bul(ham_kod)

        if temiz_kod not in depo_stoklari:
            print(f"🚨 STOKTA YOK: '{temiz_kod}' depoda bulunamadı! {talep_edilen_miktar} adet tedarik talebi açıldı.")
            tedarik_talepleri.append([temiz_kod,talep_edilen_miktar])
        elif depo_stoklari[temiz_kod]<talep_edilen_miktar:
            mevcut_stok=depo_stoklari[temiz_kod]
            eksik_miktar=talep_edilen_miktar-depo_stoklari[temiz_kod]
            print(f"⚠️ YETERSİZ STOK: '{temiz_kod}' için talep {talep_edilen_miktar} adet, stokta kalan {mevcut_stok} adet.")
            print(f"   -> {mevcut_stok} adet sevk edildi. Kalan {eksik_miktar} adet için tedarik talebi açıldı.")

            onaylanan_talepler.append([temiz_kod,mevcut_stok])
            tedarik_talepleri.append([temiz_kod,eksik_miktar])
            depo_stoklari[temiz_kod]=0
        else:
            depo_stoklari[temiz_kod]-=talep_edilen_miktar
            print(f"✅ STOK ONAYLANDI: '{temiz_kod}' için {talep_edilen_miktar} adet sevk edildi. (Kalan Depo Stoku: {depo_stoklari[temiz_kod]})")
            onaylanan_talepler.append([temiz_kod,talep_edilen_miktar])

    return onaylanan_talepler,tedarik_talepleri

robot_talepleri = [
    ["M_vida_12", 50],    # Temizlenecek (vida_12), stok yeterli, düşecek ve onaylanacak.
    ["A_rulman_05", 45],  # Temizlenecek (rulman_05), stok 30 tane var. 30'u onaylanacak, 15 tanesi tedariğe yazılacak.
    ["R_somun_08", 90],   # Temizlenecek (somun_08), stok 80 tane var. 80'i onaylanacak, 10 tanesi tedariğe yazılacak.
    ["M_sensor_01", 5] ]   # Depoda yok, direkt 5 tane tedariğe yazılacak.

onaylananlar,tedarik_edilecekler=depo_stok_guncelle(robot_talepleri)
print(f"🟢 ROBOTLARA SEVK EDİLEN PARÇALAR: {onaylananlar}")
print(f"🔴 SATIN ALMAYA GÖNDERİLEN TEDARİK TALEPLERİ: {tedarik_edilecekler}")

def fabrika_kodu_temizle(ham_kod):
    temiz_kod=ham_kod.split("-")[1]
    return temiz_kod.lower()

def enerji_analizi(tuketim_listesi):
    normal_tuketim=[]
    tasarruflu_fabrikalar=[]

    for fabrika in tuketim_listesi:
        ham_kod=fabrika[0]
        tuketim_degeri=fabrika[1]

        if tuketim_degeri<=0:
            print(f"🚨 HATALI VERİ ENGELLENDİ: '{ham_kod}' için gelen tüketim değeri ({tuketim_degeri}) geçersizdir! İşlem dışı bırakıldı.")
            continue

        temiz_kod=fabrika_kodu_temizle(ham_kod)

        if tuketim_degeri<=150:
            print(f"🌱 Tasarruflu Tüketim: '{temiz_kod}' -> {tuketim_degeri} kWh")
            tasarruflu_fabrikalar.append([temiz_kod,tuketim_degeri])
        else:
            print(f"🏭 Normal Tüketim: '{temiz_kod}' -> {tuketim_degeri} kWh")
            normal_tuketim.append([temiz_kod,tuketim_degeri])

    return normal_tuketim,tasarruflu_fabrikalar

saha_verileri = [
    ["OSB-tekstil_01", 250],   # Temizlenecek (tekstil_01), normal tüketime eklenecek.
    ["OSB-otomotiv_02", 120],  # Temizlenecek (otomotiv_02), tasarruflu listesine eklenecek.
    ["OSB-gida_03", -40],      # Negatif değer! Hatalı veri olduğu için tamamen göz ardı edilecek.
    ["OSB-kimya_04", 150]]  

normaller,tasarruflular=enerji_analizi(saha_verileri)
print(f"🟢 NORMAL/YÜKSEK TÜKETİM YAPAN FABRİKALAR: {normaller}")
print(f"🔵 TASARRUFLU (DESTEKLENECEK) FABRİKALAR   : {tasarruflular}")"""














