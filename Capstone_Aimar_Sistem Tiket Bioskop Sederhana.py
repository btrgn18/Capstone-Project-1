import prettytable
import time
import pwinput
# Data film
films = [
    {
        "id": 1,
        "judul": "1 KAKAK 7 PONAKAN",
        "rating": "SU",
        "durasi": "2 jam 15 menit",
        "waktu_penayangan": ["11:00", "13:30", "14:00", "16:45"],
        "harga": 35000,
        "studio": ["Studio 1a", "Studio 3b", "Studio 2b", "Studio 2c"],
        "kursi": [
            ["1A", "2A", "3A", "4A", "5A", "6A", "7A", "8A"],
            ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B"],
            ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C"],
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D"],
            ["1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E"]
        ]
    },
    {
        "id": 2,
        "judul": "ATTACK ON TITAN: THE LAST ATTACK",
        "rating": "D 17+",
        "durasi": "2 jam 30 menit",
        "waktu_penayangan": ["11:00", "13:45", "18:45", "19:15"],
        "harga": 35000,
        "studio": ["Studio 2a", "Studio 1b", "Studio 3d", "Studio 1d"],
        "kursi": [
            ["1A", "2A", "3A", "4A", "5A", "6A", "7A", "8A"],
            ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B"],
            ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C"],
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D"],
            ["1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E"]
        ]
    },
    {
        "id": 3,
        "judul": "CAPTAIN AMERICA: BRAVE NEW WORLD",
        "rating": "R 13+",
        "durasi": "2 jam 30 menit",
        "waktu_penayangan": ["11:00", "16:15", "16:45", "19:30"],
        "harga": 35000,
        "studio": ["Studio 3a", "Studio 3c", "Studio 1c", "Studio 2d"],
        "kursi": [
            ["1A", "2A", "3A", "4A", "5A", "6A", "7A", "8A"],
            ["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B"],
            ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C"],
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D"],
            ["1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E"]
        ]
    }
]

# Data login
users = {
    "stark": {"password": "stark123", "role": "owner"},
    "owner": {"password": "owner", "role": "owner"},
    "jarvis": {"password": "jarvis123", "role": "admin"},
    "admin": {"password": "admin", "role": "admin"},
    "guest": {"password": "", "role": "guest"}
}

# Data keamanan
keamanan = {
    "owner": {"pertanyaan": "Mission Report?", "jawaban": "16 Desember 1991"},
    "admin": {"pertanyaan": "Apa nama lain Anda?", "jawaban": "Vision"}
}

def tampilkan_daftar_film():
    table = prettytable.PrettyTable()
    table.field_names = ["ID", "Judul Film [Rating]", "Waktu Penayangan", "Harga"]
    for film in films:
        waktu_penayangan = " | ".join(film["waktu_penayangan"])
        table.add_row([film["id"], f"{film['judul']} [{film['rating']}]",
                       waktu_penayangan, film["harga"]])
    print(table)

def tambah_film_baru():
    judul = input("Masukkan judul film: ")
    rating = input("Masukkan rating film: ")
    durasi = input("Masukkan durasi film: ")
    waktu_penayangan = input("Masukkan waktu penayangan (pisahkan dengan koma): ").split(",")
    harga = int(input("Masukkan harga film: "))
    studio = input("Masukkan studio (pisahkan dengan koma): ").split(",")
    kursi = []
    for i in range(len(waktu_penayangan)):
        kursi.append(input(f"Masukkan kursi untuk waktu penayangan {waktu_penayangan[i]} (pisahkan dengan koma): ").split(","))
    films.append({
        "id": len(films) + 1,
        "judul": judul,
        "rating": rating,
        "durasi": durasi,
        "waktu_penayangan": waktu_penayangan,
        "harga": harga,
        "studio": studio,
        "kursi": kursi
    })
    print("Film berhasil ditambahkan.")

