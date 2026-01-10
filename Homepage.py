import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# 2. Sidebar dengan Logo
with st.sidebar:
    # Ganti dengan path logo Anda
    st.image("assets/logo_ruangnalar.png", use_container_width=True)
    st.markdown("---")
    st.write("💡 **Pilih fitur di bawah untuk memulai**")

# 3. Konten Utama (Tampilan Welcome)
# Membuat teks berada di tengah secara vertikal dan horizontal
st.markdown("""
    <style>
    .main-title {
        font-size: 50px;
        font-weight: 800;
        text-align: center;
        margin-top: 150px;
        letter-spacing: -1px;
    }
    .sub-title {
        font-size: 24px;
        text-align: center;
        color: #A0A0A0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">WELCOME TO<br>RUANGNALARURSAPP</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Design Your Digital Infrastructure in Minutes.</p>', unsafe_allow_html=True)