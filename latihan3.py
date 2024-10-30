def atm_program():
    # Inisialisasi saldo awal
    saldo = 1000000
    
    while True:
        # Tampilkan menu dan saldo
        print(f"\nSaldo saat ini: Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")
        
        # Meminta input dari pengguna
        pilihan = input("Pilih menu (1/2): ")
        
        # Proses pilihan menu
        if pilihan == "1":
            while True:
                try:
                    jumlah = int(input("Masukkan jumlah penarikan: "))
                    # Cek apakah jumlah penarikan valid
                    if jumlah > saldo:
                        print("Maaf, saldo Anda tidak mencukupi!")
                    elif jumlah <= 0:
                        print("Jumlah penarikan harus lebih dari 0!")
                    else:
                        saldo -= jumlah
                        print("Penarikan berhasil!")
                        break
                except ValueError:
                    print("Masukkan angka yang valid!")
                    
        elif pilihan == "2":
            print("Terima kasih telah menggunakan ATM!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1 atau 2.")

if __name__ == "__main__":
    atm_program()