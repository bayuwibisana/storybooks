# Kisah Krayon — Roadmap & Status Progres Produksi

> **Terakhir Diperbarui**: 3 November 2026  
> Dokumen ini mencatat status resmi progres produksi ilustrasi, audio narasi (TTS), teks dwibahasa, dan platform web untuk **105 cerita bergambar anak Kisah Krayon**.

---

## 📌 Ringkasan Status Global

| Kategori | Target Keseluruhan | Status Saat Ini | Keterangan |
| :--- | :--- | :--- | :--- |
| **Koleksi Cerita Ditulis** | 105 Cerita | **105 Cerita Naskah Matang (100% SELESAI) ✅** | Teks ID/EN sastrawi, kutipan, & prompt interaktif lengkap untuk seluruh 105 cerita (1.050 Halaman) di `data/stories_full.json` dan `preview/stories.json` |
| **Ilustrasi Gambar** | 1.050 Halaman (+105 Sampul) | **40 Cerita (440 Gambar) ✅** | Model Wajib: **`google/nano-banana-2.1`** (Cerita 1 s.d. 40 selesai penuh 100%) |
| **Audio Narasi (TTS)** | 105 Cerita | **Cerita 1 s.d. 26 (Wanita 100%) ✅** | Fokus: **Bahasa Indonesia Suara Wanita (`Despina`)** via `gemini-3.1-flash-tts-preview`. Cerita 27 progres 7/11 (Cover & Hal 1–6). |
| **Web Platform (`web/`)** | Digital Reader + Gating | **Live di Cloudflare Workers ✅** | URL: `https://storybooks.bayuwibisana15.workers.dev` (Neon HTTP DB, Native R2 Binding, Clerk Auth) |

---

## 🤖 Standar Model Resmi Wajib (STRICT MODEL DIRECTIVES)

1. **Model Ilustrasi Gambar Wajib**:
   - **`google/nano-banana-2.1`** (STRICT: Dilarang keras fallback ke model lain. Menjamin konsistensi goresan waxy crayon lilin dan soft oil pastel di atas kertas cat air krem kasar).
2. **Model Narasi Audio (TTS) Wajib**:
   - **`gemini-3.1-flash-tts-preview`** (STRICT: Dilarang fallback ke model 3.8 atau 2.5 karena isu noise dan instabilitas vokal).
   - Karakter suara resmi: **`Despina`** (Wanita) & **`Enceladus`** (Pria).

---

---

## 🎨 Status Ilustrasi Gambar (40 Cerita Pertama — 100% Selesai)

Semua 40 cerita berikut telah memiliki **1 Sampul + 10 Halaman Ilustrasi** (total 11 file `.jpg` per cerita) dengan gaya waxy krayon 4:3, bebas teks, mata kancing dot hitam, dan anatomi 4 anggota gerak:

