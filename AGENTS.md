# AGENTS.md — Kisah Krayon Production Guide & Project Log

> **Note for AI Agents & New Sessions**:  
> Read this document first before executing any tasks. It contains the current progress, art direction, strict anatomy and visual rules, quota handling protocols, and synchronization steps.

---

## 1. Project Mission & Overview
- **Project**: Kisah Krayon — 105 Indonesian children's bedtime picture books (*buku cerita pengantar tidur anak*).
- **Format**: Each story contains **1 Cover + 10 Pages** (11 illustrations total) with rich bilingual text (Indonesian main text + English subtitles), moral lessons, and co-reading prompts (*pertanyaan interaktif orang tua & anak*).
- **Target Audience**: Ages 2–6 (soothing, gentle, cozy bedtime atmosphere).

---

## 2. Current Progress & Status (As of October 28, 2026)

### ✅ Completed Stories & Illustrations (Stories 1 – 40: 100% DONE)
- **Total Images**: **440 high-resolution illustrations** generated, visually verified with `read_file`, saved in `preview/images/`, uploaded to Cloudflare R2 (`covers/` and `pages/`), and mirrored to `/Users/bayu/local/storybooks/preview/images/` and `web/public/`.
- **Coverage**: All 40 published stories have full 1 Cover + 10 Pages (11 illustrations each).
- **Text & Metadata**: All 40 stories have complete bilingual narratives (ID/EN), bedtime quotes, and parent-child co-reading prompts in `preview/stories.json`, bundled in `preview/stories_bundle.js`, and seeded in Neon Postgres (40 stories / 400 pages).
- **Story 37 ("Pemeriksaan Gigi Si Buaya Manis")**: ✅ **100% SELESAI**
  - Cover + Pages 1 s.d. 10 selesai 100% diproduksi menggunakan model `google/nano-banana-2.1` via Antigravity `image-generator` subagent.
  - Mematuhi anatomi ketat 4 anggota gerak (2 kaki berdiri + 2 lengan bipedal), mata kancing bulat hitam, tekstur krayon waxy & soft oil pastel di kertas watercolor bertekstur, 100% bebas teks, rasio 4:3 landscape.
- **Story 38 ("Pohon Brokoli Mini Ajaib")**: ✅ **100% SELESAI (SUDAH DIREGENERASI & KONSISTEN PENUH)**
  - Naskah dan narasi lengkap.
  - **Hasil Perbaikan Glitch & Inkonsistensi (Hal 3, 4, 6, 9)**:
    1. **Rambut Rian**: Diperbaiki 100% di semua halaman menjadi rambut lurus **HITAM PEKAT** (*straight jet-black hair with neat childlike bangs*), keriting di Hal 3 dan warna cokelat telah dihilangkan.
    2. **Rambut Mama**: Diperbaiki 100% di semua halaman menjadi sanggul rapi warna **HITAM ALAMI** (*natural jet-black hair in a neat low bun*).
    3. **Topi Koki Rian**: Di Hal 6 telah dikembalikan secara konsisten menjadi **topi kertas lipat origami putih** (*folded white origami paper chef hat*).
    4. **Glitch Hal 9 (Anatomi Tangan & Sikat Gigi)**: Glitch sikat gigi melayang telah diperbaiki sempurna — tangan kanan Rian memegang erat gagang sikat gigi saat menyikat, tangan kiri bertumpu di wastafel. Bebas dari coretan tanda tangan.
  - Seluruh 11 aset telah diverifikasi visual (`read_file`), diunggah ke Cloudflare R2, dan di-seed di Neon Postgres.
- **Story 39 ("Jembatan Bambu Goyang")**: ✅ **100% SELESAI**
  - Cover + Pages 1 s.d. 10 selesai 100% diproduksi menggunakan model resmi `google/nano-banana-2.1` via Antigravity `image-generator` subagent.
  - Konsistensi karakter Tegar (kaos biru, celana batik, sandal jepit merah, kulit sawo matang) & Bono (monyet kecil berbulu cokelat bertopi caping mini), pemandangan jembatan gantung bambu, capung jarum biru, kebun mangga kakek di kala senja, dan tidur nyenyak di ranjang bambu bertikar pandan. Seluruh 11 aset telah diverifikasi visual, diunggah ke R2, dan di-seed ke Neon DB.
- **Story 40 ("Jejak Kaki Rahasia di Pasir")**: ✅ **100% SELESAI**
  - Cover + Pages 1 s.d. 10 selesai 100% diproduksi menggunakan model resmi `google/nano-banana-2.1` via Antigravity `image-generator` subagent.
  - Konsistensi karakter Lani (gaun kuning, topi jerami pita biru, kepang dua) & Koko (kepiting oranye), mata kancing bulat hitam, tekstur krayon waxy & soft oil pastel, 100% bebas teks, rasio 4:3 landscape, anatomi ketat bipedal. Ombak senja yang tenang menyapu jejak kaki di pasir, matahari terbenam merah saga, dan tidur lelap di pondok kayu pantai berlentera kerang laut. Seluruh 11 aset telah diverifikasi visual, diunggah ke R2, dan di-seed ke Neon DB.
