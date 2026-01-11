import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# --- CUSTOM CSS UNTUK SIDEBAR (Sesuai Referensi Gambar) ---
st.markdown("""
    <style>
    /* Mengatur warna latar belakang sidebar agar gelap sesuai gambar */
    [data-testid="stSidebar"] {
        background-color: #262730;
    }
    
    /* Menyelaraskan konten sidebar ke tengah */
    [data-testid="stSidebar"] .st-emotion-cache-1647ite {
        padding-top: 2rem;
        text-align: center;
    }

    /* Styling Tombol Menu agar terlihat seperti tombol "Home" yang aktif */
    .stRadio [role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    
    .stRadio label {
        background-color: transparent;
        color: #ffffff;
        padding: 10px 20px;
        border-radius: 10px;
        font-weight: 600;
        cursor: pointer;
        transition: 0.3s;
    }

    /* Efek saat menu dipilih (Highligt abu-abu seperti di gambar) */
    .stRadio div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) {
        background-color: #4B4C54 !important;
        border: 1px solid #6B6C74;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    # 1. Logo (Powered by Ruang Nalar Urban)
    st.image("assets/logo_ruangnalar.png", width=180)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. Navigasi Utama
    # Note: Kita gunakan st.radio karena folder 'pages/' tidak mendukung styling tombol seperti ini
    menu = st.radio(
        label="Navigasi Utama",
        options=["Home", "ISP Network Planner", "KMZ Point Renamer", "Pop UP Mastering"],
        label_visibility="collapsed" # Menghilangkan label teks 'Navigasi Utama'
    )

    # 3. Parameter Teknis (Hanya muncul jika ISP Network Planner aktif)
    if menu == "ISP Network Planner":
        st.markdown("---")
        with st.container(border=True): # Membuat kotak parameter
            st.markdown("⚙️ **Parameter Teknis**")
            st.slider("Radius Maksimal Jalan (Meter)", 50, 500, 250)
            st.slider("Kapasitas Rumah per Tiang", 1, 20, 10)

# --- MAIN CONTENT ---
if menu == "Home":
    st.markdown("""
        <div style='text-align: center; margin-top: 150px;'>
            <h1 style='font-size: 50px;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
            <p style='font-size: 20px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
        </div>
        """, unsafe_allow_html=True)

elif menu == "ISP Network Planner":
    st.title("🌐 ISP Network Planner")
    # Panggil fungsi app Anda di sini