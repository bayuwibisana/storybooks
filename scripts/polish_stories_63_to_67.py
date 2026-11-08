# scripts/polish_stories_63_to_67.py
import json

def get_stories_63_to_67():
    stories = [
        # --- STORY 63: Petak Umpet yang Menyenangkan Semua ---
        {
            "id": "story63",
            "storyNumber": 63,
            "title": "Petak Umpet yang Menyenangkan Semua",
            "englishTitle": "Hide and Seek That Pleased Everyone",
            "category": "social",
            "categoryLabel": "🤝 Pertemanan & Kebaikan Hati",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Inklusivitas & kepekaan bermain bersama",
            "cover": "covers/story63_cover.jpg",
            "synopsis": "Gita dan kawan-kawannya bermain petak umpet di halaman berpagar kayu saat senja. Ketika adik kecil yang paling lambat merasa sedih karena selalu tertangkap pertama, Gita mengajak semua mengubah aturan agar setiap anak merasa dirangkul dan bahagia.",
            "protagonist": "Gita (Gadis cilik bertopi rajut)",
            "companion": "Kawan-kawan (Kelompok anak bermain petak umpet)",
            "setting": "Halaman Berpagar Kayu",
            "pages": [
                {
                    "number": 1,
                    "title": "Hitungan di Pagar Kayu",
                    "titleEn": "Counting on the Wooden Fence",
                    "textId": "Matahari sore merona jingga di atas halaman berpagar kayu yang harum rumput pangkas. Gita, gadis cilik bertopi rajut jingga, menempelkan keningnya di tiang pagar sambil memejamkan mata rapat-rapat. 'Satu... dua... tiga...!' suaranya riang membelah angin sore, memberi waktu bagi teman-temannya mencari persembunyian terbaik.",
                    "textEn": "The evening sun blushed orange above the wooden-fenced yard fragrant with fresh-cut grass. Gita, a little girl in an orange knitted hat, pressed her forehead against the fence post, closing her eyes tight. 'One... two... three...!' her cheerful voice echoed through the breeze, giving her friends time to hide.",
                    "quote": "Bermain bersama adalah merajut kegembiraan dalam setiap tawa.",
                    "coReading": "Di mana tempat sembunyi favoritmu saat bermain petak umpet di rumah?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on textured cream watercolor paper. Gita, a cute young girl in an orange knit beanie and cozy apron dungarees, standing with her face against a weathered rustic wooden fence counting with closed bead dot eyes. Yard surrounded by blooming wildflowers and soft golden afternoon sunlight. Exactly 4 limbs, no text, 4:3 horizontal landscape."
                },
                {
                    "number": 2,
                    "title": "Langkah-Langkah Mengendap",
                    "titleEn": "Tiptoeing Footsteps",
                    "textId": "Di balik semak hydrangea ungu, Bimo menahan napas sambil merapatkan lututnya. Di dekat tong penyiram air, Danu menyusup ke balik tumpukan jerami kering. Namun Dodo si beruang kecil bertubuh tambun bingung mencari celah; kakinya yang pendek tersandung akar dan napasnya terengah-engah.",
                    "textEn": "Behind the purple hydrangea bushes, Bimo held his breath and hugged his knees. Near the watering barrel, Danu tucked himself behind dry haystacks. But little chubby bear cub Dodo was puzzled, his short legs tripped over gentle roots as he panted softly.",
                    "quote": "Terkadang langkah kecil membutuhkan tempat persembunyian yang ramah.",
                    "coReading": "Apakah Dodo terlihat panik atau bingung? Mengapa ya?",
                    "imagePrompt": "Handcrafted wax crayon scribbles on heavy textured paper. Dodo, a cute chubby brown bear cub wearing green overalls with simple black bead dot eyes, clumsily stepping near flowering hydrangea bushes trying to hide. Two legs on ground, two arms holding overalls straps. Soft pastel shadows, naive folk-art style, text-free, 4:3 horizontal."
                },
                {
                    "number": 3,
                    "title": "Ketukan Pertama",
                    "titleEn": "The First Tap",
                    "textId": "'Sepuluh! Siap atau belum, aku datang!' seru Gita sambil berbalik. Baru tiga langkah berjalan, Gita langsung melihat telinga berbulu Dodo menyembul di balik pot tanah liat kecil. 'Kena kamu, Dodo!' seru Gita sambil tersenyum. Dodo menunduk lesu, telinganya terkulai.",
                    "textEn": "'Ten! Ready or not, here I come!' cheered Gita, turning around. Just three steps forward, she spotted Dodo's furry ears peeking behind a small clay flowerpot. 'Caught you, Dodo!' Gita smiled gently. Dodo lowered his head sadly, ears drooping.",
                    "quote": "Kalah atau menang bukan inti dari indahnya sebuah permainan.",
                    "coReading": "Bagaimana perasaanmu jika selalu jadi yang pertama tertangkap?",
                    "imagePrompt": "Warm oil pastel strokes on textured cream paper. Gita pointing cheerfully towards a clay flowerpot where Dodo the bear cub is sitting with drooping ears and round bead eyes looking disheartened. Blooming flowerpots, cozy backyard setting, wax crayon textures, completely text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 4,
                    "title": "Air Mata yang Menggenang",
                    "titleEn": "Well of Tiny Tears",
                    "textId": "Ini sudah putaran ketiga, dan Dodo selalu menjadi yang pertama tertangkap. 'Aku tidak bisa lari cepat seperti kalian... badanku terlalu besar untuk semak-semak ini,' bisik Dodo dengan mata berair. Teman-teman lain mulai berkumpul mengelilingi Dodo dengan tatapan iba.",
                    "textEn": "This was the third round, and Dodo was always caught first. 'I cannot run as fast as you... my body is too big for these tiny bushes,' whispered Dodo with glossy teary eyes. The other friends gathered around Dodo with tender concern.",
                    "quote": "Mendengarkan keluh sahabat adalah tanda cinta yang sejati.",
                    "coReading": "Apa yang bisa teman-teman lakukan untuk menghibur Dodo?",
                    "imagePrompt": "Handcrafted wax crayon drawing. Dodo the little bear cub wiping a tiny tear with his paw, sitting on a wooden log. Gita and child companions standing around him offering comforting gestures. Soft warm evening hues, textured cream paper, bead dot eyes, exactly 4 limbs, no letters, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Gagasan Gita",
                    "titleEn": "Gita's Bright Idea",
                    "textId": "Gita berjongkok di hadapan Dodo dan memegang kedua tangannya yang lembut. 'Permainan ini keliru jika ada yang merasa sedih, Dodo. Bagaimana kalau kita ubah aturannya? Kita mainkan Petak Umpet Berpasangan! Yang bertubuh gesit bergandengan dengan yang butuh bantuan.'",
                    "textEn": "Gita knelt before Dodo, taking his soft paws in hers. 'A game is not right if someone feels sad, Dodo. How about we change the rules? Let us play Partner Hide-and-Seek! Those who run swiftly pair up with those who need a helping hand.'",
                    "quote": "Kebaikan hati selalu menemukan cara agar semua orang tersenyum.",
                    "coReading": "Apakah usul Gita adil dan menyenangkan?",
                    "imagePrompt": "Crayon and soft oil pastel smudges. Gita kneeling softly, holding paws with Dodo the bear cub on the grassy lawn. Gita smiling warmly, wearing a knit hat, simple black bead dot eyes on both characters. Golden sunset glow, naive children book art, 4:3 landscape, text-free."
                },
                {
                    "number": 6,
                    "title": "Kawan Berpasangan",
                    "titleEn": "Paired Up Together",
                    "textId": "Mata Dodo berbinar seketika. Gita menggandeng Dodo sebagai rekan persembunyian, sementara Bimo berpasangan dengan Danu. Kini giliran Tika yang menjaga tiang pagar. 'Satu... dua... tiga...!' Gita dan Dodo berjingkat bersama menuju lumbung kayu tua di sudut halaman.",
                    "textEn": "Dodo's eyes lit up with joy. Gita took Dodo's paw as her hiding partner, while Bimo paired with Danu. Now it was Tika's turn to guard the fence post. 'One... two... three...!' Gita and Dodo tiptoed together toward the cozy old wooden barn at the corner.",
                    "quote": "Bersama seorang teman, setiap langkah terasa lebih ringan dan berani.",
                    "coReading": "Siapa yang paling kamu sukai untuk diajak berpasangan?",
                    "imagePrompt": "Soft wax crayon scribbles on textured paper. Gita holding hands with Dodo the bear cub as they tiptoe together towards an open wooden barn doorway. Golden evening light filtering between wooden slats. Cute, round bead eyes, 4 limbs constraint, completely text-free, 4:3 horizontal."
                },
                {
                    "number": 7,
                    "title": "Rahasia di Balik Jerami",
                    "titleEn": "Secret Behind the Golden Straw",
                    "textId": "Di dalam lumbung, Gita membantu Dodo menyamarkan diri di balik tumpukan jerami keemasan yang wangi. Gita menata jerami lembut di atas punggung Dodo sehingga menyerupai bukit jerami yang tidur lelap. Dodo terkikik geli menahan napas saat Tika melangkah masuk.",
                    "textEn": "Inside the barn, Gita helped Dodo tuck safely behind piles of fragrant golden straw. She gently arranged golden straw over Dodo's back until he looked like a peacefully sleeping haystack. Dodo giggled softly, holding his breath as Tika stepped inside.",
                    "quote": "Kerja sama manis melahirkan keajaiban yang menyenangkan.",
                    "coReading": "Bisa kamu melihat hidung Dodo di antara jerami?",
                    "imagePrompt": "Warm oil pastel illustration on heavy cream paper. Dodo the chubby bear nestled cozily under golden straw, only his round black nose and bead eyes peeking playfully. Gita sitting nearby pressing a finger to her lips in a quiet shh gesture. Cozy barn lanterns glowing softly, no text, 4:3 landscape."
                },
                {
                    "number": 8,
                    "title": "Tawa yang Membebas",
                    "titleEn": "Laughter Set Free",
                    "textId": "Tika celingukan memeriksa tong kayu dan rak perkakas. 'Di mana ya mereka?' gumam Tika bingung. Tiba-tiba jerami bergerak perlahan dan Dodo tak sanggup menahan geli. 'Haaatsyi!' bersin Dodo membuat jerami berhamburan. Semua anak yang bersembunyi meledak dalam tawa bahagia.",
                    "textEn": "Tika looked around, checking wooden barrels and tool racks. 'Where could they be?' Tika murmured. Suddenly the straw wiggled and Dodo could no longer hold in a tickle. 'Achoo!' Dodo's sneeze sent straw dancing in the air. All the children burst into happy laughter.",
                    "quote": "Tawa bersama adalah musik termerdu di penghujung senja.",
                    "coReading": "Pernahkah kamu bersin saat sedang bersembunyi?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel smudges. Golden straw floating through the air with soft motion lines, Dodo the bear cub sneezing with smiling eyes, Tika and Gita clapping and laughing delightfully. Cozy golden rays in rustic wooden barn, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Kemenangan Untuk Semua",
                    "titleEn": "A Victory for Everyone",
                    "textId": "Tidak ada yang merasa kalah sore itu. Dodo melompat kegirangan karena berhasil bersembunyi paling lama dibanding putaran sebelumnya. 'Ini petak umpet terbaik yang pernah kuikuti!' seru Dodo sambil memeluk Gita dengan penuh rasa terima kasih.",
                    "textEn": "Nobody felt defeated that evening. Dodo bounced with joy because he had stayed hidden longer than ever before. 'This is the best hide-and-seek ever!' cheered Dodo, wrapping Gita in a grateful, tender hug.",
                    "quote": "Kemenangan terindah adalah ketika tidak ada kawan yang tertinggal.",
                    "coReading": "Mengapa Dodo merasa sangat bahagia sekarang?",
                    "imagePrompt": "Wax crayon on textured watercolor paper. Dodo the bear cub and Gita hugging warmly on the grassy lawn. The other children cheering happily around them. Sunset sky turning lilac and peach, simple bead eyes, 4 limbs per character, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 10,
                    "title": "Bintang Senja dan Janji Esok",
                    "titleEn": "Dusk Star and Tomorrow's Promise",
                    "textId": "Lampu teras rumah dinyalakan satu per satu, mengundang anak-anak pulang untuk mandi dan makan malam. Sambil melambaikan tangan di depan pagar, Dodo berseru, 'Besok kita main lagi ya!' Gita tersenyum mengangguk, bersiap tidur lelap di bawah selimut hangat dengan hati yang damai.",
                    "textEn": "Porch lanterns flickered on one by one, calling the children home for cozy baths and dinner. Waving his paw by the wooden fence, Dodo called out, 'Let's play again tomorrow!' Gita smiled and nodded, ready to sleep soundly beneath her warm blanket with a peaceful heart.",
                    "quote": "Tidurlah dengan hati yang hangat, esok hari penuh teman yang menyayangi.",
                    "coReading": "Mari pejamkan mata dan bayangkan pelukan teman-temanmu sebelum tidur.",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Cozy evening dusk with first twinkling evening star. Warm glowing porch lanterns on cottage porch. Gita in pajamas looking out her bedroom window, waving goodbye to her friends walking home. Peaceful, sleepy atmosphere, simple bead eyes, completely text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 64: Pelukan Landak dan Kucing Bulu ---
        {
            "id": "story64",
            "storyNumber": 64,
            "title": "Pelukan Landak dan Kucing Bulu",
            "englishTitle": "The Hug of the Hedgehog and Fluffy Kitten",
            "category": "social",
            "categoryLabel": "🤝 Pertemanan & Kebaikan Hati",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menyayangi tanpa menyakiti & saling menghargai perbedaan",
            "cover": "covers/story64_cover.jpg",
            "synopsis": "Bram si landak kecil sangat ingin memeluk sahabatnya, Kuki si kucing anggora berbulu seputih salju. Namun duri-duri tajam Bram selalu membuatnya takut melukai. Dengan kesabaran dan sehelai syal rajut lembut, mereka menemukan cara manis untuk berpelukan hangat.",
            "protagonist": "Bram (Landak berduri halus)",
            "companion": "Kuki (Kucing anggora berbulu lebat)",
            "setting": "Teras Rumah Desa",
            "pages": [
                {
                    "number": 1,
                    "title": "Dua Sahabat di Teras Senja",
                    "titleEn": "Two Friends on the Porch",
                    "textId": "Di teras rumah berpapan kayu jati, Bram si landak mungil duduk berdampingan dengan Kuki, kucing anggora berbulu putih selembut gumpalan awan. Setiap sore mereka menikmati teh madu hangat sambil mendengarkan desir angin semilir yang meniup dedaunan mangga.",
                    "textEn": "On the teakwood porch of a village house, little hedgehog Bram sat beside Kuki, an Angora kitten with fur as soft as a cloud puff. Every afternoon they enjoyed warm honey tea while listening to the gentle breeze rustling through mango leaves.",
                    "quote": "Persahabatan sejati tidak memandang rupa maupun perbedaan.",
                    "coReading": "Apakah kamu punya sahabat yang berbeda kesukaan atau sifatnya denganmu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy textured cream watercolor paper. Bram the cute anthropomorphic hedgehog wearing a knitted vest and Kuki the fluffy white kitten in a lavender collar sitting side by side on a rustic wooden porch. Two ceramic teacups between them. Warm sunset glow, black bead dot eyes, exactly 4 limbs each, text-free, 4:3 landscape."
                },
                {
                    "number": 2,
                    "title": "Keinginan Sebuah Pelukan",
                    "titleEn": "A Wish for a Warm Hug",
                    "textId": "Kuki menguap manis dan merapatkan tubuhnya. 'Bram, udara mulai dingin. Bolehkah aku memelukmu?' tanya Kuki dengan mata bulat jernih. Bram tersentak dan mundur selangkah, menatap duri-duri cokelat runcing yang menyelimuti seluruh punggungnya.",
                    "textEn": "Kuki yawned gently and snuggled closer. 'Bram, the air is growing chilly. May I give you a hug?' asked Kuki with bright, round eyes. Bram flinched and stepped back, looking at the sharp brown quills covering his back.",
                    "quote": "Terkadang kita ragu mendekat karena takut melukai yang kita sayang.",
                    "coReading": "Mengapa Bram mundur saat Kuki ingin memeluknya?",
                    "imagePrompt": "Wax crayon scribbles on cream paper. Bram the hedgehog taking a cautious step back with a worried expression, while Kuki the white fluffy cat tilts her head with innocent curiosity. Soft waxy textures, simple bead dot eyes, naive folk art, text-free, 4:3 horizontal."
                },
                {
                    "number": 3,
                    "title": "Takut Menusuk Sahabat",
                    "titleEn": "Fear of Pricking a Friend",
                    "textId": "'Jangan, Kuki,' lirih Bram dengan nada sedih. 'Punggungku penuh duri tajam. Jika kita berpelukan, duri ini pasti menusuk kulitmu yang lembut. Aku tidak ingin melihatmu kesakitan karena kelalaianku.' Duri di punggung Bram bahkan meremang cemas.",
                    "textEn": "'No, Kuki,' Bram said softly with a sad tone. 'My back is covered in sharp quills. If we hug, they might prick your gentle skin. I never want to see you hurt because of me.' The quills on Bram's back trembled with worry.",
                    "quote": "Menjaga orang lain agar tidak terluka adalah bentuk kasih sayang terdalam.",
                    "coReading": "Bagaimana cara Bram menunjukkan rasa sayangnya pada Kuki?",
                    "imagePrompt": "Handcrafted oil pastel and wax crayon. Bram looking down at his own quills with a tender, concerned expression. Kuki touching Bram's little foot gently with her soft paw. Cozy ambient light, heavy textured paper, bead dot eyes, 4 limbs constraint, completely text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Kuki yang Mengerti",
                    "titleEn": "Kuki Understands",
                    "textId": "Kuki tersenyum lembut dan mendengkur pelan. 'Durimu adalah anugerah untuk melindungimu dari bahaya, Bram. Durimu bukan untuk ditakuti, tetapi untuk dipahami. Pasti ada cara agar kita bisa saling berbagi kehangatan tanpa ada yang terluka.'",
                    "textEn": "Kuki smiled gently and purred softly. 'Your quills are a gift to protect you from danger, Bram. They are not meant to be feared, but understood. Surely there is a way we can share warmth without anyone hurting.'",
                    "quote": "Sahabat sejati melihat keindahan di balik hal yang orang lain takuti.",
                    "coReading": "Kata-kata manis apa yang Kuki sampaikan untuk menghibur Bram?",
                    "imagePrompt": "Warm wax crayon drawing. Kuki the white cat smiling lovingly at Bram the hedgehog on the wooden porch floor. A small lantern glowing with golden light between them. Soft finger-blended pastel colors, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 5,
                    "title": "Keranjang Benang Nenek",
                    "titleEn": "Grandma's Yarn Basket",
                    "textId": "Kuki melompat ringan ke sudut teras dan menarik keranjang anyaman milik Nenek. Di dalamnya tersimpan gulungan benang wol tebal berwarna jingga cerah dan sehelai syal rajut wol yang sangat tebal dan empuk seperti bantal guling.",
                    "textEn": "Kuki hopped lightly to the corner of the porch and pulled over Grandma's woven basket. Inside lay thick skeins of bright orange wool yarn and a thick, puffy knitted scarf as soft as a bolster pillow.",
                    "quote": "Solusi terbaik sering kali ada di sekitar kita bila dicari bersama.",
                    "coReading": "Kira-kira apa yang akan dilakukan Kuki dengan syal wol itu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on cream watercolor paper. Kuki the white fluffy cat carrying a thick, knitted orange woolen scarf in her two front paws. An open sewing basket overflowing with colorful yarn balls beside her. Naive folk art, bead dot eyes, 4:3 horizontal, no text."
                },
                {
                    "number": 6,
                    "title": "Baju Pelindung Ajaib",
                    "titleEn": "The Magical Soft Armor",
                    "textId": "'Lihat ini, Bram!' seru Kuki riang. Dengan cermat, Kuki melingkarkan syal rajut tebal itu ke sekeliling punggung Bram. Syal itu membungkus duri-duri tajam Bram menjadi gumpalan empuk berwarna jingga yang hangat. Bram tampak seperti bola wol kecil yang menggemaskan.",
                    "textEn": "'Look at this, Bram!' Kuki cheered. Carefully, Kuki wrapped the thick knitted scarf all around Bram's prickly back. The scarf tucked the sharp quills into a warm, puffy orange bundle. Bram looked like an adorable little ball of cozy wool.",
                    "quote": "Kreativitas dan cinta mampu merangkul setiap keterbatasan.",
                    "coReading": "Apakah Bram terlihat lucu dengan syal tebalnya?",
                    "imagePrompt": "Soft oil pastel smudges and crayon scribbles. Kuki wrapping the thick, fluffy orange knitted scarf gently around Bram the hedgehog's back. Bram standing patiently on two feet, smiling with simple bead dot eyes. Cute, cozy atmosphere, text-free, 4:3 horizontal."
                },
                {
                    "number": 7,
                    "title": "Pelukan Pertama yang Hangat",
                    "titleEn": "The Very First Warm Hug",
                    "textId": "Bram meraba punggungnya; kini duri-durinya tertutup bantalan wol yang lembut. Kuki membuka kedua lengannya lebar-lebar. Bram melangkah maju dan melingkarkan pelukannya erat-erat. Tidak ada rasa sakit, tidak ada tusukan—hanya kehangatan tulus yang mengalir di antara dada mereka.",
                    "textEn": "Bram felt his back; his sharp quills were now cushioned by soft wool. Kuki opened her arms wide. Bram stepped forward and wrapped his arms around her tightly. No pain, no pricks—only pure warmth flowing between their beating hearts.",
                    "quote": "Pelukan tulus menghapus segala jarak dan kecemasan.",
                    "coReading": "Coba peluk bantalmu seerat pelukan Bram dan Kuki!",
                    "imagePrompt": "Handcrafted wax crayon art on textured cream paper. Bram the hedgehog in his orange wrapped scarf hugging Kuki the fluffy white cat tightly and happily. Warm golden glow enveloping them, cheeks pressed together, blissful expressions with simple bead eyes, completely text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Dengkuran di Telinga",
                    "titleEn": "Purrs by the Ear",
                    "textId": "Kuki mendengkur keras penuh kebahagiaan, suaranya seperti mesin pemintal benang yang menenangkan. 'Rasanya seperti memeluk awan beraroma madu,' bisik Bram sambil menyandarkan pipinya ke bulu putih Kuki. Air mata haru Bram membasahi wol oranye.",
                    "textEn": "Kuki purred loudly with sheer happiness, humming like a comforting spinning wheel. 'It feels like hugging a honey-scented cloud,' Bram whispered, resting his cheek against Kuki's white fur. Bram's tears of joy dampened the orange wool.",
                    "quote": "Kebahagiaan sederhana terasa begitu megah saat dirasakan bersama.",
                    "coReading": "Pernahkah kamu mendengar dengkuran kucing saat mereka merasa nyaman?",
                    "imagePrompt": "Soft wax crayon scribbles. Close-up of Bram the hedgehog and Kuki the white cat resting their heads together, smiling peacefully with closed bead eyes. Cozy porch setting with night falling, lantern glowing softly in background. Naive storybook illustration, no text, 4:3 landscape."
                },
                {
                    "number": 9,
                    "title": "Syal Persahabatan",
                    "titleEn": "The Scarf of Friendship",
                    "textId": "Mulai malam itu, syal wol jingga digantung di tiang teras dengan rapi. Setiap kali mereka ingin berpelukan atau kedinginan, Bram tinggal mengenakan syal itu. 'Ini bukan sekadar syal,' kata Bram, 'ini jembatan kasih sayang kita.'",
                    "textEn": "From that night on, the orange woolen scarf hung neatly on the porch peg. Whenever they wished to hug or felt cold, Bram would simply slip into it. 'This is not just a scarf,' said Bram, 'it is the bridge of our love.'",
                    "quote": "Bila ada kemauan untuk saling menjaga, selalu ada jalan kebersamaan.",
                    "coReading": "Benda apa yang paling mengingatkanmu pada kasih sayang sahabat?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Bram and Kuki sitting together holding hands on a woven porch rug, looking up fondly at the orange woolen scarf hanging on a wooden wall peg. Golden lantern light, cozy bedtime mood, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Manis di Sudut Teras",
                    "titleEn": "Sweet Dreams on the Cozy Porch",
                    "textId": "Bulan sabit bersinar perak di langit pedesaan. Kuki melingkar tidur di atas karpet perca, sementara Bram bersandar di sampingnya dengan syal wol yang hangat. Keduanya tertidur pulas, bermimpi tentang pelukan-pelukan manis di hari esok yang cerah.",
                    "textEn": "The crescent moon shone silver in the village sky. Kuki curled up sleeping on a patchwork rug, while Bram leaned beside her in his warm woolen scarf. Both fell into deep, sweet slumber, dreaming of gentle hugs in tomorrow's bright sunrise.",
                    "quote": "Tidurlah dengan damai, kasih sayang selalu melindungimu dalam lelap.",
                    "coReading": "Selamat tidur anak baik, biarkan hatimu diselimuti pelukan hangat malam ini.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream paper. Bram the hedgehog nestled cozily beside Kuki the fluffy sleeping white cat on a cozy patchwork quilt. Moonlight streaming through wooden balustrades, twinkling stars outside. Peaceful sleepy bedtime scene, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 65: Lukisan Kado Buatan Tangan ---
        {
            "id": "story65",
            "storyNumber": 65,
            "title": "Lukisan Kado Buatan Tangan",
            "englishTitle": "Handmade Gift Painting",
            "category": "social",
            "categoryLabel": "🤝 Pertemanan & Kebaikan Hati",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Ketulusan hati lebih berharga daripada hadiah mahal",
            "cover": "covers/story65_cover.jpg",
            "synopsis": "Rara tidak memiliki koin untuk membeli mainan berkilau bagi pesta ulang tahun sahabatnya. Dengan selembar kertas tebal, cat air buatan sendiri dari sari bunga, dan cinta yang melimpah, Rara melukis kenangan manis mereka yang menjadi kado terindah.",
            "protagonist": "Rara (Gadis cilik berjemari cat warna)",
            "companion": "Sahabat Rara (Teman ulang tahun bermahkotakan kertas)",
            "setting": "Pesta Ulang Tahun Sederhana",
            "pages": [
                {
                    "number": 1,
                    "title": "Undangan di Bawah Pintu",
                    "titleEn": "Invitation Under the Door",
                    "textId": "Pagi itu selembar kartu bergambar pita merah terselip di bawah pintu rumah Rara. Sahabat karibnya, Maya, berulang tahun yang keenam sore nanti. Rara bersorak girang, namun saat memeriksa celengan ayam gerabahnya, hanya terdengar gemerincing dua keping koin kecil.",
                    "textEn": "That morning, a card with a painted red ribbon slipped under Rara's front door. Her best friend, Maya, was celebrating her sixth birthday this evening. Rara cheered with joy, but checking her clay piggy bank, only two tiny coins chimed softly.",
                    "quote": "Kasih sayang sejati tidak pernah diukur dari jumlah uang.",
                    "coReading": "Pernahkah kamu membuat kartu ucapan untuk sahabatmu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Rara, a young girl with pigtails wearing a cozy apron, sitting on a wooden floor holding a handwritten invitation card and a small clay piggy bank. Morning sunlight streaming through a window, simple black bead dot eyes, exactly 4 limbs, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Toko Mainan Berkilau",
                    "titleEn": "The Sparkling Toy Shop",
                    "textId": "Di etalase toko desa, boneka berputar dan kotak musik berkerlip tampak begitu memesona. Namun harganya memerlukan sekantong penuh koin perak. Rara menatap jemari tangannya sendiri. 'Aku tidak bisa membeli mainan ini, tapi aku punya sepasang tangan dan sejuta kenangan bersama Maya,' gumamnya penuh tekad.",
                    "textEn": "In the village shop window, spinning dolls and music boxes sparkled enchantingly. But their price required a pouch full of silver coins. Rara looked down at her own two hands. 'I cannot buy these toys, but I have my hands and a million sweet memories with Maya,' she resolved.",
                    "quote": "Karya yang lahir dari tangan sendiri menyimpan detak cinta pembuatnya.",
                    "coReading": "Kado buatan sendiri atau kado toko yang lebih kamu sukai?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Rara standing outside a rustic village shop window, looking thoughtfully at displayed toys. Golden afternoon light, warm naive art style, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Warna-Warna dari Kebun",
                    "titleEn": "Colors from the Garden",
                    "textId": "Rara berlari ke kebun belakang. Ia memetik kelopak bunga telang biru tua, mengulek kunyit kuning terang, dan memeras buah naga merah jambu. Dari mangkuk-mangkuk tanah liat itu terbit cairan warna-warni yang harum semerbak, siap menjadi cat lukis istimewa.",
                    "textEn": "Rara dashed to her backyard garden. She picked deep blue butterfly pea petals, crushed bright yellow turmeric, and pressed pink dragon fruit. From the small clay bowls rose fragrant, vibrant colors, ready to become special painting dyes.",
                    "quote": "Alam menyediakan warna-warni terindah bagi hati yang penuh imajinasi.",
                    "coReading": "Warna apa saja yang dibuat Rara dari tanaman di kebun?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Rara sitting beside small stone bowls filled with vibrant natural dyes: blue flower dye, golden yellow paste, and magenta juice. Garden flowers and leaves around her, bead dot eyes, textured cream paper, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Goresan Pertama",
                    "titleEn": "The First Brushstroke",
                    "textId": "Di atas meja kayu terbentang kertas gambar tebal berserat jerami. Rara mencelupkan kuas bambunya ke dalam warna biru telang. Dengan hati berdebar dan penuh kelembutan, ia mulai melukis pohon beringin rindang tempat ia dan Maya biasa berayun bersama.",
                    "textEn": "Across her wooden table lay a sheet of thick textured paper. Rara dipped her bamboo paintbrush into the butterfly pea blue. With a fluttering, tender heart, she began painting the shady banyan tree where she and Maya loved to swing together.",
                    "quote": "Setiap goresan kuas adalah bisikan rasa terima kasih untuk seorang sahabat.",
                    "coReading": "Apa kenangan paling indah yang pernah kamu lalui bersama temanmu?",
                    "imagePrompt": "Wax crayon and soft pastel on heavy textured paper. Rara painting with focused delight at a wooden work table. Colorful jars of paint, textured cream paper showing the painted tree, paint smudges on her apron. Bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Taman Kenangan di Atas Kertas",
                    "titleEn": "Garden of Memories on Paper",
                    "textId": "Kuning kunyit melahirkan matahari senja yang ramah. Merah jambu melukis dua gadis kecil bergandengan tangan di padang rumput berhiaskan kupu-kupu. Di setiap sudut lukisan, Rara menorehkan cap ibu jarinya yang menyerupai kelopak bunga mekar.",
                    "textEn": "Yellow turmeric brought forth a friendly setting sun. Pink painted two little girls holding hands in a meadow fluttering with butterflies. In every corner of the painting, Rara pressed her thumbprints to look like blooming flower petals.",
                    "quote": "Kenangan manis adalah harta yang tak pernah bisa dibeli dengan emas.",
                    "coReading": "Dapatkah kamu melihat cap jempol Rara yang menjadi bunga?",
                    "imagePrompt": "Handcrafted oil pastel drawing showing the finished painting on paper: two young girls holding hands under a big tree with a smiling sun and thumbprint flower blooms. Beautiful naive folk-art style, wax textures, completely text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Gulungan Berikat Pita Rumput",
                    "titleEn": "Scroll Tied with Sweetgrass",
                    "textId": "Setelah cat alam itu kering sempurna dan beraroma harum dedaunan, Rara menggulung kertas lukisannya dengan rapi. Ia mengikat gulungan itu menggunakan sehelai pita rumput jepang yang ia anyam sendiri dan menyelipkan setangkai bunga melati putih di simpulnya.",
                    "textEn": "Once the natural paints dried completely, smelling fragrantly of sweet leaves, Rara rolled the paper neatly. She tied the scroll with a ribbon of braided sweetgrass and tucked a single white jasmine bloom into the knot.",
                    "quote": "Bungkus yang sederhana menjadi megah saat dibalut ketulusan.",
                    "coReading": "Mengapa Rara menyelipkan bunga melati pada ikatannya?",
                    "imagePrompt": "Wax crayon and soft oil pastel on cream watercolor paper. Rara holding a neatly rolled paper scroll tied with green woven grass ribbon and a white jasmine flower. Her face beaming with gentle pride, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 7,
                    "title": "Kado-Kado Berpita Emas",
                    "titleEn": "Gold-Ribboned Gifts",
                    "textId": "Di rumah Maya, meja pesta penuh sesak dengan kotak kado berbungkus kertas mengilap dan berpita satin emas. Ada robot mainan, gaun baru, dan boneka porselen. Rara sempat ragu memegang gulungan kertas sederhananya, menyembunyikannya di balik punggung.",
                    "textEn": "At Maya's house, the party table was piled high with gift boxes wrapped in shiny metallic papers and satin gold ribbons. There were toy robots, new dresses, and porcelain dolls. Rara hesitated for a moment, clutching her humble paper scroll behind her back.",
                    "quote": "Jangan pernah merasa kecil hanya karena apa yang kau miliki terlihat sederhana.",
                    "coReading": "Pernahkah kamu merasa malu atau minder dengan barang buatanmu?",
                    "imagePrompt": "Handcrafted wax crayon illustration. Birthday party setting with a table loaded with shiny wrapped presents. Maya wearing a paper crown greeting guests. Rara standing quietly near the door holding her paper scroll behind her back. Naive folk art, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Membuka Gulungan Cinta",
                    "titleEn": "Unrolling the Love",
                    "textId": "Maya berlari menghampiri Rara dan memeluknya hangat. 'Rara! Aku sangat senang kamu datang!' seru Maya. Rara menyerahkan gulungan beraroma melati itu. Saat ikat rumput dibuka dan lukisan terbentang, ruangan mendadak hening. Maya terperangah menatap gambar mereka berdua.",
                    "textEn": "Maya ran towards Rara and hugged her warmly. 'Rara! I am so glad you came!' Maya cheered. Rara handed over the jasmine-scented scroll. When the grass tie was undone and the painting unfurled, the room fell quietly still. Maya stared in awe at the picture of them both.",
                    "quote": "Ketulusan yang jujur selalu mampu menyentuh lubuk hati terdalam.",
                    "coReading": "Apa ekspresi wajah Maya saat melihat lukisan itu?",
                    "imagePrompt": "Warm oil pastel and wax crayon on textured cream paper. Maya in her paper crown unrolling the colorful handmade painting, her bead dot eyes wide with wonder and delight. Rara watching with a hopeful smile. Warm party lanterns in background, text-free, 4:3 landscape."
                },
                {
                    "number": 9,
                    "title": "Kado Paling Berharga",
                    "titleEn": "The Most Precious Gift",
                    "textId": "Air mata haru menitik di pipi Maya. 'Ini hari saat kita menanam bibit mangga dan tertawa kehujanan!' seru Maya penuh sukacita. 'Ini kado paling indah di seluruh dunia, Rara. Mainan bisa rusak dan usang, tapi kenangan lukisan ini akan kupajang di kamarku selamanya.'",
                    "textEn": "Tears of joy dotted Maya's cheeks. 'This was the day we planted mango seeds and laughed in the rain!' Maya exclaimed with joy. 'This is the most beautiful gift in the whole world, Rara. Toys may break and fade, but this painted memory will stay in my room forever.'",
                    "quote": "Benda materi bisa lapuk, namun cinta dan kenangan abadi selamanya.",
                    "coReading": "Mengapa kado Rara lebih berharga bagi Maya dibanding mainan mahal?",
                    "imagePrompt": "Handcrafted wax crayon drawing. Maya hugging Rara tightly, holding the painting up with one hand. Surrounding friends smiling warmly. Warm birthday party room decorated with paper garlands, bead dot eyes, 4 limbs constraint, completely text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Lukisan di Samping Bantal",
                    "titleEn": "The Painting Beside the Pillow",
                    "textId": "Malam tiba dan pesta berakhir. Di dinding kamar tidur Maya, lukisan Rara telah terpaku rapi di sisi ranjang, diterangi temaram lampu tidur berbintang. Dari kejauhan, Rara tidur pulas di rumahnya dengan jemari yang masih beraroma bunga telang dan hati yang mekar bahagia.",
                    "textEn": "Night fell and the party came to a close. On Maya's bedroom wall, Rara's painting hung neatly beside her bed, glowing softly under a starlight nightlight. Across town, Rara slept peacefully at home, fingers still fragrant with sweet pea flowers, her heart blooming with joy.",
                    "quote": "Tidurlah dengan damai, kebaikan hatimu telah menyinari dunia hari ini.",
                    "coReading": "Mari pejamkan mata dan bersyukur atas sahabat baik yang selalu ada untukmu.",
                    "imagePrompt": "Handcrafted wax crayon on heavy cream watercolor paper. Cozy bedroom at night with Maya sleeping peacefully under a quilt, with the colorful painting proudly framed on the wall beside her bed. Crescent moon and stars outside the window. Serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 66: Tunas Pertama Bunga Matahari ---
        {
            "id": "story66",
            "storyNumber": 66,
            "title": "Tunas Pertama Bunga Matahari",
            "englishTitle": "The First Sprout of the Sunflower",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kesabaran, ketelatenan merawat tanaman, & keajaiban bumi",
            "cover": "covers/story66_cover.jpg",
            "synopsis": "Lala menanam sebutir biji bunga matahari hitam bergaris putih di bedengan kebun belakang. Hari berganti hari dan tanah masih tampak sunyi. Bersama Coki si cacing tanah penggembur bumi, Lala belajar arti kesabaran menanti tunas mungil merekah menyapa mentari.",
            "protagonist": "Lala (Gadis cilik bertopi kebun membawa gembor)",
            "companion": "Coki (Cacing tanah penyubur bumi gembur)",
            "setting": "Bedengan Kebun Belakang",
            "pages": [
                {
                    "number": 1,
                    "title": "Biji Ajaib Bergaris Putih",
                    "titleEn": "The Striped Magic Seed",
                    "textId": "Di telapak tangan Lala terbaring sebutir biji bunga matahari hitam bergaris putih halus. Bentuknya kecil dan keras seperti kerikil kali. Kakek berbisik bahwa di dalam cangkang mungil ini tidur seekor raksasa kuning yang kelak akan menari mengikuti matahari.",
                    "textEn": "In Lala's palm lay a single sunflower seed, black with fine white stripes. It felt tiny and hard like a river pebble. Grandpa whispered that inside this tiny shell slept a golden giant who would one day dance with the sun.",
                    "quote": "Hal-hal terhebat di dunia sering kali bermula dari awal yang sangat kecil.",
                    "coReading": "Pernahkah kamu memegang biji tanaman? Bagaimana rasanya di tanganmu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy textured cream watercolor paper. Lala, a cute young girl in a wide woven straw sunhat and garden overalls, gazing with wonder at a single striped sunflower seed on her open palm. Warm morning sunshine in a cozy garden, simple bead dot eyes, 4 limbs, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Tempat Tidur Tanah yang Gembur",
                    "titleEn": "A Cozy Bed of Soft Soil",
                    "textId": "Lala menggunakan sekop kecilnya untuk membuat lubang sedalam jempol di bedengan kebun. Tanah hitam itu basah dan beraroma hujan segar. Dengan penuh hormat, Lala membaringkan si biji dan menyelimutinya dengan taburan tanah halus seperti merapikan selimut tidur.",
                    "textEn": "Lala used her little trowel to dig a hole as deep as her thumb in the garden bed. The rich dark soil smelled fresh like recent rain. With gentle care, Lala laid the seed down and covered it with a dusting of soft earth, just like tucking someone into bed.",
                    "quote": "Bumi adalah rumah paling hangat bagi kehidupan yang baru dimulai.",
                    "coReading": "Mengapa biji tanaman harus dikubur di dalam tanah yang gembur?",
                    "imagePrompt": "Wax crayon scribbles on cream paper. Lala kneeling on a garden kneeling pad, gently patting soil over a planted seed with her two hands. Garden trowel and small watering can beside her, naive folk art, simple black bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Kawan Bawah Tanah",
                    "titleEn": "Friend Beneath the Soil",
                    "textId": "Saat Lala merapikan tepian bedengan, gumpalan tanah bergerak perlahan. Muncullah Coki si cacing tanah berwarna merah muda cerah. 'Jangan khawatir, Lala,' gumam Coki dengan gerak meliuk lembut, 'aku akan membuat terowongan udara agar akar bijimu bisa bernapas lega.'",
                    "textEn": "As Lala smoothed the edge of the bed, a clump of soil wiggled slowly. Up popped Coki, a cheerful pink earthworm. 'Don't worry, Lala,' whispered Coki with a gentle wriggle, 'I will dig air tunnels so your seed's roots can breathe easy.'",
                    "quote": "Setiap makhluk kecil di kebun memiliki tugas mulia bagi kehidupan.",
                    "coReading": "Tahukah kamu cacing tanah membantu tanaman tumbuh subur?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Lala smiling gently, observing Coki the friendly pink earthworm poking out of rich dark soil. Lala wearing gardening gloves, cute bead dot eyes, warm garden textures, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Hujan Buatan dari Gembor Seng",
                    "titleEn": "Gentle Rain from the Tin Can",
                    "textId": "Lala mengangkat gembor seng kecilnya yang berwarna hijau lumut. Dari corong berbintik-bintik itu mengucur butiran air halus seperti gerimis pagi. Tetesan air itu membasahi tanah kering tanpa membuat si biji hanyut dari tempat tidurnya.",
                    "textEn": "Lala lifted her little moss-green tin watering can. From its spotted spout showered fine droplets like a morning drizzle. The gentle water bathed the soil without washing the sleeping seed from its cozy cradle.",
                    "quote": "Kasih sayang diberikan secukupnya, tidak berlebihan dan tidak terburu-buru.",
                    "coReading": "Bagaimana suara tetesan air dari gembor menurutmu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Lala pouring gentle droplets of water from a vintage green watering can onto dark garden soil. Sparkling water drops glistening in morning sun rays, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Menunggu di Hari Ketiga",
                    "titleEn": "Waiting on Day Three",
                    "textId": "Tiga hari berlalu. Setiap pagi Lala berlari ke kebun sebelum mencuci muka. Namun bedengan tanah masih tampak hitam sunyi. Belum ada daun, belum ada helai hijau. Lala mulai gelisah, mengira bijinya terlupa untuk bangun.",
                    "textEn": "Three days passed. Every morning Lala ran to the garden before even washing her face. But the garden bed remained still and dark. No leaves yet, not a single speck of green. Lala grew restless, wondering if the seed had forgotten to wake up.",
                    "quote": "Menunggu adalah bagian paling hening dari sebuah perjalanan indah.",
                    "coReading": "Apakah kamu pernah merasa tidak sabar menunggu sesuatu?",
                    "imagePrompt": "Wax crayon drawing on textured paper. Lala sitting on a garden bench with her chin resting on her hands, looking down anxiously at the bare dark garden plot. Soft morning light, pensive expression with bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 6,
                    "title": "Nasihat Kakek tentang Kesabaran",
                    "titleEn": "Grandpa's Lesson on Patience",
                    "textId": "Kakek datang membawa cangkir teh hangat dan mengelus kepala Lala. 'Di dalam kegelapan tanah, bijimu sedang bekerja keras, Lala. Ia merajut akar-akar halus ke dasar bumi terlebih dahulu agar kelak batangnya kokoh diterpa angin badai. Sabarlah menanti.'",
                    "textEn": "Grandpa came over with warm tea, stroking Lala's head gently. 'Inside the soil's darkness, your seed is working hard, Lala. It weaves fine roots deep into the earth first, so its stem can stand strong against stormy winds. Be patient and trust.'",
                    "quote": "Kekuatan yang sejati dibangun dalam keheningan yang tak terlihat mata.",
                    "coReading": "Mengapa akar harus tumbuh lebih dulu sebelum daun?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on cream paper. Kind elderly grandfather in a cardigan sitting beside Lala on the wooden bench, pointing tenderly toward the ground. Warm comforting atmosphere, simple bead eyes on both, exactly 4 limbs, text-free, 4:3 horizontal."
                },
                {
                    "number": 7,
                    "title": "Retakan Kecil di Pagi Buta",
                    "titleEn": "A Tiny Crack at Dawn",
                    "textId": "Pagi kelima diselimuti kabut tipis berembun. Saat Lala melangkah mendekat, ia melihat sesuatu yang berbeda di tengah bedengan. Permukaan tanah yang rata tampak merekah kecil, seperti ada jari mungil yang sedang mendorong pintu dari dalam bumi.",
                    "textEn": "The fifth morning was veiled in a gentle, dewy mist. As Lala stepped closer, she noticed something different in the center of the bed. The smooth soil surface had cracked open slightly, as if tiny fingers were pushing a door open from beneath.",
                    "quote": "Harapan selalu menemukan celah untuk merekah ke udara bebas.",
                    "coReading": "Kira-kira apa yang sedang mendorong tanah itu keluar?",
                    "imagePrompt": "Detailed wax crayon and oil pastel on textured paper. Close-up of rich dark soil cracking gently, with a bright lime-green loop of stem peeking through the soil. Dewdrops glistening on surrounding leaves, morning dawn glow, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Lengkungan Hijau Pertama",
                    "titleEn": "The First Green Arch",
                    "textId": "Lala berjongkok sangat dekat, menahan napasnya. Di sana, sehelai tunas hijau muda melengkung anggun, masih memanggul sisa kulit biji hitam di punggungnya seperti topi pelindung. 'Halo, si kecil!' bisik Lala dengan mata berkaca-kaca bahagia.",
                    "textEn": "Lala crouched very close, holding her breath. There, a bright young green sprout arched gracefully, still carrying the remnant black seed shell on its back like a little safety helmet. 'Hello, little one!' Lala whispered, eyes shimmering with happy tears.",
                    "quote": "Kehidupan baru adalah keajaiban paling suci yang dianugerahkan alam.",
                    "coReading": "Lihatlah, cangkang bijinya masih menempel! Lucu sekali ya?",
                    "imagePrompt": "Handcrafted wax crayon illustration on cream paper. Lala kneeling on the grass, face close to the tiny green sprout that carries a tiny black seed coat. Lala's hands clasping her chest in joy, simple black bead dot eyes, magical morning golden sunlight, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Dua Daun Terbuka Menyapa Surya",
                    "titleEn": "Two Leaves Unfurl to Greet the Sun",
                    "textId": "Saat sinar mentari menghangatkan udara, cangkang hitam terlepas pelan ke tanah. Dua helai daun mungil berbentuk hati membuka perlahan, menyerap hangatnya cahaya matahari pagi. Coki si cacing menyembul di samping tunas dan bertepuk tangan gembira.",
                    "textEn": "As the sunlight warmed the air, the black shell slipped gently onto the soil. Two tiny heart-shaped leaves unfurled slowly, drinking in the morning sun's golden warmth. Coki the worm poked out beside the sprout, clapping his tiny body in delight.",
                    "quote": "Kesabaran yang dirawat dengan cinta selalu berbuah kebahagiaan manis.",
                    "coReading": "Bunga matahari selalu menghadap ke mana saat pagi hari?",
                    "imagePrompt": "Soft wax crayon scribbles and oil pastel smudges. The tiny sunflower sprout with two open bright green leaves bathing in radiant morning sunlight rays. Coki the worm smiling beside it. Dewdrops sparkling, naive folk-art style, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Lullaby untuk Tunas yang Tidur",
                    "titleEn": "Lullaby for the Sleeping Sprout",
                    "textId": "Senja membungkus kebun dengan selimut ungu tenang. Sebelum masuk ke rumah, Lala membisikkan doa selamat malam untuk tunas pertamanya. Di bawah taburan bintang malam yang berkelap-kelip, si tunas kecil tertidur lelap, bersiap tumbuh semakin tinggi esok hari.",
                    "textEn": "Dusk wrapped the garden in a quiet violet blanket. Before heading inside, Lala whispered a goodnight prayer to her very first sprout. Beneath a sky of twinkling night stars, the little sprout slept soundly, ready to grow taller tomorrow.",
                    "quote": "Tidurlah dengan tenang, esok adalah hari baru untuk tumbuh lebih tinggi.",
                    "coReading": "Mari ucapkan selamat tidur untuk tanaman dan bunga-bunga di luar rumah.",
                    "imagePrompt": "Handcrafted wax crayon on heavy textured cream paper. Lala standing on her porch in soft nightgown looking back affectionately at the garden bed where the tiny sprout sleeps under a starlit night sky with a smiling crescent moon. Deep indigo and lavender tones, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 67: Aliran Sungai Jernih Bebas Ranting ---
        {
            "id": "story67",
            "storyNumber": 67,
            "title": "Aliran Sungai Jernih Bebas Ranting",
            "englishTitle": "Clear Stream Free of Twigs",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Peduli kebersihan alam & gotong royong menjaga aliran air",
            "cover": "covers/story67_cover.jpg",
            "synopsis": "Budi menemukan anak sungai favoritnya tersumbat oleh tumpukan ranting patah dan sampah dedaunan kering, membuat ikan-ikan nila kecil terjebak dan airnya keruh. Dengan sepatu bot karet dan jaring bambunya, Budi membersihkan aliran sungai hingga kembali bernyanyi merdu.",
            "protagonist": "Budi (Anak laki-laki bersepatu bot karet)",
            "companion": "Ikan Nila (Ikan-ikan sungai berenang lincah)",
            "setting": "Sungai Kerikil Jernih",
            "pages": [
                {
                    "number": 1,
                    "title": "Gemericik yang Hilang",
                    "titleEn": "The Missing Murmur",
                    "textId": "Biasanya dari ujung jalan desa, gemericik air sungai berbatu terdengar riang seperti nyanyian seruling bambu. Namun pagi ini, Budi yang mengenakan sepatu bot karet kuning cerah merasakan kesunyian aneh. Suara aliran sungai terdengar berat dan tersendat-sendat.",
                    "textEn": "Usually from the edge of the village path, the pebble stream's murmur sounded merry like a bamboo flute. But this morning, Budi in his bright yellow rubber boots sensed a strange silence. The stream's voice sounded heavy and sluggish.",
                    "quote": "Alam selalu berbicara kepada mereka yang mau mendengarkan dengan hati.",
                    "coReading": "Pernahkah kamu mendengar suara air sungai yang mengalir deras?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy textured cream watercolor paper. Budi, a young boy in yellow rain boots, blue shorts, and a warm knitted sweater, standing by a lush forest path looking towards a rocky stream. Tall trees, morning mist, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Bendungan Ranting Patah",
                    "titleEn": "The Dam of Broken Twigs",
                    "textId": "Saat tiba di tepi sungai, Budi melihat penyebabnya. Badai angin semalam telah merontokkan dahan-dahan tua pohon randu. Ranting-ranting tebal dan timbunan daun busuk tersangkut di celah bebatuan besar, menahan aliran air menjadi genangan keruh berwarna kecokelatan.",
                    "textEn": "Arriving at the stream bank, Budi saw the reason. Last night's windstorm had snapped old branches from the cotton tree. Thick twigs and rotting leaf piles were wedged between large boulders, damming the water into a muddy brownish pool.",
                    "quote": "Satu hambatan kecil dapat menghentikan kelancaran aliran yang besar.",
                    "coReading": "Apa yang terjadi pada air sungai saat tersumbat sampah ranting?",
                    "imagePrompt": "Wax crayon scribbles on heavy cream paper. A river clogged with crisscrossed dry branches, fallen twigs, and trapped leaves between smooth river stones. Muddy brown water collecting behind the blockage, naive folk-art style, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Keluhan Ikan Nila",
                    "titleEn": "The Little Tilapia's Plea",
                    "textId": "Di balik genangan yang tersumbat, sekelompok anak ikan nila bergaris perak berenang berputar-putar dengan gelisah. Sirip mereka bergetar mencari jalan keluar, tetapi air semakin surut dan dangkal. Salah satu ikan melompat kecil seolah meminta pertolongan pada Budi.",
                    "textEn": "Behind the blocked pool, a school of silver-striped little tilapia swam nervously in circles. Their fins fluttered searching for a way out, but the water grew shallower and murky. One tiny fish did a gentle hop, as if pleading for Budi's help.",
                    "quote": "Makhluk-makhluk kecil sering kali tak berdaya saat rumah mereka terganggu.",
                    "coReading": "Bagaimana perasaan ikan-ikan ketika air tempat hidupnya menjadi keruh?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Close-up of water surface with little silver fish swimming nervously in a shallow rocky pool. Budi kneeling on a large boulder by the edge, gazing down with deep concern. Simple bead dot eyes, soft ripples, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Langkah Berani ke Dalam Air",
                    "titleEn": "Brave Steps into the Water",
                    "textId": "Budi tidak ragu sedetik pun. Ia menggulung lengan bajunya hingga ke siku dan melangkah masuk ke dalam sungai dangkal. 'Kres, kres!' bunyi kerikil di bawah sepatu bot kuningnya. Dinginnya air menyapa kakinya, tetapi tekad di dadanya menyala hangat.",
                    "textEn": "Budi did not hesitate for a second. He rolled his sleeves up to his elbows and stepped into the shallow stream. 'Crunch, crunch!' sounded the pebbles under his yellow boots. The water's chill greeted his feet, but warm determination burned in his chest.",
                    "quote": "Bantuan yang nyata dimulai dari kemauan untuk mengulurkan tangan.",
                    "coReading": "Apakah kamu berani masuk ke air sungai dangkal seperti Budi?",
                    "imagePrompt": "Handcrafted oil pastel and wax crayon. Budi wading carefully in ankle-deep river water with his bright yellow rubber boots, hands outstretched ready to lift river branches. Textured cream paper, naive storybook style, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Mengangkat Dahan Pertama",
                    "titleEn": "Lifting the Heaviest Branch",
                    "textId": "Dengan kedua tangannya yang kuat, Budi menarik dahan randu paling besar yang mengunci tumpukan ranting. Dahan itu basah dan berat berlumut. Dengan tarikan perlahan tapi pasti, 'Kreek!' dahan terangkat dan diletakkan aman di tanggul sungai.",
                    "textEn": "With both sturdy hands, Budi hauled the largest cottonwood branch that locked the tangle together. It was heavy, waterlogged, and slick with moss. With a slow and steady tug, 'Creak!' the branch lifted free and was set safely on the riverbank.",
                    "quote": "Beban terberat terasa ringan bila dikerjakan dengan hati yang ikhlas.",
                    "coReading": "Berapa banyak tangan yang Budi gunakan untuk mengangkat dahan berat?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Budi using both hands to haul a large wet tree branch out of the water onto the grassy riverbank. Exactly 4 limbs (2 legs standing sturdy in water, 2 arms pulling branch), simple bead eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Jaring Daun yang Rapi",
                    "titleEn": "Clearing with the Bamboo Net",
                    "textId": "Setelah dahan besar disingkirkan, Budi menggunakan serokan bambunya untuk menyaring guguran daun kering yang mengapung. Sedikit demi sedikit, gumpalan lumpur mulai terurai terbawa arus, memperlihatkan kembali pasir putih berkilauan di dasar sungai.",
                    "textEn": "Once the big branch was removed, Budi used his bamboo hand-net to scoop up floating dried leaves. Bit by bit, clumps of mud dissolved in the gentle current, revealing sparkling white sand at the riverbed once more.",
                    "quote": "Ketelatenan membersihkan hal-hal kecil mengembalikan kejernihan hidup.",
                    "coReading": "Apa yang terlihat di dasar sungai saat airnya mulai jernih?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Budi scooping floating brown leaves with a small woven bamboo net. Sunlight piercing through clean water ripples revealing shiny pebbles on the riverbed, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Aliran yang Bernapas Lega",
                    "titleEn": "The Stream Breathes Free",
                    "textId": "'Kecipak, kecipuk!' Arus air yang tertahan seketika meluncur deras menembus sela bebatuan. Suara gemericik sungai kembali berkumandang, seperti helaan napas panjang yang penuh rasa syukur. Air yang jernih memantulkan langit biru cerah di permukaannya.",
                    "textEn": "'Splash, gurgle!' The penned-up current surged swiftly through the gaps between boulders. The stream's singing murmur rang out once more, like a long sigh of grateful relief. The crystal-clear water mirrored the bright blue sky above.",
                    "quote": "Kebaikan yang kita lakukan mengembalikan harmoni pada semesta.",
                    "coReading": "Bagaimana bunyi suara air yang mengalir bebas sekarang?",
                    "imagePrompt": "Soft oil pastel smudges and crayon lines. Fresh crystal-clear river water splashing happily over smooth grey river boulders, catching sunlight glints. Budi standing proudly by the bank with wet boots, smiling with bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Tarian Terima Kasih Ikan Nila",
                    "titleEn": "The Tilapias' Thank-You Dance",
                    "textId": "Ikan-ikan nila berenang meluncur lincah menembus arus baru. Mereka meliuk-liuk di sekitar sepatu bot Budi, menyenggol lembut karet bot seolah mengucapkan terima kasih. Sisik perak mereka berkilauan seperti kepingan permata di bawah sinar matahari.",
                    "textEn": "The little tilapia zipped joyfully through the fresh current. They danced around Budi's boots, brushing gently against the rubber as if saying thank you. Their silver scales shimmered like tiny jewels beneath the sunlight.",
                    "quote": "Rasa syukur makhluk hidup terasa nyata meski tanpa kata-kata.",
                    "coReading": "Lihatlah ikan-ikan itu berenang mengelilingi sepatu Budi!",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Clear transparent river water showing schools of shiny silver tilapia fish swimming happily around Budi's yellow boots. Budi looking down with pure happiness, simple bead dot eyes, naive folk art, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Ranting yang Menjadi Rumah Serangga",
                    "titleEn": "Twigs That Become an Insect Hotel",
                    "textId": "Budi tidak membuang ranting-ranting basah itu sembarangan. Ia menatanya rapi di bawah pohon rindang di tepi sungai. Tumpukan kayu itu kini menjadi rumah perlindungan baru bagi kumbang, jangkrik, dan semut hutan yang membutuhkan tempat berteduh.",
                    "textEn": "Budi did not discard the wet branches carelessly. He stacked them neatly beneath a leafy tree on the bank. The woodpile now became a safe haven for beetles, crickets, and forest ants in need of cozy shelter.",
                    "quote": "Tidak ada yang sia-sia di alam bila kita menatanya dengan bijaksana.",
                    "coReading": "Siapa yang akan tinggal di tumpukan kayu rapi buatan Budi?",
                    "imagePrompt": "Warm wax crayon drawing. Budi arranging broken branches into a neat habitat pile beside a sturdy tree trunk. Ladybugs and tiny beetles crawling peacefully on the wood. Golden afternoon light, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Senandung Sungai Pengantar Tidur",
                    "titleEn": "The Stream's Sleepy Lullaby",
                    "textId": "Malam tiba dan bintang-bintang tercermin indah di atas permukaan sungai yang jernih mengalir tanpa rintangan. Di kamarnya yang nyaman, Budi membuka jendela sedikit untuk mendengarkan gemericik air yang merdu dari kejauhan. Nyanyian sungai itu menemaninya terlelap dalam mimpi indah.",
                    "textEn": "Night fell and stars mirrored peacefully upon the clear, freely flowing stream. In his cozy bedroom, Budi cracked the window open slightly to hear the melodious murmur of the water from afar. The stream's lullaby lulled him gently into sweet, peaceful dreams.",
                    "quote": "Tidurlah dengan nyenyak, sungai jernih terus bernyanyi menjaga lelapmu.",
                    "coReading": "Mari pejamkan mata sambil mendengarkan gemericik air yang menenangkan hati.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Cozy bedroom with Budi sleeping soundly tucked under a blue quilt. Open bedroom window revealing moonlight sparkling on the distant clean winding river under starry night sky. Serene, peaceful bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