- **Story 39 ("Jembatan Bambu Goyang")**: ⏳ **PROGRES 7/11 SELESAI**
  - Cover + Pages 1 s.d. 6 selesai 100% diproduksi menggunakan `google/nano-banana-2.1` via `image-generator` subagent.
  - Semua 7 ilustrasi telah diverifikasi secara visual (`read_file`), disimpan di `preview/images/`, dan dimirror ke `preview/images/` serta `web/public/`.
  - Halaman 7 s.d. 10 tertunda sementara karena batas kuota mingguan model (`429 RESOURCE_EXHAUSTED: quota reset 167h50m23s`). Sesuai aturan: tidak memasang timer untuk kuota mingguan, pekerjaan dihentikan dan dilaporkan dengan jelas ke user.
- **Story 40 ("Jejak Kaki Rahasia di Pasir")**: ⏳ **PROGRES 8/11 SELESAI**
  - Cover + Pages 1 s.d. 7 selesai 100% diproduksi menggunakan model `google/nano-banana-2.1` via Antigravity `image-generator` subagent.
  - Semua 8 ilustrasi (`story40_cover.jpg`, `story40_page1.jpg` s.d. `story40_page7.jpg`) telah diverifikasi secara visual (`read_file`), disimpan di `preview/images/`, dan tersambung ke `web/public/`.
  - Mematuhi konsistensi karakter Lani (gaun kuning, topi jerami pita biru, kepang dua) & Koko (kepiting oranye), mata kancing bulat hitam, tekstur krayon waxy & soft oil pastel, 100% bebas teks, rasio 4:3 landscape, anatomi ketat bipedal (2 kaki + 2 lengan).
  - Halaman 8 s.d. 10 tertunda sementara karena batas kuota mingguan model (`429 RESOURCE_EXHAUSTED: quota will reset after 167h49m31s`). Sesuai instruksi: tidak membuat timer, eksekusi dihentikan dan sisa waktu dilaporkan kepada user.
- **Story 41 ("Membuka Mata di Air Kolam")**: ⏳ **PROGRES 0/11 (TERTAHAN BATAS KUOTA RESMI `google/nano-banana-2.1`)**
  - Sesuai instruksi mutlak user: **Dilarang menggunakan fal.ai atau kie.ai**, hanya boleh menggunakan model resmi `google/nano-banana-2.1` via Antigravity `image-generator` subagent.
  - Generasi sampul dan 10 halaman tertunda sementara karena batas limit/kuota model resmi tercapai (`429 RESOURCE_EXHAUSTED` / backend 500 error).
  - Sesuai instruksi: tidak membuat timer, proses dihentikan dan status progres diperbarui.
- **Story 15 Glitch Fix**:
  - Addressed anatomy bug where the fawn (*Bintang*) mistakenly had 6 limbs (4 quadruped legs + 2 arms).
  - Regenerated Page 1 (`story15_page1.jpg`) and Page 4 (`story15_page4.jpg`) with strict bipedal constraints (2 legs on ground + 2 arms/hooves). Verified clean and mirrored.

### 🎙️ Audio Narration (TTS) Status
- **Prioritas & Fokus Utama**:
  - **HANYA fokus mengerjakan narasi audio Bahasa Indonesia suara wanita (`Despina`)**.
  - **Suara pria (`Enceladus`) dan audio Bahasa Inggris ditunda / didefer**.
  - **Catatan Bahasa Inggris**: Jika mode Bahasa Inggris (`EN`) diaktifkan di reader/katalog, tampilkan catatan kecil: *"Audio bahasa Inggris belum tersedia dan akan segera ditambahkan."*
- **Cerita 1 ("Awan Kecil di Saku Barnaby")**: ✅ **100% SELESAI**
  - Voice Wanita (`Despina`): Cover + Hal 1–10 (11 berkas WAV).
  - Voice Pria (`Enceladus`): Cover + Hal 1–10 (11 berkas WAV).
