# scripts/polish_stories_68_to_72.py
import json

def get_stories_68_to_72():
    stories = [
        # --- STORY 68: Kotak Sarang di Pohon Mangga ---
        {
            "id": "story68",
            "storyNumber": 68,
            "title": "Kotak Sarang di Pohon Mangga",
            "englishTitle": "The Nest Box in the Mango Tree",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kepedulian terhadap satwa liar & menciptakan rumah aman",
            "cover": "covers/story68_cover.jpg",
            "synopsis": "Kakek dan cucunya membuat kotak sarang kayu beratap miring untuk diletakkan di dahan pohon mangga yang lebat. Ketika hujan deras mengguyur desa, sepasang burung gereja menemukan tempat berlindung yang kering dan hangat untuk membesarkan anak-anaknya.",
            "protagonist": "Pak Tani & Cucu (Kakek bertukang kayu dan cucunya)",
            "companion": "Sepasang Burung (Burung gereja bersarang nyaman)",
            "setting": "Dahan Pohon Mangga Lebat",
            "pages": [
                {
                    "number": 1,
                    "title": "Papan-Papan Kayu Bekas",
                    "titleEn": "Scraps of Wooden Planks",
                    "textId": "Di bawah naungan teras bengkel kakek, terhampar potongan papan kayu pinus sisa pembuatan rak buku. Arka, anak laki-laki dengan celemek kanvas kecil, memegang mistar kayu sambil mengamati kakeknya yang mengukur sudut dengan cermat. Harum serbuk kayu berterbangan seperti debu emas di udara pagi.",
                    "textEn": "Beneath the shade of grandpa's workshop porch lay scrap pine planks left over from building a bookshelf. Arka, a young boy in a little canvas apron, held a wooden ruler while watching his grandfather carefully measure the angles. The scent of pine sawdust danced like golden dust in the morning air.",
                    "quote": "Bahan sederhana di tangan penuh kasih bisa menjadi tempat bernaung berharga.",
                    "coReading": "Pernahkah kamu mencium wangi kayu yang baru dipotong?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on textured cream watercolor paper. Elderly kind grandfather in carpenter overalls and young grandson Arka in canvas apron measuring pine planks at a rustic outdoor workbench. Golden morning light, sawdust specks, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Ketukan Palu dan Lubang Mungil",
                    "titleEn": "Hammer Taps and a Round Door",
                    "textId": "'Tok, tok, tok!' Ketukan palu kakek menautkan dinding-dinding papan menjadi sebuah kotak kokoh. Kakek membuat lubang bundar seukuran tutup botol di bagian depan. 'Lubang ini cukup untuk burung gereja masuk, tetapi terlalu sempit bagi kucing pemangsa,' jelas Kakek tersenyum.",
                    "textEn": "'Tap, tap, tap!' Grandpa's hammer fastened the wooden boards into a sturdy box. He drilled a round opening the size of a jar lid in the front. 'This hole is just right for sparrows to flutter in, but too narrow for prowling cats,' Grandpa explained with a smile.",
                    "quote": "Merancang perlindungan membutuhkan kecermatan dan kelembutan rasa.",
                    "coReading": "Mengapa pintu rumah burung dibuat pas seukuran badannya?",
                    "imagePrompt": "Wax crayon scribbles on heavy cream paper. Kind grandfather helping Arka hold a sturdy wooden nest box with a neat circular entrance hole and slanted roof. Carpenter tools on table, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Kasur Rumput dan Sabut Kelapa",
                    "titleEn": "Mattress of Grass and Coconut Fiber",
                    "textId": "Arka mengumpulkan rumput kering yang wangi dan helai-helai sabut kelapa lembut dari kebun. Melalui atap kotak yang bisa dibuka, Arka menata bantalan empuk di lantai kotak. 'Sekarang burung-burung akan tidur sehangat di atas kasur kapuk,' gumam Arka gembira.",
                    "textEn": "Arka collected fragrant dried grass and soft strands of coconut fiber from the yard. Through the hinged roof, he arranged a fluffy cushion across the box floor. 'Now the birds will sleep as warm as on a down mattress,' Arka murmured happily.",
                    "quote": "Perhatian pada kenyamanan orang lain adalah inti dari keramahan sejati.",
                    "coReading": "Benda apa yang menurutmu paling empuk untuk tempat tidur anak burung?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Arka gently placing soft golden dry grass and shredded coconut fiber into the wooden birdhouse. Soft sunlight illuminating his smiling face, simple black bead dot eyes, warm colors, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Memanjat Tangga Bambu",
                    "titleEn": "Climbing the Bamboo Ladder",
                    "textId": "Kakek menyandarkan tangga bambu tinggi ke dahan utama pohon mangga berdaun lebat. Dengan hati-hati, Kakek memanjat sambil membawa kotak sarang, sementara Arka memegangi kaki tangga di bawah. 'Sedikit lebih tinggi di balik rimbun dedaunan agar terlindung dari terik matahari,' bisik Kakek.",
                    "textEn": "Grandpa rested a tall bamboo ladder against the main branch of the leafy mango tree. Carefully, Grandpa climbed while carrying the nest box, while Arka steadied the ladder feet below. 'A little higher behind the lush leaves, so it stays shaded from the hot sun,' whispered Grandpa.",
                    "quote": "Kerja sama menjaga keselamatan dan mewujudkan impian indah.",
                    "coReading": "Apakah kamu pernah melihat pohon mangga yang rimbun dan teduh?",
                    "imagePrompt": "Warm wax crayon drawing. Grandpa steady on a bamboo ladder securing the wooden birdhouse to a thick mossy tree branch of a leafy mango tree. Arka standing at the base looking up with hands on the ladder. Lush green leaves, textured paper, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Terpasang Kokoh di Dahan",
                    "titleEn": "Fastened Firm on the Branch",
                    "textId": "Kotak kayu kini terikat kuat menggunakan tali ijuk tebal yang tidak melukai kulit batang pohon. Atapnya yang miring condong ke depan untuk mengalirkan air hujan. Dari bawah, rumah burung itu tampak tersembunyi manis di balik buah mangga muda yang hijau menggantung.",
                    "textEn": "The wooden box was now securely bound with thick palm-fiber ropes that would not harm the tree bark. Its slanted roof leaned forward to shed rainwater. From below, the birdhouse looked nestled sweetly behind hanging green baby mangoes.",
                    "quote": "Kebaikan yang tersembunyi sering kali menjadi tempat bernaung paling damai.",
                    "coReading": "Bisakah kamu melihat mangga-mangga kecil di sekitar kotak sarang?",
                    "imagePrompt": "Handcrafted oil pastel on cream paper. Close-up of the wooden nest box tied securely to a sturdy mango branch nestled among lush emerald leaves and small green baby mangoes. Gentle dappled sunlight, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Tamu Bersayap Pertama",
                    "titleEn": "The First Winged Guests",
                    "textId": "Siang hari ketika suasana hening, suara 'Cuit, cuit!' terdengar riang. Dua ekor burung gereja berbulu cokelat keemasan bertengger di dahan dekat kotak. Kepalanya miring ke kiri dan ke kanan, memeriksa lubang bundar dengan rasa ingin tahu yang besar.",
                    "textEn": "In the quiet afternoon, a merry 'Chirp, chirp!' echoed through the branches. Two golden-brown sparrows perched on the branch near the box. Tilting their heads left and right, they inspected the round doorway with great curiosity.",
                    "quote": "Pintu yang terbuka dengan tulus selalu disambut dengan sukacita.",
                    "coReading": "Apa yang dilakukan burung-burung saat pertama melihat rumah baru?",
                    "imagePrompt": "Wax crayon scribbles and oil pastel smudges. Two cute plump brown sparrows perched on the branch right outside the circular entrance of the wooden birdhouse, peeking inside playfully. Simple bead dot eyes, soft textures, completely text-free, 4:3 horizontal."
                },
                {
                    "number": 7,
                    "title": "Rumah Baru yang Aman",
                    "titleEn": "A Safe New Home",
                    "textId": "Burung jantan menyusup ke dalam lubang terlebih dahulu. Tak lama kemudian ia keluar sambil berkicau gembira, mengajak pasangannya masuk. Mereka melompat-lompat di atas kasur rumput buatan Arka. Rumah itu kering, harum, dan bebas dari hembusan angin dingin.",
                    "textEn": "The little male sparrow hopped inside first. Moments later he poked out singing delightfully, inviting his mate inside. They hopped happily across the grass cushion Arka had made. The house was dry, sweet-smelling, and sheltered from chilly winds.",
                    "quote": "Rasa aman adalah hadiah paling menenangkan bagi setiap jiwa.",
                    "coReading": "Bagaimana burung menunjukkan rasa senangnya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Cutaway view of the cozy wooden birdhouse interior with two sparrows snuggled on a golden bed of dried grass, their eyes glowing with contentment. Dappled forest light outside, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Hujan Deras di Penghujung Hari",
                    "titleEn": "Downpour at Day's End",
                    "textId": "Sore itu langit gelap mendadak tumpah dalam hujan lebat. Angin mengguncang dedaunan pohon mangga, dan guntur bergemuruh di kejauhan. Arka berdiri di jendela kamar dengan cemas, mengkhawatirkan burung-burung kecil di kebun.",
                    "textEn": "That late afternoon, dark clouds burst into a heavy downpour. Wind shook the mango leaves, and thunder rumbled far away. Arka stood at his bedroom window with worry, thinking of the little birds out in the garden.",
                    "quote": "Cinta sejati membuat kita peduli pada keselamatan sesama makhluk.",
                    "coReading": "Apakah kamu pernah merasa cemas memikirkan hewan saat hujan lebat?",
                    "imagePrompt": "Handcrafted oil pastel and wax crayon. Arka looking out of a glass bedroom window streaked with raindrops. In the background, rainy garden with the mango tree swaying gently in the rainstorm, cozy warm lamp reflecting inside room, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Kicauan Hangat di Balik Hujan",
                    "titleEn": "Warm Chirps in the Rain",
                    "textId": "Namun dari balik rimbunnya dedaunan, tidak ada burung yang basah kuyup. Di dalam kotak sarang kayu, sepasang burung gereja meringkuk hangat tanpa terkena setetes air pun. Dari lubang bundar, terdengar kicauan lirih yang merdu mengalun di tengah deburan hujan.",
                    "textEn": "Yet behind the leafy branches, no birds were soaked. Inside the wooden nest box, the sparrow pair nestled warm and dry, not a single droplet touching their feathers. Through the round doorway floated a soft, sweet chirp amid the drumming rain.",
                    "quote": "Perlindungan yang kita berikan menjadi benteng di kala badai.",
                    "coReading": "Burung-burung itu aman dan kering di dalam rumahnya!",
                    "imagePrompt": "Wax crayon scribbles on textured paper. Close-up of the wooden nest box in the rain, raindrops bouncing off the slanted wooden roof, while from inside the dark circular door, two little sparrow beaks poke out safely. Cozy and heartwarming mood, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Lelap di Dahan Teduh",
                    "titleEn": "Sound Sleep on the Shady Bough",
                    "textId": "Hujan reda menyisakan aroma tanah basah dan tetesan air berkerlap-kerlip di pucuk daun. Kakek tersenyum menepuk pundak Arka. 'Tidurlah, Arka. Malam ini kawan-kawan kecil kita tidur nyenyak di rumah buatanmu.' Di bawah langit bertabur bintang, pohon mangga berdiri megah menjaga sarang yang damai.",
                    "textEn": "The rain cleared, leaving fresh earth scents and shimmering droplets on leaf tips. Grandpa smiled, patting Arka's shoulder. 'Sleep well, Arka. Tonight our little friends sleep soundly in the home you helped build.' Under a starry sky, the mango tree stood tall, cradling the peaceful nest.",
                    "quote": "Tidurlah dengan bahagia, kebaikan tanganmu telah memberi rumah bagi sesama.",
                    "coReading": "Mari pejamkan mata dan bayangkan burung-burung tidur hangat di sarangnya.",
                    "imagePrompt": "Handcrafted wax crayon and soft oil pastel on heavy cream watercolor paper. Arka tucked comfortably under a warm quilt in bed with grandpa smiling by his door. Outside the bedroom window, the leafy mango tree silhouetted under a starry night sky with a gentle glowing crescent moon. Peaceful bedtime scene, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 69: Hotel Bambu untuk Sahabat Serangga ---
        {
            "id": "story69",
            "storyNumber": 69,
            "title": "Hotel Bambu untuk Sahabat Serangga",
            "englishTitle": "Bamboo Hotel for Bug Friends",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menghargai serangga penyerbuk & melestarikan keanekaragaman hayati",
            "cover": "covers/story69_cover.jpg",
            "synopsis": "Dara menyusun potongan ruas-ruas bambu berongga dan batang ilalang kering di dalam bingkai kayu gantung di sudut kebun bunga liar. Hotel bambu buatannya segera dipenuhi oleh lebah soliter dan kepik yang mencari tempat tidur hangat di malam hari.",
            "protagonist": "Dara (Gadis cilik bercelana katun saku)",
            "companion": "Lebah Soliter (Lebah kecil pencari nektar bunga)",
            "setting": "Sudut Kebun Bunga Liar",
            "pages": [
                {
                    "number": 1,
                    "title": "Serangga Kecil di Balik Kelopak",
                    "titleEn": "Little Bugs Behind Petals",
                    "textId": "Di sudut kebun bunga liar yang penuh zinnia jingga dan kenikir kuning, Dara berlutut mengamati seekor lebah kecil bergaris hitam-kuning. Lebah itu tampak kelelahan, bersandar di bawah kelopak bunga yang basah oleh sisa gerimis pagi.",
                    "textEn": "In a wild flower garden corner blooming with orange zinnias and yellow marigolds, Dara knelt watching a tiny black-and-yellow striped solitary bee. The bee looked tired, resting beneath a petal still moist with morning drizzle.",
                    "quote": "Makhluk terkecil pun membutuhkan tempat berteduh untuk memulihkan tenaga.",
                    "coReading": "Pernahkah kamu melihat lebah kecil hinggap diam di bunga?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy textured cream watercolor paper. Dara, a young girl in cotton overalls with deep pockets, kneeling beside a blooming bush of wildflowers, looking gently at a tiny solitary bee on a flower. Morning dewdrops, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Potongan Bambu Berongga",
                    "titleEn": "Hollow Bamboo Tubes",
                    "textId": "Ibu menjelaskan bahwa lebah soliter tidak tinggal di sarang madu besar seperti lebah madu biasa. Mereka hidup sendiri dan menyukai terowongan sempit untuk tidur dan bertelur. Dara teringat tumpukan ranting bambu kuning kering di samping pagar kebun.",
                    "textEn": "Mother explained that solitary bees do not live in big hives like honeybees. They live on their own, loving narrow wooden tunnels to sleep and lay eggs. Dara remembered a pile of dry yellow bamboo canes beside the garden fence.",
                    "quote": "Belajar memahami kebutuhan alam membuat hati kita semakin peka.",
                    "coReading": "Tahukah kamu bahwa tidak semua lebah tinggal di sarang madu raksasa?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Dara and mother standing by garden fence examining bamboo poles. Mother pointing to hollow bamboo stems, warm educational moment, simple black bead dot eyes, naive folk art, text-free, 4:3 horizontal."
                },
                {
                    "number": 3,
                    "title": "Memotong dan Menghaluskan Rongga",
                    "titleEn": "Cutting and Smoothing the Tubes",
                    "textId": "Bersama Ayah, Dara memotong bambu menjadi silinder-silinder sepanjang jengkal tangan. Ayah menggunakan amplas halus untuk merapikan tepi setiap lubang agar sayap-sayap tipis serangga tidak robek saat masuk. Dara mengumpulkan puluhan silinder bambu dengan ukuran lubang berbeda-beda.",
                    "textEn": "Together with Dad, Dara cut the bamboo into cylinders the length of a handspan. Dad used fine sandpaper to smooth every tube opening so delicate bug wings would not tear upon entering. Dara gathered dozens of bamboo cylinders of varying hole sizes.",
                    "quote": "Ketelitian kecil adalah wujud kepedulian terdalam bagi yang rapuh.",
                    "coReading": "Mengapa lubang bambu harus dihaluskan terlebih dahulu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Dara and father sitting on wooden steps smoothing cut bamboo stalks with sandpaper. Piles of hollow bamboo cylinders in a wooden basket, morning sun, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 4,
                    "title": "Kotak Kayu Rumah Singgah",
                    "titleEn": "The Wooden Shelter Box",
                    "textId": "Dara menyiapkan kotak kayu bekas wadah buah yang sudah dicat hijau daun. Di dalamnya, Dara menyusun potongan bambu berongga dengan rapat hingga menyerupai susunan sarang lebah yang rapi. Ia juga menyelipkan batang alang-alang kering dan potongan kulit kayu pinus di sela-selanya.",
                    "textEn": "Dara prepared a salvaged wooden fruit crate painted leaf-green. Inside, she tightly stacked the hollow bamboo pieces until they resembled a neat honeycomb pattern. She also tucked dried reed stalks and pine bark chips between the gaps.",
                    "quote": "Keanekaragaman bahan menyediakan kenyamanan untuk beragam penghuni.",
                    "coReading": "Benda apa saja yang disusun Dara di dalam kotak?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Dara carefully arranging bamboo tubes, dried hollow reeds, and tree bark inside a green wooden crate. A miniature charming bug hotel taking shape, bead dot eyes, naive art, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Menggantung Hotel Serangga",
                    "titleEn": "Hanging the Bug Hotel",
                    "textId": "Ayah membantu menggantung hotel bambu itu pada tiang pagar yang menghadap matahari pagi dan terlindung dari guyuran hujan langsung. Atap kecil miring di atas kotak melindunginya dari terik dan terpaan badai. 'Hotel Serangga Ramah Bunga resmi dibuka!' seru Dara berbisik bangga.",
                    "textEn": "Dad helped hang the bamboo hotel on a sturdy fence post facing the morning sun and sheltered from direct rain. A small slanted roof on top guarded it from sun and storms. 'The Flower-Friendly Bug Hotel is officially open!' Dara whispered with pride.",
                    "quote": "Karya sederhana yang bermanfaat bagi alam bernilai tak terhingga.",
                    "coReading": "Mengapa hotel serangga digantung menghadap arah matahari pagi?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. The green wooden insect hotel mounted on a rustic wooden post surrounded by tall flowering sunflowers and cosmos flowers. Dara clapping her hands happily, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Tamu Pertama Bergaris Kuning",
                    "titleEn": "The First Striped Guest",
                    "textId": "Sore harinya, lebah soliter kecil yang dilihat Dara tadi pagi terbang mendekat. Ia berputar tiga kali di depan kotak, lalu meluncur masuk ke dalam salah satu rongga bambu berdiameter sedang. Kepalanya menyembul sebentar, mengusap antenanya dengan kedua kaki depan seolah merasa sangat puas.",
                    "textEn": "That late afternoon, the tiny solitary bee Dara had seen in the morning flew over. She circled three times before the crate, then slid into one of the medium-sized bamboo tubes. Her head peeked out briefly, wiping her antennae with front legs as if thoroughly satisfied.",
                    "quote": "Bila rumah disiapkan dengan cinta, penghuninya akan datang dengan damai.",
                    "coReading": "Bisakah kamu melihat lebah kecil yang sedang menyembul dari lubang bambu?",
                    "imagePrompt": "Warm oil pastel illustration. Close-up of bamboo tube openings in the insect hotel, with a tiny cute solitary bee resting snug inside one tube, brushing its antennae. Warm golden afternoon light, textured paper, text-free, 4:3 horizontal."
                },
                {
                    "number": 7,
                    "title": "Kepik Merah Berbintik Tujuh",
                    "titleEn": "Seven-Spotted Ladybug",
                    "textId": "Tak lama kemudian, seekor kepik merah cerah dengan tujuh bintik hitam merayap di celah kulit pinus. Kepik itu melipat sayap beningnya di balik perisai merah dan menyusup ke sudut yang paling empuk dan hangat untuk tidur.",
                    "textEn": "Shortly after, a bright red ladybug with seven black spots crawled among the pine bark crevices. Folding her clear wings beneath her red shield, she tucked into the softest, warmest corner for a nap.",
                    "quote": "Setiap makhluk berhak atas tempat istirahat yang aman dan tenang.",
                    "coReading": "Berapa banyak bintik hitam pada punggung kepik merah itu?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. A cute round red ladybug with black dots crawling cozily into a cleft between pine bark pieces inside the bug hotel. Rich natural textures, naive folk art, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 8,
                    "title": "Pintu Ditutup Lumpur Halus",
                    "titleEn": "A Door Sealed with Clay",
                    "textId": "Keesokan harinya, Dara melihat lebah soliter membawa butiran tanah liat basah dengan mulutnya. Dengan tekun, ia menutup mulut rongga bambu dengan dinding tanah liat yang rapi, menjaga tempat tidurnya tetap aman dan hangat dari angin malam.",
                    "textEn": "The next day, Dara watched the solitary bee carrying tiny pellets of damp clay in her mouth. Diligently, she sealed the bamboo tube opening with a neat clay wall, keeping her bed snug and protected from cold night winds.",
                    "quote": "Kerja keras dan ketekunan alam selalu menakjubkan bagi yang memperhatikannya.",
                    "coReading": "Mengapa lebah menutup pintu lubang dengan tanah liat?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A solitary bee plastering a smooth clay door over the bamboo hole. Dara watching in fascinated awe from a respectful distance. Dappled sunlight, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Taman yang Semakin Riang",
                    "titleEn": "A Happier, Living Garden",
                    "textId": "Berkat hotel serangga Dara, kebun bunga mekar semakin subur dan semarak. Kepik-kepik membantu menjaga tanaman dari kutu daun, sementara lebah-lebah membantu penyerbukan buah tomat dan stroberi. Kebun kecil itu kini bernapas dalam harmoni yang sempurna.",
                    "textEn": "Thanks to Dara's insect hotel, the flower garden bloomed richer and more vibrant. Ladybugs kept the plants safe from aphids, while bees helped pollinate juicy tomatoes and strawberries. The little garden breathed in perfect harmony.",
                    "quote": "Kebaikan yang kita tanam bagi alam akan berbuah keindahan berlipat ganda.",
                    "coReading": "Tanaman apa saja di kebun yang dibantu oleh lebah dan kepik?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Lush blooming garden with bright red strawberries, ripening tomatoes, and colorful flowers. Ladybugs on leaves and solitary bees buzzing peacefully around. Dara smiling warmly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Selamat Malam Sahabat-Sahabat Kecil",
                    "titleEn": "Goodnight, Tiny Friends",
                    "textId": "Malam tiba dan embun mulai turun membasahi rumput. Di dalam hotel bambunya, lebah-lebah dan kepik tidur nyenyak di liang masing-masing. Dara mematikan lampu senter kecilnya dan berbisik lembut, 'Selamat tidur, sahabat-sahabat kecilku.'",
                    "textEn": "Night fell and dewdrops dampened the grass. Inside their bamboo hotel, bees and ladybugs slept deeply in their cozy niches. Dara clicked off her little flashlight, whispering gently, 'Goodnight, my tiny friends.'",
                    "quote": "Tidurlah dalam lindungan malam, semesta menjaga setiap napas kehidupan.",
                    "coReading": "Mari pejamkan mata dan bayangkan serangga-serangga tidur lelap di terowongan bambunya.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Night garden scene under a velvety starlit sky and crescent moon. Soft glow illuminating the wooden bug hotel with sleeping bugs tucked inside. Dara at her bedroom window waving goodnight. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 70: Emas Hitam Daun Gugur ---
        {
            "id": "story70",
            "storyNumber": 70,
            "title": "Emas Hitam Daun Gugur",
            "englishTitle": "Black Gold of Fallen Leaves",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Daur ulang alami, pengomposan, & menghargai siklus tanah",
            "cover": "covers/story70_cover.jpg",
            "synopsis": "Hadi mengumpulkan daun-daun kering yang berguguran di halaman dan memasukkannya ke dalam kotak kompos kayu bersama kulit pisang dan sisa sayur. Dengan bantuan cacing tanah dan waktu yang sabar, tumpukan sampah daun berubah menjadi pupuk hitam gembur yang harum seperti tanah hutan.",
            "protagonist": "Hadi (Anak laki-laki bergaru taman mini)",
            "companion": "Cacing Kompos (Cacing pekerja penggembur tanah)",
            "setting": "Kotak Kompos Belakang Rumah",
            "pages": [
                {
                    "number": 1,
                    "title": "Halaman yang Penuh Daun Cokelat",
                    "titleEn": "A Yard Full of Brown Leaves",
                    "textId": "Angin musim gugur meniup dahan pohon nangka dan ketapang, menghujani halaman belakang dengan ribuan helai daun cokelat kering. Hadi, anak laki-laki dengan topi pet kanvas, memegang garu taman kecil bergigi tumpul, bersiap merapikan karpet daun yang berserakan.",
                    "textEn": "The autumn breeze rustled through jackfruit and almond boughs, showering the backyard with thousands of crisp brown leaves. Hadi, a young boy in a canvas cap, held a small blunt-toothed garden rake, ready to tidy the scattered blanket of dry leaves.",
                    "quote": "Setiap helai daun yang gugur menyimpan janji untuk kehidupan yang baru.",
                    "coReading": "Bagaimana suara daun kering saat kamu injak dengan sepatumu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Hadi, a cheerful young boy in a canvas cap and denim dungarees, holding a small wooden leaf rake amidst crunchy piles of brown and amber dry leaves. Golden afternoon sun, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Gundukan Daun Seperti Bukit Keemasan",
                    "titleEn": "A Mound Like a Golden Hill",
                    "textId": "'Srok, srok, srok!' bunyi garu Hadi mengumpulkan daun menjadi gundukan besar setinggi pinggangnya. Daun-daun itu berderik renyah dan beraroma harum kayu kering. Ayah datang membawa gerobak sorong kayu kecil untuk mengangkutnya ke sudut kebun.",
                    "textEn": "'Scrape, scrape, scrape!' sounded Hadi's rake gathering the leaves into a waist-high mound. The leaves crunched crisply, smelling fragrant of dry wood. Dad arrived with a small wooden wheelbarrow to haul them toward the garden corner.",
                    "quote": "Pekerjaan membersihkan halaman menjadi menyenangkan bila dilakukan dengan riang.",
                    "coReading": "Apakah kamu suka melompat ke atas tumpukan daun kering?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Hadi and his father loading dry crunchy leaves into a rustic wooden wheelbarrow. Giant mound of amber leaves, sunny backyard with trees, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Kotak Kayu Berselot Angin",
                    "titleEn": "The Slatted Wooden Compost Box",
                    "textId": "Di bawah pohon pisang berdiri kotak kayu berpapan renggang yang disebut Ayah sebagai 'Dapur Ajaib Bumi'. Di dalam kotak inilah semua daun kering akan diolah tanpa perlu dibakar dan menghasilkan asap pedih.",
                    "textEn": "Beneath the banana trees stood a wooden box with slatted sides that Dad called the 'Earth's Magic Kitchen'. Inside this box, all dry leaves would be transformed without burning or creating stinging smoke.",
                    "quote": "Menjaga udara tetap bersih adalah hadiah terindah bagi napas semua makhluk.",
                    "coReading": "Mengapa daun kering lebih baik dibuat kompos daripada dibakar?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A rustic slatted wooden compost bin sitting in the garden corner near banana trees. Hadi peering inside with curiosity, hands resting on the wooden rim. Bead dot eyes, warm earthy tones, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Lapisan Cokelat dan Lapisan Hijau",
                    "titleEn": "Brown Layers and Green Layers",
                    "textId": "Ayah mengajari Hadi membuat lapisan seperti kue lapis. Lapisan pertama adalah daun cokelat kering. Di atasnya, Hadi menaburkan kulit pisang, potongan tangkai bayam sisa dapur, dan sedikit ampas kelapa. Kemudian ditutup lagi dengan daun kering.",
                    "textEn": "Dad taught Hadi to build layers just like a layer cake. The first layer was dry brown leaves. On top, Hadi sprinkled banana peels, leftover spinach stems from the kitchen, and coconut shreds, then covered it with dry leaves again.",
                    "quote": "Keseimbangan dalam alam tercipta dari perpaduan berbagai unsur yang tepat.",
                    "coReading": "Sisa buah dan sayur apa saja yang ada di dapur rumahmu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Hadi scattering kitchen vegetable scraps and fruit peels over a layer of dry leaves inside the compost bin. Dad standing beside him smiling, warm family gardening scene, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Koki-Koki Bawah Tanah",
                    "titleEn": "Chefs of the Underground",
                    "textId": "Hadi menambahkan segenggam tanah gembur dari bawah pohon nangka. Di dalam tanah itu terdapat kawan-kawan pekerja: cacing tanah merah, semut kecil, dan bakteri tak kasat mata. 'Merekalah koki-koki yang akan memasak daun ini menjadi emas,' bisik Ayah.",
                    "textEn": "Hadi added a handful of rich soil from under the jackfruit tree. In that soil lived busy little workers: red earthworms, tiny ants, and invisible friendly microbes. 'They are the chefs who will cook these leaves into gold,' whispered Dad.",
                    "quote": "Pekerja paling setia di bumi sering kali berukuran paling kecil.",
                    "coReading": "Siapakah koki rahasia yang membantu mengolah daun kering?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on textured paper. Hadi holding a handful of dark crumbly soil showing a friendly wriggling pink earthworm. Close-up illustration full of wonder, simple black bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Percikan Air Penghilang Haus",
                    "titleEn": "A Splash to Quench the Thirst",
                    "textId": "Dengan gembor seng kecilnya, Hadi memercikkan air secukupnya ke atas tumpukan kompos. Tanah tidak boleh becek seperti lumpur, tetapi cukup lembap seperti spons basah yang diperas. Udara di dalam kotak mulai terasa hangat dan nyaman bagi para cacing.",
                    "textEn": "With his tin watering can, Hadi sprinkled just enough water over the compost pile. It should not be muddy like a puddle, but damp like a squeezed wet sponge. The air inside the bin grew warm and cozy for the worms.",
                    "quote": "Kecukupan air menghidupkan setiap benih kebaikan di dalam tanah.",
                    "coReading": "Mengapa tanah kompos harus disiram sedikit air?",
                    "imagePrompt": "Wax crayon drawing. Hadi gently showering the compost layers with fine water spray from a yellow watering can. Gentle steam rising slightly from the cozy warm compost pile, bead dot eyes, naive folk-art style, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Kehangatan di Tengah Tumpukan",
                    "titleEn": "Warmth at the Heart of the Pile",
                    "textId": "Dua minggu kemudian, Hadi meletakkan tangannya di dekat permukaan kotak. Terasa hawa hangat yang nyaman mengepul lembut. Daun-daun cokelat yang tadinya kaku mulai rapuh, menciut, dan berubah warna menjadi semakin gelap.",
                    "textEn": "Two weeks later, Hadi placed his hand near the compost surface. A pleasant warm glow radiated softly. The crisp brown leaves were now turning crumbly, shrinking down, and darkening into a rich cocoa hue.",
                    "quote": "Perubahan besar membutuhkan proses hangat yang sabar di dalam keheningan.",
                    "coReading": "Bisakah kamu merasakan kehangatan yang keluar dari kotak kompos?",
                    "imagePrompt": "Handcrafted oil pastel and wax crayon. Hadi resting his open palm above the compost bin feeling the gentle warmth rising with a smile of wonder. Soft amber tones, lush green garden background, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Emas Hitam yang Harum Hutan",
                    "titleEn": "Black Gold Scented Like Forest Rain",
                    "textId": "Setelah dua bulan berlalu, Ayah dan Hadi membuka penutup kotak. Tidak ada lagi daun kering yang kasar. Semuanya telah berubah menjadi butiran tanah hitam pekat yang gembur, beraroma segar seperti tanah sehabis hujan lebat di tengah hutan pinus.",
                    "textEn": "After two months had passed, Dad and Hadi opened the bin cover. No rough dry leaves remained. Everything had transformed into crumbly dark black soil, smelling fresh like the woods after a heavy forest rain.",
                    "quote": "Bumi selalu mengembalikan apa yang kita rawat dalam wujud yang jauh lebih mulia.",
                    "coReading": "Bagaimana aroma tanah kompos yang sudah matang?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Hadi holding up a scoop of rich, dark, crumbly compost soil in both hands, sniffing its fresh forest scent happily. Simple bead dot eyes, 4 limbs, textured paper, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Makanan Lezat untuk Mawar dan Cabai",
                    "titleEn": "Feast for Roses and Peppers",
                    "textId": "Dengan sekop kecilnya, Hadi menyendokkan kompos hitam itu ke pot tanaman mawar Ibu dan bedengan pohon cabai. Tanaman-tanaman itu seolah tersenyum menyerap nutrisi terbaik dari daun-daun yang dulunya gugur terinjak kaki.",
                    "textEn": "With his little trowel, Hadi scooped the black compost around Mother's rose bushes and the pepper garden beds. The plants seemed to smile, drinking in the finest nutrients born from leaves once trampled underfoot.",
                    "quote": "Siklus alam mengajarkan bahwa tidak ada akhir, yang ada hanyalah awal yang baru.",
                    "coReading": "Tanaman apa yang diberi makan kompos hitam oleh Hadi?",
                    "imagePrompt": "Soft wax crayon scribbles and oil pastel. Hadi gently spreading dark compost soil around the base of blooming pink rose bushes and green pepper plants. Sunlight filtering through leaves, bead dot eyes, naive folk art, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Malam Damai Penjaga Bumi",
                    "titleEn": "Peaceful Night for the Earth Keeper",
                    "textId": "Bintang-bintang berkelip terang di langit pedesaan. Di kamarnya yang sejuk, Hadi memeluk gulingnya dengan jemari yang bersih. Ia tahu bahwa di luar sana, cacing-cacing tanah sedang bekerja bahagia, dan esok pagi bumi akan semakin subur berkat tangannya yang teliti.",
                    "textEn": "Stars twinkled brightly in the village sky. In his cool, breezy room, Hadi hugged his bolster pillow with clean hands. He knew that outside in the dark, friendly earthworms were working happily, and tomorrow the earth would grow greener thanks to his caring hands.",
                    "quote": "Tidurlah dengan damai wahai penjaga bumi kecil, dunia berterima kasih padamu.",
                    "coReading": "Selamat tidur anak hebat, mari sayangi bumi setiap hari.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Hadi sleeping soundly in cozy bed under a forest-green blanket with a toy watering can on his bedside table. Starry night visible through the window, crescent moon shining softly. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 71: Keran Air yang Tidak Menetes ---
        {
            "id": "story71",
            "storyNumber": 71,
            "title": "Keran Air yang Tidak Menetes",
            "englishTitle": "The Faucet That Never Drips",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menghemat air bersih & peduli pada kelestarian sumber air",
            "cover": "covers/story71_cover.jpg",
            "synopsis": "Maya mendengar bunyi tetesan air 'Ting, ting, ting' di kamar mandi saat malam sunyi. Bersama Kakek, Maya belajar memutar keran dengan rapat dan mengganti karet penyekat yang aus, menyadari bahwa setiap tetes air bersih adalah permata kehidupan yang sangat berharga.",
            "protagonist": "Maya (Gadis cilik bergaun biru muda)",
            "companion": "Tetes Air Ajaib (Karakter tetesan air tersenyum)",
            "setting": "Kamar Mandi Bersih",
            "pages": [
                {
                    "number": 1,
                    "title": "Bunyi di Tengah Kesunyian",
                    "titleEn": "A Sound in the Midnight Stillness",
                    "textId": "Malam sudah larut dan jarum jam dinding berdetik teratur. Saat Maya berbaring di bawah selimut biru mudanya, telinganya menangkap bunyi berulang yang aneh dari arah lorong kamar mandi: 'Tik... tik... tik...' Suaranya kecil namun terdengar jelas di tengah hening malam.",
                    "textEn": "The night was deep and the wall clock ticked steadily. As Maya lay beneath her light blue quilt, her ears caught a peculiar rhythmic sound from down the bathroom hall: 'Drip... drip... drip...' It was quiet yet clear in the midnight silence.",
                    "quote": "Kepekaan mendengarkan hal kecil menjaga kita dari pemborosan besar.",
                    "coReading": "Pernahkah kamu mendengar suara tetesan keran saat malam hari?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Maya, a sweet young girl in pastel blue pajamas, sitting up in her cozy bed with ears tilted listening attentively. Soft nightlight glow, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Jejak Langkah Menuju Kamar Mandi",
                    "titleEn": "Footsteps to the Bathroom",
                    "textId": "Dengan sandal bulu kelincinya, Maya berjingkat perlahan menelusuri lantai kayu. Ia mendorong pintu kamar mandi yang terbuka sedikit. Di dalam wastafel porselen putih, tampak tetesan air jatuh satu per satu dari ujung keran tembaga yang berkilau di bawah lampu temaram.",
                    "textEn": "In her bunny slippers, Maya tiptoed softly along the wooden floorboards. She gently pushed the half-open bathroom door. Inside the white porcelain sink, droplets of water fell one by one from the shiny brass faucet tip under dim light.",
                    "quote": "Rasa ingin tahu yang baik menuntun kita mencari kebenaran.",
                    "coReading": "Apakah air menetes perlahan atau mengalir deras?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Maya peeking into a tidy rustic bathroom with blue floral tiles and a porcelain washbasin. Close-up of clear water droplets falling from a brass faucet, simple bead dot eyes, naive folk art, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Tetesan Kecil yang Berharga",
                    "titleEn": "Precious Tiny Droplets",
                    "textId": "Maya mencoba memutar tuas keran sekuat tenaganya, tetapi tetesan itu masih lolos satu per satu. 'Tik... tong!' bunyinya memantul di dinding keramik. Maya meletakkan cangkir kumurnya di bawah keran untuk menampung tetesan itu agar tidak terbuang sia-sia ke lubang pembuangan.",
                    "textEn": "Maya tried twisting the faucet handle with all her might, but droplets still slipped through one by one. 'Drip... plink!' chimed against the ceramic basin. Maya placed her rinse cup beneath the faucet to catch every drop so none would be wasted down the drain.",
                    "quote": "Satu tindakan kecil menyelamatkan hal berharga dari kesia-siaan.",
                    "coReading": "Mengapa Maya menaruh cangkir di bawah keran yang bocor?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Maya placing a colorful ceramic cup under the leaking brass faucet to catch the drops. Water ripples inside cup, thoughtful expression with bead dot eyes, textured cream paper, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Cangkir yang Penuh Menjelang Subuh",
                    "titleEn": "A Full Cup Before Dawn",
                    "textId": "Saat terbangun di pagi hari, Maya langsung berlari ke wastafel. Cangkir yang ditaruhnya semalam kini telah penuh meluap hingga membasahi piring sabun. 'Hanya dari tetesan kecil, airnya bisa sebanyak ini!' bisik Maya terkejut.",
                    "textEn": "Waking at dawn, Maya ran straight to the sink. The cup she had placed overnight was now brimming over, splashing the soap dish. 'Just from tiny drips, there is this much water!' Maya gasped in astonishment.",
                    "quote": "Tetesan kecil yang terus-menerus bisa mengumpulkan lautan bila tak dijaga.",
                    "coReading": "Berapa banyak air yang terkumpul dalam cangkir semalaman?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Morning sunlight spilling into bathroom. Maya looking in surprise at the overflowing water cup in the sink. Sparkling clean water, simple bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Kakek dan Kotak Perkakas",
                    "titleEn": "Grandpa and the Toolbox",
                    "textId": "Maya segera menceritakan kebocoran itu pada Kakek. Kakek tersenyum bangga atas ketelitian cucunya. Sambil membawa kotak perkakas besi tuang, Kakek berkata, 'Air bersih adalah berkah bumi dari hulu gunung. Kita tidak boleh membiarkan setetes pun terbuang percuma.'",
                    "textEn": "Maya immediately told Grandpa about the leak. Grandpa smiled with proud appreciation for his granddaughter's keen eyes. Carrying his cast-iron toolbox, Grandpa said, 'Clean water is the earth's mountain blessing. We must never let a single drop slip away in vain.'",
                    "quote": "Menghargai air adalah wujud rasa syukur atas kehidupan itu sendiri.",
                    "coReading": "Dari mana air bersih yang kita gunakan sehari-hari berasal?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Grandpa in spectacles carrying a red metal toolbox, talking warmly to Maya who holds up the cup of saved water. Morning warmth, simple bead dot eyes on both, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Karet Penahan yang Lelah",
                    "titleEn": "The Worn-Out Rubber Washer",
                    "textId": "Kakek mematikan katup utama dan menggunakan kunci pas untuk membuka kepala keran. Di dalamnya, Kakek mengeluarkan sebuah cincin karet hitam kecil yang sudah retak dan menipis. 'Karet penyekat ini sudah lelah bertugas, Maya. Saatnya kita beri pengganti baru.'",
                    "textEn": "Grandpa shut off the main valve and used a wrench to loosen the faucet head. Inside, he lifted out a small black rubber ring that was cracked and worn thin. 'This washer is tired from faithful duty, Maya. It is time for a fresh replacement.'",
                    "quote": "Merawat benda-benda di rumah dengan teliti menghindarkan kerusakan besar.",
                    "coReading": "Benda hitam kecil apakah yang rusak di dalam keran air?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Grandpa showing Maya a small worn black rubber washer next to a shiny new one on the bathroom counter. Wrench and tools laid neatly, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Pemasangan Cincin Karet Baru",
                    "titleEn": "Fitting the Brand-New Ring",
                    "textId": "Maya membantu menyodorkan cincin karet baru yang lentur dan tebal. Kakek memasangnya dengan pas, lalu mengencangkan kembali baut kuningan dengan putaran yang kokoh. 'Selesai! Sekarang mari kita uji keran baru kita,' ajak Kakek bersemangat.",
                    "textEn": "Maya helped hand over the brand-new, flexible rubber ring. Grandpa fitted it snugly in place, then tightened the brass fittings with a firm turn. 'All set! Now let us test our fixed faucet,' Grandpa invited warmly.",
                    "quote": "Bekerja bersama membuat tugas sulit menjadi mudah dan menyenangkan.",
                    "coReading": "Apakah kamu senang membantu kakek atau orang tua memperbaiki barang?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Maya handing a tiny black washer to Grandpa's sturdy hand while he tightens the faucet with a chrome wrench. Focus and harmony, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Keheningan yang Menenangkan",
                    "titleEn": "Comforting Silence",
                    "textId": "Kakek membuka kembali katup air. Maya memutar keran; air mengucur deras dan jernih. Saat Maya menutup tuas keran dengan lembut, aliran langsung terhenti seketika. Tidak ada lagi bunyi 'tik... tik... tik...'. Kamar mandi kembali hening dan kering.",
                    "textEn": "Grandpa opened the main valve once more. Maya turned the tap; water flowed clear and strong. When she gently shut the lever, the stream ceased instantly. No more 'drip... drip... plink...'. The bathroom was quiet and dry once more.",
                    "quote": "Keheningan yang rapi adalah tanda bahwa semuanya bekerja dengan sempurna.",
                    "coReading": "Apakah airnya masih menetes sekarang?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Maya turning off the clean brass faucet, not a single drip falling from the spout. Clean shiny sink, Maya and Grandpa smiling together with bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Menyiram Pohon Melati",
                    "titleEn": "Watering the Jasmine Bush",
                    "textId": "Air tampungan di dalam cangkir semalam tidak dibuang ke saluran pembuangan. Maya membawanya ke halaman depan dan menyiramkannya ke pot bunga melati putih kesayangan Nenek. Daun-daun melati tampak segar dan bunganya mekar menyebarkan aroma wangi.",
                    "textEn": "The cupful of water saved from the leak was not tipped down the drain. Maya carried it to the front yard and poured it tenderly onto Grandma's white jasmine pot. The jasmine leaves gleamed fresh, blooming sweet fragrance into the air.",
                    "quote": "Setiap tetes air yang kita selamatkan menghidupkan keindahan di sekeliling kita.",
                    "coReading": "Ke mana Maya menyiramkan air yang diselamatkan semalam?",
                    "imagePrompt": "Soft oil pastel smudges and wax crayon. Maya pouring water from her ceramic cup onto a potted blooming white jasmine bush on a sunlit veranda. Green leaves glistening, simple black bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Tenang Berselimut Damai",
                    "titleEn": "Restful Sleep Wrapped in Peace",
                    "textId": "Malam itu, kamar tidur Maya kembali diselimuti ketenangan yang sempurna. Tidak ada lagi bunyi tetesan air di lorong. Maya tidur pulas dengan senyum manis di wajahnya, bermimpi tentang sungai-sungai pegunungan yang mengalir jernih menjaga bumi tetap hijau.",
                    "textEn": "That night, Maya's bedroom was wrapped in perfect, restful peace. No more faucet drips echoed down the hall. Maya slept soundly with a sweet smile on her face, dreaming of clear mountain streams keeping the earth lush and green.",
                    "quote": "Tidurlah dengan tenang, dunia aman karena ada anak-anak baik yang peduli.",
                    "coReading": "Selamat malam, pastikan semua keran di rumah sudah tertutup rapat ya.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Maya sleeping serenely in bed tucked under pastel blue blankets with plush rabbit toy beside her. Moonlit room, starry sky outside window, deep peaceful nighttime tones, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 72: Ulat Rakus Jadi Sayap Pelangi ---
        {
            "id": "story72",
            "storyNumber": 72,
            "title": "Ulat Rakus Jadi Sayap Pelangi",
            "englishTitle": "Greedy Caterpillar Becomes Rainbow Wings",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Metamorfosis, kesabaran dalam bertumbuh, & keindahan perubahan",
            "cover": "covers/story72_cover.jpg",
            "synopsis": "Rian melihat ulat hijau gemuk yang rakus melahap daun pohon jeruk nipis di teras. Awalnya Rian ingin mengusirnya, tetapi Ibu mengajak Rian mengamati kepompong sutra emas yang hening, hingga lahirlah kupu-kupu bersayap pelangi yang memukau.",
            "protagonist": "Rian (Anak laki-laki berkaca pembesar)",
            "companion": "Kupu-kupu Emas (Kupu-kupu baru keluar dari kepompong)",
            "setting": "Pohon Jeruk Berdaun Lebat",
            "pages": [
                {
                    "number": 1,
                    "title": "Daun Jeruk yang Berlubang",
                    "titleEn": "Holes in the Lime Leaves",
                    "textId": "Di teras rumah, pohon jeruk nipis di dalam pot tanah liat tampak memiliki banyak daun berlubang-lubang gerigi. Rian, anak laki-laki yang gemar membawa kaca pembesar saku, berjongkok memeriksa tangkai dahan. Di balik sehelai daun hijau tua, bertengger seekor ulat gemuk bergaris hijau terang.",
                    "textEn": "On the porch, a potted lime tree in a clay planter had leaves dotted with jagged bite marks. Rian, a curious boy who loved carrying a pocket magnifying glass, knelt to inspect the branches. Behind a dark green leaf sat a plump, bright green striped caterpillar.",
                    "quote": "Rasa ingin tahu yang teliti membuka rahasia kecil alam semesta.",
                    "coReading": "Pernahkah kamu melihat ulat hijau di pohon jeruk atau jambu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Rian, a cute boy with a pocket magnifying glass looking closely at a lime plant. Plump bright green caterpillar sitting on a partially eaten leaf, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Nafsu Makan yang Luar Biasa",
                    "titleEn": "An Enormous Appetite",
                    "textId": "'Kres, kres, kres!' Bunyi kunyahan ulat itu terdengar cepat. Dalam sekejap, separuh helai daun jeruk yang harum telah habis ditelannya. Tubuh ulat itu begitu gemuk dan melar seperti bantal jarum. Rian cemberut, 'Ulat ini rakus sekali, Bu! Daun pohon jeruk kita bisa habis!'",
                    "textEn": "'Munch, crunch, nibble!' sounded the caterpillar's speedy chewing. In an instant, half of the fragrant lime leaf vanished into its tummy. The caterpillar was so plump, like a soft pin cushion. Rian frowned, 'This caterpillar is so greedy, Mom! Our lime tree will have no leaves left!'",
                    "quote": "Sesuatu yang terlihat rakus terkadang sedang menabung tenaga untuk hal besar.",
                    "coReading": "Mengapa ulat makan daun begitu banyak?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up through magnifying glass circle: plump cute caterpillar with bead dot eyes happily munching an emerald green citrus leaf. Rian watching with wide curious eyes, naive folk art, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Penjelasan Rahasia Ibu",
                    "titleEn": "Mother's Secret Explanation",
                    "textId": "Ibu tersenyum sambil mengelus pipi Rian. 'Jangan dimusuhi, Rian. Ulat hijau ini sedang mengumpulkan sari-sari makanan untuk tidur panjangnya. Tanpa makanan yang cukup, ia tidak akan memiliki tenaga untuk menciptakan keajaiban terindahnya.'",
                    "textEn": "Mother smiled, gently stroking Rian's cheek. 'Do not be cross, Rian. This green caterpillar is gathering nourishment for a long, deep sleep. Without enough food, it will never have the strength to create its greatest miracle.'",
                    "quote": "Pandangan yang bijak selalu melihat potensi di balik kekurangan sesaat.",
                    "coReading": "Apa keajaiban yang sedang dipersiapkan oleh ulat hijau?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Mother kneeling beside Rian by the potted citrus tree, pointing tenderly at the green caterpillar. Warm mother-son bonding, soft sunlight, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Gantungan Sutra di Balik Ranting",
                    "titleEn": "The Silk Hanger Beneath the Twig",
                    "textId": "Keesokan harinya, ulat itu berhenti makan. Ia merayap perlahan ke bagian bawah ranting kayu yang terlindung. Dengan mulutnya, ia memintal seuntai benang sutra putih yang sangat kuat, lalu menggantungkan tubuhnya terbalik membentuk huruf J yang anggun.",
                    "textEn": "The next day, the caterpillar stopped eating. It crawled slowly to the sheltered underside of a wooden twig. From its mouth, it spun a tough strand of white silk, hanging upside down in an elegant J shape.",
                    "quote": "Keheningan adalah ruang tempat jiwa bersiap untuk berubah.",
                    "coReading": "Bisakah kamu membuat bentuk huruf J dengan jari telunjukmu?",
                    "imagePrompt": "Soft oil pastel smudges on cream paper. Cute green caterpillar hanging upside down in a curled J-shape from a citrus branch anchored by a fine shiny silk thread. Dappled morning light, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Kepompong Giok yang Berkilau",
                    "titleEn": "The Glistening Jade Chrysalis",
                    "textId": "Hanya dalam beberapa jam, kulit hijau ulat terkelupas rapi. Kini tergantung sebuah kepompong halus berwarna hijau giok berhiaskan bintik-bintik emas berkilauan seperti permata putri raja. Kepompong itu tergantung diam tanpa suara di tengah desau angin teras.",
                    "textEn": "In just a few hours, the caterpillar's skin slipped away. Hanging there now was a smooth jade-green chrysalis speckled with shiny golden dots like royal jewels. The chrysalis hung quietly in the gentle porch breeze.",
                    "quote": "Keindahan sejati sering kali bersembunyi dalam kesunyian yang tenang.",
                    "coReading": "Warna apa yang tampak pada kepompong itu? Hijau dan apa lagi?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Detailed chrysalis resembling shiny green jade with tiny metallic gold speckles hanging beneath a citrus leaf. Rian observing with awestruck eyes, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Tujuh Hari Menunggu dalam Doa",
                    "titleEn": "Seven Days of Patient Waiting",
                    "textId": "Tujuh hari berlalu. Rian selalu memeriksa kepompong setiap pulang bermain, memastikan tidak ada semut atau burung yang mengganggu tempat tidur gantung itu. Kepompong perlahan berubah warna dari hijau giok menjadi cokelat keemasan transparan.",
                    "textEn": "Seven days passed. Rian checked on the chrysalis every day after playing, making sure no ants or birds disturbed the hanging cradle. Slowly, the chrysalis transformed from jade green to a transparent golden brown.",
                    "quote": "Menjaga dengan sabar adalah tanda kasih sayang yang mendalam.",
                    "coReading": "Apakah kamu bisa sabar menunggu kepompong menetas selama seminggu?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Rian standing on tiptoe beside the potted tree checking the chrysalis which is now turning translucent amber showing faint wing patterns inside. Morning glow, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Merekahnya Cangkang Sutra",
                    "titleEn": "The Silk Shell Cracks Open",
                    "textId": "Pagi hari di hari kesepuluh, dinding kepompong retak pelan. Muncullah kepala mungil dengan sepasang antena lentur, diikuti oleh tubuh beludru hitam dan sayap yang masih basah terlipat rapat seperti sapu tangan kusut.",
                    "textEn": "On the morning of the tenth day, the chrysalis wall gently split. Out poked a tiny head with curly antennae, followed by a velvety black body and wings still damp and tightly folded like a crumpled handkerchief.",
                    "quote": "Lahirnya kehidupan baru selalu diiringi oleh perjuangan yang mengagumkan.",
                    "coReading": "Mengapa sayap kupu-kupu yang baru keluar masih basah dan terlipat?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A newly emerged butterfly clinging to its empty transparent shell, wings still crumpled and wet. Rian watching with breathless wonder, morning dew sparkling, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Sayap Pelangi Terbentang Sempurna",
                    "titleEn": "Rainbow Wings Unfurl in Glory",
                    "textId": "Kupu-kupu itu memompa cairan ke urat-urat sayapnya di bawah kehangatan sinar matahari pagi. Perlahan tapi pasti, sayapnya membentang lebar! Pola hitam beludru dihiasi corak kuning keemasan, bintik biru safir, dan semburat merah marun yang megah bagai lukisan pelangi.",
                    "textEn": "The butterfly pumped fluid through its wing veins beneath the warm morning sunlight. Slowly but surely, its wings unfurled wide! Velvety black patterned with golden yellows, sapphire blue spots, and ruby red splashes, magnificent like a rainbow painting.",
                    "quote": "Kesabaran dalam kegelapan melahirkan kemegahan yang tak terduga.",
                    "coReading": "Sebutkan warna-warna indah yang ada di sayap kupu-kupu itu!",
                    "imagePrompt": "Vibrant wax crayon and oil pastel smudges on heavy cream paper. A gorgeous swallowtail butterfly with open wings showing velvety black, golden yellow, and sparkling blue spots drying its wings on a green twig. Rian and mother smiling joyfully, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Terbang Pertama Menyapa Angin",
                    "titleEn": "First Flight Greeting the Breeze",
                    "textId": "Dengan sekali kepakan lembut, kupu-kupu itu melayang anggun ke udara bebas. Ia terbang mengitari kepala Rian dua kali seolah berpamitan, lalu meluncur ringan menuju bunga-bunga kembang sepatu di seberang halaman. Rian melambaikan tangannya dengan sorak bahagia.",
                    "textEn": "With one gentle flap, the butterfly soared gracefully into the open air. It circled Rian's head twice as if saying goodbye, then floated lightly toward the red hibiscus blooms across the yard. Rian waved his hand cheering with delight.",
                    "quote": "Melepaskan kebebasan kepada yang kita sayangi adalah puncak cinta sejati.",
                    "coReading": "Apakah kamu senang melihat kupu-kupu terbang bebas di taman?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. The magnificent butterfly fluttering gracefully above Rian's head in a sunny garden filled with blooming red hibiscus. Rian waving happily with both hands, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Manis Bersayap Pelangi",
                    "titleEn": "Sweet Dreams on Rainbow Wings",
                    "textId": "Malam hari kembali membungkus bumi dengan keheningan yang sejuk. Rian tidur lelap di bawah selimut hangatnya. Di dalam mimpinya, ia terbang melayang bersama sahabat kupu-kupunya, melintasi padang bunga berhias cahaya bintang.",
                    "textEn": "Night enveloped the earth in cool, comforting tranquility once again. Rian slept deeply beneath his cozy blanket. In his dreams, he soared alongside his butterfly friend, floating across flower fields bathed in starlight.",
                    "quote": "Tidurlah dengan damai, esok harimu akan mekar seindah sayap pelangi.",
                    "coReading": "Mari pejamkan mata dan bayangkan kamu terbang bebas di langit malam.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Rian sleeping peacefully in his bedroom with a gentle smile on his face. Dream bubbles above his head showing gentle silhouettes of colorful butterflies dancing under a starry sky and crescent moon. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