def perbarui_informasi_film():
    tampilkan_daftar_film()
    id_film = int(input("Masukkan ID film yang ingin diperbarui: "))
    film = next((film for film in films if film["id"] == id_film), None)
    if film:
        judul = input(f"Masukkan judul film baru ({film['judul']}): ") or film['judul']
        rating = input(f"Masukkan rating film baru ({film['rating']}): ") or film['rating']
        durasi = input(f"Masukkan durasi film baru ({film['durasi']}): ") or film['durasi']
        waktu_penayangan = input(f"Masukkan waktu penayangan baru (pisahkan dengan koma) ({', '.join(film['waktu_penayangan'])}): ").split(",") or film['waktu_penayangan']
        harga = int(input(f"Masukkan harga film baru ({film['harga']}): ")) or film['harga']
        studio = input(f"Masukkan studio baru (pisahkan dengan koma) ({', '.join(film['studio'])}): ").split(",") or film['studio']
        kursi = []
        for i in range(len(waktu_penayangan)):
            kursi.append(input(f"Masukkan kursi baru untuk waktu penayangan {waktu_penayangan[i]} (pisahkan dengan koma) ({', '.join(film['kursi'][i])}): ").split(",") or film['kursi'][i])
        film.update({
            "judul": judul,
            "rating": rating,
            "durasi": durasi,
            "waktu_penayangan": waktu_penayangan,
            "harga": harga,
            "studio": studio,
            "kursi": kursi
        })
        print("Film berhasil diperbarui.")
    else:
        print("Film tidak ditemukan.")

def hapus_acara():
    tampilkan_daftar_film()
    id_film = int(input("Masukkan ID film yang ingin dihapus: "))
    film = next((film for film in films if film["id"] == id_film), None)
    if film:
        films.remove(film)
        print("Film berhasil dihapus.")
    else:
        print("Film tidak ditemukan.")

def hapus_acara_otomatis():
    waktu_sekarang = time.time()
    for film in films[:]:
        for waktu in film["waktu_penayangan"]:
            waktu_penayangan = time.strptime(waktu, "%H:%M")
            waktu_penayangan = time.mktime((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday,
                                           waktu_penayangan.tm_hour, waktu_penayangan.tm_min, 0, 0, 0, 0))
            if waktu_sekarang > waktu_penayangan + 90 * 60:  # 90 menit setelah waktu penayangan
                films.remove(film)
                break
    for film in films[:]:
        waktu_rilis = time.strptime(film["waktu_penayangan"][0], "%H:%M")
        waktu_rilis = time.mktime((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday,
                                   waktu_rilis.tm_hour, waktu_rilis.tm_min, 0, 0, 0, 0))
        if waktu_sekarang > waktu_rilis + 7 * 24 * 60 * 60:  # 7 hari setelah waktu rilis
            films.remove(film)

def login():
    print("Selamat Datang di Stark Corp. Cinema!")
    print("|==Menu Login==|")
    print("1. Login as Stark Corp. Owner/Admin")
    print("2. Login as Guest")
    pilihan = input("Pilih (1/2): ")
    if pilihan == "1":
        username = input("Masukkan username Anda: ").lower()
        password = pwinput.pwinput("Masukkan kata sandi Anda: ").lower()
        if username not in users or users[username]["password"] != password:
            print("Username Anda tidak cocok dengan kata sandi. Harap masukkan username dan kata sandi kembali.")
            for i in range(2):
                username = input("Masukkan username Anda: ").lower()
                password = pwinput.pwinput("Masukkan kata sandi Anda: ").lower()
                if username in users and users[username]["password"] == password:
                    break
                else:
                    print("Username Anda tidak cocok dengan kata sandi. Harap masukkan username dan kata sandi kembali.")
            else:
                print("Siapa Anda?")
                print("1. Owner")
                print("2. Admin")
                pilihan_keamanan = input("Pilih (1/2): ")
                if pilihan_keamanan == "1":
                    jawaban = input(f"{keamanan['owner']['pertanyaan']}: ").lower()
                    if jawaban == keamanan['owner']['jawaban']:
                        print(f"Username: {username}")
                        print(f"Password: {password}")
                        time.sleep(10)
                        return login()
                    else:
                        for i in range(2):
                            jawaban = input(f"{keamanan['owner']['pertanyaan']}: ").lower()
                            if jawaban == keamanan['owner']['jawaban']:
                                print(f"Username: {username}")
                                print(f"Password: {password}")
                                time.sleep(10)
                                return login()
                            else:
                                print("Jawaban Anda salah, coba lagi.")
                        else:
                            print("Harap menghubungi Admin.")
                            return login()
                elif pilihan_keamanan == "2":
                    jawaban = input(f"{keamanan['admin']['pertanyaan']}: ").lower()
                    if jawaban == keamanan['admin']['jawaban']:
                        print(f"Username: {username}")
                        print(f"Password: {password}")
                        time.sleep(10)
                        return login()
                    else:
                        for i in range(2):
                            jawaban = input(f"{keamanan['admin']['pertanyaan']}: ").lower()
                            if jawaban == keamanan['admin']['jawaban']:
                                print(f"Username: {username}")
                                print(f"Password: {password}")
                                time.sleep(10)
                                return login()
                            else:
                                print("Jawaban Anda salah, coba lagi.")
                        else:
                            print("Jarvis123")
                            time.sleep(3)
                            return login()
                else:
                    print("Pilihan tidak valid.")
                    return login()
        return username, users[username]["role"]
    elif pilihan == "2":
        return "guest", "guest"
    else:
        print("Pilihan tidak valid.")
        return login()