- **Cerita 2 ("Gadis yang Merajut Selimut Bulan")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`.
- **Cerita 3 ("Toko Roti Biji Kenari Raksasa")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 4 ("Mercusuar yang Lupa Bersinar")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 5 ("Pesta Teh Tilly di Atas Awan")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina` via `GEMINI_API_KEY_04`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 6 ("Kembang Api di Dada Kiko")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina` via `GEMINI_API_KEY_97` & `GEMINI_API_KEY_MAILPIT`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 7 ("Awan Kelabu di Saku Boni")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina` via `GEMINI_API_KEY_MAILPIT` & `GEMINI_API_KEY_STF`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 8 ("Bayangan Monster di Balik Pintu")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina` via `GEMINI_API_KEY_SIS` & `GEMINI_API_KEY_STF`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 9 ("Piala Emas untuk Bersama")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 10 ("Menunggu Roti Matang")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 11 ("Langkah Pertama Menyapa Teman")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 12 ("Dua Kata Ajaib: Maafkan Aku")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 13 ("Piknik Hujan yang Tetap Riang")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 14 ("Kursi Kosong di Bawah Pohon")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 15 ("Tepukan Bangga untuk Sahabat")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 16 ("Lagu Bintang untuk Si Kecil")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 17 ("Kasur Awan Marshmallow")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 18 ("Hembusan Napas Angin Malam")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 19 ("Lentera Emas Sang Penjaga")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 20 ("Lullaby Jangkrik di Bawah Daun")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 21 ("Bantal Penyimpan Mimpi Indah")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 22 ("Bulan Sabit Berselimut Wol")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
- **Cerita 23 ("Perahu Kertas Menuju Negeri Lelap")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
- **Cerita 24 ("Tutup Buku, Buka Mimpimu")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
- **Cerita 25 ("Hewan Hutan Mengucap Selamat Tidur")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
- **Cerita 26 ("Rahasia Jungkat-Jungkit Kayu")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
- **Cerita 27 ("Batu Tenggelam, Perahu Terapung")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 28 ("Bayangan Tubuh yang Berubah Ukuran")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 29 ("Kalung Buah Pola Tiga Warna")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 30 ("Sulap Warna Kunyit & Bunga Telang")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 31 ("Tetesan Embun yang Menghilang")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 32 ("Batu Hitam Penarik Pasir Besi")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 33 ("Roda Bundar yang Menggelinding")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 34 ("Gema Suara di Mulut Gua")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Format WAV 24kHz Mono 16-bit PCM terverifikasi. Diunggah ke Cloudflare R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 35 ("Jam Ranting Matahari")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Format WAV 24kHz Mono 16-bit PCM terverifikasi. Diunggah ke Cloudflare R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 36 ("Hari Pertama di Sekolah Alam")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul `page_0_cover.wav` & Hal 1–10 (`page_1.wav` s.d. `page_10.wav`) selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Format WAV 24kHz Mono 16-bit PCM terverifikasi. Diunggah ke Cloudflare R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 37 ("Pemeriksaan Gigi Si Buaya Manis")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Format WAV 24kHz Mono 16-bit PCM terverifikasi. Diunggah ke Cloudflare R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 38 ("Pohon Brokoli Mini Ajaib")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Format WAV 24kHz Mono 16-bit PCM terverifikasi. Diunggah ke Cloudflare R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 39 ("Jembatan Bambu Goyang")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Format WAV 24kHz Mono 16-bit PCM terverifikasi. Diunggah ke Cloudflare R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Cerita 40 ("Jejak Kaki Rahasia di Pasir")**: ✅ **SUARA WANITA 100% SELESAI (11/11)**
  - Sampul & Halaman 1 s.d. 10 selesai 100% menggunakan `gemini-3.1-flash-tts-preview` voice `Despina`. Format WAV 24kHz Mono 16-bit PCM terverifikasi. Diunggah ke Cloudflare R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
- **Status Audio Keseluruhan**: ✅ **Cerita 1 s.d. 40 (Seluruh 40 Buku Terbit) SUARA WANITA 100% SELESAI (440 file audio narasi halaman + 40 file cover = 480 file audio)**. Tersinkronisasi penuh di Cloudflare R2 dan Neon Postgres.

### ⏳ Pending Work for Next Sessions
- **Audio Batch Berikutnya**:
  - Cerita 41 s.d. 105 akan diproduksi audionya seiring atau setelah fase produksi ilustrasi selesai.
- **Story 41 s.d. 105 (Batch 2 Naskah: 100% SELESAI)**:
  - **Cerita 41 s.d. 105 (65 Cerita / 650 Halaman)**: ✅ **100% SELESAI**. Seluruh naskah dwibahasa (ID/EN) 1 Cover + 10 Halaman per cerita telah selesai dipoles secara sastrawi & puitis di `data/stories_full.json`, lengkap dengan `quote`, `coReading`, dan `imagePrompt` (4:3 horizontal, 4 limbs constraint, bead dot eyes). Siap masuk fase produksi ilustrasi bertahap menggunakan `google/nano-banana-2.1`.

---

## 3. Strict Illustration Art Direction & Rules

Every illustration must strictly adhere to the following artistic standards:

1. **Model Generasi Gambar Wajib (STRICT MODEL CONSTRAINT)**:
   - **HANYA boleh menggunakan model `google/nano-banana-2.1`**.
   - **STRICT CONSTRAINT**: DILARANG KERAS beralih atau fallback ke model lain (seperti Flux, Midjourney, Stable Diffusion, atau model lama lainnya). Semua ilustrasi 105 buku cerita anak Kisah Krayon wajib diproduksi secara konsisten menggunakan `google/nano-banana-2.1`.
2. **Medium & Texture**:
   - Handcrafted wax crayon scribbles and soft chalky oil pastel smudges on heavy textured cream watercolor paper.
   - Visible waxy crayon strokes, soft finger blending, naive folk-art perspective.
   - Warm, cozy bedtime atmosphere with gentle glowing highlights (lanterns, moonbeams, stars).
3. **Eye Style**:
   - **Simple black bead dot eyes** (*mata kancing bulat hitam*).
   - No complex pupils, iris rings, or anime-style sparkling eyes.
4. **Aspect Ratio**:
   - **4:3 horizontal landscape**.
5. **100% COMPLETELY TEXT-FREE**:
   - Absolutely no letters, words, titles, page numbers, signatures, signs, or watermarks in the generated image.
6. **CRITICAL: Strict Limb & Anatomy Constraint**:
   - For all anthropomorphic animal characters: **EXACTLY 4 LIMBS TOTAL** (2 legs walking/standing + 2 arms/hooves holding objects).
   - **STRICT NEGATIVE PROMPT**: Never render 6 limbs, never render 4 quadruped legs under the belly while having 2 extra human arms on the torso.

---

## 4. Strict Audio Narration (TTS) Direction & Rules

Setiap berkas narasi audio (*voiceover*) cerita anak wajib mematuhi standar konsistensi berikut tanpa pengecualian:

1. **Fokus Bahasa & Suara (Strict Focus Constraint)**:
   - **HANYA fokus memproduksi audio narasi Bahasa Indonesia suara wanita (`Despina`)**.
   - Suara pria (`Enceladus`) dan audio Bahasa Inggris ditunda / ditangguhkan.
   - **Ketentuan Tampilan Bahasa Inggris (EN UI Note)**: Apabila pengguna memilih atau mengganti bahasa bacaan ke Bahasa Inggris (`EN`), antarmuka web wajib menampilkan catatan kecil yang ramah:
     > *"Audio bahasa Inggris belum tersedia dan akan segera ditambahkan."*
2. **Model & Endpoint Generasi Audio**:
   - Model resmi: **`gemini-3.1-flash-tts-preview`** (cloud API) atau **Local VoiceStudio API** (`http://localhost:3900/v1/audio/speech`) dengan zero-shot cloning model `omnivoice` (MPS Apple Silicon, native 24 kHz mono output).
   - **STRICT CONSTRAINT**: DILARANG menggunakan `gemini-3.8-flash-tts` karena menghasilkan noise/glitch di akhir audio dan ketidakstabilan timbre.
