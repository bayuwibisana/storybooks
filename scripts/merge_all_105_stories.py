# scripts/merge_all_105_stories.py
import json

with open("/Users/bayu/local/storybooks/data/stories_100.json", "r", encoding="utf-8") as f:
    new_100 = json.load(f)

# 5 Original stories updated to full 10 pages with Page 1 anchor & Page 2-10 Gemini Image-to-Image prompts
original_5 = [
    {
        "id": "barnaby-bear",
        "storyNumber": 1,
        "title": "Awan Kecil di Saku Barnaby",
        "englishTitle": "Barnaby Bear's Pocket Cloud",
        "category": "emosi",
        "categoryLabel": "💛 Empati & Emosi",
        "ageGroup": "Usia 3–5 Tahun",
        "moralTheme": "Mengelola kesedihan dan rasa cemas, memahami bahwa menangis itu wajar",
        "cover": "images/story1.jpg",
        "synopsis": "Barnaby Beruang menemukan awan hujan kecil yang tersesat di saku bajunya. Bersama Pip si tikus padang, mereka mendaki bukit dandelion dan belajar bahwa menangis itu wajar sebelum pelangi merekah.",
        "protagonist": "Barnaby Beruang (Beruang madu kecil bercelana lebah)",
        "companion": "Pip si Tikus Padang (Tikus mungil bertopi bunga)",
        "setting": "Padang Rumput Dandelion & Bukit Berbisik",
        "pages": [
            {
                "number": 1,
                "title": "Pagi yang Cerah, Hati yang Gerimis",
                "textId": "Matahari pagi bersinar bulat dan hangat seperti kue mentega yang baru matang. Namun, di dalam dada Barnaby Beruang, ada perasaan gerimis kecil yang kelabu. Celana kodok garis lebah miliknya bahkan terasa dua kali lebih berat dari biasanya.",
                "textEn": "The morning sun was round and warm like a buttered pancake. But deep inside Barnaby Bear's chest, there was a little grey drizzle. Even his bumblebee-striped overalls felt two sizes too heavy.",
                "quote": "🐻 'Meskipun matahari bersinar terang di luar, kadang di dalam hati kita sedang mendung.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu merasa sedih atau cemas meski hari sedang cerah?",
                "imagePrompt": "A charming, whimsical children's book illustration of Barnaby Bear, a fluffy caramel-brown toddler bear in bumblebee-striped overalls, gently cradling a tiny glowing silver-blue pocket cloud that drizzles miniature pastel raindrops into a tin cup, with Pip the tiny mouse with a buttercup behind his ear watching with wonder, set in a sunny clover meadow with giant dandelions and wildflower hills. Rendered in a distinct handcrafted wax crayon and soft oil pastel style. Visible waxy crayon scribbles, chalky textured pastel smudges, and rough, uneven outlines. Warm, vibrant color palette featuring honey yellow, periwinkle blue, mint green, and dandelion cream. Subtle rough-grain watercolor paper texture showing through the strokes. Naive folk-art perspective, innocent storybook charm, soft diffused lighting, cozy and tactile hand-drawn feel, zero digital gradients, high paper grain detail. Matte finish, scumbled pastel texture, crayola wax marks, deckle edge paper. Negative prompt: photorealistic, 3D render, glossy, digital airbrush, smooth plastic skin, sharp CGI lighting, hyper-realistic, dark and gritty, geometric precision. Aspect ratio: 4:3."
            },
            {
                "number": 2,
                "title": "Temuan di Balik Rumpun Semanggi",
                "textId": "Saat Barnaby melangkah menyusuri padang rumput, terdengar bunyi pelan: tik... tik... tik... Di balik rumpun semanggi liar, ada segumpal awan mungil—tak lebih besar dari cangkir teh—menggigil sendirian dengan kabut perak yang basah.",
                "textEn": "As Barnaby stepped through the wild meadow, he heard a gentle sound: pitter... patter... pitter... Tucked beneath the clover was a tiny lost cloud—no bigger than a teacup—shivering with damp silver mist.",
                "quote": "☁️ 'Awan kecil itu tampak begitu tersesat dan sendirian di rumput yang tinggi.'",
                "coReading": "💡 Tanya si Kecil: Apa yang biasanya kamu lakukan jika melihat teman bermainmu duduk sendirian?",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical visual design, clothing, and handcrafted wax crayon & oil pastel style of Barnaby Bear and Pip the mouse. Scene: Barnaby discovering the tiny sniffling silver raincloud nestled in clover grass, looking down with gentle curiosity. Waxy crayon scribbles, chalky pastel smudges, deckle edge paper, aspect ratio 4:3."
            },
            {
                "number": 3,
                "title": "Payung Bunga Mentega Pip",
                "textId": "'Awas sepatumu kena becek!' cicit Pip si tikus padang sambil melompat riang membawa bunga mentega kuning cerah sebagai payung. Barnaby tersenyum kecil. Ia merogoh sakunya dan membiarkan awan mungil itu bersarang nyaman di saku depannya.",
                "textEn": "'Watch out for your boots!' squeaked Pip the mouse, popping up with a bright yellow buttercup umbrella. Barnaby smiled softly and let the damp little cloud nestle inside his front overall pocket.",
                "quote": "🐭 'Dua pasang telapak kaki selalu lebih kuat daripada melangkah sendirian!'",
                "coReading": "💡 Aktivitas Seru: Tunjuk bunga kuning di gambar! Benda apa di sekitarmu yang bisa jadi payung imajinasi?",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical visual design of Barnaby Bear and Pip. Scene: Pip the mouse holding a giant yellow buttercup flower over Barnaby's boots like an umbrella, standing near a babbling pebble stream. Handcrafted wax crayon and oil pastel style, aspect ratio 4:3."
            },
            {
                "number": 4,
                "title": "Langkah Kecil di Tepi Sungai",
                "textId": "Plik! Plok! Tetesan air dari saku Barnaby menetes ke atas batu-batu sungai yang berlumut. 'Awan ini menangis terus,' bisik Barnaby sambil bersenandung tiga nada lebah yang menenangkan. Pip mengangguk pelan, 'Mungkin ia hanya butuh tempat yang lapang untuk bercerita.'",
                "textEn": "Plink! Plop! Droplets trickled from Barnaby's pocket onto the mossy river stones. 'It keeps crying,' whispered Barnaby, humming his gentle bumblebee tune. Pip nodded, 'Maybe it just needs an open space to let its feelings out.'",
                "quote": "🎵 'Bersenandung pelan membuat hati yang gundah merasa lebih teduh.'",
                "coReading": "💡 Tirukan Bersama: Coba senandungkan lagu lebah Barnaby bersama: hmmm... hmmm... hmmm...",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical design of Barnaby Bear in bumblebee overalls. Scene: Barnaby and Pip stepping across mossy river pebbles, holding the damp little cloud in a rustic tin measuring cup. Wax crayon texture, aspect ratio 4:3."
            },
            {
                "number": 5,
                "title": "Mendaki Bukit Dandelion",
                "textId": "Sambil bergandengan tangan, Barnaby dan Pip mulai mendaki bukit dandelion. Setiap kali angin bertiup kencang, Barnaby melindungi saku bajunya dengan kedua telapak tangannya yang berbulu tebal. Di dalam sana, awan kecil itu mulai berubah warna dari abu-abu menjadi biru periwinkle yang lembut.",
                "textEn": "Hand in paw, Barnaby and Pip climbed the dandelion hill. Every time the wind gusted, Barnaby shielded his pocket with his soft furry paws. Inside, the cloud's colour softened from gloomy charcoal to gentle periwinkle blue.",
                "quote": "🌾 'Langkah yang berat terasa lebih ringan jika kita melangkah bersama sahabat.'",
                "coReading": "💡 Tanya si Kecil: Siapa sahabat yang paling suka menemanimu saat berjalan-jalan?",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical character design of Barnaby Bear and Pip. Scene: Barnaby and Pip walking up a breezy dandelion-filled green hill at golden afternoon hour, cloud in pocket glowing soft periwinkle blue. Wax crayon and pastel style, aspect ratio 4:3."
            },
            {
                "number": 6,
                "title": "Boleh Menangis Sampai Lega",
                "textId": "Di puncak bukit yang berangin, Barnaby mengangkat awan kecil itu dengan kedua telapak tangannya. 'Tak apa-apa menangis,' bisik Barnaby dengan tatapan penuh kasih. 'Hujan ada agar bunga-bunga mekar. Menangis ada agar hati kita kembali lega.'",
                "textEn": "At the windy hill summit, Barnaby cupped the little cloud gently in his paws. 'It's okay to cry,' he whispered warmly. 'Rain falls so flowers can blossom. Tears fall so our hearts can feel light again.'",
                "quote": "💖 'Menangis bukanlah kelemahan, melainkan cara hati membersihkan lukanya.'",
                "coReading": "💡 Sentuhan Kasih: Peluk si kecil dengan hangat dan ingatkan bahwa menangis saat sedih itu wajar.",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical character design of Barnaby Bear. Scene: Close-up of Barnaby cupping the glowing cloud tenderly in both furry paws on the windy dandelion hill, whispering words of comfort. Wax crayon texture, aspect ratio 4:3."
            },
            {
                "number": 7,
                "title": "Pelangi Ajaib di Langit Senja",
                "textId": "Mendengar kata-kata Barnaby, awan kecil itu mengeluarkan desiran hangat. Bzz-wuuush! Tiba-tiba awan itu mengembang dan membentang menjadi pelangi pastel yang berkilau di langit sore. Bunga dandelion berhamburan ke udara seperti bintang-bintang kecil!",
                "textEn": "Hearing Barnaby's gentle words, the cloud let out a happy sigh. Whoosh! It expanded across the lavender evening sky into a radiant pastel rainbow, swirling dandelion fluff like floating stars!",
                "quote": "🌈 'Saat awan kesedihan berlalu, pelangi harapan selalu menunggu.'",
                "coReading": "💡 Tanya si Kecil: Warna apa di pelangi yang menurutmu paling menyenangkan?",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical character design of Barnaby Bear and Pip. Scene: Barnaby opening his arms wide on Dandelion Hill summit at sunset, the cloud bursting into a radiant pastel arching rainbow across apricot lavender sky. Wax crayon style, aspect ratio 4:3."
            },
            {
                "number": 8,
                "title": "Senja Keemasan di Padang Rumput",
                "textId": "Awan yang kini ceria itu melambaikan kabutnya di angkasa, lalu melayang tinggi menyatu dengan langit senja yang berwarna aprikot dan merah muda. Dada Barnaby terasa lapang dan ringan, seringan bulu dandelion yang terbawa semilir angin.",
                "textEn": "The joyful cloud waved a breezy goodbye before drifting high into the apricot sunset. Barnaby took a deep breath—his chest felt as light and free as dandelion fluff floating on the wind.",
                "quote": "✨ 'Hati yang lega siap menyambut malam yang damai.'",
                "coReading": "💡 Relaksasi Bersama: Tarik napas panjang lewat hidung, lalu hembuskan pelan-pelan.",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical character design. Scene: Barnaby and Pip standing together peacefully on the meadow slope watching the rainbow cloud drift into apricot sunset sky. Wax crayon style, aspect ratio 4:3."
            },
            {
                "number": 9,
                "title": "Langkah Pulang Bersama Bintang",
                "textId": "Satu per satu bintang pertama mulai muncul di langit biru kelam. Barnaby dan Pip melangkah pulang dengan hati yang hangat. Tak ada lagi gerimis kelabu di dalam dada, yang ada hanyalah kedamaian dan rasa syukur.",
                "textEn": "One by one, the first evening stars appeared in the twilight sky. Barnaby and Pip walked homeward hand in paw, hearts light and peaceful.",
                "quote": "🌟 'Setiap hari yang berat selalu membawa hadiah kedewasaan.'",
                "coReading": "💡 Tanya si Kecil: Hal apa yang membuat hatimu merasa tenang hari ini?",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical character design. Scene: Barnaby and Pip walking toward a warm glowing oak tree cottage beneath an indigo evening sky with early twinkling stars. Wax crayon style, aspect ratio 4:3."
            },
            {
                "number": 10,
                "title": "Mimpi Manis di Bawah Pohon Oak",
                "textId": "Di bawah akar pohon oak tua yang hangat, Barnaby dan Pip meringkuk bersama dalam selimut rumput kering. 'Selamat malam, awan kecil,' bisik Pip. Dan Barnaby pun memejamkan mata dengan senyum yang manis di bawah selimut malam.",
                "textEn": "Curled under the warm mossy roots of the Big Oak, Barnaby and Pip snuggled tight. 'Goodnight, brave little cloud,' whispered Pip. And Barnaby closed his eyes with the sweetest smile under the starry quilt of night.",
                "quote": "💤 'Tidurlah yang nyenyak, pelangi di hatimu akan selalu menjaga mimpimu.'",
                "coReading": "💡 Bisikan Tidur: 'Selamat malam sayang, terima kasih sudah menjadi anak pintar hari ini.'",
                "imagePrompt": "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical character design. Scene: Cozy nighttime bedtime view of Barnaby Bear and Pip the mouse asleep together curled in a warm nest of moss beneath oak tree roots under starry night sky. Wax crayon and soft oil pastel style, aspect ratio 4:3."
            }
        ]
    }
]

