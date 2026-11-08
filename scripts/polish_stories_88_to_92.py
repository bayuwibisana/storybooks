# scripts/polish_stories_88_to_92.py
import json

def get_stories_88_to_92():
    stories = [
        # --- STORY 88: Pondasi Menara Balok yang Kokoh ---
        {
            "id": "story88",
            "storyNumber": 88,
            "title": "Pondasi Menara Balok yang Kokoh",
            "englishTitle": "Sturdy Foundation of the Block Tower",
            "category": "perseverance",
            "categoryLabel": "🐢 Ketekunan & Rasa Percaya Diri",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Membangun dari fondasi yang kuat, kesabaran menyusun, & tidak mudah menyerah",
            "cover": "covers/story88_cover.jpg",
            "synopsis": "Farel ingin membangun menara balok kayu yang menjulang tinggi hingga menyentuh meja belajarnya. Namun setiap kali mencapai tingkat kelima, menara itu selalu bergoyang dan roboh berantakan. Bersama Kakak, Farel belajar bahwa rahasia menara tinggi ada pada fondasi bawah yang lebar dan kokoh.",
            "protagonist": "Farel (Anak laki-laki berkemeja bergaris)",
            "companion": "Kakak Farel (Kakak memberi balok segitiga penopang)",
            "setting": "Ruang Bermain Bersih",
            "pages": [
                {
                    "number": 1,
                    "title": "Kotak Kayu Berisi Balok Warna-Warni",
                    "titleEn": "Wooden Crate of Colorful Blocks",
                    "textId": "Di atas karpet ruang bermain yang bersih, Farel menuang kotak kayu berisi puluhan balok kayu pinus halus. Ada kubus merah delima, balok panjang kuning matahari, silinder biru laut, dan prisma segitiga hijau rumput. Suara balok beradu 'Klotak-klotak!' terdengar riang mengundang petualangan.",
                    "textEn": "On the clean playroom carpet, Farel tipped over a wooden crate of smooth pine blocks. There were ruby-red cubes, sunny-yellow long planks, ocean-blue cylinders, and grass-green triangular prisms. The cheerful 'Clack-clatter!' of wooden blocks sparked excitement.",
                    "quote": "Bahan-bahan sederhana siap disusun menjadi impian yang tinggi.",
                    "coReading": "Bentuk balok kayu apa saja yang ada di dalam kotak mainan Farel?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Farel, a cute young boy in a blue-and-white striped shirt, sitting on a soft playroom rug with a wooden toy chest spilling out colorful wooden blocks. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Impian Menara Setinggi Meja",
                    "titleEn": "Dream of a Table-High Tower",
                    "textId": "Farel memandang ke atas, ke arah tepi meja belajar kayunya. 'Hari ini aku akan membangun menara istana raksasa yang puncaknya setinggi meja!' tekad Farel. Ia mulai menumpuk balok kubus satu per satu ke atas secara lurus.",
                    "textEn": "Farel looked up toward the edge of his wooden study desk. 'Today I will build a giant castle tower with a peak as tall as the desk!' Farel resolved. He began stacking block cubes straight upward one on top of the other.",
                    "quote": "Mempunyai impian yang tinggi memberi semangat untuk mulai melangkah.",
                    "coReading": "Seberapa tinggi menara yang ingin dibangun oleh Farel?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Farel carefully balancing a third yellow block onto a precarious single-column tower on the rug. Desk edge visible above, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Goyangan di Tingkat Kelima",
                    "titleEn": "A Wobble at Level Five",
                    "textId": "Ketika balok kelima diletakkan di puncak, menara mulai bergoyang pelan. Tiang itu terlalu kurus dan hanya bertumpu pada satu balok kecil di bagian bawah. Farel menahan napas, tangannya gemetar sedikit saat meletakkan balok keenam.",
                    "textEn": "As the fifth block touched the top, the tower began to sway gently. The column was too skinny, supported by just a single tiny block at the base. Farel held his breath, his hands trembling slightly as he placed a sixth block.",
                    "quote": "Kerapuhan muncul bila bagian bawah tidak mampu menahan beban di atasnya.",
                    "coReading": "Mengapa menara Farel mulai bergoyang oleng?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Close-up of a wobbly vertical stack of wooden blocks leaning to the side. Farel's hands hovering nervously, wide focused bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Prang! Runtuhnya Menara Pertama",
                    "titleEn": "Crash! The First Tower Falls",
                    "textId": "'Klotak, brakkk!' Hanya karena hembusan napas Farel yang tergesa-gesa, menara itu roboh dan balok-balok berhamburan di atas karpet. Farel menjatuhkan bahunya lesu dan cemberut. Ini sudah kali ketiga menaranya runtuh sebelum tinggi.",
                    "textEn": "'Clatter, tumble!' Just from a hurried puff of breath, the tower collapsed, blocks scattering across the carpet. Farel slumped his shoulders with a disappointed pout. This was the third time his tower had tumbled before reaching high.",
                    "quote": "Kekecewaan adalah tanda bahwa kita sungguh-sungguh peduli pada apa yang kita buat.",
                    "coReading": "Pernahkah menara balokmu roboh saat sedang seru-serunya dibangun?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Scattered wooden blocks on the rug with Farel sitting with his chin in his hands, looking discouraged. Naive storybook style, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Rahasia Fondasi dari Kakak",
                    "titleEn": "Brother's Foundation Secret",
                    "textId": "Kakak duduk bersila di samping Farel sambil tersenyum hangat. 'Farel, perhatikan pohon beringin di depan rumah. Akarnya melebar luas di tanah sebelum batangnya tumbuh menjulang tinggi. Jika ingin menaramu kokoh, buatlah bagian bawahnya lebar dan rapat.'",
                    "textEn": "Older Brother sat cross-legged beside Farel with a warm smile. 'Farel, look at the banyan tree in the yard. Its roots spread wide in the soil before its trunk climbs high into the sky. If you want your tower sturdy, make the base wide and solid.'",
                    "quote": "Belajar dari alam memberi petunjuk terbaik untuk menyelesaikan masalah.",
                    "coReading": "Mengapa pohon beringin bisa berdiri kokoh meski tinggi sekali?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Kind older brother sitting beside Farel on the rug, arranging four wide square wooden blocks side by side as a flat foundation. Farel watching with renewed interest, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Empat Balok Penopang Bawah",
                    "titleEn": "Four Base Supporting Blocks",
                    "textId": "Farel mengangguk paham. Kali ini ia tidak langsung menumpuk ke atas. Di lantai karpet, Farel menata empat balok persegi panjang membentuk dasar yang lebar dan rata seperti benteng. Di atasnya, ia menaruh tiga balok tebal mengunci sambungan.",
                    "textEn": "Farel nodded with understanding. This time he did not rush upward. On the carpet, he laid four rectangular blocks to form a wide, flat foundation like a castle base. Across them, he locked three thick blocks over the seams.",
                    "quote": "Fondasi yang lapang memberi ruang yang aman bagi pertumbuhan yang tinggi.",
                    "coReading": "Berapa banyak balok yang dipasang Farel untuk dasar menaranya?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Farel placing interlocking wooden blocks in a pyramid-like sturdy wide base on the floor. Sturdy construction taking shape, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Naik Tingkat Demi Tingkat dengan Mantap",
                    "titleEn": "Climbing Level by Level with Steadiness",
                    "textId": "Kini tingkat kelima terlewati tanpa goyangan sedikit pun! Menara itu berdiri tegak, mantap, dan berwibawa. Setiap balok saling menopang satu sama lain. Tingkat keenam, ketujuh, dan kedelapan tersusun dengan mulus di bawah tangan Farel yang tenang.",
                    "textEn": "Now level five was passed without the slightest wobble! The tower stood tall, steady, and proud. Each block braced the ones around it. Levels six, seven, and eight stacked smoothly beneath Farel's steady, patient hands.",
                    "quote": "Ketenangan hati membuat tangan bekerja dengan presisi yang sempurna.",
                    "coReading": "Apakah menaranya masih bergoyang sekarang?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. The tall wooden tower rising stably past Farel's chest, reaching up toward the desk height. Farel standing up carefully placing another block, smiling with bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Kubah Segitiga di Puncak Menara",
                    "titleEn": "Triangular Dome on the Peak",
                    "textId": "Dengan berjingkat perlahan, Farel meletakkan balok prisma segitiga merah tua di puncak tertinggi menara. Puncak segitiga itu kini sejajar sempurna dengan tepi meja belajar! 'Berhasil! Menara Mega Istana telah selesai!' bisik Farel bersorak penuh kemenangan.",
                    "textEn": "Standing gently on tiptoes, Farel placed a dark red triangular prism atop the highest spire. The pointy tip now aligned perfectly with the study desk's edge! 'I did it! The Mega Castle Tower is finished!' Farel cheered in quiet triumph.",
                    "quote": "Kepuasan sejati hadir ketika kita menyelesaikan apa yang kita mulai dengan tekun.",
                    "coReading": "Bentuk balok apa yang ditaruh Farel di puncak menara?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Farel standing on tiptoe placing the final red triangular cap block atop the towering wooden structure that aligns with the desk. Brother clapping in background, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Tepuk Tangan dan Tos Saudara",
                    "titleEn": "Applause and a High Five",
                    "textId": "Kakak bertepuk tangan bangga dan memberi tos telapak tangan pada Farel: 'Plak!' Farel memeluk menara itu dari kejauhan dengan tatapan kagum. Menara kayu itu tidak bergoyang meski lantai karpet bergetar saat mereka melompat girang.",
                    "textEn": "Brother clapped with pride and shared a high-five with Farel: 'Snap!' Farel admired his creation from a short distance with sparkling eyes. The wooden tower stood rock-solid, not flinching even as the floor vibrated with their happy bounces.",
                    "quote": "Kemenangan terasa semakin manis saat dirayakan bersama keluarga tercinta.",
                    "coReading": "Mengapa menara itu tidak roboh meski mereka melompat?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Farel and his older brother giving each other a joyful high-five beside the magnificent standing block tower. Warm playroom ambiance, sunny window, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Istana di Negeri Dongeng",
                    "titleEn": "Dreams of Fairytale Castles",
                    "textId": "Malam tiba dan menara balok dibiarkan berdiri anggun di sudut kamar sebagai pengingat keberhasilan hari ini. Di atas kasur empuknya, Farel tidur lelap diselimuti kehangatan. Di dalam mimpinya, ia menjadi arsitek cilik yang membangun istana-istana megah di atas awan keemasan.",
                    "textEn": "Night arrived and the block tower was left standing proud in the bedroom corner as a trophy of today's patience. On his soft bed, Farel slept deeply wrapped in cozy warmth. In his dreams, he was a little architect building magnificent castles upon golden clouds.",
                    "quote": "Tidurlah dengan damai wahai pembangun kecil, fondasi kuat ada di dalam ketekunanmu.",
                    "coReading": "Selamat tidur anak hebat, esok kamu bisa membangun hal-hal baru lagi.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Farel sleeping peacefully in bed with a quilt. In the corner of the room, the tall wooden block tower stands silhouetted under moonlight streaming through window. Starlit night sky outside, serene bedtime scene, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 89: Tiupan Nada Pertama Seruling Bambu ---
        {
            "id": "story89",
            "storyNumber": 89,
            "title": "Tiupan Nada Pertama Seruling Bambu",
            "englishTitle": "First Notes from the Bamboo Flute",
            "category": "perseverance",
            "categoryLabel": "🐢 Ketekunan & Rasa Percaya Diri",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kesabaran mengatur napas, ketekunan berlatih, & musik pengantar damai",
            "cover": "covers/story89_cover.jpg",
            "synopsis": "Ranu, anak gembala kecil di padang rumput berangin, mendapat seruling bambu dari kakeknya. Awalnya tiupan Ranu hanya berbunyi desis angin kosong tanpa nada. Bersama kerbau jinak kesayangannya, Si Belo, Ranu belajar memposisikan bibir dan mengatur hembusan napas hingga lahirlah nada pertama yang merdu.",
            "protagonist": "Ranu (Anak gembala berseruling bambu)",
            "companion": "Kerbau Jinak (Kerbau mendengarkan sambil mengunyah rumput)",
            "setting": "Padang Rumput Berangin",
            "pages": [
                {
                    "number": 1,
                    "title": "Seruling Bambu Berikat Benang Merah",
                    "titleEn": "Bamboo Flute Tied with Red Cord",
                    "textId": "Di punggung padang rumput berbukit yang hijau melambai, Ranu duduk beralaskan caping anyaman bambunya. Di tangannya terpegang seruling bambu tamiang kuning mengilap yang diikat benang merah pada kedua ujungnya. Seruling itu adalah hadiah ulang tahun keenam dari Kakek.",
                    "textEn": "On the rolling green pasture hill, Ranu sat on his woven bamboo farmer's hat. In his hands he held a shiny yellow bamboo flute tied with red braided cord at both ends. The flute was a sixth birthday gift from Grandpa.",
                    "quote": "Sebuah alat musik tradisional menyimpan jiwa dan kehangatan alam.",
                    "coReading": "Pernahkah kamu melihat seruling bambu yang memiliki lubang-lubang tiup?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Ranu, a sweet young shepherd boy in cotton shorts and rolled sleeves, sitting on a grassy knoll holding a polished yellow bamboo flute. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Si Belo Sahabat Pengunyah Rumput",
                    "titleEn": "Si Belo the Grazing Friend",
                    "textId": "Di samping Ranu, Si Belo—kerbau abu-abu jinak bertanduk melengkung indah—sedang asyik mengunyah rumput gajah yang manis. Telinga Si Belo bergerak-gerak mengusir lalat padang. Si Belo menoleh pada Ranu dengan mata bulat yang teduh, menunggu pertunjukan musik sahabatnya.",
                    "textEn": "Beside Ranu, Si Belo—a gentle grey water buffalo with lovely curved horns—contentedly munched sweet tall grass. Si Belo's ears flicked to shoo pasture flies, turning to Ranu with placid, gentle eyes, waiting for his friend's musical debut.",
                    "quote": "Sahabat sejati adalah pendengar paling setia di kala kita sedang belajar.",
                    "coReading": "Suara apa yang biasa dikeluarkan oleh seekor kerbau jinak?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Si Belo the gentle water buffalo with big peaceful eyes resting on green pasture grass beside Ranu. Blue sky with white fluffy clouds, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Desisan Angin Tanpa Suara",
                    "titleEn": "Hiss of Soundless Wind",
                    "textId": "Ranu menempelkan bibirnya ke lubang tiup seruling dan meniup sekuat tenaga: 'Fuuuh...!' Namun tidak ada nada merdu yang keluar, hanya desisan angin hampa seperti angin yang meniup celah jendela. Ranu meniup lagi hingga pipinya kembung dan memerah, tetapi suaranya tetap hening.",
                    "textEn": "Ranu pressed his lips to the flute blowhole and blew with all his might: 'Fuuush...!' But no sweet note came, only a hollow breeze like wind whistling through window slats. Ranu blew again until his cheeks puffed red, but still only empty air sounded.",
                    "quote": "Kekuatan tenaga yang berlebihan tidak selalu menghasilkan keindahan yang diharapkan.",
                    "coReading": "Mengapa seruling bambu tidak berbunyi saat ditiup terlalu keras?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Ranu with puffed-out cheeks blowing hard into the bamboo flute with an earnest puzzled expression. Si Belo blinking placidly beside him, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Nasihat Kakek tentang Bibir dan Napas",
                    "titleEn": "Grandpa's Lesson on Lips and Breath",
                    "textId": "Ranu teringat pesan Kakek sebelum berangkat ke padang rumput: 'Seruling bambu tidak suka ditiup kasar seperti meniup lilin kue, Ranu. Bentuklah bibirmu seperti hendak tersenyum tipis, dan hembuskan udara lembut seperti meniup sup panas.'",
                    "textEn": "Ranu recalled Grandpa's words before heading to pasture: 'A bamboo flute dislikes harsh blowing like birthday candles, Ranu. Shape your lips into a gentle half-smile, and breathe softly as if cooling warm soup.'",
                    "quote": "Kelembutan adalah kunci pembuka bagi nada-nada terindah.",
                    "coReading": "Coba bentuk bibirmu seperti tersenyum tipis dan tiup pelan!",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Ranu pausing, wiping his brow, reflecting with a gentle smile on his face, holding the flute gently against his lower lip. Peaceful pasture breeze blowing his hair, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Posisi Sudut yang Pas",
                    "titleEn": "The Perfect Slanted Angle",
                    "textId": "Ranu meletakkan tepi lubang seruling tepat di bawah garis bibir bawahnya. Ia memiringkan batang seruling sedikit ke bawah, membiarkan separuh hembusan napasnya masuk ke dalam lubang dan separuh lainnya meluncur di atas permukaan bambu.",
                    "textEn": "Ranu rested the edge of the blowhole right beneath the line of his lower lip. He angled the flute slightly downward, letting half of his gentle breath enter the hole while the other half skimmed across the bamboo rim.",
                    "quote": "Kecermatan menemukan posisi yang tepat adalah seni dari ketekunan.",
                    "coReading": "Bagaimana cara Ranu meletakkan seruling di bibirnya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Close-up of Ranu's mouth forming an elegant embouchure with the yellow bamboo flute blowhole. Morning pasture sunlight illuminating the scene, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Lahirnya Nada Emas Pertama",
                    "titleEn": "The Birth of the First Golden Note",
                    "textId": "Ranu menghembuskan napas yang lembut dan teratur. Tiba-tiba, 'Tluuurrrr...!' Dari dalam rongga bambu terdengar suara nada tinggi yang bening, bulat, dan merdu membelah keheningan bukit! Suara itu begitu bersih seperti tetesan embun yang jatuh ke dalam kendi air.",
                    "textEn": "Ranu released a soft, steady breath. Suddenly, 'Tootle-trillll...!' From within the hollow bamboo rang a crystal-clear, round, sweet note piercing the hill stillness! The tone was pure like a dewdrop falling into a water pitcher.",
                    "quote": "Momen pertama keberhasilan terasa seperti keajaiban yang menyinari jiwa.",
                    "coReading": "Bisakah kamu bersenandung menirukan nada merdu seruling bambu?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Musical notes floating like golden sparkles from the end of the bamboo flute into the open sky. Ranu's eyes wide with pure joy and wonder, Si Belo perking his ears up, naive folk art, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Kerbau yang Menghentikan Kunyahannya",
                    "titleEn": "The Buffalo Pauses Its Chew",
                    "textId": "Mendengar nada merdu itu, Si Belo berhenti mengunyah rumput seketika. Kepalanya terangkat dan telinganya tegak mengarah pada Ranu. Si Belo mendengus lembut penuh kepuasan, seolah mengakui bahwa musik sahabatnya telah lahir ke dunia.",
                    "textEn": "Hearing the sweet melody, Si Belo froze his chewing instantly. His head lifted, ears perking straight toward Ranu. Si Belo gave a low, contented huff, as if approving that his companion's music had officially entered the world.",
                    "quote": "Ketulusan musik mampu menyentuh naluri makhluk hidup di sekitar kita.",
                    "coReading": "Apa reaksi Si Belo saat mendengar nada pertama seruling Ranu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Si Belo the water buffalo tilting his head affectionately toward Ranu, listening intently with large round eyes. Ranu playing the flute with glowing cheeks, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Menutup dan Membuka Lubang Nada",
                    "titleEn": "Covering and Opening Note Holes",
                    "textId": "Ranu mencoba menutup satu lubang nada dengan ujung jari telunjuknya: suaranya berubah menjadi lebih rendah dan hangat. Ketika jari manisnya menutup lubang kedua: terciptalah melodi baru yang mengalun seperti kicauan burung kepodang di dahan asam.",
                    "textEn": "Ranu tried sealing one note hole with his index fingertip: the sound deepened into a warm, low hum. When his ring finger covered a second hole: a new melody trilled like an oriole singing on a tamarind bough.",
                    "quote": "Eksplorasi yang tekun membuka pintu bagi kekayaan kreasi baru.",
                    "coReading": "Bagaimana suara seruling berubah saat lubangnya ditutup jari?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Ranu's fingers dancing gracefully over the flute holes, playing a gentle melody. Hills rolling behind him under afternoon golden sun, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Senandung Senja Menggiring Pulang",
                    "titleEn": "Evening Lullaby Guiding Home",
                    "textId": "Matahari senja merona jingga di ufuk barat. Sambil menunggangi punggung Si Belo yang lebar dan hangat, Ranu meniup serulingnya mengalunkan lagu rakyat pengantar sore. Irama seruling itu menuntun kawanan ternak berjalan pulang ke kandang desa dengan damai.",
                    "textEn": "The evening sun blushed orange on the western horizon. Riding atop Si Belo's broad, warm back, Ranu blew his flute playing a pastoral folk tune. The flute's gentle rhythm guided grazing herds home to the village fold in tranquil harmony.",
                    "quote": "Musik yang damai membawa ketenangan bagi seluruh alam semesta.",
                    "coReading": "Di mana Ranu duduk saat meniup seruling sambil pulang ke desa?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Ranu sitting comfortably atop gentle water buffalo Si Belo, playing his yellow bamboo flute against a breathtaking sunset sky of peach and amber. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Seruling di Samping Bantal Tidur",
                    "titleEn": "The Flute Beside the Sleeping Pillow",
                    "textId": "Malam tiba dan seruling bambu berikat benang merah diletakkan rapi di meja samping ranjang Ranu. Di dalam bilik bambunya yang sejuk, Ranu tidur lelap berselimut sarung tenun. Di dalam mimpinya, nada-nada merdu serulingnya melayang di angkasa, menari bersama bintang-bintang malam yang berkilauan.",
                    "textEn": "Night fell and the bamboo flute tied with red cord lay neatly on Ranu's bedside table. Inside his cool bamboo room, Ranu slept deeply under a woven sarong. In his dreams, sweet flute notes floated across the sky, dancing with shimmering night stars.",
                    "quote": "Tidurlah dalam alunan nada kedamaian, ketekunanmu telah membuahkan harmoni indah.",
                    "coReading": "Mari pejamkan mata dan bayangkan alunan merdu seruling bambu meninabobokanmu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Ranu sleeping peacefully on a mattress under a checkered sarong. The yellow bamboo flute resting beside his pillow. Open window showing a smiling crescent moon and twinkling night sky over pastoral hills. Serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 90: Potongan Terakhir Puzzle Hutan ---
        {
            "id": "story90",
            "storyNumber": 90,
            "title": "Potongan Terakhir Puzzle Hutan",
            "englishTitle": "The Final Piece of the Forest Puzzle",
            "category": "perseverance",
            "categoryLabel": "🐢 Ketekunan & Rasa Percaya Diri",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kesabaran mencocokkan pola, ketelitian mata, & kebahagiaan menyelesaikan tugas",
            "cover": "covers/story90_cover.jpg",
            "synopsis": "Salma menyusun puzzle kayu bergambar hutan tropis dengan seratus kepingan di meja ruang tamu. Menjelang malam, tinggal satu keping terakhir yang hilang dan belum ditemukan. Dengan ketenangan dan bantuan kakek yang sabar, kepingan terakhir itu ditemukan terselip di bawah serbet meja, melengkapi gambar hutan dengan sempurna.",
            "protagonist": "Salma (Gadis cilik bertelunjuk teliti)",
            "companion": "Kakek Salma (Kakek tersenyum menyesap teh hangat)",
            "setting": "Meja Bundar Ruang Tamu",
            "pages": [
                {
                    "number": 1,
                    "title": "Kotak Puzzle Kayu Tebal",
                    "titleEn": "Sturdy Wooden Puzzle Box",
                    "textId": "Di atas meja bundar ruang tamu beralaskan taplak renda putih, Salma membuka kotak puzzle kayu bergambar 'Rimba Raya Satwa'. Di dalamnya terdapat puluhan kepingan kayu dengan lekukan dan tonjolan bergerigi yang saling menunggu untuk disatukan.",
                    "textEn": "On the round living room table draped in white lace cloth, Salma opened a wooden puzzle box titled 'The Great Jungle Realm'. Inside lay dozens of wooden jigsaw pieces with notched tabs and slots waiting to be united.",
                    "quote": "Tantangan besar terdiri dari banyak potongan kecil yang menanti ketelatenan kita.",
                    "coReading": "Apakah kamu suka bermain menyusun kepingan puzzle bergambar?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Salma, a young girl with pigtails and a cozy cardigan, sitting at a round wooden table pouring jigsaw puzzle pieces from a rustic wooden box. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Memilih Kepingan Bertepi Lurus",
                    "titleEn": "Sorting the Straight-Edged Pieces",
                    "textId": "Kakek yang sedang menyesap teh melati hangat memberi petunjuk bijak: 'Mulailah dari kepingan yang sisinya lurus dan rata, Salma. Itu adalah bingkai tepi yang akan memagari gambar hutanmu.' Salma memisahkan kepingan bertepi rata dengan jari-jarinya yang cekatan.",
                    "textEn": "Grandpa, sipping warm jasmine tea, offered wise guidance: 'Start with the pieces that have flat, straight edges, Salma. They form the border frame that will fence in your jungle picture.' Salma sorted the border pieces with nimble fingers.",
                    "quote": "Menata batas luar terlebih dahulu memberi kejelasan bagi isi di dalamnya.",
                    "coReading": "Mengapa kepingan bertepi lurus harus dipasang paling awal?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Salma sorting flat-edged puzzle pieces into a neat pile on the table. Grandpa in spectacles watching affectionately while holding a steaming teacup, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Bingkai Persegi yang Selesai",
                    "titleEn": "The Completed Rectangular Frame",
                    "textId": "'Klik, klik!' Suara kayu puzzle berpadu mantap. Dalam setengah jam, bingkai persegi panjang yang kokoh telah terpasang rapi di atas meja. Kini di tengah bingkai terhampar ruang kosong yang siap diisi oleh pepohonan, burung merak, dan harimau loreng ramah.",
                    "textEn": "'Click, snap!' The wooden pieces locked snugly. Within half an hour, a sturdy rectangular border stood complete on the table. Inside the frame now lay an open canvas ready to be filled with leafy boughs, peacocks, and friendly tigers.",
                    "quote": "Sebuah kerangka yang teratur memberi pijakan mantap bagi langkah berikutnya.",
                    "coReading": "Hewan apa saja yang akan muncul di dalam puzzle hutan Salma?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. The completed rectangular jigsaw border framing an empty space on the lace tablecloth. Salma clapping her hands gently in satisfaction, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Mencocokkan Pola Daun dan Bulu",
                    "titleEn": "Matching Leaf and Feather Patterns",
                    "textId": "Salma mengambil kepingan dengan corak bulu burung merak hijau toska. Ia memutar-mutar kepingan itu, mencari celah lekukan yang cocok di dekat dahan beringin. Ketika tonjolan kayu pas masuk ke dalam lubangnya, 'Pas!' Salma tersenyum puas.",
                    "textEn": "Salma picked a piece bearing turquoise peacock feather patterns. She rotated the piece, searching for the matching slot near the banyan branch. When the wooden tab slipped into place, 'Snug!' Salma smiled with delight.",
                    "quote": "Ketelitian mengamati detail kecil menghindarkan kita dari salah sangka.",
                    "coReading": "Bagaimana cara Salma mencocokkan kepingan yang tepat?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Close-up of Salma's small fingers pressing a wooden peacock puzzle piece into its matching slot. Vibrant colors of the jungle illustration forming, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Hutan yang Mulai Bernapas",
                    "titleEn": "The Forest Begins to Breathe",
                    "textId": "Keping demi keping bertaut sempurna. Muncul kawanan kera berayun di sulur anggur, gajah mini yang menyemprotkan air di sungai jernih, dan burung enggang berparuh kuning besar di pucuk pohon. Meja ruang tamu tampak semarak oleh kehidupan rimba.",
                    "textEn": "Piece by piece locked into place. Out came a troop of monkeys swinging on vine tendrils, a baby elephant spraying water in a clear creek, and a hornbill with a golden beak in the canopy. The table bustled with jungle life.",
                    "quote": "Ketekunan perlahan-lahan merajut bagian-bagian terpisah menjadi keutuhan yang memukau.",
                    "coReading": "Hewan apa yang sedang menyemprotkan air di sungai?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. The jungle puzzle almost fully assembled showing lush trees, monkeys, and an elephant. Salma leaning over with focused joy, simple black bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Satu Lubang yang Masih Kosong",
                    "titleEn": "One Remaining Empty Slot",
                    "textId": "Kini seluruh gambar hutan telah selesai, kecuali satu tempat! Tepat di dahan pohon tempat burung hantu tidur, ada lubang berbentuk bintang empat yang masih kosong melompong. Salma memeriksa meja dan kotak kayu, tetapi kepingan itu tidak ada di mana pun.",
                    "textEn": "Now the entire jungle scene was complete, except for one spot! Right on the branch where the sleeping owl rested, there remained an empty four-pointed gap. Salma searched the table and the wooden box, but the piece was nowhere to be seen.",
                    "quote": "Satu kekurangan kecil terkadang menguji batas kesabaran kita.",
                    "coReading": "Di bagian mana kepingan puzzle yang belum terpasang?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. The almost-finished puzzle with just one missing piece right where the owl's head should be. Salma looking puzzled with hand on cheek, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Pencarian Tenang Bersama Kakek",
                    "titleEn": "Calm Search with Grandpa",
                    "textId": "Salma hampir meneteskan air mata karena cemas. Kakek meletakkan cangkirnya dan berlutut di samping Salma. 'Tenanglah, Salma. Kepingan itu tidak punya sayap untuk terbang jauh. Mari kita periksa dengan hati yang sabar tanpa tergesa-gesa.'",
                    "textEn": "Salma nearly teared up with worry. Grandpa set his teacup down and knelt beside her. 'Peace, Salma. The piece has no wings to fly away. Let us search with patient hearts, calm and unhurried.'",
                    "quote": "Ketenangan pikiran adalah lentera terbaik di saat kita kehilangan sesuatu.",
                    "coReading": "Apa nasihat Kakek saat Salma mulai merasa panik?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Grandpa gently comforting Salma with a hand on her shoulder by the round table. Warm amber living room glow, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Terselip di Bawah Renda Taplak",
                    "titleEn": "Tucked Beneath the Lace Trim",
                    "textId": "Kakek dan Salma memeriksa kolong meja dan sela-sela karpet. Tiba-tiba tangan Salma menyentuh sesuatu yang keras di bawah lipatan serbet renda meja. 'Kakek, ini dia!' seru Salma girang. Di tangannya terpegang kepingan kayu bergambar wajah burung hantu bermata bulat ramah.",
                    "textEn": "Grandpa and Salma checked beneath the table and carpet edges. Suddenly Salma's fingers brushed something firm under a folded lace napkin. 'Grandpa, here it is!' Salma cheered with glee. In her hand rested the missing wooden piece showing the round, friendly face of the owl.",
                    "quote": "Apa yang dicari dengan sabar selalu menanti untuk ditemukan pada saat yang tepat.",
                    "coReading": "Di mana kepingan terakhir itu bersembunyi?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Salma lifting the edge of the lace napkin to reveal the missing puzzle piece with the cute owl face. Her face glowing with joyful relief, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Menutup Gambar yang Sempurna",
                    "titleEn": "Completing the Perfect Picture",
                    "textId": "Dengan tangan bergetar bahagia, Salma meletakkan kepingan terakhir itu ke tempatnya. 'Klik!' Suaranya pas mengunci celah kosong. Burung hantu rimba kini tersenyum manis di dahan beringin. Gambar hutan raya itu telah utuh, indah, dan sempurna tanpa cela.",
                    "textEn": "With hands trembling with joy, Salma lowered the final piece into place. 'Click!' It snapped snugly into the empty gap. The jungle owl now smiled sweetly on the banyan branch. The grand jungle picture was whole, breathtaking, and complete.",
                    "quote": "Ketekunan yang tak kenal menyerah selalu ditutup dengan kebahagiaan paripurna.",
                    "coReading": "Bagaimana perasaan Salma ketika puzzle-nya akhirnya utuh?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Salma pressing the final puzzle piece into place with both thumbs, smiling proudly. The finished jungle picture glowing on the wooden table, Grandpa nodding with broad smile, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Menjelajahi Rimba Raya",
                    "titleEn": "Dreams of Exploring the Great Jungle",
                    "textId": "Malam tiba dan lampu gantung ruang tamu dimatikan. Puzzle rimba raya Salma dibiarkan terbentang megah di atas meja. Di kamarnya yang nyaman, Salma tidur pulas dipeluk selimut wolnya, bermimpi menjelajahi hutan lebat yang ramah bersama burung hantu sahabat setianya.",
                    "textEn": "Night fell and the living room chandelier switched off. Salma's great jungle puzzle remained proudly assembled on the table. In her cozy room, Salma slept deeply wrapped in her woolen quilt, dreaming of trekking through friendly wild woods alongside her faithful owl companion.",
                    "quote": "Tidurlah dalam kepuasan jiwa yang tenang, karya indahmu telah selesai sempurna.",
                    "coReading": "Mari pejamkan mata dan bayangkan kamu tidur di hutan dongeng yang damai.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Salma sleeping peacefully in bed with a quilt. On her bedside table, a wooden toy owl sits watching over her. Moonlit room with starry sky outside the window, serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 91: Gerakan Kaki Gaya Katak ---
        {
            "id": "story91",
            "storyNumber": 91,
            "title": "Gerakan Kaki Gaya Katak",
            "englishTitle": "Frog-Style Kicking",
            "category": "perseverance",
            "categoryLabel": "🐢 Ketekunan & Rasa Percaya Diri",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Keberanian belajar berenang, menirukan alam, & ketekunan latihan",
            "cover": "covers/story91_cover.jpg",
            "synopsis": "Reza merasa takut saat belajar berenang di kolam dangkal; kakinya selalu kaku dan tubuhnya tenggelam. Pelatih ramah mengajaknya membayangkan katak hijau yang melompat di danau teratai: tekuk lutut, tendang melebar, dan rapatkan lurus. Dengan sabar, Reza akhirnya meluncur mulus di atas permukaan air.",
            "protagonist": "Reza (Anak laki-laki berkacamata renang biru)",
            "companion": "Pelatih Katak (Pelatih ramah memegang papan apung)",
            "setting": "Kolam Renang Dangkal",
            "pages": [
                {
                    "number": 1,
                    "title": "Air Biru yang Dingin di Kolam Dangkal",
                    "titleEn": "Cool Blue Water in the Shallow Pool",
                    "textId": "Di tepi kolam renang anak yang berlantai keramik biru muda, Reza berdiri memegang tangga besi dengan kedua tangannya. Reza mengenakan kacamata renang biru laut dan celana renang bergaris kuning. Air kolam yang sejuk berdesir menyentuh jemari kakinya.",
                    "textEn": "At the edge of the shallow children's pool with light blue tiles, Reza stood holding the stainless ladder railings with both hands. Reza wore ocean-blue goggles and yellow-striped swim trunks. The cool pool water rippled softly against his toes.",
                    "quote": "Langkah pertama memasuki hal baru membutuhkan keberanian untuk percaya.",
                    "coReading": "Pernahkah kamu berenang dan merasakan dinginnya air kolam?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Reza, a young boy in blue goggles and swim shorts, standing on the shallow steps of a sunny pool dipping his toes in the water. Gentle water ripples, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Papan Apung Busa Jingga",
                    "titleEn": "Orange Foam Kickboard",
                    "textId": "Pak Budi, pelatih renang yang bertubuh tegap dan ramah, mengulurkan sebuah papan apung dari busa tebal berwarna jingga cerah. 'Pegang papan ini di depan dadamu, Reza. Papan ini akan menjagamu tetap mengapung seperti perahu gabus,' senyum Pak Budi.",
                    "textEn": "Coach Budi, a kind and sturdy swim instructor, offered a thick, bright orange foam kickboard. 'Hold this board before your chest, Reza. It will keep you floating high like a cork raft,' Coach Budi smiled.",
                    "quote": "Alat bantu yang tepat memberi rasa aman untuk belajar hal yang menantang.",
                    "coReading": "Untuk apa papan pelampung busa digunakan saat belajar renang?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Kind swim coach standing in waist-deep clear water handing an orange foam kickboard to Reza. Sunlight sparkling on pool surface, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Kaki yang Terlalu Kaku",
                    "titleEn": "Stiff Legs and Heavy Water",
                    "textId": "Reza memegang papan pelampung dan mulai menendang-nendang air. Namun karena cemas, kedua kaki Reza kaku seperti tongkat kayu. Tendangannya hanya membuat cipratan air ke mana-mana tanpa membuat tubuhnya meluncur maju. Kaki Reza perlahan turun menyentuh dasar kolam.",
                    "textEn": "Reza gripped the kickboard and kicked. But tense with worry, his legs stayed stiff as wooden sticks. His splashing only kicked up white spray without gliding him forward. His feet slowly dragged down toward the pool bottom.",
                    "quote": "Kekakuan tubuh adalah cerminan dari pikiran yang masih memegang rasa takut.",
                    "coReading": "Mengapa tubuh Reza tidak meluncur saat kakinya kaku?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Reza in the pool splashing water unevenly with straight stiff legs, looking slightly frustrated through his goggles. Coach observing patiently beside him, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Pelajaran dari Katak di Daun Teratai",
                    "titleEn": "Lesson from the Lily Pad Frog",
                    "textId": "Pak Budi mengajak Reza duduk sejenak di undakan kolam. 'Reza, pernahkah kamu melihat katak berenang di kolam teratai? Katak tidak menendang lurus seperti menendang bola. Katak menekuk kakinya, membuka telapak kakinya ke samping, lalu mendorong air ke belakang.'",
                    "textEn": "Coach Budi brought Reza to sit briefly on the pool ledge. 'Reza, have you watched frogs swim in lily ponds? A frog does not kick stiff like kicking a soccer ball. A frog bends its knees, flares its feet out wide, then snaps water backward.'",
                    "quote": "Alam semesta adalah guru terhebat bagi setiap gerak ketangkasan.",
                    "coReading": "Bagaimana gerakan kaki katak saat berenang di danau?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Coach Budi demonstrating frog leg motions with his hands while sitting on the tiled pool edge. Reza listening attentively with goggles pushed up on his forehead, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Jurus Tiga Irama: Tekuk, Buka, Rapatkan!",
                    "titleEn": "The Three-Count Rhythm: Bend, Flare, Snap!",
                    "textId": "Pak Budi mengajarkan irama tiga ketukan: 'Satu... tekuk tumit ke arah pantat. Dua... buka telapak kaki ke samping. Tiga... tendang melingkar dan rapatkan lurus: wuuush!' Reza menirukan gerakan itu di udara beberapa kali hingga hafal.",
                    "textEn": "Coach Budi taught a three-beat rhythm: 'One... bend heels toward your seat. Two... flare feet wide sideways. Three... snap circular and glide straight: whoosh!' Reza rehearsed the motion in the air until his muscles remembered.",
                    "quote": "Membagi gerakan sulit menjadi langkah-langkah kecil membuatnya mudah dikuasai.",
                    "coReading": "Bisakah kamu menirukan irama: tekuk, buka, lalu rapatkan?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Reza lying prone on the poolside deck practicing the three-step frog leg kick motions with coach guiding his ankles gently. Sunlight reflecting on water tiles, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Meluncur dengan Dorongan Melingkar",
                    "titleEn": "Gliding on a Circular Thrust",
                    "textId": "Reza kembali masuk ke dalam air. Ia memegang papan busa jingganya, menarik napas panjang, dan membenamkan dagunya di atas permukaan air. 'Tekuk... buka... tendang rapat!' dorongan melingkar kakinya seketika melontarkan tubuh Reza meluncur mulus ke depan!",
                    "textEn": "Reza slipped back into the cool water. Gripping his orange kickboard, he took a deep breath and dipped his chin near the surface. 'Bend... flare... snap!' his circular leg thrust instantly shot him gliding smoothly forward!",
                    "quote": "Dorongan yang tepat melahirkan luncuran yang seringan angin.",
                    "coReading": "Apa yang dirasakan Reza saat tendangan kakinya berhasil mendorong air?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Underwater view showing Reza's legs kicking in a perfect circular frog-stroke, sending gentle swirl bubbles behind him. Body gliding effortlessly across clear turquoise pool, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Gelembung-Gelembung Air yang Riang",
                    "titleEn": "Bubbles of Joy in the Water",
                    "textId": "Melalui kaca matanya, Reza melihat butiran gelembung udara berkilauan berputar di belakang kakinya seperti jejak bintang perak. Reza mengulangi gerakan itu: tekuk, buka, rapatkan! Tubuhnya meluncur semakin jauh melintasi kolam dangkal tanpa rasa takut lagi.",
                    "textEn": "Through his goggles, Reza saw silver air bubbles swirling behind his heels like shooting stars. He repeated the cadence: bend, flare, snap! His body surged farther across the pool without any lingering fear.",
                    "quote": "Rasa percaya diri tumbuh subur saat kita merasakan kemajuan diri sendiri.",
                    "coReading": "Lihatlah gelembung-gelembung air di belakang kaki Reza!",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Reza swimming forward smoothly with the orange kickboard, kicking up sparkling white froth behind his feet. Face beaming under his blue goggles, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Sentuhan di Tepi Kolam",
                    "titleEn": "Touching the Far Pool Wall",
                    "textId": "'Tap!' Papan jingga Reza menyentuh dinding seberang kolam. Reza menegakkan tubuhnya dan melepaskan kacamata renangnya ke dahi. Air menetes segar di hidungnya. Pak Budi bertepuk tangan dari kejauhan: 'Luar biasa, Reza! Kamu berenang secepat katak juara!'",
                    "textEn": "'Tap!' Reza's orange board tapped the far pool wall. Reza stood up on his feet and lifted his goggles to his forehead. Water trickled refreshingly down his nose. Coach Budi clapped from the edge: 'Superb, Reza! You swim swift as a champion frog!'",
                    "quote": "Pencapaian tujuan manis diraih lewat ketekunan yang pantang menyerah.",
                    "coReading": "Apakah Reza berhasil sampai ke tepi seberang kolam renang?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Reza standing in the pool at the far edge, raising the kickboard high with a triumphant smile, water droplets glistening on his cheeks. Coach giving two thumbs up, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Handuk Hangat dan Senyuman Ibu",
                    "titleEn": "Warm Towel and Mother's Smile",
                    "textId": "Ibu menyambut Reza di tepi kolam dengan handuk katun kuning tebal yang harum semerbak. Ibu membungkus tubuh Reza yang basah menjadi bungkusan hangat seperti boneka beruang. 'Ibu melihatmu meluncur tadi, Reza. Hebat sekali tendangan katakmu!' puji Ibu sambil memeluknya.",
                    "textEn": "Mother greeted Reza at the poolside with a thick, fragrant yellow cotton towel. She bundled his damp shoulders into a cozy hug like a little bear. 'I watched you glide, Reza. Your frog kicks were magnificent!' Mother praised, holding him tight.",
                    "quote": "Kehangatan pelukan keluarga melipatgandakan rasa bahagia atas keberhasilan.",
                    "coReading": "Bagaimana rasanya dibungkus handuk tebal sehabis berenang?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother wrapping Reza in a fluffy yellow hooded bath towel on the poolside bench, kissing his damp forehead. Warm afternoon light, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Lelap Melayang di Air Tenang",
                    "titleEn": "Deep Slumber Floating on Still Waters",
                    "textId": "Malam tiba dan tubuh Reza terasa lelah namun sangat segar dan rileks. Kacamata renang birunya tergantung rapi di samping pintu kamar. Di atas ranjangnya yang empuk, Reza tidur pulas di bawah selimut biru mudanya, bermimpi berenang meluncur bebas di danau teratai berair jernih di bawah sinar rembulan.",
                    "textEn": "Night arrived and Reza's body felt pleasantly weary yet fresh and calm. His blue goggles hung neatly by the bedroom door. On his plush mattress, Reza slept deeply beneath a baby-blue duvet, dreaming of gliding freely across clear lily ponds under moonlit skies.",
                    "quote": "Tidurlah dalam kebebasan yang tenang, ketekunanmu telah memberimu sayap di dalam air.",
                    "coReading": "Mari pejamkan mata dan rasakan tubuhmu melayang ringan di atas kasur empuk.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Reza sleeping serenely in bed with a blue blanket. Blue goggles resting on his nightstand. Dream cloud showing a friendly little green frog swimming among floating water lilies under a starry night sky. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 92: Jahitan Lurus di Kain Wol ---
        {
            "id": "story92",
            "storyNumber": 92,
            "title": "Jahitan Lurus di Kain Wol",
            "englishTitle": "Straight Stitches on Woolen Cloth",
            "category": "perseverance",
            "categoryLabel": "🐢 Ketekunan & Rasa Percaya Diri",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kesabaran menyulam, ketelitian tangan, & kasih sayang antargenerasi",
            "cover": "covers/story92_cover.jpg",
            "synopsis": "Alya ingin membuat tatakan cangkir teh untuk Nenek menggunakan selembar kain felt wol hijau dan benang kuning. Awalnya jahitan Alya miring-miring dan benangnya kusut berulang kali. Dengan bimbingan sabar Nenek di kursi goyang, Alya belajar mengatur jarak jahitan hingga lurus dan rapi.",
            "protagonist": "Alya (Gadis kecil berjarum plastik tumpul)",
            "companion": "Nenek Alya (Nenek sabar membimbing tangan cucunya)",
            "setting": "Kursi Goyang Sudut Ruang",
            "pages": [
                {
                    "number": 1,
                    "title": "Keranjang Anyaman Penuh Benang Wol",
                    "titleEn": "Woven Basket Full of Wool Yarn",
                    "textId": "Di sudut ruang keluarga dekat perapian yang hangat, Nenek duduk di kursi goyang kayunya. Di samping kursi Nenek, tergeletak sebuah keranjang anyaman pandan besar berisi gulungan benang wol warna-warni, gunting bordir antik, dan lembaran kain felt lembut beraneka rupa.",
                    "textEn": "In the corner of the family room near the warm hearth, Grandma sat in her wooden rocking chair. Beside her chair rested a large woven pandan basket overflowing with colorful skeins of yarn, antique embroidery scissors, and soft felt swatches.",
                    "quote": "Sudut kerajinan tangan menyimpan kehangatan dari generasi ke generasi.",
                    "coReading": "Pernahkah kamu melihat nenek atau ibumu sedang menjahit pakaian?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Alya, a sweet little girl in an embroidered pinafore dress, sitting on a round footstool beside Grandma in her wooden rocking chair. Sewing basket with colorful yarn balls, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Jarum Plastik Berujung Tumpul",
                    "titleEn": "Blunt-Tipped Plastic Needle",
                    "textId": "Nenek memberikan sebatang jarum jahit plastik berwarna merah muda dengan lubang benang yang besar dan ujung yang bulat tumpul. Jarum ini aman untuk jemari mungil Alya. Alya memegang selembar kain felt wol hijau tua berbentuk persegi empat.",
                    "textEn": "Grandma handed over a pink plastic yarn needle with a wide eye and a round, blunt safety tip. It was safe for Alya's little fingers. Alya held a square piece of forest-green woolen felt.",
                    "quote": "Alat yang aman dan ramah memberi ketenangan saat belajar keterampilan pertama.",
                    "coReading": "Mengapa jarum jahit untuk anak-anak harus berujung tumpul?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up of Alya holding a large blunt pink plastic needle threaded with sunny yellow yarn over a square piece of green felt. Simple bead dot eyes, naive folk art, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Memasukkan Benang ke Lubang Jarum",
                    "titleEn": "Threading the Needle's Eye",
                    "textId": "Alya membasahi sedikit ujung benang wol kuningnya dengan ujung jarinya, lalu membidiknya ke lubang jarum merah muda. Dengan satu hembusan napas tertahan, 'Pluk!' ujung benang lolos menembus lubang. Nenek tersenyum dan membantu membuatkan simpul di ujung benang.",
                    "textEn": "Alya smoothed the tip of her yellow wool yarn with her fingertip, aiming carefully at the pink needle's eye. With a breath held still, 'Slip!' the thread slipped through. Grandma smiled, helping knot the yarn end firmly.",
                    "quote": "Ketelitian kecil melatih konsentrasi mata dan kelenturan jemari.",
                    "coReading": "Bisakah kamu memusatkan pandangan untuk memasukkan benang ke lubang jarum?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Alya's face filled with intense, cute concentration as she threads the yellow yarn through the pink needle eye. Grandma watching encouragingly, cozy room lighting, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Tusukan Pertama yang Miring",
                    "titleEn": "The First Crooked Stitches",
                    "textId": "Alya menusukkan jarum dari bawah kain felt dan menarik benangnya ke atas. Namun tusukan keduanya melompat terlalu jauh ke samping, dan tusukan ketiganya miring ke sudut kain. Garis jahitan kuning itu tampak berliku-liku seperti jejak cacing tanah yang bingung.",
                    "textEn": "Alya poked the needle up through the felt and drew the yarn tight. But her second stitch hopped too far sideways, and her third stitch angled crookedly toward the corner. The yellow line wandered like a puzzled earthworm trail.",
                    "quote": "Awal yang berliku adalah langkah pertama dari setiap proses belajar.",
                    "coReading": "Apakah jahitan pertama Alya sudah lurus atau masih berliku-liku?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Detailed view of the green felt square showing three crooked, uneven yellow stitches. Alya looking down with a slightly disappointed pout, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Benang Kusut yang Menahan Langkah",
                    "titleEn": "Tangled Threads Holding Up the Stride",
                    "textId": "Saat Alya menarik jarum untuk tusukan keempat, benang wol di bagian bawah kain tersangkut dan menggulung menjadi simpul kusut. Jarum tidak bisa ditarik maju maupun mundur. Alya meletakkan kainnya dengan helaan napas panjang.",
                    "textEn": "As Alya pulled the needle for her fourth stitch, the wool beneath bunched into a tangled knot. The needle would neither pull forward nor slip back. Alya set her felt down with a long, heavy sigh.",
                    "quote": "Kesulitan hadir untuk melatih kesabaran jiwa kita.",
                    "coReading": "Apa yang terjadi pada benang jahit Alya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Alya leaning back against Grandma's knee with a discouraged face as Grandma gently untangles the yellow wool yarn underneath the green felt. Warm hearth glow, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Sentuhan Lembut Tangan Nenek",
                    "titleEn": "Grandma's Gentle Touch",
                    "textId": "Nenek mengurai simpul kusut itu dengan kesabaran luar biasa. Kursi goyang Nenek berderit tenang: 'Krik, krik...' Nenek membimbing tangan Alya: 'Alya sayang, menjahit itu seperti melangkah di pematang sawah. Berilah jarak selebar sebutir beras di antara setiap tusukan jarum.'",
                    "textEn": "Grandma untangled the messy knot with extraordinary patience. Her rocking chair creaked soothingly: 'Creak, sway...' Grandma cradled Alya's hands: 'Sweet Alya, sewing is like strolling along a garden path. Leave a rice-grain's distance between each gentle needle stitch.'",
                    "quote": "Bimbingan yang sabar mengurai setiap kekusutan di hati maupun di tangan.",
                    "coReading": "Nasihat apa yang diberikan Nenek agar jahitan Alya rapi?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Grandma's loving hands resting over Alya's hands, gently guiding the pink needle through the green felt cloth. Warm, tender intergenerational moment, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Irama Jahitan: Naik dan Turun",
                    "titleEn": "Rhythm of Stitches: Up and Down",
                    "textId": "Alya menarik napas dalam-dalam dan tersenyum. Bersama Nenek yang bersenandung pelan, Alya menusukkan jarum: 'Masuk dari bawah... tarik lembut... tusuk ke atas... tarik tenang.' Satu demi satu jahitan kuning berjajar rapi di sepanjang tepi kain felt hijau.",
                    "textEn": "Alya took a deep breath and smiled. To Grandma's gentle humming, Alya dipped the needle: 'In from beneath... pull soft... pierce from above... draw calm.' One by one, neat yellow stitches marched in a straight row along the green felt edge.",
                    "quote": "Keteraturan lahir saat kita menikmati setiap hembusan napas dalam bekerja.",
                    "coReading": "Bisakah kamu menirukan irama tusukan jarum: naik, turun, naik, turun?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Alya stitching with steady confidence, a neat straight yellow dashed line forming perfectly along the edge of the dark green felt square. Grandma smiling warmly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Tatakan Cangkir Berhias Bintang",
                    "titleEn": "Star-Bordered Tea Coaster",
                    "textId": "Keempat sisi kain felt hijau kini telah terjahit rapi dengan benang kuning yang berkilau seperti untaian bintang emas. Di sudut kain, Alya membuat satu silang jahitan kecil berbentuk bunga melati. Tatakan cangkir teh buatan tangan Alya telah selesai sempurna!",
                    "textEn": "All four sides of the green felt were now bordered with yellow stitches gleaming like golden star garlands. In the corner, Alya made a tiny crossed stitch shaped like a jasmine blossom. Alya's handmade tea coaster was completely finished!",
                    "quote": "Karya yang diselesaikan dengan kesabaran memancarkan keindahan sejati.",
                    "coReading": "Benda apa yang berhasil dibuat oleh Alya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. The completed square green felt coaster with neat yellow border stitching and a tiny corner floral stitch displayed proudly on the wooden table. Alya holding it up beaming, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Secangkir Teh Hangat di Atas Karya Alya",
                    "titleEn": "Warm Tea Upon Alya's Creation",
                    "textId": "Nenek meletakkan cangkir keramik teh melatinya yang mengepul hangat tepat di atas tatakan kain buatan Alya. 'Lihat, Alya. Meja Nenek terlindung dari panas, dan setiap kali Nenek minum teh, Nenek akan selalu mengingat ketekunan cucu kesayangan Nenek.' Nenek mengecup pipi Alya penuh haru.",
                    "textEn": "Grandma set her steaming ceramic cup of jasmine tea right atop Alya's handmade felt coaster. 'Look, Alya. My table is shielded from heat, and whenever I sip tea, I will cherish my sweet granddaughter's patience.' Grandma kissed Alya's cheek with tender joy.",
                    "quote": "Karya yang bermanfaat bagi orang tersayang adalah hadiah termanis di dunia.",
                    "coReading": "Bagaimana perasaan Nenek saat cangkir tehnya beralaskan karya Alya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Steaming ceramic teacup resting on the handmade green and yellow felt coaster on a rustic wooden side table. Grandma hugging Alya affectionately in the rocking chair, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi di Bawah Selimut Rajutan",
                    "titleEn": "Dreams Beneath the Knitted Quilt",
                    "textId": "Malam tiba dan perapian keluarga meredup menjadi bara merah yang hangat. Alya tidur lelap di bawah selimut rajut Nenek, dengan jemari tangannya yang mungil beristirahat damai. Di dalam mimpinya, benang-benang kuning emas merajut jembatan pelangi yang menghubungkan bumi dengan bintang-bintang di langit malam.",
                    "textEn": "Night arrived and the hearth settled into warm, glowing embers. Alya slept deeply beneath Grandma's knitted quilt, her little fingers resting peacefully. In her dreams, golden yellow threads wove rainbow bridges connecting earth with twinkling stars in the night sky.",
                    "quote": "Tidurlah dalam kehangatan cinta, ketekunanmu hari ini adalah bekal indah bagi masa depanmu.",
                    "coReading": "Mari pejamkan mata dan bayangkan benang-benang cinta memeluk tidurmu malam ini.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Alya sleeping peacefully in a cozy wooden bedroom under a colorful knitted blanket. Soft moonlight pouring through the window with a gentle crescent moon outside. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