3. **Karakter Suara Resmi (Voice Mapping)**:
   - **Voice Wanita (Default & Utama)**: **`Despina`** (profil suara lembut, ramah, dan menenangkan untuk pengantar tidur).
   - **Voice Pria (Ditunda)**: `Enceladus`.
4. **Format & Spesifikasi Berkas Mutlak**:
   - Format: WAV 24.000 Hz (24kHz), 16-bit Mono PCM.
5. **Struktur Penyimpanan Berkas**:
   - Voice Wanita (Default): `preview/audio/story{X}/page_{N}.wav` (sampul: `page_0_cover.wav`, halaman 1–10: `page_1.wav` s.d. `page_10.wav`).
   - Voice Pria: `preview/audio/story{X}/male/page_{N}.wav` (ditunda).
6. **ATURAN MUTLAK GENERASI PER HALAMAN (STRICT SINGLE-PAGE GENERATION)**:
   - **Wajib generate PER HALAMAN (generate per page only)**.
   - **DILARANG KERAS** men-generate seluruh halaman secara massal / serentak dalam satu batch besar.
   - Prosedur: Generate 1 halaman -> verifikasi respon `HTTP 200` dan spesifikasi berkas WAV -> simpan/mirror -> jeda rate-limit -> baru lanjutkan ke halaman berikutnya. Hal ini untuk mempersingkat waktu generasi, mencegah memory pressure (`ReferenceEncodeMemoryError`), dan memastikan kontrol kualitas audio tetap terjaga.
7. **Ketentuan Profil Kloning VoiceStudio**:
   - **Style Field**: Boleh dikosongkan (`instruct=""`). Karakter vokal sepenuhnya diambil dari referensi audio (`zero-shot reference cloning`).
   - **Durasi Reference Audio**: Wajib 5 s.d. 8 detik (maksimal 10 detik). Jangan menggunakan referensi di atas 15 detik agar tidak memicu kehabisan memori CPU pada tokenizer DAC.
