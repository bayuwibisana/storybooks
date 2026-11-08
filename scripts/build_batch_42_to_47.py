# scripts/build_batch_42_to_47.py
import json

def get_stories_42_to_44():
    stories = []

    # =========================================================================
    # STORY 42: Tenda Kain di Bawah Bintang
    # =========================================================================
    s42 = {
        "id": "tenda-kain-berbintang",
        "storyNumber": 42,
        "title": "Tenda Kain di Bawah Bintang",
        "englishTitle": "The Blanket Tent Under the Stars",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 4–7 Tahun",
        "moralTheme": "Keseruan pertama kali berkemah di halaman belakang rumah dan rasa aman bersama keluarga",
        "cover": "images/story42_cover.jpg",
        "coverImage": "images/story42_cover.jpg",
        "synopsis": "Dimas dan Ayah mendirikan tenda kain buatan sendiri di atas rumput halaman belakang rumah. Dengan senter kuningan kecil, suara jangkrik malam, dan bayangan boneka di dinding kain, Dimas merasakan petualangan alam liar pertamanya yang aman dan hangat.",
        "synopsisEn": "Dimas and his Papa set up a handmade blanket tent in the grassy backyard. With a brass flashlight, the crickets' bedtime song, and hand-shadow puppets on the canvas walls, Dimas experiences his very first cozy wilderness campout.",
        "protagonist": "Dimas (Anak laki-laki 5 tahun berpiyama flanel kotak-kotak merah)",
        "companion": "Ayah Dimas (Ayah penyayang bertopi rimba rajut wol)",
        "setting": "Halaman Rumput Belakang Rumah di Bawah Langit Berbintang",
        "pages": [
            {
                "number": 1,
                "title": "Tali Jemuran dan Selimut Kanvas",
                "titleEn": "Clothesline and Canvas Blankets",
                "textId": "Sore itu, halaman belakang rumah disulap menjadi perkemahan rimba. Ayah mengikat seutas tali tambang di antara dua pohon mangga, lalu bersama Dimas menyampirkan selimut kanvas bergaris biru tebal untuk membentuk atap segitiga.",
                "textEn": "That late afternoon, the backyard was magically transformed into a wild wilderness camp. Papa tied a sturdy rope between two shady mango trees, and together with Dimas, draped a thick blue-striped canvas blanket across it to form a triangular roof.",
                "quote": "⛺ 'Imajinasi dan selembar selimut bisa membangun istana petualangan paling hebat.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu membuat tenda dari selimut dan kursi di dalam rumah?",
                "imagePrompt": "Charming children's book illustration of toddler boy Dimas in red flannel pyjamas and his kind father setting up an A-frame blanket tent in a grassy backyard under two tall mango trees. Handcrafted wax crayon and chalky oil pastel, textured cream watercolor paper, simple black bead eyes, 4:3 landscape, completely text-free."
            },
            {
                "number": 2,
                "title": "Pancang Pasak dari Ranting Kayu",
                "titleEn": "Wooden Twig Tent Stakes",
                "textId": "Agar tenda tidak terbang ditiup angin senja, Dimas mencari empat batu bulat dan pasak ranting kayu di bawah pagar. Dengan palu kayu kecil, Dimas mengetuk pasak ke tanah dengan sungguh-sungguh: tak-tak-tak!",
                "textEn": "So their tent wouldn't blow away in the twilight breeze, Dimas collected four smooth river rocks and wooden twig stakes along the garden fence. With a toy wooden mallet, Dimas tapped each stake into the lawn with earnest care: tap-tap-tap!",
                "quote": "🔨 'Bekerja sama mendirikan tenda membuat setiap sudutnya terasa lebih kokoh.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara mengetuk palu kayu bersama si kecil: 'Tak-tak-tak!'",
                "imagePrompt": "Whimsical storybook scene of boy Dimas kneeling on the grass, carefully placing round river stones and wooden pegs to pin down the edges of the blanket tent. Twilight sky painted in warm apricot and lavender, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Matras Empuk dan Karpet Jerami",
                "titleEn": "Soft Mats and Woven Straw Carpet",
                "textId": "Di dalam tenda, Ayah menggelar tikar pandan yang harum dan tumpukan bantal empuk bersarung flanel. Saat Dimas merangkak masuk, ruang sempit itu terasa begitu hangat, wangi rumput basah, dan nyaman seperti sarang tupai.",
                "textEn": "Inside the tent, Papa unrolled a fragrant woven pandan mat topped with a plush stack of flannel pillows. When Dimas crawled inside, the snug little space felt wonderfully warm, scented with fresh dewy grass, and as cozy as a squirrel's nest.",
                "quote": "🛏️ 'Ruang yang sederhana akan terasa mewah saat diisi dengan rasa nyaman dan cinta.'",
                "coReading": "💡 Tanya si Kecil: Bantal atau boneka apa yang wajib kamu bawa jika berkemah di tenda?",
                "imagePrompt": "Cozy children's illustration looking inside the warm interior of the blanket tent, featuring colorful pillows, a woven mat, and little boy Dimas peeking out with an excited happy grin. Soft crayon scribbles, warm lantern light, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Cahaya Bulat Senter Kuningan",
                "titleEn": "The Brass Flashlight's Round Beam",
                "textId": "KLIK! Dimas menyalakan senter kuningan antik peninggalan kakek. Cahaya bulat kuning keemasan memancar di langit-langit tenda kain. Di luar tenda, malam mulai turun membentangkan selendang gelap yang tenang.",
                "textEn": "CLICK! Dimas switched on Grandpa's vintage brass flashlight. A round beam of golden amber light painted a sun upon the fabric ceiling. Outside the tent, night softly draped its tranquil, starlit mantle across the garden.",
                "quote": "🔦 'Satu titik cahaya kecil cukup untuk mengusir rasa takut dari ruangan yang gelap.'",
                "coReading": "💡 Aktivitas Seru: Bentuk jari tanganmu di depan senter untuk membuat bayangan kupu-kupu atau kelinci!",
                "imagePrompt": "Heartwarming storybook illustration of Dimas holding an antique brass flashlight pointing up at the tent roof, casting a warm golden spotlight circle. Soft evening shadows, wax crayon on heavy watercolor paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Teater Bayangan Kelinci Malam",
                "titleEn": "The Midnight Rabbit Shadow Play",
                "textId": "Ayah mengangkat tangannya di depan berkas cahaya senter. Jemari Ayah bergoyang, dan di dinding kain tenda muncul bayangan seekor kelinci bertelinga panjang yang sedang melompat lucu. Dimas tertawa terkikik-kikik gembira.",
                "textEn": "Papa lifted his hands before the flashlight's beam. Moving his fingers playfully, the shadow of a long-eared bunny rabbit bounced across the canvas wall. Dimas broke into cheerful, contagious giggles.",
                "quote": "🐇 'Kegelapan malam bukanlah hal menakutkan, melainkan panggung untuk permainan yang seru.'",
                "coReading": "💡 Tanya si Kecil: Bentuk bayangan apa yang paling lucu yang pernah kamu buat di dinding?",
                "imagePrompt": "Delightful bedtime picture book scene showing Papa and Dimas making animal hand shadow puppets (a bunny rabbit and a barking dog) projected on the tent's inner blanket wall. Warm glowing yellow light, cozy bedtime atmosphere, crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Konser Jangkrik dan Desau Angin",
                "titleEn": "Crickets' Chorus and Whispering Breeze",
                "textId": "Krik-krik-krik... Dari semak-semak lavender di dekat kolam, sekawanan jangkrik mulai menyanyikan simfoni malam. Daun pohon mangga berdesir pelan diterpa angin sejuk, seperti nyanyian lembut yang menenangkan jiwa.",
                "textEn": "Chirp-chirp-chirp... From the lavender bushes by the pond, a chorus of crickets began their gentle nighttime symphony. The mango leaves rustled in the cool breeze, sounding just like a soothing lullaby from the earth.",
                "quote": "🦗 'Alam memiliki musik pengantar tidur terindah bagi siapa saja yang mau mendengarkannya.'",
                "coReading": "💡 Dengarkan Bersama: Pejamkan mata sejenak dan dengarkan bunyi-bunyian malam di sekitarmu.",
                "imagePrompt": "Serene outdoor illustration of the glowing blanket tent on the grassy lawn under a starry sky, surrounded by lavender bushes where friendly little crickets sing. Gentle moonlight washes over the garden, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Menghitung Bintang dari Pintu Tenda",
                "titleEn": "Counting Stars from the Tent Door",
                "textId": "Ayah membuka sedikit kain pintu tenda. Dari celah itu, Dimas memandangi langit malam yang ditaburi ribuan bintang perak berkilau. \"Satu, dua, tiga... banyak sekali, Ayah!\" bisik Dimas penuh takjub.",
                "textEn": "Papa folded back a flap of the tent entrance. Through the opening, Dimas gazed up into a velvet night sky sprinkled with thousands of gleaming silver stars. \"One, two, three... there are so many, Papa!\" whispered Dimas in pure awe.",
                "quote": "⭐ 'Bintang-bintang di langit malam seperti lampu-lampu kecil yang menjaga tidur kita.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat bintang jatuh dan mengucapkan permohonan dalam hati?",
                "imagePrompt": "Breathtaking children's book illustration looking out from the tent flap: boy Dimas and his father lying on their bellies gazing up at a deep indigo sky filled with swirling constellations and crescent moon. Wax crayon and chalky pastel, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Uap Teh Chamomile Hangat",
                "titleEn": "Steaming Mug of Chamomile Tea",
                "textId": "Ibu membawakan termos kecil berisi teh chamomile hangat beraroma madu dan biskuit gandum renyah. Sambil duduk bersila di dalam tenda, mereka menikmati kehangatan minuman yang menenangkan perut dan hati.",
                "textEn": "Mama brought out a little thermos of warm honeyed chamomile tea and crunchy oat biscuits. Sitting cross-legged inside the tent, they savored the fragrant warm drink that brought deep calm to tummy and heart.",
                "quote": "🍵 'Secangkir kehangatan di malam hari adalah pelukan yang bisa kita rasakan.'",
                "coReading": "💡 Tanya si Kecil: Minuman hangat apa yang paling kamu sukai di malam hari?",
                "imagePrompt": "Sweet storybook illustration of Mama sitting at the tent entrance handing a steaming cup of tea to Dimas, while Papa smiles warmly beside them. Warm lantern glow, cozy familial love, wax crayon on textured paper, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Mata yang Mulai Mengantuk",
                "titleEn": "Eyelids Growing Heavy",
                "textId": "Kancing senter dimatikan. Hanya ada cahaya keemasan lembut dari lentera kecil di luar tenda. Kelopak mata Dimas mulai terasa seberat batu kerikil. Suara Ayah yang membacakan dongeng terdengar semakin pelan dan menenangkan.",
                "textEn": "The flashlight clicked off. Only the soft golden glow of a fairy lantern flickered gently outside the tent. Dimas's eyelids grew heavy as little river stones. Papa's storytelling voice drifted softer, soothing like a warm river.",
                "quote": "😴 'Saat rasa aman memeluk kita, tidur datang dengan begitu lembut dan manis.'",
                "coReading": "💡 Peluk si Kecil: Rapatkan selimutnya dan elus kening si kecil dengan lembut.",
                "imagePrompt": "Tender illustration of boy Dimas curling under the thick quilt in the tent, yawning peacefully as his father tucks the blanket around his shoulders. Soft amber lantern light spilling in, wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Mimpi Penjelajah Bintang Rimba",
                "titleEn": "Dreams of the Star Wilderness Explorer",
                "textId": "Di dalam tenda kain di halaman belakang, Dimas terlelap pulas dalam pelukan malam. Di luar sana, bulan sabit tersenyum lembut di atas pohon mangga. Dimas bermimpi menjadi kapten penjelajah bintang di galaksi yang damai. Selamat tidur, penjelajah cilik.",
                "textEn": "Inside the backyard blanket tent, Dimas slept soundly in night's gentle embrace. Above, the smiling silver crescent moon watched over the mango trees. Dimas dreamed of being a brave star-captain in a peaceful galaxy. Goodnight, brave little camper.",
                "quote": "🌙 'Selamat malam tenda petualang, besok ada fajar baru yang menyapa dengan hangat.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak petualang, semoga mimpi indah berbintang malam ini.",
                "imagePrompt": "Magical bedtime illustration of the glowing tent under a tranquil moonlit garden. Dimas sleeps peacefully inside, clutching a small toy bear. Golden fireflies dance above the lawn, deep navy and indigo watercolor sky with stars, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s42)

    # =========================================================================
    # STORY 43: Mencapai Puncak Bukit Pelangi
    # =========================================================================
    s43 = {
        "id": "puncak-bukit-pelangi",
        "storyNumber": 43,
        "title": "Mencapai Puncak Bukit Pelangi",
        "englishTitle": "Reaching the Top of Rainbow Hill",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 4–7 Tahun",
        "moralTheme": "Ketekunan, kesabaran melangkah setapak demi setapak, dan keindahan proses",
        "cover": "images/story43_cover.jpg",
        "coverImage": "images/story43_cover.jpg",
        "synopsis": "Bukit Pelangi tampak begitu tinggi dan menjulang di kejauhan. Sinta sempat ingin menyerah karena kakinya lelah, tetapi bersama sahabatnya si Kancil yang lincah, Sinta belajar menikmati setiap langkah kecil hingga berhasil memetik bunga awan di puncak bukit.",
        "synopsisEn": "Rainbow Hill seemed impossibly tall and distant. Little Sinta felt like giving up as her legs grew tired, but with her cheerful guide Kancil the mouse-deer, Sinta learns to cherish each small step until they touch the clouds at the blooming summit.",
        "protagonist": "Sinta (Gadis cilik 6 tahun berambut kuncir kuda dengan tongkat kayu ukir)",
        "companion": "Kancil (Kancil cerdik berbulu cokelat keemasan bertotol putih halus)",
        "setting": "Lereng Bukit Berbunga Menuju Puncak Awan Pelangi",
        "pages": [
            {
                "number": 1,
                "title": "Menatap Bukit yang Menjulang",
                "titleEn": "Gazing Up at the Towering Hill",
                "textId": "Dari padang rumput bawah, Bukit Pelangi tampak menjulang tinggi menyentuh awan putih. Lerengnya dihiasi karpet bunga liar berwarna ungu, kuning mentega, dan merah muda. Sinta memegang tongkat kayu ukirnya dengan kagum bercampur ragu.",
                "textEn": "From the lowland meadow, Rainbow Hill rose majestically to touch the drifting white clouds. Its slopes were carpeted with wild mountain blossoms in violet, butter-yellow, and blush-pink. Sinta held her carved walking stick in awe and quiet wonder.",
                "quote": "🏔️ 'Gunung yang tinggi selalu terlihat paling menantang saat kita baru berdiri di kakinya.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat bukit atau tangga yang sangat tinggi?",
                "imagePrompt": "Charming children's book illustration of little girl Sinta with a wooden hiking stick and a tiny backpack standing in a flower meadow, looking up at a grand colorful hill rising into soft pastel clouds. Kancil the mouse-deer stands beside her. Handcrafted wax crayon and oil pastel, textured cream watercolor paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Langkah Lincah Si Kancil",
                "titleEn": "Kancil's Cheerful Bounds",
                "textId": "\"Tak-tik-tuk! Ayo, Sinta! Perjalanan seribu langkah dimulai dari langkah yang pertama!\" seru Kancil sambil melompati batu kali kecil. Matanya berbinar ceria, memberi semangat pada sahabat manusianya.",
                "textEn": "\"Click-clack-hop! Come along, Sinta! A journey of a thousand miles begins with a single joyful step!\" called Kancil, leaping playfully over a mossy river rock. His bright eyes danced with encouragement for his human friend.",
                "quote": "🦌 'Langkah pertama mungkin kecil, tetapi tanpa itu kita tidak akan pernah tiba di puncak.'",
                "coReading": "💡 Aktivitas Seru: Langkahkan kakimu di tempat: 'Satu, dua, tiga, kita mulai melangkah!'",
                "imagePrompt": "A whimsical storybook illustration of Kancil the adorable little mouse-deer hopping merrily along a winding stone path lined with wildflowers, looking back with a warm smile to urge Sinta onward. Crayon scribbles, warm sunlit hillside, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Jalan Setapak Berkelok Batu",
                "titleEn": "The Winding Pebble Path",
                "textId": "Mereka mulai mendaki jalan setapak yang berliku. Tongkat kayu Sinta mengetuk tanah dengan mantap: tuk, tuk, tuk. Di kanan dan kiri, kupu-kupu bersayap kuning belerang beterbangan mengiringi langkah mereka.",
                "textEn": "They began ascending the winding dirt trail. Sinta's wooden staff tapped the earth steadily: thump, thump, thump. To their left and right, sulfur-yellow mountain butterflies fluttered alongside like cheerful winged guides.",
                "quote": "🦋 'Saat kita melangkah dengan sabar, alam selalu menyuguhkan kawan-kawan yang ramah.'",
                "coReading": "💡 Tanya si Kecil: Hewan kecil apa yang sering kamu jumpai saat berjalan-jalan di taman?",
                "imagePrompt": "Picturesque illustration of Sinta hiking up a gentle mountain trail with her walking staff, surrounded by fluttering yellow butterflies and wild daisies. Kancil trots nearby. Handcrafted wax crayon, soft folk-art style, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Napas Terengah di Bawah Pohon Cemara",
                "titleEn": "Resting Beneath the Pine Tree",
                "textId": "Di tengah lereng, tanjakan terasa semakin curam. Kaki Sinta mulai pegal dan napasnya terengah-engah. \"Aduh, Kancil... Bukit ini terlalu tinggi. Bisakah kita pulang saja?\" keluh Sinta sambil duduk di akar pohon cemara.",
                "textEn": "Halfway up the slope, the climb grew noticeably steeper. Sinta's little calves began to ache and her breath came in short puffs. \"Oh, Kancil... This hill is far too high. Can we just turn back?\" sighed Sinta, sinking down onto the roots of a pine tree.",
                "quote": "🌲 'Merasa lelah bukanlah tanda gagal, itu hanya tanda bahwa tubuh kita butuh istirahat sejenak.'",
                "coReading": "💡 Tanya si Kecil: Apa yang kamu rasakan saat kakimu capek sehabis bermain atau berjalan jauh?",
                "imagePrompt": "Touching children's storybook scene of Sinta sitting resting on gnarled pine tree roots, wiping her brow with a tired but thoughtful expression. Kancil nuzzles her knee gently in comfort. Warm earthy tones, crayon texture on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Seteguk Air dan Cerita Kancil",
                "titleEn": "A Sip of Water and Kancil's Tale",
                "textId": "Kancil mengambil labu air minum Sinta dan menyodorkannya ramah. \"Lihat ke bawah sana, Sinta. Lihat betapa jauhnya kamu sudah berjalan dari rumah! Jangan tatap sisa jalannya, cukup nikmati satu langkah berikutnya.\"",
                "textEn": "Kancil fetched Sinta's water gourd and nudged it forward kindly. \"Look back down the valley, Sinta. Look how far you have already climbed from home! Don't worry about the whole mountain; just focus on one happy step at a time.\"",
                "quote": "💧 'Melihat kembali apa yang sudah kita capai akan meniupkan kekuatan baru ke dalam dada.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu merasa bangga setelah berhasil menyelesaikan tugas yang sulit?",
                "imagePrompt": "Heartwarming illustration of Sinta taking a refreshing sip from her water canteen while sitting with Kancil, looking back over the valley below dotted with tiny village rooftops. Soft watercolor-like crayon blending, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Langkah Rahasia: Menghitung Sepuluh",
                "titleEn": "The Secret Ten-Step Rhythm",
                "textId": "Sinta bangkit kembali. Kali ini, ia mencoba rahasia Kancil: menghitung sepuluh langkah, lalu bernapas pelan. Satu... dua... tiga... Langkahnya terasa ringan seperti permainan ketukan musik di tanah.",
                "textEn": "Sinta stood up with renewed energy. This time she tried Kancil's secret trick: counting ten rhythmic steps, then taking one deep breath. One... two... three... Her steps felt light and playful, like tapping out music on the earth.",
                "quote": "🎵 'Saat kita membagi tujuan besar menjadi langkah-langkah kecil, semuanya terasa mungkin.'",
                "coReading": "💡 Aktivitas Bersama: Hitung bersama dari 1 sampai 10 dengan riang sambil bertepuk tangan!",
                "imagePrompt": "Joyous children's picture book illustration of Sinta smiling brightly as she strides uphill, counting on her fingers, while Kancil bounds alongside in playful synchrony. Green slopes blossoming with mountain flora, wax crayon strokes, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Kabut Sejuk Menyambut Puncak",
                "titleEn": "Cool Mist Welcomes the Crest",
                "textId": "Tiba-tiba, udara berubah menjadi sangat sejuk dan harum embun. Gumpalan kabut putih lembut mengalir melewati kaki mereka seperti selimut sutra. Tanah berbatu mulai mendatar. Mereka hampir sampai!",
                "textEn": "Suddenly, the mountain air turned pleasantly crisp and fragrant with dewy pine. Wisps of soft white mist drifted across their ankles like sheer silk ribbons. The rocky ground began to level out. They were almost there!",
                "quote": "☁️ 'Hawa dingin dan kabut lembut adalah tanda bahwa puncak impian sudah di depan mata.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu merasakan dinginnya kabut pagi hari di kulitmu?",
                "imagePrompt": "Serene and whimsical storybook illustration of Sinta and Kancil walking through soft swirls of mountain cloud mist near the summit ridge. The ground is carpeted in miniature alpine flowers, crayon textures on textured paper, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Berdiri di Atas Awan Pelangi",
                "titleEn": "Standing Atop Rainbow Peak",
                "textId": "HOREEE! Sinta dan Kancil tiba di puncak tertinggi Bukit Pelangi! Dari puncak ini, seluruh dunia tampak membentang luas dan indah di bawah sana. Sinar matahari senja membiaskan pelangi melingkar di atas awan.",
                "textEn": "HURRAY! Sinta and Kancil stepped onto the highest crest of Rainbow Hill! From this vantage, the whole world spread vast, peaceful, and wondrous below. Late sunset rays refracted into a glowing circular rainbow right above the sea of clouds.",
                "quote": "🌈 'Pemandangan terindah selalu dipersembahkan untuk mereka yang tidak pernah menyerah.'",
                "coReading": "💡 Teriakkan Gembira: Bersoraklah bersama si kecil: 'Horeee, aku berhasil!' dengan tangan terangkat!",
                "imagePrompt": "Magnificent and joyous children's book illustration of Sinta standing on the grassy hilltop summit raising her carved walking staff high, next to Kancil jumping with joy. In the background, a breathtaking circular rainbow shines in golden evening clouds, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Memetik Bunga Bintang Edelweiss",
                "titleEn": "Picking the Little Starflower",
                "textId": "Di puncak itu, Sinta memetik sekuntum bunga abadi putih kecil berbulu halus untuk disematkan di sakunya sebagai kenang-kenangan. Bersama Kancil, ia duduk menikmati semilir angin senja sambil mengunyah bekal roti manis.",
                "textEn": "On the summit, Sinta plucked a single velvety white edelweiss starflower to tuck into her pocket as a keepsake of her courage. Side-by-side with Kancil, she sat enjoying the cooling twilight breeze while sharing a sweet bread roll.",
                "quote": "🌼 'Kenangan tentang perjuangan kita akan selalu mekar harum di dalam hati selamanya.'",
                "coReading": "💡 Tanya si Kecil: Jika kamu mendaki gunung, benda kecil apa yang ingin kamu simpan sebagai kenangan?",
                "imagePrompt": "Peaceful illustration of Sinta and Kancil sitting together on a grassy knoll atop the mountain at golden hour, admiring a white edelweiss flower, sharing bread. Sunset colors of amber, rose, and indigo, handcrafted wax crayon, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Pulas di Bawah Selimut Hangat",
                "titleEn": "Sound Slumber Under the Warm Quilt",
                "textId": "Malam itu di kamarnya, Sinta tidur lelap sekali. Kakinya yang lelah kini beristirahat dengan damai di balik selimut wol. Bunga putih kecil di meja samping ranjangnya memancarkan aroma harum keberanian. Selamat tidur, pendaki cilik yang tangguh.",
                "textEn": "That night in her snug bedroom, Sinta slept the deepest, sweetest sleep. Her tired legs rested peacefully under the warm wool quilt. The tiny white starflower on her nightstand radiated a gentle perfume of quiet bravery. Goodnight, brave little mountaineer.",
                "quote": "🌙 'Tidur yang paling pulas adalah tidur setelah seharian melangkah dengan penuh kesungguhan.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak tangguh, kamu telah membuktikan bahwa kakimu mampu melangkah jauh.",
                "imagePrompt": "Tranquil bedtime illustration of girl Sinta sleeping deeply under a patchwork quilt, smiling serenely. On her rustic wooden bedside table, the small white edelweiss blossom rests in a glass of water beneath glowing moonbeams, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s43)

    return stories

print("Story module 42-43 defined successfully")
