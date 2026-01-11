import streamlit as st
import base64
import os

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# 2. Fungsi Base64 untuk Logo
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

path_logo = "assets/logo_ruangnalar.png"
logo_css = f"data:image/png;base64,{get_base64(path_logo)}" if os.path.exists(path_logo) else ""

# 3. CSS Custom: Menghilangkan Gap, Memunculkan Ikon & Homepage, serta Center Teks
st.markdown(f"""
    <style>
    /* --- 1. MENGATUR AREA ATAS (NO GAP) --- */
    [data-testid="stSidebarNav"] {{
        padding-top: 100px !important; /* Ruang untuk logo */
    }}
    
    [data-testid="stSidebarNav"]::before {{
        content: "Powered by";
        position: absolute;
        top: 15px; /* Mepet ke atas */
        left: 50%;
        transform: translateX(-50%);
        font-size: 10px;
        color: #808495;
        font-family: sans-serif;
    }}

    [data-testid="stSidebarNav"]::after {{
        content: "";
        background-image: url("{logo_css}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        display: block;
        width: 110px;
        height: 70px;
        position: absolute;
        top: 30px; /* Tepat di bawah Powered by */
        left: 50%;
        transform: translateX(-50%);
    }}

    /* --- 2. MERAPIKAN MENU: CENTER & TAMPILKAN IKON --- */
    /* Mengatur list menu agar center */
    [data-testid="stSidebarNav"] ul {{
        padding-left: 0px;
        margin-top: 10px;
    }}

    /* Mengetengahkan item menu tanpa menghilangkan ikon */
    [data-testid="stSidebarNav"] ul li a {{
        justify-content: center !important; 
        padding: 8px 10px !important;
        gap: 10px; /* Jarak antara ikon dan teks */
    }}

    /* Memastikan teks menu berada di tengah */
    [data-testid="stSidebarNav"] ul li a span {{
        text-align: center;
        display: inline-block;
    }}

    /* Memberi warna aktif yang lebih jelas pada menu yang dipilih */
    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Konten Halaman Utama
st.markdown("""
    <div style='text-align: center; margin-top: 150px;'>
        <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
        <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
    </div>
    """, unsafe_allow_html=True)