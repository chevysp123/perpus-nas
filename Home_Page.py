#Import Libary
import streamlit as st
from PIL import Image

#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Home Page", page_icon="📚", layout="centered")

#Elemen Halaman Streamlit
st.title("📚Selamat Datang Di Perpustakaan Nasional")
st.write("Berikut ini adalah daftar buku yang tersedia di perpustakaan kami")

# Memuat gambar
image = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/1.jpg')
image1 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/2.jpg')
image2 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/3.jpg')
image3 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/4.jpg')
image4 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/5.jpg')
image5 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/6.jpg')
image6 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/7.jpg')
image7 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/8.jpg')
image8 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/9.jpg')
image9 = Image.open('C:/Kuliah SI/Perpustakaan/assets/image/10.jpg')

# Deskripsi singkat buku
deskripsi_buku = {
    "1": "As A Man Thinketh: Buku karya James Allen ini menjelaskan bahwa pikiran manusia memiliki kekuatan besar dalam membentuk kehidupan. Dengan pola pikir yang positif dan terarah, seseorang dapat mencapai kesuksesan dan kebahagiaan.",
    "2": "The Metamorphosis: Karya Franz Kafka ini bercerita tentang Gregor Samsa, seorang pria yang tiba-tiba berubah menjadi serangga raksasa. Novel ini mengeksplorasi tema alienasi, tekanan keluarga, dan perjuangan eksistensial.",
    "3": "1984: Novel karya George Orwell ini menggambarkan dunia distopia di bawah rezim totaliter. Dengan tema pengawasan ketat, manipulasi informasi, dan kehilangan kebebasan individu, 1984 menjadi peringatan akan bahaya otoritarianisme.",
    "4": "Manusia Setengan Salmon: Ditulis oleh Raditya Dika, buku ini berisi kumpulan cerita humor yang mengangkat tema kehidupan sehari-hari, mulai dari hubungan keluarga hingga pengalaman pribadi yang menggelitik.",
    "5": "Ubur Ubur Lembur: Karya Raditya Dika lainnya, buku ini menggabungkan humor dan refleksi tentang kehidupan, cinta, dan bagaimana seseorang menghadapi berbagai tantangan dengan cara yang jenaka.",
    "6": "Sang Pemimpi: Buku kedua dalam trilogi Laskar Pelangi karya Andrea Hirata ini menceritakan kisah Ikal dan teman-temannya yang penuh mimpi besar meski berasal dari lingkungan sederhana. Buku ini menginspirasi pembaca untuk tidak pernah berhenti bermimpi.",
    "7": "The Little Prince: Buku karya Antoine de Saint-Exupéry ini adalah dongeng filosofis tentang seorang pangeran kecil yang menjelajahi berbagai planet. Buku ini mengajarkan nilai kehidupan, cinta, dan persahabatan melalui perspektif yang sederhana namun mendalam.",
    "8": "The Laws Of Human Nature: Robert Greene menjelaskan 48 hukum alamiah yang mendasari perilaku manusia. Buku ini membantu pembaca memahami diri sendiri dan orang lain, serta memberikan wawasan untuk menghadapi dinamika sosial.",
    "9": "The Art Of Being Alone: Buku ini mengeksplorasi seni menikmati kesendirian, menemukan kedamaian batin, dan membangun hubungan sehat dengan diri sendiri, sehingga pembaca dapat hidup lebih seimbang dan bahagia.",
    "10": "Steal Like An Artist: Buku karya Austin Kleon ini menawarkan panduan kreatif untuk menghasilkan karya orisinal dengan cara memanfaatkan ide-ide dari berbagai sumber sebagai inspirasi, bukan plagiarisme."
}

# Membuat kolom untuk menampilkan cover buku
cols = st.columns((1,1,1))
cols1 = st.columns((1,1,1))
cols2 = st.columns((1,1,1))
cols3 = st.columns((1))

# Buku 1
with cols[0]:
    st.image(image, width=200)
    st.write("Tersedia 1 Buku")
    if st.button("Detail Buku 1"):
        st.write(deskripsi_buku["1"])

# Buku 2
with cols[1]:
    st.image(image1, width=200)
    st.write("Tersedia 5 Buku")
    if st.button("Detail Buku 2"):
        st.write(deskripsi_buku["2"])

# Buku 3
with cols[2]:
    st.image(image2, width=200)
    st.write("Tersedia 0 Buku")
    if st.button("Detail Buku 3"):
        st.write(deskripsi_buku["3"])

# Buku 4
with cols1[0]:
    st.image(image3, width=200)
    st.write("Tersedia 3 Buku")
    if st.button("Detail Buku 4"):
        st.write(deskripsi_buku["4"])
        
# Buku 5
with cols1[1]:
    st.image(image4, width=200)
    st.write("Tersedia 4 Buku")
    if st.button("Detail Buku 5"):
        st.write(deskripsi_buku["5"])
        
# Buku 6
with cols1[2]:
    st.image(image5, width=200)
    st.write("Tersedia 1 Buku")
    if st.button("Detail Buku 6"):
        st.write(deskripsi_buku["6"])
        
# Buku 7
with cols2[0]:
    st.image(image6, width=200)
    st.write("Tersedia 0 Buku")
    if st.button("Detail Buku 7"):
        st.write(deskripsi_buku["7"])
        
# Buku 8
with cols2[1]:
    st.image(image7, width=200)
    st.write("Tersedia 2 Buku")
    if st.button("Detail Buku 8"):
        st.write(deskripsi_buku["8"])
       
# Buku 9
with cols2[2]:
    st.image(image8, width=200)
    st.write("Tersedia 1 Buku")
    if st.button("Detail Buku 9"):
        st.write(deskripsi_buku["9"])

# Buku 10
with cols3[0]:
    st.image(image9, width=200)
    st.write("Tersedia 2 Buku")
    if st.button("Detail Buku 10"):
        st.write(deskripsi_buku["10"])
