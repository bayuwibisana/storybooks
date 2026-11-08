# scripts/polish_stories_58_to_62.py
import json

def get_stories_58_to_62():
    stories = []

    # =========================================================================
    # STORY 58: Bahasa Isyarat Ekor Tupai
    # =========================================================================
    s58 = {
        "id": "bahasa-isyarat-tupai",
        "storyNumber": 58,
        "title": "Bahasa Isyarat Ekor Tupai",
        "englishTitle": "The Squirrel's Tail Sign Language",
        "category": "persahabatan",
        "categoryLabel": "🤝 Persahabatan & Inklusivitas",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Memahami dan menghargai teman yang berkomunikasi dengan cara berbeda",
        "cover": "images/story58_cover.jpg",
        "coverImage": "images/story58_cover.jpg",
        "synopsis": "Sasa si tupai kecil tidak bisa bersuara, tetapi ia memiliki ekor lebat indah yang bisa meliuk-liuk membentuk berbagai tanda ramah. Bersama Beni si kelinci yang sabar memperhatikan, mereka menciptakan bahasa isyarat rahasia yang membuktikan bahwa persahabatan tidak membutuhkan kata-kata terucap untuk saling mengerti.",
        "synopsisEn": "Little Sasa the squirrel cannot speak with words, but has a magnificent fluffy tail that wiggles and twirls in cheerful signs. With patient Beni the bunny, they invent a secret sign language proving that true friendship needs no spoken words to understand each other.",
        "protagonist": "Sasa (Tupai kecil berbulu karamel berekor lebat dengan pita daun hijau)",
        "companion": "Beni (Kelinci putih bertelinga panjang yang pendengar setia)",
        "setting": "Dahan Pohon Kenari Berlumut di Tengah Hutan Ramah",
        "pages": [
            {
                "number": 1,
                "title": "Tupai Kecil Tanpa Suara",
                "titleEn": "The Little Silent Squirrel",
                "textId": "Di Hutan Hazel, tupai-tupai lain gemar bercicit riang: cit-cit-cit! Namun Sasa si tupai kecil selalu diam. Pita suaranya sunyi sejak lahir, tetapi kedua matanya berbinar cerdas dan ekor lebatnya bergerak lincah menari.",
                "textEn": "In Hazel Woods, other squirrels loved chattering merrily: chirp-chirp-squeak! But little Sasa was always silent. Her voice had been quiet since birth, yet her bead eyes shone with bright curiosity and her fluffy tail danced with lively grace.",
                "quote": "🐿️ 'Keheningan tidak pernah mengurangi keindahan isi hati seseorang.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu berbicara dengan teman hanya menggunakan gerakan tangan dan senyuman?",
                "imagePrompt": "Charming children's book illustration of little caramel squirrel Sasa sitting quietly on a mossy walnut branch, hugging her fluffy bushy tail adorned with a green leaf ribbon. Soft morning forest sunlight, handcrafted wax crayon and oil pastel on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Beni si Kelinci yang Sabar Menatap",
                "titleEn": "Beni the Patient Bunny",
                "textId": "Beni si kelinci putih melompat ke dahan rendah di samping Sasa. Beni tidak buru-buru mengajak bicara; ia duduk tenang, memasang telinga panjangnya, dan menatap Sasa dengan senyuman yang hangat dan penuh kesabaran.",
                "textEn": "Beni the white bunny hopped onto the low branch beside Sasa. Beni never rushed to talk; he sat peacefully, perking his long soft ears, looking at Sasa with a patient, welcoming smile.",
                "quote": "🐇 'Kesabaran mendengarkan dengan mata adalah bentuk kasih sayang yang tulus.'",
                "coReading": "💡 Aktivitas Seru: Pasang kedua telapak tanganmu di atas kepala seperti telinga kelinci yang menyimak!",
                "imagePrompt": "A gentle storybook illustration of white bunny Beni sitting comfortably next to squirrel Sasa on a tree bough, smiling affectionately, leaves rustling in soft breeze, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Gerakan Ekor Melengkung: Selamat Pagi!",
                "titleEn": "Curling Tail Motion: Good Morning!",
                "textId": "Sasa melompat riang. Ekor lebatnya melengkung ke atas membentuk huruf C yang membusur anggun, lalu dikibaskan dua kali: wus, wus! Beni tersenyum mengangguk: \"Artinya... Selamat pagi, kawan! Benar, kan?\"",
                "textEn": "Sasa hopped with glee. Her bushy tail curled upward into a graceful C-shape arch, waving twice gently: swish, swish! Beni nodded with a grin: \"That means... Good morning, dear friend! Am I right?\"",
                "quote": "🌤️ 'Setiap sapaan yang tulus selalu tersampaikan dengan jelas, bagaimana pun caranya.'",
                "coReading": "💡 Aktivitas Seru: Lambaikan tanganmu dua kali sambil tersenyum menyapa teman di depanmu!",
                "imagePrompt": "Whimsical children's picture book scene of Sasa arching her fluffy tail into a graceful curve like an umbrella, with bunny Beni clapping his paws in happy understanding, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Kibasan Cepat: Ayo Main!",
                "titleEn": "Brisk Flutters: Let's Play!",
                "textId": "Sasa kemudian mengibaskan ujung ekornya ke kiri dan ke kanan dengan cepat: kit-kat-kit-kat! Lalu ia menunjuk ke arah ayunan akar gantung beringin. Beni langsung paham: \"Ayo kita berayun bersama!\"",
                "textEn": "Sasa then fluttered the tip of her tail left and right briskly: flick-flack-flick! Then she pointed her paw toward the swinging banyan vine. Beni understood instantly: \"Let's go swing together!\"",
                "quote": "🎋 'Bermain bersama tidak membutuhkan aturan rumit, cukup kegembiraan yang tulus.'",
                "coReading": "💡 Tanya si Kecil: Permainan apa yang paling ingin kamu mainkan bersama sahabatmu hari ini?",
                "imagePrompt": "Playful illustration of squirrel Sasa and bunny Beni swinging gently on hanging green vines in the forest, their faces full of innocent laughter, warm dappled light, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Ekor Meringkuk: Hati-Hati, Ranting Licin!",
                "titleEn": "Curled In Tail: Careful, Slippery Twig!",
                "textId": "Saat melintasi dahan yang basah oleh embun, Sasa melingkarkan ekornya rapat-rapat ke perutnya dan berjalan berjingkat. Beni memperhatikan tanda itu dan memperlambat langkahnya. Tak ada yang terpeleset.",
                "textEn": "When crossing a branch damp with dewdrops, Sasa tucked her tail tightly around her belly and tiptoed with extreme caution. Beni noticed the sign and slowed his hops. Nobody slipped or stumbled.",
                "quote": "🛡️ 'Sahabat yang peduli selalu memberi tanda peringatan agar kita tetap aman.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana caramu mengingatkan teman agar berhati-hati saat berjalan di lantai licin?",
                "imagePrompt": "Storybook scene of Sasa tiptoeing carefully across a damp mossy log, tail tucked protective, with Beni following closely behind in careful balance, soft forest greens, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Mengetuk Biji Kenari: Lapar!",
                "titleEn": "Tapping the Walnut: Hungry!",
                "textId": "Siang hari, Sasa mengetuk dua biji kenari bersamaan: tak-tak! Lalu mengelus perutnya yang bulat. Beni tertawa renyah, \"Kamu lapar ya, Sasa? Aku membawa bekal wortel manis dan kacang hazel untuk kita berdua!\"",
                "textEn": "At midday, Sasa tapped two shiny walnuts together: clack-clack! Then she patted her round tummy. Beni laughed merrily, \"You're hungry, aren't you, Sasa? I brought sweet carrots and hazelnuts for both of us!\"",
                "quote": "🌰 'Berbagi bekal membuat setiap isyarat lapar terjawab dengan kehangatan.'",
                "coReading": "💡 Aktivitas Seru: Ketuk dua jari tanganmu seperti bunyi biji kenari: 'Tak-tak, waktunya makan!'",
                "imagePrompt": "Charming illustration of Sasa and Beni sitting on a hollow log sharing hazelnuts and carrot slices from a leaf pouch, smiling affectionately, wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Kawan-Kawan Lain Ikut Belajar",
                "titleEn": "Other Friends Learn the Signs",
                "textId": "Melihat betapa akrabnya Sasa dan Beni, burung gelatik dan musang kecil ikut bertengger di dahan. Mereka ingin belajar bahasa ekor Sasa. Sasa dengan sabar mengajari mereka tanda-tanda untuk 'senang', 'terima kasih', dan 'sahabat'.",
                "textEn": "Seeing how wonderfully Sasa and Beni understood each other, the little finch and baby badger hopped onto the bough. They wanted to learn Sasa's tail language too. Patiently, Sasa taught them signs for 'happy', 'thank you', and 'friend'.",
                "quote": "🤝 'Saat kita mau belajar bahasa orang lain, lingkaran persahabatan akan semakin meluas.'",
                "coReading": "💡 Tanya si Kecil: Senang rasanya jika semua teman di kelas bisa bermain bersama tanpa terkecuali, bukan?",
                "imagePrompt": "Heartwarming children's book scene of diverse woodland creatures (finch, badger, bunny) sitting in a semicircle around squirrel Sasa, playfully imitating her tail gestures with their paws and wings, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Ekor Membentuk Hati: Aku Sayang Kamu",
                "titleEn": "Tail Forms a Heart: I Love You",
                "textId": "Sebagai tanda terima kasih, Sasa melengkungkan ujung ekornya dan memadukannya dengan lengkungan daun pakis, membentuk pola hati yang manis di udara. Semua kawan tersenyum dan berpelukan hangat.",
                "textEn": "As a token of gratitude, Sasa curved the tip of her bushy tail alongside a looping fern frond, creating a sweet heart shape in the sunlit air. All her companions smiled and shared a warm, fuzzy group hug.",
                "quote": "💖 'Cinta dan kasih sayang tidak membutuhkan suara keras untuk dirasakan dengan mendalam.'",
                "coReading": "💡 Bentuk Hati: Buatlah bentuk hati dengan jari telunjuk dan jempolmu bersama si kecil!",
                "imagePrompt": "Touching illustration of squirrel Sasa using her tail to curve into a heart shape against the golden evening light, with Beni and other forest friends smiling warmly, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Senja Tenang di Pucuk Pohon",
                "titleEn": "Quiet Sunset at the Treetop",
                "textId": "Matahari sore tenggelam perlahan di balik bukit kenari, memancarkan sinar aprikot keemasan. Sasa dan Beni duduk berdampingan di pucuk dahan tertinggi, menikmati semilir angin senja dalam keheningan yang penuh rasa syukur.",
                "textEn": "The evening sun sank gently behind the walnut hills, casting a blanket of apricot gold. Sasa and Beni sat shoulder-to-shoulder on the highest bough, drinking in the twilight breeze in grateful, companionable silence.",
                "quote": "🌄 'Duduk dalam diam bersama sahabat sejati terasa begitu nyaman dan menenteramkan.'",
                "coReading": "💡 Tanya si Kecil: Siapa sahabat yang paling membuatmu merasa tenang saat berada di dekatnya?",
                "imagePrompt": "Picturesque storybook scene of squirrel Sasa and bunny Beni silhouetted against a magnificent sunset sky of peach, violet, and amber, sitting side by side on a high tree branch, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Nyenyak Diselimuti Ekor Sendiri",
                "titleEn": "Sound Sleep Wrapped in Her Own Tail",
                "textId": "Di dalam sarang lubang pohonnya yang empuk beralaskan lumut kering, Sasa meringkuk nyaman. Ekor lebatnya membalut tubuhnya seperti selimut sutra yang hangat. Hatinya damai, tahu bahwa ia dicintai apa adanya. Selamat tidur, tupai kecil yang manis.",
                "textEn": "Inside her cozy hollow-tree nest cushioned with dried fragrant moss, little Sasa curled up blissfully. Her fluffy tail wrapped around her body like a warm velvet quilt. Her heart was peaceful, knowing she was deeply loved just as she was. Goodnight, sweet little squirrel.",
                "quote": "🌙 'Tidurlah dengan rasa damai, karena keunikanmu adalah hadiah terindah bagi dunia.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak manis, kamu sangat berharga dan dicintai apa adanya.",
                "imagePrompt": "A peaceful bedtime illustration of squirrel Sasa sleeping curled up inside a hollow tree nest, her giant bushy tail wrapped around her like a blanket. Soft moonlight peeks in, wax crayon and oil pastel on heavy paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s58)

    # =========================================================================
    # STORY 59: Lagu Baru dari Seberang Laut
    # =========================================================================
    s59 = {
        "id": "lagu-seberang-laut",
        "storyNumber": 59,
        "title": "Lagu Baru dari Seberang Laut",
        "englishTitle": "New Song from Across the Ocean",
        "category": "persahabatan",
        "categoryLabel": "🤝 Persahabatan & Inklusivitas",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Menyambut teman baru dari tempat jauh, menghargai budaya yang berbeda, dan keindahan persatuan",
        "cover": "images/story59_cover.jpg",
        "coverImage": "images/story59_cover.jpg",
        "synopsis": "Ayu si gadis penari pantai menyambut Ken, seorang anak pendatang baru yang baru berlayar dari seberang samudra. Meskipun pakaian dan bahasa nyanyian mereka berbeda, dentingan seruling bambu Ken dan gemerincing gelang kaki Ayu berpadu menjadi lagu persahabatan yang memukau seluruh desa.",
        "synopsisEn": "Little coastal dancer Ayu welcomes Ken, a newcomer boy who sailed from across the wide ocean. Though their clothing and song words differ, Ken's bamboo flute melodies and Ayu's ankle-bell rhythms harmonize into a breathtaking song of unity.",
        "protagonist": "Ayu (Gadis cilik 5 tahun bergaun selendang tenun pantai dengan hiasan bunga kamboja)",
        "companion": "Ken (Anak laki-laki pendatang berjaket katun bersulam awan pembawa seruling)",
        "setting": "Sanggar Tari Tepi Pantai Berpasir Putih Berangin Kelapa",
        "pages": [
            {
                "number": 1,
                "title": "Perahu Layar yang Berlabuh di Teluk",
                "titleEn": "The Sailboat Anchors in the Bay",
                "textId": "Pagi itu, sebuah perahu kayu dengan layar bertambal kain sutra berlabuh di teluk desa nelayan. Dari perahu itu, turunlah seorang anak laki-laki dengan jaket katun bersulam awan perak dan memegang seruling bambu ramping.",
                "textEn": "That morning, a wooden sailboat with patched silk sails anchored in the fishing village bay. Down the plank stepped a young boy wearing a cotton jacket embroidered with silver clouds, carrying a slender bamboo flute.",
                "quote": "⛵ 'Setiap perahu yang berlabuh membawa cerita dan harapan baru dari seberang samudra.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat perahu layar di tepi laut?",
                "imagePrompt": "Charming children's book illustration of a traditional wooden sailboat anchored in a tropical turquoise bay. Little boy Ken in an embroidered blue jacket steps onto the sandy beach holding a wooden flute. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Mata Malu-Malu di Bawah Pohon Kelapa",
                "titleEn": "Shy Glances Beneath the Coconut Palms",
                "textId": "Ken duduk di atas batang pohon kelapa yang tumbang. Matanya memandang sekeliling dengan ragu. Anak-anak desa memperhatikannya dari kejauhan; bahasa dan pakaian Ken tampak begitu berbeda dari yang biasa mereka lihat.",
                "textEn": "Ken sat upon a fallen coconut trunk. His eyes gazed around with hesitant shyness. Village children watched from a distance; Ken's clothes and soft speech seemed so unfamiliar to what they were used to.",
                "quote": "🌴 'Berada di tempat yang baru seringkali membuat kita merasa sendirian di tengah keramaian.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana perasaanmu saat pertama kali tiba di lingkungan atau kota yang belum kamu kenal?",
                "imagePrompt": "A gentle storybook illustration of boy Ken sitting alone on a log by the beach looking shy, while other village children peek from behind palm trees with curious but cautious eyes, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Langkah Menyapa dari Ayu",
                "titleEn": "Ayu's Welcoming Footsteps",
                "textId": "Ayu, gadis cilik penari pantai dengan bunga kamboja harum di telinganya, tidak ingin melihat Ken sendirian. Dengan senyuman hangat, Ayu melangkah mendekat sambil mengulurkan sepiring buah mangga manis.",
                "textEn": "Ayu, the little coastal dancer with a fragrant frangipani blossom behind her ear, didn't want to see Ken sitting all alone. With a warm beaming smile, Ayu stepped forward offering a plate of sweet sliced mangoes.",
                "quote": "🌸 'Keramahan yang tulus adalah bahasa universal yang langsung dipahami oleh setiap hati.'",
                "coReading": "💡 Aktivitas Seru: Berikan senyuman termanismu dan lambaikan tangan seolah menyapa kawan baru!",
                "imagePrompt": "Touching children's book scene of little girl Ayu in a traditional woven yellow sash offering sweet mangoes to newcomer boy Ken on the white sandy shore, both beginning to smile, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Tiupan Nada Seruling yang Merdu",
                "titleEn": "The Sweet Melody of the Bamboo Flute",
                "textId": "Ken menerima buah mangga itu dengan bungkukan hormat. Untuk membalas kebaikan Ayu, Ken menempelkan seruling bambunya ke bibir. Fyuu-lii-fyuuu... Suara tiupan seruling mengalun sangat merdu, sejuk seperti angin sepoi-sepoi dari puncak gunung.",
                "textEn": "Ken accepted the mango with a polite, respectful bow. To return Ayu's kindness, Ken lifted his bamboo flute to his lips. Phee-loo-phee... The flute's notes floated sweet and airy, as refreshing as a mountain breeze over coastal dunes.",
                "quote": "🎶 'Musik memiliki kekuatan ajaib untuk menghubungkan dua hati tanpa membutuhkan terjemahan.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara tiupan seruling bambu yang mendayu-dayu: 'Fyuuu-liii-fyuuu!'",
                "imagePrompt": "Whimsical illustration of boy Ken playing a slender bamboo flute by the sea, with golden music notes swirling gently in the air toward smiling Ayu, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Gemerincing Gelang Kaki Ayu",
                "titleEn": "The Tinkling of Ayu's Ankle Bells",
                "textId": "Mendengar nada seruling yang indah, kaki Ayu bergerak dengan sendirinya. Gelang kuningan kecil di pergelangan kakinya bergemerincing berirama: kling-kling-kling! Ayu melangkah lentur menarikan tarian ombak pesisir.",
                "textEn": "Hearing the enchanting flute song, Ayu's feet began dancing of their own accord. Little brass bells on her ankles chimed in lively rhythm: clink-tinkle-clink! Ayu twirled with graceful fluidity, dancing the dance of ocean waves.",
                "quote": "💃 'Saat musik dan tarian bertemu, kegembiraan menular ke setiap orang di sekitar kita.'",
                "coReading": "💡 Aktivitas Seru: Goyangkan kakimu pelan-pelan seperti membunyikan gelang lonceng menari!",
                "imagePrompt": "Joyous children's picture book scene of little girl Ayu dancing gracefully on the white sand, her colorful woven sash swirling, while boy Ken plays his flute with sparkling eyes, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Perpaduan Irama Barat dan Timur",
                "titleEn": "The Harmony of East and West",
                "textId": "Nada seruling Ken yang tenang berpadu sempurna dengan gemerincing gelang kaki Ayu yang riang. Lagu dari seberang laut dan tarian tanah pesisir menyatu menjadi sebuah harmoni baru yang belum pernah terdengar sebelumnya.",
                "textEn": "Ken's soothing flute tones harmonized flawlessly with Ayu's spirited ankle chimes. The song from across the ocean and the dance of the tropical shore blended into an entirely new, breathtaking melody.",
                "quote": "🌊 'Perbedaan budaya yang bersatu menciptakan karya yang jauh lebih indah dan kaya.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana rasanya jika dua lagu yang berbeda dinyanyikan bersamaan dengan serasi?",
                "imagePrompt": "Magical storybook illustration of music notes and swirling flower petals connecting Ken's flute and Ayu's dancing ribbons along the seashore, with gentle turquoise waves in the background, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Anak-Anak Desa Bergabung Menari",
                "titleEn": "Village Children Join the Dance",
                "textId": "Satu per satu, anak-anak desa yang tadi ragu mulai mendekat dan bertepuk tangan mengikuti irama. Ada yang memukul kentongan kayu, ada yang bernyanyi, dan semuanya menari gembira melingkari Ken dan Ayu.",
                "textEn": "One by one, the hesitant village children drew close, clapping their hands to the infectious beat. Some tapped wooden rhythm sticks, others sang along, and soon all were dancing in a joyful circle around Ken and Ayu.",
                "quote": "🎉 'Keramahan satu orang mampu membuka pintu persahabatan bagi seluruh komunitas.'",
                "coReading": "💡 Tepuk Tangan Bersama: Bertepuk tanganlah berirama bersama si kecil: 'Prok, prok, prok-prok-prok!'",
                "imagePrompt": "Heartwarming scene of many smiling village children dancing and clapping in a big circle on the beach around Ken and Ayu. Soft golden afternoon sunlight, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Kalung Bunga Penyambut Tamu",
                "titleEn": "The Garland of Welcome Blossoms",
                "textId": "Ayu mengalungkan untaian bunga kamboja putih beraroma wangi ke leher Ken. \"Sekarang kamu bukan lagi pendatang, Ken. Kamu adalah sahabat kami di desa ini,\" kata Ayu sambil tersenyum tulus.",
                "textEn": "Ayu placed a fragrant lei of white and yellow frangipani blossoms around Ken's neck. \"You are a stranger no more, Ken. You are our dear friend in this village,\" said Ayu with an open heart.",
                "quote": "🌺 'Menyambut tamu dengan tulus membuat dunia yang luas terasa seperti satu rumah yang hangat.'",
                "coReading": "💡 Tanya si Kecil: Kalung bunga apa yang paling harum menurut penciumanmu?",
                "imagePrompt": "Touching illustration of little girl Ayu placing a floral garland around Ken's neck, while Ken touches his flute to his heart in humble, joyful gratitude, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Lentera Pantai di Bawah Langit Senja",
                "titleEn": "Beachside Lanterns Under Sunset Skies",
                "textId": "Senja ungu merekah di atas laut. Lentera-lentera minyak kelapa dinyalakan di sepanjang bibir pantai. Warga desa duduk bersama menikmati jamuan ikan bakar dan nasi kelapa, merayakan hadirnya sahabat baru dari seberang samudra.",
                "textEn": "Violet dusk blossomed over the sea. Coconut-oil lanterns were lit along the water's edge. The villagers sat together sharing roasted fish and coconut rice, celebrating the arrival of their new friend from across the sea.",
                "quote": "🏮 'Malam yang penuh kebersamaan adalah perayaan terindah bagi persaudaraan manusia.'",
                "coReading": "💡 Tanya si Kecil: Makanan apa yang paling nikmat disantap bersama teman-teman di tepi pantai?",
                "imagePrompt": "Festive and cozy seaside banquet illustration of villagers and children sitting on mats near warm lanterns, eating together at dusk, with the ocean glowing under peach twilight, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur di Iringi Desau Samudra",
                "titleEn": "Asleep to the Ocean's Whisper",
                "textId": "Malam tiba membawa kedamaian di desa teluk. Di dalam pondoknya yang berangin sejuk, Ken tidur lelap memeluk seruling bambunya dengan kalung kamboja di samping bantal. Alunan ombak menyanyikan lagu persahabatan yang tak akan pernah pudar. Selamat tidur, anak pengelana yang kini memiliki rumah.",
                "textEn": "Night enveloped the quiet bay village in deep peace. Inside his breezy guest cabin, little Ken slept soundly holding his bamboo flute, the flower garland resting beside his pillow. The gentle ocean waves whispered a song of friendship that would never fade. Goodnight, brave voyager.",
                "quote": "🌙 'Ke mana pun kita berlayar, persahabatan sejati akan selalu menyambut kita dengan pelukan rumah.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak ramah, semoga hatimu selalu terbuka untuk mencintai semua sahabat di dunia.",
                "imagePrompt": "Tranquil bedtime illustration of boy Ken sleeping peacefully in a beachside wooden cottage bedroom, the frangipani garland resting beside him on the nightstand under soft moonlight, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s59)

    # =========================================================================
    # STORY 60: Balap Karung di Jalur Landai
    # =========================================================================
    s60 = {
        "id": "balap-karung-landai",
        "storyNumber": 60,
        "title": "Balap Karung di Jalur Landai",
        "englishTitle": "The Sack Race on the Gentle Ramp",
        "category": "persahabatan",
        "categoryLabel": "🤝 Persahabatan & Inklusivitas",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Inklusivitas, kepedulian terhadap teman difabel, dan mengubah aturan agar semua bisa bermain",
        "cover": "images/story60_cover.jpg",
        "coverImage": "images/story60_cover.jpg",
        "synopsis": "Anak-anak kompleks sedang asyik bermain balap karung di lapangan rumput. Fandi, yang menggunakan kursi roda beroda kuning cerah, hanya bisa menonton dari pinggir dengan mata murung. Namun teman-temannya membuat ide cemerlang: membuat jalur landai khusus agar Fandi bisa ikut meluncur gembira bersama karung hiasnya.",
        "synopsisEn": "Neighborhood kids are playing sack races on the lawn. Fandi, who uses a bright yellow wheelchair, watches from the sideline with longing eyes. But his friends hatch a brilliant idea: crafting a smooth, gentle ramp so Fandi can race along in his decorated sack chair.",
        "protagonist": "Fandi (Anak laki-laki 5 tahun berkursi roda kuning cerah dengan topi baret merah)",
        "companion": "Rino & Sisi (Sahabat-sahabat bermain yang penuh perhatian dan kreatif)",
        "setting": "Taman Kompleks Ramah Anak Berumput Hijau Segar",
        "pages": [
            {
                "number": 1,
                "title": "Lompatan Riang Karung Goni",
                "titleEn": "Cheerful Hops in Burlap Sacks",
                "textId": "Bung-bung-bung! Suara lompatan karung goni terdengar riuh di halaman rumput taman kompleks. Anak-anak melompat berjejer sambil tertawa terbahak-bahak saat karung mereka bergoyang lucu menuju garis akhir.",
                "textEn": "Boing-boing-hop! The muffled thumps of burlap sacks echoed across the green community lawn. Children bounced in a row, bursting into joyful giggles as their sacks wobbled delightfully toward the finish line.",
                "quote": "🏃 'Permainan tradisional selalu membawa gelak tawa yang menyehatkan tubuh dan jiwa.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu mencoba melompat di dalam karung goni?",
                "imagePrompt": "Charming children's book illustration of neighborhood children laughing and hopping in burlap sacks across a green lawn in a sunny playground. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Tatapan Sepi dari Pinggir Taman",
                "titleEn": "A Quiet Look from the Sideline",
                "textId": "Di tepi jalan setapak semen, Fandi duduk di atas kursi roda kuning cerahnya. Kakinya yang lemah tidak bisa dimasukkan ke dalam karung goni. Fandi tersenyum melihat kawan-kawannya, tetapi ada sedikit rasa sepi di sudut matanya.",
                "textEn": "At the edge of the paved path, Fandi sat in his bright yellow wheelchair. His weak legs could not stand inside a burlap sack. Fandi smiled seeing his friends play, but a quiet trace of longing lingered in the corner of his eyes.",
                "quote": "🦽 'Hanya menonton dari pinggir seringkali membuat hati kecil merasa tertinggal.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana rasanya jika kamu hanya bisa menonton saat teman-temanmu sedang bermain seru?",
                "imagePrompt": "Touching storybook scene of boy Fandi in a sunny yellow wheelchair wearing a red beret, resting his chin on his hands as he watches from the paved path, soft crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Rino dan Sisi yang Berhenti Melompat",
                "titleEn": "Rino and Sisi Stop Their Hops",
                "textId": "Rino dan Sisi menyadari tatapan Fandi. Mereka segera keluar dari karung goni masing-masing dan berlari menghampiri Fandi. \"Permainan ini belum seru kalau Fandi belum ikut bermain!\" kata Rino dengan tegas dan ramah.",
                "textEn": "Rino and Sisi noticed Fandi's quiet gaze. They quickly stepped out of their burlap sacks and trotted over to him. \"This game isn't truly fun until Fandi can race with us!\" declared Rino with firm, caring warmth.",
                "quote": "🤝 'Permainan yang sesungguhnya adalah permainan yang membuat semua sahabat merasa disertakan.'",
                "coReading": "💡 Tanya si Kecil: Apa yang akan kamu lakukan jika melihat seorang teman duduk sendirian?",
                "imagePrompt": "Heartwarming illustration of boy Rino and girl Sisi running up to Fandi's wheelchair with warm smiling faces, holding their burlap sacks in hand, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Ide Jalur Landai yang Halus",
                "titleEn": "The Idea of the Gentle Smooth Ramp",
                "textId": "Sisi menunjuk ke jalan setapak berlantai semen landai di samping taman bunga. \"Lihat! Jalur ini menurun sangat lembut dan halus. Fandi bisa meluncur dengan aman menggunakan kursi rodanya di samping kami!\"",
                "textEn": "Sisi pointed toward a gently sloping paved walkway beside the flower garden. \"Look! This ramp slopes down so smoothly and gently. Fandi can roll safely in his wheelchair right alongside our hops!\"",
                "quote": "💡 'Kreativitas yang didorong oleh kasih sayang selalu mampu meruntuhkan rintangan.'",
                "coReading": "💡 Aktivitas Seru: Pikirkan bersama si kecil: cara apa lagi yang bisa dilakukan agar teman berkursi roda bisa ikut bermain?",
                "imagePrompt": "Charming children's book scene of children inspecting a wide, gently sloped paved garden ramp bordered by marigolds and smooth railings, pointing with excited smiles, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Menghias Kursi Roda dengan Karung Bintang",
                "titleEn": "Decorating the Wheelchair with Star Burlap",
                "textId": "Agar Fandi merasa menjadi bagian dari lomba karung, teman-teman memasang kain goni bertabur stiker bintang emas di bagian depan kursi roda Fandi. Kini, kursi roda Fandi tampak seperti kereta balap penjelajah bintang!",
                "textEn": "So Fandi would feel fully part of the sack race, his friends draped a neat piece of burlap adorned with gold star stickers across the front of his wheelchair. Now, his chair looked like a champion star-racer chariot!",
                "quote": "⭐ 'Sentuhan kecil dari perhatian membuat seseorang merasa begitu dihargai dan istimewa.'",
                "coReading": "💡 Aktivitas Seru: Hias kursi atau mainanmu dengan stiker bintang imajinasi bersama si kecil!",
                "imagePrompt": "Delightful illustration of children laughing as they decorate Fandi's yellow wheelchair with burlap and shiny star stickers. Fandi's face lights up with sheer delight, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Garis Awal Bersama-Sama",
                "titleEn": "At the Starting Line Together",
                "textId": "Di garis awal yang digambar dengan kapur putih di atas semen, Rino dan Sisi berdiri di dalam karung mereka di sebelah kiri, sementara Fandi berada di jalur landai di sebelah kanan. Semua bersiap dengan mata berkilat riang.",
                "textEn": "At the starting line drawn in white chalk across the path, Rino and Sisi stood inside their sacks on the grass, while Fandi aligned his wheels on the gentle paved track. Everyone readied with dancing, excited eyes.",
                "quote": "🏁 'Keadilan bukanlah memperlakukan semua sama persis, melainkan memberi kesempatan yang adil bagi semua.'",
                "coReading": "💡 Hitung Mundur: Ucapkan hitungan mulai balapan: 'Satu... dua... tiga... MULAI!'",
                "imagePrompt": "Exciting children's storybook scene at the chalk starting line: children in sacks on the lawn and Fandi in his star-decorated wheelchair on the smooth ramp, ready to race, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Meluncur dan Melompat Beriringan",
                "titleEn": "Rolling and Hopping Side by Side",
                "textId": "\"PRRRIIT!\" Peluit ditiup! Fandi mendorong kedua lingkar roda kuningnya dengan mantap: srrruuut! Kursi rodanya meluncur mulus menuruni jalur landai. Di sampingnya, Rino dan Sisi melompat: tung-tung-tung!",
                "textEn": "\"TWEEET!\" The whistle blew! Fandi pushed his yellow wheel rims with steady vigor: whoooosh! His chair glided smoothly down the gentle incline. Right beside him, Rino and Sisi bounced with hearty laughs: boing-boing-hop!",
                "quote": "💨 'Kecepatan bukanlah segalanya; yang paling berharga adalah kegembiraan melaju bersama.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara roda meluncur kencang: 'Srrruuut... meluncur laju!'",
                "imagePrompt": "Dynamic and cheerful illustration of Fandi rolling smoothly down the garden path with arms pumping happily, while friends in sacks bounce alongside on the grass, hair blowing in the wind, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Menembus Pita Garis Akhir",
                "titleEn": "Breaking Through the Finish Ribbon",
                "textId": "SREEK! Roda kursi roda Fandi dan lompatan Rino menembus pita merah di garis akhir secara bersamaan! Seluruh anak-anak di taman bersorak gembira sambil melompat-lompat menepukkan tangan.",
                "textEn": "SNAP! The wheels of Fandi's chair and Rino's hop broke through the red crepe-paper finish ribbon at the exact same instant! Every child in the playground cheered in ecstatic applause.",
                "quote": "🏆 'Kemenangan sejati tercapai saat tidak ada satu pun sahabat yang tertinggal di belakang.'",
                "coReading": "💡 Sorak Gembira: Bersoraklah bersama si kecil: 'Horeee, kita semua juara!'",
                "imagePrompt": "Joyous celebration illustration of Fandi and his friends crossing the finish line ribbon together, confetti of flower petals falling in the air, big smiles everywhere, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Piala Keberbersamaan dari Ranting Bunga",
                "titleEn": "The Friendship Trophy of Twigs and Blooms",
                "textId": "Sisi mengalungkan medali mahkota dari anyaman ranting melati harum ke leher Fandi. Fandi tertawa lebar dengan pipi bersemu merah. Hari ini adalah hari paling membahagiakan di taman bermain.",
                "textEn": "Sisi placed a woven crown medal of fragrant jasmine twigs around Fandi's neck. Fandi beamed with glowing rosy cheeks. Today was the happiest, most unforgettable afternoon in the playground.",
                "quote": "🌼 'Penghargaan terindah adalah rasa memiliki sahabat-sahabat yang selalu memikirkan kita.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana perasaanmu saat melihat teman yang difabel bisa ikut tertawa gembira?",
                "imagePrompt": "Heartwarming illustration of Fandi smiling with tears of joy as his friends place a jasmine floral wreath around his neck, hugging his wheelchair in fellowship, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Mimpi Meluncur di Jalur Bintang",
                "titleEn": "Dreaming of Gliding on Starlit Tracks",
                "textId": "Malam tiba membawa bintang-bintang ke langit kompleks. Di kamarnya, Fandi tidur pulas di balik selimut biru hangat. Kursi roda kuningnya beristirahat rapi di samping tempat tidur. Dalam mimpinya, Fandi meluncur bebas di jalan pelangi di angkasa bersama sahabat-sahabatnya. Selamat tidur, anak juara berhati mulia.",
                "textEn": "Night blanketed the neighborhood under starry skies. In his room, Fandi slept soundly under a warm blue quilt. His yellow wheelchair rested tidily beside his bed. In his dreams, Fandi rolled freely across a cosmic rainbow track alongside his best friends. Goodnight, brave little champion.",
                "quote": "🌙 'Tidur yang paling damai adalah tidur setelah merasakan indahnya dirangkul oleh persahabatan.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak hebat, terima kasih sudah belajar menyayangi semua teman tanpa membeda-bedakan.",
                "imagePrompt": "A peaceful bedtime illustration of boy Fandi sleeping soundly in his bed, with his yellow wheelchair parked beside him illuminated by soft moonlight through curtains, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s60)

    # =========================================================================
    # STORY 61: Mendengarkan Sampai Kalimat Terakhir
    # =========================================================================
    s61 = {
        "id": "mendengarkan-sampai-selesai",
        "storyNumber": 61,
        "title": "Mendengarkan Sampai Kalimat Terakhir",
        "englishTitle": "Listening Until the Very Last Word",
        "category": "persahabatan",
        "categoryLabel": "🤝 Persahabatan & Inklusivitas",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Menghargai teman, melatih kesabaran untuk tidak memotong pembicaraan, dan ketulusan menyimak",
        "cover": "images/story61_cover.jpg",
        "coverImage": "images/story61_cover.jpg",
        "synopsis": "Rangga seringkali tidak sabar dan suka memotong cerita kawan-kawannya. Di atas bale-bale bambu di bawah pohon mangga, Dian bercerita tentang petualangannya menemukan kupu-kupu bersayap kaca. Rangga belajar menutup mulutnya rapat-rapat, memasang telinganya, dan menemukan keajaiban mendengarkan sampai kalimat terakhir.",
        "synopsisEn": "Little Rangga is often impatient and interrupts his friends mid-story. Sitting on the bamboo pavilion beneath the mango tree, Dian tells of finding a glasswing butterfly. Rangga learns to keep his lips gently closed, listen with patient ears, and discover the wonder of hearing until the very last word.",
        "protagonist": "Rangga (Anak laki-laki 5 tahun berkemeja flanel kotak-kotak dengan mata lincah)",
        "companion": "Dian (Gadis cilik 5 tahun berkepang satu yang gemar bercerita ekspresif)",
        "setting": "Bale-Bale Bambu Teduh di Bawah Pohon Mangga Berbunga",
        "pages": [
            {
                "number": 1,
                "title": "Kata-Kata yang Suka Memotong",
                "titleEn": "Words That Love to Interrupt",
                "textId": "Rangga adalah anak yang cerdas dan bersemangat, tetapi lidahnya sering bergerak lebih cepat daripada telinganya. Setiap kali temannya baru mengucapkan sepatah kata, Rangga selalu buru-buru menyahut: \"Aku tahu itu! Dengarkan ceritaku saja!\"",
                "textEn": "Rangga was a clever, spirited boy, but his tongue often moved much faster than his ears. Whenever a friend began speaking, Rangga eagerly cut in: \"I know that already! Listen to my story instead!\"",
                "quote": "🗣️ 'Keinginan untuk selalu berbicara seringkali membuat kita lupa bagaimana cara menyimak.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah ceritamu dipotong saat kamu sedang asyik berbicara?",
                "imagePrompt": "Charming children's book illustration of boy Rangga in a plaid shirt waving his hands eagerly to interrupt a friend who is speaking. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Dian dan Rahasia Kupu-Kupu Kaca",
                "titleEn": "Dian and the Secret Glasswing Butterfly",
                "textId": "Sore itu di atas bale-bale bambu, Dian duduk memeluk lututnya dengan mata berbinar. \"Rangga, tadi pagi di kebun belakang, aku melihat sesuatu yang sangat luar biasa... sebuah sayap yang tembus pandang...\"",
                "textEn": "That afternoon on the bamboo daybed, Dian sat hugging her knees with sparkling eyes. \"Rangga, early this morning in the back garden, I saw something truly wondrous... wings that were completely clear like glass...\"",
                "quote": "🦋 'Setiap cerita yang tulus berhak mendapatkan ruang untuk mekar hingga selesai.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat serangga atau kupu-kupu yang unik di kebun?",
                "imagePrompt": "A gentle storybook illustration of girl Dian in a floral dress gesturing with open hands as she speaks excitedly on a bamboo porch, while Rangga sits opposite her leaning forward, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Kunci Bibir dari Kakek",
                "titleEn": "Grandpa's Secret Lip-Key",
                "textId": "Rangga sudah membuka mulutnya hendak memotong: \"Pasti itu capung biasa---\" Namun Kakek yang sedang menyeduh teh menaruh jari telunjuknya lembut di bibir sambil tersenyum: \"Kunci bibirmu dulu, Rangga kecil. Putar kuncinya: klik!\"",
                "textEn": "Rangga already opened his mouth to interrupt: \"That must just be a dragonfl---\" But Grandpa, brewing tea nearby, gently placed an index finger to his lips with a warm smile: \"Lock your lips for a moment, little Rangga. Turn the secret key: click!\"",
                "quote": "🗝️ 'Mengunci bibir sejenak memberi kesempatan bagi telinga untuk menyerap kebaikan.'",
                "coReading": "💡 Aktivitas Seru: Gerakkan jarimu di depan bibir seperti memutar kunci rahasia: 'Klik, kita kunci!'",
                "imagePrompt": "Delightful illustration of kindly grandfather touching his finger to his smiling lips, while Rangga pretends to lock his lips with an invisible key, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Membuka Dua Daun Telinga Lebar-Lebar",
                "titleEn": "Opening Two Ears Wide",
                "textId": "Rangga menelan kembali kata-katanya. Ia melipat kedua tangannya di atas pangkuan dan memasang telinganya dengan sungguh-sungguh. Angin sore berdesir pelan di antara daun mangga, mengiringi suara Dian yang lembut.",
                "textEn": "Rangga swallowed his eager words. He folded both hands politely in his lap and opened his ears wide. The afternoon breeze rustled softly through the mango canopy, accompanying Dian's gentle voice.",
                "quote": "👂 'Tuhan memberi kita dua telinga dan satu mulut agar kita mendengarkan dua kali lebih banyak.'",
                "coReading": "💡 Sentuh Telinga: Sentuh kedua daun telingamu perlahan dan rasakan betapa berharganya indra pendengaranmu.",
                "imagePrompt": "Close-up storybook scene of boy Rangga sitting quietly with hands folded, eyes focused attentively on Dian, peaceful listening expression, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Sayap Bening Seperti Jendela Kaca",
                "titleEn": "Clear Wings Like Glass Panes",
                "textId": "Dian melanjutkan ceritanya tanpa terputus. \"Sayap kupu-kupu itu bukan berwarna-warni, Rangga, melainkan bening seperti kaca jendela! Saat ia hinggap di atas kelopak anggrek ungu, warna ungu bunganya terlihat menembus sayapnya!\"",
                "textEn": "Dian continued her tale without interruption. \"The butterfly's wings weren't painted in bright colors, Rangga; they were crystal clear like window glass! When it rested on a purple orchid petal, the purple blossom shone right through its wings!\"",
                "quote": "🌸 'Keindahan detail sebuah cerita hanya bisa terungkap jika kita sabar mendengarkannya.'",
                "coReading": "💡 Tanya si Kecil: Bisakah kamu membayangkan sayap kupu-kupu yang tembus pandang seperti kaca?",
                "imagePrompt": "Whimsical children's book illustration showing Dian's imagination bubble: a delicate glasswing butterfly with transparent wings resting on an exotic purple orchid, soft sunlight glowing through it, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Rasa Ingin Tahu yang Menahan Diri",
                "titleEn": "Curiosity Learning Restraint",
                "textId": "Di dalam dada Rangga, ada rasa takjub yang meluap. Ia ingin bertanya banyak hal, tetapi ia mengingat pesan Kakek. Rangga menahan diri dan membiarkan Dian menceritakan bagian paling akhir petualangannya.",
                "textEn": "Inside Rangga's chest bubbled deep fascination. He had a dozen questions bursting to escape, but he remembered Grandpa's gentle lesson. Rangga restrained himself, allowing Dian to finish the climax of her discovery.",
                "quote": "⏳ 'Menahan diri sejenak adalah tanda rasa hormat tertinggi kepada orang yang sedang berbicara.'",
                "coReading": "💡 Tanya si Kecil: Apakah kamu bisa menunggu sampai giliranmu tiba sebelum mengajukan pertanyaan?",
                "imagePrompt": "Touching picture book illustration of Rangga leaning forward with wide, sparkling black bead eyes, completely engrossed in Dian's story without uttering a single word, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Kalimat Terakhir yang Sempurna",
                "titleEn": "The Perfect Last Sentence",
                "textId": "\"...dan sebelum terbang ke arah matahari terbenam, kupu-kupu kaca itu mengepakkan sayapnya lembut, seolah mengucapkan terima kasih karena aku tidak menangkapnya.\" Dian menghela napas lega dan tersenyum puas. Ceritanya telah tuntas.",
                "textEn": "\"...and before fluttering toward the sunset, that glasswing butterfly softly flapped its wings, as if whispering thank you because I didn't try to capture it.\" Dian let out a happy sigh and smiled with deep satisfaction. Her story was complete.",
                "quote": "✨ 'Kalimat terakhir dari sebuah cerita seringkali menyimpan pesan terindah dari semuanya.'",
                "coReading": "💡 Aktivitas Seru: Katakan bersama: 'Dan itulah akhir ceritanya yang manis!'",
                "imagePrompt": "Charming illustration of Dian finishing her story with hands placed gently over her heart, smiling contentedly at Rangga under the shady mango tree, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Pujian yang Tulus dari Sahabat",
                "titleEn": "A Heartfelt Compliment from a Friend",
                "textId": "KLIK! Rangga membuka kunci bibir imajinasinya. \"Wah, Dian... Ceritamu luar biasa indah! Aku senang sekali mendengarkannya sampai selesai!\" Wajah Dian berseri-seri bahagia karena merasa benar-benar didengar dan dihargai.",
                "textEn": "CLICK! Rangga unlocked his invisible lip-lock. \"Wow, Dian... Your story was absolutely magnificent! I am so glad I listened to the very end!\" Dian's face lit up with radiant joy, feeling genuinely heard and deeply cherished.",
                "quote": "🌟 'Didengarkan dengan sungguh-sungguh adalah salah satu hadiah terindah yang bisa kita terima.'",
                "coReading": "💡 Berikan Pujian: Puji teman atau saudaramu setelah ia selesai menceritakan pengalamannya!",
                "imagePrompt": "Warm children's book scene of boy Rangga clapping his hands with genuine admiration, praising smiling Dian on the bamboo porch, with Grandpa smiling knowingly in the background, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Teh Melati dan Biskuit Senja",
                "titleEn": "Jasmine Tea and Twilight Biscuits",
                "textId": "Kakek menuangkan teh melati hangat ke dalam dua cangkir tanah liat dan menyajikan biskuit jahe manis. Kini giliran Rangga bercerita dengan tenang, dan Dian mendengarkannya dengan penuh perhatian yang sama.",
                "textEn": "Grandpa poured warm jasmine tea into two clay mugs and offered sweet ginger biscuits. Now it was Rangga's turn to speak calmly, while Dian listened with the very same tender, patient attention.",
                "quote": "🍵 'Percakapan yang baik mengalir bolak-balik seperti ayunan yang harmonis.'",
                "coReading": "💡 Tanya si Kecil: Mengapa saling mendengarkan secara bergantian membuat obrolan terasa menyenangkan?",
                "imagePrompt": "Cozy picture book illustration of Rangga and Dian sharing tea and biscuits on the wooden daybed at sunset, talking and listening in joyful, balanced turn-taking, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Tenang di Bawah Desau Daun",
                "titleEn": "Peaceful Sleep to Rustling Leaves",
                "textId": "Malam tiba membawa hening yang sejuk. Di tempat tidur kamarnya, Rangga memejamkan mata dengan tenang. Suara desau daun di luar jendela dan nyanyian jangkrik malam terdengar begitu merdu di telinganya yang kini pandai menyimak. Selamat tidur, anak yang bijaksana dalam mendengar.",
                "textEn": "Night descended carrying a gentle cool quiet. In his snug bed, little Rangga closed his eyes in peaceful rest. The soft rustle of leaves outside and the crickets' nocturnal song sounded so sweet to his newly patient ears. Goodnight, wise little listener.",
                "quote": "🌙 'Hati yang pandai mendengarkan akan selalu dihadiahi tidur malam yang paling tenteram.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak pintar, terima kasih sudah belajar mendengarkan dengan penuh kesabaran hari ini.",
                "imagePrompt": "A serene bedtime illustration of boy Rangga sleeping soundly under a plaid blanket, with a smile of quiet contentment on his face. Soft moonlight washes through the wooden shutters, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s61)

    # =========================================================================
    # STORY 62: Kacamata Baru Kucing Ciko
    # =========================================================================
    s62 = {
        "id": "kacamata-kucing-ciko",
        "storyNumber": 62,
        "title": "Kacamata Baru Kucing Ciko",
        "englishTitle": "Ciko Cat's New Glasses",
        "category": "persahabatan",
        "categoryLabel": "🤝 Persahabatan & Inklusivitas",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Mendukung teman yang memakai kacamata, percaya diri dengan penampilan baru, dan saling menguatkan",
        "cover": "images/story62_cover.jpg",
        "coverImage": "images/story62_cover.jpg",
        "synopsis": "Ciko si kucing abu-abu merasa malu dan canggung saat pertama kali memakai kacamata bundar berbingkai merah ke sekolah hewan. Namun sahabat setianya, Mimi si kucing putih, menunjukkan bahwa kacamata baru itu justru membuat dunia menjadi terang benderang dan membuat Ciko terlihat keren seperti profesor cerdas.",
        "synopsisEn": "Little gray cat Ciko feels bashful and self-conscious wearing his new round red spectacles to animal school for the first time. But his loyal best friend, white kitten Mimi, shows him that the glasses bring the world into sharp, sparkling focus and make him look wonderfully clever.",
        "protagonist": "Ciko (Kucing abu-abu berbulu halus dengan kacamata kawat bundar merah menyala)",
        "companion": "Mimi (Kucing putih berparas manis dengan bando pita kuning cerah)",
        "setting": "Sekolah Hewan Ceria di Hutan Hazel & Halaman Berpagar Bunga",
        "pages": [
            {
                "number": 1,
                "title": "Kotak Beludru Merah di Meja",
                "titleEn": "The Red Velvet Case on the Table",
                "textId": "Pagi itu di kamarnya, Ciko si kucing abu-abu menatap sebuah kotak kacamata berbahan beludru merah. Di dalamnya terletak sepasang kacamata bundar kecil berbingkai merah cerah. Dokter Mata Burung Hantu memberikannya kemarin agar Ciko bisa membaca papan tulis dengan jelas.",
                "textEn": "That morning in his bedroom, Ciko the soft gray kitten stared at a red velvet spectacle case. Resting inside were round little glasses with bright crimson frames. Dr. Owl the optometrist had prescribed them yesterday so Ciko could read the blackboard clearly.",
                "quote": "👓 'Kacamata adalah jendela kaca ajaib yang membantu mata kita melihat dunia dengan tajam.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat kakek, nenek, atau temanmu memakai kacamata?",
                "imagePrompt": "Charming children's book illustration of little gray cat Ciko in a striped sweater looking shyly into a small vanity mirror at a pair of round red spectacles resting on the dresser. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Rasa Malu di Depan Pintu Gerbang",
                "titleEn": "Shyness at the School Gate",
                "textId": "Saat tiba di depan gerbang Sekolah Hewan Ceria, Ciko menarik topinya ke bawah untuk menyembunyikan wajahnya. Ekornya melipat ke bawah. \"Bagaimana kalau kawan-kawan menertawaiku dan memanggilku aneh?\" bisik Ciko ragu-ragu.",
                "textEn": "Upon reaching the gates of the Merry Animal School, Ciko pulled his woolen cap low to hide his face. His tail drooped. \"What if my friends laugh at me and call me funny-looking?\" whispered Ciko in hesitation.",
                "quote": "😿 'Perubahan baru pada penampilan kita seringkali memicu rasa cemas yang tak beralasan.'",
                "coReading": "💡 Tanya si Kecil: Apa yang membuatmu merasa malu saat memakai pakaian atau benda baru?",
                "imagePrompt": "A gentle storybook illustration of kitten Ciko standing hesitantly outside a wooden schoolhouse fence, looking nervous with ears flattened, clutching his little backpack straps, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Lambaian Penuh Semangat dari Mimi",
                "titleEn": "Mimi's Enthusiastic Wave",
                "textId": "\"Cikooo!\" Suara riang menyapa dari teras sekolah. Mimi si kucing putih berlari menghampiri sambil melambaikan kedua cakar berbulunya. Bando pita kuning di kepalanya berkibar ceria tertiup angin pagi.",
                "textEn": "\"Cikooo!\" A cheerful voice rang out from the school veranda. White kitten Mimi dashed over, waving both furry paws in greeting. The bright yellow ribbon on her head bobbed merrily in the morning breeze.",
                "quote": "🐱 'Sapaan hangat dari sahabat sejati seketika mengusir kabut keraguan di dalam hati.'",
                "coReading": "💡 Aktivitas Seru: Lambaikan kedua tanganmu sambil memanggil nama sahabat terbaikmu dengan riang!",
                "imagePrompt": "Delightful illustration of white kitten Mimi in a blue pinafore running up to Ciko with open arms and a radiant smile of greeting, dappled sunlight on grass, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "\"Wah, Kacamata Merahmu Keren Sekali!\"",
                "titleEn": "\"Wow, Your Red Glasses Look So Cool!\"",
                "textId": "Mimi berhenti tepat di depan Ciko dan menatap kacamata bundar merah itu dengan mata berbinar kagum. \"Wah, Ciko! Kacamatamu keren sekali! Kamu terlihat sangat gagah dan cerdas seperti profesor buku dongeng!\"",
                "textEn": "Mimi stopped right before Ciko, admiring the round red spectacles with shining, wide eyes. \"Oh, Ciko! Your glasses look wonderfully cool! You look so distinguished and clever, just like a wise storybook professor!\"",
                "quote": "🌟 'Pujian yang tulus dari sahabat mampu mengubah rasa malu menjadi rasa percaya diri.'",
                "coReading": "💡 Berikan Pujian: Puji sesuatu yang dipakai temanmu hari ini dengan kata-kata manis!",
                "imagePrompt": "Heartwarming storybook scene of white kitten Mimi clasping her paws in genuine admiration, looking closely at Ciko's stylish red spectacles, while Ciko's whiskers perk up with a shy smile, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Dunia yang Menjadi Terang Benderang",
                "titleEn": "A World Snapped into Radiant Focus",
                "textId": "Ciko membetulkan posisi kacamatanya di atas hidung mungilnya. KLIK! Tiba-tiba, daun-daun pohon oak yang semula buram kini tampak jelas hingga serat-serat kecilnya. Papan tulis kayu dan wajah ramah Bu Guru Rubah terlihat sangat tajam!",
                "textEn": "Ciko adjusted the spectacles upon his little nose. SNAP! Suddenly, the oak tree leaves that used to blur together were crisp down to every vein. The classroom blackboard and kind Teacher Fox's smile appeared in sharp, sparkling clarity!",
                "quote": "👀 'Melihat dengan jelas membuka keindahan dunia yang selama ini tersembunyi.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat benda buram menjadi sangat jelas saat dilihat dari dekat?",
                "imagePrompt": "Close-up children's book illustration showing Ciko's eyes widening in wonder behind the round glass lenses, with colorful autumn leaves and butterflies rendered in crisp, vivid detail around him, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Membaca Buku Cerita di Baris Depan",
                "titleEn": "Reading the Storybook from the Front Row",
                "textId": "Di dalam kelas, Ciko duduk di baris depan. Saat Bu Guru Rubah meminta membaca buku cerita, Ciko membaca huruf-huruf di halaman dengan lancar tanpa perlu menyipitkan mata lagi. Suaranya terdengar lantang dan percaya diri.",
                "textEn": "Inside the classroom, Ciko sat in the front row. When Teacher Fox invited someone to read aloud, Ciko read every letter across the page smoothly without squinting at all. His little voice resonated loud, clear, and confident.",
                "quote": "📖 'Kacamata adalah sahabat penolong yang membantu kita belajar dengan mudah dan riang.'",
                "coReading": "💡 Aktivitas Seru: Tirukan membaca buku dengan suara lantang dan penuh percaya diri!",
                "imagePrompt": "Charming illustration of gray kitten Ciko standing at his wooden desk wearing his red glasses, reading a picture book aloud with pride while classmates listen happily, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Kawan-Kawan yang Ikut Kagum",
                "titleEn": "Classmates Share the Admiration",
                "textId": "Saat jam istirahat, kawan-kawan kelas berkerumun mengelilingi Ciko. Tidak ada satu pun yang mengejek; mereka justru bergantian memuji bingkai merahnya yang cerah. Kancil dan Tupai bahkan ingin tahu bagaimana kacamata itu bekerja.",
                "textEn": "During recess, classroom friends gathered around Ciko. Not a single creature teased him; instead, they took turns admiring the cheerful red frames. Little mouse-deer and squirrel even wanted to understand how lenses worked.",
                "quote": "🤝 'Saat kita percaya diri dengan diri kita sendiri, orang lain pun akan menghargai kita.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana caramu bersikap baik kepada teman yang memakai kacamata atau alat bantu?",
                "imagePrompt": "Joyous children's picture book scene of little animal friends smiling around Ciko in the schoolyard, gently examining his glasses with friendly curiosity, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Menggambar Pelangi Bersama Mimi",
                "titleEn": "Painting Rainbows with Mimi",
                "textId": "Di meja gambar, Ciko dan Mimi melukis pelangi bersama. Dengan matanya yang kini dapat melihat warna dengan presisi, Ciko menggoreskan krayon merah, kuning, dan biru dengan sangat rapi dan indah.",
                "textEn": "At the art table, Ciko and Mimi painted a grand rainbow together. With eyes that now perceived colors with sharp precision, Ciko stroked red, yellow, and blue crayons across the paper with stunning neatness.",
                "quote": "🎨 'Mata yang sehat dan jernih membantu jemari kita melukis keindahan tanpa batas.'",
                "coReading": "💡 Gambar Bersama: Ambil krayonmu dan gambarlah lengkungan pelangi ceria bersama si kecil!",
                "imagePrompt": "Delightful illustration of kittens Ciko and Mimi side by side drawing a vibrant rainbow with crayons on a large sheet of paper, both laughing with colorful whiskers, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Langkah Pulang yang Tegap",
                "titleEn": "Walking Home with Head Held High",
                "textId": "Bel pulang sekolah berdentang merdu. Ciko berjalan menyusuri jalan desa tanpa menundukkan kepalanya lagi. Ekornya tegak meliuk anggun, dan kacamata merahnya memantulkan kilau emas matahari senja yang damai.",
                "textEn": "The school dismissal bell chimed sweetly. Ciko strolled down the village lane without bowing his head anymore. His tail stood high in an elegant curve, and his red glasses caught the peaceful golden gleam of the setting sun.",
                "quote": "🐾 'Percaya diri membuat setiap langkah kaki terasa ringan dan penuh kebanggaan.'",
                "coReading": "💡 Tegakkan Tubuh: Berdirilah tegap, tersenyum lebar, dan katakan: 'Aku bangga menjadi diriku!'",
                "imagePrompt": "Heartwarming illustration of gray cat Ciko walking proudly down a sunlit flower-lined village path at dusk, holding Mimi's paw, wearing his red glasses with a bright confident smile, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Nyenyak Setelah Hari yang Cerah",
                "titleEn": "Peaceful Sleep After a Bright Day",
                "textId": "Sebelum naik ke ranjang, Ciko meletakkan kacamata merahnya dengan hati-hati di dalam kotak beludru di atas nakas. Di balik selimut hangatnya, Ciko memejamkan mata dengan senyum bahagia. Besok, dunia yang jelas dan indah siap menyambutnya kembali. Selamat tidur, kucing kecil yang hebat.",
                "textEn": "Before climbing into bed, Ciko carefully laid his red glasses inside their velvet case on the nightstand. Under his warm quilt, Ciko closed his eyes with a blissful smile. Tomorrow, a sharp and wondrous world was ready to greet him anew. Goodnight, brave little kitten.",
                "quote": "🌙 'Tidurlah dengan rasa syukur, karena setiap alat bantu adalah jembatan untuk menikmati hidup lebih baik.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak pintar, kamu sungguh istimewa dan luar biasa apa adanya.",
                "imagePrompt": "A serene bedtime illustration of kitten Ciko sleeping soundly curled up under a patchwork blanket, with his red glasses resting safely in their case on the bedside table under moonlight, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s62)

    return stories

print("Story module 58-62 defined successfully")
