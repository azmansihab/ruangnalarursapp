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

# 3. CSS Custom: Navigasi Ramping (Slim) & Center
st.markdown(f"""
    <style>
    /* Mengatur area header sidebar (Powered by + Logo) */
    [data-testid="stSidebarNav"] {{
        padding-top: 100px !important;
    }}
    
    [data-testid="stSidebarNav"]::before {{
        content: "Powered by";
        position: absolute;
        top: 15px;
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
        width: 100px;
        height: 60px;
        position: absolute;
        top: 30px;
        left: 50%;
        transform: translateX(-50%);
    }}

    /* --- MENGATUR MENU MENJADI RAMPING (SLIM) --- */
    /* Menghilangkan padding kiri pada list menu */
    [data-testid="stSidebarNav"] ul {{
        padding-left: 0px !important;
        padding-right: 0px !important;
    }}

    /* Mengecilkan ukuran baris menu agar ramping */
    [data-testid="stSidebarNav"] ul li {{
        padding: 0px 10px !important; /* Jarak samping menu ke dinding sidebar */
    }}

    [data-testid="stSidebarNav"] ul li a {{
        display: flex !important;
        justify-content: center !important; /* Teks & Ikon tetap di tengah */
        align-items: center !important;
        padding: 4px 10px !important; /* Padding atas-bawah kecil agar ramping */
        gap: 8px !important;
        border-radius: 6px !important;
        margin-bottom: 2px !important;
    }}

    /* Memastikan teks menu berukuran pas dan center */
    [data-testid="stSidebarNav"] ul li a span {{
        font-size: 14px !important;
        text-align: center !important;
    }}

    /* Memberi highlight minimalis pada menu aktif */
    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {{
        background-color: rgba(255, 255, 255, 0.1) !important;
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