8. **Status Kepatuhan Audio per Cerita**:
   - **Cerita 1 ("Awan Kecil di Saku Barnaby")**: ✅ **SUDAH SESUAI** (lengkap `Despina` & `Enceladus` 100%).
   - **Cerita 2 ("Gadis yang Merajut Selimut Bulan")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 3 ("Toko Roti Biji Kenari Raksasa")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 4 ("Mercusuar yang Lupa Bersinar")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 5 ("Pesta Teh Tilly di Atas Awan")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 6 ("Kembang Api di Dada Kiko")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 7 ("Awan Kelabu di Saku Boni")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 8 ("Bayangan Monster di Balik Pintu")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 9 ("Piala Emas untuk Bersama")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 10 ("Menunggu Roti Matang")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 11 ("Langkah Pertama Menyapa Teman")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 12 ("Dua Kata Ajaib: Maafkan Aku")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 13 ("Piknik Hujan yang Tetap Riang")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 14 ("Kursi Kosong di Bawah Pohon")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 15 ("Tepukan Bangga untuk Sahabat")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 16 ("Lagu Bintang untuk Si Kecil")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 17 ("Kasur Awan Marshmallow")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 18 ("Hembusan Napas Angin Malam")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 19 ("Lentera Emas Sang Penjaga")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 20 ("Lullaby Jangkrik di Bawah Daun")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`).
   - **Cerita 21 ("Bantal Penyimpan Mimpi Indah")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 22 ("Bulan Sabit Berselimut Wol")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 23 ("Perahu Kertas Menuju Negeri Lelap")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 24 ("Tutup Buku, Buka Mimpimu")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 25 ("Hewan Hutan Mengucap Selamat Tidur")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 26 ("Rahasia Jungkat-Jungkit Kayu")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 27 ("Batu Tenggelam, Perahu Terapung")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 28 ("Bayangan Tubuh yang Berubah Ukuran")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 29 ("Kalung Buah Pola Tiga Warna")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 30 ("Sulap Warna Kunyit & Bunga Telang")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 31 ("Tetesan Embun yang Menghilang")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 32 ("Batu Hitam Penarik Pasir Besi")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 33 ("Roda Bundar yang Menggelinding")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 34 ("Gema Suara di Mulut Gua")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 35 ("Jam Ranting Matahari")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 36 ("Hari Pertama di Sekolah Alam")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 37 ("Pemeriksaan Gigi Si Buaya Manis")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 38 ("Pohon Brokoli Mini Ajaib")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 39 ("Jembatan Bambu Goyang")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 40 ("Jejak Kaki Rahasia di Pasir")**: ✅ **SUARA WANITA 100% LENGKAP (11/11)** (`Despina` via `gemini-3.1-flash-tts-preview`). Diunggah ke R2 bucket `kisah-krayon` & di-seed di Neon Postgres.
   - **Cerita 41 s.d. 105**: Siap diproses bertahap per halaman setelah fase produksi ilustrasi batch berikutnya.

---

## 5. Quota & Timer Rules (Strict User Directives)

When running image generation batches:

- **Rolling 5-Hour Limit (`429 RESOURCE_EXHAUSTED`)**:
  - Extract the reset duration from the error message.
  - Add a **5-minute buffer** to the remaining delay.
  - Schedule a one-shot wakeup timer using the `schedule` tool.
  - Once awakened, resume the story generation.
- **Weekly Quota Limit (Capacity Exhausted over several days)**:
  - **DO NOT create a timer.** (User explicitly instructed: *"jika kuota mingguan muncul, jangan buat timer"*).
  - Report the remaining reset time clearly to the user and halt execution.

---

## 6. File Architecture & Synchronization

| Component | Path | Description |
| :--- | :--- | :--- |
| **Workspace Git Tree** | `/Users/bayu/.ao/data/worktrees/storybooks/kerjakan-cerita-2` | Main worktree for editing and code changes |
| **Local Mirror** | `/Users/bayu/local/storybooks/preview/` | Local directory for web viewer live preview |
| **Story Data (JSON)** | `preview/stories.json` | Master catalog of 105 stories |
| **Viewer Bundle** | `preview/stories_bundle.js` | `window.STORIES_DATA = [...]` generated from `stories.json` |
| **Images Folder** | `preview/images/` | All cover and page `.jpg` files |
| **Viewer Frontend** | `preview/index.html`, `preview/script.js` | Web reader (has auto-scroll to top on page turns) |

### Synchronization Commands:
After generating any image or updating story narratives:
```bash
# 1. Mirror images to local directory:
cp preview/images/story*.jpg /Users/bayu/local/storybooks/preview/images/

# 2. Re-bundle stories_bundle.js from stories.json:
python3 -c "import json; d=json.load(open('preview/stories.json')); open('preview/stories_bundle.js', 'w').write('window.STORIES_DATA = ' + json.dumps(d, ensure_ascii=False, indent=2) + ';')"

