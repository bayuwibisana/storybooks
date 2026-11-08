# scripts/polish_stories_48_to_50.py
import json

def get_stories_48_to_50():
    stories = []

    # =========================================================================
    # STORY 48: Pesta Selai Stroberi Hutan
    # =========================================================================
    s48 = {
        "id": "selai-stroberi-hutan",
        "storyNumber": 48,
        "title": "Pesta Selai Stroberi Hutan",
        "englishTitle": "The Wild Strawberry Jam Feast",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Memetik hasil alam bersama dengan sabar dan manisnya menikmati hasil olahan bersama teman",
        "cover": "images/story48_cover.jpg",
        "coverImage": "images/story48_cover.jpg",
        "synopsis": "Di lereng Bukit Berbunga, Tita dan Mimi si kelinci memetik buah stroberi liar merah merona yang wangi embun. Di pondok kayu kecil mereka, buah-buah manis itu dimasak perlahan di kuali tembaga menjadi selai merah kental yang dioleskan ke atas biskuit gandum hangat.",
        "synopsisEn": "On the slopes of Flowery Hill, little Tita and Mimi the bunny harvest ruby-red wild strawberries fragrant with morning dew. In their snug wooden cottage, the berries simmer in a copper pot into rich jam spread over warm oat biscuits.",
        "protagonist": "Tita (Gadis cilik 5 tahun bercelemek merah dan bertopi jerami dengan pita stroberi)",
        "companion": "Mimi (Kelinci putih bermata bulat dengan keranjang anyaman kecil)",
        "setting": "Lereng Bukit Stroberi Liar & Dapur Pondok Kayu Beraroma Manis",
        "pages": [
            {
                "number": 1,
                "title": "Bintik Merah di Semak Hijau",
                "titleEn": "Crimson Dots in the Green Thicket",
                "textId": "Pagi itu di lereng Bukit Berbunga, embun masih berkilau di atas dedaunan. Tita melangkah riang sambil menenteng keranjang rotan kecil. Di antara semak-semak hijau rendah, buah-buah stroberi liar menyembul merah cerah seperti permata delima mungil.",
                "textEn": "That morning on the slopes of Flowery Hill, dew glistened upon the leaves. Tita skipped merrily carrying her woven wicker basket. Nestled among low green bushes, wild strawberries peeked out bright crimson like tiny ruby jewels.",
                "quote": "🍓 'Alam menyembunyikan buah-buah termanis bagi mereka yang mau mengamatinya dengan sabar.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu mencicipi buah stroberi yang asam-manis segar?",
                "imagePrompt": "Charming children's book illustration of little girl Tita in a red apron and straw hat kneeling in a sunny hillside meadow, gently picking ripe red wild strawberries into a wicker basket. White fluffy bunny Mimi helps beside her. Handcrafted wax crayon and chalky oil pastel, textured cream paper, 4:3 landscape, completely text-free."
            },
            {
                "number": 2,
                "title": "Petikan Lembut Bersama Mimi",
                "titleEn": "Gentle Picking Beside Mimi",
                "textId": "\"Petik yang sudah merah tua ya, Mimi!\" bisik Tita ramah. Krup! Tangkai stroberi lepas dengan mudah di jemari Tita. Mimi si kelinci melompat lincah dari semak ke semak, mengumpulkan buah-buah terbaik tanpa merusak dahan bunganya.",
                "textEn": "\"Pick the deep red ones, dear Mimi!\" whispered Tita kindly. Snap! The berry stems parted easily in Tita's gentle fingers. Mimi the bunny hopped nimbly from bush to bush, gathering the juiciest berries without harming the young blossom buds.",
                "quote": "🐇 'Memetik dengan lembut adalah cara kita berterima kasih kepada tanaman yang memberi makan.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara memetik buah: 'Krup! Satu stroberi merah masuk keranjang!'",
                "imagePrompt": "A delightful storybook illustration of white bunny Mimi holding a large ripe strawberry with both paws, placing it carefully into a small basket. Sunshine filters through leaves, wax crayon scribbles, textured watercolor paper, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Keranjang Penuh Beraroma Madu",
                "titleEn": "A Basket Brimming with Honey Fragrance",
                "textId": "Menjelang siang, keranjang rotan mereka sudah penuh menggunung dengan buah stroberi yang mengilap terkena sinar matahari. Aroma manis semerbak buah segar memenuhi udara sejuk pegunungan.",
                "textEn": "By late morning, their wicker basket was heaped high with shiny wild strawberries glistening in the sun. A rich, sweet berry aroma filled the cool mountain air with pure delight.",
                "quote": "🧺 'Keranjang yang penuh adalah cermin dari kesabaran dan kerjasama yang gembira.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana aroma buah segar saat baru dipetik?",
                "imagePrompt": "Whimsical children's picture book scene of Tita and Mimi sitting by a large basket overflowing with bright red wild strawberries on a sunny hill overlooking a green valley. Warm pastel tones, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Mencuci Buah di Pancuran Bambu",
                "titleEn": "Washing Berries at the Bamboo Spout",
                "textId": "Di samping pondok dapur, air sumber pegunungan mengalir sejuk dari bilah bambu. Kricik-kricik... Tita mencuci stroberi di mangkuk porselen putih hingga bersih berkilau dari sisa tanah dan butiran debu.",
                "textEn": "Beside the cottage kitchen, cool mountain spring water trickled gently from a split bamboo pipe. Gurgle-splash... Tita rinsed the berries in a white porcelain basin until they shone crystal clean, free of every speck of garden dust.",
                "quote": "💧 'Air yang jernih membasuh buah hingga siap diolah menjadi hidangan sehat.'",
                "coReading": "💡 Aktivitas Bersama: Usap kedua telapak tanganmu bersama si kecil seperti sedang mencuci buah!",
                "imagePrompt": "Close-up storybook illustration of clear spring water trickling from a bamboo spout over glistening strawberries in a white ceramic bowl. Tita's little hands rinse them gently with Mimi watching. Wax crayon on heavy cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Kuali Tembaga dan Gula Tebu",
                "titleEn": "The Copper Pot and Golden Cane Sugar",
                "textId": "Di atas kompor tanah liat, Tita menuangkan buah-buah merah itu ke dalam kuali tembaga kuno. Mimi membantu menaburkan sesendok gula tebu keemasan dan sedikit perasan air lemon segar.",
                "textEn": "Upon the clay hearth, Tita poured the crimson fruit into an antique copper kettle. Mimi helped sprinkle a spoonful of golden cane sugar and a tiny splash of fresh lemon juice.",
                "quote": "🍋 'Sedikit rasa asam membuat rasa manis buah terasa semakin istimewa.'",
                "coReading": "💡 Tanya si Kecil: Rasa apa yang kamu rasakan saat lemon bertemu dengan gula manis?",
                "imagePrompt": "Warm kitchen illustration of Tita stirring a gleaming copper pot filled with simmering red strawberries, while bunny Mimi sprinkles golden cane sugar from a wooden spoon. Cozy hearth fire glow, wax crayon texture, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Aduk Perlahan Berbusa Manis",
                "titleEn": "Stirring Slowly into Sweet Froth",
                "textId": "Kluk-kluk-kluk... Kuah stroberi mulai mendidih perlahan. Tita mengaduknya dengan sendok kayu panjang: putar, putar, melingkar. Gelembung-gelembung merah muda meletup lembut, menebarkan aroma selai paling sedap di seluruh pondok.",
                "textEn": "Bubble-simmer-glug... The strawberry sauce began to simmer gently. Tita stirred with a long wooden ladle: round, round, in patient circles. Soft pink bubbles popped merrily, releasing the sweetest jam perfume throughout the whole cottage.",
                "quote": "🥄 'Membuat selai butuh kesabaran; api yang kecil menjaga keaslian rasa buah.'",
                "coReading": "💡 Aktivitas Seru: Gerakkan tanganmu memutar perlahan menirukan gerakan mengaduk kuali selai!",
                "imagePrompt": "Heartwarming storybook scene of pink and ruby-red jam bubbling gently in the copper pot, with curling sweet steam. Tita and rabbit Mimi watch the pot with smiles of cozy anticipation. Warm amber lighting, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Kekentalan Sempurna Selai Merah",
                "titleEn": "The Perfect Ruby Thickness",
                "textId": "Setelah beberapa saat, kuah cair itu berubah menjadi selai merah delima yang kental dan mengilap. Tita meneteskan sedikit selai ke piring dingin: selai itu tidak mengalir lagi. \"Hore, selai kita sudah matang sempurna!\"",
                "textEn": "After some gentle time, the syrup thickened into a glistening, ruby-red jam. Tita spooned a drop onto a chilled saucer: it stayed firm and set. \"Hooray, our jam is cooked to perfection!\"",
                "quote": "✨ 'Kesabaran mengaduk selalu berbuah manis yang kental dan menghangatkan.'",
                "coReading": "💡 Tanya si Kecil: Makanan apa yang paling lezat jika diolesi selai stroberi?",
                "imagePrompt": "Delightful children's illustration of Tita holding up a wooden spoon dripping thick, shiny crimson jam onto a small saucer. Bunny Mimi claps with joy beside little glass jars tied with red ribbons, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Olesan Tebal di Atas Biskuit Gandum",
                "titleEn": "Thick Spread on Warm Oat Biscuits",
                "textId": "Nenek mengeluarkan setalam biskuit gandum hangat dari pemanggang. Dengan pisau tumpul kecil, Tita mengoleskan selai stroberi buatannya tebal-tebal ke atas biskuit. Kawan-kawan hutan yang datang disambut dengan piring masing-masing.",
                "textEn": "Grandmother pulled a tray of warm, golden oat biscuits from the baker. With a dull butter knife, Tita spread her homemade strawberry jam thickly over the steaming biscuits. Woodland friends gathered around to receive their savory treats.",
                "quote": "🍪 'Kenikmatan makanan berlipat ganda saat kita menikmatinya bersama sahabat terkasih.'",
                "coReading": "💡 Aktivitas Seru: Tirukan gerakan mengoles selai ke atas biskuit dengan jari tanganmu!",
                "imagePrompt": "Cozy picture book illustration of little girl Tita spreading thick strawberry jam on warm golden biscuits at a rustic wooden table, surrounded by woodland animal guests smiling. Wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Toples-Toples Kecil Bertali Renda",
                "titleEn": "Glass Jars Tied with Ribbon Lace",
                "textId": "Sisa selai dimasukkan ke dalam toples-toples kaca kecil bertutup kain renda merah. Tita dan Mimi menuliskan label 'Selai Kasih Sayang' untuk dibagikan kepada tetangga-tetangga bukit yang tidak sempat memetik buah.",
                "textEn": "The remaining jam was poured into charming glass mason jars topped with red lace fabric covers. Tita and Mimi tied neat bows, labeling them 'Love Jam' to gift to hill neighbors who could not pick berries today.",
                "quote": "🎁 'Menyimpan sebagian untuk dibagikan adalah tanda hati yang selalu bersyukur.'",
                "coReading": "💡 Tanya si Kecil: Hadiah buatan tangan apa yang paling ingin kamu berikan kepada sahabatmu?",
                "imagePrompt": "Sweet children's book scene of little glass jars filled with red strawberry jam sitting on a window sill, tied with gingham cloth and twine, while evening sunlight casts long warm shadows, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Mimpi Manis Beraroma Stroberi",
                "titleEn": "Sweet Berry Dreams Under Twilight",
                "textId": "Malam tiba dengan lembut di bukit. Di tempat tidur berseprai motif bunga, Tita dan Mimi meringkuk tidur berselimut wol merah muda. Di udara, aroma wangi stroberi hangat masih tertinggal manis mengantarkan mimpi indah. Selamat tidur, pembuat selai cilik.",
                "textEn": "Night descended softly upon the hill. In a cozy bed laid with floral quilts, little Tita and Mimi curled up to sleep under a plush pink blanket. In the air, the faint sweet aroma of warm strawberries lingered, escorting sweet dreams. Goodnight, sweet little jam-maker.",
                "quote": "🌙 'Malam yang manis memeluk mereka yang telah menebarkan rasa manis ke sekelilingnya.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak manis, semoga mimpimu malam ini seindah dan semanis buah stroberi.",
                "imagePrompt": "Serene bedtime illustration of girl Tita sleeping peacefully hugging her soft bunny Mimi in a warm cottage bedroom. Moonbeams light up the strawberry jars on the dresser, soft wax crayon and oil pastel, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s48)

    # =========================================================================
    # STORY 49: Biskuit Bintang untuk Tetangga
    # =========================================================================
    s49 = {
        "id": "biskuit-bintang-tetangga",
        "storyNumber": 49,
        "title": "Biskuit Bintang untuk Tetangga",
        "englishTitle": "Star Cookies for the Neighbors",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Kedermawanan, keramahtamahan bertetangga, dan kehangatan menyapa orang lain",
        "cover": "images/story49_cover.jpg",
        "coverImage": "images/story49_cover.jpg",
        "synopsis": "Hana dan Ibu memanggang biskuit mentega berbentuk bintang keemasan yang renyah harum. Dengan keranjang rotan bertutup serbet katun, Hana berjalan menyusuri jalan desa untuk mengantarkan toples biskuit kepada para tetangga, membawa senyuman di setiap pintu yang ia ketuk.",
        "synopsisEn": "Little Hana and Mama bake golden, star-shaped butter cookies fragrant with vanilla. With a wicker basket covered in a gingham napkin, Hana strolls through the village lane delivering cookie jars to neighbors, leaving smiles at every door she visits.",
        "protagonist": "Hana (Gadis cilik 4 tahun bercelemek merah muda dengan pipi bulat kemerahan)",
        "companion": "Ibu Hana (Ibu ramah berambut sanggul rapi pembawa nampan anyaman)",
        "setting": "Dapur Rumah yang Nyaman & Jalanan Kompleks Desa Berbunga",
        "pages": [
            {
                "number": 1,
                "title": "Adonan Mentega dan Cetakan Bintang",
                "titleEn": "Butter Dough and Star Cutters",
                "textId": "Pagi itu di dapur, aroma mentega manis dan vanili semerbak memenuhi udara. Di atas meja kayu bertabur tepung putih halus, Hana memegang cetakan kue logam berbentuk bintang bersudut lima.",
                "textEn": "That morning in the kitchen, sweet butter and vanilla aromas perfumed the cozy air. Upon the flour-dusted wooden table, little Hana clutched a shiny metal five-pointed star cookie cutter.",
                "quote": "⭐ 'Mencetak kue dengan tangan sendiri adalah cara menuangkan rasa sayang ke dalam bentuk nyata.'",
                "coReading": "💡 Tanya si Kecil: Bentuk cetakan kue apa yang paling kamu sukai saat membuat biskuit?",
                "imagePrompt": "Charming children's book illustration of little girl Hana in a pink apron standing on a wooden stool at the kitchen counter, pressing a star-shaped cutter into rolled butter dough. Mama watches smiling beside her. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Bintang-Bintang Emas di Atas Loyang",
                "titleEn": "Golden Stars Upon the Baking Tray",
                "textId": "Plek, plek, plek! Hana menekan cetakan bintangnya dengan mantap ke adonan kuning keemasan. Satu per satu, bintang-bintang biskuit kecil berbaris rapi di atas loyang yang telah diolesi mentega wangi.",
                "textEn": "Press, press, pop! Hana stamped her star cutter firmly into the golden dough. One by one, little star biscuits lined up neatly across the butter-greased baking sheet, looking like a constellation on the table.",
                "quote": "✨ 'Ketelitian dan kehati-hatian membuat setiap biskuit kecil tampak begitu cantik.'",
                "coReading": "💡 Hitung Bersama: Coba hitung bintang-bintang di gambar dari 1 sampai 5 bersama si kecil!",
                "imagePrompt": "Delightful storybook scene of neat rows of pale-yellow star-shaped dough pieces resting on a baking sheet. Flour dust floats in the sunlit air, wax crayon scribbles, naive folk art, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Kehangatan Tungku dan Taburan Gula",
                "titleEn": "Hearth Warmth and Sugar Sparkles",
                "textId": "Ibu memasukkan loyang ke dalam oven yang hangat. Saat biskuit mulai matang dan harum semerbak, Hana menaburkan gula palem halus di atasnya sehingga permukaannya berkilau seperti bintang sungguhan.",
                "textEn": "Mama slid the tray into the warm oven. As the cookies baked to golden perfection, Hana sprinkled fine raw cane sugar over the tops, making them sparkle like real little evening stars.",
                "quote": "🌟 'Sentuhan kecil dari ketulusan hati memberi kilau terindah pada apa pun yang kita buat.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat kue yang berkilau karena taburan gula halus?",
                "imagePrompt": "Warm children's book illustration showing golden baked star cookies cooling on a wire rack, with little girl Hana sprinkling sparkling sugar from a small ceramic pot. Soft golden glow, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Toples Kaca Berpita Kuning",
                "titleEn": "Glass Jars Tied with Golden Ribbons",
                "textId": "Biskuit yang renyah dimasukkan dengan hati-hati ke dalam empat toples kaca bening. Ibu mengikatkan pita kain kuning cerah di leher toples. \"Ini adalah toples kehangatan untuk tetangga kita,\" kata Ibu ramah.",
                "textEn": "The crisp cookies were packed carefully into four clean glass jars. Mama tied bright yellow fabric ribbons around each jar neck. \"These are jars of warmth for our dear neighbors,\" said Mama warmly.",
                "quote": "🫙 'Hadiah yang dikemas dengan rapi menunjukkan betapa kita menghargai orang yang menerimanya.'",
                "coReading": "💡 Tanya si Kecil: Kepada tetangga siapa kamu ingin memberikan biskuit manis ini?",
                "imagePrompt": "Charming illustration of four glass jars filled with golden star cookies, tied with yellow bows, sitting in a woven basket lined with red-and-white checked cloth, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Langkah Riang di Jalanan Desa",
                "titleEn": "Skipping Down the Village Lane",
                "textId": "Sore itu sejuk dan bersahabat. Hana menggandeng tangan Ibu sambil menjinjing keranjang rotannya. Burung-burung pipit berkicau di dahan pohon kamboja menyemangati langkah kaki kecil Hana.",
                "textEn": "The afternoon was pleasantly cool and serene. Hana held Mama's hand while swinging her wicker basket. Little sparrows chirped among the frangipani branches, cheering Hana's eager little footsteps along the lane.",
                "quote": "🏡 'Menjalin silaturahmi dengan tetangga membuat lingkungan terasa seperti keluarga besar.'",
                "coReading": "💡 Aktivitas Seru: Melangkahlah riang bersama si kecil: 'Satu, dua, tiga, kita kunjungi tetangga!'",
                "imagePrompt": "Picturesque children's book scene of little girl Hana walking with her mother down a cozy cobblestone village lane lined with blooming flower gardens and picket fences. Soft afternoon lighting, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Ketukan Pertama di Pintu Kakek Joko",
                "titleEn": "First Knock at Grandpa Joko's Door",
                "textId": "Tok-tok-tok! Hana mengetuk pintu kayu hijau rumah Kakek Joko si tukang kebun tua. Saat pintu terbuka, Kakek Joko tertegun melihat gadis kecil bercelemek merah muda menyodorkan toples biskuit dengan senyuman tulus.",
                "textEn": "Tap-tap-tap! Hana tapped on the green wooden door of Grandpa Joko, the retired village gardener. When the door opened, Grandpa Joko marveled at the sweet little girl in the pink apron offering a cookie jar with a bright smile.",
                "quote": "👴 'Senyuman anak kecil yang tulus bisa menceriakan hari siapa saja yang melihatnya.'",
                "coReading": "💡 Tanya si Kecil: Apa yang kamu katakan saat memberikan sesuatu kepada orang yang lebih tua?",
                "imagePrompt": "Heartwarming illustration of kindly elderly Grandpa Joko with white hair bending down with a wide touched smile as little Hana hands him a jar of star cookies at his doorstep, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Biskuit untuk Bayi di Seberang Jalan",
                "titleEn": "Cookies for the Baby Across the Lane",
                "textId": "Di rumah kedua, Tante Rini yang sedang menggendong bayinya menyambut mereka dengan gembira. \"Terima kasih, Hana manis! Aromanya harum sekali!\" Bayi kecil di gendongan bertepuk tangan riang melihat bentuk bintang.",
                "textEn": "At the second cottage, Auntie Rini carrying her baby greeted them with joyful surprise. \"Thank you, sweet Hana! These smell wonderfully heavenly!\" The baby clapped soft chubby hands at the shiny star shapes.",
                "quote": "👶 'Berbagi membawa gelak tawa yang membuat seluruh rumah terasa lebih hidup.'",
                "coReading": "💡 Aktivitas Seru: Tirukan tepuk tangan bayi kecil yang gembira: 'Prok-prok-prok!'",
                "imagePrompt": "Sweet children's storybook scene of Hana handing the second cookie jar to a smiling neighbor holding a baby at a sunny front porch with potted marigolds, wax crayon folk art, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Keranjang yang Kosong, Hati yang Penuh",
                "titleEn": "An Empty Basket, a Full Heart",
                "textId": "Setelah toples ketiga dan keempat dibagikan ke rumah Pak Pos dan Nenek Siti, keranjang anyaman Hana kini kosong tak bersisa. Namun anehnya, dada Hana terasa sangat penuh dan hangat oleh rasa sukacita.",
                "textEn": "After the third and fourth jars were delivered to the mailman and Grandmother Siti, Hana's wicker basket was entirely empty. Yet surprisingly, Hana's little chest felt overwhelmingly full and warm with golden joy.",
                "quote": "💖 'Semakin banyak kebaikan yang kita bagikan, semakin penuh hati kita dengan kebahagiaan.'",
                "coReading": "💡 Tanya si Kecil: Mengapa memberi membuat hati kita merasa senang dan lega?",
                "imagePrompt": "Touching illustration of little Hana looking into her empty basket with a blissful, beaming smile, standing on a flower-lined lane at sunset, holding Mama's hand, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Menikmati Biskuit Terakhir Berdua",
                "titleEn": "Sharing the Very Last Cookie",
                "textId": "Di beranda rumah sendiri, Ibu merogoh saku celemeknya. Ternyata masih ada satu biskuit bintang terakhir yang tersisa! Ibu membelahnya menjadi dua bagian yang sama besar, lalu menikmati kerenyahannya bersama Hana di bawah senja jingga.",
                "textEn": "Back on their own front porch, Mama reached into her apron pocket. There was one single last star cookie saved! Mama broke it into two equal halves, sharing the buttery crispness with Hana beneath the orange twilight.",
                "quote": "☕ 'Biskuit yang dibagi dua terasa jauh lebih lezat daripada sepiring kue yang dimakan sendirian.'",
                "coReading": "💡 Berbagi Makanan: Berikan setengah potongan biskuitmu kepada orang di sampingmu sambil tersenyum!",
                "imagePrompt": "Cozy picture book illustration of Hana and Mama sitting on wooden porch chairs, sharing the two halves of a star cookie, watching the golden sunset sky fade into violet, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur di Bawah Taburan Bintang Asli",
                "titleEn": "Sleeping Beneath Real Starlight",
                "textId": "Malam tiba membawa langit yang dipenuhi ribuan bintang sungguhan. Di ranjangnya yang nyaman, Hana memejamkan mata dengan damai. Seluruh desa tertidur malam ini dengan rasa manis persaudaraan yang indah. Selamat tidur, gadis bintang kecil.",
                "textEn": "Night arrived carrying a velvet sky adorned with thousands of real glittering stars. In her snug bed, little Hana closed her eyes in pure peace. The entire village slept tonight cushioned in the sweet warmth of neighborhood love. Goodnight, little star-baker.",
                "quote": "🌙 'Anak yang gemar berbagi akan selalu dijaga oleh bintang-bintang kedamaian.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak murah hati, semoga hatimu selalu memancarkan kebaikan seperti bintang.",
                "imagePrompt": "Serene bedtime illustration of little girl Hana sleeping soundly under a star-patterned quilt, smiling peacefully. Through the window, real stars twinkle gently in a deep navy blue sky, wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s49)

    # =========================================================================
    # STORY 50: Roti Gandum Hangat Musim Salju
    # =========================================================================
    s50 = {
        "id": "roti-gandum-salju",
        "storyNumber": 50,
        "title": "Roti Gandum Hangat Musim Salju",
        "englishTitle": "Warm Wheat Loaf in Winter",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Kepedulian terhadap yang membutuhkan, kehangatan empati, dan pengorbanan kecil",
        "cover": "images/story50_cover.jpg",
        "coverImage": "images/story50_cover.jpg",
        "synopsis": "Salju pertama turun menyelimuti Hutan Cemara dengan dingin yang membeku. Milo si rubah kecil bermantel wol merah memutuskan mengantarkan sebongkah roti gandum yang baru keluar dari tungku menembus bukit salju untuk Nenek Kelinci yang tinggal sendirian di pondok ujung bukit.",
        "synopsisEn": "The first snowfall blankets the Pine Forest in freezing white. Milo the little fox in his red wool coat journeys across snowy hills to deliver a steaming, freshly baked loaf of hearty wheat bread to elderly Grandmother Bunny who lives alone.",
        "protagonist": "Milo (Rubah kecil berbulu oranye hangat dengan mantel rajut merah dan syal tebal)",
        "companion": "Piko (Burung pipit kecil berbulu cokelat yang terbang lincah menembus salju)",
        "setting": "Hutan Cemara Bersalju Putih & Pondok Kayu Berapian Hangat",
        "pages": [
            {
                "number": 1,
                "title": "Salju Putih Pertama Turun",
                "titleEn": "The First White Snowfall",
                "textId": "Keping-keping salju putih halus melayang turun dari langit kelabu, menyelimuti ranting cemara dan tanah hutan seperti karpet kapuk tebal. Dari jendela pondoknya yang berasap, Milo si rubah kecil mengamati dunia yang mendadak menjadi putih dan dingin.",
                "textEn": "Delicate white snowflakes drifted softly from the gray sky, blanketing pine boughs and forest soil like a thick fluffy quilt. From the steamed window of his cottage, Milo the little fox watched the world turn silent, white, and freezing.",
                "quote": "❄️ 'Salju yang turun membawa keheningan sunyi ke seluruh penjuru alam.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu membayangkan bagaimana rasanya menyentuh salju dingin yang lembut?",
                "imagePrompt": "Charming children's book illustration of little orange fox Milo in a cozy knitted red coat looking out through a frosty cottage window at falling snowflakes and snow-covered pine trees. Handcrafted wax crayon and oil pastel on textured paper, simple bead eyes, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Roti Gandum Mengepul Hangat",
                "titleEn": "Steaming Warm Wheat Loaf",
                "textId": "Di atas meja dapur Milo, sebuah roti gandum lonjong baru saja keluar dari loyang pemanggang. Kulitnya cokelat keemasan dan aromanya sangat harum. Uap hangatnya mengepul lembut, melawan hawa beku yang menyusup di celah pintu.",
                "textEn": "Upon Milo's kitchen table, an oval loaf of hearty wheat bread had just emerged from the baking hearth. Its crust was golden-brown and fragrant with yeast. Gentle steam rose into the chilly air, defying the winter freeze.",
                "quote": "🍞 'Sebongkah roti yang hangat adalah lentera kecil bagi perut yang lapar.'",
                "coReading": "💡 Tanya si Kecil: Makanan hangat apa yang paling enak disantap saat hari sedang hujan atau dingin?",
                "imagePrompt": "Close-up storybook illustration of a crusty golden-brown loaf of artisan bread steaming on a wooden cutting board, with soft butter yellow and earthy brown crayon strokes on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Ingatan tentang Nenek Kelinci",
                "titleEn": "Remembering Grandmother Bunny",
                "textId": "Piko si burung pipit hinggap di ambang jendela sambil menggigil pelan. \"Cuit-cuit! Nenek Kelinci di pondok bukit sedang sakit dan kehabisan kayu bakar. Ia pasti kedinginan dan belum makan apa-apa hari ini!\"",
                "textEn": "Piko the little sparrow perched on the snowy sill, shivering slightly. \"Chirp-chirp! Grandmother Bunny in the hilltop cabin is ill and out of firewood. She must be freezing cold and has had nothing to eat today!\"",
                "quote": "👵 'Mengingat mereka yang lemah dan sendirian adalah awal dari perbuatan mulia.'",
                "coReading": "💡 Tanya si Kecil: Apa yang bisa kita lakukan jika mendengar seorang kawan atau kakek-nenek sedang sakit?",
                "imagePrompt": "Touching illustration of little fox Milo listening attentively to sparrow Piko perched on the snowy window sill. Milo's eyes are filled with caring empathy. Wax crayon textures, warm cozy interior vs snowy exterior, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Bungkus Kain Linen Tebal",
                "titleEn": "Wrapped in Warm Linen Cloth",
                "textId": "Tanpa ragu sedikit pun, Milo mengambil kain linen tebal dan membungkus roti gandum hangat itu rapat-rapat agar panasnya tidak hilang. Ia memasukkannya ke dalam tas selempang kulitnya, lalu mengenakan sepatu bot bulu dan syalnya.",
                "textEn": "Without a moment's hesitation, Milo took a thick linen cloth and wrapped the steaming wheat loaf snugly so its precious heat wouldn't escape. He tucked it into his leather satchel, pulling on his furry winter boots and woolly scarf.",
                "quote": "🧣 'Kasih sayang membungkus niat baik kita dengan kehangatan yang tak mudah padam.'",
                "coReading": "💡 Aktivitas Seru: Tirukan gerakan melilitkan syal leher hangat sebelum keluar rumah!",
                "imagePrompt": "Storybook scene of fox Milo carefully wrapping the warm loaf in woven cloth and strapping his satchel, ready for a winter journey. Cute little red boots, naive folk art, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Jejak Kaki Menembus Salju Tebal",
                "titleEn": "Footprints Through the Deep Snow",
                "textId": "Kres, kres, kres! Sepatu bot Milo membenam ke dalam salju putih yang tebal. Angin dingin meniup bulu telinganya, tetapi pelukan tas berisi roti hangat di dadanya membuat tubuh Milo tetap merasa bertenaga.",
                "textEn": "Crunch, crunch, crunch! Milo's little boots sank into the deep white snowdrifts. The biting winter wind whipped against his ears, but the warm loaf clutched close against his chest kept his little heart burning bright.",
                "quote": "👣 'Langkah kaki yang diniatkan untuk menolong orang lain tidak akan pernah merasa sia-sia.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara menginjak salju tebal bersama si kecil: 'Kres... kres... kres...'",
                "imagePrompt": "A heartwarming children's book illustration of little fox Milo in his bright red coat trudging bravely through deep white snowdrifts between snowy pine trees, with sparrow Piko fluttering ahead to guide the way, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Panduan Sayap Si Burung Pipit",
                "titleEn": "The Little Sparrow's Guiding Wings",
                "textId": "Piko terbang rendah dari dahan ke dahan, menunjukkan jalan setapak yang tidak tertimbun jurang salju. \"Lewat sini, Milo! Di balik bukit cemara kecil itu pondoknya sudah terlihat!\"",
                "textEn": "Piko fluttered low from bough to bough, pointing out the safest ridge that avoided hidden snow drifts. \"This way, dear Milo! Just over that gentle pine rise, the little cabin is in sight!\"",
                "quote": "🕊️ 'Sahabat kecil yang setia adalah penunjuk jalan paling berharga dalam badai.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah seorang teman membantumu saat kamu kebingungan mencari jalan?",
                "imagePrompt": "Whimsical illustration of sparrow Piko flying ahead of Milo through softly falling snowflakes, pointing toward a tiny wooden cabin nestled among snow-laden evergreen trees, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Asap Tipis dari Cerobong Pondok",
                "titleEn": "Faint Smoke from the Cabin Chimney",
                "textId": "Di puncak bukit salju, pondok kayu tua Nenek Kelinci tampak kedinginan. Dari cerobongnya hanya ada seuntai asap tipis yang hampir padam. Milo bergegas mempercepat langkah kakinya mendekati pintu.",
                "textEn": "At the snowy hillcrest, Grandmother Bunny's old wooden cabin sat weathered and chilled. From its stone chimney rose only the faintest wisp of dying smoke. Milo hurried his footsteps toward the snow-banked door.",
                "quote": "🏠 'Kehadiran kita yang tepat waktu adalah hadiah yang paling melegakan bagi yang menanti.'",
                "coReading": "💡 Tanya si Kecil: Mengapa cerobong asap yang hampir padam menandakan api di dalam rumah kedinginan?",
                "imagePrompt": "Atmospheric winter illustration of the small wooden cabin buried in soft white snow under twilight shadows, with Milo arriving at the front porch brushing snow off his coat, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Membuka Pintu Membawa Kehangatan",
                "titleEn": "Opening the Door with Warmth",
                "textId": "Tok-tok-tok! \"Nenek, ini Milo!\" Pintu kayu berderit terbuka perlahan. Di dalam, Nenek Kelinci duduk berselimut perca dengan mata yang redup. Saat Milo membuka bungkus linennya, aroma roti gandum panas seketika memenuhi seluruh ruangan.",
                "textEn": "Knock-knock-knock! \"Grandmother, it's Milo!\" The wooden door creaked gently open. Inside, Grandmother Bunny sat wrapped in patchwork quilts with weary eyes. When Milo unwrapped the linen cloth, the rich fragrance of hot bread instantly filled the chilly room.",
                "quote": "✨ 'Aroma kebaikan yang tulus mampu mencairkan dingin yang paling beku sekalipun.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana ekspresi wajah Nenek Kelinci saat melihat roti hangat datang?",
                "imagePrompt": "Heartwarming children's book scene inside the dim, chilly cabin. Little fox Milo opens the steaming bread loaf before frail Grandmother Bunny, whose face lights up with tears of relief and gratitude, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Makan Bersama di Dekat Perapian",
                "titleEn": "Eating Together by the Restored Hearth",
                "textId": "Milo membantu menyalakan kembali api di perapian dengan ranting kering. Nenek Kelinci memotong roti gandum itu menjadi irisan tebal dan mengolesnya dengan sedikit mentega. Mereka makan bersama dalam kehangatan yang meluap-luap.",
                "textEn": "Milo helped rekindle the hearth fire with dry twigs from his pouch. Grandmother Bunny sliced the hearty bread into thick, steaming slabs with a dab of churned butter. They dined together in an overflow of deep, comforting warmth.",
                "quote": "🔥 'Kehangatan yang sesungguhnya bukan berasal dari api perapian, melainkan dari kepedulian hati.'",
                "coReading": "💡 Tanya si Kecil: Apa yang membuat makan malam terasa paling hangat dan membahagiakan?",
                "imagePrompt": "Joyous and comforting picture book illustration of fox Milo, sparrow Piko, and Grandmother Bunny sitting around a crackling stone fireplace, eating thick warm slices of bread, drinking hot tea. Soft amber and peach crayon tones, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Damai Menanti Esok Pagi",
                "titleEn": "Peaceful Sleep Awaiting Morning",
                "textId": "Malam itu, setelah memastikan Nenek Kelinci tidur lelap berselimut hangat di samping perapian yang menyala, Milo kembali ke pondoknya dengan hati yang damai. Di ranjangnya sendiri, Milo tertidur pulas dalam pelukan malam musim salju yang tenang. Selamat tidur, rubah kecil yang penuh cinta.",
                "textEn": "That night, after tucking Grandmother Bunny into a warm quilt beside a merry crackling hearth, Milo returned to his own cabin with a deeply peaceful heart. In his own snug bed, Milo fell fast asleep in winter's tranquil embrace. Goodnight, loving little fox.",
                "quote": "🌙 'Mereka yang membagikan kehangatan kepada orang lain akan tidur dalam pelukan damai yang abadi.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak penyayang, semoga kebaikan hatimu selalu menghangatkan siapa pun yang kamu temui.",
                "imagePrompt": "A tranquil winter bedtime illustration of little fox Milo sleeping curled up under a thick red quilt in his cozy bedroom. Snow falls softly outside the frosted window where moonlight shines, handcrafted wax crayon on cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s50)

    return stories

print("Story module 48-50 defined successfully")
