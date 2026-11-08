# scripts/polish_stories_51_to_54.py
import json

def get_stories_51_to_54():
    stories = []

    # =========================================================================
    # STORY 51: Madu Secukupnya untuk Beruang
    # =========================================================================
    s51 = {
        "id": "madu-secukupnya-beruang",
        "storyNumber": 51,
        "title": "Madu Secukupnya untuk Beruang",
        "englishTitle": "Just Enough Honey for Bear",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Belajar mengambil secukupnya, tidak serakah, dan menghargai kerja keras alam",
        "cover": "images/story51_cover.jpg",
        "coverImage": "images/story51_cover.jpg",
        "synopsis": "Baru si anak beruang madu sangat menyukai madu hutan yang manis berkilau. Saat memanjat pohon sarang lebah, Baru belajar dari Ratu Lebah bahwa mengambil secukupnya di mangkuk kecil dan menyisakan untuk kawan-kawan lebah adalah rahasia menjaga hutan tetap manis selamanya.",
        "synopsisEn": "Little Baru the honey bear adores sweet golden forest honey. When climbing to the hive tree, Baru learns from the Queen Bee that taking only what is needed and leaving the rest for the hive keeps the whole forest sweet and joyful forever.",
        "protagonist": "Baru (Anak beruang madu cokelat karamel bercelana kodok denim biru)",
        "companion": "Ratu Lebah (Lebah madu emas anggun bersayap kaca gemerlap)",
        "setting": "Dahan Pohon Madu Raksasa & Hutan Bunga Liar Beraroma Nektar",
        "pages": [
            {
                "number": 1,
                "title": "Mangkuk Tanah Liat Kosong Baru",
                "titleEn": "Baru's Empty Clay Bowl",
                "textId": "Pagi itu, Baru si anak beruang madu menatap ke dasar mangkuk tanah liatnya yang kosong melompong. Tidak ada lagi tetesan madu manis untuk sarapannya. Perut bulatnya berbunyi pelan: kruyuk-kruyuk!",
                "textEn": "That morning, Baru the little honey bear peered into the bottom of his little clay bowl, which sat completely empty. Not a single golden drop remained for breakfast. His round tummy rumbled softly: rumble-tumble!",
                "quote": "🍯 'Rasa lapar yang sederhana mengingatkan kita untuk mencari rezeki dengan rasa syukur.'",
                "coReading": "💡 Tanya si Kecil: Makanan manis apa yang paling kamu sukai di pagi hari?",
                "imagePrompt": "Charming children's book illustration of toddler honey bear Baru in denim overalls sitting on a tree stump, looking curiously into an empty clay bowl with a gentle pout. Morning sun in a green woodland, handcrafted wax crayon and soft oil pastel on cream paper, simple black bead eyes, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Aroma Manis di Atas Dahan",
                "titleEn": "Sweet Aroma High in the Branches",
                "textId": "Mengikuti hidung hitamnya yang mengendus-endus udara, Baru berjalan menuju Pohon Madu Raksasa di tengah hutan. Di atas dahan tertinggi, terdengar dengungan ribuan sayap lebah yang sibuk: bzzz... bzzz... bzzz!",
                "textEn": "Following his little black nose sniffing the air, Baru trotted toward the Giant Honey Tree at the forest center. High up among the thickest boughs, thousands of busy little bee wings hummed in merry chorus: bzzz... bzzz... bzzz!",
                "quote": "🐝 'Dengungan lebah yang rajin adalah suara kerja keras yang menghasilkan kebaikan manis.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara dengungan lebah madu bersama si kecil: 'Bzzzzzz... bzzzzzz!'",
                "imagePrompt": "Whimsical storybook scene of little bear Baru standing at the base of a huge mossy ancient oak tree looking up toward a large glowing golden beehive. Flowers bloom at the roots, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Memanjat dengan Hati-Hati",
                "titleEn": "Climbing with Careful Paws",
                "textId": "Dengan cakar-cakar kecilnya yang tumpul dan kuat, Baru memanjat batang pohon berlumut itu setapak demi setapak. Di pinggangnya terikat sebuah toples tembikar kecil bertali rami.",
                "textEn": "With his blunt, sturdy little climbing paws, Baru scrambled up the mossy tree trunk one careful step at a time. Fastened around his waist was a small earthenware jar tied with hemp twine.",
                "quote": "🐾 'Memanjat perlahan dan penuh kehati-hatian menjaga langkah kita tetap aman.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu memanjat tangga atau ayunan di taman bermain?",
                "imagePrompt": "A picture book illustration of little bear Baru hugging a thick tree trunk, climbing upward with a determined smile, a small pottery jar tied to his belt. Soft green leaves, dappled sunlight, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Sarang Emas dan Ratu Lebah",
                "titleEn": "The Golden Hive and the Queen Bee",
                "textId": "Di atas dahan lebar, tergantung sarang madu yang berkilau seperti istana lilin keemasan. Dari lubang sarang, Ratu Lebah yang bersayap bening terbang mendekat dan bertengger anggun di ujung hidung Baru.",
                "textEn": "Upon a wide branch hung a honeycomb glistening like an amber wax palace. From the hive entrance, the Queen Bee with translucent shimmering wings drifted forward, perching gracefully right on Baru's button nose.",
                "quote": "👑 'Menyapa sahabat alam dengan lembut akan disambut dengan keramahan yang sama.'",
                "coReading": "💡 Aktivitas Seru: Tahan napas sejenak dan bayangkan ada kupu-kupu atau lebah kecil hinggap di hidungmu!",
                "imagePrompt": "Heartwarming storybook illustration of a glowing golden Queen Bee with crown-like antennae perched gently on the nose of little bear Baru, who giggles softly without moving. Warm golden lighting, wax crayon on heavy paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Pesan Bijak Ratu Lebah",
                "titleEn": "The Queen Bee's Wise Words",
                "textId": "\"Selamat pagi, Baru kecil,\" sapa Ratu Lebah dengan suara berdenting merdu. \"Kami mengumpulkan nektar dari sejuta bunga liar. Kamu boleh mengambil madu kami, tetapi hanya satu toples kecil, ya. Jangan habiskan sarang kami.\"",
                "textEn": "\"Good morning, little Baru,\" greeted the Queen Bee in a chime-like voice. \"We gathered this nectar from a million wild blossoms. You may take our honey, but only one small jar, dear child. Leave the rest so our nursery stays warm.\"",
                "quote": "🌸 'Mengambil secukupnya adalah tanda rasa hormat kita kepada mereka yang telah bekerja keras.'",
                "coReading": "💡 Tanya si Kecil: Mengapa kita tidak boleh menghabiskan semua makanan jika orang lain juga membutuhkannya?",
                "imagePrompt": "Close-up storybook scene of little bear Baru nodding respectfully to the Queen Bee hovering before him near a dripping golden honeycomb, wax crayon scribbles, rich amber and honey tones, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Cidukan Madu yang Secukupnya",
                "titleEn": "A Modest Scoop of Honey",
                "textId": "Baru mengangguk patuh. Dengan sendok kayu kecilnya, ia mengambil madu keemasan yang kental dan harum bunga lavender, memasukkannya ke toplesnya sampai terisi tiga perempat penuh. Ia tidak mengambil lebih.",
                "textEn": "Baru nodded obediently. With his little wooden spoon, he scooped thick golden honey fragrant with lavender blossoms into his jar until it was three-quarters full. He took not a single drop more.",
                "quote": "🍯 'Kecukupan di dalam hati membuat sedikit hal terasa begitu melimpah ruah.'",
                "coReading": "💡 Aktivitas Seru: Tirukan gerakan menciduk madu yang kental dengan sendok kayu: 'Syuuur... kental sekali!'",
                "imagePrompt": "Delightful illustration of Baru carefully ladling thick, glowing amber honey into his small clay jar, leaving the rest of the honeycomb pristine and full. Bees buzz peacefully around him without stinging, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Terima Kasih pada Para Lebah",
                "titleEn": "Gratitude to the Little Bees",
                "textId": "\"Terima kasih, Ratu Lebah! Terima kasih, lebah-lebah pekerja!\" bisik Baru dengan mata berbinar. Lebah-lebah menari berputar di sekeliling kepala Baru sebagai tanda persahabatan yang tulus.",
                "textEn": "\"Thank you, Queen Bee! Thank you, busy worker bees!\" whispered Baru with shining eyes. The worker bees danced in merry circles around Baru's fuzzy ears in a joyful display of true friendship.",
                "quote": "💛 'Ucapan terima kasih yang tulus adalah madu termanis bagi hati siapa pun.'",
                "coReading": "💡 Ucapkan Bersama: Katakan 'Terima kasih' dengan suara lembut dan senyuman paling manis!",
                "imagePrompt": "Touching children's book scene of little bear Baru bowing politely from the tree branch, surrounded by friendly bees swirling in gentle golden spirals. Warm morning glow, soft pastel blending, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Sarapan Madu di Bawah Pohon",
                "titleEn": "Honey Breakfast Beneath the Tree",
                "textId": "Setelah turun ke tanah dengan selamat, Baru duduk di atas rumput semanggi. Ia mencelupkan buah apel hutan ke dalam toples madunya: nyam-nyam! Rasanya begitu manis, legit, dan menghangatkan seluruh tubuhnya.",
                "textEn": "After climbing safely back down, Baru sat upon the green clover grass. He dipped a crisp wild forest apple into his honey jar: crunch-munch! It tasted exquisitely sweet, rich, and warmed his whole tummy.",
                "quote": "🍎 'Makanan yang diperoleh dengan cara yang baik terasa berkali-kali lebih nikmat.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu mencelupkan buah apel ke dalam madu manis?",
                "imagePrompt": "Charming picture book illustration of toddler bear Baru sitting on a sunny mossy lawn, dipping a slice of crisp red apple into his clay jar of honey, chewing with blissfully round cheeks, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Membagikan Tetesan pada Semut Hutan",
                "titleEn": "Sharing a Drop with the Forest Ants",
                "textId": "Saat setetes madu jatuh di atas batu kerikil, sebaris semut kecil datang mendekat. Baru tidak mengusir mereka; ia justru tersenyum dan membiarkan semut-semut itu menikmati manisnya rezeki bersama-sama.",
                "textEn": "When a single drop of golden honey fell onto a smooth river stone, a line of tiny woodland ants marched up. Baru did not brush them away; instead, he smiled gently and let the little ants share in the sweet bounty.",
                "quote": "🐜 'Bahkan tetesan terkecil dari rezeki kita bisa menjadi pesta besar bagi makhluk yang lebih kecil.'",
                "coReading": "💡 Tanya si Kecil: Mengapa kita harus menyayangi makhluk-makhluk kecil di sekitar kita?",
                "imagePrompt": "Cute illustration of tiny black ants sipping a glistening drop of golden honey on a gray pebble, with little bear Baru resting his chin on his paws, watching them lovingly, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Pulas Berdengung Damai",
                "titleEn": "Sound Slumber in a Peaceful Hum",
                "textId": "Sore berganti malam yang sejuk di Hutan Hazel. Di dalam gua pohonnya yang empuk beralaskan daun kering harum, Baru memeluk toples madunya yang tersisa sedikit. Dengungan lebah-lebah yang damai mengiringi mimpi manisnya. Selamat tidur, beruang kecil yang bijaksana.",
                "textEn": "Dusk turned to cool night in Hazel Woods. Inside his snug tree hollow cushioned with sweet dried leaves, little Baru curled up hugging his little honey jar. The distant, peaceful hum of the hive carried him into sweet dreams. Goodnight, wise little bear.",
                "quote": "🌙 'Tidur yang paling damai adalah tidur setelah kita hidup selaras dengan alam sekitar.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak bijak, terima kasih sudah belajar merasa cukup dan selalu bersyukur hari ini.",
                "imagePrompt": "A peaceful bedtime illustration of little bear Baru sleeping curled up in a cozy hollow tree bedroom under a patchwork quilt, with his little honey jar resting beside him under the moonlight, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s51)

    # =========================================================================
    # STORY 52: Piknik Buah di Bawah Beringin
    # =========================================================================
    s52 = {
        "id": "piknik-buah-beringin",
        "storyNumber": 52,
        "title": "Piknik Buah di Bawah Beringin",
        "englishTitle": "Fruit Picnic Under the Banyan Tree",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Kesenangan berbagi bekal, menikmati keanekaragaman, dan persahabatan rukun",
        "cover": "images/story52_cover.jpg",
        "coverImage": "images/story52_cover.jpg",
        "synopsis": "Dita menggelar tikar pandan di bawah naungan pohon beringin tua yang teduh. Bersama kawan-kawannya yang membawa kotak bekal masing-masing, mereka saling bertukar potongan semangka merah, melon hijau, dan anggur ungu, menciptakan pelangi buah yang menyatukan semua hati.",
        "synopsisEn": "Little Dita unrolls a woven pandan mat beneath the cool shade of the ancient banyan tree. Gathering with her playground friends who each brought a snack box, they trade slices of red watermelon, green melon, and purple grapes into a colorful fruit rainbow.",
        "protagonist": "Dita (Gadis cilik 5 tahun bertopi anyaman jerami dan bergaun katun polkadot kuning)",
        "companion": "Kawan-kawan (Kinan, Bimo, dan Luki si kelinci sahabat bermain)",
        "setting": "Taman Pohon Beringin Rindang Berangin Sejuk",
        "pages": [
            {
                "number": 1,
                "title": "Tikar Pandan Terbentang Teduh",
                "titleEn": "Pandan Mat Rolled Out in the Shade",
                "textId": "Di bawah pohon beringin tua yang memiliki tirai akar gantung panjang, udara terasa sangat sejuk terlindung dari terik siang. Dita membentangkan tikar pandan harum di atas rumput hijau yang rata.",
                "textEn": "Beneath the ancient banyan tree with its long curtain of hanging aerial roots, the air felt delightfully cool, sheltered from the midday sun. Dita unrolled her fragrant woven pandan mat across the even green lawn.",
                "quote": "🌳 'Pohon rindang selalu menyediakan tempat teduh yang ramah bagi siapa saja yang ingin bersahabat.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu menggelar tikar untuk piknik di bawah pohon rindang?",
                "imagePrompt": "Charming children's book illustration of little girl Dita in a yellow polka-dot dress laying out a woven straw picnic mat under a majestic leafy banyan tree. Dappled sunlight on green grass, handcrafted wax crayon and soft oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Kotak-Kotak Bekal Berwarna-Warni",
                "titleEn": "Colorful Lunchboxes Gather Round",
                "textId": "Satu per satu kawan-kawan datang membawa kotak bekal masing-masing. Kinan membawa kotak biru, Bimo membawa kotak hijau, dan Luki si kelinci membawa keranjang kecil. Mereka duduk melingkar bersila di atas tikar.",
                "textEn": "One by one, playground friends arrived carrying their colorful lunchboxes. Kinan held a blue tin, Bimo brought a green box, and Luki the bunny carried a woven basket. They sat cross-legged in a cheerful circle on the mat.",
                "quote": "🧺 'Duduk melingkar bersama sahabat membuat setiap obrolan terasa hangat dan akrab.'",
                "coReading": "💡 Hitung Bersama: Coba hitung kotak bekal yang ada di gambar bersama si kecil!",
                "imagePrompt": "Delightful storybook scene of diverse toddler friends and a friendly white bunny sitting in a circle on a picnic mat, opening their colorful lunchboxes with eager smiles, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Irisan Semangka Merah Berbiji Manis",
                "titleEn": "Slices of Red Watermelon",
                "textId": "KLIK! Dita membuka kotak bekalnya. Di dalamnya berbaris potongan semangka merah merona berbentuk segitiga yang berair segar. \"Aku punya semangka manis dari kulkas Ibu!\" seru Dita gembira.",
                "textEn": "CLICK! Dita opened her lunchbox. Inside lined up freshly sliced triangular wedges of ruby-red watermelon, cool and glistening. \"I have sweet crisp watermelon chilled from Mama's icebox!\" declared Dita happily.",
                "quote": "🍉 'Warna merah semangka segar membawa keceriaan seketika ke atas tikar piknik.'",
                "coReading": "💡 Tanya si Kecil: Rasa buah apa yang paling menyegarkan saat hari sedang terik?",
                "imagePrompt": "Close-up illustration of a wooden tray holding juicy bright red watermelon slices on the picnic mat, with toddler hands reaching forward politely, wax crayon and oil pastel on textured paper, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Melon Hijau dan Butiran Anggur Ungu",
                "titleEn": "Honeydew Melon and Purple Grapes",
                "textId": "Kinan membuka bekalnya: bola-bola melon hijau muda yang wangi madu! Lalu Bimo menyodorkan seikat anggur ungu pekat tanpa biji. Luki si kelinci menambahkan irisan wortel bayi yang manis renyah.",
                "textEn": "Kinan popped open her container: spheres of honeydew melon smelling of sweet honey! Then Bimo offered a bunch of plump seedless purple grapes. Luki the bunny added crunchy little baby carrots.",
                "quote": "🍇 'Setiap buah membawa warna, aroma, dan kelezatan yang berbeda-beda.'",
                "coReading": "💡 Sebutkan Warna: Tunjuk dan sebutkan warna buah-buah di atas tikar: merah, hijau, ungu, dan oranye!",
                "imagePrompt": "Vibrant children's picture book scene showing a spread of colorful fruits on the mat: red watermelon, green melon balls, purple grapes, and orange carrot sticks in bamboo bowls, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Piring Besar Pelangi Buah",
                "titleEn": "The Big Rainbow Fruit Platter",
                "textId": "\"Bagaimana kalau kita satukan semuanya di piring kayu besar ini?\" usul Dita. Bersama-sama, mereka menata buah-buah itu melingkar. Ajaib! Piring kayu itu kini menjadi lukisan pelangi buah yang memukau mata.",
                "textEn": "\"How about we combine them all upon this large wooden platter?\" suggested Dita. Together, they arranged the fruit pieces in concentric rings. Magic! The wooden platter became a breathtaking rainbow of garden bounty.",
                "quote": "🌈 'Saat kita memadukan apa yang kita miliki, keindahan yang tercipta jauh lebih menakjubkan.'",
                "coReading": "💡 Aktivitas Seru: Susunlah mainan atau pensil warnamu membentuk lingkaran pelangi bersama si kecil!",
                "imagePrompt": "Charming illustration of children's hands joyfully arranging colorful fruit slices into a rainbow pattern on a round rustic wooden platter, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Mencicipi Bersama dengan Tawa",
                "titleEn": "Tasting Together with Laughter",
                "textId": "Nyam-kriuk-nyam! Dita mencicipi melon hijau Kinan yang manis legit. Kinan menikmati semangka berair Dita. Bimo menyuapkan anggur ungu ke mulutnya sambil tertawa riang. Berbagi membuat rasa buah menjadi seratus kali lebih lezat.",
                "textEn": "Munch-crunch-slurp! Dita tasted Kinan's sweet honey melon. Kinan bit into Dita's juicy crisp watermelon. Bimo popped purple grapes into his mouth with bubbly giggles. Sharing made every fruit taste a hundred times more delicious.",
                "quote": "😋 'Rasa terbaik bukanlah rasa manis di lidah, melainkan rasa kebersamaan di dalam dada.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara mengunyah buah renyah bersama si kecil: 'Kriuk, nyam-nyam, segar!'",
                "imagePrompt": "Joyous children's book scene of the little friends and rabbit laughing with happy cheeks, holding watermelon wedges and eating fruit slices on the shady picnic mat, soft golden light, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Tamu Kecil dari Dahan Beringin",
                "titleEn": "Little Guest from the Banyan Bough",
                "textId": "Seekor burung pipit kecil terbang turun ke tepi tikar, memiringkan kepalanya dengan mata kancing yang penasaran. Luki si kelinci meletakkan sebutir buah anggur kecil di atas daun rumput untuk sahabat bersayap itu.",
                "textEn": "A tiny sparrow fluttered down to the edge of the mat, tilting its head with curious bead eyes. Luki the bunny gently placed one little grape upon a clover leaf for their feathered visitor.",
                "quote": "🕊️ 'Kebaikan di meja makan selalu memiliki ruang untuk menyapa makhluk lain yang membutuhkan.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu membagikan remah biskuit kepada burung di halaman?",
                "imagePrompt": "Sweet storybook illustration of a tiny brown sparrow pecking gently at a purple grape on a leaf at the edge of the picnic mat, while children watch with quiet smiling wonder, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Meneguk Air Lemon Madu Segar",
                "titleEn": "Sipping Cool Honey Lemonade",
                "textId": "Sebagai penutup piknik, Dita menuangkan air lemon madu dingin dari termos kaca miliknya ke cangkir-cangkir bambu kecil. Rasa sejuk asam-manis membasuh tenggorokan mereka yang dahaga setelah asyik bercerita.",
                "textEn": "To conclude their picnic, Dita poured cool honey lemonade from her glass flask into little bamboo cups. The chilled, sweet-tangy sip refreshed their thirsty throats after an afternoon filled with happy stories.",
                "quote": "🍋 'Kesegaran yang sederhana melengkapi hari yang dipenuhi tawa dan kasih.'",
                "coReading": "💡 Tanya si Kecil: Minuman segar apa yang paling kamu sukai saat piknik di taman?",
                "imagePrompt": "Cozy children's book scene of little girl Dita pouring pale yellow lemonade from a flask into bamboo cups for her friends on the picnic blanket, warm sunny afternoon glow, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Membereskan Tikar Menjelang Senja",
                "titleEn": "Folding the Mat as Twilight Glows",
                "textId": "Matahari mulai condong ke barat, mewarnai langit dengan selendang aprikot. Bersama-sama, mereka memasukkan kotak bekal yang kosong ke dalam tas dan menggulung tikar pandan dengan rapi. Tidak ada satu pun sampah yang tertinggal di bawah beringin.",
                "textEn": "The sun tilted low into the west, painting the sky with apricot ribbons. Together, they packed their empty containers and rolled up the pandan mat with tidy care. Not a single scrap of litter was left beneath the ancient banyan tree.",
                "quote": "🧹 'Menjaga tempat bermain tetap bersih adalah tanda terima kasih kita kepada alam.'",
                "coReading": "💡 Aktivitas Bersama: Bantu orang tua merapikan barang-barang mainan di kamar sebelum tidur!",
                "imagePrompt": "Heartwarming illustration of the children helping each other fold the picnic mat and tidy up their bags, with the banyan tree glowing in warm golden twilight, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Pulas Beraroma Buah Manis",
                "titleEn": "Sweet Slumber Scented with Fruit",
                "textId": "Malam itu di kamarnya, Dita tidur pulas dengan senyum tersungging di bibir. Di balik selimut lembutnya, Dita bermimpi menari di atas pelangi buah bersama sahabat-sahabat terbaiknya. Selamat tidur, anak yang pandai berbagi.",
                "textEn": "That night in her bedroom, little Dita slept deeply with a gentle smile upon her lips. Tucked beneath her soft quilt, Dita dreamed of dancing across a fruit rainbow with all her dearest friends. Goodnight, sweet little sharer.",
                "quote": "🌙 'Tidur malam yang paling damai berakar dari hari yang diisi dengan tawa dan persahabatan tulus.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak baik, terima kasih sudah selalu menjadi teman yang manis dan suka berbagi.",
                "imagePrompt": "A serene bedtime illustration of girl Dita sleeping peacefully in her bed under a yellow-and-white blanket, smiling in her sleep. A soft fruit-rainbow dream glow above her, moonlight through the window, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s52)

    # =========================================================================
    # STORY 53: Jus Jeruk Peras Gotong Royong
    # =========================================================================
    s53 = {
        "id": "jus-jeruk-peras",
        "storyNumber": 53,
        "title": "Jus Jeruk Peras Gotong Royong",
        "englishTitle": "The Teamwork Fresh Orange Juice",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Bahu-membahu, kepedulian terhadap kawan yang lelah, dan kesegaran kerjasama",
        "cover": "images/story53_cover.jpg",
        "coverImage": "images/story53_cover.jpg",
        "synopsis": "Setelah teman-teman kelelahan bermain bola di lapangan desa, Raka dan Doni berinisiatif memeras sekeranjang jeruk keprok manis di gazebo kebun. Dengan alat pemeras kayu sederhana dan tenaga gotong royong, mereka menyuguhkan teko jus jeruk dingin yang mengembalikan senyuman semua orang.",
        "synopsisEn": "After village friends grow exhausted playing soccer in the meadow, Raka and Doni team up to squeeze a basket of sweet oranges in the gazebo. With a wooden juicer and cheerful teamwork, they brew a big pitcher of cool orange juice that restores smiles to all.",
        "protagonist": "Raka (Anak laki-laki 5 tahun berkaus garis biru yang bersemangat)",
        "companion": "Doni (Sahabat penyabar pembawa teko kaca bertutup kayu)",
        "setting": "Gazebo Kayu Tepi Lapangan Berangin Sejuk",
        "pages": [
            {
                "number": 1,
                "title": "Lelah dan Haus di Pinggir Lapangan",
                "titleEn": "Tired and Thirsty by the Pitch",
                "textId": "Peluit tanda selesai bermain bola berbunyi. Teman-teman duduk bersandar di rumput tepi lapangan dengan napas terengah-engah dan keringat bercucuran. Tenggorokan mereka terasa kering dan haus setelah berlari ke sana-kemari.",
                "textEn": "The whistle blew marking the end of the afternoon soccer match. Friends sat resting against the grassy embankment, panting and drenched in sweat. Their little throats felt parched and thirsty after running back and forth under the sun.",
                "quote": "⚽ 'Bermain sungguh-sungguh membuat tubuh lelah, tetapi hati terasa puas.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana rasanya tenggorokanmu saat kamu selesai berlari-lari kencang?",
                "imagePrompt": "Charming children's book illustration of village children in soccer jerseys resting on the grass beside a goalpost, wiping sweat, looking thirsty. Raka and Doni observe them from the shaded wooden gazebo. Wax crayon on textured paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Sekeranjang Jeruk Keprok Manis",
                "titleEn": "A Basket of Sweet Mandarin Oranges",
                "textId": "Raka melihat ke meja gazebo. Di sana ada sekeranjang penuh jeruk keprok berkulit jingga cerah hasil petikan kebun Paman. \"Doni, ayo kita buatkan jus jeruk peras segar untuk kawan-kawan!\" ajak Raka dengan mata berbinar.",
                "textEn": "Raka looked toward the wooden gazebo table. Sitting there was a large wicker basket overflowing with bright orange mandarins picked fresh from Uncle's orchard. \"Doni, let's make fresh squeezed orange juice for our friends!\" suggested Raka with bright eyes.",
                "quote": "🍊 'Melihat kebutuhan orang lain dan bergegas membantu adalah tanda kebaikan sejati.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu membantu membawakan minuman untuk kawan yang kehausan?",
                "imagePrompt": "Delightful storybook scene of boy Raka pointing to a large basket of glossy orange mandarins on a wooden gazebo table, smiling enthusiastically at his friend Doni who holds a glass pitcher, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Membelah Jeruk Menjadi Dua Bulan",
                "titleEn": "Slicing Oranges into Two Moons",
                "textId": "Dengan pisau buah kayu yang tumpul dan aman, Doni membelah jeruk-jeruk itu tepat di tengah. Sret! Bulir-bulir jingga yang padat air menyembur harum. Dua belahan jeruk tampak seperti mangkuk matahari kecil yang berkilau.",
                "textEn": "With a safe, blunt wooden fruit knife, Doni carefully sliced each orange across the middle. Slice! Plump orange juice vesicles burst with sweet perfume. The two halves looked like glowing miniature sun bowls.",
                "quote": "🔪 'Setiap irisan yang rapi membuka jalan bagi sari manis yang tersimpan di dalam.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara membelah buah: 'Sreeet! Jeruk terbelah dua!'",
                "imagePrompt": "Close-up illustration of halved oranges revealing glistening citrus segments and droplet splashes, resting on a clean wooden board with a glass jug nearby. Wax crayon and chalky oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Alat Pemeras Kayu Berputar",
                "titleEn": "The Wooden Juicer Turns and Twists",
                "textId": "Raka memegang alat pemeras kayu berbentuk kerucut beralur. Ia menancapkan belahan jeruk ke ujung kerucut lalu menekannya dengan kedua tangan: tekan, putar, putar! Keringat kecil muncul di kening Raka yang bersemangat.",
                "textEn": "Raka held the ridged wooden hand-juicer. He placed an orange half upon the cone and pressed down firmly with both hands: press, twist, swirl! Tiny beads of sweat popped up on Raka's determined forehead.",
                "quote": "💪 'Tenaga yang kita keluarkan untuk menolong orang lain tidak akan pernah terasa sia-sia.'",
                "coReading": "💡 Latihan Bersama: Buat gerakan memutar kedua telapak tanganmu seperti sedang memeras jeruk!",
                "imagePrompt": "Action children's illustration of little boy Raka pressing and twisting an orange half on a wooden cone reamer, with rich orange juice streaming down into a ceramic bowl. Crayon textures, dynamic strokes, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Guyuran Sari Jeruk Emas",
                "titleEn": "A Waterfall of Golden Orange Nectar",
                "textId": "Kucuuuur! Sari jeruk jingga keemasan mengalir deras dari corong pemeras, memenuhi mangkuk penampung. Aromanya begitu segar dan manis alami tanpa perlu tambahan pemanis buatan.",
                "textEn": "Splash-gush! Rich golden-orange juice poured in a fragrant waterfall from the strainer spout, filling the catch basin. The scent was delightfully tart, sweet, and purely natural without needing any added sugar.",
                "quote": "✨ 'Kebaikan alami dari alam selalu memberikan kesegaran terbaik bagi tubuh kita.'",
                "coReading": "💡 Tanya si Kecil: Lebih suka jus jeruk yang manis atau yang sedikit asam segar?",
                "imagePrompt": "Vibrant illustration of bright orange juice cascading smoothly into a clear glass pitcher, with little citrus droplets caught in the golden sunlight. Warm folk art, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Menyaring Biji Bersama Doni",
                "titleEn": "Straining the Seeds with Doni",
                "textId": "Doni memegang saringan bambu kecil di atas teko kaca besar. Raka menuangkan perasan jeruk itu perlahan: ssshhh... Biji-biji putih tertahan rapi di saringan, sementara sari buah yang lembut lolos ke dalam teko.",
                "textEn": "Doni held a small bamboo sieve over the mouth of the tall glass pitcher. Raka poured the squeezed juice slowly: whoosh... White seeds were neatly caught by the mesh, while velvety smooth nectar streamed into the pitcher.",
                "quote": "🤝 'Dua tangan yang bekerja sama menyelesaikan pekerjaan dua kali lebih cepat dan rapi.'",
                "coReading": "💡 Tanya si Kecil: Mengapa biji jeruk harus disaring sebelum diminum?",
                "imagePrompt": "Touching storybook scene of teamwork between Raka pouring the bowl of juice while Doni steadily holds the bamboo strainer over the pitcher, both smiling with concentration, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Teko Kaca Penuh Kesegaran",
                "titleEn": "A Pitcher Full of Sunshine",
                "textId": "Teko kaca itu kini penuh berisi cairan jingga menyala seperti sinar matahari cair. Doni menambahkan beberapa bongkah es batu bening yang bergemerincing merdu: klinting-klinting! Embun sejuk mengalir di dinding kaca teko.",
                "textEn": "The tall glass pitcher was now brimming with glowing orange nectar, looking like liquid sunshine. Doni added a few clear ice cubes that chimed merrily: clink-clink-clink! Cool condensation trickled down the glass.",
                "quote": "🧊 'Kesejukan yang hadir di saat yang tepat terasa seperti hadiah terindah dari langit.'",
                "coReading": "💡 Aktivitas Seru: Tirukan bunyi es batu yang beradu di dalam gelas kaca: 'Klinting... klinting!'",
                "imagePrompt": "Close-up children's book illustration of a condensation-covered glass pitcher brimming with vibrant orange juice and bobbing ice cubes, resting on the wooden gazebo railing, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Membagikan Gelas ke Lapangan",
                "titleEn": "Handing Glasses Across the Pitch",
                "textId": "\"Minuman segar datang!\" seru Raka sambil membawa nampan berisi gelas-gelas bambu kecil. Teman-teman bersorak gembira. Mereka menerima cangkir jus jeruk peras itu dengan mata berbinar penuh terima kasih.",
                "textEn": "\"Fresh drinks have arrived!\" called Raka, carrying a tray loaded with small bamboo tumblers. The tired friends cheered in delight. They accepted the cups of fresh-squeezed juice with eyes glowing with gratitude.",
                "quote": "🥤 'Memberi minum kepada yang kehausan adalah bentuk kepedulian yang paling menyegarkan hati.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana ekspresi teman-temanmu saat kamu membawakan mereka minuman dingin?",
                "imagePrompt": "Joyous illustration of little boy Raka and Doni handing cups of orange juice to smiling, grateful children resting on the grass. Golden afternoon light washes over the meadow, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Tegukan Nikmat yang Mengembalikan Semangat",
                "titleEn": "Delicious Gulps that Bring Back Smiles",
                "textId": "Gleg-gleg-gleg! Semua anak meneguk jus jeruk peras itu hingga tandas. Rasa manis asam yang dingin seketika mengusir lelah mereka. Wajah-wajah yang semula lesu kini kembali ceria dan penuh tawa.",
                "textEn": "Gulp-gulp-ahhh! Every child drank the fresh orange juice down to the very last drop. The cool sweet-tangy burst instantly chased away their fatigue. Faces that were once weary blossomed back into lively laughter.",
                "quote": "😄 'Senyuman yang kembali mekar di wajah kawan adalah upah terindah dari kerja keras kita.'",
                "coReading": "💡 Aktivitas Seru: Tarik napas lega dan ucapkan bersama: 'Aaaaah, segaaar sekali!'",
                "imagePrompt": "Delightful children's book scene of children cheering, drinking from bamboo cups, laughing together with orange juice mustaches on their upper lips. Warm sunlit meadow, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Nyenyak Setelah Hari yang Berarti",
                "titleEn": "Sound Sleep After a Meaningful Day",
                "textId": "Senja ungu berganti malam yang damai. Di kamarnya yang hangat, Raka merebahkan tubuhnya di atas kasur kapuk yang empuk. Tangannya yang lelah memeras jeruk kini beristirahat dengan tenang. Di alam mimpinya, kebaikan hari ini mekar menjadi bintang-bintang yang ramah. Selamat tidur, anak yang berjiwa penolong.",
                "textEn": "Purple twilight yielded to peaceful night. In his warm bedroom, little Raka nestled onto his soft cotton mattress. His arms, tired from squeezing oranges, now rested in serene stillness. In his sweet dreams, today's kindness blossomed into friendly stars. Goodnight, helpful little friend.",
                "quote": "🌙 'Tidurlah dengan hati yang ringan, karena kamu telah membawa senyuman ke wajah banyak orang hari ini.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak hebat, terima kasih sudah selalu senang menolong sesama dengan riang gembira.",
                "imagePrompt": "Tranquil bedtime illustration of boy Raka sleeping soundly under a cozy blue blanket, smiling gently. The room is softly illuminated by a nightlamp shaped like a round orange, moonlight through window, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s53)

    # =========================================================================
    # STORY 54: Pancake Madu Minggu Pagi
    # =========================================================================
    s54 = {
        "id": "pancake-madu-minggu",
        "storyNumber": 54,
        "title": "Pancake Madu Minggu Pagi",
        "englishTitle": "Sunday Morning Honey Pancakes",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Kesabaran menunggu giliran, kasih sayang kepada saudara, dan manisnya mengalah",
        "cover": "images/story54_cover.jpg",
        "coverImage": "images/story54_cover.jpg",
        "synopsis": "Di hari Minggu pagi yang cerah, Ibu memanggang pancake bundar keemasan yang beraroma vanili harum. Adit sangat ingin menjadi yang pertama menyantapnya, tetapi melihat mata lapar adik kecilnya Alya, Adit belajar bahwa memberikan potongan pancake pertama untuk adik menghadirkan rasa manis yang jauh lebih istimewa.",
        "synopsisEn": "On a sunny Sunday morning, Mama flips round golden pancakes fragrant with vanilla. Adit eagerly wants the very first pancake, but seeing his toddler sister Alya's hungry eyes, Adit learns that gifting the first warm slice to his sister brings a sweetness far richer than honey.",
        "protagonist": "Adit (Anak laki-laki 5 tahun berpiyama garis hijau bertopi tidur santai)",
        "companion": "Adik Alya (Adik perempuan 2 tahun bertopi pita dengan sendok bayi kecil)",
        "setting": "Meja Makan Keluarga yang Hangat Disinari Matahari Minggu",
        "pages": [
            {
                "number": 1,
                "title": "Desis Mentega di Wajan Datar",
                "titleEn": "Sizzle of Butter on the Griddle",
                "textId": "Cesss! Mentega kuning meleleh di atas wajan datar hitam, menebarkan wangi gurih ke seluruh dapur. Adit melompat dari tempat tidur dengan mata berbinar; hari ini adalah hari Minggu, hari pancake madu buatan Ibu!",
                "textEn": "Sizzle! Golden butter melted across the black griddle, sending savory, mouthwatering aromas throughout the kitchen. Adit hopped out of bed with sparkling eyes; today was Sunday, Mama's famous honey pancake morning!",
                "quote": "🥞 'Aroma sarapan Minggu pagi selalu menyimpan janji hari yang penuh kebahagiaan.'",
                "coReading": "💡 Tanya si Kecil: Sarapan apa yang paling kamu nanti-nantikan di hari libur?",
                "imagePrompt": "Charming children's book illustration of little boy Adit in green striped pyjamas padding into a sunny, cheerful kitchen where Mama stands at the stove flipping pancakes. Handcrafted wax crayon on textured cream paper, simple black bead eyes, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Adonan Putih yang Menggelembung",
                "titleEn": "Bubbling Batter on the Stove",
                "textId": "Ibu menuangkan sesendok sayur adonan putih susu ke tengah wajan. Plop! Adonan itu melebar menjadi lingkaran sempurna. Gelembung-gelembung kecil mulai muncul di permukaannya: pletok, pletok, pletok!",
                "textEn": "Mama ladled creamy white batter right into the griddle center. Plop! The batter spread into a perfect round circle. Tiny air bubbles began popping across its golden surface: pop, pop, pop!",
                "quote": "🍳 'Memasak kue mengajarkan kita mengamati tanda-tanda kecil sebelum semuanya matang sempurna.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara gelembung pancake yang meletup: 'Pletok, pletok, pletok!'",
                "imagePrompt": "Close-up storybook illustration of a round pancake cooking on a griddle, showing tiny bubbles forming on the golden batter. A wooden spatula rests nearby, warm amber morning sunlight, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Balikan Sempurna Menjadi Emas",
                "titleEn": "The Perfect Golden Flip",
                "textId": "HUP! Dengan spatula kayunya, Ibu membalik pancake itu dengan lincah di udara. Bagian bawahnya kini berwarna cokelat keemasan yang mulus dan empuk seperti bantal kecil. Perut Adit berbunyi keras saking laparnya.",
                "textEn": "FLIP! With a swift flick of her wooden spatula, Mama tossed the pancake into the air. The underside was now a velvety golden-brown, puffed and soft as a tiny pillow. Adit's tummy growled with hungry anticipation.",
                "quote": "✨ 'Keterampilan dan kesabaran mengubah bahan sederhana menjadi mahakarya lezat.'",
                "coReading": "💡 Aktivitas Seru: Tirukan gerakan membalik pancake di udara dengan kedua tanganmu: 'Hup, balik!'",
                "imagePrompt": "Delightful illustration of Mama deftly flipping a round golden pancake in the air, while little boy Adit claps his hands in excited wonder. Warm yellow and honey crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Adik Alya Mengetuk Kursi Makan",
                "titleEn": "Little Sister Alya Taps Her High Chair",
                "textId": "Tuk-tuk-tuk! Dari kursi makan bayinya, Adik Alya mengetuk-ngetukkan sendok plastiknya. Pipinya yang tembem kemerahan bergerak-gerak, dan matanya menatap pancake pertama yang mendarat di piring keramik.",
                "textEn": "Tap-tap-tap! From her high chair, little sister Alya tapped her colorful plastic spoon. Her chubby rosy cheeks twitched, and her round eyes fixated on the very first pancake landing on the ceramic plate.",
                "quote": "👶 'Adik kecil belum pandai berkata-kata, tetapi tatapan matanya mengungkapkan segalanya.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat adik atau bayi kecil mengetuk sendok saat lapar?",
                "imagePrompt": "Sweet children's picture book scene of toddler sister Alya with pigtails sitting in a wooden high chair, tapping her little spoon eagerly, gazing at the hot pancake plate on the table, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Keinginan Menjadi yang Pertama",
                "titleEn": "The Urge to be First",
                "textId": "Adit sudah memegang garpunya erat-erat. Ia ingin sekali menjadi orang pertama yang memotong pancake hangat itu. \"Pancake pertama ini pasti yang paling empuk!\" pikir Adit dalam hati.",
                "textEn": "Adit gripped his little fork tightly. He desperately wanted to be the very first to cut into that steaming pancake. \"The first pancake is always the fluffiest of all!\" thought Adit to himself.",
                "quote": "🤔 'Keinginan untuk selalu menjadi yang pertama adalah godaan yang sering menghampiri kita.'",
                "coReading": "💡 Tanya si Kecil: Apakah sulit rasanya untuk menunggu giliran saat kamu sangat lapar?",
                "imagePrompt": "Storybook illustration of boy Adit holding his fork, glancing from the steaming pancake to his hungry little sister in the high chair, a thoughtful, hesitating look on his face, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Mata Bulat Alya yang Berharap",
                "titleEn": "Alya's Hopeful Round Eyes",
                "textId": "Saat Adit menatap Alya, adik kecilnya itu tersenyum manis sambil menunjuk ke arah piring: \"Kue... kue...\" Tiba-tiba, ada rasa hangat yang mengalir di dada Adit, rasa sayang seorang kakak kepada adiknya.",
                "textEn": "As Adit looked over at Alya, his toddler sister flashed an innocent, toothy smile and pointed tiny fingers at the plate: \"Cake... cake...\" Suddenly, a surge of tender warmth flooded Adit's chest—the protective love of a big brother.",
                "quote": "💖 'Kasih sayang kepada saudara membuat keinginan diri sendiri meleleh dengan rela.'",
                "coReading": "💡 Peluk Saudara: Jika ada adik atau kakak di rumah, berikan senyuman termanismu kepadanya!",
                "imagePrompt": "Heartwarming illustration of toddler sister Alya smiling innocently at Adit with sparkling eyes, reaching out a little hand. Adit's face softens from hesitation into a gentle, loving smile, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Menggeser Piring Pertama untuk Adik",
                "titleEn": "Sliding the First Plate to Sister",
                "textId": "Dengan kedua tangannya, Adit menggeser piring pancake pertama itu ke meja kursi makan Alya. \"Untuk Alya dulu ya, Dik. Kakak tunggu pancake kedua saja,\" kata Adit dengan suara lembut yang dewasa.",
                "textEn": "With gentle hands, Adit nudged the first plate of pancake over to Alya's high chair tray. \"For you first, little Alya. Big brother can wait for the second one,\" said Adit in a proud, caring voice.",
                "quote": "🌟 'Mengalah demi kebahagiaan adik adalah tanda kedewasaan yang sesungguhnya.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu membiarkan saudaramu memilih makanan atau mainan terlebih dahulu?",
                "imagePrompt": "Touching children's book scene of boy Adit placing the warm pancake plate before his toddler sister Alya, who claps in pure glee. Mama looks on from the stove with proud, shining eyes, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Kucuran Madu Hutan Keemasan",
                "titleEn": "Drizzle of Golden Forest Honey",
                "textId": "Ibu tersenyum bangga sekali memandangi Adit. Ibu mengambil kendi madu dan mengucurkan madu bunga randu ke atas pancake Alya dan pancake kedua yang baru matang untuk Adit. Madu itu mengalir berkilau keemasan.",
                "textEn": "Mama smiled with immense pride at Adit. She picked up the ceramic honey pot and drizzled fragrant golden wildflower honey over Alya's pancake and over the steaming second pancake made just for Adit. The honey cascaded like liquid sunshine.",
                "quote": "🍯 'Kebaikan hati yang manis pantas diganjar dengan curahan madu yang melimpah.'",
                "coReading": "💡 Aktivitas Seru: Tirukan gerakan menuang madu dari kendi: 'Syuuur... mengalir manis!'",
                "imagePrompt": "Close-up picture book illustration of thick golden honey being drizzled from a pottery jug onto a stack of fluffy pancakes topped with a pat of melting butter. Steam and honey droplets, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Sarapan Terlezat Bersama Keluarga",
                "titleEn": "The Sweetest Family Breakfast",
                "textId": "Nyam-nyam! Alya menyuap potongan kecil pancake madu dengan tawa renyah. Adit menikmati pancake keduanya yang ternyata terasa jauh lebih empuk dan manis dari biasanya. Ruang makan dipenuhi kehangatan cinta keluarga.",
                "textEn": "Yum-yum! Alya chewed soft bites of honey pancake with delightful giggles. Adit savored his second pancake, which tasted twice as fluffy and sweet as he could ever remember. The dining room brimmed with pure familial warmth.",
                "quote": "👨‍👩‍👧 'Kebahagiaan keluarga tercipta dari hal-hal kecil saat kita saling mendahulukan sesama.'",
                "coReading": "💡 Tanya si Kecil: Apa yang membuat sarapan bersama keluarga terasa begitu membahagiakan?",
                "imagePrompt": "Joyous children's illustration of the family sitting around the sunny breakfast table, eating pancakes with honey and drinking milk, smiling at each other. Soft morning sunlight streaming through the window, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Mimpi Manis Berselimut Kasih",
                "titleEn": "Sweet Dreams Wrapped in Love",
                "textId": "Malam harinya setelah seharian bermain ceria di hari Minggu, Adit tidur lelap di kamarnya. Di ranjang sebelah, Alya sudah terlelap memeluk bonekanya. Adit memejamkan mata dengan damai, bangga telah menjadi kakak yang penuh kasih sayang. Selamat tidur, anak yang baik hati.",
                "textEn": "That night, after a joyful Sunday of playful games, Adit slept deeply in his room. In the crib nearby, little Alya was fast asleep hugging her soft doll. Adit closed his eyes in serene peace, proud to be such a loving big brother. Goodnight, kindhearted boy.",
                "quote": "🌙 'Tidurlah dengan senyum manis, karena cinta yang kamu berikan akan menjaga mimpimu tetap indah.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak hebat, terima kasih sudah belajar menyayangi dan mengalah dengan penuh kebaikan.",
                "imagePrompt": "A tranquil bedtime illustration of boy Adit sleeping soundly under a soft green quilt, with his little sister sleeping peacefully in her adjacent cot. Warm nightlight glow, moon and stars outside the window, wax crayon and oil pastel, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s54)

    return stories

print("Story module 51-54 defined successfully")