# 3. Mirror JSON and JS bundle to local preview:
cp preview/stories.json preview/stories_bundle.js /Users/bayu/local/storybooks/preview/
```

---

## 7. How to Continue Next Session (Storybook Production)

1. **Audio Narration Continuation**:
   - Fokus: Bahasa Indonesia suara wanita (`Despina`).
   - Story 1, 2, & 3 suara wanita (`Despina`): 100% SELESAI (Sampul & Hal 1–10).
   - Lanjutkan audio narration untuk Cerita 4 s.d. 36 secara bertahap satu per satu (Wanita: `Despina`).
2. **Batch 2 Story Writing & Illustrations (Stories 37 – 105)**:
   - Draft bilingual narratives, bedtime quotes, and prompts in `preview/stories.json`.
   - Generate 1 Cover + 10 Pages per story following strict 4-limb, bead eyes, crayon aesthetic rules.
   - Mirror files to `/Users/bayu/local/storybooks/preview/images/` and re-bundle `stories_bundle.js`.
3. **Web Platform Integrations**:
   - Implement Lynk.id webhook handler (`web/src/pages/api/webhook/lynk.ts`).
   - Configure R2 storage or keep static public asset routing.

---

## 8. Web Application Platform (`web/`) — Architecture & Roadmap

> **Context for Hermes & Future Coding Sessions**:  
> The project includes a full-stack digital picture book web app located in `web/`.

### 🛠️ Tech Stack & Services
- **Framework**: Astro 5 SSR with `@astrojs/cloudflare` adapter.
- **Node Requirement**: `>=22.23.4` (enforced in `web/.nvmrc`).
- **Database**: Neon Serverless Postgres via `@neondatabase/serverless` & Drizzle ORM.
- **Authentication**: Clerk (`@clerk/astro` v4 Core 2).
- **Payment Gateway**: Lynk.id (One-time payment model, without recurring subscription).
- **Asset Storage**: Cloudflare R2 (keys: `covers/storyX_cover.jpg`, `pages/storyX_page1.jpg`). Local development symlinks in `web/public/` connect directly to `preview/images/`.

### 💰 Business & Gating Model
- **Free Tier**: 3 free stories (`storyNumber <= 3`: #1 Barnaby Bear, #2 Selimut Bulan, #3 Tokoh Roti Kenari).
- **Paywall / Locked Tier**: Stories #4 to #40 are locked.
  - **Zero Leak Constraint**: When locked, the server **NEVER** sends page narratives, quotes, prompts, or page images to the client. DevTools/inspect element cannot unlock them.
- **Audio Functionality**: Deliberately disabled/hidden in the UI (`audio_enabled = false`) until full narration tracks are generated.
- **Package Tiers (Lynk.id)**:
  - `kecil`: Paket Kecil — 10 cerita pilihan (Rp 15.000, credit-based: 10 story picks)
  - `lengkap`: Paket Lengkap — 40 cerita saat ini (Rp 49.000, all-access 40 buku Batch 1)
  - `sahabat`: Paket Sahabat — semua cerita saat ini + update cerita baru tiap minggu selamanya (Rp 79.000, lifetime all-access)
  - Upgrades priced at difference: `kecil` → `lengkap` (Rp 34.000), `kecil` → `sahabat` (Rp 64.000), `lengkap` → `sahabat` (Rp 30.000).

### 📁 Web Directory Structure
```
web/
├── package.json
├── astro.config.mjs         # Astro + @clerk/astro + @astrojs/vercel
├── drizzle.config.ts        # Drizzle config targeting Neon
├── .env                     # Neon DB URL, Clerk keys, Lynk secrets, R2 config
├── .nvmrc                   # 22.23.4
├── drizzle/                 # 0000_init.sql migrations
├── scripts/
│   └── seed.mjs             # Idempotent seed script from preview/stories.json -> Neon
├── public/
│   ├── covers -> preview/images
│   └── pages  -> preview/images
└── src/
    ├── db/
    │   ├── client.ts        # Neon SQL + Drizzle instance
    │   ├── schema.ts        # stories, story_pages, products, users, purchases, entitlements, story_grants
    │   ├── entitlements.ts  # Access checks (free/granted/locked) & grantStory credit burner
    │   └── users.ts         # Lazy Clerk mirror to DB
    ├── layouts/
    │   └── Layout.astro     # Responsive header, auth state (UserButton/SignIn), status badge
    ├── lib/
    │   └── session.ts       # getViewer(Astro) memoised per-request resolver
    ├── middleware.ts        # Clerk middleware
    └── pages/
        ├── index.astro      # 36-book catalog, badge status, real artwork covers
        ├── sign-in.astro    # Clerk sign-in
        ├── sign-up.astro    # Clerk sign-up
        ├── akun.astro       # Paket Saya: user access, remaining credits, unlocked stories, pricing
        ├── baca/
        │   └── [id].astro   # 10-page bedtime reader (bilingual ID/EN, Aa font scaling, zero-leak lock screen)
        └── api/
            └── stories/
                └── claim.ts # POST endpoint to burn 1 credit to unlock a story
```

### ✅ Completed Milestones in `web/`
1. Neon Database setup, schema migrations, and idempotent seed of 36 stories + products.
2. Clerk authentication integration with lazy user synchronization into Neon.
3. Handshake token verification bug resolved (proper Node 22.23.4 restart & matching keys in instance `ins_3LBK8Wpn6M6p8LCbdWaQNpARYYa`).
4. Full bedtime reader ([`src/pages/baca/[id].astro`](file:///Users/bayu/local/storybooks/web/src/pages/baca/[id].astro)) with bilingual toggle, keyboard/paddle controls, progress bar, co-reading prompts, and finish celebration modal.
5. Server-side security gating preventing page payload leaks for locked stories.
6. Story credit burner API ([`src/pages/api/stories/claim.ts`](file:///Users/bayu/local/storybooks/web/src/pages/api/stories/claim.ts)).
7. Account & package viewer ([`src/pages/akun.astro`](file:///Users/bayu/local/storybooks/web/src/pages/akun.astro)).
8. Quick Story Navigation Drawer in reader ([`src/pages/baca/[id].astro`](file:///Users/bayu/local/storybooks/web/src/pages/baca/[id].astro)) with slide-in animation, floating left edge tab, live search filter, auto-scroll to active story, and entitlement badges.
9. Production build verified with `@astrojs/cloudflare` adapter.
10. **Git Repository Isolation**: Repositori Git diinisialisasi khusus di dalam `web/` (`web/.git`) dan di-push ke GitHub (`https://github.com/bayuwibisana/storybooks`).
11. **Cloudflare Workers Deployment (LIVE)**:
    - Domain live: **`https://storybooks.bayuwibisana15.workers.dev`** (HTTP/2 200 OK).
    - Native Cloudflare R2 bucket binding (`R2_BUCKET_BINDING` → `kisah-krayon`) di `wrangler.json`, memungkinkan streaming gambar cover, halaman, dan audio narasi berkecepatan tinggi tanpa hambatan kredensial S3.
    - Driver database dimigrasikan ke `drizzle-orm/neon-http` via `neon()` dengan Lazy Proxy resolution untuk mencegah crash isolasi WebSocket edge.
    - Resolusi runtime environment menggunakan `import { env } from "cloudflare:workers"` via helper `src/lib/env.ts`.
    - Custom diagnostics page `src/pages/500.astro` untuk menangkap error server dengan jelas.
