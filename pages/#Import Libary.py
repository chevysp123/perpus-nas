#Import Libary
import time
import sys
import os
import streamlit as st
from Array_Buku import buku
from Array_Peminjam import peminjam
from Array_Peminjam import key_peminjam
import datetime
import qrcode
from PIL import Image


#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

#Inisialisasi Variabel
arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]

#Elemen Halaman Streamlit
st.empty()
st.title("📖 Menu Peminjaman Buku")
st.write("Silahkan Masukkan Data Diri Anda")

