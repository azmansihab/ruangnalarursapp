import streamlit as st
import base64
import os

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# 2. Fungsi Base64 (Tetap dipertahankan agar logo muncul)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

path_logo = "assets/logo_ruangnalar.png"
logo_css = f"data:image/png;base64,{get_base64(path_logo)}" if os.path.exists(path_logo) else ""

# 3. CSS Refined: Menghilangkan Gap & Teks Menu Center
st.markdown(f"""
    <style>
    /* Mengurangi gap di paling atas sidebar */
    [data-testid="stSidebarNav"] {{
        padding-top: 110px !important;
    }}
    
    /* Memposisikan teks "Powered by" lebih rapat ke atas */
    [data-testid="stSidebarNav"]::before {{
        content: "Powered by";
        position: absolute;
        top: 10px; /* Dikurangi agar lebih naik */
        left: 50%;
        transform: translateX(-50%);
        font-size: 10px;
        color: #808495;
        font-family: sans-serif;
        letter-spacing: 0.5px;
    }}

    /* Memposisikan Logo lebih rapat di bawah tulisan Powered by */
    [data-testid="stSidebarNav"]::after {{
        content: "";
        background-image: url("{logo_css}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        display: block;
        width: 100px; /* Ukuran disesuaikan agar proporsional */
        height: 70px;
        position: absolute;
        top: 25px; /* Menaikkan posisi logo */
        left: 50%;
        transform: translateX(-50%);
    }}

    /* --- MEMBUAT TEKS MENU MENJADI CENTER --- */
    [data-testid="stSidebarNav"] ul {{
        padding-left: 0px;
        text-align: center;
    }}

    [data-testid="stSidebarNav"] ul li a {{
        justify-content: center !important; /* Mengetengahkan konten menu */
        text-align: center !important;
        margin-left: 0 !important;
    }}
    
    /* Menghilangkan margin ikon agar teks benar-benar di tengah */
    [data-testid="stSidebarNav"] ul li a span:first-child {{
        display: none; 
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