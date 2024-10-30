from random import random

def generate_random_numbers():
    # Input nilai n dari user
    try:
        n = int(input("Masukkan nilai N: "))
        
        # Validasi input harus positif
        if n <= 0:
            print("Nilai N harus lebih besar dari 0!")
            return
            
        # Counter untuk while loop
        count = 1
        
        # Menggunakan kombinasi while dan for
        while count <= n:
            # Generate bilangan acak
            num = random()
            
            # Cek apakah bilangan lebih kecil dari 0.5
            if num < 0.5:
                print(f"data ke: {count} => {num}")
                count += 1
        
        print("Selesai")
        
    except ValueError:
        print("Input harus berupa angka!")

if __name__ == "__main__":
    generate_random_numbers()