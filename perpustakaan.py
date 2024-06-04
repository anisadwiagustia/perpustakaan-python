import os
import datetime

def garis():
    print(61*"-")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()

x = datetime.datetime.now()
tanggal = x.strftime("%x")
tgl=x.today()
kode=tgl.day
denda=0
def date(year=22,month=12,day=1):
    global telat
    global denda
    i="01"
    telat=kode-day
    denda=telat*1000
    print("Batas Pengembalian Buku  : ",month,"/",i,"/",year)
    return denda



kodebuku=[]
buku = [
    " Bahasa Indonesia               |  Erlangga             | ",
    " Bahasa Inggris                 |  Erlangga             | ",
    " Matematika                     |  Erlangga             | ",
    " Rasa                           |  Tereliye             | ",
    " Orion                          |  Ciinderella Sarif    | ",
    " Shea                           |  Asri Aci             | ",
    " Iris                           |  Innayah putri        | ",
    " Resep Masakan Serba Tusuk      |  Jethro Ido Pasaribu  | ",
    " Resep Masakan Pilihan Keluarga |  Rih Lasmiatik        | "
]

stock = [20,10,25,10,8,7,6,8,5]


def menu1():
    global username
    for i in range (True):
        print("\n                 Selamat Datang di Rumah Baca \n")
        garis()
        print()
        print("      A        -          Pustakawan")
        print("      B        -          Pengunjung Perpustakaan")
        garis()
        pilawal=input("Masukkan Pilihan [A/B] :")
        if pilawal=="A"or pilawal=="a":
            clear_screen()
            print("\n                       Situs Rumah Baca \n")
            garis()
            namapegawai=str(input("Masukkan Nama Anda     : "))
            password=str(input("Masukkan Password Anda : "))
            for i in range(True) :
                clear_screen()
                print("\n                       Situs Rumah Baca \n")
                garis()
                username = str(input("Masukkan Nama Anda     :"))
                password_1 = str(input("Masukkan Password Anda :"))
                if username == namapegawai and password_1 == password :
                    clear_screen()
                    menu()
                else :
                    print("Mohon Maaf Username Atau Password Anda Salah")
                    kembali()
                    menu1()
        
        elif pilawal=="B" or pilawal=="b":
            clear_screen()
            print("Silahkan Pilih Buku : ")
            display()
            print("\nApakah Anda Sudah Menentukan Buku Mana Yang Akan Anda Pinjam ??")
            print("Jika Sudah Silahkan Pergi Ke Pustakawan Untuk Memproses Peminjaman...\n")
            kembali()
            menu1()
        else:
            print("Menu Yang Anda Masukkan Salah!!")
            kembali()
            menu()


#tampilan
def menu():
    for i in range (True):
        print("\n                 Selamat Datang di Rumah Baca \n")
        garis()
        print()
        print("      A        -          Peminjaman Buku")
        print("      B        -          Pengembalian Buku")  
        print("      C        -          Display")
        print("      D        -          Untuk Keluar")
        garis()
        awal=input("Masukkan Kode Menu [A/B/C/D] : ")
        print()
        #percabangan untuk menu
        if awal == "A" or awal == "a" :
            clear_screen()
            print("                 Peminjaman Buku Rumah Baca")
            garis()
            peminjaman()
        elif awal == "B" or awal == "b" :
            clear_screen()
            print("                 Pengembalian Buku Rumah Baca")
            garis()
            pengembalian()
        elif awal =="C" or awal=="c":
            clear_screen()
            stockB()
            kembali()
            menu()
        elif awal == "D" or awal == "d" :
            clear_screen()
            print("\n                  Buku Adalah Jendela Dunia \n")
            penutup()
            input("\n\nTekan tombol apa saja untuk kembali ke Menu...")

            break
        else:
            print("Menu Yang Anda Masukkan Salah!!")
            kembali()
            menu()

#display
def display ():
    print("\n Pilih Menu Dibawah Ini : \n")
    print("  No.","                  ","Judul Buku & Pengarang")
    garis()
    for i in range(len(buku)):
        print(" ",(i+1) ,"   ", buku[i])
    garis()

