# scripts/build_batch_44_to_47.py
import json

def get_stories_44_to_47():
    stories = []

    # =========================================================================
    # STORY 44: Kompas Daun di Aliran Air
    # =========================================================================
    s44 = {
        "id": "kompas-daun-alir",
        "storyNumber": 44,
        "title": "Kompas Daun di Aliran Air",
        "englishTitle": "The Floating Leaf Compass",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 4–7 Tahun",
        "moralTheme": "Membaca tanda-tanda alam, tetap tenang saat tersesat, dan kepintaran observasi",
        "cover": "images/story44_cover.jpg",
        "coverImage": "images/story44_cover.jpg",
        "synopsis": "Nico si anak pramuka cilik kehilangan arah di tengah rimbunnya hutan pinus. Bersama Kancil Mini yang cermat, Nico belajar mengamati aliran sungai kecil dan menggunakan sehelai daun oak kuning sebagai kompas alami untuk memandu jalan pulang.",
        "synopsisEn": "Little cub scout Nico loses his way in the dense pine forest. With sharp-eyed Kancil Mini by his side, Nico learns to observe the gentle flow of a forest creek and uses a floating oak leaf as a natural compass pointing the way home.",
        "protagonist": "Nico (Anak pramuka cilik 6 tahun bertopi baret cokelat dan berompi saku)",
        "companion": "Kancil Mini (Kancil cerdas bertotol putih dengan kalung lonceng kayu)",
        "setting": "Hutan Belantara Rindang & Aliran Sungai Kerikil Bening",
        "pages": [
            {
                "number": 1,
                "title": "Pohon-Pohon yang Tampak Sama",
                "titleEn": "Trees That All Look Alike",
                "textId": "Matahari sore menyelinap di antara celah dahan pinus yang tinggi. Nico berdiri memegang tali ranselnya, menatap ke sekeliling. Jalan setapak yang tadi ia lewati seolah menghilang, tertutup karpet tebal jarum pinus kering yang seragam.",
                "textEn": "The afternoon sun peeked through the high canopy of towering pine branches. Nico stood clutching his backpack straps, looking all around. The trail he had followed seemed to have vanished under a thick carpet of uniform pine needles.",
                "quote": "🌲 'Saat jalanan terasa membingungkan, hal pertama yang harus kita lakukan adalah berhenti dan diam sejenak.'",
                "coReading": "💡 Tanya si Kecil: Apa yang harus kamu lakukan jika terpisah dari orang tuamu di tempat umum?",
                "imagePrompt": "Charming children's book illustration of little scout boy Nico in a brown beret and scout vest standing thoughtfully in a tranquil pine forest. Handcrafted wax crayon and chalky oil pastel on textured cream paper, simple black bead eyes, 4:3 landscape, completely text-free."
            },
            {
                "number": 2,
                "title": "Dentingan Lonceng Kancil Mini",
                "titleEn": "Kancil Mini's Wooden Chime",
                "textId": "Kling... klung... Dari balik rimbun pakis liar, muncullah Kancil Mini dengan kalung lonceng kayu kecilnya. \"Jangan panik, Nico! Hutan ini sahabat kita. Hutan selalu memberikan petunjuk jika kita mendengarkan dengan seksama.\"",
                "textEn": "Clink... clonk... From behind a thicket of wild ferns appeared Kancil Mini wearing a little wooden chime. \"Don't fret, Nico! This forest is our friend. It always whispers gentle clues if we pause and listen closely.\"",
                "quote": "🦌 'Ketenangan adalah kunci pertama untuk menemukan kembali jalan yang hilang.'",
                "coReading": "💡 Aktivitas Seru: Pejamkan mata dan dengarkan suara terkecil yang bisa kamu tangkap sekarang!",
                "imagePrompt": "A delightful storybook illustration of Kancil Mini the mouse-deer emerging from lush green ferns, looking up at Nico with warm reassuring eyes. Soft forest shadows, wax crayon textures, 4:3 landscape, completely text-free."
            },
            {
                "number": 3,
                "title": "Gemercik Air yang Berbisik",
                "titleEn": "The Whispering Water Stream",
                "textId": "Kancil Mini memiringkan telinganya yang runcing. \"Dengarkan, Nico! Bunyi gemercik itu!\" Di balik bukit berbatu, terdengar senandung air mengalir pelan: kricik, kricik, kricik. Air sungai selalu tahu ke mana ia harus mengalir.",
                "textEn": "Kancil Mini cocked his pointed ears. \"Listen, Nico! That trickling sound!\" Behind the rocky ridge came the sweet bubbling murmur of running water: splash, ripple, gurgle. A forest stream always knows where it is bound.",
                "quote": "💧 'Air selalu mengalir menuju tempat yang lebih rendah, menuju lembah dan desa kita.'",
                "coReading": "💡 Tanya si Kecil: Ke mana biasanya air sungai mengalir?",
                "imagePrompt": "Whimsical children's picture book scene of scout boy Nico and Kancil Mini following the sound of water toward a glistening woodland brook bordered by rounded river stones and moss, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Sehelai Daun Oak Kuning Emas",
                "titleEn": "A Golden-Yellow Oak Leaf",
                "textId": "Di tepi sungai kecil yang jernih, Nico memungut sehelai daun oak kuning cerah yang gugur. \"Ini kompas kita!\" seru Kancil Mini. Daun itu berbentuk seperti perahu mungil yang siap mengarungi petualangan riam air.",
                "textEn": "By the bank of the clear woodland creek, Nico picked up a fallen golden-yellow oak leaf. \"Here is our compass!\" chirped Kancil Mini. The leaf was shaped just like a tiny sailboat, eager to navigate the gentle ripples.",
                "quote": "🍂 'Benda yang paling sederhana di alam bisa menjadi penolong yang paling berharga.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu menghanyutkan daun di atas air seperti perahu mini?",
                "imagePrompt": "Close-up storybook illustration of little Nico's hands holding a dry golden oak leaf shaped like a canoe, resting near clear swirling creek water with smooth colorful pebbles below. Handcrafted wax crayon, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Perahu Daun Menari di Arus",
                "titleEn": "The Leaf Boat Dances on Current",
                "textId": "Nico meletakkan daun oak itu perlahan ke atas permukaan air. Fyuuh! Daun itu berputar anggun, lalu meluncur lincah mengikuti arus air yang tenang, membelah bayangan pohon pinus di air.",
                "textEn": "Nico gently placed the oak leaf upon the water's cool skin. Swish! The leaf pirouetted gracefully, then drifted smoothly along the steady current, gliding over the reflected pine tree shadows.",
                "quote": "⛵ 'Mengikuti arus kebaikan alam akan selalu membawa kita pulang dengan selamat.'",
                "coReading": "💡 Aktivitas Seru: Tiup sehelai kertas tipis di mejamu agar meluncur seperti perahu daun!",
                "imagePrompt": "A charming children's illustration of the bright yellow leaf boat floating serenely downstream on clear turquoise water, while Nico and Kancil walk along the pebbled bank alongside it. Wax crayon and pastel, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Lumut Hijau Penunjuk Utara",
                "titleEn": "Green Moss the North Pointer",
                "textId": "Sambil menyusuri tepian sungai, Kancil Mini menunjuk ke batang pohon kenari tua. \"Lihat lumut tebal di sisi pohon ini, Nico! Lumut hijau selalu tumbuh lebih subur di sisi yang terlindung dari terik matahari.\"",
                "textEn": "As they strolled along the creek bank, Kancil Mini pointed to the trunk of an old walnut tree. \"Look at the thick moss on this side, Nico! Green moss always grows lusher on the cool, shaded northern bark.\"",
                "quote": "🌱 'Pohon dan lumut adalah buku cerita alam yang terbuka lebar bagi mereka yang mau belajar.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu meraba lumut pohon yang terasa empuk seperti beludru?",
                "imagePrompt": "Touching illustration of Nico touching soft green velvet moss on an old tree trunk with wonder, as Kancil explains the secret signs of nature. Golden sun filtering through branches, wax crayon texture, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Jembatan Batu Penyeberangan",
                "titleEn": "The Stepping Stone Bridge",
                "textId": "Di depan mereka, sungai menyempit dan ada deretan batu pipih yang membentuk jembatan alami. Satu per satu, Nico melompati batu-batu itu dengan seimbang. Kancil Mini melompat ringan mendampinginya.",
                "textEn": "Ahead of them, the stream narrowed, revealing a natural bridge of flat stepping stones. One by one, Nico hopped across with steady balance. Kancil Mini bounded lightly beside him in joyful companionship.",
                "quote": "🪨 'Setiap batu pijakan adalah jembatan kepercayaan diri yang kita bangun sendiri.'",
                "coReading": "💡 Aktivitas Seru: Melompatlah pelan dari satu lantai ubin ke ubin lain seperti menyeberang batu kali!",
                "imagePrompt": "Vibrant and cheerful children's book scene of scout boy Nico balancing on smooth stepping stones across a shallow brook, holding his arms out for balance, with Kancil hopping ahead. Soft wax crayon marks, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Aroma Asap Dapur dan Atap Merah",
                "titleEn": "Woodsmoke Aroma and Red Rooftops",
                "textId": "Saat aliran sungai berbelok di balik rumpun bambu, aroma sedap kayu bakar dan uap sup jagung tercium di udara. Di ujung lembah, atap merah rumah Nico tampak menyembul di antara pepohonan desa!",
                "textEn": "As the stream bent around a bamboo grove, the sweet aroma of woodsmoke and hot sweetcorn soup drifted through the air. At the valley's edge, the familiar red tile roof of Nico's home peeked through the trees!",
                "quote": "🏡 'Aroma rumah selalu menjadi lentera paling hangat yang menuntun langkah pulang.'",
                "coReading": "💡 Tanya si Kecil: Aroma masakan apa yang paling membuatmu merasa senang saat tiba di rumah?",
                "imagePrompt": "Heartwarming illustration of Nico emerging from the forest edge, spotting his cozy village house with smoking chimney in the meadow below. Golden sunset lighting up the valley, wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Lambaian Tangan Ibu di Pintu Pagar",
                "titleEn": "Mother's Wave by the Garden Gate",
                "textId": "Di depan pagar kebun, Ibu berdiri melambaikan tangan dengan senyum lega. Nico berlari memeluk Ibu erat-erat sambil menunjukkan daun oak kuning di tangannya. \"Ibu, aku menemukan jalan pulang berkat kompas daun!\"",
                "textEn": "By the garden gate, Mother stood waving with a relieved, beaming smile. Nico dashed into her warm embrace, proudly holding up his golden oak leaf. \"Mama, I found the way back with a magic leaf compass!\"",
                "quote": "💛 'Kekhawatiran yang berakhir dengan pelukan hangat adalah rasa syukur terindah di dunia.'",
                "coReading": "💡 Peluk si Kecil: Peluk si kecil erat dan katakan kamu selalu menunggu kehadirannya di rumah.",
                "imagePrompt": "Tender children's book scene of Mother kneeling to hug scout boy Nico at the rustic garden gate, surrounded by blooming sunflowers. Kancil Mini watches with a warm smile from the forest edge, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Tenang di Kamar Berbintang",
                "titleEn": "Tranquil Sleep in the Starry Room",
                "textId": "Malam itu, daun oak kuning diletakkan rapi di atas meja belajar Nico di samping baret cokelatnya. Di balik selimut hangat, Nico memejamkan mata dengan tenang, diiringi desau angin malam yang menuntunnya ke alam mimpi yang damai. Selamat tidur, penjelajah cilik.",
                "textEn": "That night, the golden oak leaf rested neatly upon Nico's study desk right beside his brown beret. Tucked beneath his warm quilt, Nico closed his eyes in serene peace, guided by the soothing night wind into sweet slumber. Goodnight, brave little scout.",
                "quote": "🌙 'Alam selalu menjaga mereka yang memperhatikannya dengan cinta dan rasa hormat.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak pintar, terima kasih sudah belajar mengamati dunia dengan teliti hari ini.",
                "imagePrompt": "A peaceful bedtime illustration of boy Nico sleeping soundly in his rustic bedroom under a green quilt. The golden oak leaf sits on the wooden desk beneath moonlight through the window. Wax crayon on heavy watercolor paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s44)

    # =========================================================================
    # STORY 45: Gerobak Kayu Beroda Tiga
    # =========================================================================
    s45 = {
        "id": "gerobak-roda-tiga",
        "storyNumber": 45,
        "title": "Gerobak Kayu Beroda Tiga",
        "englishTitle": "The Three-Wheeled Wooden Cart Ride",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 4–7 Tahun",
        "moralTheme": "Kerjasama, kerja keras yang menyenangkan, dan rasa bangga membantu keluarga",
        "cover": "images/story45_cover.jpg",
        "coverImage": "images/story45_cover.jpg",
        "synopsis": "Gilang si anak petani kecil mendapat tugas mengangkut labu-labu kuning raksasa dari kebun menuju lumbung desa. Bersama Boni si anak sapi tutul penarik gerobak, mereka melintasi jalan setapak berbunga dengan gerobak kayu beroda tiga yang berderit riang.",
        "synopsisEn": "Little farmer Gilang is entrusted with transporting giant golden pumpkins from the field to the village granary. With Boni the spotted calf pulling their cheerful three-wheeled wooden cart, they journey along flowering village lanes filled with laughter.",
        "protagonist": "Gilang (Anak petani cilik 5 tahun bersandal karet dan bertopi jerami lebar)",
        "companion": "Boni (Anak sapi putih bertutul hitam dengan pita lonceng tembaga)",
        "setting": "Kebun Labu Kuning & Jalan Desa Berbunga Matahari",
        "pages": [
            {
                "number": 1,
                "title": "Panen Labu Kuning Raksasa",
                "titleEn": "Harvesting the Giant Golden Pumpkins",
                "textId": "Matahari pagi menyinari kebun sayur desa yang subur. Di atas tanah gembur, terhampar labu-labu kuning tua yang bulat besar dan berkilau seperti emas matang. Gilang menepuk salah satu labu: duk-duk! Labu ini sudah manis dan siap dipanen.",
                "textEn": "The morning sun beamed down upon the lush village vegetable patch. Nestled in rich dark soil were giant golden-orange pumpkins, round and gleaming like ripe treasures. Gilang patted a big pumpkin: thump-thump! It was sweet and ready for harvest.",
                "quote": "🎃 'Melihat hasil tanaman yang tumbuh subur memberi rasa syukur yang meluap di dada.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat buah labu kuning yang besar di pasar?",
                "imagePrompt": "Charming children's book illustration of little farmer boy Gilang in denim overalls and wide straw hat, standing in a sunny pumpkin patch beside huge round golden pumpkins. Handcrafted wax crayon and oil pastel on textured paper, simple black bead eyes, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Gerobak Berderit yang Setia",
                "titleEn": "The Faithful Creaking Cart",
                "textId": "Kakek mengeluarkan gerobak kayu tua beroda tiga dari gudang jerami. Dua roda besar dari kayu jati di belakang, dan satu roda kemudi kecil di depan. \"Gerobak ini sudah berumur, tetapi tenaganya masih sekuat kuda beban!\" kata Kakek sambil tertawa.",
                "textEn": "Grandpa rolled out the old three-wheeled wooden cart from the straw barn. Two tall teakwood wheels sat in the back, with one smaller steering wheel up front. \"This cart is old, but it carries loads as strong as a sturdy pony!\" laughed Grandpa.",
                "quote": "🛒 'Benda-benda tua yang dirawat dengan baik selalu menyimpan banyak cerita kebaikan.'",
                "coReading": "💡 Tanya si Kecil: Berapa roda gerobak kayu Gilang? Coba hitung bersama: Satu, dua, tiga!",
                "imagePrompt": "Whimsical storybook scene of an old rustic three-wheeled wooden cart with carved handles parked by a barn. Grandpa and Gilang inspect the sturdy wooden spokes. Warm sunlight, crayon textures on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Boni Si Anak Sapi Penarik",
                "titleEn": "Boni the Spotted Little Calf",
                "textId": "Mooo! Boni si anak sapi putih bertutul hitam melangkah riang dengan lonceng tembaga yang berdenting merdu di lehernya. Gilang mengelus hidung basah Boni yang lembut. \"Hari ini kita bertualang bersama, Boni!\"",
                "textEn": "Mooo! Boni the little white calf with black spots trotted merrily, a small copper bell jingling merrily around his neck. Gilang gently stroked Boni's soft, damp snout. \"Today we embark on an adventure together, dear Boni!\"",
                "quote": "🐮 'Hewan sahabat yang diperlakukan dengan penuh kasih akan selalu membalas dengan kesetiaan.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara anak sapi Boni yang ramah: 'Moo-oo-oo!'",
                "imagePrompt": "A heartwarming children's illustration of Boni the cute spotted calf nuzzling Gilang's cheek affectionately. Boni wears a tiny woven harness attached to the wooden cart. Soft wax crayon blending, naive folk art, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Menyusun Labu di Atas Jerami",
                "titleEn": "Arranging Pumpkins on Soft Straw",
                "textId": "Gilang dan Ayah meletakkan lapisan jerami kering di dasar gerobak agar labu tidak terbentur. Satu, dua, tiga labu kuning besar disusun rapi berdampingan. Gerobak kini penuh berisi keajaiban hasil bumi yang harum tanah.",
                "textEn": "Gilang and Father laid a bed of dry golden straw across the cart bottom to cushion the harvest. One, two, three giant pumpkins were arranged snugly side-by-side. The cart was now brimming with the fragrant bounty of the earth.",
                "quote": "🌾 'Bekerja dengan cermat dan hati-hati membuat hasil panen tetap utuh dan sempurna.'",
                "coReading": "💡 Tanya si Kecil: Mengapa jerami diletakkan di bawah buah labu yang berat?",
                "imagePrompt": "Charming picture book scene of Gilang and his father carefully lifting a huge golden pumpkin onto the straw-lined wooden cart. Warm harvest palette, amber, olive green, and earthy terracotta crayon strokes, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Roda Kayu Mulai Berputar",
                "titleEn": "Wooden Wheels Begin to Turn",
                "textId": "Krek-krek-krek! Gilang memegang kendali tali rami, dan Boni melangkah mantap. Roda kayu berputar di atas jalan setapak tanah liat. Suara derit kayu dan denting lonceng berpadu menjadi lagu kerja yang menyenangkan.",
                "textEn": "Creak-clack-roll! Gilang held the gentle hemp reins, and Boni stepped forward with steady stride. The wooden wheels turned along the packed clay trail. The creak of teak and the chime of the bell blended into a cheerful work song.",
                "quote": "🎵 'Pekerjaan yang dilakukan bersama sahabat selalu terasa seringan lagu nyanyian.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara roda gerobak kayu: 'Krek-krek-krek, krek-krek-krek!'",
                "imagePrompt": "Vibrant storybook illustration of boy Gilang walking alongside the three-wheeled cart pulled gently by spotted calf Boni, traveling down a sun-dappled village dirt road lined with blooming sunflowers, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Menyapa Kawan di Pinggir Kebun",
                "titleEn": "Greeting Friends Along the Garden Lane",
                "textId": "Di sepanjang jalan, para petani dan anak-anak desa melambaikan tangan sambil tersenyum. Bebek-bebek sawah berbaris di parit membunyikan 'Kwek-kwek!' menyemangati rombongan gerobak labu kuning Gilang.",
                "textEn": "Along the lane, village farmers and smiling children waved warmly from their porches. White farm ducks waddled along the irrigation ditch, quacking 'Quack-quack!' in cheerful parade alongside Gilang's pumpkin caravan.",
                "quote": "🦆 'Senyuman dan lambaian ramah tetangga adalah pelumas terbaik bagi roda kehidupan desa.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana caramu menyapa tetangga yang kamu temui di jalan?",
                "imagePrompt": "Delightful children's illustration showing smiling village neighbors and marching yellow ducklings waving as Gilang's pumpkin cart rolls past a quaint village fence. Warm cheerful tones, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Tanjakan Kecil Menuju Balai Desa",
                "titleEn": "The Little Hill to the Village Hall",
                "textId": "Di depan balai desa, ada tanjakan kecil berpasir. Boni menarik napas dan melangkah lebih kuat. Gilang tidak tinggal diam; ia ikut mendorong bagian belakang gerobak dengan sekuat tenaga: \"Satu, dua, doroong!\"",
                "textEn": "Before the village hall stood a gentle sandy slope. Boni dug his hooves into the earth with determination. Gilang did not just stand by; he leaned his shoulder against the back of the cart, pushing with all his might: \"One, two, heeeave!\"",
                "quote": "💪 'Saling membantu membagi beban membuat tanjakan terberat pun bisa terlampaui.'",
                "coReading": "💡 Latihan Bersama: Coba dorong dinding dengan kedua telapak tanganmu sambil berkata: 'Doroong!'",
                "imagePrompt": "Inspiring children's book scene of little Gilang pushing the back of the wooden cart with earnest determination while calf Boni pulls from the front, cresting the small hill together. Crayon scribbles, warm dynamic lighting, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Tiba di Lumbung Desa dengan Selamat",
                "titleEn": "Safe Arrival at the Village Granary",
                "textId": "HUP! Roda gerobak berhenti tepat di depan pintu lumbung desa. Kepala desa dan warga bersorak menyambut mereka. Tiga labu kuning raksasa mendarat dengan utuh tanpa goresan sedikit pun. Gilang tersenyum lebar dengan pipi kemerahan.",
                "textEn": "HUP! The cart wheels rolled to a halt right before the great timber doors of the village granary. The village elder and neighbors cheered in warm celebration. The three giant pumpkins had arrived without a single scratch. Gilang beamed with rosy cheeks.",
                "quote": "🌟 'Tanggung jawab yang dituntaskan dengan baik memberikan kebanggaan yang tak ternilai.'",
                "coReading": "💡 Berikan Pujian: Berikan pelukan hangat pada si kecil atas bantuannya membereskan mainan hari ini!",
                "imagePrompt": "Celebratory illustration of village villagers admiring the enormous golden pumpkins delivered by Gilang. A friendly elder pats Gilang's straw hat with pride, while Boni the calf munches fresh grass. Warm crayon folk art, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Semangkuk Kolak Labu Hangat",
                "titleEn": "A Warm Bowl of Pumpkin Sweet Stew",
                "textId": "Sebagai hadiah kerja keras, Nenek menyajikan semangkuk kolak labu kuning berkuah santan gula kelapa yang harum daun pandan. Gilang menyuap kuah manis itu dengan lahap, sementara Boni menikmati seikat jerami manis di samping bale-bale.",
                "textEn": "As a reward for their honest labor, Grandmother ladled out bowls of sweet pumpkin stew simmered with rich coconut milk and fragrant pandan leaves. Gilang savored the sweet, warm treat, while Boni contentedly chewed sweet fresh clover nearby.",
                "quote": "🥣 'Makanan yang dimasak dari hasil jerih payah sendiri terasa seratus kali lebih lezat.'",
                "coReading": "💡 Tanya si Kecil: Makanan apa yang dibuat dari labu kuning yang paling kamu sukai?",
                "imagePrompt": "Cozy picture book scene of boy Gilang sitting on a rustic wooden bench eating warm pumpkin soup from a coconut bowl, with calf Boni resting peacefully beside him under sunset-lit eaves. Handcrafted wax crayon on textured paper, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Nyenyak di Ranjang Jerami",
                "titleEn": "Deep Slumber in the Hay Loft",
                "textId": "Malam melingkupi desa tani yang damai. Di loteng rumah panggung yang beralaskan jerami wangi, Gilang tidur lelap memeluk selimut sarungnya. Roda gerobak beristirahat di bawah naungan pohon randu. Selamat tidur, petani cilik yang hebat.",
                "textEn": "Night enveloped the tranquil farming village in soft indigo. In the airy loft scented with sweet dried grass, Gilang slept deeply wrapped in his soft sarong quilt. Down below, the wooden cart rested peacefully beneath the stars. Goodnight, brave little farmer.",
                "quote": "🌙 'Tidurlah dengan rasa bangga, karena tangan kecilmu telah membawa banyak kebaikan hari ini.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak hebat, terima kasih sudah menjadi penolong yang rajin dan penuh kasih.",
                "imagePrompt": "Serene bedtime illustration of boy Gilang sleeping soundly in a cozy loft bed under glowing moonlight, a straw hat resting on the peg. Down in the yard, calf Boni sleeps under a starry sky beside the cart. Wax crayon and soft oil pastel, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s45)

    # =========================================================================
    # STORY 46: Pai Apel Delapan Potong
    # =========================================================================
    s46 = {
        "id": "pai-apel-delapan-potong",
        "storyNumber": 46,
        "title": "Pai Apel Delapan Potong",
        "englishTitle": "The Eight-Slice Apple Tart",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Kedermawanan, keadilan membagi sama rata, dan kehangatan berbagi makanan",
        "cover": "images/story46_cover.jpg",
        "coverImage": "images/story46_cover.jpg",
        "synopsis": "Bramble si landak bulat memanggang pai apel kayu manis yang harum di Toko Roti Pohon Oak. Saat delapan sahabat hutan datang berkunjung kedinginan, Bramble dan Squeak belajar memotong pai bulat itu menjadi delapan potong segitiga yang sama persis agar semua kebagian kehangatan.",
        "synopsisEn": "Bramble the plump hedgehog bakes a fragrant cinnamon apple tart in the Oak Tree Bakery. When eight woodland friends arrive in the chilly evening, Bramble and Squeak learn to slice the round pie into eight equal pieces so every guest shares the warm comfort.",
        "protagonist": "Bramble (Landak bulat ramah bersarung tangan rajut merah dan celemek tepung)",
        "companion": "Squeak (Tupai lincah bermata bulat dengan topi kulit kenari)",
        "setting": "Toko Roti Pohon Oak yang Hangat Berbau Kayu Manis",
        "pages": [
            {
                "number": 1,
                "title": "Aroma Apel Panggang dari Tungku",
                "titleEn": "Cinnamon Apple Aroma from the Oven",
                "textId": "Sore di Hutan Hazel terasa dingin berangin. Namun di dalam Toko Roti Pohon Oak, udara begitu hangat dan berbau manis kayu manis. Bramble si landak bulat mengeluarkan seloyang pai apel bundar berkerak keemasan dari tungku batu.",
                "textEn": "The evening in Hazel Woods blew crisp and chilly. But inside the Oak Tree Bakery, the air was deliciously warm and perfumed with sweet cinnamon. Bramble the plump hedgehog drew a round, golden-crusted apple tart from the stone hearth.",
                "quote": "🥧 'Aroma kue yang baru matang selalu membawa kehangatan ke setiap sudut ruangan.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu mencium bau kue yang baru saja keluar dari oven?",
                "imagePrompt": "Charming children's book illustration of plump hedgehog Bramble in a floury baker's apron and red knitted mitts, proudly taking a golden-brown round apple pie out of a glowing stone oven. Squeak the squirrel watches with glee. Handcrafted wax crayon and oil pastel on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Ketukan di Pintu Toko Roti",
                "titleEn": "Knocks at the Bakery Door",
                "textId": "Tok-tok-tok! Suara ketukan kecil terdengar di pintu kayu bundar. Saat Squeak membukanya, berdirilah kawan-kawan hutan yang kedinginan: dua kelinci kecil, seekor luwak pemalu, dua burung gelatik, dan seekor musang kecil bersyal biru.",
                "textEn": "Knock-knock-knock! Gentle taps rattled the round wooden door. When Squeak swung it open, there stood their woodland friends shivering in the dusk: two little bunnies, a shy badger, two tiny finches, and a young badger with a blue scarf.",
                "quote": "🚪 'Pintu yang selalu terbuka untuk sahabat adalah tanda hati yang dermawan.'",
                "coReading": "💡 Aktivitas Seru: Ketuk mejamu pelan-pelan: 'Tok-tok-tok! Siapa di luar?'",
                "imagePrompt": "Whimsical storybook scene of Squeak the squirrel opening the Dutch wooden bakery door to welcome friendly woodland animal neighbors into the warm bakery light. Snow/autumn leaves outside, cozy interior, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Tantangan Delapan Sahabat",
                "titleEn": "The Eight Friends Challenge",
                "textId": "Bramble menghitung tamu-tamunya: ditambah dirinya dan Squeak, tepat ada delapan sahabat yang berkumpul di meja bundar! Tetapi, mereka hanya memiliki satu loyang pai apel. \"Bagaimana cara membaginya agar semua puas?\" tanya Squeak bingung.",
                "textEn": "Bramble counted his guests: counting himself and Squeak, there were exactly eight dear friends gathered around the round table! Yet they had only one single apple tart. \"How can we divide it so everyone gets their fair share?\" asked Squeak in a puzzle.",
                "quote": "🤔 'Berbagi dengan adil membutuhkan kecermatan dan hati yang tulus.'",
                "coReading": "💡 Hitung Bersama: Coba hitung jarimu sampai 8 bersama si kecil: 1, 2, 3, 4, 5, 6, 7, 8!",
                "imagePrompt": "A charming children's illustration showing eight diverse little woodland animal friends gathered around a rustic wooden table, all looking thoughtfully at a single round pie in the center. Crayon and pastel on textured paper, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Potongan Pertama: Membelah Dua",
                "titleEn": "The First Cut: Halving the Pie",
                "textId": "Bramble mengambil pisau kayu kue miliknya. Dengan gerakan mantap, ia memotong pai itu tepat di garis tengah: SREK! Pai apel bundar kini terbelah menjadi dua bagian setengah lingkaran yang sama besar.",
                "textEn": "Bramble took up his wooden pastry blade. With a steady paw, he sliced the tart right down the middle: SLICE! The round pie was now divided into two equal semicircles, releasing fragrant puffs of cinnamon steam.",
                "quote": "✂️ 'Membagi dua sama rata adalah langkah awal dari keadilan berbagi.'",
                "coReading": "💡 Tanya si Kecil: Jika satu buah apel dipotong tepat di tengah, menjadi berapa bagian?",
                "imagePrompt": "Close-up storybook illustration of hedgehog Bramble's wooden blade slicing the round apple pie directly across the center line into two halves. Steam curls upward in soft pastel spirals. Warm kitchen setting, wax crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Potongan Silang: Menjadi Empat",
                "titleEn": "The Cross Cut: Four Equal Quarters",
                "textId": "Squeak menunjuk dengan ekor lebatnya. \"Sekarang potong menyilang, Bramble!\" SREK! Bramble memotong garis kedua tegak lurus. Ajaib! Dua belahan kini berubah menjadi empat potong segitiga kue yang montok.",
                "textEn": "Squeak pointed with his bushy tail. \"Now cut across like a cross, Bramble!\" SLICE! Bramble made a second cut straight across. Magic! The two halves transformed into four plump triangular quarters.",
                "quote": "➕ 'Satu lingkaran utuh bisa dibagi menjadi empat sudut yang sama cantiknya.'",
                "coReading": "💡 Tanya si Kecil: Sekarang ada berapa potong? Coba hitung: Satu, dua, tiga, empat!",
                "imagePrompt": "Storybook illustration of the pie neatly cut into four equal quarters shaped like triangles. Squeak claps his paws while Bramble smiles behind his floury whiskers. Warm golden lighting, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Dua Garis Miring: Delapan Potong!",
                "titleEn": "Two Diagonal Slices: Eight Perfect Pieces!",
                "textId": "\"Tinggal dua potongan miring lagi!\" seru Bramble gembira. Srek! Srek! Setiap potongan empat dibagi dua lagi. Cling! Di atas piring porselen, kini ada tepat DELAPAN potong pai apel keemasan yang sama besar!",
                "textEn": "\"Just two diagonal cuts left!\" cheered Bramble happily. Slice! Slice! Each of the four quarters was divided cleanly in half. Clink! Resting upon the porcelain platter were now exactly EIGHT equal golden slices of warm apple tart!",
                "quote": "✨ 'Keadilan dan ketelitian membuat semua orang merasa dihargai tanpa iri hati.'",
                "coReading": "💡 Aktivitas Seru: Tunjuk gambar delapan potong pai dan hitung bersama si kecil dari 1 sampai 8!",
                "imagePrompt": "Delightful illustration showing the apple tart sliced into eight perfect, steaming triangular pieces, like a flower of crust and fruit on a blue ceramic platter. All eight animals look on with shining eyes, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Membagikan Piring ke Setiap Sahabat",
                "titleEn": "Serving Every Single Friend",
                "textId": "Squeak dengan lincah membagikan piring-piring daun maple kecil ke setiap kawan. Satu potong untuk Kelinci Putih, satu potong untuk Kelinci Cokelat, satu untuk Musang, satu untuk Luwak... dan setiap sahabat mendapatkan potongan yang sama lezatnya.",
                "textEn": "Squeak nimbly handed out little maple-leaf saucers to each friend. One slice for White Bunny, one for Brown Bunny, one for Weasel, one for Badger... and every single companion received an identically delicious, warm portion.",
                "quote": "🍁 'Memberi dengan sukacita membuat makanan yang sederhana terasa seperti pesta kerajaan.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana perasaanmu saat kamu berbagi kue atau mainan dengan temanmu?",
                "imagePrompt": "Heartwarming children's book scene of squirrel Squeak handing a maple-leaf plate with a slice of apple pie to a smiling little bunny wrapped in a scarf. Warm bakery ambiance, crayon scribbles, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Kunyahan Manis Penuh Senyuman",
                "titleEn": "Sweet Bites and Happy Cheeks",
                "textId": "Nyam-nyam-kriuk! Ruangan toko roti dipenuhi bunyi kunyahan gembira. Rasa apel madu panggang yang lembut dan kayu manis yang harum menghangatkan perut dan pipi mereka yang semula kedinginan.",
                "textEn": "Munch-munch-crunch! The bakery filled with merry sounds of contentment. Soft baked honey apples and fragrant cinnamon spice warmed their tummies and chilled rosy cheeks from the inside out.",
                "quote": "😋 'Rasa hangat yang paling awet di dunia adalah kebersamaan di sekeliling meja makan.'",
                "coReading": "💡 Aktivitas Seru: Usap perutmu pelan-pelan sambil berkata: 'Nyam-nyam, enaaak sekali!'",
                "imagePrompt": "Joyful illustration of all eight woodland creatures sitting around the wooden table happily eating their slices of pie, sipping hot berry tea. Flour dust floats in the warm lamplight, wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Piring Bersih dan Hati yang Hangat",
                "titleEn": "Clean Plates and Warm Hearts",
                "textId": "Semua piring kini kosong bersih. Kawan-kawan hutan saling berpelukan dan mengucapkan terima kasih kepada Bramble dan Squeak sebelum melangkah pulang ke sarang masing-masing di bawah sinar rembulan.",
                "textEn": "Every leaf saucer was now wiped clean. The forest friends shared warm hugs and whispered heartfelt thanks to Bramble and Squeak before journeying home to their cozy nests under the silvery moonlight.",
                "quote": "🤝 'Kebaikan kecil yang kita bagikan hari ini akan menjadi cerita manis yang mereka bawa pulang.'",
                "coReading": "💡 Tanya si Kecil: Kata ajaib apa yang kita ucapkan saat seseorang memberi kita makanan enak?",
                "imagePrompt": "Tender storybook scene of the woodland animal friends hugging Bramble at the doorway of the bakery under a starry night sky, waving goodbye with happy smiles. Crayon textures on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Tidur Damai di Loteng Pohon Oak",
                "titleEn": "Peaceful Sleep in the Oak Loft",
                "textId": "Lampu minyak toko roti dipadamkan. Di loteng atas beralaskan serbuk kayu harum, Bramble si landak bulat dan Squeak si tupai meringkuk tidur berselimut wol tebal. Aroma apel panggang masih tertinggal lembut mengiringi mimpi mereka. Selamat tidur, sahabat-sahabat dermawan.",
                "textEn": "The bakery's oil lamps were gently blown out. In the cozy loft bed cushioned with sweet wood shavings, plump Bramble the hedgehog and Squeak the squirrel curled up under a thick wool blanket. The soft scent of baked apple lingered into their sweet dreams. Goodnight, kindhearted friends.",
                "quote": "🌙 'Hati yang suka berbagi akan selalu dihadiahi tidur malam yang paling lapang dan tenang.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak dermawan, terima kasih sudah selalu mau berbagi dengan sesama.",
                "imagePrompt": "A serene, comforting bedtime scene in the cozy loft above the bakery. Bramble the hedgehog and Squeak the squirrel are fast asleep curled together under a warm blanket. Crescent moon glows through round window, wax crayon and oil pastel on heavy paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s46)

    # =========================================================================
    # STORY 47: Panci Sup Sayur Gotong Royong
    # =========================================================================
    s47 = {
        "id": "panci-sup-gotong-royong",
        "storyNumber": 47,
        "title": "Panci Sup Sayur Gotong Royong",
        "englishTitle": "The Community Vegetable Pot",
        "category": "berbagi",
        "categoryLabel": "🥧 Dapur & Berbagi",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Gotong royong, kebersamaan, dan keajaiban memberi apa yang kita miliki",
        "cover": "images/story47_cover.jpg",
        "coverImage": "images/story47_cover.jpg",
        "synopsis": "Di alun-alun Desa Hutan, Kakek Beruang menyalakan api di bawah panci besi raksasa yang hanya berisi air mendidih. Satu per satu, hewan-hewan hutan menyumbang sebutir wortel, sebonggol jagung, dan segenggam jamur dari kebun masing-masing, menciptakan sup sayur gotong royong paling lezat di dunia.",
        "synopsisEn": "In the village square, Grandpa Bear kindles a fire beneath a giant iron pot filled with just bubbling water. One by one, woodland creatures bring a single carrot, an ear of corn, or a handful of mushrooms from their gardens, brewing the most delicious community soup in the world.",
        "protagonist": "Kakek Beruang (Beruang tua bertopi koki berjanggut putih dan bercelemek rami)",
        "companion": "Kelinci & Musang (Sahabat-sahabat hutan pembawa keranjang sayuran kebun)",
        "setting": "Alun-alun Desa Hutan di Bawah Naungan Pohon Beringin Tua",
        "pages": [
            {
                "number": 1,
                "title": "Panci Besi Raksasa di Bawah Pohon",
                "titleEn": "The Giant Iron Pot Under the Tree",
                "textId": "Udara musim gugur di Desa Hutan berhembus dingin menusuk tulang. Di tengah alun-alun, Kakek Beruang menyalakan api unggun kecil dari ranting kayu kering di bawah sebuah panci besi raksasa yang diisi air sumber yang bening.",
                "textEn": "The autumn air in the Forest Village blew crisp and chilling. Right in the middle of the village square, Grandpa Bear kindled a crackling fire of dry oak twigs beneath a giant black iron kettle filled with fresh spring water.",
                "quote": "🍲 'Satu panci besar bisa mengumpulkan seratus hati dalam kehangatan yang sama.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat panci sup yang sangat besar saat acara kumpul keluarga?",
                "imagePrompt": "Charming children's book illustration of kind elderly Grandpa Bear in a tall chef's hat and white beard, stirring a huge black iron pot over a crackling stone fire in a cobblestone village square. Autumn leaves falling, handcrafted wax crayon and soft oil pastel on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 2,
                "title": "Air Mendidih yang Masih Kosong",
                "titleEn": "Bubbling Water Still Empty",
                "textId": "Kluk-kluk-kluk... Air di dalam panci mulai mendidih mengeluarkan uap putih yang bergulung-gulung. Tetapi di dalam panci itu belum ada apa-apa selain air tawar bening. \"Siapa yang punya sedikit bahan untuk sup ajaib kita?\" seru Kakek Beruang dengan suara ramah.",
                "textEn": "Glug-bubble-glug... The water in the great pot began to simmer, sending up swirling clouds of fragrant white steam. But inside, there was nothing yet save clear pure water. \"Who has a little garden treasure for our wonder soup?\" called Grandpa Bear merrily.",
                "quote": "💧 'Awal yang kosong memberi ruang bagi setiap orang untuk menyumbangkan kebaikannya.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara air mendidih bersama si kecil: 'Kluk-kluk-kluk-kluk!'",
                "imagePrompt": "Whimsical storybook scene of steam billowing softly from the giant cauldron in the square, with Grandpa Bear smiling warmly, inviting woodland neighbors who peek curious from their doorsteps, 4:3 landscape, text-free."
            },
            {
                "number": 3,
                "title": "Tiga Wortel Jingga dari Kelinci",
                "titleEn": "Three Orange Carrots from the Bunny",
                "textId": "Lompat, lompat! Kelinci Putih berlari kecil membawa keranjang anyamannya. \"Kakek, aku hanya punya tiga wortel manis dari kebunku!\" Kakek Beruang tersenyum lebar. Cemplung! Tiga wortel jingga terpotong bundar masuk ke dalam panci.",
                "textEn": "Hop, hop! White Bunny came scampering with her woven basket. \"Grandpa, I only have three sweet carrots from my garden patch!\" Grandpa Bear beamed warmly. Plop! Three freshly sliced bright orange carrots tumbled into the bubbling kettle.",
                "quote": "🥕 'Sumbangan sekecil apa pun sangat berharga jika diberikan dengan hati yang tulus.'",
                "coReading": "💡 Tanya si Kecil: Warna apa sayuran wortel yang disumbangkan oleh Kelinci Putih?",
                "imagePrompt": "A delightful illustration of a cute white bunny with a floral scarf handing three bright orange carrots to Grandpa Bear by the steaming pot. Warm crayon strokes, naive folk art, 4:3 landscape, text-free."
            },
            {
                "number": 4,
                "title": "Sebonggol Jagung Manis dari Musang",
                "titleEn": "Sweet Corn from the Little Badger",
                "textId": "Melihat Kelinci menyumbang, Musang Kecil memberanikan diri mendekat membawa dua tongkol jagung manis berbiji emas. Pipil, pipil, butiran jagung kuning keemasan berhamburan masuk ke dalam kuah sup.",
                "textEn": "Seeing Bunny's generous gift, Little Badger stepped forward bravely carrying two ears of golden sweetcorn. Plink, plink, sweet sun-yellow corn kernels cascaded cheerfully into the warming broth.",
                "quote": "🌽 'Kebaikan satu orang selalu menularkan keberanian berbagi kepada yang lain.'",
                "coReading": "💡 Tanya si Kecil: Makanan apa saja yang bisa dibuat dari bulir jagung manis?",
                "imagePrompt": "Charming picture book illustration of a badger in a knitted vest dropping golden corn kernels into the giant iron pot, watching the ripples with delight. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 5,
                "title": "Jamur Payung dari Keluarga Tupai",
                "titleEn": "Umbrella Mushrooms from the Squirrels",
                "textId": "Dari atas dahan beringin, keluarga Tupai meluncur turun membawa segenggam jamur payung hutan yang wangi tanah segar. Cemplung! Kuah sup kini mulai berubah warna menjadi kaldu keemasan yang kental dan harum.",
                "textEn": "Down from the oak branches skittered the Squirrel family carrying a bundle of wild umbrella mushrooms fragrant with forest dew. Splash! The broth began turning into a rich, golden stock smelling of pure autumn comfort.",
                "quote": "🍄 'Setiap aroma yang berbeda bersatu padu menciptakan rasa yang semakin kaya.'",
                "coReading": "💡 Aktivitas Seru: Hirup udara dalam-dalam melalui hidung: 'Hhhmm, harum sekali baunya!'",
                "imagePrompt": "Storybook scene of fluffy squirrels handing delicate wild mushrooms to Grandpa Bear. The broth in the pot turns golden and aromatic, with bubbles sparkling under warm afternoon light, 4:3 landscape, text-free."
            },
            {
                "number": 6,
                "title": "Bawang Bombay dan Seledri Segar",
                "titleEn": "Onions and Fresh Crisp Celery",
                "textId": "Ibu Berang-berang membawakan dua butir bawang bombay manis, dan Burung Hantu membawakan seikat seledri hijau harum. Tak ada yang datang dengan tangan kosong; semua membawa apa yang mereka miliki dari rumah.",
                "textEn": "Mother Beaver brought two sweet round onions, and wise Grandmother Owl fluttered down with a fragrant bunch of crisp garden celery. No one arrived empty-handed; everyone contributed whatever modest treasure their home held.",
                "quote": "🧅 'Saat kita saling melengkapi kekurangan, kebersamaan menjadi sempurna.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu membantu orang tua menyiapkan sayuran di dapur?",
                "imagePrompt": "Heartwarming illustration of diverse forest animals gathering around the village pot, placing celery leaves, potatoes, and onions into the stew. Community spirit, rich crayon textures, 4:3 landscape, text-free."
            },
            {
                "number": 7,
                "title": "Sendok Kayu Pengaduk Ajaib",
                "titleEn": "The Magic Wooden Ladle",
                "textId": "Kakek Beruang mengambil sendok kayu raksasa miliknya lalu mengaduk sup itu perlahan: swiiish, swiiish... Wortel jingga, jagung kuning, jamur cokelat, dan seledri hijau menari berputar dalam pusaran kebersamaan yang indah.",
                "textEn": "Grandpa Bear took his giant carved wooden ladle and stirred the great soup in wide, steady circles: swiiish, swiiish... Orange carrots, yellow corn, brown mushrooms, and emerald celery danced together in a beautiful swirl of harmony.",
                "quote": "🥄 'Gotong royong mengubah hal-hal kecil yang terpisah menjadi satu kebaikan yang agung.'",
                "coReading": "💡 Aktivitas Seru: Gerakkan tanganmu memutar seperti sedang mengaduk panci sup raksasa!",
                "imagePrompt": "Vibrant children's book scene of Grandpa Bear stirring the swirling colorful vegetable soup with a large wooden ladle. Golden steam curls playfully, illuminating the happy faces of the surrounding animals, 4:3 landscape, text-free."
            },
            {
                "number": 8,
                "title": "Mangkuk Keramik untuk Semua",
                "titleEn": "Ceramic Bowls for Everyone",
                "textId": "\"Sup sudah matang!\" seru Kakek Beruang. Seluruh warga desa mengambil mangkuk tanah liat masing-masing dan berbaris rapi dengan sabar. Kakek menuangkan kuah sup kental hangat ke setiap mangkuk sampai semuanya terisi penuh.",
                "textEn": "\"The soup is ready!\" declared Grandpa Bear with a booming joyful laugh. The entire village retrieved their clay bowls and formed an orderly, polite line. Grandpa ladled steaming, rich vegetable soup into each bowl until all were brim-full.",
                "quote": "🥣 'Makanan yang dimasak bersama-sama selalu memiliki rasa kehangatan persaudaraan.'",
                "coReading": "💡 Tanya si Kecil: Mengapa antre dengan tertib membuat semua orang merasa senang dan nyaman?",
                "imagePrompt": "Joyous illustration of forest animals lined up holding ceramic bowls, smiling as Grandpa Bear ladles rich soup for each of them. Autumn leaves glowing golden in the sunset, wax crayon on cream paper, 4:3 landscape, text-free."
            },
            {
                "number": 9,
                "title": "Pesta Sup di Bawah Lampu Lentera",
                "titleEn": "The Lantern Soup Feast",
                "textId": "Lentera-lentera kertas dinyalakan di dahan beringin tua. Di atas meja panjang alun-alun, seluruh warga desa duduk berdampingan, menikmati sup sayur paling lezat yang pernah mereka kecap. Dinginnya malam terkalahkan oleh hangatnya rasa syukur.",
                "textEn": "Paper lanterns were strung across the old banyan branches, glowing soft gold. Along long wooden tables in the square, all the villagers sat side-by-side, savoring the most delicious vegetable soup they had ever tasted. The cold night was banished by the warmth of grateful hearts.",
                "quote": "🏮 'Tidak ada yang merasa kekurangan saat semua orang mau berbagi dengan rela.'",
                "coReading": "💡 Tanya si Kecil: Apa yang paling kamu sukai saat makan bersama keluarga besar atau teman-temanmu?",
                "imagePrompt": "Heartwarming children's book feast scene of woodland animal friends dining together at long wooden tables in the village square beneath hanging paper lanterns. Soft twilight sky, warm amber glows, wax crayon and oil pastel, 4:3 landscape, text-free."
            },
            {
                "number": 10,
                "title": "Mimpi Damai di Desa Hutan",
                "titleEn": "Peaceful Slumber in the Forest Village",
                "textId": "Panci besi raksasa kini bersih berkilau, apinya telah padam menyisakan bara hangat. Di rumah-rumah kayu yang tenteram, seluruh warga desa tertidur dengan perut kenyang dan hati yang damai. Gotong royong telah menghangatkan seluruh desa. Selamat tidur, desa hutan yang rukun.",
                "textEn": "The giant iron pot stood clean and resting, its hearth coals glowing low with cozy embers. Inside tranquil cottages throughout the village, every creature drifted off to sleep with full bellies and peaceful hearts. Working together had warmed the whole valley. Goodnight, harmonious forest village.",
                "quote": "🌙 'Tidur yang paling damai adalah tidur di tengah lingkungan yang saling mengasihi dan menjaga.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak baik, semoga hatimu selalu dipenuhi rasa ingin berbagi dan membantu sesama.",
                "imagePrompt": "A serene bedtime illustration of the quiet village square under starry skies and crescent moon. Chimneys puff gentle smoke from cozy cottages where animal families sleep peacefully. Handcrafted wax crayon on textured cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s47)

    return stories

print("Story module 44-47 defined successfully")