12. **Reader Image Loading UX & Predictive Caching**:
    - Loader bertema krayon (`#image-loader` & `.crayon-spinner`) saat pergantian halaman jika gambar belum ter-cache di memori browser.
    - `preloadUpcomingPages(currentStep)` melakukan background prefetching untuk 2 halaman berikutnya secara bertahap (`new Image()`), membuat pembalikan halaman menjadi instan.
    - Proteksi race-condition sequence number (`imageLoadSeq`) saat orang tua / anak menekan tombol next/prev dengan cepat.
13. **Smart Auth Gating & Redirect Guard**:
    - Tombol katalog buku terkunci di `src/pages/index.astro` disesuaikan secara cerdas berdasarkan status autentikasi:
      - Belum login: "Masuk untuk Buka" (`/sign-in`).
      - Login & punya kredit (> 0): "Buka (1 Kredit)" (`/baca/[id]`).
      - Login & 0 kredit: "Pilih Paket Cerita" (`/akun`).
    - Banner selamat datang di katalog menyesuaikan kondisi kredit pengguna.
    - Guard redirect otomatis di `/sign-in` dan `/sign-up`: jika sudah login (`userId` aktif), langsung di-redirect kembali ke beranda `/`.
14. **Pricing Strategy & Tiers Restructure (CRO & Behavioral Economics)**:
    - Struktur paket resmi: Paket Kecil (Rp 15.000 / 10 cerita), Paket Lengkap (Rp 49.000 / 40 cerita Batch 1), Paket Sahabat (Rp 79.000 / Semua cerita + update cerita baru tiap minggu selamanya).
    - Efek Decoy diterapkan: selisih harga dari Paket Lengkap ke Paket Sahabat hanya Rp 30.000.
    - Matriks upgrade database Neon Postgres: `upgrade-kecil-lengkap` (Rp 34k), `upgrade-kecil-sahabat` (Rp 64k), `upgrade-lengkap-sahabat` (Rp 30k).
15. **Mobile Touch Swipe Gestures, Bedtime Dim Mode, & PWA / Social Share Meta**:
    - **Touch Swipe Gestures**: Membalik halaman di HP/tablet cukup diusap horizontal (`touchstart`/`touchend` sensitivitas $\ge 45\text{px}$).
    - **Mode Temaram Pengantar Tidur (🌙 Bedtime Dim Mode)**: Tombol bulan di navbar reader dengan palet hangat Dark Espresso (`#161412`), teks soft cream (`#e7e0d3`), filter kecerahan krayon malam hari, dan persistensi `localStorage`.
    - **Social Share & WhatsApp Rich Preview**: Tag OpenGraph & Twitter Card dinamis dengan thumbnail sampul cerita resolusi tinggi.
    - **PWA & Standalone App**: `public/manifest.json`, ikon krayon `public/favicon.svg`, dan Apple mobile web app mode.
16. **Smart Story URL Resolution & Human-Friendly Semantic Slugs (`src/lib/story-url.ts`)**:
    - Masalah `/baca/story-2` 404 teratasi tuntas.
    - Resolusi multi-format otomatis di `src/pages/baca/[id].astro`:
      - Format nomor: `/baca/2`, `/baca/story-2`, `/baca/cerita-2`.
      - Format judul semantik (SEO friendly): `/baca/gadis-yang-merajut-selimut-bulan`.
      - Format ID legacy: `/baca/selimut-bulan`, `/baca/story-006-emosi`.
    - Tautan di seluruh platform (`index.astro`, `perpustakaan.astro`, `akun.astro`, drawer navigasi) dimigrasikan ke URL semantik judul yang bersih tanpa kode internal dev (`story-006-emosi`).
17. **Mobile Responsive Reader Redesign & Horizontal Leak Fix**:
    - Mengatasi isu halaman terpotong/bergeser ke kiri di layar HP (iPhone 16 / 393px & Android / 360px).
    - **Top Bar 2-Tier Reflow**: Di layar mobile (`<= 768px`), tombol kontrol navigasi (`←`, `40 Cerita`) dan tools (`Audio`, `ID`, `Aa`, `🌙`) tetap berada di baris atas tanpa desak-desakan, sementara judul cerita (`#N · Judul`) ditata di baris bawah dengan pemisah lembut, menghilangkan overflow $520\text{px} \rightarrow 361\text{px}$.
    - **Eliminasi Tab Tumpang Tindih**: Tombol tab hijau mengambang (`.floating-edge-tab`) otomatis disembunyikan di HP (`display: none`), mencegah tab menutupi gambar sampul dan kartu cerita.
    - **Proteksi Horizontal Scroll Leak**: `html, body { overflow-x: hidden; max-width: 100%; }` dan `touch-action: pan-y` pada kanvas baca agar gesture swipe membalik halaman tidak menyebabkan viewport bergeser miring.
    - Skala tipografi responsif & padding ramah sentuhan (touch targets $\ge 40\text{px}$).
