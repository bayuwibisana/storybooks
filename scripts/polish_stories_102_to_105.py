# scripts/polish_stories_102_to_105.py
import json

def get_stories_102_to_105():
    stories = [
        # --- STORY 102: Kerja Bakti Hari Minggu ---
        {
            "id": "story102",
            "storyNumber": 102,
            "title": "Kerja Bakti Hari Minggu",
            "englishTitle": "Sunday Family Clean-Up Day",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Gotong royong di rumah, merawat kebersihan bersama, & keceriaan kerja bakti",
            "cover": "covers/story102_cover.jpg",
            "synopsis": "Minggu pagi yang cerah disambut dengan musik ceria dari radio tua Ayah. Rio memegang kemoceng bulu ayam berbulu pelangi, Adik Ani membawa lap basah berbusa sabun, dan Ayah serta Ibu membersihkan jendela dan teras. Bersama-sama, mereka membuat rumah bersih berkilauan dan harum lemon segar.",
            "protagonist": "Kakak Rio & Adik Ani (Sepasang saudara membawa kemoceng dan sapu)",
            "companion": "Kucing Rumah (Kucing memperhatikan dari atas lemari)",
            "setting": "Ruang Tamu Terbuka",
            "pages": [
                {
                    "number": 1,
                    "title": "Musik Ceria dari Radio Tua",
                    "titleEn": "Merry Tunes from the Vintage Radio",
                    "textId": "Minggu pagi disapa oleh kicau burung pipit dan lagu ceria berirama cepat dari radio kayu tua Ayah di ruang tengah. Jendela-jendela rumah dibuka lebar-lebar membiarkan semilir angin sejuk dan harum embun rumput masuk menyegarkan seisi rumah.",
                    "textEn": "Sunday morning was welcomed by sparrow chirps and brisk, cheerful melodies from Dad's vintage wooden radio in the living room. Windows were swung wide open, inviting cool breezes and fresh dewy garden scents inside.",
                    "quote": "Hari Minggu adalah hari untuk merawat rumah bersama penuh sukacita.",
                    "coReading": "Apa yang biasanya kamu dan keluargamu lakukan di hari Minggu pagi?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Sunny family living room on Sunday morning, with wide open windows showing green garden. Vintage radio on shelf playing musical notes, Rio holding a feather duster, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Kemoceng Bulu Pelangi Rio",
                    "titleEn": "Rio's Rainbow Feather Duster",
                    "textId": "Rio mengenakan ikat kepala merah seperti pendekar cilik. Di tangannya terpegang kemoceng bulu ayam warna-warni yang empuk dan lebat. Rio mengayunkan kemocengnya ke atas rak buku: 'Syuuut, syuuut!' Debu-debu halus berterbangan dan lenyap tertiup angin jendela.",
                    "textEn": "Rio wore a red bandana like a little warrior. In his hand he waved a fluffy, colorful feather duster. Rio swept it across the bookshelf: 'Swish, flick!' Fine dust motes scattered and vanished out the breezy window.",
                    "quote": "Tugas membersihkan rumah terasa ringan saat dilakukan dengan hati yang riang.",
                    "coReading": "Warna apa saja bulu kemoceng yang dipegang Rio?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Rio standing on tiptoe dusting a wooden bookshelf filled with colorful books using a fluffy rainbow feather duster. Naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Lap Basah Beraroma Lemon Adik Ani",
                    "titleEn": "Sister Ani's Lemon-Scented Rag",
                    "textId": "Adik Ani membawa ember kecil berisi air berbusa sabun lemon. Dengan lap katun kuningnya, Ani mengelap permukaan meja kopi kayu hingga berkilau bersih. 'Mejanya sekarang wangi seperti permen lemon, Kak!' seru Ani sambil tersenyum bangga.",
                    "textEn": "Little Sister Ani carried a small bucket of lemon-soap suds. With a yellow cotton cloth, she wiped the wooden coffee table until it shone spotless. 'The table smells like sweet lemon candy now, Brother!' Ani cheered with pride.",
                    "quote": "Kebersihan menghadirkan kesegaran yang menyenangkan bagi seisi rumah.",
                    "coReading": "Bagaimana aroma pembersih meja yang digunakan Ani?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Little sister Ani in an apron kneeling by the wooden coffee table, wiping it shiny with a yellow soapy cloth. Small tin bucket with bubbles beside her, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Kucing Penonton di Atas Lemari",
                    "titleEn": "The Cat Spectator Atop the Wardrobe",
                    "textId": "Milo, kucing belang abu-abu mereka, melompat ke puncak lemari pakaian untuk menghindari lantai yang basah. Dari atas, Milo mengamati sapuan sapu Ayah dan kemoceng Rio dengan kepala miring ke kiri dan ke kanan, bertindak sebagai mandor cilik berbulu.",
                    "textEn": "Milo, their grey tabby cat, bounded atop the tall wardrobe to avoid the damp floor. From above, Milo watched Dad's broom strokes and Rio's duster, tilting his head left and right like a furry little foreman.",
                    "quote": "Bahkan hewan peliharaan pun menikmati keceriaan kerja bakti keluarga.",
                    "coReading": "Di mana kucing Milo duduk memperhatikan kerja bakti?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Cute grey tabby cat perched high on a wooden wardrobe, peering down with curious black bead dot eyes at the busy family below. Cozy home details, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Semprotan Kaca dan Gerakan Memutar",
                    "titleEn": "Glass Spray and Circular Wipes",
                    "textId": "Ibu menyemprotkan air bersih ke kaca jendela: 'Cres, cres!' Ayah menggunakan karet pembersih kaca untuk menarik air dari atas ke bawah: 'Sreeet!' Kaca jendela yang tadinya berdebu kini menjadi bening transparan seperti kristal es tanpa noda.",
                    "textEn": "Mother spritzed clean water on the window panes: 'Spritz, mist!' Dad used a rubber squeegee to pull the water down: 'Glide!' The dusty panes turned crystal-clear, transparent as ice without a single smudge.",
                    "quote": "Kaca yang bersih membuat sinar matahari pagi masuk dengan sempurna.",
                    "coReading": "Alat apa yang digunakan Ayah untuk membersihkan kaca jendela?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother spraying glass cleaner and Dad wiping a large window with a squeegee, smiling together. Sparkling clean glass revealing green yard outside, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Tarian Sapu Lidi di Teras",
                    "titleEn": "Broom Dance on the Porch",
                    "textId": "Rio membantu Ayah menyapu daun-daun kering di teras depan menggunakan sapu lidi bertangkai bambu. 'Srok, srok, srok!' irama sapuan lidi berpadu dengan ketukan lagu radio, membuat kerja bakti terasa seperti tarian bersama di bawah sinar mentari pagi.",
                    "textEn": "Rio helped Dad sweep dry leaves off the front porch with a bamboo-handled palm-leaf broom. 'Scrape, swish, scrape!' the rhythmic sweep blended with the radio beat, turning the chore into a merry dance in the morning sun.",
                    "quote": "Gotong royong terasa menyenangkan saat diiringi irama kegembiraan.",
                    "coReading": "Bisakah kamu menirukan bunyi sapu lidi yang menyapu lantai teras?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Rio sweeping dry leaves on the front porch with a broom, making dancing steps with Dad. Warm morning sunbeams, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Lantai yang Bersih Mengilap",
                    "titleEn": "Shiny Gleaming Floors",
                    "textId": "Ibu mengepel lantai terakota dengan kain pel hangat beraroma serai wangi. Lantai merah itu kini bersih mengilap, sejuk di telapak kaki tanpa ada sebutir debu pun yang tersisa. Seluruh perabotan tertata rapi di tempatnya masing-masing.",
                    "textEn": "Mother mopped the terracotta tiles with warm lemongrass-scented floor wash. The reddish tiles gleamed cool and spotless beneath bare feet, not a speck of dust remaining. Every piece of furniture sat neatly in its place.",
                    "quote": "Rumah yang bersih menghadirkan kesehatan dan ketenteraman bagi keluarga.",
                    "coReading": "Bagaimana aroma lantai yang baru saja dipel oleh Ibu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Pristine clean living room with shiny red terracotta tiles reflecting sunlight. Potted ferns, neat sofas, family admiring the tidy room, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Es Kelapa Muda Pelepas Dahaga",
                    "titleEn": "Young Coconut Ice to Quench Thirst",
                    "textId": "Kerja bakti selesai! Ayah membawa nampan berisi empat gelas es kelapa muda dengan perasan jeruk nipis dan gula aren cair. Mereka berempat duduk di teras bersih, meminum es yang dingin menyegarkan sambil mengelap keringat dengan senyuman puas.",
                    "textEn": "Clean-up was complete! Dad brought a tray with four glasses of iced young coconut water with a splash of lime and palm sugar syrup. The four sat on the clean porch, sipping refreshing cold drinks, wiping sweat with satisfied smiles.",
                    "quote": "Hadiah terbaik sehabis kerja keras adalah kesegaran yang dinikmati bersama.",
                    "coReading": "Minuman segar apa yang dinikmati keluarga Rio sehabis kerja bakti?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. The family of four sitting together on the clean porch steps enjoying glasses of iced coconut water with lime slices, laughing merrily. Cat rubbing against Rio's ankles, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Pujian Hangat untuk Anak-Anak Rajin",
                    "titleEn": "Warm Praise for Helpful Children",
                    "textId": "Ayah merangkul pundak Rio dan Ani. 'Kalian berdua adalah pahlawan kebersihan rumah hari ini. Berkat bantuan Rio dan Ani, rumah kita terasa seratus kali lebih luas, nyaman, dan indah.' Rio dan Ani bertepuk tangan bangga.",
                    "textEn": "Dad put his arms around Rio and Ani's shoulders. 'You two are our home cleaning heroes today. Thanks to Rio and Ani, our house feels a hundred times roomier, cozier, and brighter.' Rio and Ani clapped with pride.",
                    "quote": "Bekerja sama membangun rumah adalah fondasi persatuan keluarga.",
                    "coReading": "Mengapa Ayah menyebut Rio dan Ani sebagai pahlawan kebersihan?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Father hugging Rio and Ani warmly on the porch steps, with Mother smiling proudly beside them holding an empty tray. Golden afternoon sun, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Siang yang Paling Nyenyak",
                    "titleEn": "The Sweetest Afternoon Nap",
                    "textId": "Siang hari sehabis mandi bersih, semilir angin berhembus melalui tirai jendela yang bersih. Di kamarnya yang harum serai dan lemon, Rio dan Ani tidur siang pulas di kasur masing-masing, bermimpi terbang di atas awan-awan putih bersih di langit yang cerah.",
                    "textEn": "After a refreshing bath, gentle breezes fluttered through clean window curtains. In their room smelling of lemongrass and lemon, Rio and Ani took a deep, peaceful afternoon nap, dreaming of soaring over pure white clouds in a bright sunny sky.",
                    "quote": "Tidurlah dalam kenyamanan rumah yang bersih, kerja kerasmu telah membuahkan damai.",
                    "coReading": "Selamat beristirahat di rumah yang bersih dan nyaman, anak-anak hebat.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Rio sleeping peacefully in his tidy bedroom bed, with fresh clean curtains billowing in the soft breeze. Cat sleeping curled at the foot of the bed. Serene peaceful resting atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 103: Album Foto Bayi Sebesar Semangka ---
        {
            "id": "story103",
            "storyNumber": 103,
            "title": "Album Foto Bayi Sebesar Semangka",
            "englishTitle": "Baby Photo Album the Size of a Watermelon",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menghargai kenangan masa kecil, rasa syukur tumbuh kembang, & cinta abadi orang tua",
            "cover": "covers/story103_cover.jpg",
            "synopsis": "Di sore yang gerimis sejuk, Dika diajak Ayah dan Ibu membuka album foto keluarga bersampul beludru biru tua. Dika tertawa geli melihat foto dirinya saat baru lahir: kepalanya botak licin, pipinya merah gembul, dan tubuhnya hanya sebesar buah semangka di dalam pelukan Ayah.",
            "protagonist": "Keluarga Ceria (Ayah dan Ibu membuka album bersampul beludru)",
            "companion": "Anak Balita (Balita menunjuk foto dirinya sendiri)",
            "setting": "Karpet Tebal Lantai",
            "pages": [
                {
                    "number": 1,
                    "title": "Album Beludru Biru di Lemari Kaca",
                    "titleEn": "The Navy Velvet Album in the Glass Cabinet",
                    "textId": "Hujan gerimis turun menitik lembut di kaca jendela ruang keluarga. Udara terasa dingin dan sejuk. Dari lemari kaca kayu jati, Ayah menurunkan sebuah buku besar bersampul kain beludru biru tua dengan sudut-sudut kuningan berkilau emas. Itu adalah album foto kenangan keluarga.",
                    "textEn": "A gentle drizzle tapped softly on the living room window glass. The air was cool and crisp. From the teak glass cabinet, Father brought down a large book bound in navy velvet with shiny brass corner clasps. It was the family memory photo album.",
                    "quote": "Album foto adalah peti harta karun yang menyimpan jejak cinta di masa lalu.",
                    "coReading": "Pernahkah kamu melihat foto-fotomu saat masih bayi kecil?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Father lifting a thick navy blue velvet album with gold brass corners from a wooden cabinet. Dika, a cute young boy in a sweater, sitting on the thick floor rug with Mother, looking up eagerly, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Aroma Kertas Tua dan Kenangan",
                    "titleEn": "Scent of Old Paper and Memories",
                    "textId": "Ayah meletakkan album tebal itu di tengah karpet bulu empuk. Ketika sampul beludru dibuka, menguar aroma khas kertas foto tua yang harum bernostalgia. Dika merapatkan duduknya di antara Ayah dan Ibu, memandang halaman pertama yang berbingkai renda kertas.",
                    "textEn": "Father set the heavy album in the center of the plush floor rug. When the velvet cover opened, a nostalgic scent of aged photo paper wafted out. Dika nestled close between Father and Mother, gazing at the first lace-bordered page.",
                    "quote": "Kenangan manis selalu membawa kehangatan saat dibuka kembali bersama.",
                    "coReading": "Bagaimana aroma buku foto kenangan saat dibuka?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up of the open album showing vintage sepia and color photographs framed in delicate paper borders. Dika's small finger pointing with wonder, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Bayi Mungil Sebesar Buah Semangka",
                    "titleEn": "Tiny Baby the Size of a Watermelon",
                    "textId": "Di lembar pertama, tampak foto seorang bayi mungil yang dibungkus kain bedong kuning muda. Bayi itu memiliki kepala botak licin berkilau dan pipi merah gembul seperti bakpao kukus. 'Ayah, siapa bayi lucu yang seperti buah semangka ini?' tanya Dika penasaran.",
                    "textEn": "On the first leaf sat a photo of a tiny baby bundled in a pale yellow swaddle. The baby had a smooth shiny bald head and chubby cheeks like a steamed bun. 'Father, who is this funny baby the size of a watermelon?' Dika asked with curiosity.",
                    "quote": "Setiap anak yang besar bermula dari awal yang sangat kecil dan menggemaskan.",
                    "coReading": "Tahukah Dika siapa bayi mungil di dalam foto itu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A photograph in the album showing a newborn baby wrapped in a yellow blanket sleeping in Father's big hands. Dika looking at the photo with a surprised smile, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Tawa Ibu Menyibak Rahasia",
                    "titleEn": "Mother's Laughter Reveals the Secret",
                    "textId": "Ibu tertawa lembut dan mengelus pipi Dika: 'Itu kamu, Dika sayang! Saat kamu baru lahir ke dunia empat tahun lalu, tubuhmu begitu mungil hingga muat digendong dengan satu lengan Ayah saja.' Dika terbelalak tak percaya menatap fotonya sendiri.",
                    "textEn": "Mother chuckled softly, stroking Dika's cheek: 'That is you, sweet Dika! When you were born into the world four years ago, you were so tiny you fit in just one of Father's arms.' Dika's eyes widened in disbelief at his own picture.",
                    "quote": "Melihat masa kecil kita menumbuhkan rasa takjub atas anugerah kehidupan.",
                    "coReading": "Apakah kamu percaya bahwa dulu kamu pernah sekecil bayi itu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Mother laughing gently with arm around Dika, pointing to the baby photo. Father smiling beside them, warm family bonding on the living room rug, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Jejak Telapak Kaki Sekecil Daun Melati",
                    "titleEn": "Footprint Stamp as Tiny as a Jasmine Leaf",
                    "textId": "Di samping foto, ada cap tinta biru telapak kaki bayi Dika di atas kartu kelahiran. Dika menempelkan telapak kakinya yang sekarang di atas cap tinta itu: kakinya kini sudah tiga kali lebih besar! 'Lihat, Yah! Kakiku sudah tumbuh panjang seperti kaki kelinci!' seru Dika girang.",
                    "textEn": "Beside the photo was a blue ink stamp of baby Dika's footprint on a birth certificate card. Dika pressed his current foot over the ink mark: his foot was now three times bigger! 'Look, Dad! My feet grew big like a rabbit's!' Dika cheered.",
                    "quote": "Pertumbuhan tubuh adalah bukti nyata dari kasih sayang dan perawatan orang tua.",
                    "coReading": "Berapa kali lebih besar telapak kaki Dika sekarang dibanding saat bayi?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Dika placing his bare foot near the tiny ink footprint stamp in the open baby album. Father and Mother watching with wide happy smiles, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Foto Mandi Busa di Ember Plastik",
                    "titleEn": "Bubble Bath in the Plastic Tub",
                    "textId": "Halaman berikutnya menampilkan foto Dika saat berusia satu tahun, sedang mandi di ember plastik merah dengan gelembung busa sabun menempel di kepalanya seperti topi koki. Dika tertawa terpingkal-pingkal melihat wajah lucunya yang belepotan busa.",
                    "textEn": "The next page showed Dika at one year old, splashing in a red plastic tub with white soap suds piled on his head like a chef's hat. Dika burst into giggles at his silly, suds-covered baby face.",
                    "quote": "Tawa masa kecil adalah melodi abadi yang menghangatkan hari-hari keluarga.",
                    "coReading": "Apa yang menempel di kepala Dika pada foto mandi busa?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. The album page showing a funny photo of a baby splashing in a bubble bath with suds on head. Dika clutching his tummy laughing happily, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Langkah Tertatih Mengejar Bola",
                    "titleEn": "Toddling Steps Chasing the Ball",
                    "textId": "Ada juga foto saat Dika belajar berjalan di halaman rumput: kedua tangannya terangkat tinggi menjaga keseimbangan, mengejar bola sepak karet biru. Di belakang Dika dalam foto itu, tangan Ayah dan Ibu siap menangkap bila Dika terjatuh.",
                    "textEn": "There was also a photo of Dika learning to walk on the lawn: both arms raised high for balance, toddling after a blue rubber soccer ball. Behind Dika in the photo, Mother and Father's hands hovered ready to catch him if he tumbled.",
                    "quote": "Orang tua selalu menjadi pelindung yang tak kasat mata di setiap langkah pertama kita.",
                    "coReading": "Siapa yang selalu menjaga di belakang saat kamu belajar berjalan?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Album page displaying a photo of toddler Dika walking wobbly across green lawn towards a ball, parents kneeling behind him. Dika looking at the photo with a touched, loving face, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Pelukan Tiga Orang yang Hangat",
                    "titleEn": "A Warm Three-Way Embrace",
                    "textId": "Dika menutup album beludru itu perlahan dan menatap Ayah serta Ibunya. Dika melingkarkan kedua lengannya ke leher Ayah dan Ibu sekaligus: 'Terima kasih, Ayah dan Ibu, sudah merawat Dika dari sebesar semangka sampai bisa berlari kencang seperti sekarang.'",
                    "textEn": "Dika closed the velvet album softly and looked at Father and Mother. He wrapped both arms around their necks in a big warm hug: 'Thank you, Father and Mother, for loving and caring for me from when I was a watermelon until I can run fast today.'",
                    "quote": "Rasa syukur anak adalah mahkota paling mulia bagi perjuangan orang tua.",
                    "coReading": "Kata-kata manis apa yang diucapkan Dika kepada Ayah dan Ibunya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Dika hugging Father and Mother together in a tight, affectionate group embrace in the center of the rug. Blue velvet album closed beside them, warm glowing room light, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Menyimpan Kembali Harta Karun",
                    "titleEn": "Shelving the Treasure Once More",
                    "textId": "Ayah menggendong Dika untuk bersama-sama meletakkan album beludru biru itu kembali ke rak lemari kaca. Album itu kini menyimpan satu kenangan baru: sore hari yang penuh tawa hangat dan rasa syukur di antara mereka bertiga.",
                    "textEn": "Father lifted Dika onto his hip so they could place the blue velvet album back onto the glass cabinet shelf together. The album now held a fresh new memory: an afternoon brimming with shared laughter and gratitude.",
                    "quote": "Setiap hari yang dijalani bersama keluarga adalah halaman baru dalam buku cinta kita.",
                    "coReading": "Di mana album foto kenangan disimpan kembali?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Father carrying Dika as Dika gently slides the blue album back into the wooden glass cabinet. Mother smiling beside them, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Nyenyak Diselimuti Kasih Sayang",
                    "titleEn": "Sound Sleep Wrapped in Love",
                    "textId": "Malam tiba dan gerimis telah reda menyisakan udara sejuk beraroma tanah basah. Dika tidur lelap di bawah selimut kuning hangatnya, memeluk guling kapuk empuk. Di dalam mimpinya, ia melihat dirinya tumbuh semakin kuat dan berani di bawah tatapan penuh cinta kedua orang tuanya.",
                    "textEn": "Night arrived and the drizzle stopped, leaving cool, fresh earthy air. Dika slept deeply beneath his warm yellow quilt, hugging his soft bolster. In sweet dreams, he saw himself growing stronger and braver under the loving gaze of his parents.",
                    "quote": "Tidurlah dalam pelukan cinta abadi, hidupmu adalah anugerah terindah bagi keluargamu.",
                    "coReading": "Selamat tidur anak tersayang, kamu selalu dicintai sepenuh hati.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Dika sleeping peacefully in bed with a yellow quilt. On the wall hangs a small framed photo of baby Dika. Outside the window, a bright crescent moon and starry night sky. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 104: Menjemur Kasur di Bawah Mentari ---
        {
            "id": "story104",
            "storyNumber": 104,
            "title": "Menjemur Kasur di Bawah Mentari",
            "englishTitle": "Sun-Drying the Mattress Beneath the Sky",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menjaga kebersihan tempat tidur, aroma hangat matahari, & kebiasaan sehat keluarga",
            "cover": "covers/story104_cover.jpg",
            "synopsis": "Di hari yang cerah dengan matahari terik menyinari pekarangan, Adit membantu Ayah mengangkat kasur kapuk tebal ke atas jemuran bambu. Dengan sapu penebah lidi, Adit menepuk-nepuk kasur hingga debunya hilang dan kasur mengembang empuk beraroma sinar mentari yang segar.",
            "protagonist": "Adit (Anak laki-laki memegang penebah lidi)",
            "companion": "Ayah Adit (Ayah mengangkat kasur ke jemuran bambu)",
            "setting": "Halaman Terik Siang",
            "pages": [
                {
                    "number": 1,
                    "title": "Mentari Terik di Pekarangan Depan",
                    "titleEn": "Radiant Sunshine in the Front Yard",
                    "textId": "Matahari tengah hari bersinar terang benderang dari langit biru bersih tanpa awan. Angin hangat bertiup mengeringkan rumput dan daun-daun mangga. Ayah keluar dari kamar tidur sambil memikul kasur kapuk tebal bermotif garis-garis merah di pundaknya yang kokoh.",
                    "textEn": "The midday sun shone brilliantly from a cloudless azure sky. A warm breeze dried the grass and mango leaves. Father stepped out of the bedroom hauling a thick red-striped kapok mattress on his sturdy shoulders.",
                    "quote": "Sinar mentari adalah karunia alam yang membersihkan dan menyehatkan rumah kita.",
                    "coReading": "Pernahkah kamu melihat kasur dijemur di bawah terik matahari?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Father carrying a thick striped kapok mattress on his shoulder into a sunny green yard. Adit, an enthusiastic boy in shorts and t-shirt, trotting beside him carrying a woven reed beater, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Palang Bambu Kuning yang Kokoh",
                    "titleEn": "Sturdy Yellow Bamboo Drying Rack",
                    "textId": "Di tengah pekarangan berdiri dua tiang bambu kuning besar dengan palang horizontal yang kokoh. Bersama Adit yang memegangi ujung bawah kasur, Ayah membentangkan kasur kapuk itu di atas palang bambu. Kasur itu tergantung seperti perahu layar yang siap menyerap panas surya.",
                    "textEn": "In the center of the yard stood two sturdy bamboo poles with a strong horizontal rack. With Adit holding the lower edge, Father draped the kapok mattress over the bamboo bar. The mattress hung like a sail ready to soak up the sun's warmth.",
                    "quote": "Pekerjaan mengangkat beban berat terasa ringan saat dikerjakan bersama.",
                    "coReading": "Benda apa yang digunakan sebagai jemuran kasur di halaman?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Father and Adit draping the thick mattress over a tall bamboo outdoor clothesline rack in the sunny yard. Bright blue sky, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Penebah Lidi Beranyam Rotan",
                    "titleEn": "Palm-Leaf Beater Tied with Rattan",
                    "textId": "Ayah memberikan sebilah penebah kasur yang terbuat dari jalinan lidi kelapa tua bertangkai rotan. 'Ini senjatamu, Adit! Pukul kasur ini dengan irama yang rata agar debu di serat kapuk keluar dan kapuknya mengembang kembali seperti bantal awan.'",
                    "textEn": "Father handed over a mattress beater woven from mature palm-leaf ribs with a rattan handle. 'Here is your tool, Adit! Beat the mattress with an even rhythm so dust flies out and the cotton fluffs up like cloud cushions.'",
                    "quote": "Alat tradisional menyimpan kearifan sederhana yang sangat ampuh.",
                    "coReading": "Terbuat dari apakah alat penebah kasur yang dipegang Adit?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Close-up of Adit holding a woven flat palm-rib mattress beater, smiling excitedly with sleeves rolled up. Warm sunbeams around him, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Irama Ketukan: Buk, Buk, Buk!",
                    "titleEn": "Rhythmic Beats: Thump, Thump, Thump!",
                    "textId": "Dengan kedua tangannya, Adit mengayunkan penebah lidi menepuk permukaan kasur: 'Buk, buk, buk!' Suara tepukan itu berdentum mantap dan berirama. Dari serat kain kasur mengepul debu-debu halus yang seketika disapu bersih oleh hembusan angin terik.",
                    "textEn": "With both hands, Adit swung the reed beater against the mattress surface: 'Thump, thump, whack!' The solid rhythmic beat echoed cheerily. From the fabric fibers puffed tiny dust motes, immediately whisked away by the warm breeze.",
                    "quote": "Gerakan tubuh yang bertenaga memberi kesehatan bagi yang melakukannya.",
                    "coReading": "Bagaimana suara tepukan penebah lidi pada kasur?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Adit swinging the woven beater striking the suspended mattress, fine dust motes dancing in the bright sunbeams. Father smiling beside him with his own beater, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Ayah dan Anak Memukul Bergantian",
                    "titleEn": "Father and Son Taking Turns",
                    "textId": "Ayah memukul di sisi kiri, dan Adit memukul di sisi kanan: 'Buk-tak, buk-tak!' Mereka memukul kasur sambil bersenandung lagu riang. Butiran keringat menetes di pelipis Adit, tetapi tawanya berderai melihat kasur kapuk itu perlahan mengembang semakin gemuk.",
                    "textEn": "Father struck on the left, and Adit tapped on the right: 'Thump-whack, thump-whack!' They beat the mattress while humming a lively tune. Sweat dotted Adit's brow, but he giggled seeing the kapok mattress slowly puff up rounder and fatter.",
                    "quote": "Bekerja bersama mengubah tugas rumah tangga menjadi kenangan yang menyenangkan.",
                    "coReading": "Apakah kasur kapuk itu menjadi semakin empuk setelah ditepuk-tepuk?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Father and Adit beating the mattress together in tandem on the sunny lawn, laughter on their faces. Green garden bushes and mango tree in background, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Membalik Sisi di Tengah Hari",
                    "titleEn": "Flipping Sides at Midday",
                    "textId": "Tepat saat tengah hari, Ayah membantu membalik sisi kasur agar bagian bawahnya juga bermandikan terik matahari. Kain kasur terasa sangat hangat dan memancarkan wangi khas kapas yang dijemur di bawah langit terbuka.",
                    "textEn": "Right at high noon, Father helped flip the mattress so the other side bathed in hot sunlight too. The fabric felt wonderfully warm, radiating the sweet, distinct aroma of sun-baked natural cotton.",
                    "quote": "Keadilan perawatan memastikan setiap sudut mendapatkan kehangatan yang sama.",
                    "coReading": "Mengapa kasur harus dibalik saat dijemur?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Father flipping the thick mattress over the bamboo bar while Adit holds one side to steady it. Golden midday sun high in the blue sky, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Bantal dan Guling yang Ikut Berjemur",
                    "titleEn": "Pillows and Bolsters Basking Too",
                    "textId": "Adit menata bantal tidur dan guling kapuknya di atas tikar pandan yang terbentang di rumput kering. Semua bantalnya bermandikan sinar matahari, mengembang empuk seperti roti yang baru keluar dari pemanggang.",
                    "textEn": "Adit arranged his sleeping pillows and kapok bolsters on a pandan mat spread across the dry grass. All his pillows soaked in the sun, puffing up delightfully soft like freshly baked rolls.",
                    "quote": "Kebersihan menyeluruh memberi kenyamanan tidur yang tak tertandingi.",
                    "coReading": "Benda apa lagi yang dijemur Adit di atas tikar rumput?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A woven pandan mat on the grass with fluffy pillows and bolsters basking under the bright sun. Adit patting a bolster gently, smiling with bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Aroma Hangat Matahari",
                    "titleEn": "The Warm Scent of Sunshine",
                    "textId": "Sore hari ketika matahari mulai condong, Adit menempelkan pipinya ke permukaan kasur yang sudah hangat. 'Ayah, cium ini! Kasurnya berbau seperti matahari dan wangi padang rumput!' seru Adit takjub. Kasur itu kini begitu empuk, tebal, dan bebas dari rasa lembap.",
                    "textEn": "In the late afternoon as the sun softened, Adit pressed his cheek against the warm mattress. 'Dad, smell this! It smells like pure sunshine and sweet meadows!' Adit exclaimed in awe. The mattress was now plump, thick, and free of any dampness.",
                    "quote": "Aroma matahari adalah keharuman alami paling menenangkan bagi tidur manusia.",
                    "coReading": "Bagaimana aroma kasur sehabis dijemur seharian di bawah matahari?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Adit pressing his cheek happily against the warm puffy mattress, eyes closed in bliss, inhaling the fresh sunbaked scent. Father smiling warmly beside him, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Mengangkat Kasur Kembali ke Kamar",
                    "titleEn": "Carrying the Mattress Back Inside",
                    "textId": "Ayah dan Adit mengangkat kasur yang hangat dan empuk itu kembali ke ranjang kamar tidur. Ketika diletakkan di atas dipan kayu, kasur itu tampak mengembang dua kali lipat lebih tebal dibanding tadi pagi. Sprei katun bersih bermotif bintang segera dipasang rapi.",
                    "textEn": "Father and Adit carried the warm, fluffy mattress back to the bedroom bedstead. Resting on the wooden frame, the mattress looked twice as thick as it had this morning. A crisp cotton sheet with star patterns was smoothed over it.",
                    "quote": "Keringat yang dicurahkan siang hari berbuah kenyamanan di malam hari.",
                    "coReading": "Bagaimana bentuk kasur Adit setelah dipasang kembali di kamar?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Father and Adit laying the puffy mattress onto the wooden bedframe in the bedroom, fitting a clean star-patterned sheet. Bedroom window letting in evening glow, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tertidur di Atas Kasur Beraroma Mentari",
                    "titleEn": "Sleeping Upon the Sun-Scented Mattress",
                    "textId": "Malam tiba dan udara kamar tidur terasa sejuk dan damai. Begitu Adit merebahkan tubuhnya di kasur yang empuk dan hangat beraroma matahari, rasa kantuk yang nikmat langsung membuainya. Adit tertidur pulas dalam lelap yang sempurna, dipeluk kehangatan mentari siang yang tersimpan di dalam serat kapuknya.",
                    "textEn": "Night fell and the bedroom air felt cool and serene. The moment Adit sank into the warm, fluffy, sun-scented mattress, a delicious sleepiness enveloped him. Adit slept soundly in perfect rest, cradled by the sun's warmth woven deep into the cotton fibers.",
                    "quote": "Tidurlah dalam kehangatan murni, mentari siang menjaga lelapmu sepanjang malam.",
                    "coReading": "Mari pejamkan mata dan rasakan kehangatan kasur empukmu sebelum terlelap.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Adit sleeping peacefully in bed, sinking comfortably into the thick puffy mattress under a cozy quilt, smiling in deep slumber. Crescent moon and stars glowing outside the window, serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 105: Doa Bersama Menyapa Bintang ---
        {
            "id": "story105",
            "storyNumber": 105,
            "title": "Doa Bersama Menyapa Bintang",
            "englishTitle": "Praying Together Greeting the Stars",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Rasa syukur keluarga, doa pengantar tidur, & cinta kasih semesta",
            "cover": "covers/story105_cover.jpg",
            "synopsis": "Di malam penutup hari yang hening dan bertabur ribuan bintang perak di langit luas, seluruh keluarga—Ayah, Ibu, Kakak, dan Adik—berkumpul di dekat jendela besar kamar tidur. Mereka bergandengan tangan, memanjatkan doa syukur atas hari yang indah, dan menyapa bintang-bintang sebelum terlelap dalam pelukan kasih sayang abadi.",
            "protagonist": "Keluarga Bahagia (Seluruh keluarga bergandengan tangan berdoa)",
            "companion": "Jendela Malam (Langit malam berhias bulan dan bintang)",
            "setting": "Kamar Tidur Utama",
            "pages": [
                {
                    "number": 1,
                    "title": "Jendela Kamar yang Terbuka ke Langit Malam",
                    "titleEn": "The Bedroom Window Open to the Night Sky",
                    "textId": "Malam telah membungkus desa dengan selimut biru gelap yang tenang. Di kamar tidur utama rumah kayu, jendela besar terbuka ke arah perbukitan. Angin malam bertiup semilir membawa aroma harum bunga sedap malam dan kesunyian yang menyejukkan jiwa.",
                    "textEn": "Night wrapped the village in a peaceful navy-blue blanket. In the master bedroom of the wooden house, the wide window stood open to the hills. A gentle night breeze wafted the sweet fragrance of night-blooming tuberose and a quiet that soothed the soul.",
                    "quote": "Malam hari adalah waktu paling suci untuk mengistirahatkan raga dan pikiran.",
                    "coReading": "Pernahkah kamu memandang langit malam yang gelap dan berbintang bersama orang tuamu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. A cozy bedroom with a wide rustic wooden window looking out onto a dark velvet night sky sparkling with countless stars and a smiling crescent moon. Breezy white curtains, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Ribuan Bintang Perak yang Berkelip",
                    "titleEn": "Thousands of Twinkling Silver Stars",
                    "textId": "Di angkasa yang luas tanpa batas, ribuan bintang perak berkelip-kelip seperti taburan permata di atas kain beledu hitam. Bulan sabit bersinar terang dengan cahaya perak yang lembut, menerangi atap-atap rumah dan dahan pepohonan dengan cahaya damai.",
                    "textEn": "Across the boundless sky, thousands of silver stars twinkled like scattered diamonds upon black velvet. The crescent moon shone bright with gentle silvery light, bathing rooftops and tree boughs in peaceful radiance.",
                    "quote": "Bintang-bintang di langit selalu setia menemani malam anak-anak bumi.",
                    "coReading": "Bisakah kamu menunjuk bintang paling terang yang kamu lihat malam ini?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Breathtaking close-up view of the night sky through the window: deep indigo sky, glowing silver crescent moon, swirling constellations and twinkling golden-white stars. Naive folk art, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Lingkaran Tangan yang Saling Menggenggam",
                    "titleEn": "A Circle of Clasped Hands",
                    "textId": "Ayah, Ibu, Kakak, dan Adik berdiri melingkar di depan jendela. Mereka saling mengaitkan jemari tangan mereka erat-erat. Telapak tangan Ayah yang hangat, tangan Ibu yang lembut, dan tangan mungil anak-anak membentuk lingkaran cinta yang tak terputus.",
                    "textEn": "Father, Mother, Sister, and Brother stood in a circle before the open window. They clasped their fingers tightly together. Father's warm palm, Mother's soft touch, and the children's little hands formed an unbroken circle of love.",
                    "quote": "Genggaman tangan keluarga adalah benteng terkuat yang mengusir segala kecemasan.",
                    "coReading": "Genggamlah tangan orang di sampingmu sekarang sehangat lingkaran ini!",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. The family of four standing hand-in-hand in a gentle circle before the moonlit window, their silhouettes glowing with soft ambient light. Peaceful smiles, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Bisikan Syukur atas Hari yang Indah",
                    "titleEn": "Whispers of Gratitude for a Beautiful Day",
                    "textId": "Ayah memimpin doa dengan suara yang berat, tenang, dan berwibawa: 'Tuhan yang Maha Pengasih, terima kasih atas tawa yang telah kami bagi hari ini, atas rezeki makanan di meja makan, dan atas perlindungan yang menjaga kami sepanjang siang.'",
                    "textEn": "Father led the prayer in a voice deep, calm, and tender: 'Merciful Creator, we thank You for the laughter shared today, for the nourishing food upon our table, and for the grace that guided us through the day.'",
                    "quote": "Doa syukur adalah kunci pembuka ketenangan batin yang sejati.",
                    "coReading": "Hal baik apa yang paling kamu syukuri hari ini sebelum tidur?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Father leading the prayer with eyes closed peacefully, head bowed. Mother and children listening with solemn happy expressions under the moonbeams, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Doa Ibu untuk Anak-Anak Tersayang",
                    "titleEn": "Mother's Blessing for Her Beloved Children",
                    "textId": "Ibu menyambung doa dengan bisikan selembut desau angin: 'Berkahilah tidur putra-putri kami, jagalah mimpi-mimpi mereka dengan kebaikan, dan bangunkanlah kami esok hari dengan hati yang selalu penuh kasih bagi sesama.' Air mata syukur merebak di mata Ibu.",
                    "textEn": "Mother continued the prayer with a whisper as gentle as the breeze: 'Bless the sleep of our dear children, watch over their dreams with goodness, and awaken us tomorrow with hearts forever brimming with love.' Tears of gratitude shone in Mother's eyes.",
                    "quote": "Doa seorang ibu adalah sayap pelindung yang tak kasat mata di malam hari.",
                    "coReading": "Dengarkanlah doa ibumu yang selalu mengharapkan kebaikan bagimu.",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother whispering her blessing with hands clasped, tears of love glinting in the starlight. The two children leaning gently against her side, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Menyapa Bintang Kejora di Ufuk Timur",
                    "titleEn": "Greeting the Morning Star in the East",
                    "textId": "Adik kecil membuka matanya sedikit dan memandang bintang kejora yang bersinar paling terang di dekat bulan: 'Selamat malam, bintang yang baik! Bersinarlah terus menjaga langit kami!' Seluruh keluarga tersenyum mendengar kepolosan doa si kecil.",
                    "textEn": "Little brother fluttered his eyes open, gazing at the morning star shining brightest beside the moon: 'Goodnight, friendly star! Keep shining and guarding our sky!' The whole family smiled warmly at the little one's innocent greeting.",
                    "quote": "Kepolosan hati anak-anak menghubungkan bumi dengan keagungan semesta.",
                    "coReading": "Mari lambaikan tanganmu menyapa bintang-bintang di luar jendela!",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Little boy waving his small hand toward a bright glowing star in the night sky through the window. Family smiling tenderly, moonlight washing over them, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Kecupan Kening Pembawa Kedamaian",
                    "titleEn": "Forehead Kisses Bringing Peace",
                    "textId": "Selesai berdoa, Ayah dan Ibu mencium kening Kakak dan Adik satu per satu: 'Selamat tidur, belahan jiwa kami.' Kecupan hangat itu terasa seperti tetesan embun penyejuk yang menghapus segala rasa lelah dan kantuk yang tersisa.",
                    "textEn": "As prayer ended, Father and Mother kissed the foreheads of Sister and Brother one by one: 'Sleep sweet, our dearest treasures.' The warm kisses felt like soothing dew that dissolved every fatigue into blissful drowsiness.",
                    "quote": "Kecupan kasih sayang orang tua adalah segel rasa aman pengantar mimpi.",
                    "coReading": "Rasakan kecupan kasih sayang di keningmu sebelum kamu memejamkan mata.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Mother kissing her young daughter's forehead tenderly while Father kisses the little boy's hair. Deep emotional family warmth under starry night window, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Menutup Tirai Renda Putih Perlahan",
                    "titleEn": "Gently Drawing the White Lace Curtains",
                    "textId": "Ayah merapatkan tirai renda putih jendela perlahan. Angin malam yang sejuk masih bisa masuk melalui celah renda, tetapi udara kamar tetap hangat dan terlindung. Cahaya bulan membiaskan pola-pola bunga renda yang indah di atas lantai kayu.",
                    "textEn": "Father gently pulled the sheer white lace curtains closed. The cool night air still drifted through the lace weave, but the room remained snug and protected. Moonlight cast lovely floral lace patterns across the wooden floor.",
                    "quote": "Perlindungan yang lembut memberi rasa nyaman sepanjang malam.",
                    "coReading": "Bisakah kamu melihat bayangan renda yang terlukis oleh cahaya bulan?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Father pulling sheer white lace curtains closed, moonlight filtering through the floral lace casting intricate patterns on the floor. Children climbing into bed, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Selimut Kasih yang Menyelimuti Raga",
                    "titleEn": "The Quilt of Love Tucked Snug",
                    "textId": "Anak-anak naik ke ranjang mereka yang empuk dan harum mentari. Ayah dan Ibu menarik selimut tebal hingga ke dada mereka, menyelipkan sisinya dengan rapi. Seluruh ruangan diselimuti oleh keheningan yang agung dan rasa damai yang sempurna.",
                    "textEn": "The children tucked into their soft, sun-scented bed. Father and Mother pulled the thick quilt up to their chests, tucking the edges snug. The entire room was wrapped in majestic quiet and perfect, tranquil peace.",
                    "quote": "Di dalam rumah yang penuh cinta, setiap malam adalah pelukan yang abadi.",
                    "coReading": "Tarik selimutmu rapat-rapat, biarkan tubuhmu merasa hangat dan aman.",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Both children tucked comfortably under a warm quilt in their cozy bed, smiling serenely. Father and Mother sitting on the bedside stroking their blankets, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Lelap Abadi dalam Dekapan Semesta",
                    "titleEn": "Eternal Slumber in the Embrace of the Universe",
                    "textId": "Lampu kamar dipadamkan menyisakan temaram lembut cahaya bintang yang menembus tirai. Seluruh napas di dalam rumah berhembus teratur dan tenang. Semua anak tertidur pulas dalam lelap yang bahagia, bermimpi tentang hari esok yang penuh cinta di bumi yang indah ini. Selamat tidur, anak-anak manis Kisah Krayon.",
                    "textEn": "The room lamp clicked off, leaving only the soft starlight filtering through the lace. Every breath in the home flowed steady and calm. All children slept deeply in blissful rest, dreaming of a tomorrow brimming with love on this beautiful earth. Sleep well, sweet children of Kisah Krayon.",
                    "quote": "Tidurlah dalam damai abadi, semesta dan keluargamu selalu menjagamu dalam cinta selamanya.",
                    "coReading": "Selamat malam, pejamkan matamu dan tidurlah dengan nyenyak sampai pagi tiba.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. The whole family sleeping peacefully in their cozy home, children tucked in bed, soft moonlight through lace curtains. Deep velvety indigo starry sky outside with glowing crescent moon and shooting star. The ultimate peaceful bedtime lullaby scene, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
