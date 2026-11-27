import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analisis Curah Hujan | Proyek Fisika",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp { background: #0b132b; color: #f1f5f9; }
    [data-testid="stSidebar"] { background: #0f172a; border-right: 1px solid #1e293b; }
    [data-testid="stSidebar"] * { color: #e2e8f0 !important; }
    .hero {
        background: linear-gradient(125deg, #0284c7 0%, #1e3a8a 100%);
        padding: 28px 32px; border-radius: 16px; color: white;
        margin-bottom: 24px; border-left: 6px solid #38bdf8;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35);
    }
    .hero-kicker {
        color: #bae6fd; font-size: 12px; font-weight: 700;
        letter-spacing: 1.2px; text-transform: uppercase;
    }
    .hero h1 { color: #ffffff !important; font-size: 36px; margin: 8px 0 6px 0; font-weight: 800; }
    .hero p { color: #e2e8f0 !important; margin: 0; font-size: 15px; }
    .section-heading {
        display: flex; align-items: center; gap: 10px; margin: 10px 0 4px 0;
    }
    .section-number {
        background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 8px; padding: 4px 10px; font-size: 12px; font-weight: 800;
    }
    .section-title { color: #f8fafc; font-size: 24px; font-weight: 750; }
    .section-note { color: #94a3b8; font-size: 13.5px; margin: 0 0 18px 2px; }
    div[data-testid="stMetric"] {
        background: #1e293b; border: 1px solid #334155;
        padding: 14px 16px; border-radius: 12px;
    }
    .stButton button, .stDownloadButton button { border-radius: 9px; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

def section_heading(number, title, note=None):
    st.markdown(
        f'<div class="section-heading"><span class="section-number">{number}</span>'
        f'<span class="section-title">{title}</span></div>',
        unsafe_allow_html=True
    )
    if note:
        st.markdown(f'<p class="section-note">{note}</p>', unsafe_allow_html=True)


def classify_rainfall(value):
    """Klasifikasi contoh berdasarkan batas pada rancangan proyek."""
    if value <= 0:
        return "Tidak hujan"
    elif value <= 20:
        return "Hujan ringan"
    elif value <= 50:
        return "Hujan sedang"
    elif value <= 100:
        return "Hujan lebat"
    return "Hujan sangat lebat"

# Header
st.markdown("""
<div class="hero">
    <div class="hero-kicker">Bidang Kebumian · Tema 07 · Kelompok B07</div>
    <h1>🌧️ Rainfall Data Analyzer</h1>
    <p>Analisis data curah hujan, statistik sederhana, dan pengelompokan intensitas hujan.</p>
</div>
""", unsafe_allow_html=True)

# Data contoh
data_dummy = pd.DataFrame({
    "Tanggal": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"],
    "Suhu_C": [24.5, 23.1, 26.0, 22.8],
    "Kelembapan_%": [80, 90, 75, 95],
    "Curah_Hujan_mm": [12.4, 58.2, 2.0, 110.5]
})
data_dummy["Kategori"] = data_dummy["Curah_Hujan_mm"].apply(classify_rainfall)

# Sidebar
with st.sidebar:
    st.markdown("## 🧭 Menu Proyek")
    st.caption("Prodi Fisika · Semester 1")
    menu = st.radio(
        "Pilih bagian:",
        [
            "Ringkasan",
            "Algoritma & Source Code",
            "GUI & Simulasi",
            "Data & Analisis",
            "Flowchart & Sistem",
            "Laporan & Dokumentasi"
        ]
    )
    st.markdown("---")
    st.markdown("**Tim Kelompok B07**")
    st.write("• Malik Fathan A — Web & dokumentasi")
    st.write("• Anggota 2 — Menunggu konfirmasi")
    st.write("• Anggota 3 — Menunggu konfirmasi")
    st.write("• Anggota 4 — Menunggu konfirmasi")
    st.markdown("---")
    st.caption("Algoritma dan Pemrograman · 2026")

# Ringkasan
if menu == "Ringkasan":
    section_heading("00", "Ringkasan proyek", "Gambaran singkat isi dan fitur yang tersedia.")
    st.write(
        "Proyek ini disusun untuk mengolah data curah hujan dalam bentuk tabel, "
        "menampilkan ringkasan statistik, dan mengelompokkan intensitas hujan "
        "berdasarkan nilai curah hujan harian."
    )
    a, b, c = st.columns(3)
    a.metric("Jumlah data contoh", len(data_dummy))
    b.metric("Curah hujan tertinggi", f"{data_dummy['Curah_Hujan_mm'].max():.1f} mm")
    c.metric("Rentang data", f"{data_dummy['Tanggal'].iloc[0]} – {data_dummy['Tanggal'].iloc[-1]}")

    section_heading("01", "Isi aplikasi")
    cards = st.columns(3)
    cards[0].markdown("**01 · Source code**")
    cards[0].caption("Alur program dan fungsi klasifikasi.")
    cards[1].markdown("**02 · Simulasi**")
    cards[1].caption("Uji perubahan suhu, kelembapan, dan curah hujan.")
    cards[2].markdown("**03 · Analisis data**")
    cards[2].caption("Unggah CSV, lihat tabel, dan buat grafik.")
    st.info("Data yang tampil saat pertama dibuka adalah data contoh. Gunakan menu Data & Analisis untuk mencoba dataset sendiri.")

# Algoritma
elif menu == "Algoritma & Source Code":
    section_heading("01", "Algoritma & source code", "Urutan kerja program dari data masuk sampai hasil ditampilkan.")
    st.subheader("Alur pengolahan data")
    steps = [
        ("1", "Input", "Memuat data curah hujan dari file CSV."),
        ("2", "Pemeriksaan", "Memeriksa kolom dan nilai kosong pada dataset."),
        ("3", "Analisis", "Menghitung ringkasan statistik data."),
        ("4", "Klasifikasi", "Mengelompokkan intensitas berdasarkan curah hujan."),
        ("5", "Visualisasi", "Menampilkan tabel, metrik, dan grafik.")
    ]
    for number, title, description in steps:
        with st.container(border=True):
            st.markdown(f"**{number}. {title}**")
            st.caption(description)

    st.subheader("Fungsi klasifikasi")
    st.caption("Contoh fungsi Python untuk mengelompokkan curah hujan.")
    kode = "\n".join([
        "def klasifikasi_hujan(curah_hujan_mm):",
        "    if curah_hujan_mm <= 0:",
        '        return "Tidak hujan"',
        "    elif curah_hujan_mm <= 20:",
        '        return "Hujan ringan"',
        "    elif curah_hujan_mm <= 50:",
        '        return "Hujan sedang"',
        "    elif curah_hujan_mm <= 100:",
        '        return "Hujan lebat"',
        "    else:",
        '        return "Hujan sangat lebat"'
    ])
    st.code(kode, language="python")

    st.subheader("Repository")
    st.text_input("Link GitHub kelompok", placeholder="https://github.com/username/nama-repository")
    st.warning("Batas kategori di atas mengikuti contoh pada rancangan kode. Pastikan kembali kesesuaiannya dengan acuan klasifikasi yang dipakai dalam laporan.")

# GUI & simulasi
elif menu == "GUI & Simulasi":
    section_heading("02", "GUI & simulasi", "Ubah parameter untuk melihat bagaimana hasil klasifikasi berubah.")
    st.subheader("Simulasi kondisi atmosfer")
    left, middle, right = st.columns(3)
    with left:
        suhu_c = st.slider("Suhu udara (°C)", 15.0, 38.0, 26.0, 0.5)
    with middle:
        kelembapan = st.slider("Kelembapan relatif (%)", 30, 100, 82, 1)
    with right:
        hujan_mm = st.slider("Curah hujan (mm/hari)", 0.0, 150.0, 23.5, 0.5)

    titik_embun = round(suhu_c - ((100 - kelembapan) / 5.0), 1)
    kategori = classify_rainfall(hujan_mm)

    m1, m2, m3 = st.columns(3)
    m1.metric("Kategori curah hujan", kategori, f"{hujan_mm:.1f} mm/hari")
    m2.metric("Estimasi titik embun", f"{titik_embun:.1f} °C")
    m3.metric("Kelembapan relatif", f"{kelembapan}%")

    if hujan_mm <= 0:
        st.info("Tidak ada curah hujan pada nilai input.")
    elif hujan_mm <= 20:
        st.success("Termasuk kelompok hujan ringan.")
    elif hujan_mm <= 50:
        st.info("Termasuk kelompok hujan sedang.")
    elif hujan_mm <= 100:
        st.warning("Termasuk kelompok hujan lebat.")
    else:
        st.error("Termasuk kelompok hujan sangat lebat.")

    with st.expander("Bagaimana hasil ini dihitung?"):
        st.write(
            "Kategori ditentukan dari nilai curah hujan yang dimasukkan. "
            "Titik embun di sini memakai pendekatan sederhana dari suhu udara "
            "dan kelembapan relatif, sehingga hasilnya merupakan estimasi."
        )

    st.subheader("Dokumentasi tampilan")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Desain antarmuka**")
        st.caption("Tempatkan gambar mockup aplikasi setelah desain selesai.")
    with col2:
        st.markdown("**Hasil aplikasi**")
        st.caption("Tempatkan screenshot aplikasi yang sudah dijalankan.")

# Data & analisis
elif menu == "Data & Analisis":
    section_heading("03", "Data & analisis", "Gunakan data contoh atau unggah file CSV milik kelompok.")
    uploaded_file = st.file_uploader("Unggah dataset (.csv)", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"File berhasil dibaca: {len(df)} baris dan {len(df.columns)} kolom.")
        except Exception as error:
            st.error(f"File belum bisa dibaca. Periksa format CSV. Detail: {error}")
            df = data_dummy.copy()
    else:
        df = data_dummy.copy()
        st.info("Saat ini aplikasi menggunakan data contoh.")

    with st.expander("Lihat data", expanded=True):
        st.dataframe(df, use_container_width=True, hide_index=True)

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    if numeric_columns:
        selected_column = st.selectbox("Pilih kolom numerik untuk dianalisis", numeric_columns)
        values = pd.to_numeric(df[selected_column], errors="coerce").dropna()
        if not values.empty:
            x1, x2, x3, x4 = st.columns(4)
            x1.metric("Rata-rata", f"{values.mean():.2f}")
            x2.metric("Median", f"{values.median():.2f}")
            x3.metric("Nilai maksimum", f"{values.max():.2f}")
            x4.metric("Jumlah data valid", f"{len(values)}")
            st.subheader("Grafik data")
            st.bar_chart(values.reset_index(drop=True), use_container_width=True)
            csv_download = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Unduh data yang sedang ditampilkan",
                data=csv_download,
                file_name="data_curah_hujan.csv",
                mime="text/csv"
            )
        else:
            st.warning("Kolom yang dipilih tidak memiliki angka yang bisa dianalisis.")
    else:
        st.warning("Dataset belum memiliki kolom numerik untuk dibuat grafik.")

    st.subheader("Rencana pengembangan machine learning")
    st.write(
        "Model Random Forest dapat ditambahkan setelah dataset, fitur masukan, "
        "dan label kategori sudah ditetapkan. Pada versi ini, proses pelatihan "
        "dan evaluasi model belum dijalankan."
    )

# Flowchart
elif menu == "Flowchart & Sistem":
    section_heading("04", "Flowchart & sistem", "Dokumentasikan alur program dan hubungan antarbagian aplikasi.")
    st.subheader("Alur sistem")
    st.graphviz_chart("""
    digraph {
        rankdir=LR;
        node [shape=box, style="rounded,filled", fillcolor="#e5f3f7", color="#176b87"];
        A [label="Mulai"];
        B [label="Input dataset CSV"];
        C [label="Periksa data"];
        D [label="Hitung statistik"];
        E [label="Klasifikasi hujan"];
        F [label="Tampilkan hasil"];
        G [label="Selesai"];
        A -> B -> C -> D -> E -> F -> G;
    }
    """)
    st.subheader("Berkas pendukung")
    st.caption("Gambar flowchart atau arsitektur final dapat ditambahkan ke bagian ini.")
    st.file_uploader("Unggah gambar flowchart (PNG/JPG)", type=["png", "jpg", "jpeg"], key="flowchart_upload")

# Laporan
elif menu == "Laporan & Dokumentasi":
    section_heading("05", "Laporan & dokumentasi", "Ringkasan latar belakang, tujuan, metode, dan referensi.")
    with st.expander("Latar belakang", expanded=True):
        st.write(
            "Curah hujan merupakan salah satu variabel dalam siklus hidrologi "
            "dan dinamika atmosfer. Pengolahan data curah hujan dapat membantu "
            "menggambarkan pola hujan serta perubahan intensitas dari waktu ke waktu."
        )
    with st.expander("Tujuan"):
        st.write(
            "Membuat aplikasi Python yang dapat membaca data curah hujan, "
            "menampilkan ringkasan statistik, dan mengelompokkan intensitas hujan."
        )
    with st.expander("Metode yang direncanakan"):
        st.write(
            "Tahapan meliputi pengumpulan dataset, pemeriksaan data, analisis statistik, "
            "klasifikasi intensitas, dan visualisasi. Penggunaan Random Forest menjadi "
            "pengembangan lanjutan setelah data dan label siap."
        )
    with st.expander("Referensi"):
        st.write("• Badan Meteorologi, Klimatologi, dan Geofisika (BMKG).")
        st.write("• Dokumentasi resmi Python dan pandas.")
        st.write("• Dokumentasi resmi scikit-learn, jika model machine learning diterapkan.")
    st.caption("Lengkapi bagian ini dengan sumber, tahun, dan tautan referensi yang benar-benar digunakan.")
