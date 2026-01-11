import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# 2. CSS untuk Memaksa Logo di Atas Menu Sidebar
st.markdown("""
    <style>
    /* Memberi ruang di atas menu navigasi otomatis */
    [data-testid="stSidebarNav"] {
        padding-top: 130px !important;
    }
    
    /* Menempatkan logo dan teks di area kosong tersebut */
    [data-testid="stSidebarNav"]::before {
        content: "Powered by";
        margin-left: 20px;
        margin-top: 20px;
        font-size: 11px;
        color: #808495;
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
    }

    /* Mengatur Logo agar muncul di atas navigasi */
    [data-testid="stSidebarNav"]::after {
        content: "";
        background-image: url("https://raw.githubusercontent.com/[USER]/[REPO]/main/assets/logo_ruangnalar.png");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        display: block;
        width: 120px;
        height: 100px;
        position: absolute;
        top: 35px;
        left: 50%;
        transform: translateX(-50%);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Konten Utama
st.markdown("""
    <div style='text-align: center; margin-top: 150px;'>
        <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
        <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
    </div>
    """, unsafe_allow_html=True)