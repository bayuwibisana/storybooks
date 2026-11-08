# scripts/polish_stories_98_to_101.py
import json

def get_stories_98_to_101():
    stories = [
        # --- STORY 98: Langkah Pertama Adik Merangkak ---
        {
            "id": "story98",
            "storyNumber": 98,
            "title": "Langkah Pertama Adik Merangkak",
            "englishTitle": "Baby Sister's First Crawling Steps",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kasih sayang kakak pada adik, menyemangati tumbuh kembang, & kehangatan keluarga",
            "cover": "covers/story98_cover.jpg",
            "synopsis": "Adik bayi yang baru berusia delapan bulan sedang belajar merangkak di atas karpet busa lembut ruang keluarga. Kakak Gilang menaruh mainan kerincingan beruang di hadapannya dan merangkak di sampingnya untuk menyemangati adik hingga berhasil mencapai pelukan hangat Ibu.",
            "protagonist": "Kakak Gilang (Kakak laki-laki bertubuh lincah)",
            "companion": "Adik Baby (Bayi mungil berpipi gembul tersenyum)",
            "setting": "Karpet Lembut Ruang Tengah",
            "pages": [
                {
                    "number": 1,
                    "title": "Karpet Busa Bergambar Awan",
                    "titleEn": "Cloud-Patterned Foam Mat",
                    "textId": "Di tengah ruang keluarga terhampar karpet busa lembut bermotif awan putih dan bintang pastel. Adik bayi, yang mengenakan baju terusan kuning cerah dengan pipi gembul semerah apel, sedang bertumpu pada perutnya sambil mengayun-ayunkan kaki mungilnya di udara.",
                    "textEn": "In the center of the living room lay a soft foam mat patterned with white clouds and pastel stars. Baby sister, wearing a sunny yellow onesie with cheeks plump and rosy as apples, rested on her tummy swinging her chubby feet in the air.",
                    "quote": "Setiap awal kehidupan dipenuhi oleh gerakan-gerakan kecil yang menakjubkan.",
                    "coReading": "Apakah kamu masih ingat saat adikmu masih bayi mungil?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Gilang, an affectionate young boy in shorts and t-shirt, lying on his stomach on a cloud-patterned playmat looking lovingly at his chubby baby sister. Sunlight streaming into living room, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Kerincingan Beruang Kayu",
                    "titleEn": "Wooden Bear Rattle",
                    "textId": "Gilang memegang mainan kerincingan kayu berbentuk beruang madu. Ketika Gilang menggoyangkannya pelan, terdengar bunyi 'Kling-klong, kling-klong!' yang merdu. Mata bulat adik bayi berbinar dan tangannya terulur ke depan ingin meraih mainan itu.",
                    "textEn": "Gilang held a wooden honey-bear rattle. When he shook it gently, a sweet 'Jingle-chime, clack-clack!' chimed through the room. Baby's round eyes sparkled and her little hands reached forward wanting to grab the toy.",
                    "quote": "Benda sederhana menjadi pemantik rasa ingin tahu yang besar bagi anak-anak.",
                    "coReading": "Bagaimana bunyi mainan kerincingan beruang kayu Gilang?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Gilang shaking a cute wooden bear rattle with a gentle smile. Baby sister on her tummy with arms outstretched, mouth open in delighted baby babble, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Dorongan Lutut yang Masih Goyah",
                    "titleEn": "Wobbly Knee Pushes",
                    "textId": "Adik mencoba mengangkat perutnya dari karpet. Kedua lutut kecilnya menekan busa empuk, dan kedua tangannya menopang lantai: 'Hup!' Tubuh mungilnya terangkat, namun ia bergoyang ke kiri dan ke kanan seperti kura-kura kecil yang belum terbiasa dengan cangkangnya.",
                    "textEn": "Baby tried lifting her tummy off the mat. Both chubby knees pushed into the foam, and little palms planted on the floor: 'Oof!' Her little body rose up, wobbling left and right like a tiny turtle getting used to its shell.",
                    "quote": "Usaha pertama selalu memerlukan perjuangan yang mengagumkan.",
                    "coReading": "Bisakah kamu berlutut dan bertumpu pada kedua tangan seperti adik bayi?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Baby sister up on hands and knees rocking back and forth wobbling cutely on the soft rug. Gilang kneeling beside her with hands ready to catch her, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Teladan Merangkak Sang Kakak",
                    "titleEn": "Big Brother's Crawling Example",
                    "textId": "Melihat adik ragu, Gilang ikut bertumpu pada kedua tangan dan lututnya di samping adik. 'Lihat Kakak, adik sayang! Majukan tangan kiri, lalu dorong lutut kanan: tep, tep, tep!' Gilang merangkak pelan di sampingnya sambil tertawa geli.",
                    "textEn": "Seeing baby hesitate, Gilang dropped to his hands and knees right beside her. 'Look at big brother, sweet sister! Move left hand, then push right knee: pat, pat, push!' Gilang crawled slowly beside her with a playful laugh.",
                    "quote": "Contoh yang sabar adalah guru terbaik bagi yang sedang bertumbuh.",
                    "coReading": "Bagaimana cara Gilang mengajari adik merangkak?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Gilang crawling happily on all fours alongside his baby sister on the colorful rug, showing her how to move forward. Mother watching from the sofa with proud smile, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Langkah Maju Pertama",
                    "titleEn": "The Very First Forward Step",
                    "textId": "Adik bayi menatap Gilang lalu menatap mainan beruang di hadapannya. Dengan dorongan jempol kakinya yang gemuk, adik memajukan tangan kanannya: 'Plok!' Lalu disusul lutut kirinya: 'Pluk!' Tubuhnya meluncur maju satu jengkal!",
                    "textEn": "Baby looked at Gilang, then at the wooden bear rattle ahead. With a push from her chubby toes, baby reached her right hand forward: 'Plap!' Followed by her left knee: 'Plop!' Her body surged forward by a whole handspan!",
                    "quote": "Satu langkah kecil adalah lompatan raksasa dalam perjalanan kehidupan.",
                    "coReading": "Apakah adik bayi berhasil meluncur maju?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Baby sister successfully taking her first crawling crawl step forward, beaming with toothless baby grin. Gilang cheering softly with two thumbs up, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Tepukan Tangan dan Tawa Ibu",
                    "titleEn": "Mother's Claps and Laughter",
                    "textId": "Dari sofa ruang tamu, Ibu bertepuk tangan tanpa suara agar tidak mengagetkan adik. 'Pintar sekali anak Ibu! Ayo sedikit lagi, sayang!' bisik Ibu menyemangati dengan mata yang berbinar haru.",
                    "textEn": "From the sofa, Mother clapped softly so as not to startle baby. 'So clever, my sweet girl! Just a little further, darling!' Mother whispered encouragingly with misty, joyful eyes.",
                    "quote": "Sorak dukungan dari orang tua adalah bahan bakar bagi keberanian anak.",
                    "coReading": "Bagaimana reaksi Ibu saat melihat adik mulai merangkak?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Mother sitting on the living room rug with open arms, smiling radiantly and clapping softly. Baby crawling steadily across the floor toward her, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Merangkak Menembus Karpet",
                    "titleEn": "Crawling Across the Playmat",
                    "textId": "Kini adik tidak ragu lagi. Kedua tangan dan lututnya bergerak selaras: tep, tap, tep, tap! Cepat sekali seperti anak kucing yang mengejar bola benang. Gilang merangkak mundur di depannya, membunyikan kerincingan beruang sebagai pemandu jalan.",
                    "textEn": "Now baby hesitated no longer. Her hands and knees moved in harmony: pat, crawl, pat, crawl! Swift as a kitten chasing a yarn ball. Gilang crawled backward before her, gently ringing the wooden bear rattle as a guide.",
                    "quote": "Bila rasa percaya diri sudah tumbuh, setiap rintangan terasa ringan dilalui.",
                    "coReading": "Bisakah kamu merangkak cepat seperti adik mengejar mainan?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Baby sister crawling with determined joyful face, moving rapidly across the rug toward Mother's outstretched hands. Gilang crawling backward smiling proudly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Mendarat di Pelukan Hangat Ibu",
                    "titleEn": "Landing in Mother's Warm Arms",
                    "textId": "'Hup!' Telapak tangan mungil adik akhirnya menyentuh ujung gaun Ibu. Ibu langsung mengangkat adik tinggi-tinggi ke udara, mencium pipi gembulnya yang basah oleh liur bahagia. Adik tertawa terbahak-bahak dalam pelukan hangat Ibu.",
                    "textEn": "'Up!' Baby's little palms finally reached the hem of Mother's dress. Mother lifted her high into the air, kissing chubby cheeks wet with happy baby giggles. Baby squealed with delight in Mother's warm embrace.",
                    "quote": "Pelukan ibu adalah garis akhir paling manis dari setiap perjuangan anak.",
                    "coReading": "Siapa yang menyambut adik di ujung karpet?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Mother lifting baby sister high in a loving embrace, baby laughing with arms wide. Gilang sitting beside Mother hugging her knees, glowing family warmth, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Ciuman Bangga Sang Kakak",
                    "titleEn": "Big Brother's Proud Kiss",
                    "textId": "Gilang memegang tangan mungil adik dan mencium jemarinya. 'Adik hebat sekali hari ini! Besok kita belajar merangkak sampai ke taman belakang ya!' Adik mengoceh riang seolah menjawab janji sang kakak dengan penuh semangat.",
                    "textEn": "Gilang took baby's tiny hand, kissing her little knuckles. 'You were wonderful today, little sister! Tomorrow we will crawl all the way to the garden!' Baby babbed cheerfully as if promising to join big brother's adventures.",
                    "quote": "Ikatan persaudaraan yang dirawat sejak dini mekar menjadi persahabatan abadi.",
                    "coReading": "Apa janji Gilang kepada adik untuk esok hari?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Gilang gently kissing his baby sister's chubby cheek as Mother cradles her. Warm golden afternoon light in the living room, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Pulas di Boks Berenda",
                    "titleEn": "Sound Sleep in the Lace Crib",
                    "textId": "Malam tiba dan sehabis mandi air hangat serta meminum susu, adik bayi tertidur pulas di ranjang boks kayu berendanya, memeluk boneka beruang kayu. Di kamar sebelah, Gilang tidur lelap dengan senyum bangga di wajahnya, bermimpi menjelajahi dunia bersama adik tercintanya.",
                    "textEn": "Night arrived and after a warm bath and sweet milk, baby sister slept deeply in her wooden crib draped in lace, hugging the wooden bear rattle. In the next room, Gilang slept soundly with a proud smile, dreaming of exploring the wide world alongside his sweet sister.",
                    "quote": "Tidurlah dalam lindungan cinta, rumah kita selalu dipenuhi kehangatan dan rasa syukur.",
                    "coReading": "Selamat tidur anak-anak baik, biarkan mimpi indah menjaga lelapmu malam ini.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Baby sleeping peacefully in a cozy wooden crib with a pastel quilt. Gilang sleeping peacefully in his adjoining bed visible through the open doorway. Starry night and crescent moon outside, serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 99: Gambar Mobil Merah untuk Ayah ---
        {
            "id": "story99",
            "storyNumber": 99,
            "title": "Gambar Mobil Merah untuk Ayah",
            "englishTitle": "Red Car Drawing for Father",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Ungkapan cinta anak pada ayah, karya krayon tulus, & kehangatan menyambut kepulangan",
            "cover": "covers/story99_cover.jpg",
            "synopsis": "Tomi tahu Ayah sering lelah setelah pulang bekerja lembur di kota. Dengan selembar kertas putih dan krayon merah menyala, Tomi menggambar mobil merah keluarga lengkap dengan jendela bundar dan matahari tersenyum. Ketika Ayah pulang di malam hari, gambar sederhana itu menghapus seluruh lelah di wajah Ayah.",
            "protagonist": "Tomi (Anak laki-laki membawa kertas krayon)",
            "companion": "Ayah Tomi (Ayah tersenyum berlutut memeluk anaknya)",
            "setting": "Pintu Masuk Rumah",
            "pages": [
                {
                    "number": 1,
                    "title": "Lilin Krayon Merah Menyala",
                    "titleEn": "Vibrant Red Wax Crayon",
                    "textId": "Di atas meja belajarnya yang diterangi lampu belajar kuning hangat, Tomi membuka kotak krayon lilinnya. Dari deretan warna yang berjajar, jari Tomi memilih krayon merah cabai yang ujungnya sudah agak tumpul karena sering dipakai. Merah adalah warna favorit Ayah.",
                    "textEn": "At his little desk lit by a warm yellow study lamp, Tomi opened his box of wax crayons. From the neat colorful row, his fingers picked the chili-red crayon, its tip rounded from frequent use. Red was Father's favorite color.",
                    "quote": "Mengingat kesukaan orang tua adalah tanda cinta yang peka dari anak.",
                    "coReading": "Warna apa yang paling disukai oleh ayahmu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Tomi, a thoughtful young boy in pajamas, sitting at a wooden desk choosing a bright red wax crayon from an open wooden crayon box. Warm lamp glow, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Goresan Badan Mobil Persegi Panjang",
                    "titleEn": "Outlining the Rectangular Car Body",
                    "textId": "Dengan tekun, Tomi menarik garis lurus tebal di atas kertas gambar putihnya. Ia membuat badan mobil berbentuk balok panjang dengan moncong depan yang ramah. Tomi mewarnai seluruh badan mobil itu dengan sapuan krayon merah yang rapat dan mengilap.",
                    "textEn": "With steady hands, Tomi drew thick straight lines on his white paper. He shaped a long car body with a friendly front bumper. Tomi filled the car with dense, waxy strokes of bright red crayon until it gleamed.",
                    "quote": "Karya yang dibuat dengan kesungguhan hati memancarkan ketulusan murni.",
                    "coReading": "Bentuk apa yang digambar Tomi untuk badan mobilnya?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up of Tomi's small hands coloring a charming, naive red car outline on textured paper. Little red crayon shavings on the table, simple bead dot eyes, naive folk art, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Roda Hitam dan Jendela Bundar",
                    "titleEn": "Black Wheels and Round Windows",
                    "textId": "Dengan krayon hitam pekat, Tomi menggambar dua roda bundar besar di bagian bawah mobil. Di bagian kaca jendela, ia menggambar dua kepala kecil yang tersenyum: satu kepala bertopi kerja untuk Ayah, dan satu kepala kecil berambut ikal untuk dirinya sendiri.",
                    "textEn": "With deep black crayon, Tomi added two big round wheels beneath the car. In the window glass, he drew two smiling faces: one wearing a work cap for Father, and one with curly hair for himself.",
                    "quote": "Kebersamaan dalam angan-angan menghangatkan setiap goresan gambar.",
                    "coReading": "Siapa saja yang duduk di dalam mobil merah buatan Tomi?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. The drawing showing a cute red car with big black tires, two smiling bead-eyed figures waving from the windows. Tomi adding yellow stars in the sky, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Matahari Senyum dan Bintang Kejora",
                    "titleEn": "Smiling Sun and Evening Star",
                    "textId": "Di sudut atas kertas, Tomi menambahkan matahari kuning yang tersenyum lebar dengan sinar-sinar jingga hangat. Di samping matahari, ia menggambar sebutir bintang perak kecil yang berkilau: lambang kepulangan Ayah saat senja menjelang malam.",
                    "textEn": "In the paper's top corner, Tomi added a golden sun with a broad happy smile and warm orange rays. Beside it, he drew a twinkling silver evening star: signaling Father's return at dusk.",
                    "quote": "Cahaya kasih sayang menyinari setiap sudut gelap dalam kehidupan.",
                    "coReading": "Gambar apa yang ditambahkan Tomi di langit mobil merahnya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Tomi holding the completed vibrant wax crayon drawing up to the lamp light: a bright red car, smiling sun, and glowing star. His face beaming with happy pride, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Menunggu di Depan Pintu Masuk",
                    "titleEn": "Waiting by the Front Door",
                    "textId": "Tomi melipat kedua tangannya di atas kertas gambar dan duduk di undakan karpet dekat pintu masuk rumah. Jam dinding berdentang tujuh kali. Ibu menyelimuti pundak Tomi dengan syal rajut: 'Ayah sebentar lagi sampai dari halte bus, Tomi.'",
                    "textEn": "Tomi held his drawing with both hands, sitting on the foyer rug near the front door. The wall clock chimed seven times. Mother draped a knit scarf over his shoulders: 'Father will be home from the bus stop any moment, Tomi.'",
                    "quote": "Menunggu kepulangan orang tercinta adalah kehangatan tersendiri bagi hati.",
                    "coReading": "Di mana Tomi duduk menunggu kepulangan Ayah?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Tomi sitting patiently by the front door holding his drawing sheet flat across his knees. Warm hallway lamp glowing, Mother smiling from the kitchen doorway, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Bunyi Derap Sepatu di Halaman",
                    "titleEn": "Sound of Footsteps on the Gravel",
                    "textId": "'Kres, kres, kres!' Bunyi langkah sepatu kerja di atas kerikil halaman terdengar mendekat. Kunci pintu berputar pelan dari luar: 'Klek!' Pintu kayu terbuka, memperlihatkan Ayah yang berdiri dengan tas jinjing kerja dan mantel yang berdebu perjalanan.",
                    "textEn": "'Crunch, crunch, step!' Sound of work shoes on the gravel path drew near. The door key turned gently from outside: 'Click!' The wooden door swung open, revealing Father standing with his briefcase, tired from a long commute.",
                    "quote": "Pintu rumah yang terbuka adalah pelabuhan damai bagi mereka yang berjuang.",
                    "coReading": "Bagaimana suara langkah kaki Ayah saat tiba di halaman?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Father opening the wooden front door, wearing a coat and carrying a work bag. His face looks tired but his eyes widen with warmth seeing Tomi, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Hadiah Sambutan Penuh Kejutan",
                    "titleEn": "A Surprising Welcome Gift",
                    "textId": "Sebelum Ayah sempat meletakkan tasnya, Tomi melompat berdiri dan membentangkan kertas gambarnya dengan kedua tangan terangkat tinggi: 'Ayah! Lihat ini! Ini mobil merah ajaib untuk mengantar Ayah jalan-jalan tanpa lelah!'",
                    "textEn": "Before Father could set his bag down, Tomi sprang to his feet, holding his drawing high with both hands: 'Father! Look! A magic red car to take you on trips so you never feel tired!'",
                    "quote": "Kepolosan cinta seorang anak mampu menembus lelahnya hari yang panjang.",
                    "coReading": "Apa yang diucapkan Tomi saat menyerahkan gambarnya pada Ayah?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Tomi holding up the bright red car drawing in front of Father in the warm doorway. Father's face breaking into a radiant joyful smile, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Lutut yang Bertekuk dan Pelukan Erat",
                    "titleEn": "Kneeling Down in a Tight Hug",
                    "textId": "Ayah menjatuhkan tas kerjanya ke lantai dan berlutut memeluk Tomi erat-erat. Ayah memandang gambar mobil merah itu dengan mata yang berkaca-kaca haru. Seluruh rasa penat dan letih di pundak Ayah seolah sirna tertiup senyuman tulus putranya.",
                    "textEn": "Father dropped his work bag to the floor and knelt down, wrapping Tomi in a tight, heartfelt embrace. Father gazed at the red car drawing with misty eyes. All the weight and exhaustion on his shoulders melted away in his son's sweet smile.",
                    "quote": "Pelukan anak adalah obat paling mujarab bagi segala rasa lelah orang tua.",
                    "coReading": "Bagaimana perasaan Ayah saat memeluk Tomi di depan pintu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Father kneeling on the entryway floor embracing Tomi tightly, holding the red car drawing in one hand. Warm hallway lighting, pure emotional family warmth, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Gambar yang Terpasang di Meja Kerja Ayah",
                    "titleEn": "Drawing Mounted on Father's Desk",
                    "textId": "Sehabis makan malam bersama, Ayah menempelkan gambar mobil merah Tomi di dinding kayu tepat di atas meja kerja rumahnya menggunakan selotip kertas. 'Sekarang setiap kali Ayah bekerja, mobil merah Tomi akan selalu memberi Ayah semangat baru,' puji Ayah bangga.",
                    "textEn": "After dinner together, Father taped Tomi's red car drawing on the wooden wall right above his home desk with paper tape. 'Now whenever I work, Tomi's red car will always give me fresh energy,' Father praised proudly.",
                    "quote": "Karya anak yang dihargai menjadi lentera penerang bagi keluarga.",
                    "coReading": "Di mana Ayah menempelkan gambar mobil merah buatan Tomi?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Father taping the red car drawing onto the wooden wall above his study desk. Tomi standing on a chair beside him watching happily, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Nyenyak di Bawah Naungan Bintang",
                    "titleEn": "Sound Sleep Beneath Starry Skies",
                    "textId": "Malam semakin larut dan keheningan menyelimuti seluruh rumah yang hangat. Ayah menyelimuti Tomi di ranjangnya dan mengecup keningnya dengan penuh rasa syukur: 'Selamat tidur, anak baik kebanggaan Ayah.' Tomi tertidur pulas, bermimpi meluncur menaiki mobil merah bersama Ayah melintasi jalanan bintang di langit malam.",
                    "textEn": "The night deepened and quiet comfort wrapped the warm home. Father tucked Tomi into bed, kissing his forehead with deep gratitude: 'Sleep well, my sweet boy, Father's greatest pride.' Tomi slept soundly, dreaming of riding the red car with Father across starlit roads.",
                    "quote": "Tidurlah dalam cinta yang tak bertepi, kasih sayang ayah dan anak abadi selamanya.",
                    "coReading": "Mari pejamkan mata dan rasakan kehangatan kasih sayang ayahmu sebelum tidur.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Tomi sleeping peacefully in bed with a cozy blanket. Father standing by the door looking back affectionately with a soft smile. Moonlight streaming through the window with twinkling stars, serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 100: Segelas Air & Pelukan untuk Ibu ---
        {
            "id": "story100",
            "storyNumber": 100,
            "title": "Segelas Air & Pelukan untuk Ibu",
            "englishTitle": "A Glass of Water & a Hug for Mother",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Bakti anak pada ibu, kepekaan terhadap rasa lelah orang tua, & kehangatan perhatian",
            "cover": "covers/story100_cover.jpg",
            "synopsis": "Dina melihat Ibu duduk menyandarkan kepala di sofa ruang tengah sehabis seharian merapikan rumah dan memasak. Dengan kedua tangan kecilnya yang berhati-hati, Dina membawakan segelas air sejuk dari gentong tanah liat dan memijat lembut pundak Ibu, menghadiahkan pelukan paling menenangkan di penghujung hari.",
            "protagonist": "Dina (Gadis cilik bertelapak tangan mungil)",
            "companion": "Ibu Dina (Ibu tersenyum haru memeluk putrinya)",
            "setting": "Sofa Ruang Istirahat",
            "pages": [
                {
                    "number": 1,
                    "title": "Ibu yang Bersandar di Sofa Hijau",
                    "titleEn": "Mother Resting on the Green Sofa",
                    "textId": "Sore hari ketika matahari meredup di balik jendela ruang tengah, Ibu duduk menyandarkan punggungnya di sofa kain hijau beludru. Kelopak mata Ibu terpejam lelah sehabis seharian mencuci pakaian, menyapu halaman, dan menyiapkan makanan lezat bagi keluarga.",
                    "textEn": "In the late afternoon as the sun softened outside the living room window, Mother sat leaning back on the green velvet sofa. Her eyes were closed in weariness after a full day of laundry, sweeping the yard, and cooking meals for the family.",
                    "quote": "Ibu bekerja tanpa lelah demi kehangatan dan kebahagiaan seluruh rumah.",
                    "coReading": "Pernahkah kamu melihat ibumu tampak lelah sehabis bekerja seharian?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Mother resting wearily with closed eyes on a cozy green sofa in a warm living room. Dina, a sweet little girl in a floral dress, watching her thoughtfully from the doorway, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Kepekaan Hati Gadis Cilik",
                    "titleEn": "The Gentle Heart of a Little Girl",
                    "textId": "Dina, gadis cilik berambut kepang dua berpita merah jambu, melangkah berjingkat tanpa alas kaki di atas lantai kayu. Dina tidak ingin membuat suara yang membangunkan Ibu. Dina melihat dahi Ibu yang berkeringat dan tenggorokannya yang tampak haus.",
                    "textEn": "Dina, a little girl with twin braids tied in pink ribbons, tiptoed barefoot across the wooden floorboards. She wanted to make no sound that might startle Mother. Dina noticed Mother's brow dampened with sweat and her parched lips.",
                    "quote": "Kepekaan melihat kebutuhan orang lain adalah awal dari bakti yang sejati.",
                    "coReading": "Apa yang dirasakan Dina saat melihat ibunya beristirahat?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Dina tiptoeing quietly across the room, finger pressed to her lips in a soft 'shh' gesture. Warm afternoon shadows, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Gelas Kaca Bening dan Gentong Sejuk",
                    "titleEn": "Clear Glass and the Cool Clay Urn",
                    "textId": "Dina melangkah ke dapur dengan hati-hati. Di atas meja dapur berdiri gentong air tanah liat yang menjaga air minum tetap dingin alami. Dina mengambil sebuah gelas kaca bening berhiaskan motif daun clover dari rak piring rendah.",
                    "textEn": "Dina stepped into the kitchen with careful steps. On the counter stood a clay water urn that kept drinking water naturally cool. Dina lifted a clear glass cup patterned with clover leaves from the low dish shelf.",
                    "quote": "Setiap tindakan penuh perhatian bermula dari niat yang murni dan tulus.",
                    "coReading": "Dari mana air minum yang sejuk itu diambil oleh Dina?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Dina standing on tiptoe at the kitchen counter, using a wooden ladle to scoop clear cool water from a clay urn into a glass cup. Sunlight illuminating the kitchen, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Cedukan Gayung Kayu yang Tenang",
                    "titleEn": "Quiet Scoop of the Wooden Ladle",
                    "textId": "Dengan gayung kayu kecil bertangkai panjang, Dina menceduk air jernih dari gentong. Tetesan air bergemericik lembut seperti nyanyian mata air pegunungan. Dina mengisi gelas itu hingga tiga perempat penuh agar tidak tumpah saat dibawa berjalan.",
                    "textEn": "With a long-handled wooden ladle, Dina scooped crystal-clear water from the urn. Droplets trickled softly like mountain spring music. Dina filled the glass three-quarters full so it wouldn't splash as she walked.",
                    "quote": "Kehati-hatian menjaga niat baik agar terwujud dengan sempurna.",
                    "coReading": "Mengapa Dina tidak mengisi air sampai penuh meluap?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Close-up of water pouring smoothly from a wooden ladle into the glass cup, sparkling drops glinting in the light. Dina's focused sweet face, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Langkah Perlahan Membawa Air",
                    "titleEn": "Slow Steps Carrying the Water",
                    "textId": "Dengan kedua tangannya memegangi gelas kaca erat-erat, Dina berjalan selangkah demi selangkah menyeberangi lorong rumah. Matanya terpaku pada permukaan air yang bergoyang tenang tanpa meneteskan setitik pun ke lantai.",
                    "textEn": "Holding the glass firmly with both small hands, Dina walked pace by pace across the hallway. Her eyes fixed upon the quiet water surface, not spilling a single droplet onto the floor.",
                    "quote": "Kesungguhan anak kecil tampak dari caranya menjaga apa yang dibawanya.",
                    "coReading": "Bisakah kamu membawa segelas air tanpa menumpahkannya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Dina carrying the glass of water with both hands, walking slowly with intense careful concentration along the hallway. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Bisikan Lembut di Tepi Sofa",
                    "titleEn": "A Gentle Whisper by the Sofa",
                    "textId": "Dina sampai di samping sofa hijau. Ia meletakkan gelas air di atas meja bundar kecil beralaskan tatakan kayu. Dengan lembut, Dina berbisik di telinga Ibu: 'Ibu... minumlah air sejuk ini, Dina sudah siapkan untuk Ibu.'",
                    "textEn": "Dina reached the green sofa. She set the glass on the little round side table atop a wooden coaster. Tenderly, Dina whispered by Mother's ear: 'Mother... please drink this cool water, Dina prepared it for you.'",
                    "quote": "Kata-kata lembut anak bagai embun penyejuk di tengah terik kelelahan.",
                    "coReading": "Apa yang dibisikkan Dina saat membangunkan Ibu?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Dina leaning gently toward Mother on the sofa, resting her hand on Mother's shoulder, pointing to the cool glass of water on the side table. Mother opening her eyes with a touched smile, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Tegukan Sejuk Penghilang Dahaga",
                    "titleEn": "Cool Sips That Quench the Thirst",
                    "textId": "Ibu membuka matanya perlahan dan tertegun menatap putrinya yang tersenyum manis. Ibu mengambil gelas itu dan meminum air sejuknya dengan penuh rasa syukur: 'Gluk, gluk, gluk...' Rasa dingin dan segar mengalir seketika menyegarkan tubuh Ibu yang lelah.",
                    "textEn": "Mother opened her eyes slowly, touched by the sight of her smiling little daughter. She lifted the glass, drinking the refreshing water with deep gratitude: 'Gulp, sip, swallow...' The cool freshness flowed, reviving her weary body.",
                    "quote": "Segelas air yang diantarkan dengan cinta terasa lebih manis dari madu manapun.",
                    "coReading": "Bagaimana perasaan Ibu saat meminum air pemberian Dina?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Mother drinking water from the clear glass with a relieved, grateful expression. Dina standing beside her holding Mother's hand, evening sunbeams casting warm golden light, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Pijatan Lembut di Pundak Ibu",
                    "titleEn": "Gentle Kneading on Mother's Shoulders",
                    "textId": "Setelah gelas kosong diletakkan kembali, Dina naik ke sofa di belakang Ibu. Dengan kedua telapak tangan mungilnya yang hangat, Dina memijat pundak Ibu perlahan: 'Pijat, tekan, usap lembut.' Otot-otot leher Ibu yang kaku perlahan mengendur dan rileks.",
                    "textEn": "Once the empty glass rested on the table, Dina climbed onto the sofa behind Mother. With warm little palms, Dina gently kneaded Mother's shoulders: 'Press, rub, gentle squeeze.' The tense muscles in Mother's neck loosened and relaxed.",
                    "quote": "Sentuhan tangan anak yang penuh kasih memiliki keajaiban penyembuh.",
                    "coReading": "Bisakah kamu memijat pundak ibumu seperti Dina?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Dina kneeling on the sofa behind Mother, gently massaging Mother's shoulders with both hands. Mother resting her head back with a peaceful blissful smile, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Pelukan Erat Paling Menghangatkan",
                    "titleEn": "The Warmest, Tightest Embrace",
                    "textId": "Ibu berbalik dan menarik Dina ke dalam pelukan dadanya yang hangat dan harum aroma bunga melati. Air mata haru menetes di pipi Ibu. 'Terima kasih, bidadari kecil Ibu. Segelas air dan pelukanmu adalah hadiah terindah di seluruh dunia.' Dina membenamkan wajahnya di ceruk leher Ibu.",
                    "textEn": "Mother turned, pulling Dina into her warm, jasmine-scented embrace. Tears of joy dotted Mother's cheeks. 'Thank you, my little angel. Your glass of water and hug are the most precious gift in the whole world.' Dina buried her face in Mother's neck.",
                    "quote": "Bakti yang tulus menciptakan ikatan batin yang tak akan pernah putus.",
                    "coReading": "Peluklah ibumu sekarang sehangat pelukan Dina dan Ibunya!",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother hugging Dina tightly against her chest on the green sofa, cheeks pressed together with tears of joy on Mother's face. Warm living room ambiance, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Damai Berdua di Sofa Senja",
                    "titleEn": "Peaceful Sleep Together on the Twilight Sofa",
                    "textId": "Lampu meja dinyalakan temaram, dan selimut rajut wol menutupi tubuh Ibu dan Dina. Keduanya tertidur pulas berdampingan di sofa hijau yang empuk. Di luar jendela, bintang senja pertama berkelip terang di langit ungu, menjaga kedamaian rumah yang penuh cinta itu.",
                    "textEn": "The side lamp glowed softly, and a knitted woolen blanket draped over Mother and Dina. Both drifted into peaceful sleep side by side on the plush green sofa. Outside the window, the first evening star twinkled brightly in the violet sky, guarding the peace of a home overflowing with love.",
                    "quote": "Tidurlah dalam dekapan kasih sayang sejati, dunia damai karena ada cinta di hatimu.",
                    "coReading": "Selamat tidur anak berbakti, semoga mimpi indah selalu melindungimu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Mother and Dina sleeping peacefully snuggled together on the green sofa under a soft floral quilt. Warm table lamp glowing, crescent moon and first star visible outside window. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 101: Makan Malam Tanpa Layar Kaca ---
        {
            "id": "story101",
            "storyNumber": 101,
            "title": "Makan Malam Tanpa Layar Kaca",
            "englishTitle": "Dinner Without Screens",
            "category": "family",
            "categoryLabel": "🏡 Keluarga & Rumah Hangat",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kehadiran utuh bersama keluarga, mendengarkan cerita meja makan, & kehangatan percakapan",
            "cover": "covers/story101_cover.jpg",
            "synopsis": "Malam ini Ayah dan Ibu sepakat menyimpan semua gawai dan mematikan televisi saat makan malam. Di meja makan bundar yang diterangi lentera gantung hangat, Budi, Kakak, dan kedua orang tua saling bercerita tentang hari mereka, diiringi sup jagung manis yang mengepul dan tawa riang.",
            "protagonist": "Keluarga Budi (Ayah, Ibu, Kakak, dan Adik duduk melingkar)",
            "companion": "Meja Penuh Makanan (Nasi hangat dan sup sayur beruap)",
            "setting": "Ruang Makan Hangat",
            "pages": [
                {
                    "number": 1,
                    "title": "Keranjang Anyaman Penyimpan Gawai",
                    "titleEn": "Woven Basket for Storing Gadgets",
                    "textId": "Sebelum duduk di meja makan, Ayah meletakkan sebuah keranjang anyaman bambu kecil di atas bufet ruang tengah. Ayah, Ibu, dan Kakak meletakkan telepon genggam mereka di dalam keranjang itu. Layar televisi di sudut ruangan juga dimatikan, menyisakan kesunyian yang tenang dan hangat di seluruh rumah.",
                    "textEn": "Before sitting at the dinner table, Father placed a small woven bamboo basket on the living room credenza. Father, Mother, and Sister placed their mobile phones inside. The television screen in the corner was switched off too, leaving a peaceful, warm silence throughout the home.",
                    "quote": "Mematikan layar adalah menyalakan kehadiran utuh bagi orang-orang tercinta.",
                    "coReading": "Pernahkah keluargamu makan bersama tanpa melihat layar gawai atau televisi?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Father placing his phone into a woven bamboo basket on a wooden sideboard with a smile. Budi and family gathered by the dining table in the background, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Lentera Gantung di Atas Meja Kayu",
                    "titleEn": "Hanging Lantern Over the Wooden Table",
                    "textId": "Di atas meja makan bundar berpapan jati, tergantung sebuah lampu gantung kap anyaman rotan yang memancarkan cahaya keemasan lembut. Meja makan beralaskan taplak kain perca buatan Nenek, menciptakan suasana seperti pondok peristirahatan di tengah hutan dongeng.",
                    "textEn": "Above the round teak dining table hung a rattan-shaded pendant lamp casting a soft, golden glow. The table was dressed in Grandma's handmade patchwork tablecloth, creating an atmosphere like a cozy woodland lodge.",
                    "quote": "Cahaya hangat mempertemukan tatapan mata yang saling menyayangi.",
                    "coReading": "Bagaimana suasana ruang makan keluarga Budi saat lampu gantung dinyalakan?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. A cozy dining room scene with a warm glowing rattan lantern hanging above a round wooden table. Family members pulling out chairs smiling, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Sup Jagung Manis yang Mengepul",
                    "titleEn": "Steaming Sweet Corn Soup",
                    "textId": "Ibu membawa mangkuk keramik besar berisi sup jagung manis wortel yang mengepulkan uap harum kaldu ayam kampung. Di sampingnya terhidang piring tempe goreng renyah dan nasi pulen yang hangat. Aroma sedap masakan rumah seketika membangkitkan selera makan semua orang.",
                    "textEn": "Mother brought a large ceramic tureen of sweet corn and carrot soup steaming with fragrant farm chicken broth. Beside it sat crispy fried tempeh and fluffy warm rice. The delightful aroma of home cooking instantly awakened everyone's appetite.",
                    "quote": "Makanan buatan rumah adalah wujud cinta yang paling mengenyangkan jiwa.",
                    "coReading": "Makanan apa yang disajikan Ibu di meja makan malam ini?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Mother setting down a steaming tureen of yellow corn soup on the dining table. Bowls of rice and crispy tempeh, mouthwatering steam curls, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Doa Bersama Mengawali Santap",
                    "titleEn": "Praying Together Before the Meal",
                    "textId": "Ayah memimpin doa syukur. Seluruh keluarga menundukkan kepala dan melipat tangan dengan khidmat, bersyukur atas rezeki berkah dan kesehatan yang dianugerahkan hari ini. Suasana terasa sangat damai tanpa gangguan bunyi dering telepon sama sekali.",
                    "textEn": "Father led the prayer of thanksgiving. The whole family bowed their heads, hands clasped solemnly, giving thanks for today's blessings and health. The room felt profoundly peaceful without a single phone ring interrupting.",
                    "quote": "Rasa syukur melipatgandakan kenikmatan dari setiap suapan makanan.",
                    "coReading": "Bagaimana caramu berdoa bersama keluarga sebelum makan?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. The family of four sitting around the round dining table with heads bowed and eyes closed in peaceful prayer. Warm golden lantern light, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Cerita Budi tentang Kucing Pohon",
                    "titleEn": "Budi's Story of the Tree Cat",
                    "textId": "Sambil menyendok sup jagung manisnya, Budi bercerita dengan riang: 'Tadi siang di sekolah, ada anak kucing loreng yang memanjat pohon mangga dan takut turun! Pak Guru harus membawa tangga bambu untuk menolongnya!' Seluruh meja makan tertawa mendengar gaya cerita Budi yang penuh gaya.",
                    "textEn": "Sipping his sweet corn soup, Budi shared cheerfully: 'At school today, a striped kitten climbed the mango tree and was too scared to climb down! The teacher had to bring a bamboo ladder to rescue it!' The whole table chuckled at Budi's animated storytelling.",
                    "quote": "Mendengarkan kisah anak dengan penuh perhatian menumbuhkan rasa percaya diri.",
                    "coReading": "Apa cerita seru yang dibagikan Budi di meja makan?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Budi gesturing with his spoon with an excited animated expression, telling his school story. Father, Mother, and Sister laughing and listening attentively, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Kisah Lukisan Bunga Milik Kakak",
                    "titleEn": "Sister's Story of the Flower Painting",
                    "textId": "Kakak melanjutkan dengan menceritakan tugas melukis bunga mataharinya yang mendapat bintang emas dari guru seni. Ayah mendengarkan sambil menatap mata putrinya dengan bangga, memuji perpaduan warna yang dipilih Kakak. Tidak ada yang menunduk melihat layar kaca.",
                    "textEn": "Sister followed by sharing about her sunflower painting that earned a gold star from the art teacher. Father listened, looking into his daughter's eyes with pride, praising her choice of colors. Nobody looked down at screens.",
                    "quote": "Tatapan mata yang tertuju utuh adalah hadiah perhatian paling berharga.",
                    "coReading": "Prestasi apa yang diraih Kakak di sekolah hari ini?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Sister talking happily with hands open, while Father and Mother smile proudly across the table. Warm dinner dishes, glowing lantern, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Tawa Renyah yang Memenuhi Ruangan",
                    "titleEn": "Crisp Laughter Filling the Room",
                    "textId": "Ayah kemudian menceritakan pengalamannya saat sepatunya kemasukan kerikil kecil di kantor. Lelucon Ayah membuat seisi meja terbahak-bahak. Tawa mereka berpadu dengan denting sendok keramik di atas piring, menciptakan musik keluarga yang sangat membahagiakan.",
                    "textEn": "Father then told a funny story about a pebble stuck inside his work shoe at the office. Father's joke sent the whole table into bursts of laughter. Their chuckles blended with the clink of ceramic spoons on plates, creating joyful family music.",
                    "quote": "Tawa bersama di meja makan adalah perekat terkuat bagi keutuhan keluarga.",
                    "coReading": "Cerita lucu apa yang pernah membuat seluruh keluargamu tertawa bersama?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. The whole family laughing wholeheartedly together around the round table, cheeks glowing with merriment. Warm dishes of food nearly finished, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Membantu Ibu Merapikan Piring",
                    "titleEn": "Helping Mother Clear the Plates",
                    "textId": "Sehabis santap malam, Budi dan Kakak tidak langsung berlari ke kamar. Mereka membantu mengangkat piring-piring kotor ke wastafel dapur. Ayah menyeka meja dengan kain lap bersih. Bekerja sama merapikan meja makan terasa seringan permainan petualangan.",
                    "textEn": "After dinner, Budi and Sister didn't bolt to their rooms. They helped carry dishes to the kitchen sink. Father wiped down the table with a clean cloth. Clearing the dining room together felt as breezy as a shared game.",
                    "quote": "Gotong royong di rumah melatih tanggung jawab dan kemandirian anak.",
                    "coReading": "Bagaimana cara Budi dan Kakak membantu setelah makan malam?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Budi carrying a stack of bowls carefully toward the kitchen, Sister carrying drinking cups, Father wiping the round table. Cozy teamwork ambiance, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Teh Chamomile Hangat Sebelum Tidur",
                    "titleEn": "Warm Chamomile Tea Before Bed",
                    "textId": "Ibu menyeduh teko porselen berisi teh chamomile beraroma bunga apel yang menenangkan. Seluruh keluarga duduk sejenak di ruang tengah, menikmati tegukan teh hangat tanpa menyalakan televisi. Ruangan terasa dipenuhi oleh ketenangan dan kebersamaan yang mendalam.",
                    "textEn": "Mother brewed a porcelain pot of chamomile tea scented with calming apple blossoms. The whole family sat together in the living room, savoring warm sips without turning on the television. The room breathed with deep peace and togetherness.",
                    "quote": "Ketenangan jiwa lahir saat kita terbebas dari kebisingan dunia luar.",
                    "coReading": "Minuman hangat apa yang diseduh Ibu untuk diminum bersama?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Family sitting peacefully on sofa cushions around a low coffee table with steaming ceramic tea cups. Warm lamp light, peaceful smiles, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Pulas Berbantal Kedamaian",
                    "titleEn": "Sound Sleep Pillowed on Peace",
                    "textId": "Malam tiba dan seluruh lampu dipadamkan menyisakan temaram lampu malam. Budi tidur lelap di kamarnya dengan hati yang penuh rasa hangat dan dicintai. Tanpa silau layar kaca, tidur malamnya begitu pulas dan tenang, ditemani mimpi-mimpi indah tentang keluarga yang selalu saling menyayangi.",
                    "textEn": "Night arrived and lights were extinguished, leaving only the soft glow of nightlights. Budi slept deeply in his room with a heart brimming with warmth and love. Free from harsh screen glare, his sleep was sound and sweet, embraced by dreams of a family that forever cherishes one another.",
                    "quote": "Tidurlah dalam kehangatan keluarga, cinta di rumahmu adalah pelindung abadi jiwamu.",
                    "coReading": "Selamat tidur anak hebat, besok meja makan hangat akan menunggumu kembali.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Budi sleeping serenely in bed with a quilt, smiling in peaceful rest. Crescent moon and stars glowing outside the open window, serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