def stockB ():
    print(70*"-")
    print("                            Situs Rumah Baca")
    print(70*"-")
    print("  No.","                   ","Judul Buku & Pengarang","               ","Stock")
    print(70*"-")
    for i in range(len(buku)):
        print(" ",(i+1) ,"   ", buku[i]                                              ,stock[i])
    print(70*"-")
    print() 
    kembali()
    menu1()

#code untuk peminjaman buku            
def peminjaman ():
    global ulang
    print("Oleh Pustakawan : ",username)
    nama_peminjam=input("\nNama Peminjam              : ")
    ulang=int(input("Jumlah Jenis Buku Dipinjam : "))
    if ulang > 9 :
        print("Jenis Buku Yang Tersedia Tidak Lebih Dari 9..\n\n\n\n")
        kembali()
        menu()
    display()
    garis()
    cabang1 ()
    stock_buku()
    print("\n\n")
    input("\n\nTekan Enter Untuk Cetak Bukti!! ")

    #output peminjaman buku
    clear_screen()
    print("\n                 Peminjaman Buku Rumah Baca")
    garis()
    print("Oleh Pustakawan : ",username)
    i=0
    print("Kode Peminjaman      :  RBP-",(i+1),kode,ulang,nama_peminjam)
    print("Nama Peminjam        : ",nama_peminjam)
    print("Tanggal Peminjaman   : ",tanggal)
    for i in range (ulang):
        print("\nBuku Ke - ",i+1)
        print("Kode Buku            : RB-",kodebuku[i],jenisB)
        print("Judul Buku           :",judulB)
        print("Pengarang            :",penulis)
    print("\n Batas Pengembalian   : 5 hari dari Tanggal Peminjaman")
    print(" Jika Telat Denda     : Rp. 1000/hari")
    print(" Jangan Lupa Dikembalikan ... \n")
    penutup()
    ds=input("\n\nIngin Melihat Sisa Stok Y/T ? ")
    if ds == "Y" or ds =="y":
        clear_screen()
        stockB()
    elif ds == "T" or ds == "t":
        penutup()


#output pengembalian buku
def pengembalian ():
    global ulang
    print("Oleh Pustakawan : ",username)
    nama=input("\nNama Peminjam                 : ")
    ulang=int(input("Jumlah Buku Yang Dikembalikan : "))
    garis()
    print("\n Buku Yang Anda Pinjam ? \n")
    print("  No.","                 ","Judul Buku & Pengarang")
    garis()
    for i in range(len(buku)):
        print(" ",(i+1) ,"   ", buku[i])
    garis()
    cabang ()

    #output pengembalian buku
    clear_screen()
    print("\n                 Pengembalian Buku Rumah Baca")
    garis()
    print("Oleh Pustakawan : ",username)
    print("\nPengembalian Atas Nama   : ",nama)
    date()
    i=0
    print("Kode Pengembalian        :  RBP-",(i+1),kode,ulang,nama)
    print("Dikembalikan Pada        : ",tanggal)
    print("Telat Pengembalian       : ",telat,"Hari")

    
    for i in range (ulang):
        print("\nBuku Ke - ",i+1)
        print("Kode Buku            : RB-",kodebuku[i],jenisB)
        print("Judul Buku           :",judulB)
        print("Pengarang            :",penulis)
    penutup()
    garis()
    print("Telat Pengembalian   :",telat,"Hari")
    print("Total Denda          : Rp.",denda)
    ds=input("\n\nIngin Melihat Sisa Stok Y/T ? ")
    if ds == "Y" or ds =="y":
        clear_screen()
        stockB()
    elif ds == "T" or ds == "t":
        penutup()




