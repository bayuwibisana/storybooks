# scripts/polish_stories_93_to_97.py
import json

def get_stories_93_to_97():
    stories = [
        # --- STORY 93: Hafal Dendang Lagu Daerah ---
        {
            "id": "story93",
            "storyNumber": 93,
            "title": "Hafal Dendang Lagu Daerah",
            "englishTitle": "Memorizing the Folk Lullaby",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Mencintai budaya leluhur, ketekunan mengingat bait lagu, & kebersamaan hangat",
            "cover": "covers/story93_cover.jpg",
            "synopsis": "Taufiq ingin mempersembahkan lagu daerah 'Bungong Jeumpa' di teras senja untuk menyambut kepulangan Ayah dari ladang. Awalnya Taufiq sering tertukar antara bait kedua dan ketiga. Dengan bimbingan bertepuk tangan berirama dari Ibu, Taufiq berhasil menghafal seluruh syair lagu dengan merdu dan lancar.",
            "protagonist": "Taufiq (Anak laki-laki berpeci rajut hitam)",
            "companion": "Ibu Taufiq (Ibu bertepuk tangan berirama gembira)",
            "setting": "Teras Senja Hari",
            "pages": [
                {
                    "number": 1,
                    "title": "Peci Rajut Hitam dan Angin Sore",
                    "titleEn": "Black Knitted Cap and the Evening Breeze",
                    "textId": "Di teras rumah berpilar kayu berukir, Taufiq duduk mengenakan peci rajut hitam kesayangannya dan sarung tenun kotak-kotak hijau. Udara senja bertiup semilir membawa wangi bunga cempaka kuning dari pekarangan. Hari ini Taufiq bertekad menghafal bait lagu daerah untuk menyambut Ayah.",
                    "textEn": "On the porch with carved wooden pillars, Taufiq sat wearing his favorite black knitted cap and a green-checkered woven sarong. The evening breeze blew gently, carrying sweet yellow champaca scents from the garden. Today Taufiq was determined to memorize a folk song to welcome Father home.",
                    "quote": "Melodi warisan leluhur menyimpan kehangatan tanah air di setiap baitnya.",
                    "coReading": "Lagu daerah apa yang paling kamu sukai saat dinyanyikan di rumah?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Taufiq, a polite young boy in a black knit cap and checkered sarong, sitting on rustic porch steps in golden evening sunlight. Blooming yellow champaca blossoms in the garden, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Bait-Bait yang Sering Tertukar",
                    "titleEn": "Verses That Often Mixed Up",
                    "textId": "'Bungong jeumpa, bungong jeumpa meugah di Aceh...' dendang Taufiq riang. Namun saat memasuki bait berikutnya, lidah Taufiq tersandung: apakah bunga putih kuning yang mekar lebih dulu, atau semerbak harumnya yang disebut dahulu? Taufiq menggaruk pecinya yang tidak gatal sambil meringis.",
                    "textEn": "'Bungong jeumpa, bungong jeumpa meugah di Aceh...' Taufiq sang merrily. But reaching the next verse, his tongue stumbled: do the white and yellow blossoms open first, or does their sweet scent come before? Taufiq scratched his cap with an embarrassed grin.",
                    "quote": "Kesalahan adalah batu loncatan untuk memahami dengan lebih mendalam.",
                    "coReading": "Pernahkah kamu lupa lirik lagu di tengah-tengah bernyanyi?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Taufiq tilting his black cap with one hand, mouth open mid-song with a puzzled humorous smile. Mother sitting nearby on a woven mat smiling gently, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Tepukan Berirama Dua Ketukan",
                    "titleEn": "Rhythmic Two-Count Clapping",
                    "textId": "Ibu meletakkan mangkuk pisang rebus di atas meja teras dan berlutut di depan Taufiq. 'Bernyanyi itu seperti berjalan bergandengan tangan, Taufiq. Mari kita gunakan tepuk tangan untuk menjaga tempo langkah syairnya: Prok... prok... hening... prok!'",
                    "textEn": "Mother set a bowl of steamed bananas on the porch table and knelt before Taufiq. 'Singing is just like walking hand in hand, Taufiq. Let us use gentle claps to keep the rhythm of the verses: Clap... clap... rest... clap!'",
                    "quote": "Irama yang teratur menuntun ingatan kita melangkah dengan pasti.",
                    "coReading": "Bisakah kamu bertepuk tangan mengikuti irama Ibu: prok, prok, hening?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Mother clapping her hands with a warm radiant smile, demonstrating the song rhythm to Taufiq. Sunbeams slanting across the wooden porch floor, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Membayangkan Bunga Cempaka Mekar",
                    "titleEn": "Picturing the Champaca in Bloom",
                    "textId": "Ibu menunjuk kuntum bunga cempaka di pekarangan: 'Ingatlah urutannya, sayang. Bunganya kuncup dahulu, lalu mekar putih kuning berseri, baru kemudian wanginya semerbak diterbangkan angin ke seluruh desa.' Mata Taufiq berbinar membayangkan urutan bunga itu.",
                    "textEn": "Mother pointed to the champaca blossoms in the yard: 'Remember the story, my love. First comes the green bud, then it blooms yellow and white, and only then does its sweet perfume ride the breeze across the village.' Taufiq's eyes lit up picturing the blossoms.",
                    "quote": "Memahami makna cerita di balik lagu membuat ingatan melekat abadi.",
                    "coReading": "Bagaimana bunga cempaka mekar sebelum menebarkan wangi?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Mother pointing toward a blooming yellow champaca tree in the yard. Taufiq looking at the flowers with an understanding smile, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Bait Kedua yang Mengalun Mulus",
                    "titleEn": "The Second Verse Glides Smooth",
                    "textId": "Taufiq menarik napas dalam-dalam. Sambil menepuk pahanya mengikuti ketukan irama Ibu, suara Taufiq mengalun jernih: 'Puteh kuneng meujampu mirah... keumang si tangke...' Bait kedua terucap dengan lancar tanpa ada satu kata pun yang tertinggal!",
                    "textEn": "Taufiq took a deep breath. Tapping his knees to Mother's rhythmic beat, his voice soared pure and clear: 'Puteh kuneng meujampu mirah... keumang si tangke...' The second verse flowed smoothly, not a single word missed!",
                    "quote": "Latihan yang dipandu dengan cinta selalu membuahkan hasil manis.",
                    "coReading": "Apakah Taufiq berhasil menyanyikan bait kedua sekarang?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Taufiq singing with chest high and a bright confident smile, clapping hands gently in time with Mother. Golden late afternoon light, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Gerakan Tangan yang Lembut",
                    "titleEn": "Graceful Hand Gestures",
                    "textId": "Ibu mengajari Taufiq menggerakkan kedua telapak tangannya: meliuk perlahan ke kiri dan ke kanan seperti kelopak bunga yang menari dihembus angin semilir. Gerakan tangan itu membuat dendang lagu terasa semakin hidup dan memesona.",
                    "textEn": "Mother taught Taufiq to wave his hands gracefully: swaying gently left and right like flower petals dancing in the breeze. The delicate hand motions made the folk song feel even more alive and enchanting.",
                    "quote": "Harmoni antara suara dan gerak tubuh melahirkan keindahan yang sempurna.",
                    "coReading": "Bisakah kamu menggerakkan kedua tanganmu meliuk seperti bunga menari?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Taufiq making graceful curved hand gestures while singing, his checkered sarong fluttering gently. Mother smiling with proud teary eyes, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Langkah Kaki Ayah di Gerbang Kayu",
                    "titleEn": "Father's Footsteps at the Wooden Gate",
                    "textId": "Terdengar derit pintu pagar kayu di ujung pekarangan. Ayah melangkah pulang memanggul cangkul dengan caping lebar di kepala. Wajah Ayah tampak lelah sehabis seharian bekerja di sawah, namun seketika bersinar mendengar suara nyanyian dari teras.",
                    "textEn": "The wooden garden gate creaked in the distance. Father walked up the path carrying a hoe, wearing a broad sunhat. His face looked tired from a long day in the rice fields, but lit up instantly upon hearing singing from the porch.",
                    "quote": "Sambutan hangat dari rumah menghapus segala penat dan lelah seharian.",
                    "coReading": "Siapa yang baru pulang melalui gerbang pekarangan?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Father walking through the wooden yard gate carrying a farm hoe, pausing with a broad happy smile as he hears Taufiq singing. Evening sunset hues, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Persembahan Nyanyian Sempurna",
                    "titleEn": "A Perfect Song Performance",
                    "textId": "Taufiq berdiri tegak di undakan teras. Dengan suara yang bulat, merdu, dan penuh penghayatan, ia menyanyikan seluruh bait lagu dari awal hingga akhir tanpa ragu sedikit pun. Gerakan tangannya meliuk anggun diiringi tepuk tangan Ibu yang selaras.",
                    "textEn": "Taufiq stood proudly on the porch steps. With a round, melodious, and heartfelt voice, he sang every single verse from beginning to end without a single hesitation. His hands moved gracefully to Mother's harmonized claps.",
                    "quote": "Ketekunan belajar adalah persembahan cinta terbaik untuk orang tua.",
                    "coReading": "Bagaimana perasaan Ayah mendengarkan nyanyian lengkap Taufiq?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Taufiq singing on the porch steps with hands outstretched in performance. Father resting his hoe against the wall, listening with touched pride, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Pelukan Hangat Beraroma Padi",
                    "titleEn": "Warm Hug Scented Like Rice Fields",
                    "textId": "Begitu bait terakhir berakhir, Ayah melepaskan capingnya dan memeluk Taufiq erat-erat. 'Luar biasa merdu, Taufiq! Rasa lelah Ayah langsung hilang mendengar nyanyianmu,' bisik Ayah haru. Ibu membawakan segelas teh manis hangat untuk dinikmati bersama di teras.",
                    "textEn": "As the final verse ended, Father set down his hat and lifted Taufiq into a warm embrace. 'Magnificent, Taufiq! All my fatigue vanished the moment I heard your song,' Father whispered with joy. Mother brought glasses of warm sweet tea to share on the porch.",
                    "quote": "Kebahagiaan keluarga adalah surga terindah di muka bumi.",
                    "coReading": "Apa yang dikatakan Ayah setelah mendengar lagu Taufiq?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Father hugging Taufiq warmly on the porch with Mother beside them holding steaming glasses of tea. Sunset sky in amber and violet, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Bunga Cempaka Emas",
                    "titleEn": "Dreams of Golden Champaca Blooms",
                    "textId": "Malam tiba dan angin pegunungan bertiup sejuk meninabobokan desa. Taufiq tidur pulas di ranjang kayunya berselimut sarung hangat. Di dalam mimpinya, dendang lagu daerah mengalun lembut membawanya melayang di atas taman bunga cempaka emas yang mekar di bawah sinar bintang.",
                    "textEn": "Night arrived and cool mountain breezes lulled the village to sleep. Taufiq slept deeply in his wooden bed under a warm sarong. In his dreams, the folk melody hummed softly, lifting him across golden champaca gardens blooming beneath starlight.",
                    "quote": "Tidurlah dalam kebanggaan budaya leluhurmu, hatimu selalu kaya akan kebaikan.",
                    "coReading": "Mari pejamkan mata sambil mendengarkan nyanyian pengantar tidur yang menenangkan.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Taufiq sleeping peacefully in bed with a checkered sarong quilt. His black cap resting on the nightstand. Outside the window, the champaca tree silhouetted under a starlit night and crescent moon. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 94: Kotak Balok yang Rapi Kembali ---
        {
            "id": "story94",
            "storyNumber": 94,
            "title": "Kotak Balok yang Rapi Kembali",
            "englishTitle": "The Tidy Toy Crate Again",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Tanggung jawab merapikan mainan, kemandirian, & rumah yang nyaman",
            "cover": "covers/story94_cover.jpg",
            "synopsis": "Sehabis bermain membangun kota seharian, lantai kamar Pandu dipenuhi ratusan balok kayu yang berserakan. Awalnya Pandu malas merapikannya karena lelah. Mama mengajak Pandu bermain 'Kereta Pengangkut Balok' yang membuat tugas merapikan mainan menjadi permainan seru dan tuntas.",
            "protagonist": "Pandu (Anak laki-laki bercelemek kerja mini)",
            "companion": "Mama Pandu (Mama mengusap kepala anak dengan bangga)",
            "setting": "Kamar Bermain Anak",
            "pages": [
                {
                    "number": 1,
                    "title": "Kota Balok di Tengah Karpet",
                    "titleEn": "Block City in the Middle of the Rug",
                    "textId": "Lantai kamar bermain Pandu tampak seperti miniatur kota besar: ada jembatan layang, stasiun kereta, gedung bertingkat, dan garasi mobil-mobilan dari balok kayu. Pandu duduk di tengah kota itu sambil menguap lebar, matanya mulai terasa mengantuk sehabis bermain seru.",
                    "textEn": "Pandu's playroom floor looked like a miniature bustling metropolis: there were overpasses, train stations, towers, and toy garages built from wooden blocks. Pandu sat in the center with a big yawn, his eyelids growing heavy after an afternoon of fun.",
                    "quote": "Bermain dengan gembira adalah hak setiap anak yang bersemangat.",
                    "coReading": "Bangunan apa saja yang dibuat Pandu dari balok kayunya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Pandu, an imaginative boy in a yellow tee and blue dungarees, sitting on a colorful playroom rug surrounded by elaborate wooden block towers and toy cars. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Lantai yang Sulit Dilalui",
                    "titleEn": "A Floor Hard to Walk Upon",
                    "textId": "Mama membuka pintu kamar dan harus melangkah berjingkat dengan sangat hati-hati agar tidak menginjak balok runcing. 'Wah, kota buatanmu luar biasa megah, Pandu! Tapi sekarang matahari sudah terbenam, dan para balok butuh kembali ke rumah kotaknya untuk tidur,' senyum Mama.",
                    "textEn": "Mother opened the door, tiptoeing with great care so she wouldn't step on pointy wooden corners. 'My, your city is so grand, Pandu! But now the sun has set, and the wooden blocks need to return to their toy crate bed,' Mother smiled.",
                    "quote": "Kerapian menjaga ruangan tetap aman dan menyenangkan bagi semua orang.",
                    "coReading": "Apa yang terjadi jika balok mainan terinjak kaki di malam hari?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Mother tiptoeing carefully across the playroom floor avoiding scattered colorful blocks, smiling down at Pandu. Cozy lamplight in bedroom, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Rasa Malas yang Menyapa",
                    "titleEn": "A Wave of Sleepy Laziness",
                    "textId": "Pandu menatap ratusan balok yang berserakan dengan malas. Tubuhnya terasa lelah dan ingin langsung melompat ke kasur empuknya. 'Baloknya banyak sekali, Ma... bagaimana kalau besok pagi saja dirapikannya?' rengek Pandu pelan.",
                    "textEn": "Pandu looked at the hundreds of scattered blocks with a lazy sigh. His body felt tired and wanted to hop straight into bed. 'There are so many blocks, Mom... can't we just tidy them tomorrow morning?' Pandu whined softly.",
                    "quote": "Menunda pekerjaan membuat beban terasa berlipat ganda di kemudian hari.",
                    "coReading": "Apakah kamu pernah merasa malas merapikan mainan sehabis bermain?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Pandu sitting with knees hugged to chest, looking tiredly at the sprawling wooden blocks on the rug. Mother kneeling beside him with comforting posture, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Permainan Kereta Pengangkut Balok",
                    "titleEn": "The Block Hauler Train Game",
                    "textId": "Mama tersenyum mengerti dan tidak marah. Mama mengambil gerobak dorong kayu kecil Pandu dan membunyikan suara klakson: 'Tut, tut, gujes, gujes! Kereta pengangkut barang membutuhkan Masinis Pandu untuk memuat kargo kayu sebelum stasiun tutup!' Mata Pandu berbinar seketika.",
                    "textEn": "Mother smiled with understanding without a scolding tone. She grabbed Pandu's little wooden pull-cart and tooted like an engine: 'Choo, choo, chugga, chugga! The freight train needs Engineer Pandu to load wooden cargo before the station closes!' Pandu's eyes sparked with fun.",
                    "quote": "Kreativitas orang tua mampu mengubah tugas yang berat menjadi permainan yang seru.",
                    "coReading": "Kendaraan apa yang digunakan untuk mengangkut balok ke kotaknya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Mother playfully pushing a small wooden pull-wagon toward Pandu like a toy train. Pandu grinning as he reaches for blocks to load, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Muatan Warna Merah dan Kuning",
                    "titleEn": "Red and Yellow Cargo Loads",
                    "textId": "'Stasiun pertama: kargo warna merah!' seru Mama. Dengan cekatan, Pandu mengumpulkan balok-balok merah delima dan memasukkannya ke dalam gerobak. 'Klotak, klotak!' bunyi balok bersarang rapi di dalam gerobak dorong.",
                    "textEn": "'First station: red cargo load!' called Mother. Nimbly, Pandu collected the ruby-red blocks, piling them into the wagon. 'Clack, clonk!' sounded the blocks nesting neatly inside the cart.",
                    "quote": "Mengelompokkan berdasarkan warna membuat pekerjaan teratur dan cepat selesai.",
                    "coReading": "Warna balok apa yang pertama kali diangkut oleh Masinis Pandu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Pandu cheerfully loading red and yellow wooden blocks into the wooden wagon. Playroom floor gradually clearing, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Kereta Meluncur Menuju Peti Besar",
                    "titleEn": "The Train Rolls to the Big Crate",
                    "textId": "Pandu menarik tali gerobak sambil berseru menirukan kereta api: 'Chugga-chugga-choo-choo!' Ia membawa muatan itu ke peti kayu besar di sudut kamar. Di sana, Pandu menyusun balok-balok itu dengan rapi seperti menata buku di rak perpustakaan.",
                    "textEn": "Pandu pulled the cart's cord, tooting like a locomotive: 'Chugga-chugga-choo-choo!' He hauled the load to the large wooden toy chest in the corner. There, he stacked the blocks neatly like books on a library shelf.",
                    "quote": "Kerapian yang tertata rapi memberi kepuasan tersendiri bagi mata yang memandang.",
                    "coReading": "Di mana rumah tempat balok-balok itu disimpan?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Pandu pulling the loaded wooden wagon across the rug toward a large rustic toy chest in the corner. Playful dynamic motion, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Stasiun Terakhir: Balok Biru dan Hijau",
                    "titleEn": "Last Station: Blue and Green Blocks",
                    "textId": "Tinggal putaran kedua: balok biru silinder dan balok hijau prisma. Pandu dan Mama bekerja sama dengan cepat sambil bernyanyi riang. Hanya dalam sepuluh menit, karpet ruang bermain yang tadinya penuh sesak kini kembali lapang, bersih, dan lembut.",
                    "textEn": "Just the second run remained: blue cylinders and green prisms. Pandu and Mother teamed up swiftly, singing a cheerful working song. In just ten minutes, the crowded rug was once again wide, clean, and soft.",
                    "quote": "Bekerja bersama membuat pekerjaan berat selesai dalam sekejap mata.",
                    "coReading": "Berapa lama waktu yang dibutuhkan Pandu dan Mama untuk membereskan kamar?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Pandu and Mother placing the last green triangular blocks into the wooden chest. The playroom rug now completely clear and tidy, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Menutup Peti Kayu dengan Rapat",
                    "titleEn": "Shutting the Toy Chest Lid Tight",
                    "textId": "'Klek!' Tutup peti kayu ditutup rapat. Di atas tutupnya tidak ada lagi mainan yang tercecer. Pandu menepuk kedua tangannya yang bersih dan memandang sekeliling kamarnya. Ruangan itu terasa begitu luas, lapang, dan nyaman untuk ditinggali.",
                    "textEn": "'Click!' The wooden toy chest lid shut firm. No stray toys remained on top. Pandu brushed his clean hands and looked around his room. The space felt so airy, spacious, and inviting to rest in.",
                    "quote": "Ruangan yang rapi menghadirkan ketenangan bagi pikiran dan hati.",
                    "coReading": "Bagaimana perasaan ruangan kamar setelah semua mainan dirapikan?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Pandu standing proudly with hands on hips before the closed, tidy wooden toy chest. Clean rug, tidy bedroom, warm golden light, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Usapan Kepala Penuh Kebanggaan",
                    "titleEn": "A Proud Stroke on the Head",
                    "textId": "Mama mengusap rambut Pandu dengan penuh rasa bangga dan mencium keningnya. 'Terima kasih, Masinis Pandu. Kamarmu kini siap untuk tidur yang nyaman tanpa ada yang tersandung di malam hari.' Pandu tersenyum lebar, merasa dirinya sudah menjadi anak besar yang mandiri.",
                    "textEn": "Mother stroked Pandu's hair with pride, kissing his forehead. 'Thank you, Engineer Pandu. Your room is now ready for sweet sleep without anyone tripping in the dark.' Pandu beamed, feeling like a responsible big boy.",
                    "quote": "Tanggung jawab yang dituntaskan melahirkan rasa percaya diri yang sejati.",
                    "coReading": "Apa yang dilakukan Mama untuk memuji tanggung jawab Pandu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother kneeling down hugging Pandu tenderly on the clean rug, stroking his hair with a loving smile. Soft bedtime bedroom lighting, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Tenang di Kamar yang Rapi",
                    "titleEn": "Peaceful Sleep in a Tidy Room",
                    "textId": "Pandu melompat ke atas kasurnya dan menarik selimut biru hangatnya. Lampu tidur berbentuk bintang dinyalakan, memancarkan cahaya lembut ke seluruh ruangan yang bersih. Pandu memejamkan mata dan tertidur pulas, bermimpi mengemudikan kereta uap ajaib melintasi awan-awan perak.",
                    "textEn": "Pandu hopped into bed and pulled up his warm blue blanket. The star-shaped nightlight turned on, casting a gentle glow over the tidy room. Pandu closed his eyes, sleeping soundly, dreaming of driving a magical steam train across silver clouds.",
                    "quote": "Tidurlah dalam ketenangan, kamar yang rapi menjaga istirahatmu tetap damai.",
                    "coReading": "Mari rapikan tempat tidurmu sebelum tidur agar tidurmu senyaman Pandu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Pandu sleeping soundly in his cozy bed with a star nightlight glowing softly on the bedside table. Clean floor, tidy wooden toy chest in corner. Crescent moon shining through the window, serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 95: Menunggu Adonan Ragi Mengembang ---
        {
            "id": "story95",
            "storyNumber": 95,
            "title": "Menunggu Adonan Ragi Mengembang",
            "englishTitle": "Waiting for the Yeast Dough to Rise",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kesabaran menunggu proses alami, kehangatan memasak bersama ibu, & aroma kasih sayang",
            "cover": "covers/story95_cover.jpg",
            "synopsis": "Bintang memakai topi koki kecil membantu Bunda membuat roti manis kismis di dapur. Ketika adonan tepung selesai diuleni, Bintang ingin langsung memanggangnya ke dalam oven. Bunda mengajarinya menutup adonan dengan kain lembap dan bersabar menanti ragi bekerja hingga adonan mengembang dua kali lipat.",
            "protagonist": "Bintang (Anak koki kecil bertopi putih)",
            "companion": "Bunda Bintang (Bunda mengukur jam dapur analog)",
            "setting": "Dapur Roti Rumah",
            "pages": [
                {
                    "number": 1,
                    "title": "Topi Koki Putih dan Celemek Mini",
                    "titleEn": "White Chef's Hat and Mini Apron",
                    "textId": "Pagi yang sejuk di dapur rumah, Bintang berdiri di atas bangku kayu kecil agar kepalanya sejajar dengan meja dapur. Bintang mengenakan topi koki putih kain yang lucu dan celemek bermotif garis-garis biru. Di hadapannya terhampar mangkuk keramik besar berisi tepung terigu putih halus.",
                    "textEn": "On a cool morning in the kitchen, Bintang stood on a small wooden stepstool so his head reached the counter. Bintang wore an adorable white fabric chef's hat and a blue-striped apron. Before him sat a large ceramic mixing bowl filled with fine white flour.",
                    "quote": "Dapur keluarga adalah laboratorium cinta tempat keajaiban tercipta.",
                    "coReading": "Pernahkah kamu membantu Ibu memasak atau membuat kue di dapur?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Bintang, a cute little boy in a puffy white chef hat and apron, standing on a wooden stool at the kitchen counter beside a ceramic bowl of flour. Mother measuring ingredients beside him, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Ragi Ajaib yang Berbusa Manis",
                    "titleEn": "Magic Yeast with Sweet Froth",
                    "textId": "Bunda mencampurkan sebutir ragi kering ke dalam segelas air hangat berlumur madu. Dalam lima menit, cairan itu mulai mengeluarkan busa lembut dan gelembung-gelembung kecil yang beraroma harum roti segar. 'Ragi ini adalah kawan kecil yang akan meniupkan udara ke dalam adonan kita, Bintang,' jelas Bunda.",
                    "textEn": "Mother stirred dry yeast into a glass of warm honey water. In five minutes, the liquid foamed up with gentle frothy bubbles smelling fragrantly of fresh bread. 'This yeast is our tiny helper who will breathe air into our dough, Bintang,' Mother explained.",
                    "quote": "Bahan alami yang hidup membutuhkan kehangatan untuk mulai bekerja.",
                    "coReading": "Bagaimana aroma ragi yang mulai berbusa?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up of a glass cup showing warm foamy yeast bubbling softly on the kitchen counter. Bintang peeking into the cup with wide wonder, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Menguleni Adonan yang Kenyal",
                    "titleEn": "Kneading the Springy Dough",
                    "textId": "Bunda menuangkan cairan ragi, susu hangat, dan mentega kuning ke dalam tepung. Dengan kedua tangan kecilnya yang sudah ditaburi tepung, Bintang meremas dan menekan adonan: 'Tekan, lipat, dorong!' Adonan yang tadinya lengket perlahan berubah menjadi gumpalan bulat halus selembut pipi bayi.",
                    "textEn": "Mother poured the foamy yeast, warm milk, and golden butter into the flour. With little flour-dusted hands, Bintang pressed and kneaded the dough: 'Push, fold, roll!' The sticky mixture slowly turned into a smooth, springy ball as soft as a baby's cheek.",
                    "quote": "Ketekunan tangan mengubah bahan yang terpisah menjadi satu kesatuan yang kenyal.",
                    "coReading": "Bisakah kamu menirukan gerakan menekan dan melipat adonan roti?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Bintang pressing his small hands into a smooth golden ball of dough on a floured wooden board, cheeks smudged with flour. Mother smiling beside him, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Ingin Langsung Memanggang",
                    "titleEn": "Wanting to Bake Right Away",
                    "textId": "Bintang bersiap mengangkat loyang oven. 'Bunda, adonannya sudah bulat! Ayo kita masukkan ke oven sekarang agar rotinya cepat matang!' pinta Bintang tak sabar. Perutnya sudah membayangkan kelezatan roti manis bertabur kismis.",
                    "textEn": "Bintang reached for the baking pan eagerly. 'Mom, the dough is round now! Let us bake it in the oven right away so it is ready fast!' Bintang pleaded impatiently. His tummy was already picturing sweet raisin buns.",
                    "quote": "Ketergesaan sering kali membuat kita melewatkan proses pematangan yang penting.",
                    "coReading": "Mengapa adonan roti belum boleh langsung dipanggang ke oven?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Bintang holding a baking tray looking up eagerly at Mother who points gently toward the dough bowl. Cozy sunny kitchen, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Selimut Kain Lembap Pengantar Istirahat",
                    "titleEn": "Damp Cloth Blanket for Resting",
                    "textId": "Bunda tersenyum dan menggeleng lembut. 'Belum saatnya, koki kecil. Jika dipanggang sekarang, rotinya akan keras dan bantat seperti batu kali. Adonan ini lelah sehabis diuleni; ia butuh tidur sejenak di bawah selimut hangat.' Bunda menutup mangkuk dengan kain serbet bersih yang lembap.",
                    "textEn": "Mother smiled and gently shook her head. 'Not yet, little chef. If baked now, the bread will be hard and dense as river stones. This dough is tired from kneading; it needs to rest beneath a cozy blanket.' Mother covered the bowl with a clean, damp towel.",
                    "quote": "Istirahat yang cukup memberi ruang bagi kekuatan baru untuk bertumbuh.",
                    "coReading": "Benda apa yang digunakan Bunda untuk menyelimuti mangkuk adonan?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother draping a clean checkered damp cloth over the ceramic bowl of dough. Bintang resting his elbows on the counter watching curiously, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Detik Jam Dapur Analog",
                    "titleEn": "Ticking of the Kitchen Clock",
                    "textId": "'Tik, tok, tik, tok...' Jarum merah jam dinding dapur berdetik lambat. Bintang duduk di kursinya menopang dagu, memandangi mangkuk berselimut kain itu. Sepuluh menit terasa seperti sepuluh jam. Bunda mengajak Bintang membaca buku dongeng agar waktu menunggu terasa menyenangkan.",
                    "textEn": "'Tick, tock, tick, tock...' The kitchen wall clock ticked steadily. Bintang sat on his stool with his chin propped in his hands, watching the covered bowl. Ten minutes felt like ten hours. Mother opened a picture book so the wait would feel delightful.",
                    "quote": "Menunggu menjadi indah saat kita mengisinya dengan kegiatan yang bermakna.",
                    "coReading": "Apa yang dilakukan Bintang dan Bunda sambil menunggu adonan mengembang?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Mother and Bintang sitting at the kitchen table reading an open picture book together, with the covered bowl resting in the background beside a wall clock. Warm cozy mood, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Keajaiban di Balik Selimut Kain",
                    "titleEn": "The Wonder Beneath the Cloth",
                    "textId": "Satu jam berlalu. Bunda mengajak Bintang mengintip: 'Satu... dua... tiga... buka!' Ketika kain serbet diangkat, 'Wah!' seru Bintang takjub. Adonan yang tadinya kecil kini telah mengembang raksasa, montok, dan empuk memenuhi seluruh mangkuk seperti bantal awan!",
                    "textEn": "An hour drifted by. Mother invited Bintang to peek: 'One... two... three... open!' When the towel lifted, 'Wow!' Bintang gasped in awe. The once-small dough had puffed up enormous, plump, and springy, filling the entire bowl like a puffy cloud cushion!",
                    "quote": "Kesabaran menanti selalu dihadiahi oleh pertumbuhan yang menakjubkan.",
                    "coReading": "Bagaimana ukuran adonan roti setelah didiamkan selama satu jam?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Bintang and Mother lifting the cloth together to reveal the dough risen to twice its size, puffy and golden-white in the ceramic bowl. Bintang's mouth open in sheer delight, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Sentuhan Kismis dan Olesan Kuning Telur",
                    "titleEn": "Raisin Toppings and Egg Wash Glaze",
                    "textId": "Dengan hati gembira, Bintang membagi adonan menjadi roti-roti bulat kecil. Ia menancapkan butiran kismis manis di atasnya dan mengoleskan kuning telur menggunakan kuas bulu halus. Roti-roti itu kini siap masuk ke dalam oven yang sudah dipanaskan.",
                    "textEn": "With a singing heart, Bintang shaped the dough into little round buns. He pressed sweet raisins into their tops and brushed them with golden egg glaze using a pastry brush. The buns were now ready for the preheated oven.",
                    "quote": "Sentuhan akhir yang manis menyempurnakan karya yang dirawat dengan sabar.",
                    "coReading": "Bahan manis apa yang ditancapkan Bintang di atas rotinya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Bintang carefully pressing dark raisins into little round buns on a baking tray, brushing them with golden glaze. Chef hat tilted cute, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Aroma Roti Hangat yang Menyapa Rumah",
                    "titleEn": "Warm Bread Aroma Fills the Home",
                    "textId": "Dari dalam oven kaca, aroma mentega harum, ragi matang, dan manisnya kismis menguar memenuhi seluruh sudut rumah. Ketika pintu oven dibuka, tampak roti-roti manis berwarna cokelat keemasan yang merekah sempurna. Bintang mencicipi gigitan pertama: rotinya begitu lembut dan meleleh di lidah!",
                    "textEn": "From inside the oven, aromas of buttery yeast and sweet raisins wafted into every corner of the house. When the door opened, there lay golden-brown sweet rolls puffed to perfection. Bintang took his first bite: the bread was feather-soft, melting on his tongue!",
                    "quote": "Hasil dari kesabaran terasa seribu kali lebih lezat daripada yang terburu-buru.",
                    "coReading": "Bagaimana rasa roti buatan Bintang dan Bunda?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother pulling a tray of steaming, golden-brown raisin buns from the oven with oven mitts. Bintang cheering with hands raised, steam rising with sweet aroma lines, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Lelap Beraroma Roti Manis",
                    "titleEn": "Sound Sleep Scented of Sweet Rolls",
                    "textId": "Malam tiba dan dapur telah bersih dan rapi kembali. Di atas meja makan tersimpan sekeranjang roti manis yang ditutup tudung saji. Bintang tidur pulas di ranjangnya dengan perut kenyang dan hati yang bahagia, bermimpi tentang awan-awan roti manis yang empuk di langit malam berbintang.",
                    "textEn": "Night arrived and the kitchen was spotless and tidy again. On the dining counter rested a basket of sweet buns under a mesh cover. Bintang slept deeply in bed with a full tummy and happy heart, dreaming of puffy sweet-bread clouds floating across a starlit night.",
                    "quote": "Tidurlah dalam kehangatan cinta, kesabaranmu hari ini telah berbuah manis.",
                    "coReading": "Mari pejamkan mata dan bayangkan aroma harum roti hangat menemani tidurmu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Bintang sleeping peacefully in bed with his white chef hat resting on the wooden nightstand. Soft moonlight filtering through window, crescent moon and stars outside. Serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 96: Janggut Putih & Kisah Kakek ---
        {
            "id": "story96",
            "storyNumber": 96,
            "title": "Janggut Putih & Kisah Kakek",
            "englishTitle": "White Beard & Grandpa's Stories",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Menghormati kakek nenek, menyimak dongeng kebijaksanaan, & kehangatan keluarga",
            "cover": "covers/story96_cover.jpg",
            "synopsis": "Di malam yang dingin berangin, Ciko duduk di atas karpet tebal di samping kursi goyang Kakek yang berjanggut putih selembut kapas. Di dekat perapian bata merah yang gemeretak hangat, Kakek menceritakan kisah tentang rusa emas penolong di hutan masa lalu, menidurkan Ciko dalam damai.",
            "protagonist": "Ciko (Anak laki-laki bertopi pet abu-abu)",
            "companion": "Kakek Ciko (Kakek tua berkursi goyang kayu jati)",
            "setting": "Ruang Keluarga Berperapian",
            "pages": [
                {
                    "number": 1,
                    "title": "Gemeretak Api di Perapian Bata",
                    "titleEn": "Crackling Fire in the Brick Hearth",
                    "textId": "Di luar rumah kayu di tepi bukit, angin malam berhembus kencang meniup pucuk-pucuk pohon cemara. Namun di dalam ruang keluarga, perapian bata merah menyala hangat dengan kayu bakar pohon asam yang gemeretak riang: 'Kletek, pletuk!' Cahaya api keemasan menari-nari di dinding.",
                    "textEn": "Outside the hillside cabin, the night wind blew chilly through pine boughs. But inside the family room, the brick hearth crackled warmly with dry logs: 'Snap, pop!' Golden firelight danced across the timber walls.",
                    "quote": "Kehangatan rumah adalah tempat perlindungan paling damai dari dinginnya dunia luar.",
                    "coReading": "Pernahkah kamu duduk dekat api unggun atau perapian yang hangat?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Cozy rustic living room with a glowing brick fireplace, stone hearth, and soft braided rug. Kind grandfather in spectacles and rocking chair, young boy Ciko sitting beside him, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Kursi Goyang Jati Kakek",
                    "titleEn": "Grandpa's Teak Rocking Chair",
                    "textId": "Kakek duduk di kursi goyang kayu jati tua warisan leluhur yang berderit tenang: 'Nguuut, krik... nguuut, krik...' Kakek memiliki janggut putih panjang yang terurai halus selembut kapas randu. Ciko duduk di atas bantal beludru hijau di samping lutut Kakek, menyandarkan kepalanya dengan manja.",
                    "textEn": "Grandpa sat in his heirloom teak rocking chair that creaked gently: 'Sway, creak... sway, creak...' Grandpa had a long white beard as soft as silk-cotton fluff. Ciko sat on a green velvet floor cushion by Grandpa's knee, leaning his head affectionately.",
                    "quote": "Kehadiran orang tua yang bijak memberi rasa damai yang tak tergantikan.",
                    "coReading": "Bagaimana suara kursi goyang Kakek saat bergerak perlahan?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up of kind grandfather with gentle eyes and flowing white beard stroking Ciko's hair. Ciko in cozy pajamas leaning against Grandpa's knee, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Permintaan Dongeng Masa Lalu",
                    "titleEn": "A Request for a Tale of Yesteryear",
                    "textId": "'Kakek, ceritakan padaku tentang masa ketika Kakek masih kecil di hutan seberang sungai,' pinta Ciko sambil memegang ujung janggut putih Kakek yang menggelitik telapak tangannya. Kakek tertawa renyah, suaranya berat dan dalam seperti gema seruling kayu.",
                    "textEn": "'Grandpa, tell me about the times when you were a little boy in the forest across the river,' Ciko asked, lightly touching Grandpa's fluffy white beard that tickled his palm. Grandpa chuckled warmly, his voice deep and comforting like an antique wooden horn.",
                    "quote": "Mendengarkan kisah orang tua adalah cara kita merajut sejarah keluarga.",
                    "coReading": "Kisah apa yang ingin didengarkan oleh Ciko?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Ciko looking up with shining round eyes at Grandpa who smiles tenderly. Fireplace glow illuminating their faces, tea mugs on a side table, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Kisah Rusa Emas Penunjuk Jalan",
                    "titleEn": "Tale of the Golden Guiding Deer",
                    "textId": "Kakek mulai bertutur perlahan. 'Dahulu kala, ketika Kakek tersesat saat mencari kayu bakar di hutan berkabut tebal, muncullah seekor rusa berbulu kuning keemasan. Rusa itu tidak lari, melainkan berjalan perlahan menoleh ke belakang, menuntun langkah Kakek melewati jurang terjal menuju batas desa.'",
                    "textEn": "Grandpa began his slow, melodic tale. 'Long ago, when I lost my way gathering firewood in a dense mountain mist, there appeared a deer with golden-yellow coat. The deer did not flee, but walked ahead turning gently, guiding my footsteps past steep ravines back to the village path.'",
                    "quote": "Pertolongan selalu datang dalam rupa yang tak terduga bila hati kita tetap tenang.",
                    "coReading": "Hewan apakah yang menolong Kakek di hutan berkabut?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Imaginary flashback scene in gentle golden mist: young boy Grandpa following a graceful glowing golden deer along a mossy forest trail. Whimsical fairytale atmosphere, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Pesan Kebaikan dari Sang Rusa",
                    "titleEn": "The Deer's Message of Kindness",
                    "textId": "'Rusa emas itu mengajarkan Kakek bahwa setiap kebaikan yang kita berikan pada hutan akan dibalas dengan perlindungan oleh semesta,' bisik Kakek sambil mengelus pundak Ciko. Ciko mendengarkan tanpa berkedip, membayangkan tanduk rusa yang berkilauan seperti mahkota daun.",
                    "textEn": "'That golden deer taught me that every kindness we offer to the wild forest returns as protection from the universe,' Grandpa whispered, patting Ciko's shoulder. Ciko listened without blinking, picturing the deer's antlers branching like leafy crowns.",
                    "quote": "Kebaikan yang ditanam tidak pernah hilang, ia selalu kembali pada kita.",
                    "coReading": "Apa pesan kebaikan yang diajarkan oleh rusa emas kepada Kakek?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Ciko looking into the flickering fireplace embers with dreamy eyes, seeing soft silhouettes of a deer among the glowing coals. Grandpa's arm around his shoulder, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Secangkir Cokelat Panas Berempah",
                    "titleEn": "A Cup of Spiced Hot Cocoa",
                    "textId": "Nenek datang membawakan dua cangkir tembikar berisi cokelat panas manis yang ditaburi kayu manis bubuk. Uap harumnya melayang menari di udara ruang keluarga. Ciko menyesap cokelatnya perlahan; kehangatan manis itu mengalir menyejukkan tenggorokannya.",
                    "textEn": "Grandma arrived carrying two earthenware mugs of rich hot cocoa dusted with sweet cinnamon. Fragrant steam curled through the family room air. Ciko sipped slowly; the sweet warmth flowed soothing his throat and heart.",
                    "quote": "Kenikmatan sederhana terasa begitu mewah saat dinikmati dalam kebersamaan.",
                    "coReading": "Minuman hangat apa yang dibawakan Nenek untuk Ciko dan Kakek?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Grandma handing a steaming ceramic mug of hot cocoa to Ciko beside the rocking chair. Warm embers glowing, cozy family warmth, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Kelopak Mata yang Mulai Berat",
                    "titleEn": "Eyelids Growing Heavy",
                    "textId": "Suara Kakek yang berirama tenang bagai nyanyian pengantar tidur berpadu dengan suara derit kursi goyang. Kelopak mata Ciko mulai terasa sangat berat. Ciko menyandarkan pipinya ke bantalan lutut wol Kakek, mendengarkan detak jam dinding yang tenang.",
                    "textEn": "Grandpa's soothing, rhythmic storytelling blended with the gentle creak of the rocking chair like a lullaby. Ciko's eyelids grew heavy as velvet. Ciko rested his cheek against Grandpa's woolen knee blanket, listening to the peaceful clock ticks.",
                    "quote": "Suara orang yang kita cintai adalah nyanyian paling menenangkan jiwa.",
                    "coReading": "Apakah Ciko sudah mulai mengantuk mendengarkan cerita Kakek?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Ciko resting his head sleepily on Grandpa's knee blanket, eyes half-closed in sweet drowsiness. Grandpa gently patting Ciko's back, firelight soft and low, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Gendongan Ayah Menuju Kamar",
                    "titleEn": "Father's Arms Carrying to Bed",
                    "textId": "Ayah melangkah masuk tanpa suara, lalu dengan lembut mengangkat Ciko ke dalam pelukan dadanya yang kokoh. Ciko tidak terbangun; ia hanya melingkarkan tangannya ke leher Ayah sambil bergumam pelan tentang si rusa emas.",
                    "textEn": "Father stepped in silently, gently lifting sleeping Ciko into his strong, warm arms. Ciko did not wake; he only hooked his sleepy arms around Father's neck, mumbling softly about the golden deer.",
                    "quote": "Pelukan orang tua adalah bahtera paling aman di malam hari.",
                    "coReading": "Siapa yang menggendong Ciko menuju tempat tidurnya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Father gently carrying sleeping Ciko in his arms down the wooden hallway toward the bedroom. Kakek smiling from his rocking chair by the fire, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Selimut Tebal yang Menyelimuti",
                    "titleEn": "Thick Quilt Tucked In",
                    "textId": "Ayah membaringkan Ciko di ranjang kayu pinusnya dan menyelimutinya dengan selimut tebal bermotif kotak-kotak hangat. Kakek datang ke pintu kamar, melambaikan tangan dengan senyum tulus berjanggut putihnya: 'Selamat tidur, cucu pemberani Kakek.'",
                    "textEn": "Father settled Ciko onto his pine bed and tucked a thick checkered quilt around him. Grandpa appeared at the bedroom doorway, waving with a gentle smile beneath his white beard: 'Sleep well, my brave little grandson.'",
                    "quote": "Doa tulus dari kakek nenek melingkupi tidur anak-anak dengan kedamaian abadi.",
                    "coReading": "Kata-kata manis apa yang dibisikkan Kakek sebelum Ciko tidur?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Ciko tucked warmly into bed, smiling in deep sleep. Grandpa in the doorway smiling with his hand raised in a gentle blessing, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Rusa Emas di Padang Bintang",
                    "titleEn": "Dreams of the Golden Deer in Star Fields",
                    "textId": "Malam semakin sunyi dan bulan sabit bersinar keperakan di atas pucuk-pucuk pohon cemara bukit. Di dalam mimpinya yang damai, Ciko menunggangi rusa emas menembus padang rumput bertabur bintang-bintang bercahaya, tertidur pulas dalam pelukan kasih sayang keluarganya.",
                    "textEn": "The night grew tranquil and the crescent moon shone silvery over the hilltop pines. In his peaceful dreams, Ciko rode the golden deer through starry meadows, sleeping soundly wrapped in his family's loving embrace.",
                    "quote": "Tidurlah dalam damai wahai anak terkasih, cerita para leluhur selalu menjagamu.",
                    "coReading": "Mari pejamkan mata dan rasakan kehangatan cerita kakek membawamu ke mimpi indah.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Ciko sleeping serenely in his bed. A dreamy golden deer silhouetted among stars and a smiling crescent moon outside the bedroom window. Deep peaceful bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 97: Donat Tabur Gula Nenek ---
        {
            "id": "story97",
            "storyNumber": 97,
            "title": "Donat Tabur Gula Nenek",
            "englishTitle": "Grandma's Sugar-Dusted Doughnuts",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Tradisi keluarga, kebahagiaan berbagi makanan manis, & kehangatan dapur nenek",
            "cover": "covers/story97_cover.jpg",
            "synopsis": "Ratih berkunjung ke rumah Nenek yang asri di desa. Bersama Nenek yang bersanggul rapi, Ratih belajar melubangi cincin donat kentang empuk menggunakan tutup botol, menggorengnya hingga kuning keemasan, dan mengocoknya di dalam toples gula halus putih seperti salju.",
            "protagonist": "Ratih (Gadis kecil berjemari putih gula)",
            "companion": "Nenek Ratih (Nenek bersanggul menyajikan nampan kayu)",
            "setting": "Dapur Nenek yang Asri",
            "pages": [
                {
                    "number": 1,
                    "title": "Dapur Desa Berjendela Lebar",
                    "titleEn": "Village Kitchen with Wide Windows",
                    "textId": "Dapur rumah Nenek di pedesaan selalu bermandikan sinar matahari pagi yang menembus jendela kayu lebar yang terbuka. Di luar jendela, rumpun pisang raja melambai ditiup semilir angin. Ratih, gadis cilik berambut ikal pendek, mengenakan celemek kain perca kecil, siap belajar rahasia donat kentang legendaris Nenek.",
                    "textEn": "Grandma's village kitchen was always bathed in morning sunshine pouring through wide open wooden windows. Outside, banana leaves swayed in the breeze. Ratih, a sweet curly-haired girl in a patchwork apron, was ready to learn the secrets of Grandma's legendary potato doughnuts.",
                    "quote": "Dapur nenek adalah tempat paling kaya akan aroma nostalgia dan kehangatan.",
                    "coReading": "Pernahkah kamu membuat kue donat bersama nenekmu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Ratih, a cute young girl in a floral patchwork apron, sitting at a wooden kitchen table watching Grandma in a neat hair bun mash boiled golden potatoes in a clay bowl. Sunlight pouring through window, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Kentang Rebus yang Dihaluskan",
                    "titleEn": "Mashed Boiled Potatoes",
                    "textId": "Nenek merebus kentang kuning pilihan hingga empuk. Dengan penumbuk kayu bulat, Ratih membantu menumbuk kentang itu di dalam mangkuk tanah liat hingga menjadi adonan lumat yang lembut seperti bubur bayi. 'Kentang inilah rahasia agar donat kita tetap empuk sepanjang hari, Ratih,' bisik Nenek.",
                    "textEn": "Grandma boiled golden potatoes until fork-tender. With a round wooden masher, Ratih helped crush them in a clay bowl into a mash as smooth as baby purée. 'Potatoes are the secret that keeps our doughnuts pillow-soft all day, Ratih,' whispered Grandma.",
                    "quote": "Bahan alami yang tulus memberikan kelezatan yang tak tertandingi.",
                    "coReading": "Mengapa donat buatan Nenek diberi campuran kentang rebus?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Ratih using a wooden masher to crush golden steamed potatoes in a rustic bowl. Grandma adding flour and eggs, sunny kitchen ambiance, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Adonan Bulat yang Mengembang Cantik",
                    "titleEn": "Dough Balls Rising Beautifully",
                    "textId": "Setelah dicampur tepung, telur kampung, dan mentega wangi, adonan diuleni hingga kalis dan didiamkan hingga mengembang bulat seperti bantal tidur. Ratih membagi adonan menjadi bola-bola kecil seukuran bola tenis meja dan menatanya di atas nampan kayu yang ditaburi tepung.",
                    "textEn": "Mixed with flour, farm eggs, and sweet butter, the dough was kneaded springy and left to rise into puffy mounds like little cushions. Ratih divided it into ping-pong-sized balls, lining them on a flour-dusted wooden tray.",
                    "quote": "Kerapian menata membuat proses memasak terasa menyenangkan.",
                    "coReading": "Berapa banyak bola donat kecil yang berhasil dibuat Ratih?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Ratih rolling smooth dough balls between her palms, placing them on a wooden board sprinkled with white flour. Flour dust on her nose, Grandma smiling warmly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Melubangi Tengah dengan Tutup Botol",
                    "titleEn": "Poking the Center Hole with a Bottle Cap",
                    "textId": "Nenek memberikan sebuah tutup botol selai kecil yang bersih. Ratih menekan tutup botol itu tepat di tengah setiap bulatan adonan: 'Pletuk!' Bagian tengah adonan terpotong rapi, membentuk cincin donat yang menggemaskan dengan sebuah kelereng adonan kecil di sampingnya.",
                    "textEn": "Grandma handed over a clean, round jam jar lid. Ratih pressed the lid right into the center of each dough ball: 'Pop!' The middle popped out cleanly, forming an adorable doughnut ring with a tiny dough ball beside it.",
                    "quote": "Kreativitas menggunakan alat sederhana melahirkan bentuk yang sempurna.",
                    "coReading": "Alat apa yang digunakan Ratih untuk membuat lubang di tengah donat?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Close-up of Ratih's hands using a round cap to punch out the center hole of a plump dough ring on the floured wooden table. Delightful pastry making scene, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Minyak Kelapa yang Berdesir Hangat",
                    "titleEn": "Sizzling Coconut Oil in the Wok",
                    "textId": "Di atas kompor tanah liat, wajan besi Nenek berisi minyak kelapa murni yang harum. Ketika Nenek menurunkan cincin donat pertama menggunakan sumpit bambu panjang, minyak berdesir riang: 'Kecesss!' Gelembung-gelembung minyak menari mengelilingi donat yang mengapung ringan.",
                    "textEn": "On the clay stove, Grandma's cast-iron wok was filled with fragrant pure coconut oil. As Grandma lowered the first doughnut ring using long bamboo chopsticks, the oil sizzled merrily: 'Sizzle!' Tiny oil bubbles danced around the floating, bobbing pastry.",
                    "quote": "Kehati-hatian di dekat api dapur menjaga keselamatan kita bersama.",
                    "coReading": "Bagaimana suara minyak saat donat dimasukkan ke dalam wajan?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Grandma safely frying golden doughnuts in a deep wok with long wooden chopsticks. Ratih watching from a safe step back with wide curious eyes, warm kitchen light, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Warna Kuning Keemasan yang Menggoda",
                    "titleEn": "Tempting Golden-Brown Hue",
                    "textId": "Hanya dalam beberapa menit, donat itu mengembang semakin gemuk dan berubah warna menjadi cokelat keemasan yang berkilau. Nenek membaliknya sekali saja agar kedua sisinya matang merata, lalu meniriskannya di atas saringan kawat bambu.",
                    "textEn": "In just a few minutes, the doughnuts puffed plumper, turning into a shiny golden-brown. Grandma flipped them just once so both sides cooked evenly, then lifted them onto a bamboo wire strainer.",
                    "quote": "Kematangan yang pas melahirkan kerenyahan di luar dan kelembutan di dalam.",
                    "coReading": "Warna apa yang menandakan donat sudah matang sempurna?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. A tray of fresh, puffy, golden-brown fried doughnuts cooling on a woven bamboo rack, steam rising gently. Ratih sniffing the sweet aroma with hands clasped, naive folk art, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Toples Ajaib Salju Gula Halus",
                    "titleEn": "The Magic Powdered Sugar Jar",
                    "textId": "Setelah donat agak dingin dan hangat-hangat kuku, Nenek menyiapkan toples kaca besar berisi gula halus putih selembut salju. Nenek memasukkan dua buah donat ke dalam toples dan menutupnya rapat: 'Sekarang tugasmu, Ratih: kocok toples ini seperti menari!'",
                    "textEn": "Once the doughnuts cooled to warm to the touch, Grandma brought out a large glass jar filled with powdered sugar as fine as snow. She dropped two doughnuts inside and sealed the lid: 'Now your task, Ratih: shake the jar like dancing!'",
                    "quote": "Menyelesaikan pekerjaan dengan tawa membuat rasa makanan berlipat lezatnya.",
                    "coReading": "Apa yang dilakukan Ratih dengan toples gula halus itu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Ratih shaking a large glass jar filled with white powdered sugar and golden doughnuts, laughing joyfully with her whole body swaying. Grandma smiling beside her, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Donat Berselimut Salju Manis",
                    "titleEn": "Doughnuts Wrapped in Sweet Snow",
                    "textId": "'Kocok, kocok, goyang!' Ratih mengguncang toples ke atas dan ke bawah. Ketika tutupnya dibuka, tampak donat-donat itu telah terselimuti bedak gula putih salju yang tebal dan merata. Jemari tangan dan ujung hidung Ratih ikut berlumur gula putih yang manis.",
                    "textEn": "'Shake, shake, shimmy!' Ratih shook the jar up and down. When the lid popped open, the doughnuts were completely coated in a thick, even blanket of powdery sweet snow. Ratih's fingertips and the tip of her nose were dusted white too.",
                    "quote": "Keceriaan yang berlepotan manis adalah kenangan masa kecil yang paling berharga.",
                    "coReading": "Lihatlah hidung Ratih terkena gula putih, lucu sekali ya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Ratih lifting a sugar-dusted doughnut from the jar, with a white powdered sugar smudge on the tip of her cute nose. Grandma laughing lovingly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Gigitan Pertama yang Meleleh di Lidah",
                    "titleEn": "First Bite That Melts on the Tongue",
                    "textId": "Di beranda belakang, Ratih dan Nenek duduk menikmati donat tabur gula bersama secangkir teh melati hangat. Ratih menggigit donatnya: 'Kres!' bagian luarnya renyah ringan dan bagian dalamnya begitu empuk dan wangi kentang. Gula manisnya meleleh hangat di lidah Ratih.",
                    "textEn": "On the back porch, Ratih and Grandma sat enjoying the sugar doughnuts with warm cups of jasmine tea. Ratih took a bite: 'Crunch!' crisp on the outside, and delightfully pillowy soft inside with sweet potato aroma. The sweet sugar melted on her tongue.",
                    "quote": "Makanan buatan rumah yang dimasak bersama keluarga selalu memiliki rasa cinta tak ternilai.",
                    "coReading": "Bagaimana tekstur donat kentang buatan Nenek saat digigit?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Ratih taking a happy bite of the powdered sugar doughnut on the sunny veranda with Grandma. Sugar powder dust on their smiling cheeks, teacups steaming on the wooden table, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Pulas Beraroma Gula Salju",
                    "titleEn": "Sound Sleep Scented of Powdered Snow",
                    "textId": "Malam tiba dan angin pedesaan berhembus menyejukkan kamar tidur Nenek yang wangi kayu manis. Di atas ranjang berkelambu putih halus, Ratih tidur pulas dipeluk selimut perca hangat. Di dalam mimpinya, ia berjalan-jalan di bukit salju gula yang manis bersama Nenek tercintanya.",
                    "textEn": "Night arrived and the village breeze cooled Grandma's cinnamon-scented bedroom. On the bed draped in sheer white netting, Ratih slept deeply wrapped in a warm patchwork quilt. In sweet dreams, she wandered rolling hills of powdered sugar alongside her beloved Grandma.",
                    "quote": "Tidurlah dalam manisnya kasih sayang, esok hari penuh kehangatan baru menantimu.",
                    "coReading": "Mari pejamkan mata dan rasakan kehangatan pelukan nenek mengantar tidur lelapmu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Ratih sleeping peacefully in Grandma's guest room under a soft mosquito net and patchwork quilt. White lace curtains fluttering gently in night breeze, crescent moon and stars outside window. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