| # | Judul Cerita | Kategori | Ilustrasi (Cover + 10 Hal) | Status Audio TTS |
| :-: | :--- | :--- | :-: | :--- |
| **1** | Awan Kecil di Saku Barnaby | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **100% Lengkap** (Despina & Enceladus) |
| **2** | Gadis yang Merajut Selimut Bulan | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **3** | Toko Roti Biji Kenari Raksasa | 🥧 Dapur & Berbagi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **4** | Mercusuar yang Lupa Bersinar | ⛵ Petualangan | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **5** | Pesta Teh Tilly di Atas Awan | 🤝 Persahabatan | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **6** | Kembang Api di Dada Kiko | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **7** | Awan Kelabu di Saku Boni | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **8** | Bayangan Monster di Balik Pintu | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **9** | Piala Emas untuk Bersama | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **10** | Menunggu Roti Matang | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **11** | Langkah Pertama Menyapa Teman | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **12** | Dua Kata Ajaib: Maafkan Aku | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **13** | Piknik Hujan yang Tetap Riang | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **14** | Kursi Kosong di Bawah Pohon | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **15** | Tepukan Bangga untuk Sahabat | 💛 Empati & Emosi | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **16** | Lagu Bintang untuk Si Kecil | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **17** | Kasur Awan Marshmallow | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **18** | Hembusan Napas Angin Malam | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **19** | Lentera Emas Sang Penjaga | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **20** | Lullaby Jangkrik di Bawah Daun | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **21** | Bantal Penyimpan Mimpi Indah | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **22** | Bulan Sabit Berselimut Wol | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **23** | Perahu Kertas Menuju Negeri Lelap | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **24** | Tutup Buku, Buka Mimpimu | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **25** | Hewan Hutan Mengucap Selamat Tidur | 🦉 Pengantar Tidur | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **26** | Rahasia Jungkat-Jungkit Kayu | 🧩 Logika & Sains | ✅ Selesai (11/11) | ✅ **Wanita 100% Selesai (11/11)** (`Despina`) |
| **27** | Batu Tenggelam, Perahu Terapung | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ **Progres 7/11 Selesai** (Cover & Hal 1–6) |
| **28** | Bayangan Tubuh yang Berubah Ukuran | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **29** | Kalung Buah Pola Tiga Warna | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **30** | Sulap Warna Kunyit & Bunga Telang | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **31** | Tetesan Embun yang Menghilang | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **32** | Batu Hitam Penarik Pasir Besi | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **33** | Roda Bundar yang Menggelinding | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **34** | Gema Suara di Mulut Gua | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **35** | Jam Ranting Matahari | 🧩 Logika & Sains | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **36** | Hari Pertama di Sekolah Alam | ⛵ Petualangan | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **37** | Pemeriksaan Gigi Si Buaya Manis | ⛵ Petualangan | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **38** | Pohon Brokoli Mini Ajaib | ⛵ Petualangan | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **39** | Jembatan Bambu Goyang | ⛵ Petualangan | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **40** | Jejak Kaki Rahasia di Pasir | ⛵ Petualangan | ✅ Selesai (11/11) | ⏳ Menunggu antrean TTS |
| **41** | Membuka Mata di Air Kolam | ⛵ Petualangan | ⏳ Tertahan Kuota Resmi (0/11) | ⏳ Menunggu antrean TTS |
| **42** | Tenda Kain di Bawah Bintang | ⛵ Petualangan | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **43** | Mencapai Puncak Bukit Pelangi | ⛵ Petualangan | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **44** | Kompas Daun di Aliran Air | ⛵ Petualangan | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **45** | Gerobak Kayu Beroda Tiga | ⛵ Petualangan | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **46** | Pai Apel Delapan Potong | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **47** | Panci Sup Sayur Gotong Royong | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **48** | Pesta Selai Stroberi Hutan | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **49** | Biskuit Bintang untuk Tetangga | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **50** | Roti Gandum Hangat Musim Salju | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **51** | Madu Secukupnya untuk Beruang | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **52** | Piknik Buah di Bawah Beringin | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **53** | Jus Jeruk Peras Gotong Royong | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **54** | Pancake Madu Minggu Pagi | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **55** | Bekal Kasih Sayang untuk Adik | 🥧 Dapur & Berbagi | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **56** | Langkah Kura-kura & Sayap Walet | 🤝 Persahabatan | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |
| **57** | Gajah Kecil Bertelinga Payung | 🤝 Persahabatan | 📝 Naskah Selesai Dipoles (10 Hal) | ⏳ Menunggu antrean gambar & TTS |

---

## 🎙️ Detail & Aturan Narasi Audio (TTS)

1. **Model Mutlak**:
   - **`gemini-3.1-flash-tts-preview`** (STRICT: Dilarang keras menggunakan 3.8 atau 2.5 karena adanya isu vokal tidak stabil dan noise ujung audio).
2. **Suara Resmi**:
   - Wanita (Default Reader): **`Despina`**
   - Pria: **`Enceladus`**
3. **Spesifikasi Teknis**: WAV 24kHz, 16-bit Mono PCM.
4. **Status Eksekusi Audio**:
   - **Cerita 1 ("Awan Kecil di Saku Barnaby")**: 
     - Suara Wanita (`Despina`): `preview/audio/story1/page_0_cover.wav` s.d. `page_10.wav` (11 file) ✅
     - Suara Pria (`Enceladus`): `preview/audio/story1/male/page_0_cover.wav` s.d. `page_10.wav` (11 file) ✅
   - **Cerita 2 ("Gadis yang Merajut Selimut Bulan")**: 
     - Suara Wanita (`Despina`): Sampul (`page_0_cover.wav`) & Halaman 1 s.d. 10 (`page_1.wav` s.d. `page_10.wav`) ✅ **100% Selesai (11/11)** via `gemini-3.1-flash-tts-preview`.
     - Suara Pria (`Enceladus`): ⏳ **Belum diproses** (antrean berikutnya untuk digenerate per halaman).
   - **Cerita 3 s.d. 36**: Menunggu antrean generasi bertahap.

