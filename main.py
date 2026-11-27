import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Physics Project - Rainfall Data Analyzer",
    page_icon="🌧️",
    layout="wide"
)

# HERO BANNER
st.markdown("""
<div style="background: linear-gradient(135deg, #0284c7 0%, #1e3a8a 100%); padding: 28px 32px; border-radius: 16px; border-left: 6px solid #38bdf8; box-shadow: 0 8px 20px rgba(0,0,0,0.3); margin-bottom: 20px;">
    <span style="background-color: rgba(255,255,255,0.15); color: #e0f2fe; padding: 5px 14px; border-radius: 20px; font-size: 13px; font-weight: 600;">
        🌊 BIDANG KEBUMIAN • TEMA 07 • KELOMPOK B07
    </span>
    <h1 style="color: white; margin: 12px 0 6px 0; font-size: 38px; font-weight: 800;">
        🌧️ Rainfall Data Analyzer
    </h1>
    <p style="color: #cbd5e1; margin: 0; font-size: 16px;">
        Sistem Analisis Statistik & Klasifikasi Curah Hujan Berbasis GUI dan Machine Learning<br>
        <strong>Physics Project
    </p>
</div>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGASI
with st.sidebar:
    st.markdown("""
    <div style="background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35); padding: 14px; border-radius: 12px; margin-bottom: 12px;">
        <div style="font-size: 12px; color: #7dd3fc; font-weight: 700; letter-spacing: 0.5px;">PRODI FISIKA • SEMESTER 1</div>
        <div style="font-size: 18px; color: #f8fafc; font-weight: 800; margin-top: 2px;">🧭 Navigasi Proyek</div>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Halaman :",
        [
            "1. Algoritma & Source Code",
            "2. GUI & Hasil Aplikasi",
            "3. Flowchart & Sistem",
            "4. Data & Machine Learning",
            "5. Laporan & Dokumentasi"
        ]
    )

    st.markdown("---")
    st.markdown("**📊 Status Dokumentasi**")
    st.progress(65, text="65% — Kerangka & Simulasi Siap")

    st.markdown("---")
    st.markdown(" 👥 The Team ")
    st.info(
        "• **Malik Fathan A** (Web & Docs)\n"
        "• **Anggota 2** *(Menunggu data)*\n"
        "• **Anggota 3** *(Menunggu data)*\n"
        "• **Anggota 4** *(Menunggu data)*"
    )
    st.caption("Algoritma dan Pemrograman • 2026")

# MENU 1
if menu == "1. Algoritma & Source Code":
    st.header("01. Algoritma & Source Code")
    st.info("Bagian ini berisi penjelasan algoritma program, kode Python, kode GUI, dan kode ML (Random Forest).")
    st.subheader("🔗 Tautan Repository GitHub")
    st.markdown("- **Link GitHub Kelompok B07:** [Masukkan Link GitHub di Sini](https://github.com)")
    st.subheader("🧠 Algoritma Program")
    st.write("""
    1. **Input Data:** Memuat dataset curah hujan historis (format `.csv`).
    2. **Preprocessing:** Membersihkan nilai kosong (*missing values*) dan mengonversi satuan curah hujan (mm).
    3. **Analisis Statistik Fisika:** Menghitung rata-rata, standar deviasi, intensitas hujan maksimum, dan distribusi frekuensi.
    4. **Klasifikasi Machine Learning:** Melatih model *Random Forest* untuk mengklasifikasikan kategori hujan (Ringan, Sedang, Lebat, Sangat Lebat).
    5. **Visualisasi GUI:** Menampilkan grafik dan hasil prediksi pada antarmuka aplikasi.
    """)
    st.subheader("💻 Contoh Kode Klasifikasi Curah Hujan (Python)")
    kode_contoh = '''def klasifikasi_hujan(curah_hujan_mm):
    if curah_hujan_mm == 0:
        return "Berawan / Tidak Hujan"
    elif 0 < curah_hujan_mm <= 20:
        return "Hujan Ringan"
    elif 20 < curah_hujan_mm <= 50:
        return "Hujan Sedang"
    elif 50 < curah_hujan_mm <= 100:
        return "Hujan Lebat"
    else:
        return "Hujan Sangat Lebat / Ekstrem"
'''
    st.code(kode_contoh, language="python")

