import streamlit as st
import base64

st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# Fungsi untuk mengubah gambar lokal ke Base64 agar bisa dibaca CSS
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load logo Anda
# Pastikan path file benar sesuai folder Anda
logo_base64 = get_base64_of_bin_file('assets/logo_ruangnalar.png')

# --- CSS MAGIC: Meletakkan Logo di Atas Menu ---
st.markdown(f"""
    <style>
    /* 1. Memberi ruang kosong di atas menu navigasi asli */
    [data-testid="stSidebarNav"] {{
        padding-top: 130px !important;
    }}

    /* 2. Membuat container logo melayang di area merah yang Anda tandai */
    .custom-header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%; /* Menyesuaikan lebar sidebar */
        padding: 20px 10px;
        background-color: #262730; /* Warna gelap sidebar */
        z-index: 999;
        text-align: center;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}

    .powered-by {{
        font-size: 10px;
        color: #808495;
        margin-bottom: 2px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .logo-img {{
        width: 100px;
    }}
    </style>
    
    <div class="custom-header">
        <p class="powered-by">Powered by</p>
        <img class="logo-img" src="data:image/png;base64,{logo_base64}">
    </div>
    """, unsafe_allow_html=True)

# --- KONTEN HALAMAN UTAMA ---
st.markdown("""
    <div style='text-align: center; margin-top: 150px;'>
        <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
        <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
    </div>
    """, unsafe_allow_html=True)