---

## 💻 Status Platform Web (`web/`)

- **Live Production URL**: **`https://storybooks.bayuwibisana15.workers.dev`** ✅ (HTTP/2 200 OK untuk HTML, Covers, Pages, dan Audio).
- **Tech Stack**: Astro 5 SSR (`@astrojs/cloudflare` Adapter v14), Cloudflare Workers Runtime dengan `nodejs_compat`, Neon Serverless Postgres via `drizzle-orm/neon-http`, Clerk Auth (`@clerk/astro`).
- **Node.js**: Wajib `>=22.23.4`.
- **Database & Data**: 36 cerita + 360 halaman tersimpan di Neon Postgres dan ter-seed penuh.
- **Arsitektur Edge Cloudflare Workers**:
  - **Native R2 Bucket Binding**: Dikonfigurasi di [`web/wrangler.json`](web/wrangler.json) (`R2_BUCKET_BINDING` → `kisah-krayon`). Menghilangkan kebutuhan credentials/keys AWS S3 di edge dan memberikan performa streaming nol-latensi.
  - **Neon HTTP Driver**: Migrasi dari driver WebSocket `Pool` ke `neon(connectionString)` stateless via `drizzle-orm/neon-http` dengan Lazy Proxy resolution di [`web/src/db/client.ts`](web/src/db/client.ts), mencegah crash edge isolate.
  - **Runtime Environment Resolution**: Menggunakan helper [`web/src/lib/env.ts`](web/src/lib/env.ts) yang mengimpor native `env` dari `cloudflare:workers` (standar resmi pengganti `Astro.locals.runtime.env`).
  - **Public Variables**: Variabel publik seperti `PUBLIC_CLERK_PUBLISHABLE_KEY` dan `PUBLIC_SITE_URL` didaftarkan langsung di `wrangler.json` `vars`.
  - **Error Diagnostics**: Halaman kustom [`web/src/pages/500.astro`](web/src/pages/500.astro) dan error boundary di `index.astro`.
- **Manajemen Repositori Git**:
  - Repositori Git diinisialisasi khusus di dalam folder [`web/`](web/) (`web/.git`) dan terhubung ke GitHub `https://github.com/bayuwibisana/storybooks`.
  - Seluruh file rahasia `.env`, build `.astro`, `.wrangler`, `dist`, dan file biner media diabaikan oleh `.gitignore`.
- **Media Asset Storage**:
  - Semua 429 file media (36 covers, 360 pages, 33 audio WAVs) telah tersimpan di **Cloudflare R2** bucket `kisah-krayon`.
  - Streaming media ditangani oleh endpoint SSR (`/covers/*`, `/pages/*`, `/audio/*`).
- **Reader Interface**:
  - Tampilan bacaan 4:3 responsif dengan kontrol keyboard & sentuh.
  - Sakelar bahasa ID/EN dan penskala font (`Aa`).
  - Laci navigasi cepat (**Story Navigation Drawer**) untuk melompat antar 36 cerita langsung dari halaman pembaca.
  - Perlindungan server-side *Zero-Leak*: Cerita berbayar (#4–#36) tidak membocorkan teks maupun gambar jika belum dibuka.
- **Audio Feature Flag**: Otomatis aktif di lingkungan lokal (`import.meta.env.DEV`), dan dinonaktifkan di produksi sampai seluruh audio siap.

---

## 🔭 Rencana Kerja Berikutnya (Next Steps)

1. **Generate Audio Cerita 2 Suara Pria (`Enceladus`)**: Generate Halaman 0 s.d. 10 secara bertahap satu per satu (`scripts/generate_story_tts.py 2 --voice Enceladus`).
2. **Sinkronisasi Audio Pria ke R2**: Jalankan skrip upload R2 setelah audio `Enceladus` Cerita 2 terverifikasi.
3. **Mulai Batch Audio untuk Cerita 3 s.d. 36** secara bertahap mematuhi aturan per halaman.
4. **Batch Tulis & Ilustrasi Cerita 37 s.d. 105** (Task 4 s.d. 11).
