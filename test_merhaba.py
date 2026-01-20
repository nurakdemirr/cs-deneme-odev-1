import subprocess

def test_calistir():
    # Öğrencinin yazdığı merhaba.py dosyasını çalıştırır
    sonuc = subprocess.run(["python", "merhaba.py"], capture_output=True, text=True)
    cikti = sonuc.stdout.strip() # Boşlukları temizle

    # Beklenen sonuç kontrolü
    beklenen = "Merhaba Dünya"

    if cikti == beklenen:
        print("✅ TEST GEÇTİ! Tebrikler.")
    else:
        print(f"❌ TEST KALDI. Beklenen: '{beklenen}', Senin çıktın: '{cikti}'")
        exit(1) # Hata kodu döndür ki GitHub 'Kırmızı Çarpı' göstersin.

if __name__ == "__main__":
    test_calistir()
