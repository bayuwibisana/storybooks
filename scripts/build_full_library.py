# scripts/build_full_library.py
import json
import os

MASTER_STYLE = (
    "A charming, whimsical children's book illustration of {action}, set in {setting}. "
    "Featuring {protagonist_desc} and {companion_desc}. "
    "Rendered in a distinct handcrafted wax crayon and soft oil pastel style. "
    "Visible waxy crayon scribbles, chalky textured pastel smudges, and rough, uneven outlines. "
    "Warm, vibrant color palette featuring {palette}. "
    "Subtle rough-grain watercolor paper texture showing through the strokes. "
    "Naive folk-art perspective, innocent storybook charm, soft diffused lighting, cozy and tactile hand-drawn feel, zero digital gradients, high paper grain detail. "
    "Matte finish, scumbled pastel texture, crayola wax marks, deckle edge paper. "
    "Negative prompt: photorealistic, 3D render, glossy, digital airbrush, smooth plastic skin, sharp CGI lighting, hyper-realistic, dark and gritty, geometric precision. Aspect ratio: 4:3."
)

IMAGE_TO_IMAGE_STYLE = (
    "Gemini Image-to-Image Reference: [Use Page 1 anchor image as reference]. "
    "Maintain the identical visual design, clothing, and handcrafted wax crayon & oil pastel style of {protagonist_name} and {companion_name}. "
    "Scene: {action}, set in {setting}. "
    "Palette mood: {palette}. "
    "Visible waxy crayon scribbles, chalky pastel smudges, and rough outlines on rough-grain watercolor paper texture. "
    "Zero digital gradients, high tactile paper grain detail. Aspect ratio: 4:3."
)

