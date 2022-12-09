mahasiswa = {}

def header():
    print("\nMenampilkan Data Nilai")
    print("="*23)

def tambah_data():
    '''fungsi tambah data'''
    nama = input("Nama : ")
    nilai = int(input("Nilai : "))
    mahasiswa[nama] = {nama, nilai}
    return nama,nilai

def lihat_data():
    '''fungsi lihat data'''
    for x in mahasiswa.values():
        print(x)

def ubah_data():
    '''fungsi ubah data'''
    nama = input("Nama : ")
    if nama in mahasiswa:
        nilai = input("Nilai : ")
        mahasiswa[nama] = {nama, nilai}
        print("Data Diubah")

def hapus_data():
    '''fungsi hapus data'''
    nama = input("Nama : ")
    if nama in mahasiswa:
        mahasiswa.pop(nama)
        print("Data dihapus ")

while True :
    header()

    print("1. Tambah \n2. Lihat \n3.Hapus \n4.Ubah \n5.Keluar")
    fungsi = input("Pilih fungsi : ")
    if fungsi == '5':
        break
    if fungsi == '1':
        tambah_data()
    if fungsi == '2':
        lihat_data()
    if fungsi == '3':
        hapus_data()
    if fungsi == '4':
        ubah_data()
print("Program selesai, terima kasih")

