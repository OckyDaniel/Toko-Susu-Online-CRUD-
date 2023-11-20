etalase = [
    {'Kode':"101",
     'Nama':'Nutrilon Royal 3 300g',
     'Kategori':'Bayi',
     'Jenis':'Bubuk',
     'Stok': 20, 
     'Harga': 105000},
    {'Kode':"102",
     'Nama':'SGM Eksplor 1+ 600g',
     'Kategori':'Bayi',
     'Jenis':'Bubuk',
     'Stok': 10, 
     'Harga': 63350},
    {'Kode':"103",
     'Nama':'Ultra Mimi FC 125 ML',
     'Kategori':'Anak',
     'Jenis':'Cair',
     'Stok': 120, 
     'Harga': 3500},
     {'Kode':"104",
     'Nama':'Milo UHT 110 ML',
     'Kategori':'Anak',
     'Jenis':'Cair',
     'Stok': 120, 
     'Harga': 3000},
     {'Kode':"105",
     'Nama':'Prenagen Mommy 400g',
     'Kategori':'Hamil',
     'Jenis':'Bubuk',
     'Stok': 20, 
     'Harga': 74000},
     {'Kode':"106",
     'Nama':'Lactamil Pregnasis',
     'Kategori':'Hamil',
     'Jenis':'Bubuk',
     'Stok': 20, 
     'Harga': 74500},
     {'Kode':"107",
     'Nama':'Diabetasol 1000g',
     'Kategori':'Dewasa',
     'Jenis':'Bubuk',
     'Stok': 20, 
     'Harga': 172500},
     {'Kode':"108",
     'Nama':'Entrasol Gold 600g',
     'Kategori':'Dewasa',
     'Jenis':'Bubuk',
     'Stok': 20, 
     'Harga': 103500},
     {'Kode':"109",
     'Nama':'Ultra Milk LF 1000 ML',
     'Kategori':'Dewasa',
     'Jenis':'Cair',
     'Stok': 120, 
     'Harga': 20500},
     {'Kode':"110",
     'Nama':'Greenfield 1000 ML',
     'Kategori':'Dewasa',
     'Jenis':'Cair',
     'Stok': 120, 
     'Harga': 22500},
]


cart = []
def search(kodevar, etalase):
    searched_data = (list(filter(lambda data: data['Kode'] == str(kodevar), etalase)))
    return searched_data


def show(etalase):
    print('\n\t\t\t\t===ETALASE SUSU===\n')
    print('KODE ITEM\t NAMA SUSU\t\t KATEGORI\tJENIS\t STOK\t HARGA')
    for i in range(len(etalase)):
        print('   {}\t|{}\t\t|{}\t\t|{}\t|{}\t|{}'.format(etalase[i]['Kode'], etalase[i]['Nama'],etalase[i]['Kategori'],etalase[i]['Jenis'], etalase[i]['Stok'], etalase[i]['Harga']))


def read(etalase):
    while True:
        pilih = int(input('''
        Menampilkan Daftar Susu:
        1. Daftar Seluruh Susu
        2. Mencari Daftar Susu
        3. Tampilkan Berdasarkan Kategori
        4. Tampilkan Berdasarkan Jenis
        5. Kembali Ke Menu Utama

        Masukkan angka untuk memilih menu: '''))

        if pilih == 1:
            show(etalase)
        
        elif pilih == 2:
            # tampilan pencarian
            kodevar = (input("\n\tMasukkan Kode Untuk Mencari Data [101-109]: "))
            search(kodevar, etalase)
            if len(search(kodevar, etalase)):
                show(search(kodevar, etalase))
            else:
                print("\n\t**Kode Tidak Ditemukan**")

        elif pilih == 3:
            # Menampilkan berdasarkan kategori
            kategori = input("\nMasukkan Kategori Susu [Bayi/Anak/Hamil/Dewasa]: ").capitalize()
            filtered_by_kategori = [item for item in etalase if item['Kategori'] == kategori]
            if filtered_by_kategori:
                show(filtered_by_kategori)
            else:
                print("\nTidak ada susu dengan kategori yang dimasukkan.")

        elif pilih == 4:
            # Menampilkan berdasarkan jenis
            jenis = input("\nMasukkan Jenis Susu [Bubuk/Cair]: ").capitalize()
            filtered_by_jenis = [item for item in etalase if item['Jenis'] == jenis]
            if filtered_by_jenis:
                show(filtered_by_jenis)
            else:
                print("\nTidak ada susu dengan jenis yang dimasukkan.")

        elif pilih == 5:
            break
        else:
            print("\n*Pilihan yang anda masukkan tidak tersedia* ")
            continue


        

