# scripts/build_batch_38_to_47.py
import json
import os

from polish_stories_38_to_47 import get_stories_38_to_47 as get_stories_38_to_39

def get_stories_40_to_43():
    stories = []

    # =========================================================================
    # STORY 40: Jejak Kaki Rahasia di Pasir
    # =========================================================================
    s40 = {
        "id": "jejak-kaki-pasir",
        "storyNumber": 40,
        "title": "Jejak Kaki Rahasia di Pasir",
        "englishTitle": "Secret Footprints in the Sand",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 4–7 Tahun",
        "moralTheme": "Petualangan mengamati alam, rasa ingin tahu, dan ketenangan pesisir senja",
        "cover": "images/story40_cover.jpg",
        "coverImage": "images/story40_cover.jpg",
        "synopsis": "Di tepi pantai berpasir putih, Lani menemukan pola jejak-jejak misterius yang tercetak sebelum ombak datang. Bersama Koko si kepiting kecil bercangkang oranye, Lani mengikuti jejak-jejak itu dan belajar membaca rahasia satwa pesisir.",
        "synopsisEn": "Along the white sand shoreline, Lani discovers mysterious little tracks pressed before the tide rolls in. Together with Koko the little orange fiddler crab, Lani follows the clues and uncovers the gentle secrets of seashore creatures.",
        "protagonist": "Lani (Gadis pesisir 5 tahun berkepang dua dengan topi jerami pita biru)",
        "companion": "Koko (Kepiting kecil bercangkang oranye dengan capit ramah)",
        "setting": "Garis Pantai Pasir Putih Berombak Tenang",
        "pages": [
            {
                "number": 1,
                "title": "Kanvas Pasir yang Masih Basah",
                "titleEn": "The Damp Sand Canvas",
                "textId": "Air laut surut perlahan meninggalkan hamparan pasir putih yang halus dan basah seperti adonan tepung kue. Lani menenteng ember kecilnya sambil merasakan buih ombak yang menggelitik jari-jari kakinya yang mungil.",
                "textEn": "The tide receded softly, leaving behind an expanse of smooth white sand as fine as pastry dough. Lani carried her little pail, feeling the bubbly seafoam tickle her bare toes with gentle coolness.",
                "quote": "🌊 'Pantai di sore hari adalah kanvas raksasa yang selalu siap dilukis kembali.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu merasakan pasir pantai yang basah di sela-sela jarimu?",
                "imagePrompt": "Charming children's book illustration of little coastal girl Lani in a yellow sundress and straw sunhat holding a tin bucket, walking along a wet white sand shoreline at low tide. Seafoam laps at her feet. Handcrafted wax crayon and oil pastel, textured cream watercolor paper, naive folk-art style, simple bead eyes, 4:3 landscape, completely text-free."
            },
            {
                "number": 2,
                "title": "Titik-Titik Renda Koko",
                "titleEn": "Koko's Little Lace Dots",
                "textId": "Klip-klap! Dari balik cangkang kerang belang, Koko si kepiting kecil muncul dengan capit oranyenya yang lucu. Di sekeliling lubang pasirnya, ada deretan butiran pasir bulat kecil yang tertata rapi seperti renda gaun.",
                "textEn": "Click-clack! From behind a striped seashell, Koko the little orange crab popped out, waving a friendly claw. Circling his little sand burrow were tiny, perfect sand pearls arranged like dainty lace embroidery.",
                "quote": "🦀 'Setiap makhluk kecil di pantai memiliki cara unik untuk menyapa dunia.'",
                "coReading": "💡 Aktivitas Seru: Gerakkan jari-jarimu seperti capit kepiting kecil: Klip-klap-klip-klap!",
                "imagePrompt": "A whimsical children's picture book illustration of Koko the tiny friendly orange crab with big expressive black bead eyes, standing beside a small sand burrow surrounded by neat decorative sand pellets. Lani kneels down smiling. Crayon scribbles, textured paper, warm golden sunlight, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Jejak Bintang Bercabang Tiga",
                "titleEn": "Three-Pronged Star Prints",
                "textId": "\"Lihat ini, Koko!\" seru Lani sambil menunjuk ke arah gundukan karang. Di atas pasir basah, ada pola jejak berbentuk panah bercabang tiga: V-V-V. Jejak itu melangkah lincah menuju genangan air asin.",
                "textEn": "\"Look at this, Koko!\" gasped Lani, pointing toward a mound of coral rock. Upon the damp sand was a trail of three-pronged arrow prints: V-V-V. The tracks trotted briskly toward a shallow saltwater pool.",
                "quote": "🔍 'Mencari jejak membuat kita belajar mengamati detail-detail yang tersembunyi.'",
                "coReading": "💡 Tanya si Kecil: Kira-kira hewan apa yang memiliki kaki bercabang tiga seperti itu?",
                "imagePrompt": "Close-up storybook illustration of small bird footprints shaped like three-pronged stars pressed into damp glistening shoreline sand. Lani and little crab Koko bend low to inspect them with magnifying curiosity. Wax crayon and chalky oil pastel, 4:3 landscape, completely text-free."
            },
            {
                "number": 4,
                "title": "Burung Camar Penari Pesisir",
                "titleEn": "The Coastal Dancer Gull",
                "textId": "Di ujung jejak itu, seekor burung camar kecil berbulu abu-abu mutiara sedang berdiri dengan satu kaki, mengeringkan sayapnya di bawah semilir angin. Lani melangkah berjingkat agar tidak mengejutkan kawan barunya itu.",
                "textEn": "At the trail's end, a petite pearl-gray seagull stood peacefully upon one leg, drying its soft feathers in the evening breeze. Lani tiptoed softly so as not to startle her new feathered friend.",
                "quote": "🕊️ 'Langkah yang pelan dan lembut adalah tanda hormat kita kepada sahabat alam.'",
                "coReading": "💡 Aktivitas Seru: Coba tirukan berjalan berjingkat-jingkat tanpa mengeluarkan suara sama sekali!",
                "imagePrompt": "Tender storybook illustration of Lani tiptoeing with her hands behind her back, watching a fluffy little gray seagull perched on a driftwood log by the water's edge. Warm sunset light, soft oil pastel blending on cream watercolor paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Garis Belit Berkelok Rahasia",
                "titleEn": "The Secret Winding Ribbon",
                "textId": "Tiba-tiba Koko mengetukkan capitnya ke pasir. Ada jejak lain lagi! Bukan jejak kaki, melainkan garis berliku-liku halus seperti pita sutra yang ditarik pelan di atas pasir. \"Jejak siapa ini?\" gumam Lani heran.",
                "textEn": "Suddenly Koko tapped his claw upon the sand. Another track! It wasn't footprints, but a smooth winding groove like a silk ribbon drawn gently across the dunes. \"Whose secret trail could this be?\" wondered Lani.",
                "quote": "🐚 'Tidak semua pengelana berjalan dengan kaki; sebagian meluncur dengan sabar.'",
                "coReading": "💡 Tanya si Kecil: Hewan apa yang berjalan lambat dan membawa rumahnya ke mana-mana?",
                "imagePrompt": "Charming illustration of a smooth winding trail in the sand leading to a beautiful spiraled hermit crab shell. Lani and crab Koko follow the curvy line with wonder. Handcrafted wax crayon, textured sand tones, naive perspective, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Kelomang Bertopi Kerang Spiral",
                "titleEn": "The Hermit Crab in a Spiral Shell",
                "textId": "Garis pita itu berhenti di samping batu karang berlumut. Di sana, seekor kelomang mungil dengan cangkang spiral berwarna jingga sedang mengintip malu-malu dengan sungut kecilnya yang bergoyang ramah.",
                "textEn": "The ribbon groove ended beside a mossy tide-pool stone. There, a tiny hermit crab tucked inside a spiral orange shell peeked out bashfully, wiggling its little antennae in friendly greeting.",
                "quote": "🏠 'Rumah yang paling nyaman adalah rumah yang selalu kita bawa dengan rasa damai.'",
                "coReading": "💡 Tanya si Kecil: Mengapa kelomang suka berpindah cangkang saat tubuhnya semakin besar?",
                "imagePrompt": "Adorable children's book illustration of a shy little hermit crab peeking out of an ornate orange-striped seashell on the wet sand. Koko waves his claw happily at his fellow crustacean cousin. Warm crayon marks, folk art charm, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Jejak Kaki Lani Sendiri",
                "titleEn": "Lani's Very Own Footprints",
                "textId": "Lani menoleh ke belakang. Di sepanjang pantai putih yang telah mereka lewati, terbentang jejak telapak kaki kecil Lani yang berdampingan dengan jejak capit Koko. Dua jejak berbeda yang berjalan bersama dengan rukun.",
                "textEn": "Lani looked back over her shoulder. Stretching all along the white strand was a trail of her own little barefoot prints, walking side-by-side with Koko's tiny crab dots. Two different tracks wandering together in harmony.",
                "quote": "👣 'Jejak persahabatan selalu meninggalkan kenangan indah yang menghangatkan hati.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat jejak kakimu sendiri di pasir atau tanah basah?",
                "imagePrompt": "Picturesque children's book scene looking down a peaceful beach where a child's footprints and a tiny crab's claw-tracks travel side by side along the edge of glistening water. Golden amber and lavender twilight, waxy crayon scribbles, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Sapu Lembut Ombak Senja",
                "titleEn": "The Gentle Sweep of the Dusk Tide",
                "textId": "Syuuush... Ombak senja yang tenang bergulung lembut ke tepian, membasuh semua jejak kaki camar, kelomang, dan jejak Lani. Pasir pantai kembali bersih dan rata, bersiap menyambut tidur malamnya.",
                "textEn": "Whooosh... The quiet evening tide rolled softly ashore, gently smoothing away the footprints of the gull, the hermit crab, and little Lani. The sandy shore returned to pristine calm, ready for night's rest.",
                "quote": "🌊 'Ombak laut selalu mengajarkan kita untuk melepaskan hari yang telah usai dengan damai.'",
                "coReading": "💡 Dengarkan Bersama: Tirukan suara ombak laut yang lembut dan berirama: 'Syuuuush... syuuuush...'",
                "imagePrompt": "Serene storybook illustration of a gentle foamy wave softly washing over footprints in the sand, smoothing the shore into a gleaming mirror of sunset colors. Crayon and pastel blending on textured watercolor paper, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Salam Perpisahan untuk Koko",
                "titleEn": "A Fond Farewell to Koko",
                "textId": "Matahari bulat merah saga perlahan tenggelam di cakrawala laut. Koko melambaikan capitnya sebelum masuk kembali ke liang pasirnya yang hangat. \"Sampai jumpa besok, Koko,\" bisik Lani sambil melambaikan tangan.",
                "textEn": "The great ruby-red sun dipped slowly beneath the ocean horizon. Koko waved his little claw once more before tucking back into his snug sand burrow. \"See you tomorrow, dear Koko,\" whispered Lani with a gentle wave.",
                "quote": "🌅 'Setiap hari yang indah ditutup dengan lambaian hangat kepada para sahabat.'",
                "coReading": "💡 Tanya si Kecil: Kepada siapa saja kamu mengucapkan selamat tidur setiap malam?",
                "imagePrompt": "Warm, peaceful illustration of Lani waving goodbye to little crab Koko at the mouth of his burrow. The sunset sky blazes with soft pink, tangerine, and lilac strokes. Handcrafted wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur di Iringi Deburan Ombak",
                "titleEn": "Sleeping to the Lullaby of the Sea",
                "textId": "Di pondok kayu tepi pantai, jendela kamar Lani terbuka sedikit, membiarkan angin laut sejuk dan desau ombak yang tenang menjadi lagu pengantar tidurnya. Lani memejamkan mata di balik selimut putihnya, tidur lelap dengan hati yang damai. Selamat tidur, Lani.",
                "textEn": "In the cozy seaside wooden cottage, Lani's bedroom window stood slightly ajar, letting the cool sea breeze and rhythmic ocean murmurs become her bedtime lullaby. Lani closed her eyes under her crisp white quilt, fast asleep with a peaceful heart. Goodnight, sweet Lani.",
                "quote": "🌙 'Biarkan desau ombak yang tenang membawamu ke pulau mimpi yang paling indah.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak manis, biarkan malam membawakanmu mimpi seindah lautan luas.",
                "imagePrompt": "A cozy, tranquil bedtime illustration of little girl Lani sleeping soundly in her bed inside a coastal wooden room. A small seashell nightlight glows warm amber on the bedside table. Moonbeams illuminate the curtains and waves outside, wax crayon on heavy cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s40)

    # =========================================================================
    # STORY 41: Membuka Mata di Air Kolam
    # =========================================================================
    s41 = {
        "id": "membuka-mata-di-air",
        "storyNumber": 41,
        "title": "Membuka Mata di Air Kolam",
        "englishTitle": "Opening Eyes in Clear Water",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 4–7 Tahun",
        "moralTheme": "Mengatasi rasa takut air saat belajar berenang dan menemukan keindahan bawah air",
        "cover": "images/story41_cover.jpg",
        "coverImage": "images/story41_cover.jpg",
        "synopsis": "Bayu selalu memejamkan matanya rapat-rapat saat mencelupkan wajah ke kolam sumber alami. Bersama Ikan Mas bersirip sutra yang ramah, Bayu mengumpulkan keberanian untuk membuka kacamata renangnya dan melihat dunia bawah air yang jernih berkilau keemasan.",
        "synopsisEn": "Little Bayu always squeezes his eyes tight whenever he dips his face into the natural spring pool. With the help of a friendly silk-finned Goldfish, Bayu finds the courage to open his swim goggles underwater and marvels at a shimmering sunlit world.",
        "protagonist": "Bayu (Anak laki-laki 5 tahun berpelampung bebek kuning dan kacamata renang biru)",
        "companion": "Ikan Mas (Ikan mas gemuk bersirip sutra keemasan yang berenang anggun)",
        "setting": "Kolam Air Sumber Alami Berbatu Lumut di Kaki Gunung",
        "pages": [
            {
                "number": 1,
                "title": "Kecipak Kaki di Tepian Kolam",
                "titleEn": "Kicking Feet by the Pool's Edge",
                "textId": "Air di kolam mata air alami itu begitu jernih hingga batu-batu kerikil putih di dasarnya terlihat jelas. Bayu duduk di undakan batu berlumut, mengenakan pelampung bebek kuning kesayangannya sambil mengepakkan kakinya: kecipak-kecipuk!",
                "textEn": "The water in the natural mountain spring pool was so crystal clear that smooth white pebbles on the floor were plainly visible. Bayu sat upon the mossy stone steps, wearing his favorite yellow duck floatie and kicking his little legs: splash-splash-splash!",
                "quote": "💦 'Merasakan sejuknya air adalah langkah awal untuk bersahabat dengannya.'",
                "coReading": "💡 Tanya si Kecil: Apakah kamu suka bermain cipratan air saat mandi sore?",
                "imagePrompt": "Charming children's book illustration of toddler boy Bayu wearing a yellow duck inflatable ring and blue swim goggles, sitting on mossy stone steps of a clear natural pool, splashing water with his bare feet. Lush green ferns and mountain forest surrounding. Handcrafted wax crayon, soft pastel smudges, 4:3 landscape, completely text-free."
            },
            {
                "number": 2,
                "title": "Rasa Takut yang Menahan Napas",
                "titleEn": "The Fear That Holds the Breath",
                "textId": "Namun setiap kali harus mencelupkan wajahnya ke dalam air, dada Bayu berdegup kencang. Ia takut air masuk ke dalam hidungnya, dan ia takut kegelapan saat memejamkan mata di dalam air.",
                "textEn": "Yet whenever it came time to dip his face into the water, Bayu's heart thumped rapidly. He was afraid water might rush into his nose, and he feared the dark void when squeezing his eyes tightly shut underwater.",
                "quote": "😟 'Ketakutan akan air adalah hal yang wajar dialami setiap anak yang sedang belajar.'",
                "coReading": "💡 Tanya si Kecil: Apa yang biasanya kamu lakukan jika air membasahi matamu saat keramas?",
                "imagePrompt": "A gentle picture book scene of boy Bayu hesitating with his face hovering just above the sparkling water surface, hands holding tight to his duck floatie. Soft water reflections dance on his face. Wax crayon texture, innocent folk-art expression, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Gelembung Napas Seperti Ikan",
                "titleEn": "Bubble Breaths Like a Little Fish",
                "textId": "Plop! Seekor ikan mas gemuk bersirip sutra meluncur anggun ke dekat kaki Bayu. Ikan itu membuka mulutnya pelan: blub... blub... blub... mengeluarkan rantai gelembung udara berkilau yang menari ke permukaan.",
                "textEn": "Plop! A plump, silky-finned goldfish glided gracefully near Bayu's toes. The fish opened its round mouth softly: blub... blub... blub... sending up a chain of shimmering air bubbles that danced to the surface.",
                "quote": "🐠 'Ikan kecil mengajari kita cara bernapas gelembung dengan tenang dan gembira.'",
                "coReading": "💡 Aktivitas Seru: Tiup napasmu pelan-pelan seperti membuat gelembung sabun: 'Blluuub... bllluub...'",
                "imagePrompt": "Whimsical children's book illustration of a friendly golden carp with flowing translucent fins swimming up to Bayu, releasing floating crystalline air bubbles. The water is shaded in luminous turquoise and jade crayon strokes. 4:3 landscape, completely text-free."
            },
            {
                "number": 4,
                "title": "Menempelkan Kacamata Renang",
                "titleEn": "Fitting the Blue Goggles",
                "textId": "Bayu membetulkan tali kacamata renang birunya. Karetnya pas dan lembut di sekeliling matanya. \"Kacamata ini adalah jendela ajaibmu, Bayu,\" kata Ayah dengan senyum menenangkan dari tepi kolam.",
                "textEn": "Bayu adjusted the strap of his blue swim goggles. The soft silicone sealed snugly around his eyes. \"These goggles are your magical picture window, Bayu,\" encouraged Papa with a reassuring smile from the pool's edge.",
                "quote": "🥽 'Perlengkapan yang tepat memberi kita rasa aman untuk memulai petualangan baru.'",
                "coReading": "💡 Tanya si Kecil: Benda apa yang paling membantumu saat belajar berenang?",
                "imagePrompt": "Storybook illustration of boy Bayu adjusting his blue swim goggles with determination, smiling at his father whose gentle hands give him support in the clear shallow pool. Warm sunlight filtering through forest canopy, wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Celupan Wajah Pertama",
                "titleEn": "The Very First Face Dip",
                "textId": "Tarik napas panjang... tahan... lalu celup! Wajah Bayu masuk ke bawah permukaan air. Ia meniup gelembung dari bibirnya: blub-blub-blub! Telinganya kini hanya mendengar desau air yang sunyi dan menyejukkan.",
                "textEn": "Take a deep breath... hold it gentle... and dip! Bayu lowered his face beneath the water's surface. He blew tiny bubbles from his lips: blub-blub-blub! His ears now heard only the peaceful, muffled hush of the cool mountain pool.",
                "quote": "🫧 'Di bawah air, dunia berubah menjadi tempat yang tenang dan penuh keheningan damai.'",
                "coReading": "💡 Latihan Bersama: Coba tahan napas selama 3 detik bersama-sama: Satu... dua... tiga... hembuskan!",
                "imagePrompt": "Delightful underwater-split-view children's illustration showing Bayu's face submerged in sparkling clear water, blowing streams of round bubbles from his mouth. Yellow duck floatie rests on the surface above. Turquoise and golden crayon blending, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Mata yang Terbuka di Bawah Air",
                "titleEn": "Eyes Opening Wide Underwater",
                "textId": "Ikan Mas berenang perlahan tepat di depan kacamatanya. Perlahan, Bayu memberanikan diri membuka kedua matanya di balik lensa. KLIK! Dunia bawah air seketika menjadi terang benderang!",
                "textEn": "The Goldfish drifted slowly right before his goggles. Very gently, Bayu gathered all his courage and opened both eyes wide behind the lenses. CLICK! The underwater realm instantly burst into radiant clarity!",
                "quote": "✨ 'Saat kita berani membuka mata, ketakutan kita menghilang berganti takjub.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat benda di dalam air yang tampak berkilau seperti harta karun?",
                "imagePrompt": "Magical underwater storybook scene of Bayu looking through his goggles with wide, astonished black bead eyes. Right before him swims the shimmering golden fish, surrounded by sunbeams cutting through clear turquoise water. Handcrafted wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Hutan Lumut dan Sinar Emas",
                "titleEn": "Mossy Forest and Golden Sunbeams",
                "textId": "Batu-batu kali di dasar kolam ternyata tampak seperti gunung-gunung kecil yang diselimuti karpet lumut zamrud. Sinar matahari senja menembus air seperti pilar-pilar emas krayon yang megah. Indah sekali!",
                "textEn": "The river stones on the pool floor resembled miniature mountains carpeted in emerald moss. Rays of late afternoon sun pierced the water like grand pillars of golden crayon light. It was breathtakingly beautiful!",
                "quote": "🌿 'Ada keajaiban tersembunyi yang hanya bisa dilihat oleh mereka yang berani menatapnya.'",
                "coReading": "💡 Tanya si Kecil: Warna apa saja yang bisa kamu lihat di dasar air yang jernih?",
                "imagePrompt": "Lush and tranquil underwater illustration showing mossy river rocks, waving water lilies, and dancing golden light rays playing on smooth white river pebbles. Soft chalky pastel and wax crayon marks on textured paper, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Muncul ke Permukaan dengan Tawa",
                "titleEn": "Surfacing with Pure Joy",
                "textId": "HUP! Bayu mengangkat kepalanya ke atas permukaan air, menyeka tetesan air di keningnya sambil tertawa riang. \"Ayah, aku melihat istana Ikan Mas di dasar kolam! Airnya sama sekali tidak menakutkan!\"",
                "textEn": "HUP! Bayu popped his head back up above the water, wiping away the cool droplets with a ringing laugh of joy. \"Papa, I saw the Goldfish's palace at the bottom! The water isn't scary at all!\"",
                "quote": "😄 'Keberanian yang kita temukan membuat tawa kita terdengar dua kali lebih renyah.'",
                "coReading": "💡 Beri Semangat: Tepuk pundak si kecil dan puji setiap keberanian yang ia tunjukkan hari ini!",
                "imagePrompt": "Joyous children's illustration of Bayu lifting his head above the water, hair delightfully wet, laughing with a bright triumphant smile. Water droplets glisten like stars in the afternoon light. Warm crayon strokes, naive folk art, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Balutan Handuk Hangat dan Senja",
                "titleEn": "A Warm Towel Hug at Sunset",
                "textId": "Ayah membungkus tubuh Bayu dengan handuk katun oranye yang tebal dan wangi matahari. Sambil duduk bersandar di batu hangat, Bayu melihat Ikan Mas melompat kecil di kolam seolah memberi salam selamat jalan.",
                "textEn": "Papa wrapped Bayu in a thick, sun-warmed orange cotton towel. Sitting back against the sun-warmed rocks, Bayu watched the Goldfish make a gentle splash, as if bidding a fond farewell until next time.",
                "quote": "🧡 'Rasa hangat di tubuh kita terasa begitu nikmat setelah berpetualang di air yang sejuk.'",
                "coReading": "💡 Tanya si Kecil: Benda hangat apa yang paling nyaman kamu peluk setelah selesai mandi?",
                "imagePrompt": "Cozy children's book scene of boy Bayu wrapped snug in a fluffy orange hooded towel on a grassy bank, sipping warm tea from a thermos with his father. Twilight sky painted in peach and violet, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Mimpi Melayang di Kolam Berbintang",
                "titleEn": "Drifting in a Pool of Stars",
                "textId": "Malam itu, di tempat tidurnya yang kering dan empuk, tubuh Bayu terasa ringan seperti melayang di atas air tenang. Dalam tidurnya, ia bermimpi berenang bebas di danau malam bertabur bintang keemasan. Selamat tidur, perenang cilik pemberani.",
                "textEn": "That night in his snug, dry bed, Bayu's little body felt weightless, as if floating effortlessly upon tranquil waters. In his sweet dreams, he swam freely across a midnight lake dusted with golden starlight. Goodnight, brave little swimmer.",
                "quote": "🌙 'Hati yang berani melangkah akan dihadiahi tidur malam yang paling tenang dan lelap.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak hebat, besok kamu bisa menjelajahi dunia dengan senyuman baru.",
                "imagePrompt": "Peaceful bedtime story illustration of boy Bayu sleeping peacefully under an aqua-blue blanket, a dreamy smile on his lips. A faint dreamy swirl above shows stars floating like golden fish in a calm night sky. Crescent moon outside, soft crayon and oil pastel on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s41)

    return stories

print("Story module 40-41 defined successfully")
