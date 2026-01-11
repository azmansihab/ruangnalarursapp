import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Ruangnalarurs App", layout="wide")

# --- CUSTOM CSS (Menghilangkan Navigasi Bawaan & Styling Sidebar) ---
st.markdown("""
    <style>
    /* 1. Menghilangkan Navigasi Bawaan Streamlit agar tidak double */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* 2. Styling Sidebar agar konten ke tengah */
    [data-testid="stSidebar"] .st-emotion-cache-1647ite {
        padding-top: 1rem;
    }

    /* 3. Styling Teks 'Powered by' */
    .powered-by {
        font-size: 10px;
        color: #A0A0A0;
        text-align: center;
        margin-bottom: -10px;
    }

    /* 4. Menghilangkan bulatan radio button asli agar terlihat seperti menu button */
    div[role="radiogroup"] .st-emotion-cache-16t9833 {
        display: none;
    }
    
    /* 5. Membuat menu radio terlihat seperti tombol (pills) */
    .stRadio [role="radiogroup"] {
        padding: 0 10px;
    }
    
    .stRadio label {
        background-color: transparent;
        color: #ffffff;
        padding: 8px 15px;
        border-radius: 8px;
        font-weight: 500;
        width: 100%;
        margin-bottom: 5px;
        transition: 0.2s;
    }

    /* Efek Highlight saat menu dipilih */
    .stRadio div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) {
        background-color: #4B4C54 !important;
        border: 1px solid #6B6C74;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CUSTOM ---
with st.sidebar:
    # 1. Bagian Atas: Powered by + Logo
    st.markdown('<p class="powered-by">Powered by</p>', unsafe_allow_html=True)
    st.image("assets/logo_ruangnalar.png", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. Navigasi Custom (Tanpa bulatan radio)
    # Ini menggantikan sidebar bawaan yang Anda lingkari merah
    menu = st.radio(
        label="Menu",
        options=["Home", "ISP Network Planner", "KMZ Point Renamer", "Pop UP Mastering"],
        label_visibility="collapsed"
    )

    # 3. Parameter Teknis (Muncul secara dinamis)
    if menu == "ISP Network Planner":
        st.markdown("---")
        with st.container(border=True):
            st.markdown("⚙️ **Parameter Teknis**")
            st.slider("Radius Maksimal Jalan (Meter)", 50, 500, 250)
            st.slider("Kapasitas Rumah per Tiang", 1, 20, 10)

# --- MAIN CONTENT ---
if menu == "Home":
    st.markdown("""
        <div style='text-align: center; margin-top: 150px;'>
            <h1 style='font-size: 45px; font-weight: 800;'>WELCOME TO<br>RUANGNALARURSAPP</h1>
            <p style='font-size: 18px; color: #A0A0A0;'>Design Your Digital Infrastructure in Minutes.</p>
        </div>
        """, unsafe_allow_html=True)

elif menu == "ISP Network Planner":
    st.title("🌐 ISP Network Planner")
    # Panggil modul aplikasi Anda di sini

elif menu == "KMZ Point Renamer":
    st.title("📍 KMZ Point Renamer")

elif menu == "Pop UP Mastering":
    st.title("💬 Pop UP Mastering")