def create(etalase):
    kategori_valid = ['Bayi', 'Anak', 'Hamil', 'Dewasa']
    jenis_valid = ['Bubuk', 'Cair']
    
    while True:
        pilih = int(input('''
        1. Tambah Susu
        2. Kembali ke Menu Utama

        Masukkan angka untuk memilih menu: '''))

        if pilih == 1:
            kode = input("\nMasukkan Kode Item: ")
            while any(item['Kode'] == kode for item in etalase):
                print("\n**Kode Item yang sama sudah ada**")
                kode = input("\nMasukkan Kode Item: ")
            
            nama = input("Masukkan Nama Susu: ")
            while any(item['Nama'].lower() == nama.lower() for item in etalase):
                print("\n**Nama susu yang sama sudah ada**")
                nama = input("\nMasukkan Nama Susu: ")
            
            kategori = input("\nMasukkan Kategori Susu [Bayi/Anak/Hamil/Dewasa]: ")
            while kategori.capitalize() not in kategori_valid:
                print("\n**Pilih Salah Satu Kategori [Bayi/Anak/Hamil/Dewasa]**")
                kategori = input("\nMasukkan Kategori Susu [Bayi/Anak/Hamil/Dewasa]: ")
            
            jenis = input("\nMasukkan Jenis Susu [Bubuk/Cair]: ")
            while jenis.capitalize() not in jenis_valid:
                print("\n**Pilih Salah Satu Jenis [Bubuk/Cair]**")
                jenis = input("\nMasukkan Jenis Susu [Bubuk/Cair]: ")
            
            stok = int(input("\nMasukkan Stok Susu: "))
            harga = int(input("\nMasukkan Harga Susu: "))
            
            cek = input("\nApakah data akan disimpan? (Y/N): ").capitalize()
            if cek == 'Y':
                etalase.append({
                    'Kode Item': kode,
                    'Nama': nama,
                    'Kategori': kategori.capitalize(),
                    'Jenis': jenis.capitalize(),
                    'Stok': stok,
                    'Harga': harga
                })
                print("\n**Data berhasil disimpan**")
            else:
                print("\n**Data tidak jadi disimpan**")
        
        elif pilih == 2:
            break
        else:
            print("\n***Pilihan yang anda masukkan tidak tersedia***")



def update(etalase):
    kategori_valid = ['Bayi', 'Anak', 'Hamil', 'Dewasa']
    jenis_valid = ['Bubuk', 'Cair']
    
    while True:
        pilih = int(input('''
        1. Update Etalase
        2. Kembali Ke Menu Utama

        Masukkan angka untuk memilih menu: '''))

        if pilih == 1:
            kodevar = input("\nMasukkan Kode Untuk Mencari Data [101-110]: ")
            hasil_pencarian = search(kodevar, etalase)
            if len(hasil_pencarian):
                show(hasil_pencarian)
            else:
                print("\n**Tidak ada susu dengan kode yang sesuai.**")
                continue
            
            cek = input("Apakah ingin melanjutkan update? [Y/N]: ").capitalize()
            if cek == 'Y': 
                jenis_update = input("Masukkan field yang ingin Anda update?\n1. Nama\n2. Kategori\n3. Jenis\n4. Stok\n5. Harga\nSilahkan pilih angka [1/5]: ")
                
                if jenis_update == '1':
                    nama_baru = input("Masukkan Nama Susu Baru: ")
                    while any(item['Nama'].lower() == nama_baru.lower() for item in etalase):
                        print("\n**Nama susu yang sama sudah ada**")
                        nama_baru = input("\nMasukkan Nama Susu Baru: ")
                
                elif jenis_update == '2':
                    kategori_baru = input("\nMasukkan Kategori Susu Baru [Bayi/Anak/Hamil/Dewasa]: ").capitalize()
                    while kategori_baru not in kategori_valid:
                        print("\n**Pilih Salah Satu Kategori [Bayi/Anak/Hamil/Dewasa]**")
                        kategori_baru = input("\nMasukkan Kategori Susu Baru [Bayi/Anak/Hamil/Dewasa]: ").capitalize()
                
                elif jenis_update == '3':
                    jenis_baru = input("\nMasukkan Jenis Susu Baru [Bubuk/Cair]: ").capitalize()
                    while jenis_baru not in jenis_valid:
                        print("\n**Pilih Salah Satu Jenis [Bubuk/Cair]**")
                        jenis_baru = input("\nMasukkan Jenis Susu Baru [Bubuk/Cair]: ").capitalize()
                
                elif jenis_update == '4':
                    stok_baru = int(input("\nMasukkan Stok Susu yang Baru: "))
                
                elif jenis_update == '5':
                    harga_baru = int(input("\nMasukkan Harga Susu yang Baru: "))
                
                else:
                    print("\n***Pilihan yang Anda masukkan tidak tersedia***")
                    continue

                konfirmasi = input("\nApakah data akan disimpan? (Y/N): ").capitalize()
                if konfirmasi == 'Y':
                    for susu in etalase:
                        if susu['Kode'] == kodevar:
                            if jenis_update == '1':
                                susu['Nama'] = nama_baru
                            elif jenis_update == '2':
                                susu['Kategori'] = kategori_baru
                            elif jenis_update == '3':
                                susu['Jenis'] = jenis_baru
                            elif jenis_update == '4':
                                susu['Stok'] = stok_baru
                            elif jenis_update == '5':
                                susu['Harga'] = harga_baru

                    print("\n**Data Berhasil disimpan**")
                else:
                    print("\n**Data tidak berhasil disimpan**")
        
        elif pilih == 2:
            break
        else:
            print("\n***Pilihan yang anda masukkan tidak tersedia***")



