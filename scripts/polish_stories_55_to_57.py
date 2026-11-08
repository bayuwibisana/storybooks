# scripts/polish_stories_55_to_57.py
import json

def get_stories_55_to_57():
    stories = []

    # =========================================================================
    # STORY 55: Bekal Kasih Sayang untuk Adik
    # =========================================================================
    s55 = {
        "id": "bekal-kasih-sayang",
        "storyNumber": 55,
        "title": "Bekal Kasih Sayang untuk Adik",
        "englishTitle": "The Lunchbox Made with Love",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Kasih sayang saudara, perhatian dalam menyiapkan makanan, dan memberi semangat",
        "cover": "images/story55_cover.jpg",
        "coverImage": "images/story55_cover.jpg",
        "synopsis": "Hari ini adalah hari pertama Adik Rio masuk sekolah taman kanak-kanak, dan ia merasa cemas. Kakak Nadia berinisiatif bangun pagi untuk menyiapkan kotak bekal istimewa: bola-bola nasi berbentuk beruang tersenyum, wortel bintang, dan telur gulung keemasan yang menghangatkan hati adik tercinta.",
        "synopsisEn": "Today is little brother Rio's very first day of kindergarten, and he feels nervous jitters. Big sister Nadia wakes up early to prepare a special lunchbox: smiling bear onigiri rice balls, star-cut carrots, and golden tamagoyaki egg rolls that comfort his little heart.",
        "protagonist": "Kakak Nadia (Gadis cilik 7 tahun berambut kuncir dua dengan celemek kotak-kotak biru)",
        "companion": "Adik Rio (Anak laki-laki 3 tahun bertas ransel katak hijau dengan mata bulat)",
        "setting": "Dapur Rumah Pagi Hari yang Cerah & Kotak Bekal Berwarna Kuning",
        "pages": [
            {
                "number": 1,
                "title": "Pagi yang Cemas Menjelang Sekolah",
                "titleEn": "A Nervous Morning Before School",
                "textId": "Fajar merekah lembut di ufuk timur. Di kamar tidur, Adik Rio duduk memeluk ransel katak hijaunya dengan mata murung. Hari ini adalah hari pertamanya masuk sekolah, dan Rio takut tidak punya teman di kelas baru.",
                "textEn": "Dawn broke gently along the eastern horizon. In the bedroom, little brother Rio sat hugging his green froggy backpack with solemn eyes. Today was his very first morning of preschool, and Rio feared he wouldn't find any friends.",
                "quote": "🎒 'Menghadapi tempat baru memang seringkali membuat hati kecil kita merasa ragu.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu merasa malu atau takut saat pertama kali pergi ke sekolah?",
                "imagePrompt": "Charming children's book illustration of toddler boy Rio sitting on his bed hugging a cute green frog backpack looking worried, while older sister Nadia in pigtails looks at him with caring empathy from the doorway. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Rencana Rahasia Kakak Nadia",
                "titleEn": "Sister Nadia's Secret Plan",
                "textId": "Kakak Nadia tersenyum penuh kasih. Ia tahu apa yang bisa membuat Rio tersenyum kembali. Nadia berjingkat ke dapur, mengambil kotak bekal kuning kesayangan Rio, lalu menyingsingkan lengan bajunya di depan meja dapur.",
                "textEn": "Big sister Nadia smiled with deep affection. She knew exactly what could bring back Rio's bright smile. Nadia tiptoed into the kitchen, retrieved Rio's favorite sunny-yellow lunchbox, and rolled up her sleeves at the counter.",
                "quote": "💡 'Kasih sayang selalu menemukan cara kreatif untuk menyemangati orang yang kita cintai.'",
                "coReading": "💡 Tanya si Kecil: Apa yang biasanya kamu lakukan untuk membuat adik atau temanmu merasa gembira?",
                "imagePrompt": "Delightful storybook scene of young girl Nadia standing at a clean wooden kitchen counter tying her blue gingham apron, opening a bright yellow bento lunchbox with morning sunlight streaming in, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Nasi Hangat Berbentuk Beruang",
                "titleEn": "Warm Rice Shaped Like a Smiling Bear",
                "textId": "Dari periuk, Nadia mengambil sekepal nasi putih hangat yang pulen. Dengan selembar plastik bersih, Nadia mengepal nasi itu bulat-bulat, membentuk kepala beruang lucu dengan dua telinga kecil di atasnya.",
                "textEn": "From the rice cooker, Nadia scooped a warm handful of fragrant, fluffy white rice. Using a clean wrap, Nadia rolled and molded the rice into a round, cute little bear face with two perky round ears on top.",
                "quote": "🍚 'Makanan yang dibentuk dengan cinta membawa kebahagiaan bahkan sebelum disantap.'",
                "coReading": "💡 Aktivitas Seru: Tirukan gerakan mengepal-ngepal nasi di tanganmu bersama si kecil: 'Kepal, kepal, jadi beruang!'",
                "imagePrompt": "Close-up illustration of Nadia's hands shaping fluffy white rice into an adorable bear-shaped onigiri on a wooden cutting board, wax crayon scribbles and soft chalky pastel, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Mata Nori dan Hidung Zaitun",
                "titleEn": "Nori Seaweed Eyes and Olive Nose",
                "textId": "Dengan gunting dapur kecil, Nadia memotong rumput laut nori hitam menjadi dua lingkaran mata kancing dan sebuah senyuman melengkung. Cring! Bola nasi beruang itu kini tersenyum ramah seolah menyapa Rio.",
                "textEn": "With tiny kitchen scissors, Nadia clipped black nori seaweed into two round dot eyes and a gentle curving smile. Snap! The rice bear now smiled warmly, as if greeting Rio with cheerful encouragement.",
                "quote": "😊 'Satu senyuman kecil pada makanan bisa menghapus rasa cemas sepanjang hari.'",
                "coReading": "💡 Tanya si Kecil: Bentuk wajah apa yang paling kamu sukai jika nasi bekalmu dihias?",
                "imagePrompt": "Touching children's book scene of Nadia carefully using tweezers to place tiny nori seaweed eyes and smile on the bear rice ball. A bowl of edamame and cherry tomatoes sits nearby, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Gulungan Telur Emas Tamagoyaki",
                "titleEn": "Golden Tamagoyaki Egg Rolls",
                "textId": "Di atas wajan kecil, Nadia dan Ibu mendadar telur kocok kuning cerah. Gulung, gulung, gulung... Telur dadar itu digulung rapi lalu dipotong menjadi lingkaran-lingkaran emas yang lembut dan manis berkaldu.",
                "textEn": "Upon a small skillet, Nadia and Mama cooked a beaten egg of sunny golden yellow. Roll, roll, roll... The omelet was gently rolled and sliced into tender, sweet golden pinwheels.",
                "quote": "🍳 'Kuning telur yang cerah seperti sinar matahari pagi yang menghangatkan jiwa.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana rasa telur gulung kesukaanmu?",
                "imagePrompt": "Vibrant illustration of sliced golden yellow rolled omelet pinwheels arranged neatly in a bamboo dish, with morning steam rising softly, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Bintang Wortel Rebus yang Manis",
                "titleEn": "Sweet Boiled Carrot Stars",
                "textId": "Nadia mencetak irisan wortel rebus menjadi bintang-bintang jingga kecil. Ditambah dua kuntum brokoli hijau mini dan sebutir tomat ceri merah, kotak bekal itu kini penuh warna seperti taman bunga musim semi.",
                "textEn": "Nadia pressed a star cutter through tender boiled carrot rounds into miniature orange stars. Adding two tiny green broccoli florets and a bright red cherry tomato, the lunchbox bloomed into a vibrant spring garden.",
                "quote": "⭐ 'Sayuran beraneka warna membuat tubuh kita kuat dan mata kita berbinar sehat.'",
                "coReading": "💡 Hitung Bersama: Coba hitung bintang-bintang wortel yang ada di dalam kotak bekal!",
                "imagePrompt": "Charming close-up picture book illustration of the yellow bento box packed with bear onigiri, star carrots, golden egg rolls, green broccoli, and red cherry tomato, looking cheerful and appetizing, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Surat Rahasia Bergambar Pelangi",
                "titleEn": "The Secret Rainbow Note",
                "textId": "Sebelum menutup kotak bekal, Nadia menyelipkan selembar kertas kecil bergambar pelangi di bawah tutupnya. Tulisannya rapi: 'Semangat sekolah adikku sayang! Kakak selalu bangga padamu.'",
                "textEn": "Before snapping the lid shut, Nadia slipped a small folded card drawn with a bright rainbow under the elastic band. It read in neat letters: 'Have a wonderful day at school, dear Rio! Big sister is so proud of you.'",
                "quote": "💌 'Kata-kata penyemangat dari keluarga adalah jimat keberanian paling ampuh.'",
                "coReading": "💡 Pesan Kasih: Katakan kalimat penyemangat paling manis untuk adik atau saudaramu hari ini!",
                "imagePrompt": "Sweet children's illustration of Nadia placing a folded rainbow card gently into the lunchbox bag, tying it with a yellow ribbon, smiling with sisterly pride, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Membuka Bekal di Meja Sekolah",
                "titleEn": "Opening the Box at the School Table",
                "textId": "Siang hari di sekolah, bel istirahat berbunyi. Rio yang semula pendiam duduk di meja makannya. Saat membuka kotak bekal kuningnya, mata Rio terbelalak gembira: beruang nasi kecil tersenyum menyapanya!",
                "textEn": "At midday at preschool, the recess bell rang. Rio, who had been quiet all morning, sat at the low wooden lunch table. When he popped open his yellow bento box, his eyes widened with pure delight: the smiling rice bear welcomed him!",
                "quote": "🍱 'Membuka bekal dari rumah terasa seperti membuka pelukan keluarga di tengah tempat asing.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana perasaan Rio saat melihat bekal buatan kakaknya yang lucu?",
                "imagePrompt": "Heartwarming storybook scene of toddler Rio sitting at a colorful preschool table, grinning happily with wide eyes as he looks at his beautiful lunchbox. Other children look over with curious friendly smiles, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Teman Baru yang Duduk Bersama",
                "titleEn": "New Friends Sitting Side by Side",
                "textId": "\"Lucu sekali beruang nasimu!\" puji seorang anak laki-laki bertopi dinosaurus di sebelahnya. Rio tersenyum bangga dan membagikan sebutir wortel bintangnya. Rasa cemas seketika lenyap, berganti tawa riang bersama teman baru.",
                "textEn": "\"Your rice bear is so cute!\" admired a little boy wearing a dinosaur cap sitting nearby. Rio beamed proudly and shared a tiny star carrot. All his worries dissolved away, replaced by merry laughter with new playmates.",
                "quote": "🤝 'Kebaikan yang kita bawa dari rumah menjadi jembatan terindah untuk menyapa sahabat baru.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana caramu mengajak teman baru mengobrol di sekolah?",
                "imagePrompt": "Joyous children's illustration of Rio sharing a star carrot with a smiling new school friend at the kindergarten lunch table, both laughing merrily, soft crayon folk art, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Damai Bergandengan Tangan",
                "titleEn": "Peaceful Sleep Holding Hands",
                "textId": "Malam tiba membawa kelegaan di rumah mereka. Kotak bekal telah dicuci bersih dan kering di rak piring. Di kamar tidur, Nadia dan Rio terlelap damai berselimut hangat, saling berpegangan tangan dalam tidur yang tenang. Selamat tidur, kakak dan adik yang saling mengasihi.",
                "textEn": "Night descended carrying sweet relief to their home. The little lunchbox lay washed and dry upon the dish rack. In the bedroom, Nadia and Rio slept peacefully under a warm quilt, holding hands in tranquil slumber. Goodnight, loving brother and sister.",
                "quote": "🌙 'Kasih sayang persaudaraan adalah pelita abadi yang menjaga tidur malam tetap hangat dan damai.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak penyayang, semoga rasa kasih sayang di hatimu selalu mekar setiap hari.",
                "imagePrompt": "Serene bedtime illustration of sister Nadia and little brother Rio sleeping side by side in a cozy twin bed under a patchwork quilt, soft moonlight streaming through the window, handcrafted wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s55)

    # =========================================================================
    # STORY 56: Langkah Kura-kura & Sayap Walet
    # =========================================================================
    s56 = {
        "id": "langkah-kura-walet",
        "storyNumber": 56,
        "title": "Langkah Kura-kura & Sayap Walet",
        "englishTitle": "Turtle Steps and Swallow Wings",
        "category": "persahabatan",
        "categoryLabel": "🤝 Persahabatan & Inklusivitas",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Dua sahabat berbeda kecepatan yang saling menghargai dan melengkapi tanpa membanding-bandingkan",
        "cover": "images/story56_cover.jpg",
        "coverImage": "images/story56_cover.jpg",
        "synopsis": "Tomi si kura-kura berjalan sangat lambat di atas pasir karang, sementara Wali si burung walet melesat secepat angin di langit luas. Meskipun hidup di dunia dan ritme yang berbeda, mereka adalah sahabat sejati yang saling menceritakan keajaiban bumi dan langit setiap senja tiba.",
        "synopsisEn": "Tomi the tortoise moves slow and steady across coastal rocks, while Wali the swift swallow swoops like the wind across endless skies. Though living in different rhythms, they are truest companions who meet at sunset to share the wonders of earth and sky.",
        "protagonist": "Tomi (Kura-kura darat kecil bertempurung motif lumut berhati sabar)",
        "companion": "Wali (Burung walet laut ramping bersayap sabit dengan ekor garpu lincah)",
        "setting": "Pesisir Tebing Karang Laut & Padang Rumput Angin Semilir",
        "pages": [
            {
                "number": 1,
                "title": "Dua Sahabat dari Dua Alam",
                "titleEn": "Two Friends from Two Worlds",
                "textId": "Di tebing karang yang menatap Samudra Biru, hiduplah dua sahabat yang paling berbeda di seluruh pantai. Tomi si kura-kura yang melangkah sangat pelan di tanah, dan Wali si burung walet yang terbang secepat kilat di angkasa.",
                "textEn": "On the coastal cliff overlooking the Azure Ocean lived two friends as different as night and day. Tomi the tortoise, who walked very slowly on the earth, and Wali the swallow, who soared as swift as lightning in the sky.",
                "quote": "🐢 'Perbedaan bukanlah pemisah, melainkan jembatan untuk saling melengkapi.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu memiliki teman yang cara bicaranya atau cara berjalannya berbeda denganmu?",
                "imagePrompt": "Charming children's book illustration of little land tortoise Tomi looking up from a mossy cliff edge as sleek swallow Wali swoops playfully low above him against a sea breeze. Handcrafted wax crayon on textured cream paper, simple black bead eyes, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Langkah Sabar Menatap Kerikil",
                "titleEn": "Patient Steps Observing Pebbles",
                "textId": "Tomi melangkah setapak demi setapak: plok... plok... plok... Karena berjalan perlahan, Tomi bisa melihat bunga lumut terkecil di sela karang, kerang emas mungil, dan semut-semut yang sedang bercakap-cakap di akar rumput.",
                "textEn": "Tomi stepped one deliberate pace at a time: plop... plop... plop... Because he moved so slowly, Tomi could see the tinniest moss blossoms, miniature golden shells, and friendly ants chatting along grass roots.",
                "quote": "🔍 'Berjalan perlahan memungkinkan mata kita menangkap keindahan tersembunyi di atas bumi.'",
                "coReading": "💡 Aktivitas Seru: Berjalanlah sangat lambat seperti kura-kura Tomi: 'Saaatuuu... duuuaaa...'",
                "imagePrompt": "Close-up storybook scene of tortoise Tomi admiring tiny flowering moss and a spiral yellow seashell on a coastal rock, wax crayon textures, rich moss greens and earthy tones, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Sayap Sabit Menari di Angkasa",
                "titleEn": "Sickle Wings Dancing in the Sky",
                "textId": "Wuuush! Wali meluncur menukik dari awan putih, membelah angin laut dengan sayap sabitnya yang ramping. Dari atas langit, Wali bisa melihat garis pulau yang melengkung indah dan kapal nelayan yang tampak seperti perahu kertas.",
                "textEn": "Whoooosh! Wali swooped down from drifting clouds, slicing through the ocean breeze with sleek sickle wings. From high above, Wali could see the curving shoreline and fishing boats that looked like tiny paper sailboats.",
                "quote": "🕊️ 'Terbang tinggi membuka cakrawala luas tentang betapa megahnya dunia ini.'",
                "coReading": "💡 Aktivitas Seru: Rentangkan kedua tanganmu seperti sayap burung walet dan melayanglah pelan!",
                "imagePrompt": "Vibrant illustration of swallow Wali soaring high above a turquoise ocean with whitecaps and distant miniature islands, under a brilliant sunlit sky, wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Tidak Pernah Mengejek Kecepatan",
                "titleEn": "Never Mocking Each Other's Pace",
                "textId": "Wali tidak pernah mengejek Tomi karena jalannya yang lambat, dan Tomi tidak pernah cemburu pada sayap Wali yang cepat. Mereka saling mengagumi keistimewaan masing-masing dengan hati yang tulus.",
                "textEn": "Wali never teased Tomi for his plodding gait, and Tomi never envied Wali's swift wings. Each genuinely admired the other's unique gifts with an open, affectionate heart.",
                "quote": "💖 'Persahabatan sejati tidak mengenal perlombaan; persahabatan adalah tentang saling menghargai.'",
                "coReading": "💡 Tanya si Kecil: Mengapa kita tidak boleh membanding-bandingkan diri kita dengan teman lain?",
                "imagePrompt": "Touching children's picture book scene of swallow Wali perched peacefully on a flat sun-warmed stone beside tortoise Tomi, looking at each other with warm smiling eyes, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Batu Pertemuan Waktu Senja",
                "titleEn": "The Twilight Meeting Stone",
                "textId": "Setiap sore saat matahari mulai condong ke ufuk laut, mereka selalu bertemu di Batu Karang Datar di tepi tebing. Wali melipat sayapnya dan bertengger tenang di samping tempurung hijau lumut Tomi.",
                "textEn": "Every evening as the sun leaned toward the sea, they met at the Flat Coastal Boulder at the cliff's edge. Wali folded his wings and perched comfortably beside Tomi's moss-green shell.",
                "quote": "🌅 'Waktu yang disisihkan untuk sahabat adalah waktu yang paling berharga dalam sehari.'",
                "coReading": "💡 Tanya si Kecil: Kapan waktu favoritmu untuk bercerita dengan sahabat atau orang tua?",
                "imagePrompt": "Picturesque storybook illustration of tortoise Tomi and swallow Wali sitting together on a smooth seaside rock as the sunset sky turns shades of apricot, peach, and lavender, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Cerita dari Atas Langit Lepas",
                "titleEn": "Stories from the Boundless Sky",
                "textId": "Wali mulai bercerita dengan mata berbinar: tentang paus raksasa yang menyemburkan air mancur perak di tengah samudra, dan formasi awan merah muda yang tampak seperti istana kapas terapung.",
                "textEn": "Wali began his tale with sparkling eyes: telling of giant whales spouting silver fountains out at sea, and pink cloud castles that drifted across sunset skies like floating cotton islands.",
                "quote": "☁️ 'Mendengarkan cerita sahabat seperti membuka jendela ke dunia yang belum pernah kita lihat.'",
                "coReading": "💡 Tanya si Kecil: Jika kamu bisa terbang seperti burung, tempat apa yang ingin kamu lihat dari atas?",
                "imagePrompt": "Whimsical illustration with a dream bubble showing a friendly whale spouting water in the sea and floating pink clouds, as Wali chirps animatedly to listening tortoise Tomi, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Rahasia dari Dasar Bumi",
                "titleEn": "Secrets from the Ancient Earth",
                "textId": "Lalu giliran Tomi bertutur dengan suara berat dan tenang: tentang biji bunga dandelion yang baru bertunas di bawah tanah, dan mata air kecil tersembunyi yang airnya sedingin es batu.",
                "textEn": "Then it was Tomi's turn to speak in his deep, soothing voice: telling of tiny dandelion seeds sprouting in the dark soil, and a secret hidden freshwater spring cold as pure mountain ice.",
                "quote": "🌱 'Kebijaksanaan bumi yang tenang melengkapi kegembiraan langit yang bebas.'",
                "coReading": "💡 Tanya si Kecil: Hal menarik apa yang pernah kamu amati di bawah tanah atau di rumput pekarangan?",
                "imagePrompt": "Delightful illustration showing Tomi gently pointing his snout toward a tiny sprouting green seedling between the rocks, with swallow Wali leaning down listening with keen interest, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Melindungi Sahabat dari Angin Dingin",
                "titleEn": "Sheltering a Friend from Coastal Chills",
                "textId": "Saat angin laut berhembus kencang dan dingin, Wali menggigil kecil. Tomi membuka sedikit celah tempurungnya yang tebal dan hangat, membiarkan Wali bersandar nyaman terlindung dari terpaan angin malam.",
                "textEn": "When a gust of sharp ocean wind blew cold, Wali shivered slightly. Tomi drew close and offered the sheltered side of his thick, sturdy shell, letting Wali tuck in warmly away from the coastal chill.",
                "quote": "🛡️ 'Kekuatan kita ada untuk melindungi sahabat yang sedang membutuhkan perlindungan.'",
                "coReading": "💡 Peluk Hangat: Berikan pelukan hangat untuk sahabat atau saudaramu agar merasa nyaman!",
                "imagePrompt": "Heartwarming storybook scene of swallow Wali snuggled against the warm mossy side of tortoise Tomi's shell under a protective stone alcove while wind rustles the wild grasses, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Bintang-Bintang Laut dan Langit",
                "titleEn": "Stars of the Sea and Sky",
                "textId": "Malam tiba menggelar tirai berbintang. Di langit atas, bintang perak berkelap-kelip. Di air laut bawah tebing, plankton menyala biru kehijauan seperti bintang air. Kedua sahabat memandangi keajaiban itu dalam keheningan yang penuh syukur.",
                "textEn": "Night descended drawing a starry velvet curtain. High above, silver stars twinkled brightly. Down in the calm tide pools below, glowing plankton sparked blue like water-stars. Both friends gazed upon the wonder in grateful hush.",
                "quote": "✨ 'Dunia ini penuh keajaiban saat kita menyaksikannya bersama sahabat sejati.'",
                "coReading": "💡 Pejamkan Mata: Bayangkan ribuan bintang berkelip lembut di langit malam yang damai.",
                "imagePrompt": "Breathtaking children's book illustration of starry night over the sea cliff. Sky is dusted with golden stars, and the sea below glows with bioluminescent turquoise waves. Tomi and Wali sit side by side in quiet companionship, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Tenang di Bawah Naungan Karang",
                "titleEn": "Tranquil Sleep Beneath the Rock Arch",
                "textId": "Di dalam ceruk batu karang yang hangat, Tomi menarik kepalanya ke dalam tempurung dengan damai. Di dahan kecil di atasnya, Wali tidur pulas menyelipkan paruhnya di balik sayap. Dua sahabat tidur lelap dalam harmoni malam yang indah. Selamat tidur, kura-kura bijak dan walet pemberani.",
                "textEn": "Inside a sheltered alcove beneath a natural stone arch, Tomi tucked his head into his shell in peaceful slumber. On a little ledge just above, Wali slept deeply with beak tucked under wing. Two friends fast asleep in nocturnal harmony. Goodnight, wise tortoise and brave swallow.",
                "quote": "🌙 'Tidurlah dalam damai, karena persahabatan yang tulus adalah rumah paling aman di bumi.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak baik, semoga kamu selalu memiliki sahabat-sahabat sejati yang saling mengasihi.",
                "imagePrompt": "A peaceful, cozy bedtime illustration of tortoise Tomi asleep in his mossy shell inside a rocky seaside cave, with swallow Wali asleep perched above him. Moonbeams illuminate the cave entrance, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s56)

    # =========================================================================
    # STORY 57: Gajah Kecil Bertelinga Payung
    # =========================================================================
    s57 = {
        "id": "gajah-telinga-payung",
        "storyNumber": 57,
        "title": "Gajah Kecil Bertelinga Payung",
        "englishTitle": "The Little Elephant's Umbrella Ears",
        "category": "persahabatan",
        "categoryLabel": "🤝 Persahabatan & Inklusivitas",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Menerima keunikan diri, rasa percaya diri, dan menolong teman dengan kelebihan kita",
        "cover": "images/story57_cover.jpg",
        "coverImage": "images/story57_cover.jpg",
        "synopsis": "Elphi si anak gajah biru sering merasa malu karena memiliki daun telinga yang jauh lebih lebar dan besar daripada gajah-gajah lainnya. Namun saat badai hujan lebat mendadak mengguyur padang rumput sabana, telinga lebar Elphi menjadi payung peneduh ajaib yang menyelamatkan seluruh hewan kecil dari kedinginan.",
        "synopsisEn": "Little blue elephant Elphi feels self-conscious about having enormous, floppy ears much bigger than other calves. But when a sudden thunderstorm drenches the savannah meadow, Elphi's giant ears become a magical umbrella sheltering all woodland creatures from the chill.",
        "protagonist": "Elphi (Anak gajah kecil berwarna biru pastel bertelinga sangat lebar dan ramah)",
        "companion": "Poli si Tupai & Kiki si Pipit (Sahabat-sahabat kecil padang rumput sabana)",
        "setting": "Padang Rumput Sabana yang Luas Berpohon Baobab",
        "pages": [
            {
                "number": 1,
                "title": "Telinga Lebar yang Sering Disembunyikan",
                "titleEn": "Wide Ears Often Hidden Away",
                "textId": "Di padang rumput sabana yang luas, hiduplah Elphi si anak gajah kecil berbulu halus biru pastel. Elphi memiliki dua telinga yang sangat lebar seperti daun teratai raksasa. Seringkali, Elphi melipat telinganya ke belakang karena merasa malu terlihat berbeda.",
                "textEn": "Across the vast savannah meadow lived Elphi, a petite pastel-blue elephant calf. Elphi had two enormous, floppy ears as wide as giant lotus leaves. Often, Elphi tucked his ears back shyly, feeling self-conscious about looking different from other calves.",
                "quote": "🐘 'Kadang kita merasa malu pada hal-hal yang justru membuat diri kita istimewa.'",
                "coReading": "💡 Tanya si Kecil: Bagian tubuh apa yang membuatmu merasa unik dan lucu?",
                "imagePrompt": "Charming children's book illustration of adorable toddler blue elephant Elphi walking shyly through tall golden savannah grass, with unusually large, soft floppy ears. Handcrafted wax crayon and chalky oil pastel, textured cream paper, simple black bead eyes, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Bermain Bersama Sahabat Mungil",
                "titleEn": "Playing with Tiny Companions",
                "textId": "Meskipun pemalu, Elphi sangat disayangi oleh hewan-hewan kecil. Poli si tupai tanah sering melompat ke belalai Elphi, dan Kiki si burung pipit gemar bernyanyi di atas punggungnya sambil menyusuri pohon baobab.",
                "textEn": "Though shy, Elphi was deeply adored by the small creatures. Poli the ground squirrel loved balancing on Elphi's curling trunk, and Kiki the sparrow sang sweet melodies on his back as they strolled beneath baobab trees.",
                "quote": "🐿️ 'Kebaikan hati yang ramah selalu menarik sahabat-sahabat terbaik ke dekat kita.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara belalai gajah meniup angin: 'Fyuuuh... trompet gajah!'",
                "imagePrompt": "Delightful storybook scene of little blue elephant Elphi smiling gently as squirrel Poli balances on his trunk tip and little bird Kiki perches on his head, warm sunny savannah grassland, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Awan Kelabu Bergulung Tiba-Tiba",
                "titleEn": "Dark Rainclouds Roll in Suddenly",
                "textId": "Tiba-tiba, angin kencang bertiup dingin. Langit biru sabana mendadak berubah menjadi abu-abu gelap. Awan mendung tebal bergulung cepat di atas kepala mereka, membawa guruh yang menggelegar pelan di kejauhan.",
                "textEn": "Suddenly, a brisk chilly wind swept across the plain. The brilliant blue savannah sky turned a deep, dusky gray. Heavy storm clouds rolled swiftly overhead, carrying a distant, muffled rumble of thunder.",
                "quote": "🌧️ 'Cuaca di alam bisa berubah dalam sekejap, menguji kesiapsiagaan kita.'",
                "coReading": "💡 Tanya si Kecil: Apa yang kamu rasakan saat melihat awan mendung gelap di langit?",
                "imagePrompt": "Dramatic yet gentle storybook illustration of dark rain clouds gathering over the vast savannah landscape, with baobab trees swaying in the wind, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Tetesan Air Hujan yang Deras",
                "titleEn": "Heavy Splashing Raindrops",
                "textId": "Tik... tik... tik... BYURRR! Hujan badai lebat mengguyur padang rumput tanpa ampun. Tidak ada pohon rindang di dekat situ, dan sarang hewan-hewan kecil masih sangat jauh di seberang sungai.",
                "textEn": "Pitter... patter... WHOOSH! A torrential downpour crashed upon the savannah meadow without warning. There were no shady trees nearby, and the tiny creatures' burrows were far across the swollen brook.",
                "quote": "⛈️ 'Saat badai datang, makhluk yang paling kecil selalu membutuhkan pertolongan pertama.'",
                "coReading": "💡 Aktivitas Seru: Ketukkan jemarimu ke meja seperti suara hujan deras: 'Tik-tok-tik-tok-byuur!'",
                "imagePrompt": "Atmospheric children's book illustration of heavy rain sheets falling over the savannah grass. Little ground squirrels and field mice huddle shivering in the puddles, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Hewan-Hewan Kecil yang Menggigil",
                "titleEn": "Little Animals Shivering in the Wet",
                "textId": "Poli si tupai basah kuyup hingga bulu ekornya lepek. Tiga anak kelinci hutan menggigil kedinginan di bawah semak berduri yang bocor. Mereka ketakutan dan tidak tahu harus berlindung di mana.",
                "textEn": "Poli the squirrel was drenched to the skin, his fluffy tail dripping wet. Three baby rabbits huddled shivering under a leaky thorn bush. They whimpered in fear, having nowhere dry to shelter.",
                "quote": "😟 'Melihat teman kedinginan menggerakkan hati kita untuk segera bertindak.'",
                "coReading": "💡 Tanya si Kecil: Apa yang kamu lakukan saat melihat temanmu kehujanan di jalan?",
                "imagePrompt": "Touching illustration of wet baby rabbits and a shivering squirrel huddled together under a leaky thistle leaf, water droplets splashing all around, soft crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Membuka Telinga Lebar-Lebar",
                "titleEn": "Spreading Ears Wide Like Umbrellas",
                "textId": "Melihat kawan-kawannya dalam bahaya, Elphi tidak berpikir dua kali. Ia berlutut di tanah berumput. Fwaaap! Elphi melebarkan kedua daun telinganya ke kanan dan ke kiri seluas-luasnya seperti kanopi payung kembar yang megah.",
                "textEn": "Seeing his dear companions in distress, Elphi didn't hesitate for a second. He knelt down upon the grassy lawn. FWUMP! Elphi unfurled both of his enormous floppy ears to the left and right, spreading them wide like grand twin canopy umbrellas.",
                "quote": "🐘 'Keunikan kita yang sesungguhnya diciptakan untuk menjadi berkat bagi sesama.'",
                "coReading": "💡 Aktivitas Seru: Rentangkan kedua tanganmu lebar-lebar seperti payung pelindung yang kokoh!",
                "imagePrompt": "Heroic and adorable children's book scene of little blue elephant Elphi kneeling down, spreading his giant soft ears out wide to create a huge dry canopy beneath him, rain bouncing off his ears, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Tenda Teduh di Bawah Telinga Elphi",
                "titleEn": "A Dry Haven Beneath Elphi's Ears",
                "textId": "\"Cepat masuk ke bawah sini!\" seru Elphi ramah. Poli si tupai, anak-anak kelinci, katak kecil, dan burung-burung pipit berlarian masuk ke bawah naungan telinga Elphi. Di bawah sana, udara terasa kering, hangat, dan terlindung dari guyuran air.",
                "textEn": "\"Quick, tuck in beneath here!\" called Elphi warmly. Poli the squirrel, the baby bunnies, little tree frogs, and baby sparrows scurried beneath the shelter of Elphi's ears. Underneath, it was wonderfully dry, cozy, and safe from the storm.",
                "quote": "☂️ 'Perlindungan yang tulus membuat tempat yang paling basah sekalipun terasa hangat.'",
                "coReading": "💡 Tanya si Kecil: Siapa saja hewan kecil yang berlindung di bawah telinga Elphi? Tunjuk di gambar!",
                "imagePrompt": "Heartwarming illustration looking beneath Elphi's wide ear canopy: baby rabbits, squirrels, and birds huddled together dry and cozy on green clover, smiling up with deep gratitude, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Hujan Mereda dan Pelangi Muncul",
                "titleEn": "Rain Subsides and Rainbow Appears",
                "textId": "Badai perlahan mereda menjadi gerimis tipis. Matahari sore menyembul kembali menembus awan, membiaskan lengkungan pelangi tujuh warna di atas sabana. Air di atas telinga Elphi meluncur jatuh seperti tirai air terjun kristal.",
                "textEn": "The storm gradually softened into a gentle misty drizzle. The afternoon sun broke through the clouds, painting a radiant seven-colored rainbow arch over the savannah. Rainwater slid off Elphi's ears like crystalline waterfall curtains.",
                "quote": "🌈 'Setiap badai pasti akan berlalu, menyisakan pelangi yang indah dan rasa syukur.'",
                "coReading": "💡 Sebutkan Warna: Sebutkan warna-warni pelangi yang kamu ketahui bersama si kecil!",
                "imagePrompt": "Magnificent children's picture book scene of the rain clearing over the green savannah, with a brilliant rainbow arching across the sky. Little animals emerge happily from beneath Elphi's ears, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Sorak-Sorai Sahabat Sabana",
                "titleEn": "Cheers from Savannah Friends",
                "textId": "\"Horeee untuk Elphi! Telinga Elphi adalah payung terbaik di seluruh dunia!\" seru hewan-hewan kecil sambil menari gembira. Elphi tersipu malu, tetapi kali ini pipinya kemerahan oleh rasa bahagia dan bangga pada telinganya.",
                "textEn": "\"Hooray for Elphi! Elphi's ears are the greatest umbrellas in the whole wide world!\" cheered the little animals, dancing with joy. Elphi blushed bashfully, but this time his cheeks glowed with genuine happiness and pride in his unique ears.",
                "quote": "🎉 'Saat kita menerima diri kita apa adanya, orang lain pun akan melihat keindahan sejati kita.'",
                "coReading": "💡 Berikan Pujian: Puji satu kelebihan unik yang dimiliki si kecil agar ia semakin percaya diri!",
                "imagePrompt": "Joyous illustration of little woodland and savannah animals hugging Elphi's trunk and cheering around him, while Elphi smiles broadly with ears perked up proudly, wax crayon folk art, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Nyenyak Berpayung Kasih",
                "titleEn": "Deep Slumber Under Love's Canopy",
                "textId": "Malam tiba dengan taburan bintang yang berkilau di langit sabana yang jernih. Di bawah pohon baobab tua, Elphi berbaring nyaman di atas rumput harum. Kedua telinga lebarnya kini membungkus tubuhnya sendiri seperti selimut sutra yang hangat. Selamat tidur, gajah kecil bertelinga ajaib.",
                "textEn": "Night settled with sparkling stars scattered across the clear savannah sky. Beneath the ancient baobab tree, little Elphi lay peacefully upon the fragrant grass. His two wide ears now wrapped around his own body like a warm silk quilt. Goodnight, brave elephant with magical ears.",
                "quote": "🌙 'Tidurlah dengan damai dan rasa bangga, karena setiap ciptaan Tuhan sungguh sempurna adanya.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak istimewa, kamu diciptakan dengan indah dan begitu berharga di dunia ini.",
                "imagePrompt": "A tranquil, comforting bedtime illustration of baby blue elephant Elphi sleeping peacefully under a starry African night sky beneath a silhouette baobab tree, his large ears wrapped snugly around him like a cozy blanket, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s57)

    return stories

print("Story module 55-57 defined successfully")