CATEGORIES = [
    {
        "id": "emosi",
        "label": "💛 Empati & Emosi",
        "age": "Usia 3–5 Tahun",
        "description": "Mengenal rasa marah, sedih, cemas, dan belajar menenangkan diri",
        "items": [
            ("Kembang Api di Dada Kiko", "Kiko's Chest Firework", "Belajar menarik napas saat marah agar tidak meletup", "Kiko", "Kucing oren gemuk berompi kancing kayu", "Mimi", "Kelinci kecil penyabar bertelinga belang", "Taman Bunga Lavender"),
            ("Awan Kelabu di Saku Boni", "Boni's Grey Pocket Cloud", "Menerima kesedihan dan menangis sampai lega", "Boni", "Beruang madu kecil bercelana kodok garis lebah", "Pip", "Tikus padang mungil bertopi bunga mentega", "Padang Rumput Dandelion"),
            ("Bayangan Monster di Balik Pintu", "The Shadow Behind the Door", "Mengatasi rasa takut gelap dan mencari tahu kebenarannya", "Arka", "Anak laki-laki 4 tahun berpiyama garis biru", "Riko", "Anjing pudel cokelat berbulu keriting", "Kamar Tidur Berbintang"),
            ("Piala Emas untuk Bersama", "The Golden Trophy for Both", "Mengatasi rasa cemburu saat teman menang permainan", "Tobi", "Kelinci pelari cepat berikat kepala merah", "Kimi", "Kura-kura mungil bercangkang hijau", "Lintasan Lari Kebun Stroberi"),
            ("Menunggu Roti Matang", "Waiting for the Warm Bread", "Melatih kesabaran saat harus menunggu giliran", "Momo", "Monyet kecil bertopi jerami", "Cici", "Burung pipit kuning bersayap lincah", "Dapur Roti Nenek Beruang"),
            ("Langkah Pertama Menyapa Teman", "First Step to Say Hello", "Mengatasi rasa malu saat bertemu orang baru", "Sora", "Gadis kecil pemalu berjaket wol merah", "Piko", "Burung hantu mini bermata bundar", "Taman Bermain Kota Kecil"),
            ("Dua Kata Ajaib: Maafkan Aku", "Two Magic Words: I Am Sorry", "Keberanian meminta maaf saat tidak sengaja merusak mainan", "Dino", "Anak dinosaurus hijau pemalu bersyal kuning", "Tika", "Tupai lincah berbando pita", "Lembah Pasir Mainan"),
            ("Piknik Hujan yang Tetap Riang", "The Rainy Day Picnic", "Mengatasi rasa kecewa saat rencana tidak berjalan lancar", "Lulu", "Anak berang-berang bercelemek polkadot", "Beno", "Katak hijau bertopi daun talas", "Tepi Danau Teratai"),
            ("Kursi Kosong di Bawah Pohon", "The Empty Chair by the Tree", "Peka dan peduli pada teman yang menyendiri", "Nara", "Gadis cilik berkuncir dua bergaun katun", "Milo", "Anak anjing setia bersyal rajut", "Halaman Sekolah Alam"),
            ("Tepukan Bangga untuk Sahabat", "Proud Clap for a Friend", "Rasa bangga yang rendah hati dan saling mendukung", "Bintang", "Anak rusa bertanduk mini beludru", "Koko", "Ayam kalkun kecil yang ceria", "Padang Rumput Ilalang")
        ]
    },
    {
        "id": "tidur",
        "label": "🦉 Pengantar Tidur",
        "age": "Usia 2–4 Tahun",
        "description": "Dongeng menenangkan, langit malam berbintang, dan rasa aman sebelum terlelap",
        "items": [
            ("Lagu Bintang untuk Si Kecil", "Starlight Song for Little One", "Menghitung bintang yang berkedip lembut di jendela", "Maya", "Gadis cilik 3 tahun berpiyama kuning mentega", "Oliver", "Burung hantu salju berkacamata bulat", "Jendela Loteng Desa"),
            ("Kasur Awan Marshmallow", "The Marshmallow Cloud Bed", "Membayangkan kasur empuk yang melayang di langit damai", "Tilly", "Kelinci putih bergaun celemek daisy", "Bumble", "Lebah madu bulat bertopi bowler", "Langit Awan Kapuk"),
            ("Hembusan Napas Angin Malam", "Night Breeze Deep Breath", "Ritual relaksasi menghembuskan napas pelan sebelum tidur", "Gani", "Gajah kecil bertelinga lebar bersyal rajut", "Kuki", "Kupu-kupu malam bersayap beludru", "Hutan Bambu Tenang"),
            ("Lentera Emas Sang Penjaga", "The Golden Lantern Keeper", "Merasa aman karena ada lampu hangat yang menjaga", "Leo", "Anak laki-laki berjas hujan kuning", "Marina", "Anak anjing laut bersyal toska", "Mercusuar Teluk Pebblewick"),
            ("Lullaby Jangkrik di Bawah Daun", "Cricket Lullaby Under the Leaf", "Melodi alam malam yang mengantar kelopak mata terpejam", "Kimi", "Landak mini berbulu lembut cokelat", "Suri", "Jangkrik kecil bertopi daun", "Bawah Ranting Pohon Hazel"),
            ("Bantal Penyimpan Mimpi Indah", "The Pillow of Sweet Dreams", "Menyimpan harapan indah di balik sarung bantal", "Alif", "Anak laki-laki bertopi tidur bintang", "Pompom", "Boneka panda gendut berbulu lembut", "Kamar Tidur Loteng"),
            ("Bulan Sabit Berselimut Wol", "The Crescent Moon's Wool Quilt", "Kisah bulan yang diselimuti rajutan benang hangat", "Maya", "Gadis perajut cilik bersyal panjang", "Oliver", "Burung hantu tua penyayang", "Atap Rumah Cerobong Asap"),
            ("Perahu Kertas Menuju Negeri Lelap", "The Paper Boat to Sleepy Land", "Perjalanan mengarungi danau mimpi yang tenang", "Samudra", "Anak pelaut cilik bertopi nakhoda mini", "Lumba", "Lumba-lumba kecil bercahaya", "Danau Air Tenang Biru"),
            ("Tutup Buku, Buka Mimpimu", "Close the Book, Open Your Dream", "Menutup dongeng terakhir dengan hati penuh syukur", "Ina", "Gadis cilik berambut ikal berselimut perca", "Kucing Manis", "Kucing tidur melingkar di ujung ranjang", "Kamar Tidur Hangat"),
            ("Hewan Hutan Mengucap Selamat Tidur", "Forest Friends Say Goodnight", "Melihat hewan-hewan hutan satu per satu terlelap", "Rusa Kecil", "Anak rusa bertutul putih", "Rubah Manis", "Anak rubah meringkuk di liang tanah", "Hutan Pinus Berbintang")
        ]
    },
    {
        "id": "logika",
        "label": "🧩 Logika & Sains",
        "age": "Usia 4–7 Tahun",
        "description": "Sebab-akibat, timbangan, pola bentuk, bayangan, dan observasi alam",
        "items": [
            ("Rahasia Jungkat-Jungkit Kayu", "The Seesaw Secret Balance", "Memahami konsep keseimbangan berat dan jarak tumpuan", "Bimo", "Beruang besar gemuk yang ceria", "Tupi", "Tupai mungil berekor lebat", "Taman Bermain Rumput"),
            ("Batu Tenggelam, Perahu Terapung", "Stone Sinks, Boat Floats", "Menemukan mengapa batu berat tenggelam tapi perahu kayu mengapung", "Arka", "Anak laki-laki ingin tahu berkacamata", "Kiko", "Kucing petualang berompi saku", "Tepi Sungai Kerikil"),
            ("Bayangan Tubuh yang Berubah Ukuran", "The Changing Shadow Dance", "Mengamati bayangan memanjang di pagi hari dan memendek siang hari", "Nara", "Gadis cilik bertopi caping matahari", "Chirp", "Burung gereja yang lincah", "Halaman Pasir Cerah"),
            ("Kalung Buah Pola Tiga Warna", "The Three-Color Berry Necklace", "Belajar urutan pola berulang merah-kuning-biru", "Cita", "Kancil cerdik berkantung daun", "Tomi", "Kura-kura penghitung sabar", "Kebun Buah Hutan"),
            ("Sulap Warna Kunyit & Bunga Telang", "Turmeric and Blue Pea Magic", "Percobaan mencampur warna kuning dan biru menjadi hijau", "Putri", "Gadis kecil bercelemek pelukis", "Riri", "Kelinci berbulu putih bersih", "Dapur Percobaan Alami"),
            ("Tetesan Embun yang Menghilang", "The Disappearing Dewdrop", "Mengamati proses penguapan air saat disapa panas mentari", "Zaki", "Anak laki-laki berjaket hijau daun", "Kumbang", "Kumbang tutul merah kepik", "Daun Talas Berembun"),
            ("Batu Hitam Penarik Pasir Besi", "The Magnetic Black Stone", "Menemukan keajaiban daya tarik magnet di alam", "Bani", "Anak pandai besi cilik bertopi kulit", "Guguk", "Anjing pelacak berhidung basah", "Muara Sungai Pasir Hitam"),
            ("Roda Bundar yang Menggelinding", "The Rolling Round Wheel", "Mengapa bentuk bulat lebih mudah ditarik daripada kotak", "Dodo", "Anak badak cilik bercula mini", "Pio", "Kancil perancang gerobak", "Jalanan Tanah Bukit"),
            ("Gema Suara di Mulut Gua", "The Friendly Cave Echo", "Memahami bahwa gema adalah pantulan suara kita sendiri", "Faris", "Anak pemberani bertongkat kayu", "Mimi", "Kelelawar buah kecil yang ramah", "Mulut Gua Batu Kapur"),
            ("Jam Ranting Matahari", "The Sundial Stick Clock", "Mengetahui waktu pulang makan siang dari bayangan ranting", "Sari", "Gadis gembala bertopi jerami", "Kambing Putih", "Anak kambing berbulu ikal", "Padang Rumput Hijau")
        ]
    },
    {
        "id": "petualangan",
        "label": "⛵ Petualangan",
        "age": "Usia 4–7 Tahun",
        "description": "Menjelajahi lingkungan baru, mencoba hal baru, dan mengatasi rasa ragu",
        "items": [
            ("Hari Pertama di Sekolah Alam", "First Day at Forest School", "Menemukan bahwa tempat baru penuh dengan keseruan", "Alfi", "Anak laki-laki bertas ransel rubah", "Kiki", "Burung kutilang berkicau riang", "Gerbang Sekolah Kayu"),
            ("Pemeriksaan Gigi Si Buaya Manis", "The Sweet Crocodile Dentist", "Mengetahui dokter gigi itu ramah dan giginya jadi bersih berkilau", "Coki", "Anak buaya kecil berpiyama hijau", "Dokter Beruang", "Dokter beruang berjas putih bersih", "Klinik Pohon Rindang"),
            ("Pohon Brokoli Mini Ajaib", "The Magic Broccoli Tree", "Memberanikan diri mencicipi sayuran hijau pertama kali", "Rian", "Anak laki-laki bertopi koki kecil", "Mama Rian", "Ibu penyayang bercelemek bunga", "Meja Makan Keluarga"),
            ("Jembatan Bambu Goyang", "The Wobbly Bamboo Bridge", "Belajar percaya diri dan melangkah hati-hati bersama teman", "Tegar", "Anak desa berkulit sawo matang", "Bono", "Monyet lincah penunjuk jalan", "Jurang Sungai Berbatu"),
            ("Jejak Kaki Rahasia di Pasir", "Secret Footprints in the Sand", "Petualangan menebak jejak hewan laut di pantai", "Lani", "Gadis pesisir berkepang dua", "Koko", "Kepiting kecil bercangkang oranye", "Garis Pantai Pasir Putih"),
            ("Membuka Mata di Air Kolam", "Opening Eyes in Clear Water", "Mengatasi rasa takut air saat belajar berenang", "Bayu", "Anak laki-laki berpelampung bebek", "Ikan Mas", "Ikan mas bersirip gemulai", "Kolam Air Sumber Alami"),
            ("Tenda Kain di Bawah Bintang", "The Blanket Tent Adventure", "Keseruan pertama kali berkemah di halaman belakang rumah", "Dimas", "Anak laki-laki bersenter kuningan", "Ayah Dimas", "Ayah penyabar bertopi rimba", "Halaman Rumput Belakang"),
            ("Mencapai Puncak Bukit Pelangi", "Climbing the Rainbow Hill", "Kepuasan melangkah sampai puncak bukit dengan kaki sendiri", "Sinta", "Gadis cilik bertongkat kayu ukir", "Kancil", "Kancil sahabat penunjuk jalan", "Lereng Bukit Berbunga"),
            ("Kompas Daun di Aliran Air", "The Floating Leaf Compass", "Menemukan arah pulang dengan mengamati arus sungai", "Nico", "Anak pramuka cilik bertopi baret", "Kancil Mini", "Kancil pandai penunjuk arah", "Hutan Belantara Rindang"),
            ("Gerobak Kayu Beroda Tiga", "The Three-Wheeled Cart Ride", "Perjalanan mengangkut labu kuning melintasi desa", "Gilang", "Anak petani cilik bersandal karet", "Sapi Kecil", "Anak sapi putih bertutul hitam", "Jalan Kebun Sayur Desa")
        ]
    },
    {
        "id": "berbagi",
        "label": "🥧 Dapur & Berbagi",
        "age": "Usia 3–6 Tahun",
        "description": "Kerjasama memasak, kedermawanan, memotong rata, dan nikmatnya makan bersama",
        "items": [
            ("Pai Apel Delapan Potong", "The Eight-Slice Apple Tart", "Memotong pai sama besar agar semua kawan kebagian", "Bramble", "Landak bulat bersarung tangan rajut merah", "Squeak", "Tupai lincah bertopi kulit kenari", "Toko Roti Pohon Oak"),
            ("Panci Sup Sayur Gotong Royong", "The Community Vegetable Pot", "Setiap orang menyumbang satu sayuran menjadi sup terlezat", "Kakek Beruang", "Beruang tua bertopi koki berjanggut putih", "Kelinci & Musang", "Sahabat-sahabat hutan pembawa sayur", "Alun-alun Desa Hutan"),
            ("Pesta Selai Stroberi Hutan", "The Wild Strawberry Jam Feast", "Memetik buah bersama dan mengaduk selai di kendi tanah", "Tita", "Gadis cilik berkeranjang rotan", "Mimi", "Kelinci penyuka buah manis", "Kebun Stroberi Lereng Bukit"),
            ("Biskuit Bintang untuk Tetangga", "Star Cookies for the Neighbors", "Membagikan toples kue buatan sendiri kepada tetangga", "Hana", "Gadis kecil bercelemek merah muda", "Ibu Hana", "Ibu ramah pembawa nampan", "Jalanan Kompleks Desa"),
            ("Roti Gandum Hangat Musim Salju", "Warm Wheat Loaf in Winter", "Mengantarkan roti hangat untuk nenek kelinci yang kesepian", "Milo", "Rubah kecil bermantel tebal", "Piko", "Burung pipit penunjuk jalan", "Pondok Kayu Beratap Salju"),
            ("Madu Secukupnya untuk Beruang", "Just Enough Honey for Bear", "Belajar mengambil secukupnya dan menyisakan untuk lebah", "Baru", "Anak beruang madu bercelana biru", "Ratu Lebah", "Lebah emas bersayap gemerlap", "Dahan Pohon Madu"),
            ("Piknik Buah di Bawah Beringin", "Fruit Picnic Under Banyan Tree", "Menata tikar dan saling bertukar bekal buah potong", "Dita", "Gadis ceria bertopi anyaman", "Kawan-kawan", "Kelompok anak bermain bersama", "Taman Pohon Beringin"),
            ("Jus Jeruk Peras Gotong Royong", "The Teamwork Orange Juice", "Bahu-membahu memeras jeruk manis untuk teman yang lelah", "Raka", "Anak laki-laki berotot kecil bersemangat", "Doni", "Sahabat pembawa teko kaca", "Gazebo Tepi Lapangan"),
            ("Pancake Madu Minggu Pagi", "Sunday Morning Honey Pancakes", "Sabar menunggu giliran mendapatkan pancake hangat pertama", "Adit", "Anak laki-laki bertopi tidur", "Adik Alya", "Adik kecil berpita rambut", "Meja Makan Keluarga"),
            ("Bekal Kasih Sayang untuk Adik", "The Lunchbox Made with Love", "Menghias nasi bekal adik dengan bentuk wajah tersenyum", "Kakak Nadia", "Kakak perempuan penyayang", "Adik Rio", "Adik kecil bermata bulat", "Dapur Pagi Hari")
        ]
    },
    {
        "id": "persahabatan",
        "label": "🤝 Persahabatan",
        "age": "Usia 3–6 Tahun",
        "description": "Menerima teman yang berbeda, saling mendengarkan, dan merangkul keunikan",
        "items": [
            ("Langkah Kura-kura & Sayap Walet", "Turtle Steps and Swallow Wings", "Dua sahabat berbeda kecepatan yang saling melengkapi", "Tomi", "Kura-kura sabar bertempurung lumut", "Wali", "Burung walet cepat bersayap sabit", "Pesisir Tebing Laut"),
            ("Gajah Kecil Bertelinga Payung", "The Little Elephant's Umbrella Ears", "Kekurangan diri ternyata bisa menjadi berkah penolong sesama", "Elphi", "Gajah biru kecil bertelinga lebar", "Kancil & Kancil", "Hewan-hewan kecil berteduh hujan", "Padang Rumput Sabana"),
            ("Bahasa Isyarat Ekor Tupai", "The Squirrel's Tail Sign Language", "Belajar mengerti teman yang berkomunikasi dengan cara berbeda", "Sasa", "Tupai bisu berekor lebat berisyarat", "Beni", "Kelinci pendengar yang baik", "Dahan Pohon Kenari"),
            ("Lagu Baru dari Seberang Laut", "New Song from Across the Ocean", "Menyambut teman pendatang dan belajar kebudayaannya", "Ayu", "Gadis penari bertopi bunga melati", "Ken", "Anak pendatang bermata sipit ramah", "Sanggar Tari Tepi Pantai"),
            ("Balap Karung di Jalur Landai", "Sack Race on the Gentle Ramp", "Membuat modifikasi permainan agar teman difabel bisa ikut gembira", "Fandi", "Anak laki-laki berkursi roda ceria", "Kawan Bermain", "Anak-anak kompleks perumahan", "Taman Bermain Ramah Anak"),
            ("Mendengarkan Sampai Kalimat Terakhir", "Listening Until the Very Last Word", "Menghargai teman dengan tidak memotong bicaranya", "Rangga", "Anak laki-laki berkemeja kotak-kotak", "Dian", "Gadis kecil bercerita antusias", "Bale-Bale Bambu"),
            ("Kacamata Baru Kucing Ciko", "Ciko Cat's New Glasses", "Mendukung sahabat yang baru memakai kacamata agar percaya diri", "Ciko", "Kucing abu-abu berkacamata bundar merah", "Mimi", "Kucing putih penyemangat setia", "Sekolah Hewan Ceria"),
            ("Petak Umpet yang Menyenangkan Semua", "Hide and Seek for Everyone", "Aturan main yang ramah agar anak pemalu tidak merasa tertinggal", "Gita", "Gadis cilik bertopi rajut", "Kawan-kawan", "Kelompok anak bermain petak umpet", "Halaman Berpagar Kayu"),
            ("Pelukan Landak dan Kucing Bulu", "The Hug of Hedgehog and Fluffy Cat", "Menemukan cara saling menyayangi tanpa menyakiti", "Bram", "Landak berduri halus", "Kuki", "Kucing anggora berbulu lebat", "Teras Rumah Desa"),
            ("Lukisan Kado Buatan Tangan", "The Handmade Birthday Picture", "Hadiah gambar tulus dari hati lebih bermakna dari mainan mahal", "Rara", "Gadis cilik berjemari cat warna", "Sahabat Rara", "Teman ulang tahun bermahkotakan kertas", "Pesta Ulang Tahun Sederhana")
        ]
    },
    {
        "id": "alam",
        "label": "🌿 Cinta Alam",
        "age": "Usia 3–6 Tahun",
        "description": "Merawat tanaman, membersihkan aliran air, menghormati habitat satwa, dan bumi",
        "items": [
            ("Tunas Pertama Bunga Matahari", "First Sprout of the Sunflower", "Menyiram setiap pagi dan takjub melihat kehidupan tumbuh", "Lala", "Gadis cilik bertopi kebun membawa gembor", "Cacing Tanah", "Cacing tanah penyubur tanah gembur", "Bedengan Kebun Belakang"),
            ("Aliran Sungai Jernih Bebas Ranting", "Clear Stream Free of Debris", "Membersihkan sampah daun agar ikan bisa berenang leluasa", "Budi", "Anak laki-laki bersepatu bot karet", "Ikan Nila", "Ikan-ikan sungai berenang lincah", "Sungai Kerikil Jernih"),
            ("Kotak Sarang di Pohon Mangga", "Nest Box on the Mango Tree", "Membuat rumah perlindungan burung pipit saat musim hujan", "Pak Tani & Cucu", "Kakek bertukang kayu dan cucunya", "Sepasang Burung", "Burung gereja bersarang nyaman", "Dahan Pohon Mangga Lebat"),
            ("Hotel Bambu untuk Sahabat Serangga", "Bamboo Hotel for Bug Friends", "Menyusun bilah bambu berongga untuk lebah penyerbuk", "Dara", "Gadis cilik bercelana katun saku", "Lebah Soliter", "Lebah kecil pencari nektar bunga", "Sudut Kebun Bunga Liar"),
            ("Emas Hitam Daun Gugur", "Black Gold of Fallen Leaves", "Mengolah daun kering menjadi kompos subur penyegar tanaman", "Hadi", "Anak laki-laki bergaru taman mini", "Cacing Kompos", "Cacing pekerja penggembur tanah", "Kotak Kompos Belakang Rumah"),
            ("Keran Air yang Tidak Menetes", "The Faucet That Never Drips", "Belajar menghargai setiap tetes air bersih untuk bumi", "Maya", "Gadis cilik bergaun biru muda", "Tetes Air Ajaib", "Karakter tetesan air tersenyum", "Kamar Mandi Bersih"),
            ("Ulat Rakus Jadi Sayap Pelangi", "Hungry Caterpillar to Rainbow Wings", "Menghargai proses metamorfosis ulat menjadi kupu-kupu indah", "Rian", "Anak laki-laki berkaca pembesar", "Kupu-kupu Emas", "Kupu-kupu baru keluar dari kepompong", "Pohon Jeruk Berdaun Lebat"),
            ("Langkah Pelan di Rumah Rusa", "Quiet Steps in Deer Home", "Belajar berbisik di hutan agar satwa liar merasa damai", "Sena", "Anak penjelajah berompong hijau lumut", "Induk Rusa & Bayi", "Rusa tutul menyusui anaknya", "Hutan Lindung Pinus"),
            ("Pohon Cemara Penahan Angin Pantai", "Coastal Pine Windbreaker", "Menanam bibit cemara laut untuk melindungi desa pesisir", "Nelayan Cilik", "Anak pesisir berkulit sawo matang", "Bibit Cemara", "Bibit pohon cemara kecil bergoyang", "Bibit Pasir Pantai"),
            ("Vas Dandelion dari Botol Kaca", "Dandelion Vase from Glass Bottle", "Memanfaatkan kembali wadah bekas menjadi pajangan indah", "Tia", "Gadis kreatif berpita rambut", "Keluarga Tia", "Meja makan berhias bunga liar", "Meja Ruang Tamu")
        ]
    },
    {
        "id": "kreativitas",
        "label": "🎨 Kreativitas",
        "age": "Usia 4–7 Tahun",
        "description": "Membuat mainan dari kardus, orkestra dari alam, dan melihat dari sudut pandang baru",
        "items": [
            ("Pesawat Kardus Penjelajah Galaksi", "Cardboard Spaceship to the Galaxy", "Mengubah kotak kardus bekas menjadi pesawat terbang", "Rafa", "Anak laki-laki berhelm mangkuk astronot", "Kucing Astronot", "Kucing oren mengenakan syal bintang", "Ruang Tengah Rumah"),
            ("Gendang Tempurung Kelapa", "Coconut Shell Rhythm Drum", "Menciptakan irama musik gembira dari bahan alam sekitar", "Wayang Cilik", "Anak laki-laki berpakaian adat sederhana", "Kawan Perkusi", "Anak-anak bernyanyi sambil memukul batok", "Bawah Pohon Kelapa"),
            ("Lukisan Cap Daun Warna Pelangi", "Leaf Stamp Painting in Rainbow", "Mencelupkan daun bertekstur ke cat alami untuk membuat lukisan", "Lilis", "Gadis bercelemek penuh bercak warna", "Kelinci Putih", "Kelinci menemani di samping kertas gambar", "Meja Gambar Kayu"),
            ("Topeng Rubah dari Kantong Belanja", "Fox Mask from Grocery Bag", "Membuat topeng sandiwara dari kertas belanja cokelat", "Fahri", "Anak laki-laki bergunting ujung tumpul", "Adik Fahri", "Adik kecil memakai topeng tupai", "Lantai Karpet Kamar"),
            ("Cangkir Tanah Liat Mini", "Tiny Clay Cups for Tea", "Membentuk perabot mini dari tanah liat tepi sungai", "Nanda", "Gadis cilik bertangan belepotan lumpur", "Nenek Nanda", "Nenek tersenyum mengajari memutar tanah", "Bengkel Tembikar Desa"),
            ("Benteng Pasir Berparit Kerang", "Sand Castle with Shell Moat", "Membangun istana pasir megah dengan parit penahan ombak", "Aldo", "Anak pesisir bertopi ember mini", "Kepiting Cilik", "Kepiting mengintip dari parit pasir", "Tepi Pantai Pasir Halus"),
            ("Selendang Sutra Penari Angin", "The Silk Scarf Wind Dancer", "Mengekspresikan gerak tubuh meniru tarian dedaunan musim gugur", "Kirana", "Gadis cilik berselendang kuning melambai", "Kupu-kupu", "Kupu-kupu terbang beriringan", "Puncak Bukit Angin"),
            ("Burung Terbang Bayangan Jari", "Finger Shadow Flying Bird", "Membuat teater bayangan hewan di dinding dengan cahaya lentera", "Danis", "Anak laki-laki melengkungkan kedua jempolnya", "Mama Danis", "Ibu memegang lampu senter kecil", "Dinding Kamar Tidur"),
            ("Ksatria Bunga Bermantel Selimut", "Flower Knight with Blanket Cloak", "Bermain peran menjadi pahlawan pelindung tanaman kebun", "Zidan", "Anak kecil bertopi helm kardus", "Ayam Jago", "Ayam jago berkokok gagah", "Pekarangan Kebun Bunga"),
            ("Kartu Kolase Kelopak Mawar", "Rose Petal Collage Greeting Card", "Merangkai kelopak bunga gugur menjadi kartu ucapan kasih sayang", "Melati", "Gadis cilik berpita ungu membawa lem kayu", "Ibu Melati", "Ibu terharu menerima kartu kolase", "Teras Depan Berbunga")
        ]
    },
    {
        "id": "ketekunan",
        "label": "🐢 Ketekunan",
        "age": "Usia 4–7 Tahun",
        "description": "Belajar langkah demi langkah, tidak putus asa saat gagal, dan menghargai latihan",
        "items": [
            ("Kayuhan Sepeda Roda Dua Pertama", "First Pedal on Two Wheels", "Jatuh di rumput empuk, bangkit lagi, hingga meluncur seimbang", "Bima", "Anak laki-laki berhelm pelindung oranye", "Ayah Bima", "Ayah memegang sadel sepeda dengan sabar", "Jalanan Taman Berumput"),
            ("Simpul Telinga Kelinci Tali Sepatu", "Bunny Ears Shoelace Knot", "Latihan berulang kali mengikat tali sepatu sampai rapi", "Tari", "Gadis cilik bersepatu kanvas merah", "Kucing Tari", "Kucing memperhatikan ujung tali sepatu", "Undakan Teras Rumah"),
            ("Pondasi Menara Balok yang Kokoh", "The Strong Block Tower Base", "Tersenyum saat menara roboh dan menyusun kembali lebih kuat", "Farel", "Anak laki-laki berkemeja bergaris", "Kakak Farel", "Kakak memberi balok segitiga penopang", "Ruang Bermain Bersih"),
            ("Tiupan Nada Pertama Seruling Bambu", "First Note on the Bamboo Flute", "Dari desis angin hampa menjadi nada merdu berkat ketekunan", "Ranu", "Anak gembala berseruling bambu", "Kerbau Jinak", "Kerbau mendengarkan sambil mengunyah rumput", "Padang Rumput Berangin"),
            ("Potongan Terakhir Puzzle Hutan", "The Last Piece of the Forest Puzzle", "Menyelesaikan teka-teki 50 keping dengan mencari tepi dahulu", "Salma", "Gadis cilik bertelunjuk teliti", "Kakek Salma", "Kakek tersenyum menyesap teh hangat", "Meja Bundar Ruang Tamu"),
            ("Gerakan Kaki Gaya Katak", "Frog Kick Swimming Practice", "Latihan mengayuh kaki sampai tubuh mengapung maju di kolam", "Reza", "Anak laki-laki berkacamata renang biru", "Pelatih Katak", "Pelatih ramah memegang papan apung", "Kolam Renang Dangkal"),
            ("Jahitan Lurus di Kain Wol", "Straight Stitches on Wool Felt", "Menenun benang miring yang perlahan menjadi lurus berkat telaten", "Alya", "Gadis kecil berjarum plastik tumpul", "Nenek Alya", "Nenek sabar membimbing tangan cucunya", "Kursi Goyang Sudut Ruang"),
            ("Hafal Dendang Lagu Daerah", "Mastering the Folk Melody", "Mengulang lirik tiga bait setiap sore sampai lancar bernyanyi", "Taufiq", "Anak laki-laki berpeci rajut hitam", "Ibu Taufiq", "Ibu bertepuk tangan berirama gembira", "Teras Senja Hari"),
            ("Kotak Balok yang Rapi Kembali", "The Tidy Toy Box Mission", "Memasukkan mainan satu per satu sampai lantai bersih tuntas", "Pandu", "Anak laki-laki bercelemek kerja mini", "Mama Pandu", "Mama mengusap kepala anak dengan bangga", "Kamar Bermain Anak"),
            ("Menunggu Adonan Ragi Mengembang", "Waiting for the Yeast to Rise", "Sabar menunggu adonan roti naik dua kali lipat sebelum oven", "Bintang", "Anak koki kecil bertopi putih", "Bunda Bintang", "Bunda mengukur jam dapur analog", "Dapur Roti Rumah")
        ]
    },
    {
        "id": "keluarga",
        "label": "🏡 Keluarga",
        "age": "Usia 2–5 Tahun",
        "description": "Kasih kakek-nenek, rukun adik-kakak, kebersamaan meja makan, dan rasa syukur",
        "items": [
            ("Janggut Putih & Kisah Kakek", "White Beard and Grandpa's Tales", "Mendengarkan kisah masa lalu sambil dipangku kakek tercinta", "Ciko", "Anak laki-laki bertopi pet abu-abu", "Kakek Ciko", "Kakek tua berkursi goyang kayu jati", "Ruang Keluarga Berperapian"),
            ("Donat Tabur Gula Nenek", "Grandma's Sugar Powdered Donuts", "Menaburkan gula halus di atas donat kentang hangat buatan nenek", "Ratih", "Gadis kecil berjemari putih gula", "Nenek Ratih", "Nenek bersanggul menyajikan nampan kayu", "Dapur Nenek yang Asri"),
            ("Langkah Pertama Adik Merangkak", "Baby Sister's First Crawl", "Kakak menyingkirkan bantal agar jalur merangkak adik aman", "Kakak Gilang", "Kakak laki-laki bertubuh lincah", "Adik Baby", "Bayi mungil berpipi gembul tersenyum", "Karpet Lembut Ruang Tengah"),
            ("Gambar Mobil Merah untuk Ayah", "The Red Car Drawing for Papa", "Kejutan kartu ucapan untuk ayah yang baru pulang bekerja", "Tomi", "Anak laki-laki membawa kertas krayon", "Ayah Tomi", "Ayah tersenyum berlutut memeluk anaknya", "Pintu Masuk Rumah"),
            ("Segelas Air & Pelukan untuk Ibu", "A Glass of Water and Hug for Mama", "Menyuguhkan air putih dan pelukan erat saat ibu tampak letih", "Dina", "Gadis cilik bertelapak tangan mungil", "Ibu Dina", "Ibu tersenyum haru memeluk putrinya", "Sofa Ruang Istirahat"),
            ("Makan Malam Tanpa Layar Kaca", "Dinner Table Story Time", "Bercerita tentang hal paling lucu yang terjadi seharian di meja makan", "Keluarga Budi", "Ayah, Ibu, Kakak, dan Adik duduk melingkar", "Meja Penuh Makanan", "Nasi hangat dan sup sayur beruap", "Ruang Makan Hangat"),
            ("Kerja Bakti Hari Minggu", "Sunday Cleaning Harmony", "Kakak menyapu, adik mengelap meja, sambil berdendang gembira", "Kakak Rio & Adik Ani", "Sepasang saudara membawa kemoceng dan sapu", "Kucing Rumah", "Kucing memperhatikan dari atas lemari", "Ruang Tamu Terbuka"),
            ("Album Foto Bayi Sebesar Semangka", "Baby Album as Small as Watermelon", "Tertawa bersama melihat foto diri saat masih bayi merah", "Keluarga Ceria", "Ayah dan Ibu membuka album bersampul beludru", "Anak Balita", "Balita menunjuk foto dirinya sendiri", "Karpet Tebal Lantai"),
            ("Menjemur Kasur di Bawah Mentari", "Beating the Mattress in Sunshine", "Membantu menepuk kasur kapuk dengan sapu lidi di halaman", "Adit", "Anak laki-laki memegang penebah lidi", "Ayah Adit", "Ayah mengangkat kasur ke jemuran bambu", "Halaman Terik Siang"),
            ("Doa Bersama Menyapa Bintang", "Bedtime Family Prayer Under Stars", "Menyebutkan nama seluruh keluarga dalam doa malam yang hangat", "Keluarga Bahagia", "Seluruh keluarga bergandengan tangan berdoa", "Jendela Malam", "Langit malam berhias bulan dan bintang", "Kamar Tidur Utama")
        ]
    }
]

