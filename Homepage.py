import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# 2. CSS Magic untuk Memindahkan Navigasi ke Bawah Logo
st.markdown("""
    <style>
    /* Menggeser menu navigasi otomatis ke bawah agar ada ruang untuk logo */
    [data-testid="stSidebarNav"] {
        padding-top: 120px !important;
    }
    
    /* Container untuk Logo dan Powered By yang akan ditempel di paling atas sidebar */
    .custom-sidebar-header {
        position: absolute;
        top: 20px;
        left: 0;
        right: 0;
        text-align: center;
        z-index: 1000;
    }

    .powered-by {
        font-size: 11px;
        color: #808495;
        margin-bottom: 5px;
        font-family: sans-serif;
    }

    .logo-img {
        width: 100px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Menyuntikkan Logo di Atas Menu Navigasi
# Ganti URL gambar dengan link GitHub atau file lokal assets/logo_ruangnalar.png
st.sidebar.markdown(f"""
    <div class="custom-sidebar-header">
        <p class="powered-by">Powered by</p>
        <img src="logo_ruangnalar.png" class="logo-img">
    </div>
    """, unsafe_allow_html=True)

# 4. Konten Halaman Utama
st.markdown("""
    <div style='text-align: center; margin-top: 150px;'>
        <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
        <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
    </div>
    """, unsafe_allow_html=True)