18. **Bedtime Sleep Timer, Preferences Persistence, Viral WhatsApp Share & SEO Engine**:
    - **Sleep Timer (15/30 Menit)**: Tombol timer `⏱️` di toolbar reader. Menghitung mundur waktu tidur anak, otomatis melakukan fade-out audio perlahan 2,5 detik, mematikan pembalik halaman otomatis, dan mengaktifkan mode redup temaram saat timer selesai.
    - **Persistensi Preferensi Membaca (`localStorage`)**: Pilihan bahasa (`ID/EN`) dan skala font (`Aa`) kini tersimpan permanen di `localStorage`, tidak lagi reset saat berpindah cerita atau reload.
    - **Eliminasi Janji Lembar Mewarnai Sementara**: Copywriting paket di `index.astro` dan `akun.astro` disesuaikan menjadi nilai murni: *"100% Bebas Iklan & Notifikasi (Lingkungan Aman Anak)"* demi menjaga integritas produk.
    - **Viral WhatsApp Share**: Tombol *"Bagikan ke WhatsApp"* di finish celebration modal dengan tautan kanonikal cerita dan pesan ramah keluarga.
    - **Dynamic Sitemap (`/sitemap.xml`) & robots.txt**: Endpoint SSR sitemap XML memuat semua 40 cerita terbit dengan tag `<image:image>`, `<lastmod>`, dan prioritas search engine.
    - **Structured Data (Schema.org JSON-LD)**: Schema markup `Book` lengkap dengan metadata usia pembaca (2–6 tahun) dan penerbit untuk rich results Google Search.
19. **Bedtime Dim Mode Visual & High-Contrast Typography Overhaul**:
    - **Perbaikan Kontras Ekstrem (Teks Hilang/Hitam)**: Mengatasi teks narasi cerita yang sebelumnya tidak terbaca karena syntax CSS terputus. Warna teks ditingkatkan menjadi *Crisp Warm Off-White* (`#f3eee6`, rasio kontras 14:1 terhadap latar `#221d1a`), judul menjadi *Warm Honey Gold* (`#fde68a`), dan pil karakter menjadi *Warm Amber Gold* (`#fbbf24`).
    - **Integrasi Tema Header Global**: Mode malam meresap hingga ke navbar situs utama (`rgba(22, 20, 18, 0.96)`) di `Layout.astro`, menciptakan pengalaman membaca malam yang konsisten dan nyaman di mata.
    - **Tata Letak 7 Tombol Mobile**: Menyesuaikan skala tombol toolbar reader pada layar HP agar tombol matahari/bulan (`☀️`/`🌙`) tidak terpotong di tepi kanan, dengan margin lega $\ge 70\text{px}$.
### 🚀 Engineering & Development Progress Roadmap

#### 🎯 Prioritas Utama Berikutnya (P0 — Immediate Focus / Revenue Engine)
1. **Lynk.id Webhook Handler (`web/src/pages/api/webhook/lynk.ts`)**:
   - Endpoint POST untuk menerima notifikasi pembayaran sukses dari Lynk.id.
   - Verifikasi otentikasi webhook (`LYNK_WEBHOOK_SECRET` / HMAC signature).
   - Pemrosesan idempoten: update status transaksi di tabel `purchases` menjadi `paid`.
   - Aktivasi otomatis:
     - Paket `sahabat` / `lengkap`: inject baris `entitlements (kind='all_access')` dan aktifkan `users.has_all_access = true`.
     - Paket `kecil`: inject baris `entitlements (kind='credit', credits=10)` dan tambahkan `users.story_credits`.
2. **Manual Checkout / WhatsApp Fallback CTA (`web/src/pages/akun.astro`)**:
   - Sediakan tombol alternatif: *"Konfirmasi Pembelian via WhatsApp / QRIS Manual"* pada kartu paket selama link checkout Lynk.id sedang dihubungkan.
   - Mencegah kehilangan calon pembeli (*zero drop-off*).
3. **Penyediaan Bonus Cetak: Lembar Mewarnai (Printables PDF)**:
   - Buat endpoint atau tombol unduh di reader / akun: *"Unduh Lembar Mewarnai Karakter Cerita (PDF)"* sebagai pemenuhan janji Paket Sahabat.

#### 🌙 Prioritas Fitur Membaca & Bedtime (P1 — Core Reader UX)
4. **Sleep Timer / Pengatur Waktu Tidur**:
   - Timer 15/30 menit yang otomatis meredupkan layar dan menghentikan audio secara perlahan (*fade-out*) saat anak sudah tertidur.
5. **Continuous Audio Auto-Play Mode**:
   - Begitu narasi audio di suatu halaman selesai, otomatis membalik halaman berikutnya dan melanjutkan narasi tanpa perlu disentuh.
6. **Service Worker Offline Cache (PWA Offline Reading)**:
   - Service worker ringan untuk menyimpan cerita yang sudah dibuka ke IndexedDB/Cache API, memungkinkan orang tua membaca cerita dalam mode pesawat (*airplane mode* bebas radiasi/gangguan notifikasi).

#### 📈 Prioritas Pertumbuhan & SEO (P2 — Growth & Viral Loop)
7. **Tombol "Bagikan Momen Tidur Nyenyak" di Finish Modal**:
   - Di modal akhir cerita, tambahkan direct share ke WhatsApp dengan pesan ramah keluarga.
8. **Sitemap Dinamis & Structured Data (`sitemap.xml` & JSON-LD)**:
   - Generator `sitemap.xml` untuk semua 40 cerita rilis.
   - Schema.org markup (`Book` & `Offer`) agar katalog terindeks kaya di Google Search dan LLM search engines.
9. **Security Headers Cloudflare (`public/_headers`)**:
   - `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`.