def delete(etalase):
    while True:
        show(etalase)
        delete = input('''
        Menghapus Daftar Susu di Etalase
        1. Hapus Susu
        2. Kembali Ke Menu Utama

        Masukkan angka untuk memilih menu: ''')

        if delete == '1':
            if len(etalase) != 0:
                kodevar = input("\n\tMasukkan Kode Untuk Mencari Data [101-109]: ")
                index_to_delete = None
                
                for index, item in enumerate(etalase):
                    if item['Kode'] == kodevar:
                        index_to_delete = index
                        break
                
                if index_to_delete is not None:
                    konfirmasi = input("Apakah data diatas akan dihapus? [Y/N]: ").capitalize()
                    if konfirmasi == 'Y':
                        del etalase[index_to_delete]
                        print("\n**Data berhasil dihapus**")
                    elif konfirmasi == 'N':
                        print("\n\t**Data batal dihapus**")
                    else:
                        print("\n**Pilihan anda tidak tersedia**")
                else:
                    print("\n**Tidak ada susu dengan kode yang sesuai.**")
                    
        elif delete == '2':
            break
        else:
           print("\n**Pilihan menu tidak tersedia**")


def buy(etalase):
    while True:
        pilihan = int(input('''
        1. Beli Susu
        2. Kembali ke Menu Utama
        
        Masukkan angka untuk memilih menu: '''))

        if pilihan == 1:
            show(etalase)
            checker = None
            while True:
                try:
                    KodeSusu = input("\nMasukkan Kode Susu yang ingin dibeli [101-110]: ")
                    susu = next((item for item in etalase if item['Kode'] == KodeSusu), None)
                    if susu:
                        KodeBuah = etalase.index(susu)
                    else:
                        print("\nKode Susu tidak valid. Coba lagi.")
                        continue
                except ValueError:
                    print("\nInput harus berupa angka. Coba lagi.")
                    continue

                while True:
                    JmlhSusu = int(input("\nMasukkan Jumlah Susu yang ingin dibeli: "))
                    if JmlhSusu <= 0:
                        print("\nJumlah susu harus lebih dari 0. Coba lagi.")
                    elif JmlhSusu > etalase[KodeBuah]['Stok']:
                        print('\nMaaf, stok tidak mencukupi. Stok tinggal {}'.format(etalase[KodeBuah]['Stok']))
                    else:
                        cart.append([etalase[KodeBuah]['Nama'], JmlhSusu, etalase[KodeBuah]['Harga'], KodeBuah])
                        
                        # Update stok
                        etalase[KodeBuah]['Stok'] -= JmlhSusu
                        
                        print('\nDaftar Belanja Anda:\n')
                        print('\tNama\t\t|Jumlah\t|Harga')
                        for item in cart:
                            print('{}\t|{}\t|{}'.format(item[0], item[1], item[2]))
                        
                        checker = (input('\nMau beli yang lain? (Y/N): ').capitalize())
                        if checker == 'N':
                            break
                    break

                if checker == 'N':
                    break
            if len(cart) > 0:
                print('\n\t============Daftar Belanja============ ')
                print('\n\tNama\t\t\t|Jumlah\t|Harga\t|Total Harga')
                totalharga = 0
                for item in cart:
                    total_per_item = item[1] * item[2]
                    print('{}\t\t|{}\t|{}\t|{}'.format(item[0], item[1], item[2], total_per_item))
                    totalharga += total_per_item
                print(f"\nTotal Harga yang Harus Dibayar: {totalharga}")

                while True:
                    uanganda = int(input('\nMasukkan Jumlah Uang Anda: '))
                    kembalian = (uanganda - totalharga)
                    kekurangan = (uanganda - totalharga) * (-1)
                    if uanganda > totalharga:
                        print('\n==Terimakasih Sudah Berbelanja== \n\n Kembalian Anda : {}'.format(kembalian))
                        cart.clear()
                        break
                    elif uanganda == totalharga:
                        print('\n===Terimakasih Sudah Berbelanja===')
                        cart.clear()
                        break
                    else:
                        print('\n**Maaf Uang Anda Kurang {} Rupiah**'.format(kekurangan))

        elif pilihan == 2:
            break
        else:
            print("\n***Pilihan yang anda masukkan tidak tersedia***")



def MainMenu():
    while True:
        pilihanmenu = input('''
    Selamat Datang di Pasar Buah

    Daftar Pilihan :
    1. Menampilkan Daftar Susu
    2. Menambah Susu
    3. Update Susu
    4. Menghapus Susu
    5. Membeli Susu
    6. Exit Program

    Masukkan angka untuk memilih pilihan: ''')
        if pilihanmenu == '1':
            read(etalase)   
        elif pilihanmenu == '2':
            create(etalase)
        elif pilihanmenu == '3':
            update(etalase)    
        elif pilihanmenu == '4':
            delete(etalase)    
        elif pilihanmenu == '5':
            buy(etalase)    
        elif pilihanmenu == '6':
            break
    
              
MainMenu()   

