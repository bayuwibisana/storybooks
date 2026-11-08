# 🖍️ Kisah Krayon — 105 Buku Cerita Pengantar Tidur Anak

**Kisah Krayon** adalah seri 105 buku cerita bergambar pengantar tidur (*bedtime picture books*) dwibahasa (Bahasa Indonesia & English) untuk anak usia 2–6 tahun. Mengusung gaya ilustrasi krayon lilin (*handcrafted wax crayon*) dan goresan kapur pastel (*soft chalky oil pastel*) di atas kertas cat air bertekstur, setiap buku dirancang untuk menciptakan suasana tidur yang hangat, tenang, dan aman.

Setiap cerita dilengkapi dengan:
- **1 Sampul + 10 Halaman Ilustrasi Penuh** (Rasio lanskap 4:3, bebas teks, mata kancing bulat hitam).
- **Narasi Dwibahasa (Bilingual ID/EN)**: Kalimat pendek dan menenangkan.
- **Kutipan Pengantar Tidur (*Bedtime Quote*)** & **Pertanyaan Interaktif (*Co-reading Guidance*)**.
- **Voiceover Narasi Audio (TTS)**: Menggunakan model resmi Google `gemini-3.1-flash-tts-preview` dengan karakter suara `Despina` (Wanita) dan `Enceladus` (Pria).

---

## 📁 Struktur Repositori

```text
storybooks/
├── AGENTS.md               # Panduan mutlak instruksi AI, art direction, aturan kuota, & log proyek
├── PROGRESS.md             # Status progres rinci ilustrasi, teks, audio TTS, & platform web
├── README.md               # Dokumentasi master proyek (berkas ini)
├── data/
│   └── stories_full.json   # Master katalog dan naskah 105 cerita
├── preview/                # Web viewer statis & aset produksi
│   ├── images/             # 410 berkas ilustrasi produksi (.jpg) untuk Cerita 1 s.d. 36
│   ├── audio/              # Berkas suara narasi (.wav)
│   ├── stories.json        # Katalog data 36 cerita terbit
│   ├── stories_bundle.js   # Bundle browser untuk preview reader
│   └── index.html          # Static preview reader
├── scripts/                # Skrip utilitas produksi & audio TTS
│   ├── generate_story_tts.py   # Generator audio Gemini 3.1 TTS
│   ├── build_full_library.py   # Compiler metadata naskah
│   ├── generate_105_stories.py # Generator draft naskah 105 cerita
│   ├── merge_all_105_stories.py# Merger naskah dwibahasa
│   └── verify_stories_1_to_10.py # Skrip verifikasi aset
└── web/                    # Platform aplikasi web full-stack (Astro 5 SSR)
    ├── src/pages/          # Routing: Perpustakaan (/), Baca (/baca/[id]), Akun (/akun)
    ├── src/db/             # Drizzle ORM schema & Neon Postgres client
    └── scripts/seed.mjs    # Idempotent database seeder
```

---

## 🤖 Standar Model Resmi Wajib (STRICT MODEL DIRECTIVES)

Untuk menjaga konsistensi tekstur visual dan karakter suara di seluruh 105 cerita, proyek ini menerapkan **aturan model mutlak tanpa toleransi fallback**:

| Fungsi | Model Wajib (STRICT) | Ketentuan Khusus |
| :--- | :--- | :--- |
| **Generasi Gambar (Illustrations)** | **`google/nano-banana-2.1`** | Dilarang beralih ke Flux, Midjourney, SD, dll. Menjamin goresan krayon lilin & tekstur kertas cat air konsisten. |
| **Narasi Suara (TTS Voiceover)** | **`gemini-3.1-flash-tts-preview`** | Dilarang beralih ke model 3.8 atau 2.5 (mencegah noise/vokal pecah). Voice: **`Despina`** (Wanita) & **`Enceladus`** (Pria). |

---

## 🎨 Standar Seni & Visual (Strict Art Direction)

Semua ilustrasi buku wajib mematuhi aturan visual yang tertera di [`AGENTS.md`](AGENTS.md):
1. **Model Generasi Wajib**: HANYA menggunakan `google/nano-banana-2.1`.
2. **Medium & Tekstur**: Goresan krayon lilin bertekstur nyata (*waxy crayon strokes*) dengan bauran lembut kapur pastel pada kertas cat air krem bertekstur kasar.
3. **Mata Karakter**: Sederhana berupa titik hitam bulat (*simple black bead dot eyes*). Dilarang mata bercincin iris atau gaya anime.
4. **Aspek Rasio**: Lanskap 4:3 horizontal.
5. **100% Bebas Teks**: Tanpa huruf, angka, judul, tanda tangan, atau watermark di dalam gambar.
6. **Batasan Anatomi Anggota Gerak (4 Limbs Only)**: Hewan antropomorfik wajib memiliki **tepat 4 anggota gerak** (2 kaki berdiri + 2 tangan/kaki depan memegang benda). Dilarang memiliki 6 anggota gerak.

---

## 🎙️ Standar Narasi Audio (TTS)

- **Model Mutlak**: `gemini-3.1-flash-tts-preview` (Dilarang beralih ke 3.8 atau 2.5 guna menjaga konsistensi tekstur vokal tanpa noise).
- **Karakter Suara Resmi**:
  - Wanita (Default): `Despina` (lembut, menenangkan untuk pengantar tidur).
  - Pria: `Enceladus` (hangat, berwibawa mendongeng).
- **Format**: WAV 24.000 Hz, 16-bit Mono PCM.

---

## 🚀 Menjalankan Proyek

### 1. Menjalankan Web Platform (Astro 5)
Aplikasi web digital reader dengan database Neon Postgres dan Clerk Auth berada di folder `web/`:

```bash
# Gunakan Node.js >= 22.23.4
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
nvm use 22.23.4

cd web
npm install
npm run dev
# Buka di browser: http://localhost:4321
```

### 2. Menjalankan Static Preview Viewer
Untuk melihat preview katalog 36 cerita statis secara langsung:
```bash
python3 -m http.server 8080 --directory preview
# Buka di browser: http://localhost:8080
```

### 3. Generate Audio Narasi (TTS)
```bash
# Generate audio Cerita 2 dengan suara Despina
python3 scripts/generate_story_tts.py 2 --voice Despina

# Generate audio Cerita 2 dengan suara Enceladus (Pria)
python3 scripts/generate_story_tts.py 2 --voice Enceladus
```

---

## 📊 Status Progres Ringkas
- **Ilustrasi Gambar (Cerita 1 s.d. 36)**: ✅ **100% Selesai (410 ilustrasi resolusi tinggi)** tersimpan di Cloudflare R2 bucket `kisah-krayon` dan disk lokal.
- **Audio Narasi**: 
  - Cerita 1: ✅ **100% Selesai** (Suara Wanita `Despina` & Pria `Enceladus` lengkap, total 22 file).
  - Cerita 2: ⏳ **Suara Wanita `Despina` 100% Selesai (11/11 berkas)**; Suara Pria `Enceladus` belum digenerate.
- **Platform Web**: Digital bedtime reader dwibahasa, Cloudflare R2 media streaming via Astro SSR endpoint, laci navigasi cepat 36 buku (*Story Navigation Drawer*), proteksi server-side *Zero-Leak*, dan sistem kredit cerita telah aktif.
- Rincian lengkap dapat dibaca pada [PROGRESS.md](PROGRESS.md).
