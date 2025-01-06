#Import Libary
import streamlit as st
from Array_Peminjam import peminjam

#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu List Peminjam", layout="centered")

#List Peminjam
st.title("List Peminjam")


for index, item in enumerate(peminjam):
    # st.write(item[0])
    st.write(f"{str(index + 1)} - {item[0]} - {item[1]} - tanggal Pinjam : {item[2]} - tanggal Pengembalian : {item[3]} ")