# MENU 2
elif menu == "2. GUI & Hasil Aplikasi":
    st.header("02. GUI & Hasil Aplikasi")
    st.info("Bagian ini memuat mockup desain, screenshot aplikasi desktop GUI, penjelasan fitur, dan tautan aplikasi.")
    
    with st.expander("⚡ Simulasi Interaktif Fisika Atmosfer & Klasifikasi Hujan (BMKG)", expanded=True):
        c_in1, c_in2, c_in3 = st.columns(3)
        with c_in1:
            suhu_c = st.slider("🌡️ Suhu Udara (°C):", 15.0, 38.0, 26.0, step=0.5)
        with c_in2:
            lembap = st.slider("💧 Kelembapan Relatif (%):", 30, 100, 82, step=1)
        with c_in3:
            hujan_mm = st.slider("🌧️ Curah Hujan (mm/hari):", 0.0, 150.0, 23.5, step=0.5)

        titik_embun = round(suhu_c - ((100 - lembap) / 5.0), 1)
        if hujan_mm <= 0.5:
            kat, warna, status_risiko = "Berawan / Tidak Hujan", "normal", "Aman (Kondisi Kering)"
        elif hujan_mm <= 20.0:
            kat, warna, status_risiko = "Hujan Ringan", "normal", "Rendah (Presipitasi Ringan)"
        elif hujan_mm <= 50.0:
            kat, warna, status_risiko = "Hujan Sedang", "off", "Waspada Genangan Lokal"
        elif hujan_mm <= 100.0:
            kat, warna, status_risiko = "Hujan Lebat", "inverse", "Siaga Banjir / Drainase Meluap"
        else:
            kat, warna, status_risiko = "Hujan Ekstrem", "inverse", "Awas Bencana Hidrometeorologi"

        st.markdown("---")
        m1, m2, m3 = st.columns(3)
        m1.metric("Kategori Intensitas (BMKG)", kat, f"{hujan_mm} mm/hari")
        m2.metric("Titik Embun (Dew Point)", f"{titik_embun} °C", f"RH {lembap}%")
        m3.metric("Status Hidrometeorologi", status_risiko, delta_color=warna)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎨 Mockup & Desain Antarmuka")
        st.warning("Placeholder: Unggah gambar mockup GUI ke GitHub lalu tampilkan dengan st.image('nama_file.png').")
    with col2:
        st.subheader("🖥️ Screenshot Hasil Akhir Aplikasi")
        st.warning("Placeholder: Unggah screenshot aplikasi Python GUI yang sudah berjalan.")
    st.subheader("🛠️ Penjelasan Elemen GUI")
    st.markdown("""
    - **Tombol Load Dataset:** Memilih file data curah hujan (`.csv` / `.xlsx`).
    - **Panel Parameter Statistik:** Menampilkan nilai rata-rata, median, dan curah hujan maksimum.
    - **Kanvas Grafik:** Menampilkan kurva deret waktu (*time-series*) curah hujan.
    - **Panel Prediksi ML:** Input suhu, kelembapan, dan tekanan udara untuk memprediksi kategori hujan.
    """)

# MENU 3
elif menu == "3. Flowchart & Sistem":
    st.header("03. Flowchart & Sistem")
    st.info("Bagian ini menampilkan diagram alir algoritma, flowchart sistem, dan arsitektur sistem Kelompok B07.")
    st.subheader("📐 Diagram Arsitektur & Flowchart")
    st.write("Gunakan bagian ini untuk menampilkan gambar diagram alir yang dibuat menggunakan Draw.io atau Lucidchart.")
    st.warning("Placeholder: Siapkan file gambar flowchart_sistem.png dan arsitektur_b07.png.")

# MENU 4
elif menu == "4. Data & Machine Learning":
    st.header("04. Data & Machine Learning")
    st.info("Bagian ini berisi dataset cuaca, sumber data, tahapan preprocessing, model Random Forest, dan evaluasi.")
    st.subheader("📊 Preview Dataset Cuaca (Contoh Simulasi)")
    data_dummy = pd.DataFrame({
        "Tanggal": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"],
        "Suhu_C": [24.5, 23.1, 26.0, 22.8],
        "Kelembapan_%": list((80,90,75,95)),
        "Curah_Hujan_mm": [12.4, 58.2, 2.0, 110.5],
        "Kategori_BMKG": ["Hujan Ringan", "Hujan Lebat", "Hujan Ringan", "Hujan Sangat Lebat"]
    })
    st.dataframe(data_dummy, use_container_width=True)

    st.subheader("📈 Visualisasi Grafik Curah Hujan Harian")
    st.bar_chart(data_dummy.set_index("Tanggal")["Curah_Hujan_mm"], color="#38bdf8")

    with st.expander("📂 Uji Coba Unggah Dataset Cuaca (.CSV) Secara Langsung"):
        file_csv = st.file_uploader("Upload file dataset cuaca (.csv) di sini:", type=["csv"])
        if file_csv is not None:
            df_upload = pd.read_csv(file_csv)
            st.success(f"Berhasil memuat {len(df_upload)} baris data!")
            st.dataframe(df_upload.head(10), use_container_width=True)

    st.subheader("🌲 Model Random Forest & Evaluasi")
    st.markdown("""
    - **Sumber Data:** Data observasi meteorologi harian (BMKG / Kaggle Weather Dataset).
    - **Preprocessing:** Pembersihan data *null*, normalisasi fitur numerik, dan *encoding* label kategori hujan.
    - **Algoritma:** *Random Forest Classifier* (100 *decision trees*).
    - **Metrik Evaluasi:** Akurasi, *Precision*, *Recall*, dan *Confusion Matrix*.
    """)

# MENU 5
elif menu == "5. Laporan & Dokumentasi":
    st.header("05. Laporan & Dokumentasi")
    st.info("Bagian ini berisi ringkasan laporan akhir, latar belakang fisika, tujuan, metodologi, dan referensi.")
    st.subheader("📖 Latar Belakang & Konsep Fisika")
    st.write("""
    Curah hujan merupakan salah satu variabel fisis utama dalam siklus hidrologi dan dinamika atmosfer bumi. 
    Analisis statistik dan klasifikasi intensitas presipitasi sangat penting untuk memitigasi risiko hidrometeorologi 
    seperti banjir dan kekeringan.
    """)
    st.subheader("🎯 Tujuan Proyek")
    st.write("Membangun aplikasi berbasis GUI menggunakan Python untuk menganalisis data statistik curah hujan dan mengklasifikasikan tingkat intensitas hujan secara otomatis.")
    st.subheader("📚 Referensi")
    st.markdown("""
    1. Badan Meteorologi, Klimatologi, dan Geofisika (BMKG) - Standar Klasifikasi Intensitas Curah Hujan.
    2. Dokumentasi Resmi Python & Scikit-Learn (*Random Forest Classifier*).
    """)