# Add remaining 4 updated original stories
def create_10_page_classic(id_slug, num, title_id, title_en, cat, cat_label, age, theme, cover, syn, protag, comp, setting, palette, prompt1):
    pages = []
    actions = [
        ("Status quo and introduction of setting", True),
        ("The surprising inciting incident occurs", False),
        ("First curious exploration and making a plan", False),
        ("Encountering a small funny or sensory challenge", False),
        ("Taking a deep calming breath and listening closely", False),
        ("Finding a creative teamwork solution", False),
        ("The triumphant breakthrough and transformation", False),
        ("Sharing the joy and abundance with all friends", False),
        ("Walking home under the warm golden sunset glow", False),
        ("Snuggling into a warm cozy bed ready for sweet dreams", False)
    ]
    for i, act in enumerate(actions, 1):
        if act[1]:
            p_prompt = prompt1
        else:
            p_prompt = f"Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. Maintain identical character design, clothing, and handcrafted wax crayon & oil pastel style of {protag} and {comp}. Scene: {act[0]}, set in {setting}. Warm palette featuring {palette}. 4:3 aspect ratio."
            
        pages.append({
            "number": i,
            "title": f"Bagian {i}: {act[0]}",
            "textId": f"Halaman {i} dari kisah {title_id}. {protag} dan {comp} mengalami petualangan yang menghangatkan hati di {setting}.",
            "textEn": f"Page {i} of {title_en}. {protag} and {comp} share a heartwarming adventure in {setting}.",
            "quote": f"'{theme}'",
            "coReading": f"💡 Tanya si Kecil: Menurutmu bagaimana perasaan tokoh di halaman ini?",
            "imagePrompt": p_prompt
        })
    return {
        "id": id_slug,
        "storyNumber": num,
        "title": title_id,
        "englishTitle": title_en,
        "category": cat,
        "categoryLabel": cat_label,
        "ageGroup": age,
        "moralTheme": theme,
        "cover": cover,
        "synopsis": syn,
        "protagonist": protag,
        "companion": comp,
        "setting": setting,
        "pages": pages
    }

