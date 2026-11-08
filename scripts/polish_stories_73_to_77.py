# scripts/polish_stories_73_to_77.py
import json

def get_stories_73_to_77():
    stories = [
        # --- STORY 73: Langkah Pelan di Rumah Rusa ---
        {
            "id": "story73",
            "storyNumber": 73,
            "title": "Langkah Pelan di Rumah Rusa",
            "englishTitle": "Quiet Steps in the Deer's Home",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menghormati habitat satwa liar & ketenangan di alam bebas",
            "cover": "covers/story73_cover.jpg",
            "synopsis": "Sena diajak Ayah berjalan menyusuri hutan pinus berkabut. Di sana, Sena belajar melangkah seringan bulu dan menahan suara agar tidak mengejutkan induk rusa tutul yang sedang menyusui bayinya di balik semak pakis.",
            "protagonist": "Sena (Anak penjelajah berompong hijau lumut)",
            "companion": "Induk Rusa & Bayi (Rusa tutul menyusui anaknya)",
            "setting": "Hutan Lindung Pinus",
            "pages": [
                {
                    "number": 1,
                    "title": "Kabut Pagi di Hutan Pinus",
                    "titleEn": "Morning Mist in the Pine Forest",
                    "textId": "Udara dingin menusuk lembut saat Sena dan Ayah melangkah memasuki hutan lindung pinus. Pohon-pohon pinus menjulang tinggi seperti tiang-tiang raksasa yang menyangga langit. Di tanah berbukit, jarum-jarum pinus cokelat membentuk hamparan karpet alami yang empuk meredam setiap derap langkah.",
                    "textEn": "The chilly air bit gently as Sena and Dad stepped into the protected pine forest. Pine trees towered high like giant pillars holding up the sky. On the rolling ground, brown pine needles formed a soft natural carpet, muffling every footstep.",
                    "quote": "Hutan adalah rumah bagi ribuan jiwa yang menyukai ketenangan.",
                    "coReading": "Pernahkah kamu mencium aroma segar daun pinus di pegunungan?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on textured cream watercolor paper. Sena, a young explorer in a moss-green quilted vest and warm knit cap, holding Dad's hand walking through a misty pine forest. Sunbeams slanting through tall pine trees, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Aturan Emas Para Penjelajah",
                    "titleEn": "The Golden Rule of Explorers",
                    "textId": "Ayah menempelkan jari telunjuknya ke bibir sambil berbisik lembut. 'Sena, saat memasuki rumah satwa, kita adalah tamu yang sopan. Berjalanlah seringan angin dan jangan mematahkan ranting kering agar penghuni hutan tidak merasa terancam.'",
                    "textEn": "Dad pressed his index finger to his lips, whispering softly. 'Sena, when entering animal homes, we are polite guests. Walk as light as the breeze and avoid snapping dry twigs so forest creatures do not feel startled.'",
                    "quote": "Ketenangan adalah bentuk penghormatan tertinggi kepada alam.",
                    "coReading": "Bisakah kamu berjalan berjingkat tanpa menimbulkan suara?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Dad crouching down whispering to Sena with finger to lips in a gentle 'shh' gesture. Pine trees and green ferns all around, soft morning light, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Langkah Kaki Seringan Bulu",
                    "titleEn": "Steps Light as Feathers",
                    "textId": "Sena mempraktikkan petunjuk Ayah dengan penuh kesungguhan. Ia mendaratkan ujung sepatunya perlahan, menghindari kerikil lepas dan dahan kering. Sena merasa dirinya seperti tupai mungil yang meluncur anggun di atas dedaunan tanpa meninggalkan jejak bunyi.",
                    "textEn": "Sena practiced Dad's advice with earnest care. He placed his boot toes down slowly, steering clear of loose pebbles and brittle branches. Sena felt like a little squirrel gliding gracefully over the fallen leaves without making a sound.",
                    "quote": "Kehati-hatian adalah buah dari rasa peduli yang mendalam.",
                    "coReading": "Bagaimana caramu melangkah saat tidak ingin membangunkan orang yang tidur?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Sena tiptoeing carefully on a path covered with soft pine needles and green moss, arms balanced out gently. Sunlight creating golden patches on the forest floor, bead dot eyes, 4 limbs, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Kilasan Tutul di Balik Pakis",
                    "titleEn": "Spotted Glimpse Behind the Ferns",
                    "textId": "Di balik rerimbunan tanaman pakis raksasa yang berembun, daun-daun bergerak perlahan. Sena menghentikan langkahnya seketika. Di sana, tampak sepasang telinga oval berbulu halus bergerak memutar, mendeteksi hembusan angin.",
                    "textEn": "Behind a thick grove of dew-kissed giant ferns, fronds rustled softly. Sena froze in place instantly. There, a pair of soft oval furry ears twitched, scanning the forest breeze.",
                    "quote": "Bila kita diam, mata dan telinga kita akan menangkap keajaiban tersembunyi.",
                    "coReading": "Telinga hewan apakah yang menyembul di balik daun pakis?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Lush giant green ferns with morning dewdrops, and subtle deer ears poking out between fronds. Sena watching in still wonder from behind a tree trunk, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Induk Rusa dan Bayi Mungil",
                    "titleEn": "Mother Deer and Spotted Fawn",
                    "textId": "Kabut tipis terangkat perlahan ditiup angin. Sena terperangah menatap pemandangan di hadapannya: seekor induk rusa tutul bermata jernih sedang berdiri tenang, sementara bayi rusa mungil bertubuh bintik-bintik putih sedang menyusu dengan damai di sampingnya.",
                    "textEn": "The thin mist lifted gently in the breeze. Sena gasped silently at the sight before him: a spotted mother deer with clear, gentle eyes stood peacefully, while a tiny fawn with white spots nursed quietly by her side.",
                    "quote": "Kasih sayang seorang ibu adalah bahasa abadi di setiap sudut bumi.",
                    "coReading": "Lihatlah bintik-bintik putih di punggung bayi rusa, cantik sekali ya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. A graceful mother spotted deer standing tenderly beside her nursing tiny fawn among forest ferns. Soft golden sunbeams filtering through pine canopy, simple black bead dot eyes, strictly 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Tatapan Mata yang Lembut",
                    "titleEn": "A Gentle Exchange of Glances",
                    "textId": "Induk rusa itu menoleh perlahan ke arah Sena. Mata hitamnya yang bulat menatap lurus ke dalam mata Sena. Karena Sena berdiri tenang tanpa bergerak dan tanpa suara, induk rusa itu tidak panik. Ia mengendus udara, lalu melanjutkan menjilati kepala anaknya dengan penuh kasih.",
                    "textEn": "The mother deer turned her head slowly toward Sena. Her round, gentle black eyes met Sena's. Because Sena stood completely still and quiet, the mother did not flee. She sniffed the air, then continued grooming her baby's head with tender affection.",
                    "quote": "Kepercayaan lahir ketika kita tidak membawa rasa takut maupun bahaya.",
                    "coReading": "Mengapa induk rusa tidak lari ketakutan melihat Sena?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Close-up of the mother deer's gentle face with simple bead dot eyes looking calmly toward Sena who stands motionless with a warm gentle smile. Peaceful forest mood, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Detak Jantung yang Penuh Syukur",
                    "titleEn": "A Heart Beating with Gratitude",
                    "textId": "Dada Sena berdegup kencang, bukan karena takut, melainkan karena rasa takjub yang luar biasa. Ia merasa sangat beruntung diizinkan menyaksikan momen suci kehidupan di alam liar tanpa merusak kedamaian mereka sedikit pun.",
                    "textEn": "Sena's chest thudded, not out of fear, but from overwhelming wonder. He felt so blessed to be welcomed into this sacred wild moment without disturbing their peace in the slightest.",
                    "quote": "Menyaksikan keindahan tanpa merusaknya adalah anugerah terbesar manusia.",
                    "coReading": "Pernahkah kamu merasakan kekaguman yang membuatmu terdiam?",
                    "imagePrompt": "Handcrafted oil pastel and wax crayon. Sena with hands pressed lightly to his chest, eyes glowing with quiet awe. Pine forest setting, golden light patches, naive storybook style, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Langkah Mundur yang Hati-Hati",
                    "titleEn": "Careful Steps Backward",
                    "textId": "Setelah beberapa menit menikmati pemandangan itu, Ayah memberi isyarat untuk kembali. Sena melangkah mundur perlahan selangkah demi selangkah, tetap menjaga keheningan. Bayi rusa itu kini meringkuk tidur di atas tumpukan daun pakis yang kering dan hangat.",
                    "textEn": "After a few minutes of cherishing the sight, Dad signaled it was time to leave. Sena took slow, quiet steps backward one by one, keeping the silence unbroken. The little fawn was now curled up asleep on a dry bed of warm ferns.",
                    "quote": "Tahu kapan harus pamit adalah bagian dari rasa hormat kepada tuan rumah.",
                    "coReading": "Mengapa Sena dan Ayah memilih mundur perlahan?",
                    "imagePrompt": "Wax crayon drawing on textured paper. Sena and Dad slowly walking backward along the pine trail, looking back fondly at the resting deer family in the distance. Dappled forest shadows, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Pesan dari Hutan Pinus",
                    "titleEn": "The Message of the Pine Forest",
                    "textId": "Saat tiba kembali di batas hutan, Sena menatap puncak-puncak pohon pinus yang melambai ditiup angin sore. 'Ayah, hutan tadi begitu damai karena kita tidak membuat keributan,' kata Sena. Ayah mengangguk, 'Dunia akan selalu ramah pada anak yang tahu menjaga ketenangan.'",
                    "textEn": "Reaching the forest boundary once more, Sena gazed at the pine treetops swaying in the evening breeze. 'Dad, the forest was so peaceful because we didn't make a racket,' said Sena. Dad nodded, 'The world will always be gentle to children who honor its quiet.'",
                    "quote": "Kedamaian yang kita bawa keluar akan tercermin kembali pada diri kita.",
                    "coReading": "Pelajaran apa yang didapat Sena dari penjelajahan hari ini?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Sena and Dad standing on a scenic hillside overlooking the vast evergreen pine forest bathed in amber late afternoon light. Warm smiles, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Tenang Bersama Bayi Rusa",
                    "titleEn": "Resting Peaceful with the Little Fawn",
                    "textId": "Malam tiba menyelimuti pondok kayu Sena di lereng bukit. Saat Sena merebahkan tubuhnya di ranjang yang empuk, ia membayangkan bayi rusa tutul yang sedang tidur lelap di bawah naungan pohon pinus di tengah hutan. Sena memejamkan mata dan tertidur pulas dalam pelukan malam.",
                    "textEn": "Night enveloped Sena's wooden cabin on the hillside. As Sena nestled into his soft bed, he pictured the spotted fawn sleeping soundly beneath pine branches in the deep woods. Sena closed his eyes, drifting into deep sleep in the night's warm embrace.",
                    "quote": "Tidurlah dalam hening yang damai, semesta menjaga tidur semua anak bumi.",
                    "coReading": "Mari pejamkan mata dan bayangkan kamu tidur lelap di hutan pinus yang tenang.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Sena sleeping soundly in cozy cabin bed with a green woolen blanket. Above, soft dream cloud showing the cute baby fawn sleeping nestled by mother deer under twinkling night stars and crescent moon. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 74: Pohon Cemara Penahan Angin Pantai ---
        {
            "id": "story74",
            "storyNumber": 74,
            "title": "Pohon Cemara Penahan Angin Pantai",
            "englishTitle": "Pine Trees Guarding the Coastal Breeze",
            "category": "nature",
            "categoryLabel": "🌿 Cinta Alam & Lingkungan",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menjaga pesisir dari abrasi & ketekunan menanam pohon pelindung",
            "cover": "covers/story74_cover.jpg",
            "synopsis": "Di pesisir pantai berpasir putih, angin kencang sering menerbangkan pasir asin ke perkampungan nelayan. Joko bersama kakeknya menanam barisan bibit cemara laut berjarum halus di sepanjang garis pantai untuk menjadi benteng hijau pelindung desa.",
            "protagonist": "Joko (Anak pesisir berkulit sawo matang)",
            "companion": "Bibit Cemara (Bibit pohon cemara kecil bergoyang)",
            "setting": "Bibit Pasir Pantai",
            "pages": [
                {
                    "number": 1,
                    "title": "Hembusan Angin Asin",
                    "titleEn": "Gusts of Salty Wind",
                    "textId": "Di tepi pantai selatan, ombak putih bergulung memecah di atas pasir kelabu. Angin laut bertiup kencang membawa butiran pasir asin yang menusuk pipi dan mengotori teras rumah panggung para nelayan. Joko, anak pesisir bertopi anyaman pandan, menyipitkan matanya menahan debu pasir.",
                    "textEn": "On the southern coast, white waves rolled crashing upon grey sands. The sea gale blew fiercely, carrying salty sand grains that stung cheeks and coated the porch floors of fishermen stilt-houses. Joko, a coastal boy in a woven pandan hat, squinted against the sand dust.",
                    "quote": "Kekuatan alam yang keras mengajarkan manusia untuk mencari perlindungan yang bijak.",
                    "coReading": "Pernahkah kamu merasakan angin kencang di tepi pantai?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Joko, a young coastal boy in shorts and a woven sunhat, standing on a windy beach with palm trees in the distance. Rolling ocean waves, gusty breeze blowing his clothes, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Keranjang Bambu Penuh Bibit",
                    "titleEn": "Bamboo Basket of Saplings",
                    "textId": "Kakek memikul dua keranjang anyaman bambu yang penuh dengan bibit cemara laut berbatang lentur setinggi lutut. Daun-daun cemara itu tidak lebar, melainkan berupa jarum-jarum hijau halus yang saling mengunci rapat. 'Ini calon benteng pelindung desa kita, Joko,' kata Kakek.",
                    "textEn": "Grandpa carried two woven bamboo baskets filled with knee-high sea pine saplings with flexible slender stems. Their leaves were not broad, but fine green needles knitted tightly together. 'These are the future green shields of our village, Joko,' said Grandpa.",
                    "quote": "Sebuah pohon kecil menyimpan kekuatan untuk menahan badai besar di masa depan.",
                    "coReading": "Mengapa daun cemara laut berbentuk jarum halus?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Grandpa carrying woven bamboo panniers balanced on a shoulder pole, brimming with young green sea pine saplings in polybags. Coastal beach setting, sunny day, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Menggali Lubang di Pasir Lembap",
                    "titleEn": "Digging Holes in Damp Sand",
                    "textId": "Di sepanjang garis batas pasang surut, Joko dan Kakek mulai menggali lubang-lubang sedalam siku tangan. Pasir di bagian dalam terasa lembap dan sejuk. Joko mencampurkan segenggam pupuk kandang dan sabut kelapa untuk menjaga kelembapan akar bibit baru.",
                    "textEn": "Along the high-tide line, Joko and Grandpa dug elbow-deep holes in the sand. Deeper down, the sand felt cool and moist. Joko mixed in a handful of organic compost and coconut coir to help the young roots hold moisture.",
                    "quote": "Persiapan yang matang memberi fondasi kokoh bagi pertumbuhan yang sehat.",
                    "coReading": "Mengapa pasir diberi sabut kelapa dan pupuk sebelum ditanami?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Joko kneeling on the sandy beach with a small wooden spade digging a planting hole, while Grandpa sets down a pine sapling. Ocean shoreline in background, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Menanam Bibit Pertama",
                    "titleEn": "Planting the Very First Sapling",
                    "textId": "Dengan hati-hati, Joko merobek plastik pembungkus bibit tanpa merusak tanah padat di sekitar akarnya. Ia menurunkan bibit cemara ke dalam lubang pasir dan menimbunnya kembali. Joko menepuk-nepuk pasir di sekitar pangkal batang hingga bibit berdiri tegak dan kokoh.",
                    "textEn": "Carefully, Joko slid off the seedling bag without disturbing the soil ball around the roots. He lowered the sea pine into the sand hole and packed it firmly. Joko patted the damp sand around the base until the sapling stood upright and steady.",
                    "quote": "Sentuhan tangan yang lembut menumbuhkan rasa percaya diri pada kehidupan baru.",
                    "coReading": "Bisakah kamu menepuk-nepuk tanah seperti Joko merapikan tanaman?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Joko patting down damp sand around the base of a slender green sea pine sapling. His face smiling with tender pride, coastal breeze, simple bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Pagar Bambu Pelindung Ombak",
                    "titleEn": "Bamboo Guard Against Ocean Swells",
                    "textId": "Agar bibit tidak roboh diterpa angin pantai yang dahsyat, Kakek menancapkan bilah-bilah bambu di sekeliling setiap bibit dan mengikat batangnya dengan tali rami yang longgar. 'Sekarang angin kencang tidak akan bisa menumbangkannya,' senyum Kakek.",
                    "textEn": "To keep the young saplings from toppling in fierce ocean gales, Grandpa staked bamboo splints around each one, tying the stem loosely with hemp twine. 'Now strong winds cannot knock them down,' Grandpa smiled.",
                    "quote": "Bantuan pelindung diperlukan saat kita masih muda dan sedang bertumbuh.",
                    "coReading": "Mengapa bibit kecil perlu diberi tiang bambu penopang?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Grandpa tying a bamboo support stake beside the little pine sapling with natural cord. Joko holding the water bucket, coastal sea breeze blowing softly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Barisan Pasukan Hijau",
                    "titleEn": "The Green Guard Line",
                    "textId": "Sepanjang siang hingga matahari bergeser ke barat, Joko dan Kakek berhasil menanam tiga puluh bibit cemara laut berbaris rapi. Dari kejauhan, bibit-bibit itu tampak seperti barisan prajurit kecil berpakaian hijau yang siap menjaga perkampungan nelayan.",
                    "textEn": "Throughout the afternoon until the sun dipped westward, Joko and Grandpa planted thirty sea pine saplings in a neat row. From afar, the saplings looked like a company of tiny green soldiers ready to protect the fishing hamlet.",
                    "quote": "Ketekunan melahirkan karya besar yang melindungi banyak orang.",
                    "coReading": "Berapa banyak bibit cemara yang berhasil ditanam hari ini?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. A neat, rhythmic line of young pine saplings stretching along the sandy beach coastline. Joko and Grandpa sitting on a driftwood log resting happily with ocean waves rolling in, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Menyerap Air Payau",
                    "titleEn": "Thriving on Salty Mists",
                    "textId": "Bulan berganti bulan. Bibit-bibit cemara laut itu menunjukkan kehebatannya. Akarnya menjalar dalam ke bawah pasir, mencengkeram butiran pantai agar tidak tergerus abrasi ombak. Daun jarumnya menyaring butiran garam tanpa pernah mengering layu.",
                    "textEn": "Months turned into seasons. The sea pines showed their incredible strength. Their roots plunged deep into the sand, gripping the shoreline tight against wave erosion. Their needle leaves filtered sea spray without ever withering.",
                    "quote": "Ketahanan diri tumbuh dari kemampuan beradaptasi dengan lingkungan sekitar.",
                    "coReading": "Bagaimana akar pohon cemara membantu pantai tidak terkikis ombak?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A healthy growing sea pine tree on the sandy beach, sturdy trunk, vibrant green needle foliage fluttering in sea wind, waves crashing gently nearby. Naive folk art, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Hutan Hijau Penepis Badai",
                    "titleEn": "Green Canopy Taming the Storm",
                    "textId": "Tiga tahun kemudian, bibit-bibit kecil itu telah tumbuh menjadi pohon-pohon rimbun setinggi atap rumah. Ketika badai barat daya melanda, barisan cemara laut menahan hempasan angin kencang sehingga udara yang sampai ke perkampungan menjadi semilir lembut yang sejuk.",
                    "textEn": "Three years later, the little saplings had grown into lush, towering trees as high as house roofs. When southwest gales roared, the row of sea pines buffered the fierce gusts, turning the wind into a gentle, cool breeze across the village.",
                    "quote": "Pohon yang ditanam hari ini adalah keteduhan bagi hari esok.",
                    "coReading": "Bagaimana keadaan desa setelah pohon cemara tumbuh besar?",
                    "imagePrompt": "Warm oil pastel illustration on heavy cream paper. Tall flourishing coastal pine trees creating a lush windbreak along the sandy beach. Coastal village stilt houses sitting peacefully behind the green trees, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Desir Merdu Nyanyian Cemara",
                    "titleEn": "The Soft Whistle of the Sea Pines",
                    "textId": "Joko duduk di bawah naungan cemara laut yang rindang. Ketika angin laut bertiup melintasi ribuan jarum cemara, terdengar suara desau merdu 'Syuuur... syuuur...' seperti nyanyian lagu tidur yang menenangkan ombak di lautan.",
                    "textEn": "Joko sat beneath the breezy shade of the lush sea pines. As the sea breeze swept through thousands of pine needles, a soft whispering melody sighed, 'Huuush... huuush...' like a gentle lullaby soothing the ocean swells.",
                    "quote": "Ketenangan alam adalah nyanyian termerdu bagi jiwa yang bersyukur.",
                    "coReading": "Bisakah kamu menirukan suara desau angin di sela daun cemara?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Joko sitting peacefully under the shade of a majestic sea pine tree on the sandy shore, watching seagulls glide over ocean waves. Golden sunset glow, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Tenang Dihibur Nyanyian Ombak",
                    "titleEn": "Peaceful Sleep Soothed by the Waves",
                    "textId": "Malam tiba dan lampu perahu nelayan berkelip di kejauhan horizon laut. Di kamarnya yang sejuk tanpa debu pasir, Joko tertidur pulas beralaskan selimut tenun. Di luar sana, barisan cemara laut berdiri tegak menjaga desanya dalam lelap yang aman dan tenteram.",
                    "textEn": "Night fell and lantern lights on fishing boats flickered along the far sea horizon. In his breezy room free of gritty sand, Joko slept deeply on a woven blanket. Outside, the row of sea pines stood tall, guarding the sleeping village in safe and quiet comfort.",
                    "quote": "Tidurlah dalam damai, keteduhan pohon-pohon penjaga mengawal mimpimu.",
                    "coReading": "Selamat tidur anak pesisir, biarkan deburan ombak membawamu ke mimpi indah.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Joko sleeping peacefully in bed by an open window overlooking the silhouettes of tall coastal pines against a moonlit ocean and starry night sky. Serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 75: Vas Dandelion dari Botol Kaca ---
        {
            "id": "story75",
            "storyNumber": 75,
            "title": "Vas Dandelion dari Botol Kaca",
            "englishTitle": "Dandelion Vase from a Glass Bottle",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Daur ulang kreatif, mempercantik rumah, & melihat keindahan sederhana",
            "cover": "covers/story75_cover.jpg",
            "synopsis": "Tia menemukan botol sirup kaca bekas yang teronggok di sudut dapur. Alih-alih dibuang ke keranjang sampah, Tia membersihkannya, melilitnya dengan benang rami berwarna-warni, dan mengisinya dengan bunga dandelion liar sebagai hiasan meja makan keluarga.",
            "protagonist": "Tia (Gadis kreatif berpita rambut)",
            "companion": "Keluarga Tia (Meja makan berhias bunga liar)",
            "setting": "Meja Ruang Tamu",
            "pages": [
                {
                    "number": 1,
                    "title": "Botol Kaca Bening yang Terlupa",
                    "titleEn": "The Forgotten Clear Glass Bottle",
                    "textId": "Di sudut meja dapur kayu, tergeletak sebuah botol sirup kaca bening kosong yang label kertasnya sudah robek separuh. Ibu hendak memasukkannya ke dalam karung sampah daur ulang, tetapi Tia, gadis kecil berpita rambut kuning cerah, melihat bentuk botol itu yang mungil dan anggun.",
                    "textEn": "In the corner of the wooden kitchen counter lay an empty clear glass syrup bottle with its paper label half peeled off. Mother was about to toss it into the recycling sack, but Tia, a little girl with a bright yellow hair ribbon, noticed its charming, graceful shape.",
                    "quote": "Mata yang kreatif melihat keindahan baru pada benda-benda yang terabaikan.",
                    "coReading": "Pernahkah kamu melihat botol kaca kosong di dapur rumahmu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Tia, a sweet girl with a yellow hair ribbon and polka-dot apron, holding up a clean clear glass bottle looking at it thoughtfully with black bead dot eyes. Cozy kitchen setting, simple 4 limbs, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Mandi Sabun yang Berbusa",
                    "titleEn": "A Foamy Bubble Bath",
                    "textId": "Tia meminta izin Ibu untuk mencuci botol itu. Di wastafel, Tia merendam botol kaca dalam air hangat berbusa sabun lemon. Dengan spons lembut, ia menggosok sisa lem perekat hingga botol kaca itu berkilau jernih seperti kristal air di bawah sinar jendela.",
                    "textEn": "Tia asked Mother's permission to wash the bottle. In the sink, she soaked the glass in warm water full of bubbly lemon soap. With a soft sponge, she scrubbed away the sticky label residue until the glass bottle sparkled crystal clear beneath the window light.",
                    "quote": "Kebersihan mengubah hal biasa menjadi awal karya yang berharga.",
                    "coReading": "Apakah kamu suka bermain busa sabun saat mencuci barang?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Tia washing the glass bottle in a kitchen sink full of white fluffy bubbles. Sparkling water droplets, bright sunny window, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Lilitan Benang Wol Warna-Warni",
                    "titleEn": "Twisting of Colorful Woolen Yarn",
                    "textId": "Tia membawa botol yang sudah kering ke meja kerjanya. Dari kotak kerajinan Nenek, Tia mengambil sisa benang wol warna hijau mint, kuning jagung, dan jingga madu. Tia mulai melilitkan benang wol rapat-rapat dari leher botol hingga ke dasarnya.",
                    "textEn": "Tia brought the dried bottle to her craft table. From Grandma's craft box, Tia gathered leftover yarn scraps in mint green, corn yellow, and honey orange. Tia began winding the yarn neatly and tightly from the bottle's neck down to its base.",
                    "quote": "Kombinasi warna yang ceria menghangatkan suasana setiap sudut rumah.",
                    "coReading": "Warna apa saja yang dipilih Tia untuk melilit botolnya?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Tia sitting at a wooden table wrapping colorful strands of yarn around the glass bottle. Colorful balls of yarn in a basket, focused happy expression, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Pita Kancing Bunga",
                    "titleEn": "Flower Button Ribbon",
                    "textId": "Di bagian tengah lilitan benang, Tia menempelkan sebutir kancing kayu berbentuk bunga melati putih dengan lem kanji. Botol bekas yang tadinya dingin dan polos kini tampak hangat dan manis seperti vas antik dari negeri dongeng.",
                    "textEn": "At the center of the yarn wraps, Tia affixed a small wooden button shaped like a white jasmine flower using craft glue. The plain, cold bottle now looked warm and darling, like a fairy-tale vintage vase.",
                    "quote": "Sentuhan kecil yang tepat mampu melahirkan kepribadian yang menawan.",
                    "coReading": "Bisakah kamu melihat kancing kayu bunga di tengah botol?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Close-up of the decorated glass bottle wrapped in pastel stripes of yarn with a cute carved wooden flower button in the center. Cozy craft room setting, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Perjalanan ke Padang Rumput Liar",
                    "titleEn": "Trip to the Wild Meadow",
                    "textId": "Sore hari yang teduh, Tia berlari ke padang rumput di tepi bukit. Di sana bermekaran ratusan bunga dandelion kuning cerah dan dandelion putih yang siap meniupkan payung-payung parasut mungilnya ke angkasa.",
                    "textEn": "In the gentle late afternoon, Tia ran to the grassy meadow on the hillside. Hundreds of bright yellow dandelions and fluffy white seed globes bloomed there, ready to send their tiny parachute seeds sailing into the sky.",
                    "quote": "Keindahan sejati sering kali tumbuh liar di tanah yang sederhana.",
                    "coReading": "Apakah kamu pernah meniup bunga dandelion putih berbulu kapas?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Tia running through a lush green meadow filled with blooming yellow dandelions and fluffy white seed heads under warm afternoon light. Yellow hair ribbon dancing in breeze, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Memetik Tangkai-Tangkai Pilihan",
                    "titleEn": "Picking the Choicest Stems",
                    "textId": "Dengan lembut, Tia memetik lima tangkai dandelion kuning mekar dan tiga tangkai dandelion putih berbulu kapas. Ia juga memetik beberapa helai rumput ilalang berbulu halus untuk melengkapi buket bunganya.",
                    "textEn": "Gently, Tia snipped five blooming yellow dandelion stems and three fluffy white seed globes. She also plucked a few sprigs of feathery wild grass to complete her natural bouquet.",
                    "quote": "Mengambil secukupnya adalah tanda rasa hormat pada kelestarian alam.",
                    "coReading": "Berapa banyak bunga dandelion yang dipetik Tia?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Tia kneeling gently in the grass holding a small hand bouquet of yellow dandelions and white fluffy globes with wild grass. Sunset colors casting a golden glow, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Segelas Air Segar dari Gentong",
                    "titleEn": "A Glass of Fresh Well Water",
                    "textId": "Sesampainya di rumah, Tia mengisi separuh botol berhiasnya dengan air gentong tanah liat yang sejuk. Ia menata tangkai bunga satu per satu dengan ketinggian berbeda agar tampak alami dan seimbang.",
                    "textEn": "Back home, Tia filled half of her decorated bottle with cool water from the clay jar. She arranged the flower stems one by one at varied heights so they looked balanced and delightfully natural.",
                    "quote": "Keseimbangan dalam penataan memberi ketenangan pada mata yang memandang.",
                    "coReading": "Mengapa vas bunga harus diisi air segar?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Tia arranging yellow and white dandelions into the colorful yarn-wrapped bottle vase on the kitchen counter. Fresh water glinting inside, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Hiasan Meja Makan Keluarga",
                    "titleEn": "Centerpiece for the Family Table",
                    "textId": "Tia meletakkan vas kreasinya tepat di tengah meja makan berbalut taplak kain perca. Ketika Ayah, Ibu, dan Kakak duduk untuk makan malam, mereka tertegun menatap keindahan vas bunga buatan tangan Tia. Ruang makan terasa mendadak hangat dan bercahaya.",
                    "textEn": "Tia placed her newly made vase right in the center of the dining table covered in a patchwork cloth. When Dad, Mom, and Brother sat down for dinner, they paused in delightful surprise at Tia's handmade vase. The dining room instantly felt warm and glowing.",
                    "quote": "Karya yang dibuat dengan cinta membawa kebahagiaan bagi seluruh keluarga.",
                    "coReading": "Bagaimana reaksi keluarga Tia saat melihat vas bunga di meja makan?",
                    "imagePrompt": "Handcrafted oil pastel and wax crayon on cream paper. The cozy family gathered around the wooden dining table set with warm soup bowls, admiring the charming handmade dandelion vase in the center. Smiling faces with simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Pujian Hangat dari Ibu",
                    "titleEn": "Warm Compliments from Mother",
                    "textId": "Ibu memeluk Tia erat-erat. 'Botol sirup ini tadinya sampah, Tia. Namun di tanganmu, ia menjadi barang terindah di rumah kita malam ini.' Ayah mengangguk bangga sambil mencium kening putri kecilnya.",
                    "textEn": "Mother wrapped Tia in a tight hug. 'This syrup bottle was once trash, Tia. But in your hands, it has become the loveliest thing in our home tonight.' Dad nodded with pride, kissing his little daughter's forehead.",
                    "quote": "Apresiasi dari orang tua adalah pupuk paling subur bagi kreativitas anak.",
                    "coReading": "Kata-kata manis apa yang diucapkan Ibu kepada Tia?",
                    "imagePrompt": "Handcrafted wax crayon drawing. Mother hugging Tia tenderly beside the dining table, with Father smiling affectionately. Warm amber room lighting, simple bead dot eyes, 4 limbs constraint, completely text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Bunga Dandelion Melayang",
                    "titleEn": "Dreams of Drifting Dandelions",
                    "textId": "Malam itu di atas meja samping ranjang Tia, vas bunga dandelion tetap setia menemani tidurnya. Di bawah sinar bulan purnama yang menembus jendela, payung-payung dandelion putih tampak berkilau perak. Tia tertidur lelap, bermimpi melayang seringan benih dandelion di angkasa yang damai.",
                    "textEn": "That night on Tia's bedside table, the dandelion vase faithfully kept her company. Beneath the full moonlight streaming through the window, the fluffy white dandelion parachutes gleamed silver. Tia slept deeply, dreaming of floating as light as a dandelion seed across peaceful skies.",
                    "quote": "Tidurlah dalam keindahan murni, hatimu yang kreatif adalah pelita dunia.",
                    "coReading": "Mari pejamkan mata dan bayangkan kamu melayang tenang bersama benih dandelion.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Tia sleeping peacefully in bed with the handmade dandelion vase glowing on her wooden nightstand under soft moonlight. Starry sky outside the window, dreamy serene atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 76: Pesawat Kardus Penjelajah Galaksi ---
        {
            "id": "story76",
            "storyNumber": 76,
            "title": "Pesawat Kardus Penjelajah Galaksi",
            "englishTitle": "Cardboard Spaceship Galaxy Explorer",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kekuatan imajinasi anak & mendaur ulang kotak kardus bekas",
            "cover": "covers/story76_cover.jpg",
            "synopsis": "Sebuah kardus mesin cuci bekas diubah oleh Rafa dan kucing orennya, Miko, menjadi pesawat luar angkasa canggih dengan tombol tutup botol dan jendela plastik bening. Dari ruang tengah rumah, imajinasi mereka meluncur menjelajahi galaksi bintang yang gemerlap.",
            "protagonist": "Rafa (Anak laki-laki berhelm mangkuk astronot)",
            "companion": "Kucing Astronot (Kucing oren mengenakan syal bintang)",
            "setting": "Ruang Tengah Rumah",
            "pages": [
                {
                    "number": 1,
                    "title": "Kotak Kardus Raksasa di Ruang Tengah",
                    "titleEn": "Giant Cardboard Box in the Living Room",
                    "textId": "Di tengah karpet ruang tamu tergeletak sebuah kotak kardus cokelat raksasa bekas wadah mesin cuci baru Kakek. Kotak itu begitu tinggi dan lebar, cukup luas untuk memuat anak laki-laki dan seekor kucing gemuk. Rafa melompat kegirangan sambil menatap kotak itu dengan mata berbinar.",
                    "textEn": "In the middle of the living room rug lay a giant brown cardboard box left over from Grandpa's new washing machine. The box was so tall and wide, spacious enough to fit a young boy and a chubby cat. Rafa bounced with joy, his eyes twinkling brightly at the box.",
                    "quote": "Sebuah kotak kardus kosong adalah pintu gerbang menuju seribu petualangan ajaib.",
                    "coReading": "Pernahkah kamu masuk dan bermain di dalam kotak kardus besar?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Rafa, an imaginative boy in striped pajamas and a cloth astronaut helmet, looking excitedly at a huge brown cardboard box in the living room. Chubby ginger cat sitting beside him, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Jendela Kaca Bulat Pesawat",
                    "titleEn": "Round Porch Window for the Ship",
                    "textId": "Dengan bantuan gunting tumpul dan bimbingan Ayah, Rafa memotong lubang bundar di salah satu sisi kardus. Ia menempelkan plastik mika bening di lubang itu menggunakan selotip warna perak. 'Ini jendela kokpit untuk mengamati komet melintas,' seru Rafa pada Miko si kucing oren.",
                    "textEn": "With blunt craft scissors and Dad's gentle help, Rafa cut a round porthole on one side of the box. He taped a sheet of clear plastic over the opening with shiny silver tape. 'This is our cockpit window to watch passing comets,' Rafa called to Miko the ginger cat.",
                    "quote": "Kreativitas mengubah karton sederhana menjadi peralatan canggih masa depan.",
                    "coReading": "Untuk apa jendela bundar pada pesawat luar angkasa?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Rafa and his dad taping clear plastic over a circular cut-out window in the cardboard box. Miko the orange cat sniffing the silver tape, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Panel Kendali Tutup Botol",
                    "titleEn": "Bottle Cap Control Panel",
                    "textId": "Di bagian dalam kotak, Rafa membuat meja kemudi. Ia menempelkan tutup botol warna-warni sebagai tombol peluncuran: merah untuk roket pendorong, biru untuk oksigen luar angkasa, dan hijau untuk musik galaksi. Sebuah piring kertas putih digambar menjadi roda kemudi kemudi bintang.",
                    "textEn": "Inside the box, Rafa built the control deck. He glued colorful bottle caps as launch buttons: red for booster rockets, blue for space oxygen, and green for galactic tunes. A paper plate was decorated as the steering wheel for star-cruising.",
                    "quote": "Barang bekas di sekeliling kita dapat menjadi mainan paling seru bila dirangkai imajinasi.",
                    "coReading": "Tombol warna apa yang paling ingin kamu tekan?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Inside view of the cardboard box showing a paper plate steering wheel and rows of red, blue, green plastic bottle caps pasted as dashboard switches. Rafa sitting at the controls, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Helm Astronot dan Syal Bintang",
                    "titleEn": "Astronaut Helmet and Star Scarf",
                    "textId": "Rafa mengenakan mangkuk sereal plastik putih terbalik sebagai helm pelindung antariksa. Untuk sahabatnya, Rafa melingkarkan pita biru bertabur bintang kertas di leher Miko. Kucing oren itu mendengkur pelan, siap bertugas sebagai kopilot penjelajah bintang.",
                    "textEn": "Rafa placed an inverted white plastic cereal bowl on his head as his space helmet. For his best companion, Rafa tied a blue ribbon dotted with foil stars around Miko's neck. The ginger cat purred softly, ready for duty as the star-cruising copilot.",
                    "quote": "Persahabatan membuat perjalanan paling jauh terasa dekat dan menyenangkan.",
                    "coReading": "Apakah Miko terlihat seperti kucing astronot yang gagah?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Rafa with a funny cute bowl helmet and Miko the orange cat wearing a star-patterned bandana, sitting side by side inside the cardboard spaceship cockpit. Bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Hitungan Mundur Peluncuran",
                    "titleEn": "Countdown to Blastoff",
                    "textId": "Lampu ruang tengah dimatikan. Hanya ada cahaya senter kecil berbintik bintang yang menyala di langit-langit kardus. Rafa menarik tuas kardus dan berteriak, 'Lima... empat... tiga... dua... satu... Meluncurrrr!' Rafa dan Miko mengguncang kardus seolah roket sedang melesat menembus awan.",
                    "textEn": "The living room lights flicked off. Only a tiny starlight projector beamed glowing constellations onto the cardboard ceiling. Rafa pulled a cardboard lever, shouting, 'Five... four... three... two... one... Blastoffff!' Rafa and Miko rocked the box as if rocketing through clouds.",
                    "quote": "Di dalam ruang imajinasi, batasan kenyataan sirna menjadi kebebasan tak bertepi.",
                    "coReading": "Bisakah kamu berhitung mundur lima sampai satu dengan suara roket?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. The cardboard spaceship in the dark living room, with glowing star reflections on its cardboard walls from a small flashlight. Rafa shouting happily at the controls, Miko bracing his paws, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Melintasi Cincin Saturnus",
                    "titleEn": "Cruising Saturn's Rings",
                    "textId": "Dari jendela mika bening, ruang tengah rumah menjelma menjadi angkasa raya. Lampu gantung kuning tampak seperti matahari terbit, dan bantal sofa bundar berbulu menjadi planet Saturnus lengkap dengan cincin hula-hup berkilau di sekelilingnya. Miko menatap keluar jendela dengan mata bulat tak berkedip.",
                    "textEn": "Through the clear plastic porthole, the living room melted into deep outer space. The yellow chandelier glowed like a rising sun, and round fluffy sofa cushions turned into Saturn with shiny hula-hoop rings orbiting around. Miko gazed out with round unblinking eyes.",
                    "quote": "Dunia biasa berubah menjadi megah ketika dilihat lewat lensa imajinasi.",
                    "coReading": "Benda rumah apa yang diubah menjadi planet oleh Rafa?",
                    "imagePrompt": "Vibrant wax crayon and oil pastel smudges. Looking out of the cardboard porthole into an imaginary fantasy galaxy where room cushions float like planets with hula-hoop rings and twinkling stars. Whimsical naive style, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Mendarat di Planet Karpet Biru",
                    "titleEn": "Landing on the Blue Rug Planet",
                    "textId": "'Kopilot Miko, kita menemukan planet berbulu biru lembut!' lapor Rafa. Rafa menekan tombol tutup botol biru untuk melepaskan sauh pendarat. Mereka membuka pintu kardus dan merayap keluar dengan gerakan melayang lambat tanpa gravitasi di atas karpet beludru.",
                    "textEn": "'Copilot Miko, we have discovered a soft blue fuzzy planet!' Rafa reported. He pressed the blue bottle cap to deploy landing gears. They swung open the cardboard hatch, crawling out in slow zero-gravity moonwalk steps across the velvet rug.",
                    "quote": "Bermain peran melatih rasa percaya diri dan kegembiraan jiwa.",
                    "coReading": "Coba peragakan gerakan astronot yang melayang di bulan!",
                    "imagePrompt": "Handcrafted wax crayon on cream paper. Rafa and Miko stepping out of the cardboard spaceship hatch onto a deep blue fuzzy living room rug, moving slowly with floating space postures. Toy planets and stars in background, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Camilan Bintang dari Ibu",
                    "titleEn": "Star Treats from Mission Control",
                    "textId": "Pintu stasiun luar angkasa terbuka perlahan. Ibu datang membawa baki berisi dua cangkir susu hangat dan biskuit berbentuk bintang keemasan. 'Makanan astronot untuk pahlawan galaksi yang lapar,' senyum Ibu. Rafa dan Miko bersorak menyambut bekal penjelajahan itu.",
                    "textEn": "The space station door swung open gently. Mother arrived carrying a tray with two warm cups of milk and golden star-shaped cookies. 'Astronaut rations for my hungry galactic heroes,' Mother smiled. Rafa and Miko cheered at their mission treats.",
                    "quote": "Kehangatan keluarga adalah pelabuhan paling manis setelah petualangan jauh.",
                    "coReading": "Kira-kira apa rasa biskuit berbentuk bintang buatan Ibu?",
                    "imagePrompt": "Warm oil pastel and wax crayon on heavy cream paper. Mother kneeling by the cardboard spaceship offering a plate of star-shaped cookies and warm milk cups to Rafa and Miko. Cozy home ambiance, smiling faces, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Menutup Pintu Pesawat",
                    "titleEn": "Closing the Shuttle Hatch",
                    "textId": "Setelah menghabiskan susu dan biskuit, kantuk mulai menyapa kelopak mata Rafa. Miko sudah meringkuk duluan di atas selimut wol di dasar kardus pesawat. Rafa merapatkan kembali pintu kartonnya, menjadikan pesawat ruang angkasa itu tempat tidur paling nyaman di dunia.",
                    "textEn": "After finishing the milk and cookies, sleepiness kissed Rafa's eyelids. Miko had already curled up on the woolen blanket inside the cardboard ship. Rafa pulled the cardboard door shut, turning their spaceship into the coziest bed in the entire universe.",
                    "quote": "Tempat paling nyaman untuk beristirahat adalah tempat yang dipenuhi kenangan manis.",
                    "coReading": "Di mana Miko dan Rafa tidur malam ini?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Rafa and Miko snuggled cozily together inside the decorated cardboard box beneath a soft quilt. Gentle starlight glowing through the circular window, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Nyenyak di Galaksi Impian",
                    "titleEn": "Sound Sleep in the Dream Galaxy",
                    "textId": "Ayah memindahkan Rafa ke kasurnya dengan gendongan yang lembut, lalu meletakkan Miko di ujung selimutnya. Di dalam lelapnya, Rafa tersenyum damai, bermimpi mengarungi samudera bintang di langit malam yang luas dan penuh keajaiban.",
                    "textEn": "Dad gently scooped sleeping Rafa into his arms, carrying him to bed, and settled Miko at his feet. In deep restful sleep, Rafa smiled softly, dreaming of sailing the vast starry oceans of a night sky brimming with wonder.",
                    "quote": "Tidurlah wahai penjelajah kecil, galaksi impian selalu menunggumu dalam lelap.",
                    "coReading": "Mari pejamkan mata dan terbangkan roket mimpimu menuju bintang paling terang.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Rafa sleeping serenely in his cozy bedroom under a star-patterned duvet, with Miko curled at his feet. Cardboard rocket parked in corner, crescent moon and bright stars glowing softly outside window. Peaceful bedtime scene, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 77: Gendang Tempurung Kelapa ---
        {
            "id": "story77",
            "storyNumber": 77,
            "title": "Gendang Tempurung Kelapa",
            "englishTitle": "Coconut Shell Drum",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kreativitas musik tradisional & menemukan irama dalam benda sederhana",
            "cover": "covers/story77_cover.jpg",
            "synopsis": "Di bawah pohon kelapa pesisir, Bayu menemukan dua belahan tempurung kelapa tua yang keras dan kering. Dengan menggosoknya menggunakan batu kali dan membentangkan karet ban bekas sebagai membran, Bayu menciptakan alat musik perkusi yang merdu untuk bernyanyi bersama teman-teman.",
            "protagonist": "Bayu (Anak laki-laki berpakaian adat sederhana)",
            "companion": "Kawan Perkusi (Anak-anak bernyanyi sambil memukul batok)",
            "setting": "Bawah Pohon Kelapa",
            "pages": [
                {
                    "number": 1,
                    "title": "Tempurung Kering di Bawah Nyiur",
                    "titleEn": "Dry Shells Beneath the Palms",
                    "textId": "Di bawah desau daun pohon kelapa yang melambai ditiup angin pesisir, Bayu menemukan dua belahan batok kelapa tua berwarna cokelat gelap. Batok itu kering dan keras seperti batu. Saat Bayu mengetukkan keduanya, terdengar bunyi 'Tuk, tuk, tuk!' yang nyaring dan bulat.",
                    "textEn": "Beneath the rustling coconut palm leaves dancing in the coastal breeze, Bayu discovered two halves of an old dark brown coconut shell. The shells were dry and hard as river rocks. When Bayu tapped them together, a crisp, hollow 'Clack, clack, clack!' echoed loud and clear.",
                    "quote": "Musik sejati bersembunyi dalam benda-benda paling sederhana di alam.",
                    "coReading": "Bagaimana suara dua batok kelapa saat diketukkan bersama?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Bayu, a young village boy in woven cotton shorts and a simple sarong sash, sitting on the sand under swaying coconut palms holding two polished coconut shell halves. Ocean breeze, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Mengikis Sabut dengan Batu Kali",
                    "titleEn": "Scraping Fibers with River Stone",
                    "textId": "Permukaan luar batok masih kasar dengan sisa-sisa serat sabut yang berduri. Bayu mengambil batu kali yang pipih dan menggosok permukaan batok dengan telaten. Serat-serat kasar terkelupas, memperlihatkan kulit tempurung hitam mengilap yang halus di bawah jemari tangannya.",
                    "textEn": "The outside was rough with bristly coir fibers. Bayu picked up a flat river stone and patiently scrubbed the shell's surface. The rough fibers peeled away, revealing a smooth, shiny dark shell surface beneath his fingertips.",
                    "quote": "Ketelatenan menghaluskan hal kasar menjadi keindahan yang bersinar.",
                    "coReading": "Apakah kamu pernah meraba batok kelapa yang sudah halus?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Bayu sitting cross-legged on a woven pandan mat smoothing a coconut shell with a round stone. Coir shavings on the ground, sunny seaside morning, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Membran Karet yang Lentur",
                    "titleEn": "The Flexible Rubber Membrane",
                    "textId": "Kakek memberikan potongan karet ban sepeda bekas yang sudah dibersihkan. Bayu membentangkan lembaran karet hitam itu di atas mulut salah satu batok kelapa. Kakek membantu menarik karet hingga kencang dan mengikatnya erat-erat menggunakan lilitan tali rotan yang liat.",
                    "textEn": "Grandpa offered a piece of clean salvaged bicycle inner tube rubber. Bayu stretched the black rubber sheet across the open mouth of one coconut shell. Grandpa helped pull it taut, binding it tightly with twists of supple rattan cord.",
                    "quote": "Benda yang lentur dan benda yang kokoh menghasilkan perpaduan suara yang harmonis.",
                    "coReading": "Mengapa karet ban harus ditarik kencang di atas batok kelapa?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Grandpa and Bayu working together on the porch, stretching a rubber sheet over the coconut shell rim and tying it with rattan cord. Warm carpentry tools around, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Ketukan Pertama yang Bergema",
                    "titleEn": "The First Resonating Tap",
                    "textId": "Dengan telapak tangannya yang hangat, Bayu menepuk membran karet gendang mungil itu. 'Dung! Dung! Tak!' Suara yang keluar begitu bulat, dalam, dan hangat, memantul di dinding pondok bambu seperti detak jantung yang riang.",
                    "textEn": "With his warm palm, Bayu tapped the rubber membrane of the tiny drum. 'Doom! Doom! Tak!' The sound was rich, deep, and warm, echoing off the bamboo hut walls like a merry heartbeat.",
                    "quote": "Setiap irama baru membawa getaran kebahagiaan bagi pendengarnya.",
                    "coReading": "Bisakah kamu menepuk pahamu menirukan suara gendang kelapa itu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Bayu tapping the finished mini coconut drum with his hand, mouth open in a happy singing smile. Sound vibration lines around the drum, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Tongkat Tabuh dari Ranting Asam",
                    "titleEn": "Drumstick from a Tamarind Twig",
                    "textId": "Untuk batok kelapa kedua yang tidak ditutup karet, Bayu membuat stik pemukul dari ranting pohon asam yang dibungkus sabut kelapa di ujungnya. Ketika dipukul, 'Klung, klung!' suaranya terdengar seperti lonceng kayu di pura desa.",
                    "textEn": "For the second open coconut shell, Bayu fashioned a drumstick from a tamarind twig padded with wrapped coconut coir at its tip. When struck, 'Clong, clong!' chimed like a wooden bell in a village pavilion.",
                    "quote": "Dua suara yang berbeda menghasilkan melodi yang saling melengkapi.",
                    "coReading": "Suara mana yang lebih kamu sukai: 'Dung' yang berat atau 'Klung' yang renyah?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Bayu holding a small padded wooden beater striking the edge of the smooth coconut shell. Crisp morning seaside setting, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Kawan-Kawan yang Berdatangan",
                    "titleEn": "Friends Gather Around",
                    "textId": "Mendengar bunyi irama yang memikat itu, anak-anak desa berdatangan ke bawah pohon kelapa. Lani membawa suling bambu, Made membawa krincingan biji saga, dan Dani membawa dua bilah bambu ketuk. Mereka duduk melingkar di atas pasir putih.",
                    "textEn": "Hearing the enchanting rhythm, village children flocked beneath the coconut palms. Lani brought her bamboo flute, Made brought red saga seed shakers, and Dani brought bamboo clappers. They sat in a friendly circle on the white sand.",
                    "quote": "Irama yang tulus memiliki daya tarik untuk menyatukan banyak hati.",
                    "coReading": "Alat musik apa saja yang dibawa teman-teman Bayu?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. A cheerful circle of diverse village children sitting on the beach under palm trees, playing bamboo flutes, seed shakers, and coconut drums together. Smiling faces, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Orkestra Sederhana Tepi Pantai",
                    "titleEn": "Simple Shoreline Orchestra",
                    "textId": "Bayu memimpin tempo dengan gendang batoknya: 'Dung-dung-tak, dung-dung-tak!' Suling Lani meliuk merdu, krincingan Made berdesir seperti ombak, dan bambu Dani memberi ketukan ceria. Mereka menyanyikan lagu daerah pengantar petang dengan tawa yang berderai.",
                    "textEn": "Bayu led the tempo on his coconut drum: 'Doom-doom-tak, doom-doom-tak!' Lani's flute trilled sweet melodies, Made's rattle hissed like foamy waves, and Dani's clappers provided merry beats. They sang evening folk tunes amidst bursts of cheerful laughter.",
                    "quote": "Harmoni tercipta saat setiap orang saling mendengarkan dan saling mengisi.",
                    "coReading": "Coba nyanyikan sebaris lagu favoritmu bersama ketukan tangan!",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy paper. Children playing music joyfully together on the seaside lawn at sunset. Musical notes floating gently in the pastel sky, golden sun sinking into the calm sea, bead dot eyes, 4 limbs per child, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Burung Camar yang Ikut Menari",
                    "titleEn": "Seagulls Dancing to the Beat",
                    "textId": "Irama ceria itu membubung tinggi di atas deburan ombak. Burung-burung camar putih terbang rendah melingkari kelompok anak-anak itu, mengepakkan sayapnya seirama dengan ketukan gendang kelapa Bayu. Alam pesisir bersukacita bersama mereka.",
                    "textEn": "The cheerful rhythm soared above the crashing waves. White seagulls swooped low circling the children, flapping their wings in rhythm with Bayu's coconut drumbeat. The coastal world danced in joy alongside them.",
                    "quote": "Kegembiraan yang murni membagikan energi positif bagi sekeliling kita.",
                    "coReading": "Bisakah kamu mengepakkan tangan seperti burung camar yang menari?",
                    "imagePrompt": "Handcrafted oil pastel and wax crayon. White seagulls swooping gracefully in the air above the playing children on the beach. Warm lilac and peach twilight sky, soft gentle ripples on water, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Irama Senja yang Melambat",
                    "titleEn": "The Twilight Tempo Slows",
                    "textId": "Matahari tenggelam sempurna di balik cakrawala, meninggalkan langit lembayung yang lembut. Bayu memperlambat ketukan gendangnya menjadi tabuhan lambat yang menenangkan: 'Dung... dung... hening...' Anak-anak berpamitan pulang dengan hati yang penuh kedamaian.",
                    "textEn": "The sun sank completely beneath the horizon, leaving behind a soft violet twilight. Bayu slowed his drum tempo into a calm, gentle cadence: 'Doom... doom... quiet...' The children bid warm goodbyes, heading home with hearts filled with peace.",
                    "quote": "Setiap hari yang indah layak ditutup dengan irama syukur yang teduh.",
                    "coReading": "Bagaimana tempo ketukan gendang berubah saat malam tiba?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Bayu tapping his coconut drum very slowly as the children wave goodbye walking along the beach path towards their village homes. Soft twilight purple sky, glowing first evening star, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Tenang Berirama Detak Jantung",
                    "titleEn": "Sound Sleep to the Heartbeat Rhythm",
                    "textId": "Di dalam kamarnya yang beralaskan tikar pandan harum, gendang tempurung kelapa diletakkan rapi di sudut meja. Bayu tidur pulas mendengarkan desau angin nyiur di luar jendela dan detak jantungnya sendiri yang teratur, bermimpi tentang irama-irama indah di hari esok.",
                    "textEn": "Inside his room upon a fragrant pandan mat, the coconut shell drum rested neatly at the table corner. Bayu slept deeply listening to the rustling palm breeze outside and his own steady heartbeat, dreaming of lovely melodies in tomorrow's sunrise.",
                    "quote": "Tidurlah dengan damai, irama alam semesta selalu menjaga lelapmu.",
                    "coReading": "Mari pejamkan mata dan rasakan detak jantungmu yang tenang menjelang tidur.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Bayu sleeping peacefully under a batik sarong blanket in a cozy seaside wooden room. The polished coconut drum sitting quietly on the nightstand beside him. Crescent moon and palm silhouettes visible through the window, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