def generate_pages_for_story(story_id, title_id, title_en, theme, protag_name, protag_desc, comp_name, comp_desc, setting, palette):
    pages = []
    
    # 10 progressive narrative beats
    beats = [
        ("Awal Mula yang Tenang", "A Gentle Beginning", 
         f"Pagi hari di {setting} selalu terasa istimewa bagi {protag_name}. Bersama {comp_name}, mereka memulai hari dengan senyuman dan hati yang penuh rasa ingin tahu.",
         f"Morning at {setting} always felt special for {protag_name}. Together with {comp_name}, they began the day with warm smiles and curious hearts.",
         f"'{theme[0]} dimulai dari langkah pertama yang tulus.'",
         f"{protag_name} and {comp_name} enjoying the morning in {setting}",
         True),
        ("Kejutan Tak Terduga", "An Unexpected Occurrence",
         f"Tiba-tiba, sesuatu terjadi di depan mereka! {protag_name} tertegun mengamati, sementara {comp_name} mendekat dengan mata berbinar penasaran.",
         f"Suddenly, something unexpected caught their eye! {protag_name} paused to look closely, while {comp_name} stepped forward with wide curious eyes.",
         f"'Kejadian baru adalah pintu menuju petualangan baru.'",
         f"{protag_name} observing an interesting surprise with {comp_name}",
         False),
        ("Rencana dan Rasa Ingin Tahu", "Curious Plan",
         f"Keduanya berdiskusi dengan penuh semangat. {comp_name} memberikan ide cerdas yang membuat {protag_name} mengangguk setuju.",
         f"The two discussed enthusiastically. {comp_name} offered a clever idea that made {protag_name} nod with delight.",
         f"'Dua kepala selalu berpikir lebih terang daripada satu.'",
         f"{protag_name} and {comp_name} discussing their plan together",
         False),
        ("Tantangan Kecil di Jalan", "A Small Challenge",
         f"Namun perjalanan tidak selalu mulus. Ada rintangan kecil yang menghadang, menguji kesabaran dan kerjasama mereka berdua.",
         f"Yet the journey wasn't without hurdles. A small challenge arose, gently testing their patience and teamwork.",
         f"'Rintangan kecil membuat kita belajar untuk lebih teliti.'",
         f"{protag_name} navigating a gentle obstacle with help from {comp_name}",
         False),
        ("Momen Mengambil Napas", "A Calming Breath",
         f"{protag_name} sempat merasa ragu, tetapi {comp_name} mengingatkan untuk menarik napas dalam-dalam. Keheningan membawa ketenangan.",
         f"{protag_name} felt a moment of doubt, but {comp_name} reminded them to take a deep, gentle breath. Calmness brought clarity.",
         f"'Saat bingung, berhentilah sejenak dan dengarkan detak hatimu.'",
         f"{protag_name} taking a calming deep breath beside {comp_name}",
         False),
        ("Gagasan Cemerlang Bersama", "A Brilliant Idea",
         f"Dengan pikiran yang kembali jernih, sebuah solusi kreatif muncul! Mereka mencoba cara baru yang belum pernah dilakukan sebelumnya.",
         f"With a clear mind, a creative solution blossomed! They tried a fresh approach they had never thought of before.",
         f"'Kreativitas adalah jembatan menuju jalan keluar.'",
         f"{protag_name} and {comp_name} trying their creative solution",
         False),
        ("Puncak Keberhasilan & Keajaiban", "The Joyful Breakthrough",
         f"Berhasil! Usaha dan ketekunan mereka membuahkan hasil yang membanggakan. Wajah {protag_name} berseri-seri penuh sukacita.",
         f"It worked! Their persistence and teamwork bore sweet fruit. {protag_name}'s face glowed with pure joy.",
         f"'Kerja keras bersama sahabat selalu berbuah manis.'",
         f"{protag_name} celebrating the joyful breakthrough with {comp_name}",
         False),
        ("Berbagi Senyuman dengan Sekitar", "Sharing the Joy",
         f"Mereka tidak menikmati keberhasilan ini sendirian. Kawan-kawan sekitar turut merasakan kehangatan dan kebaikan yang tercipta.",
         f"They did not keep the success to themselves. Friends and neighbors gathered around, feeling the warmth of kindness.",
         f"'Kebahagiaan bertambah berkali-kali lipat saat dibagikan.'",
         f"{protag_name} and {comp_name} sharing their joy with friends",
         False),
        ("Senja Emas Menyapa Rumah", "Golden Sunset Glow",
         f"Matahari sore perlahan turun, mewarnai langit dengan selendang aprikot dan merah muda. Waktunya pulang ke pelukan rumah yang damai.",
         f"The evening sun dipped low, painting the sky in ribbons of apricot and blush rose. It was time to return home.",
         f"'Hari yang penuh makna diakhiri dengan rasa syukur.'",
         f"{protag_name} and {comp_name} walking home under the sunset sky",
         False),
        ("Malam Berbintang & Mimpi Indah", "Starlit Bedtime Goodnight",
         f"Lampu kamar meredup, bintang-bintang di luar jendela berkelip ramah. {protag_name} memejamkan mata dalam selimut hangat, siap bermimpi indah.",
         f"Room lights softened, and friendly stars twinkled outside the window. {protag_name} closed their eyes under the warm quilt, ready for sweet dreams.",
         f"'Selamat malam dunia, besok ada petualangan baru yang menunggu.'",
         f"{protag_name} sleeping peacefully in a cozy warm bed under starry window",
         False)
    ]
    
    for idx, beat in enumerate(beats, 1):
        is_anchor = beat[6]
        if is_anchor:
            img_p = MASTER_STYLE.format(
                action=f"{protag_name} ({protag_desc}) and {comp_name} ({comp_desc}) starting their day in {setting}",
                setting=setting,
                protagonist_desc=protag_desc,
                companion_desc=comp_desc,
                palette=palette
            )
        else:
            img_p = IMAGE_TO_IMAGE_STYLE.format(
                protagonist_name=protag_name,
                companion_name=comp_name,
                action=beat[5],
                setting=setting,
                palette=palette
            )
            
        pages.append({
            "number": idx,
            "title": beat[0],
            "titleEn": beat[1],
            "textId": beat[2],
            "textEn": beat[3],
            "quote": beat[4],
            "coReading": f"💡 Tanya si Kecil: Menurutmu apa yang dirasakan {protag_name} di halaman ini? Bagaimana jika kamu yang ada di sana?",
            "imagePrompt": img_p
        })
        
    return pages