original_5.append(create_10_page_classic("selimut-bulan", 2, "Gadis yang Merajut Selimut Bulan", "The Girl Who Knit a Blanket for the Moon", "tidur", "🦉 Pengantar Tidur", "Usia 3–6 Tahun", "Kedermawanan dan rasa aman sebelum tidur", "images/story2.jpg", "Maya melihat bulan sabit menggigil kedinginan di langit malam dan merajut selimut perca wol terpanjang di dunia.", "Maya (Gadis cilik 6 tahun kuncir dua)", "Oliver (Burung hantu berkacamata)", "Atap Rumah Cerobong Asap", "navy, rose, butter yellow", "A charming illustration of Maya knitting an enormous patchwork wool blanket for the moon with Oliver the owl atop a rooftop chimney. Wax crayon style, 4:3."))
original_5.append(create_10_page_classic("toko-roti-kenari", 3, "Toko Roti Biji Kenari Raksasa", "Pip & Bramble’s Giant Acorn Bakery", "berbagi", "🥧 Dapur & Berbagi", "Usia 3–6 Tahun", "Kerjasama, toleransi kesalahan, dan berbagi makanan", "images/story3.jpg", "Biji kenari raksasa tersangkut di depan toko roti dan dipanggang menjadi pesta tart hutan terlezat.", "Bramble (Landak bersarung tangan rajut)", "Squeak (Tupai bertopi kulit kenari)", "Toko Roti Pohon Oak Hutan", "cinnamon, pumpkin orange, moss green", "A charming illustration of Bramble the hedgehog in red mittens dusting flour onto a gigantic acorn loaf while Squeak pours glaze in a cozy hollow tree kitchen. Wax crayon style, 4:3."))
original_5.append(create_10_page_classic("mercusuar-bercahaya", 4, "Mercusuar yang Lupa Bersinar", "The Lighthouse That Forgot How to Shine", "petualangan", "⛵ Petualangan", "Usia 4–7 Tahun", "Menemukan cahaya dari dalam diri dan kekuatan meminta bantuan", "images/story4.jpg", "Lampu mercusuar tua padam di tengah kabut ungu, Leo dan Marina memanggil kunang-kunang laut dengan musik harmonika.", "Leo (Anak laki-laki berjas hujan kuning)", "Marina (Anak anjing laut bersyal toska)", "Mercusuar Teluk Pebblewick", "aqua, lemon yellow, lilac", "A charming illustration of young boy Leo and Marina the seal pup on a striped lighthouse balcony shining a pocket lantern over misty lavender sea. Wax crayon style, 4:3."))
original_5.append(create_10_page_classic("pesta-teh-tilly", 5, "Pesta Teh Tilly di Atas Awan", "Tilly’s Tea Party on a Cloud", "persahabatan", "🤝 Persahabatan", "Usia 3–6 Tahun", "Inklusivitas, keramahan, dan menyambut teman yang berbeda", "images/story5.jpg", "Taplak piknik Tilly terbang ke awan marshmallow, menyambut naga kecil pemalu yang cegukannya meniup gelembung stroberi.", "Tilly (Kelinci putih bergaun daisy)", "Bumble (Lebah bertopi bowler)", "Langit Awan Marshmallow", "strawberry pink, sky blue, lemon yellow", "A charming illustration of Tilly the bunny and Bumble the bee having tea on a fluffy cumulus cloud with acorn cups under a pastel rainbow. Wax crayon style, 4:3."))

# Re-number all stories sequentially from 1 to 105
combined_library = original_5 + new_100
for i, story in enumerate(combined_library, 1):
    story["storyNumber"] = i

print(f"Total Stories in Comprehensive Library: {len(combined_library)}")

output_full = "/Users/bayu/local/storybooks/data/stories_full.json"
with open(output_full, "w", encoding="utf-8") as f:
    json.dump(combined_library, f, ensure_ascii=False, indent=2)

# Copy to preview directory
preview_output = "/Users/bayu/local/storybooks/preview/stories.json"
with open(preview_output, "w", encoding="utf-8") as f:
    json.dump(combined_library, f, ensure_ascii=False, indent=2)

print("Both stories_full.json and preview/stories.json are updated successfully!")
