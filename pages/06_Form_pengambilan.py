import time
import sys
import os
import streamlit as st
# from Array_Buku import buku
# from Array_Peminjam import peminjam
# from Array_Peminjam import key_peminjam
import datetime
# import qrcode
import Array_Peminjam
import Array_Buku
import importlib
from PIL import Image


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
form3 = st.form(key="annotation1",clear_on_submit=False)
with form3:
        submitted = st.form_submit_button(label="Scan", on_click=None)  
        nama = form3.text_input("Scan QR Code :")
        # submitted = st.form_submit_button(label="Submit")
                     
        #Pengiriman Data
        if submitted:
            key = nama
            if key in Array_Peminjam.key_peminjam:
                index = Array_Peminjam.key_peminjam.index(key)
                data_peminjam = Array_Peminjam.peminjam[index]
                st.write("Data Peminjam:")
                st.write(f"ID: {data_peminjam[0]}")
                st.write(f"Nama: {data_peminjam[1]}")
                st.write(f"Judul Buku: {data_peminjam[2]}")
                st.write(f"Tanggal Pinjam: {data_peminjam[3]}")
                st.write(f"Tanggal Kembali: {data_peminjam[4]}")
            else:
                st.error("Data tidak ditemukan.")
        
form4 = st.form(key="annotation2", clear_on_submit=False)
with form4:
    submitted2 = st.form_submit_button(label="Pinjam Buku")
    if submitted2:
        id = str(nama.split(" - ")[0]) 
        buku = str(nama.split(" - ")[2])
        if Array_Buku.buku[0][1] == 0:
            st.error("Maaf, Buku yang Anda Pilih Sedang Tidak Tersedia")
        else: 
            index = next((i for i, sublist in enumerate(Array_Peminjam.peminjam) if id in sublist), None)
            index_buku = next((i for i, sublist in enumerate(Array_Buku.buku) if buku in sublist), None)
            Array_Buku.buku[index_buku][1] -= 1
            st.success("Buku berhasil dipinjam.")
                            