# Generate all 100 stories across 10 categories
all_stories = []
story_counter = 1

for cat in CATEGORIES:
    cat_id = cat["id"]
    cat_label = cat["label"]
    cat_age = cat["age"]
    
    for item in cat["items"]:
        title_id, title_en, moral_summary, protag_name, protag_desc, comp_name, comp_desc, setting = item
        story_slug = f"story-{story_counter:03d}-{cat_id}"
        palette = "warm honey gold, soft pastel earth tones, cream paper texture"
        
        pages = generate_pages_for_story(
            story_id=story_slug,
            title_id=title_id,
            title_en=title_en,
            theme=(title_id, moral_summary),
            protag_name=protag_name,
            protag_desc=protag_desc,
            comp_name=comp_name,
            comp_desc=comp_desc,
            setting=setting,
            palette=palette
        )
        
        all_stories.append({
            "id": story_slug,
            "storyNumber": story_counter,
            "title": title_id,
            "englishTitle": title_en,
            "category": cat_id,
            "categoryLabel": cat_label,
            "ageGroup": cat_age,
            "moralTheme": moral_summary,
            "cover": f"images/cover_{cat_id}.jpg",
            "synopsis": f"{protag_name} dan {comp_name} belajar tentang {moral_summary.lower()} melalui petualangan hangat di {setting}.",
            "protagonist": f"{protag_name} ({protag_desc})",
            "companion": f"{comp_name} ({comp_desc})",
            "setting": setting,
            "pages": pages
        })
        story_counter += 1

print(f"Generated {len(all_stories)} rich children's stories across {len(CATEGORIES)} distinct categories!")

# Save to destination
output_path = "/Users/bayu/local/storybooks/data/stories_100.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_stories, f, ensure_ascii=False, indent=2)

print(f"Successfully saved complete database to {output_path}")
