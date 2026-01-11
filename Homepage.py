import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# --- CUSTOM CSS (Final Fix) ---
st.markdown("""
    <style>
    /* 1. Memaksa logo tetap di paling atas (mengatasi margin default Streamlit) */
    [data-testid="stSidebarNav"] {
        padding-top: 20px !important;
    }
    
    /* 2. Styling Teks 'Powered by' agar berada di posisi paling atas */
    .powered-by-container {
        text-align: center;
        margin-top: -60px; /* Menarik ke atas agar di atas menu */
        margin-bottom: 10px;
    }
    
    .powered-by-text {
        font-size: 11px;
        color: #808495;
        font-family: sans-serif;
    }

    /* 3. Membuat Logo kecil dan di tengah */
    .centered-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100px;
    }

    /* 4. Memastikan menu navigasi bawaan (yang minimalis) berada di bawah logo */
    [data-testid="stSidebarNav"] ul {
        padding-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    # Bagian Atas: Logo & Powered by (Disuntikkan via HTML agar posisi stabil di atas)
    st.markdown(f"""
        <div class="powered-by-container">
            <p class="powered-by-text">Powered by</p>
            <img src="https://raw.githubusercontent.com/[YOUR_USERNAME]/[YOUR_REPO]/main/assets/logo_ruangnalar.png" class="centered-logo">
        </div>
    """, unsafe_allow_html=True)
    
    # Catatan: Karena Anda ingin menu minimalis bawaan, 
    # kita tidak menggunakan st.radio lagi.
    # Menu akan otomatis muncul jika file diletakkan di folder /pages
    
    st.markdown("---") # Garis pemisah tipis

# --- LOGIKA HALAMAN UTAMA ---
# (Karena kita menggunakan folder /pages, file ini otomatis jadi 'Homepage')
st.markdown("""
    <div style='text-align: center; margin-top: 150px;'>
        <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
        <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
    </div>
    """, unsafe_allow_html=True)