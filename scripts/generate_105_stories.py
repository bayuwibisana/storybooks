# scripts/generate_105_stories.py
import json
import os

MASTER_STYLE = "Rendered in a distinct handcrafted wax crayon and soft oil pastel style. Visible waxy crayon scribbles, chalky textured pastel smudges, and rough, uneven outlines. Subtle rough-grain watercolor paper texture showing through the strokes. Naive folk-art perspective, innocent storybook charm, soft diffused lighting, cozy and tactile hand-drawn feel, zero digital gradients, high paper grain detail. Matte finish, scumbled pastel texture, crayola wax marks, deckle edge paper. Negative prompt: photorealistic, 3D render, glossy, digital airbrush, smooth plastic skin, sharp CGI lighting, hyper-realistic, dark and gritty, geometric precision. Aspect ratio: 4:3."

CATEGORIES = [
    ("emosi", "💛 Empati & Regulasi Emosi", "Pengelolaan rasa marah, takut, cemas, dan belajar menenangkan diri"),
    ("tidur", "🦉 Pengantar Tidur & Ketenangan", "Dongeng rileks sebelum tidur, malam berbintang, dan rasa aman"),
    ("logika", "🧩 Logika & Pemecahan Masalah", "Sebab-akibat, observasi sains alam, timbangan, dan teka-teki cerdas"),
    ("petualangan", "⛵ Petualangan & Keberanian", "Mencoba hal baru, menjelajahi lingkungan, dan mengatasi rasa ragu"),
    ("berbagi", "🥧 Berbagi & Kerjasama Dapur", "Kedermawanan, memasak bersama, antre, dan merayakan keberlimpahan"),
    ("persahabatan", "🤝 Persahabatan & Inklusivitas", "Menerima perbedaan, mendengarkan teman, dan merangkul keunikan"),
    ("alam", "🌿 Cinta Alam & Lingkungan", "Merawat tanaman, membersihkan sungai, sahabat satwa, dan pergantian musim"),
    ("kreativitas", "🎨 Kreativitas & Imajinasi", "Membuat mainan sendiri, melihat dari sudut baru, dan musik alam"),
    ("ketekunan", "🐢 Ketekunan & Proses", "Belajar langkah demi langkah, menghargai kesalahan, dan kesabaran"),
    ("keluarga", "🏡 Keluarga & Rumah Hangat", "Kasih kakek-nenek, rukun saudara, makan malam bersama, dan syukur")
]

# We will generate rich, distinct concepts
def make_page(num, title, text_id, text_en, quote, prompt_action, protag_desc, comp_desc, setting_desc, palette, is_anchor=False):
    if is_anchor:
        img_prompt = f"A charming, whimsical children's book illustration of {prompt_action}, featuring {protag_desc} and {comp_desc}, set in {setting_desc}. Warm, vibrant color palette featuring {palette}. {MASTER_STYLE}"
    else:
        img_prompt = f"Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain the identical visual design, clothing, and handcrafted wax crayon & oil pastel style of {protag_desc} and {comp_desc}. Scene: {prompt_action}, set in {setting_desc}. Color mood: {palette}. Visible waxy crayon scribbles, chalky pastel smudges, and rough-grain paper texture. Zero digital gradients, 4:3 aspect ratio."
    
    return {
        "number": num,
        "title": title,
        "textId": text_id,
        "textEn": text_en,
        "quote": quote,
        "coReading": f"💡 Tanya si Kecil: Menurutmu bagaimana perasaan tokoh di halaman ini? Pernahkah kamu mengalaminya?",
        "imagePrompt": img_prompt
    }

print("Template generator initialized")
