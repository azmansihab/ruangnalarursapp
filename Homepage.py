import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# --- CUSTOM CSS (Minimalis & Bersih) ---
st.markdown("""
    <style>
    /* 1. Menghilangkan Navigasi Otomatis Streamlit (Yang dilingkari merah sebelumnya) */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* 2. Mengatur padding atas sidebar */
    [data-testid="stSidebar"] .st-emotion-cache-1647ite {
        padding-top: 0.5rem;
    }

    /* 3. Styling Teks 'Powered by' agar kecil dan pas di atas logo */
    .powered-by {
        font-size: 11px;
        color: #808495;
        text-align: center;
        margin-bottom: -5px;
        font-family: sans-serif;
    }

    /* 4. Menghilangkan bulatan radio button agar minimalis */
    div[role="radiogroup"] .st-emotion-cache-16t9833 {
        display: none;
    }

    /* 5. Styling Menu Minimalis (Hanya teks dengan sedikit highlight saat aktif) */
    .stRadio [role="radiogroup"] label {
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 15px;
        color: #C1C2C6;
        transition: 0.2s;
        cursor: pointer;
    }

    /* Warna teks saat menu dipilih (Aktif) */
    .stRadio div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    # Bagian Logo: Kecil & Berada di paling atas
    st.markdown('<p class="powered-by">Powered by</p>', unsafe_allow_html=True)
    # Width disetel ke 120 agar lebih kecil sesuai permintaan
    st.image("assets/logo_ruangnalar.png", width=120) 
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigasi Minimalis (Menggantikan menu bawaan)
    menu = st.radio(
        label="Navigation",
        options=["Home", "ISP Network Planner", "KMZ Point Renamer", "Pop UP Mastering"],
        label_visibility="collapsed"
    )

    # Menampilkan Parameter Teknis hanya untuk ISP Planner
    if menu == "ISP Network Planner":
        st.markdown("---")
        with st.expander("⚙️ Parameter Teknis", expanded=True):
            st.slider("Radius Maksimal Jalan (Meter)", 50, 500, 250)
            st.slider("Kapasitas Rumah per Tiang", 1, 20, 10)

# --- LOGIKA TAMPILAN KONTEN ---
if menu == "Home":
    st.markdown("""
        <div style='text-align: center; margin-top: 150px;'>
            <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
            <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
        </div>
        """, unsafe_allow_html=True)

elif menu == "ISP Network Planner":
    st.title("🌐 ISP Network Planner")
    # Tempatkan kode atau panggil fungsi ISP Planner Anda di sini

elif menu == "KMZ Point Renamer":
    st.title("📍 KMZ Point Renamer")
    # Tempatkan kode atau panggil fungsi KMZ Renamer Anda di sini

elif menu == "Pop UP Mastering":
    st.title("💬 Pop UP Mastering")