def hitung_laba():
    # Modal awal
    modal = 100000000
    
    # Array untuk menyimpan laba tiap bulan
    laba_bulanan = []
    
    # Menghitung laba untuk 8 bulan
    for bulan in range(1, 9):
        # Bulan 1 dan 2: belum ada laba
        if bulan <= 2:
            laba = 0
            
        # Bulan 3: mulai dapat laba 1%
        elif bulan == 3:
            laba = modal * 0.01
            
        # Bulan 4: laba tetap 1%
        elif bulan == 4:
            laba = modal * 0.01
            
        # Bulan 5-7: laba naik menjadi 5%
        elif bulan >= 5 and bulan <= 7:
            laba = modal * 0.05
            
        # Bulan 8: laba turun menjadi 3%
        else:
            laba = modal * 0.03
            
        laba_bulanan.append(laba)
        print(f"Laba bulan ke-{bulan} sebesar: {laba:,.1f}")
    
    # Menghitung total laba
    total_laba = sum(laba_bulanan)
    print(f"Total laba adalah: {total_laba:,.1f}")
    
    return total_laba

if __name__ == "__main__":
    hitung_laba()