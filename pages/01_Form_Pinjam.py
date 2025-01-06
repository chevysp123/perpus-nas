#Import Libary
import time
import sys
import os
import streamlit as st
from Array_Buku import buku
from Array_Peminjam import peminjam
from Array_Peminjam import key_peminjam
import datetime


#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

#Inisialisasi Variabel
arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]

#Elemen Halaman Streamlit
st.empty()
st.title("📖 Menu Peminjaman Buku")
st.write("Silahkan Masukkan Data Diri Anda")

# if st.button("pinjem Buku" ):
#     buku[0][1] = buku[0][1] - 1

# list_buku = []
# for item, index in enumerate(buku):
#     list_buku.append(str(item[3]))

#Input Form
form1 = st.form(key="annotation1",clear_on_submit=True)
with form1:
        cols = st.columns((1,1))
        nama = cols[0].text_input("Nama Lengkap :")
        judul = cols[1].selectbox('Pilih Judul Buku',('','0 - As A Man Thinketh by James Allen','1 - The Metamorphosis by Franz Kafka','2 - 1984 by George Orwell','3 - Manusia Setengan Salmon by Raditya Dika','4 - Ubur Ubur Lembur by Raditya Dika','5 - Sang Pemimpi by Andrea Hirata','6 - The Little Prince by Antonie De Saint-Exupery','7 - The Laws Of Human Nature by Robert Greene','8 - The Art Of Being Alone by Renuka Gavrani','9 - Steal Like An Artist by Austin Kleon'))
        # judul = cols[1].selectbox('Pilih Judul Buku',list_buku)
        cols = st.columns(2)
        tglpinjam = cols[0].date_input("Tanggal Peminjaman :")
        tglkembali = cols[1].date_input("Tanggal Kembali :")
        submitted = st.form_submit_button(label="Submit")
        
        #Pengiriman Data
        if submitted:
            index = int(judul.split(" - ")[0]) 
            judul = str(judul.split(" - ")[1]) 
            buku[index][1] = buku[index][1] - 1
            st.success(judul)
            st.success("Terimakasih sudah meminjam buku di perpustakaan Nasional! Jangan lupa simpan struk peminjaman ya")
            st.balloons()
            
            id = time.strftime("%d%m%y%H%M%S")
            
            peminjam.append(
                [
                    id,
                    nama,
                    judul,
                    tglpinjam.strftime("%Y-%m-%d"),
                    tglkembali.strftime("%Y-%m-%d")
                ]
            )
            
            key_peminjam.append( id + ' - ' + nama + " - " + judul)
            
            #Menyimpan Data dan Membuat Struk
            for i in range(1):
                arynama.append(nama)
                aryjudul.append(judul)
                arytglpinjam.append(tglpinjam)
                arytglkembali.append(tglkembali)
                #Membuat File Struk
                sys.stdout = open("struk-"+nama+"-"+str(tglpinjam)+".txt", "w")
                print('''
                    ************************  PERPUS NASIONAL  ************************
                    ************ Sistem Peminjaman Buku Perpustakaan Digital ************
                    ************************ Struk Bukti Pinjam *************************
                    ''')
                print('\t\t\tTanggal : ',tglpinjam)
                print("\t\t\tNama Peminjam Buku : ",nama)
                print("\t\t\tJudul Buku : ",judul)
                print("\t\t\tTanggal Peminjaman : ",tglpinjam)
                print("\t\t\tTanggal Kembali : ",tglkembali)
                print('''
                            ---Terima Kasih Telah Meminjam Buku Ditempat Kami---
                            ---Struk Harap Dibawa pada saat pengembalian Buku---
                    ''')
                sys.stdout.close()
                sys.stdout = sys.__stdout__
                time.sleep(1) #Fungsi Tambahan
                os.system("struk-"+nama+"-"+str(tglpinjam)+".txt") #Membuka File Struk