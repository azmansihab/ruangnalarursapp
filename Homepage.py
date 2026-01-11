import streamlit as st
import base64
import os

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# 2. Fungsi untuk Konversi Gambar ke Base64 (Agar Logo Muncul)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path logo - Pastikan folder 'assets' dan file 'logo_ruangnalar.png' ada
path_logo = "assets/logo_ruangnalar.png"

if os.path.exists(path_logo):
    bin_str = get_base64(path_logo)
    logo_css = f"data:image/png;base64,{bin_str}"
else:
    # Fallback jika file tidak ditemukan (untuk testing)
    logo_css = ""
    st.sidebar.error("File logo tidak ditemukan di folder assets/")

# 3. CSS untuk Memasukkan Logo & Teks ke Sidebar
st.markdown(f"""
    <style>
    /* Memberi ruang di atas menu navigasi otomatis */
    [data-testid="stSidebarNav"] {{
        padding-top: 130px !important;
    }}
    
    /* Menaruh teks "Powered by" */
    [data-testid="stSidebarNav"]::before {{
        content: "Powered by";
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 11px;
        color: #808495;
        font-family: sans-serif;
    }}

    /* Menaruh Logo di area yang sudah dikosongkan */
    [data-testid="stSidebarNav"]::after {{
        content: "";
        background-image: url("{logo_css}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        display: block;
        width: 120px;
        height: 80px;
        position: absolute;
        top: 40px;
        left: 50%;
        transform: translateX(-50%);
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Konten Utama
st.markdown("""
    <div style='text-align: center; margin-top: 150px;'>
        <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
        <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
    </div>
    """, unsafe_allow_html=True)