#untuk percabangan dan perulangan buku
def cabang1 ():
    global jenisB
    global judulB
    global penulis
    global k_buku
    for i in range (ulang):
        k_buku=input("Masukkan Nomor Buku : ")
        kodebuku.append(k_buku)
        if kodebuku[i] == "1" :
            jenisB="MATA PELAJARAN"
            judulB="Bahasa Indonesia"
            penulis="Erlangga"
            sisa=stock[0]-1
            stock[0]=sisa
            
        elif kodebuku[i]== "2" :
            jenisB="MATA PELAJARAN"
            judulB="Bahasa Inggris"
            penulis="Erlangga"
            sisa=stock[1]-1
            stock[1]=sisa
            
        elif kodebuku[i]== "3" :
            jenisB="MATA PELAJARAN"
            judulB="Matematika"
            penulis="Erlangga"
            sisa=stock[2]-1
            stock[2]=sisa
            
        elif kodebuku[i] == "4" :
            jenisB="NOVEL"
            judulB="Rasa"
            penulis="Tereliye"
            sisa=stock[3]-1
            stock[3]=sisa
            
        elif kodebuku[i] == "5" :
            jenisB="NOVEL"
            judulB="Orion"
            penulis="Ciinderella Sarif"
            sisa=stock[4]-1
            stock[4]=sisa
            
        elif kodebuku[i]== "6" :
            jenisB="NOVEL"
            judulB="Shea"
            penulis="Asri Aci"            
            sisa=stock[5]-1
            stock[5]=sisa

        elif kodebuku[i] == "7" :
            jenisB="NOVEL"
            judulB="Iris"
            penulis="Innayah Putri"
            sisa=stock[6]-1
            stock[6]=sisa

        elif kodebuku[i] == "8" :
            jenisB="UMUM"
            judulB="Resep Masakan Serba Tusuk"
            penulis="Jethro Ido Pasaribu"
            sisa=stock[7]-1
            stock[7]=sisa

        elif kodebuku[i] == "9" :
            jenisB="UMUM"
            judulB="Resep Masakan Pilihan Keluarga"
            penulis="Rih Lasmiatik"
            sisa=stock[8]-1
            stock[8]=sisa

        else :
            print("Buku Tidak Tersedia..")
            peminjaman()
            continue

def cabang ():
    global jenisB
    global judulB
    global penulis
    global k_buku
    for i in range (ulang):
        k_buku=input("Masukkan Nomor Buku : ")
        kodebuku.append(k_buku)
        if kodebuku[i] == "1" :
            jenisB="MATA PELAJARAN"
            judulB="Bahasa Indonesia"
            penulis="Erlangga"
            sisa=stock[0]+1
            stock[0]=sisa
            
        elif kodebuku[i]== "2" :
            jenisB="MATA PELAJARAN"
            judulB="Bahasa Inggris"
            penulis="Erlangga"
            sisa=stock[1]+1
            stock[1]=sisa
            
        elif kodebuku[i]== "3" :
            jenisB="MATA PELAJARAN"
            judulB="Matematika"
            penulis="Erlangga"
            sisa=stock[2]+1
            stock[2]=sisa
            
        elif kodebuku[i] == "4" :
            jenisB="NOVEL"
            judulB="Rasa"
            penulis="Tereliye"
            sisa=stock[3]+1
            stock[3]=sisa
            
        elif kodebuku[i] == "5" :
            jenisB="NOVEL"
            judulB="Orion"
            penulis="Ciinderella Sarif"
            sisa=stock[4]+1
            stock[4]=sisa
            
        elif kodebuku[i]== "6" :
            jenisB="NOVEL"
            judulB="Shea"
            penulis="Asri Aci"            
            sisa=stock[5]+1
            stock[5]=sisa

        elif kodebuku[i] == "7" :
            jenisB="NOVEL"
            judulB="Iris"
            penulis="Innayah Putri"
            sisa=stock[6]+1
            stock[6]=sisa

        elif kodebuku[i] == "8" :
            jenisB="UMUM"
            judulB="Resep Masakan Serba Tusuk"
            penulis="Jethro Ido Pasaribu"
            sisa=stock[7]-1
            stock[7]=sisa

        elif kodebuku[i] == "9" :
            jenisB="UMUM"
            judulB="Resep Masakan Pilihan Keluarga"
            penulis="Rih Lasmiatik"
            sisa=stock[8]+1
            stock[8]=sisa

        else :
            print("Buku Tidak Tersedia..")
            peminjaman()
            continue


def stock_buku():
    a=1
    for i in range (a):
        if stock[i]>0 :
            keterangan = "Buku Tersedia"
            print("Stock        : ",keterangan)
            print()

        else :
            keterangan = "Buku Tidak Tersedia"
            print("Stock        : ",keterangan)
            print()
            clear_screen()
            cabang()
    
#output penutup
def penutup():
    garis()
    print("\n        Terimakasih Sudah Menggunakan Situs Rumah Baca \n")
    garis()

#pemanggilan def    
garis()
menu1()