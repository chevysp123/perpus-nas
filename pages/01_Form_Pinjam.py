#Import Libary
import time
import sys
import os
import streamlit as st
from Array_Buku import buku

#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

#Inisialisasi Variabel
arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]

#Elemen Halaman Streamlit
st.empty()
st.title("📖 Menu Peminjaman Buku")
st.write("Silahkan Masukkan Data Diri Anda")

if st.button("pinjem Buku" ):
    buku[0][1] = buku[0][1] - 1

list_buku = []
for item, index in enumerate(buku):
    list_buku.append(str(item[3]))

#Input Form
form1 = st.form(key="annotation1",clear_on_submit=True)
with form1:
        cols = st.columns((1,1))
        nama = cols[0].text_input("Nama Lengkap :")
        # judul = cols[1].selectbox('Pilih Judul Buku',('','As A Man Thinketh by James Allen','The Metamorphosis by Franz Kafka','1984 by George Orwell','Manusia Setengan Salmon by Raditya Dika','Ubur Ubur Lembur by Raditya Dika','Sang Pemimpi by Andrea Hirata','The Little Prince by Antonie De Saint-Exupery','The Laws Of Human Nature by Robert Greene','The Art Of Being Alone by Renuka Gavrani','Steal Like An Artist by Austin Kleon'))
        judul = cols[1].selectbox('Pilih Judul Buku',list_buku)
        cols = st.columns(2)
        tglpinjam = cols[0].date_input("Tanggal Peminjaman :")
        tglkembali = cols[1].date_input("Tanggal Kembali :")
        submitted = st.form_submit_button(label="Submit")
        
        #Pengiriman Data
        if submitted:
            st.success("Terimakasih sudah meminjam buku di perpustakaan Nasional! Jangan lupa simpan struk peminjaman ya")
            st.balloons()
            
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