def menu_utama(role):
    while True:
        print("|==Menu Utama==|")
        print("1. Tampilkan Daftar Film")
        print("2. Tambah Film Baru")
        print("3. Perbarui Informasi Film")
        print("4. Hapus Film")
        print("5. Keluar/Log Out")
        pilihan = input("Pilih Menu (1/5): ")
        if pilihan == "1":
            tampilkan_daftar_film()
            pilih_film()
        elif pilihan == "2" and role in ["owner", "admin"]:
            tambah_film_baru()
        elif pilihan == "3" and role in ["owner", "admin"]:
            perbarui_informasi_film()
        elif pilihan == "4" and role in ["owner", "admin"]:
            hapus_acara_otomatis()
            hapus_acara()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid.")

def pilih_film():
    id_film = int(input("Pilih Film yang ingin Anda Pesan: "))
    film = next((film for film in films if film["id"] == id_film), None)
    if film:
        print(f"\n{film['judul']} [{film['rating']}]")
        print(f"{film['durasi']}")
        for i, waktu in enumerate(film["waktu_penayangan"]):
            print(f"\n{i + 1}. Waktu penayangan {i + 1}")
            print(f"Seat Available at {film['studio'][i]}")
        print("\n00. Kembali ke Daftar Film")
        print("01. Kembali ke Menu Awal")
        pilihan_waktu = input("Pilih Waktu Penayangan: ")
        if pilihan_waktu == "00":
            return
        elif pilihan_waktu == "01":
            return
        elif pilihan_waktu.isdigit() and 1 <= int(pilihan_waktu) <= len(film["waktu_penayangan"]):
            waktu_index = int(pilihan_waktu) - 1
            print(f"\nSeat Available at {film['studio'][waktu_index]}")
            for baris in film["kursi"][waktu_index]:
                print(" | ".join(baris))
            kursi_pilihan = input("Silakan pilih kursi Anda (bisa lebih dari 1): ").split(",")
            if kursi_pilihan:
                konfirmasi = input("Apakah Anda sudah yakin?\n1. Ya\n2. Tidak\nPilih salah satu (1/2): ")
                if konfirmasi == "1":
                    print("\nCetak Tiket")
                    print(f"Judul Film: {film['judul']}")
                    print(f"Waktu Penayangan: {film['waktu_penayangan'][waktu_index]}")
                    print(f"Kursi: {', '.join(kursi_pilihan)}")
                    print(f"Studio: {film['studio'][waktu_index]}")
                    time.sleep(10)
        else:
            print("Pilihan tidak valid.")
    else:
        print("Film tidak ditemukan.")

def main():
    while True:
        username, role = login()
        menu_utama(role)

if __name__ == "__main__":
    main()
