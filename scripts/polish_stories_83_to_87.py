# scripts/polish_stories_83_to_87.py
import json

def get_stories_83_to_87():
    stories = [
        # --- STORY 83: Burung Terbang Bayangan Jari ---
        {
            "id": "story83",
            "storyNumber": 83,
            "title": "Burung Terbang Bayangan Jari",
            "englishTitle": "Flying Bird of Finger Shadows",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kreativitas seni bayangan tangan & mengusir rasa takut dalam gelap",
            "cover": "covers/story83_cover.jpg",
            "synopsis": "Ketika lampu kamar dimatikan sebelum tidur, Danis sempat merasa cemas melihat dinding yang gelap. Mama menyalakan senter kecil dan mengaitkan kedua jempol tangannya membentuk burung bayangan yang mengepakkan sayap di dinding, membawa tawa hangat sebelum tidur.",
            "protagonist": "Danis (Anak laki-laki melengkungkan kedua jempolnya)",
            "companion": "Mama Danis (Ibu memegang lampu senter kecil)",
            "setting": "Dinding Kamar Tidur",
            "pages": [
                {
                    "number": 1,
                    "title": "Lampu Utama yang Dipadamkan",
                    "titleEn": "The Main Light Clicks Off",
                    "textId": "Klik! Sakelar dinding ditekan dan lampu utama kamar Danis padam seketika. Kamar tidur mendadak menjadi remang-remang disinari cahaya temaram lampu lorong. Danis menarik selimut birunya hingga ke bawah hidung, memandang dinding putih polos dengan rasa agak berdebar.",
                    "textEn": "Click! The wall switch snapped and the main bedroom light went out. The room fell into cozy shadows lit only by a faint hall glow. Danis pulled his blue blanket up to his nose, gazing at the bare white wall with a fluttering heart.",
                    "quote": "Kegelapan sering kali hanya membutuhkan sedikit percikan cahaya untuk menjadi ramah.",
                    "coReading": "Apakah kamu pernah merasa sedikit takut saat lampu kamar dimatikan?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Danis, a cute young boy in patterned pajamas, tucked under a blue quilt in bed, looking at the dim bedroom wall with big round eyes. Mother standing by the doorway smiling gently, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Sorot Senter Kecil Mama",
                    "titleEn": "Mama's Little Flashlight Beam",
                    "textId": "Mama duduk di tepi ranjang dan mengeluarkan senter saku kuning kecil dari sakunya. Ketika Mama menyalakannya, sebuah lingkaran cahaya bulat keemasan menyala di dinding, seperti panggung sandiwara mini yang siap menampilkan pertunjukan.",
                    "textEn": "Mother sat on the edge of the bed and pulled a little yellow pocket flashlight from her robe. When she clicked it on, a round golden circle of light illuminated the wall, like a miniature theater stage ready for a show.",
                    "quote": "Sebuah cahaya kecil mampu mengubah rasa takut menjadi rasa ingin tahu yang hangat.",
                    "coReading": "Bisakah kamu membuat lingkaran cahaya dengan senter di dinding?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Mother aiming a small flashlight beam onto a smooth white wall, creating a glowing golden circle. Danis sitting up in bed with curious smiling face, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Kaitan Dua Jempol Tangan",
                    "titleEn": "Hooking the Two Thumbs",
                    "textId": "Mama meletakkan tangannya di antara senter dan dinding. Mama menyilangkan pergelangan tangannya dan mengaitkan kedua ibu jarinya erat-erat. Jari-jari lainnya direntangkan ke samping seperti bulu-bulu sayap. 'Lihat, Danis, siapa yang datang mengunjungi kamarmu?' bisik Mama.",
                    "textEn": "Mother placed her hands between the beam and the wall. Crossing her wrists, she hooked both thumbs firmly together. Her other fingers spread wide like feather tips. 'Look, Danis, who has come to visit your room?' whispered Mother.",
                    "quote": "Benda paling ajaib ada di ujung jemari tangan kita sendiri.",
                    "coReading": "Coba silangkan pergelangan tanganmu dan kaitkan kedua jempolmu!",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Close-up of Mother's hands gracefully crossed with thumbs linked, casting a sharp shadow of a flying bird onto the wall circle. Intimate warm lighting, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Burung Merpati yang Mengepakkan Sayap",
                    "titleEn": "The Dove Flapping Its Wings",
                    "textId": "Di dinding kamar, tampak bayangan hitam pekat seekor burung merpati yang anggun! Saat Mama menggerakkan jari-jarinya naik-turun, bayangan burung itu mengepakkan sayapnya seolah sedang terbang melayang di angkasa. Danis bertepuk tangan tanpa suara karena takjub.",
                    "textEn": "On the bedroom wall appeared the crisp dark shadow of an elegant flying dove! As Mother fluttered her fingers up and down, the shadow bird flapped its wings as if soaring across open skies. Danis clapped silently in sheer wonder.",
                    "quote": "Imajinasi menghidupkan bayangan menjadi teman bermain yang menyenangkan.",
                    "coReading": "Bisakah kamu menggerakkan jari-jarimu menirukan kepakan sayap burung?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. The bird hand-shadow flapping dynamically on the wall inside the golden circle of light. Danis smiling happily with hands clapping in bed, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Kelinci Lucu yang Menggoyangkan Telinga",
                    "titleEn": "A Cute Bunny Wiggling Its Ears",
                    "textId": "Mama mengubah bentuk tangannya: mengepalkan satu tangan dan menegakkan dua jari telunjuk serta jari tengah. Di dinding muncul kepala kelinci kecil! Jari kelingking Mama bergerak maju mundur seperti hidung kelinci yang sedang mengendus wortel manis.",
                    "textEn": "Mother changed her hand shape: making a loose fist and raising two fingers high. On the wall popped a little rabbit head! Mother's pinky wiggled back and forth like a bunny sniffing a sweet carrot.",
                    "quote": "Variasi sederhana melahirkan karakter-karakter baru yang menggemaskan.",
                    "coReading": "Hewan apakah yang telinganya panjang dan suka makan wortel?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother casting a cute bunny shadow with long wiggling ears on the wall. Danis leaning forward with bright eyes full of laughter, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Giliran Jemari Danis Mencoba",
                    "titleEn": "Danis's Fingers Take a Turn",
                    "textId": "Danis mengulurkan kedua tangannya sendiri ke arah sorot cahaya senter. Jemarinya yang mungil sedikit gemetar. Mama dengan lembut membetulkan posisi jempol Danis hingga saling mengunci. 'Ayo kepakkan sayapmu, Danis!' dorong Mama.",
                    "textEn": "Danis reached both of his own small hands into the flashlight beam. His little fingers trembled slightly. Mother gently adjusted his thumb lock. 'Go ahead, flap your wings, Danis!' Mother encouraged.",
                    "quote": "Mencoba sendiri memberi rasa percaya diri yang berharga.",
                    "coReading": "Apakah kamu pernah mencoba membuat bayangan tangan di dinding rumahmu?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Mother gently guiding Danis's hands in front of the warm flashlight light. Danis focusing with an adorable earnest expression, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Anak Burung Melayang Bersama Induk",
                    "titleEn": "The Baby Bird Flies with Mother",
                    "textId": "Danis menggerakkan jari-jarinya. Di dinding kini terbang dua ekor burung bayangan: satu burung besar milik Mama dan satu anak burung mungil milik Danis. Kedua burung itu terbang beriringan, saling bersentuhan paruh dengan penuh kelembutan.",
                    "textEn": "Danis fluttered his fingers. On the wall now flew two shadow birds: a big mother bird and Danis's little baby bird. The two birds glided side by side, gently touching beaks in sweet affection.",
                    "quote": "Kebersamaan orang tua dan anak adalah melodi terindah pengantar tidur.",
                    "coReading": "Lihatlah dua burung bayangan itu saling menyentuh paruhnya!",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Two shadow birds (one large, one small) flying together on the illuminated wall circle. Mother and Danis sitting side by side on the bed holding their hands up, smiling with bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Anjing Setia yang Menjaga Pintu",
                    "titleEn": "The Faithful Dog Guarding the Door",
                    "textId": "Danis melipat jemarinya lagi membentuk moncong anjing dengan telinga terkulai. Bayangan itu membuka dan menutup mulutnya: 'Guk, guk!' tiru Danis sambil terkikik. 'Ini anjing setia yang akan menjaga kamarku sepanjang malam, Ma,' kata Danis bangga.",
                    "textEn": "Danis folded his fingers into a dog snout with floppy ears. The shadow opened and shut its mouth: 'Woof, woof!' Danis mimicked with a giggle. 'This is our faithful pup who will guard my room all night, Mom,' Danis declared proudly.",
                    "quote": "Rasa aman tercipta ketika hati dipenuhi oleh tawa dan imajinasi ceria.",
                    "coReading": "Suara hewan apa yang ditirukan Danis?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Danis casting a playful puppy dog shadow on the wall that appears to bark happily. Mother laughing warmly, cozy bedtime ambiance, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Mengepakkan Sayap Menuju Langit Bintang",
                    "titleEn": "Wings Flapping to Starlit Skies",
                    "textId": "Mama mematikan senter kuningnya perlahan. Kini kamar kembali remang-remang disinari cahaya bulan dari balik jendela. Danis tidak lagi merasa takut pada dinding yang gelap. Di matanya, dinding itu kini dipenuhi jejak-jejak tawa burung dan kelinci ajaib.",
                    "textEn": "Mother clicked off the yellow flashlight softly. The room returned to gentle dusk lit by moonlight through the curtains. Danis no longer feared the dark wall. In his eyes, the wall was now filled with footprints of magical flying birds and friendly rabbits.",
                    "quote": "Cinta kasih mengubah hal yang menakutkan menjadi ruang penuh kehangatan.",
                    "coReading": "Apakah Danis masih takut pada kamar yang gelap?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother kissing Danis's forehead tenderly as he lies tucked under his blue quilt. Soft blue moonlight streaming across the bed and bedroom wall, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Pulas Bersama Burung Impian",
                    "titleEn": "Sound Sleep with the Dream Bird",
                    "textId": "Mama menyelimuti Danis dengan rapi dan berbisik, 'Selamat tidur, anak berani.' Danis memejamkan matanya sambil tersenyum manis. Di dalam mimpinya, burung bayangan bersayap emas terbang membawanya melintasi samudra bintang menuju pagi yang cerah.",
                    "textEn": "Mother tucked Danis in warmly, whispering, 'Goodnight, my brave boy.' Danis closed his eyes with a sweet smile. In his dreams, the golden-winged shadow bird flew him across oceans of stars toward a sunny tomorrow.",
                    "quote": "Tidurlah dengan damai, mimpi indah selalu terbang menyambut hatimu.",
                    "coReading": "Mari pejamkan mata dan terbangkan burung mimpimu ke langit malam.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Danis sleeping serenely with a peaceful smile. A gentle glowing dream-bird silhouette flying above under twinkling night stars and a smiling crescent moon outside the window. Deep peaceful bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 84: Ksatria Bunga Bermantel Selimut ---
        {
            "id": "story84",
            "storyNumber": 84,
            "title": "Ksatria Bunga Bermantel Selimut",
            "englishTitle": "Flower Knight with a Blanket Cloak",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Keberanian melindungi yang lemah & imajinasi ksatria pelindung alam",
            "cover": "covers/story84_cover.jpg",
            "synopsis": "Zidan memakai helm kardus berhiaskan daun pakis dan mantel selimut tidur merah tua. Bersama ayam jago kesayangannya, Si Jalu, Ksatria Zidan berpatroli menjaga kebun mawar dan bunga kamboja dari gangguan angin kencang dan ulat nakal.",
            "protagonist": "Zidan (Anak kecil bertopi helm kardus)",
            "companion": "Ayam Jago (Ayam jago berkokok gagah)",
            "setting": "Pekarangan Kebun Bunga",
            "pages": [
                {
                    "number": 1,
                    "title": "Pahlawan dari Negeri Selimut",
                    "titleEn": "Hero from the Blanket Realm",
                    "textId": "Pagi itu di beranda belakang rumah, Zidan mengikatkan selimut tidur wol merah tuanya di sekeliling leher dengan simpul longgar yang aman. Selimut itu melambai ke belakang seperti jubah jenderal perkasa. Di kepalanya terpasang mahkota helm dari karton berkilau perak.",
                    "textEn": "That morning on the back veranda, Zidan fastened his deep red woolen blanket loosely around his neck with a safe knot. The blanket billowed behind him like a valiant general's cape. Atop his head rested a cardboard knight's helmet sparkling with silver paper.",
                    "quote": "Keberanian dimulai dari tekad untuk menjaga keindahan di sekitar kita.",
                    "coReading": "Pernahkah kamu memakai selimut sebagai jubah pahlawan super?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Zidan, a spirited young boy in a silver cardboard helmet and a flowing red blanket cape, standing bravely on the veranda steps. Wooden sword in hand, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Kuda Tempur Bersayap Emas",
                    "titleEn": "The Golden-Feathered Steed",
                    "textId": "Di samping Zidan, Si Jalu, ayam jago berbulu merah keemasan dengan jengger merah tegak, berkokok nyaring: 'Kuk-kuruyuuuk!' Bagi Ksatria Zidan, Si Jalu adalah kawan setia yang selalu siap menemani patroli menjaga perbatasan pekarangan kebun.",
                    "textEn": "Beside Zidan stood Si Jalu, a handsome rooster with fiery golden-red feathers and an upright crimson comb, crowing proudly: 'Cock-a-doodle-doo!' To Knight Zidan, Si Jalu was his faithful companion always ready for duty on the garden frontier.",
                    "quote": "Kawan sejati selalu berdiri di samping kita dalam setiap petualangan.",
                    "coReading": "Bagaimana suara kokokan ayam jago peliharaan Zidan?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Zidan in his red cape standing proudly beside Si Jalu the handsome golden-red rooster who crows with neck stretched high. Sunny backyard garden, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Pedang Bambu Berujung Halus",
                    "titleEn": "Smooth-Tipped Bamboo Sword",
                    "textId": "Kakek telah membuatkan sebilah pedang kayu bambu tumpul yang diamplas sangat halus dan berujung bulat. 'Ingat, Ksatria Zidan,' pesan Kakek, 'pedang ksatria sejati bukan untuk melukai, melainkan tongkat penolong untuk menyangga tangkai tanaman yang patah.'",
                    "textEn": "Grandpa had whittled a smooth wooden toy sword from bamboo, rounded at the tip. 'Remember, Knight Zidan,' Grandpa reminded, 'a true knight's sword is not for hurting, but a staff to prop up fallen flower stems.'",
                    "quote": "Kekuatan sejati digunakan untuk menolong dan menyembuhkan.",
                    "coReading": "Untuk apa ksatria menggunakan pedang kayunya?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Grandpa handing the smooth rounded wooden sword to Zidan on the porch. Zidan bowing respectfully in his red cape, bead dot eyes, warm family atmosphere, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Patroli di Bawah Rindang Kamboja",
                    "titleEn": "Patrol Beneath Shady Frangipani",
                    "textId": "Ksatria Zidan melangkah gagah menyusuri jalan setapak di antara semak mawar merah dan pohon kamboja putih yang wangi. Mantel merahnya berdesir menyapu bunga-bunga rumput. Si Jalu melangkah di sampingnya, mematuk kerikil sambil mengawasi sekitar dengan waspada.",
                    "textEn": "Knight Zidan marched proudly down the garden path between red rose bushes and sweet-smelling white frangipani trees. His red cape swept gently over grass blooms. Si Jalu strutted alongside, pecking pebbles while keeping a watchful eye on their surroundings.",
                    "quote": "Tanggung jawab yang diemban dengan bangga terasa sangat mulia.",
                    "coReading": "Bunga apa saja yang dijaga oleh Ksatria Zidan?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Zidan marching purposefully down a garden stone path lined with blooming flowers, red cape fluttering. Rooster strutting proudly beside him, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Tangkai Mawar yang Terkulai",
                    "titleEn": "The Drooping Rose Stem",
                    "textId": "Di sudut pagar, Ksatria Zidan menemukan setangkai mawar merah muda yang terkulai lemas karena ditiup angin semalam. Bunganya hampir menyentuh tanah berlumpur. 'Bertahanlah, Putri Mawar! Ksatria Bunga datang menolongmu!' seru Zidan.",
                    "textEn": "By the fence corner, Knight Zidan discovered a pink rose stem drooping wearily from last night's gust. Its petals were nearly brushing the muddy earth. 'Hold on, Princess Rose! The Flower Knight is here to rescue you!' cried Zidan.",
                    "quote": "Mata yang sigap selalu menemukan siapa yang membutuhkan bantuan.",
                    "coReading": "Apa yang terjadi pada bunga mawar merah muda di sudut pagar?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Zidan kneeling tenderly in his cape beside a drooping pink rose bush. Rooster tilting its head curiously, simple black bead dot eyes, garden fence background, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Tongkat Penopang Sang Ksatria",
                    "titleEn": "The Knight's Support Staff",
                    "textId": "Zidan menancapkan bilah bambu halusnya ke dalam tanah di samping mawar. Dengan seutas tali sabut kelapa yang lembut, ia mengikat tangkai mawar ke tiang bambu dengan ikatan longgar. Bunga mawar itu kini kembali berdiri tegak dan anggun menyapa matahari pagi.",
                    "textEn": "Zidan staked his smooth bamboo stick into the soil beside the rose. With a soft strand of coconut fiber, he tied the stem loosely to the wooden post. The pink rose now stood tall and lovely once more, greeting the morning sun.",
                    "quote": "Bantuan yang sederhana mampu mengembalikan kehormatan dan keindahan.",
                    "coReading": "Bagaimana cara Zidan menolong bunga mawar agar tegak kembali?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Zidan carefully tying a soft plant tie around a tall pink rose stem and a bamboo stake. Si Jalu crowing happily beside him, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Ulat Bulu yang Dipindahkan",
                    "titleEn": "The Relocated Woolly Caterpillar",
                    "textId": "Tiba-tiba Si Jalu berkokok memperingatkan. Di atas daun melati, seekor ulat berbulu hitam sedang bersiap mengerat kuncup bunga. Alih-alih menyakitinya, Zidan menggunakan sehelai daun kering untuk memindahkan si ulat ke semak liar di balik pagar luar kebun.",
                    "textEn": "Suddenly Si Jalu gave a warning cluck. On a jasmine leaf, a fuzzy black caterpillar was preparing to nibble a fresh bud. Instead of hurting it, Zidan used a dry fallen leaf to carry the caterpillar safely to wild bushes beyond the garden fence.",
                    "quote": "Ksatria sejati bersikap adil dan melindungi semua makhluk hidup.",
                    "coReading": "Ke mana Zidan memindahkan ulat bulu itu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Zidan gently carrying a dry leaf with a small fuzzy caterpillar on it toward the garden gate. Red cape flowing, rooster following faithfully, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Mahkota Bunga dari Ratu Ibu",
                    "titleEn": "Flower Crown from the Queen Mother",
                    "textId": "Ibu yang menyaksikan dari teras tersenyum haru. Ibu memetik tiga kuntum melati dan merangkainya menjadi kalung bunga harum. Ibu mengalungkan bunga itu di leher Zidan. 'Untuk Ksatria Bunga paling pemberani dan penuh kasih di seluruh kerajaan,' puji Ibu hangat.",
                    "textEn": "Mother, watching from the veranda, smiled with pride. She wove three jasmine blossoms into a fragrant floral garland, placing it over Zidan's shoulders. 'For the bravest and kindest Flower Knight in the entire kingdom,' Mother praised warmly.",
                    "quote": "Pujian atas kebaikan hati adalah mahkota terindah bagi seorang anak.",
                    "coReading": "Hadiah apa yang diberikan Ibu kepada Ksatria Zidan?",
                    "imagePrompt": "Warm oil pastel illustration on heavy cream paper. Mother placing a sweet white jasmine garland around Zidan's neck as he stands proudly in his red blanket cape and cardboard helmet. Sunlight pouring over the blooming veranda, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Pelepasan Mantel dan Pedang Kayu",
                    "titleEn": "Laying Down the Cloak and Wooden Sword",
                    "textId": "Matahari sore mulai condong dan Si Jalu telah melompat ke dahan pohon jambu untuk tidur. Zidan melepaskan helm kardusnya dan melipat mantel selimut merahnya dengan rapi. Tugas ksatria hari ini telah selesai dengan penuh kemenangan damai.",
                    "textEn": "The evening sun dipped low and Si Jalu roosted onto a guava branch for the night. Zidan set down his cardboard helmet and folded his red blanket cape neatly. The knight's patrol for today was peacefully and triumphantly complete.",
                    "quote": "Pahlawan yang bijak tahu kapan waktu beristirahat dengan tenang.",
                    "coReading": "Di mana Si Jalu tidur malam ini?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Zidan setting his cardboard helmet on a chair and folding his red blanket on the bed. Rooster sleeping on a tree branch outside the window, soft twilight glow, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Lelap Sang Ksatria Pelindung",
                    "titleEn": "Deep Slumber of the Guardian Knight",
                    "textId": "Zidan merebahkan tubuhnya di ranjang dan menyelimuti dirinya dengan mantel wol merah yang harum melati. Di luar jendela, bunga-bunga mawar dan kamboja tidur lelap dalam lindungan malam. Ksatria kecil kita tersenyum damai, terlelap dalam mimpi indah penuh keberanian.",
                    "textEn": "Zidan tucked into bed, pulling the jasmine-scented red woolen cape over himself as a cozy blanket. Outside the window, the roses and frangipanis slept soundly in the peaceful night. Our little knight smiled softly, drifting into heroic, sweet dreams.",
                    "quote": "Tidurlah dalam damai wahai ksatria kecil, kebaikan hatimu menjaga dunia.",
                    "coReading": "Selamat tidur pahlawan kebun, esok bunga-bunga akan menyapamu kembali.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Zidan sleeping peacefully under the red blanket in his cozy room, cardboard helmet resting on his bedside stand. Outside the window, blooming flowers under moonlit night sky and stars. Serene bedtime scene, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 85: Kartu Kolase Kelopak Mawar ---
        {
            "id": "story85",
            "storyNumber": 85,
            "title": "Kartu Kolase Kelopak Mawar",
            "englishTitle": "Rose Petal Collage Card",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Ungkapan rasa syukur pada ibu, kerajinan kolase, & kehangatan cinta",
            "cover": "covers/story85_cover.jpg",
            "synopsis": "Melati mengumpulkan kelopak-kelopak mawar merah dan merah muda yang luruh di atas rumput kebun depan. Bersama selembar karton lipat dan getah lem kanji, Melati menempelkan kelopak-kelopak bunga itu menjadi bentuk hati beraroma semerbak untuk kado ulang tahun Ibu.",
            "protagonist": "Melati (Gadis cilik berpita ungu membawa lem kayu)",
            "companion": "Ibu Melati (Ibu terharu menerima kartu kolase)",
            "setting": "Teras Depan Berbunga",
            "pages": [
                {
                    "number": 1,
                    "title": "Kelopak Mawar yang Rontok di Atas Rumput",
                    "titleEn": "Rose Petals Fallen on the Grass",
                    "textId": "Pagi yang sejuk di teras depan, rumpun bunga mawar Ibu bermekaran dengan indahnya. Angin pagi yang berhembus lembut merontokkan puluhan kelopak bunga merah beludru dan merah jambu ke atas rumput hijau. Kelopak-kelopak itu masih segar dan berembun bening.",
                    "textEn": "On a cool morning on the front porch, Mother's rose bushes bloomed radiantly. A gentle morning breeze shook dozens of velvety red and blush-pink petals down onto the green grass. The petals were still dewy and delightfully fresh.",
                    "quote": "Kelopak bunga yang luruh masih menyimpan keharuman dan keindahan yang utuh.",
                    "coReading": "Pernahkah kamu memegang kelopak bunga mawar yang lembut seperti kain sutra?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Melati, a sweet young girl in a purple hair ribbon and floral pinafore dress, kneeling on a lush lawn collecting fallen red and pink rose petals into an enameled tin plate. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Piring Seng Berisi Bunga",
                    "titleEn": "An Enameled Plate Filled with Blooms",
                    "textId": "Melati memunguti kelopak-kelopak itu satu demi satu dengan jemari tangannya yang mungil. Piring seng putih berbintik biru di pangkuannya segera penuh dengan tumpukan kelopak mawar aneka warna yang menebarkan wangi manis semerbak.",
                    "textEn": "Melati gathered the petals one by one with her delicate little fingers. The blue-speckled white enamel plate on her lap soon brimmed with colorful rose petals, wafting a sweet, heavenly fragrance.",
                    "quote": "Mengumpulkan hal-hal kecil dengan cinta melahirkan persembahan yang agung.",
                    "coReading": "Warna apa saja kelopak mawar yang dikumpulkan Melati?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up of Melati's hands gently arranging fresh velvety red and soft pink rose petals on an enameled vintage plate. Morning sunbeams, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Kertas Tebal Berserat Wangi",
                    "titleEn": "Fragrant Textured Cardstock",
                    "textId": "Melati membawa kelopak mawar ke meja teras. Di sana terbentang selembar kertas karton tebal berwarna krem yang dilipat menjadi kartu ucapan dua muka. Hari ini adalah hari ulang tahun Ibu, dan Melati ingin membuat hadiah terindah dengan tangannya sendiri.",
                    "textEn": "Melati carried the petals to the porch table. There lay a sheet of thick cream cardstock folded into a greeting card. Today was Mother's birthday, and Melati wished to create the loveliest gift with her own two hands.",
                    "quote": "Hadiah buatan tangan menyimpan detak kasih sayang yang tulus.",
                    "coReading": "Kado apa yang ingin dibuat Melati untuk ulang tahun Ibu?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Melati sitting at a wooden table with a folded cream card, small pot of starch glue, and a bowl of rose petals. Pigtails tied with purple ribbons, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Garis Pensil Berbentuk Hati",
                    "titleEn": "Pencil Lines in a Heart Shape",
                    "textId": "Dengan pensil warnanya, Melati menggambar sebuah bentuk hati besar di halaman depan kartu. Garisnya melengkung bulat dan ramah. Di tengah bentuk hati itu, Melati menuliskan huruf-huruf pertamanya: 'UNTUK IBU TERCINTA'.",
                    "textEn": "With her colored pencil, Melati sketched a big heart in the center of the card front. The lines curved round and cheerful. Inside the heart, Melati carefully lettered her first words: 'FOR DEAREST MOTHER'.",
                    "quote": "Bentuk hati adalah simbol sederhana bagi kasih yang tak bertepi.",
                    "coReading": "Bisakah kamu menggambar bentuk hati dengan jarimu di udara?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Close-up of the cream cardstock showing a large sketched heart outline, with Melati's hands ready to decorate it. Colorful crayons nearby, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Olesan Lem Kanji yang Lembut",
                    "titleEn": "Gentle Dabs of Starch Paste",
                    "textId": "Melati menggunakan kuas kecil berbulu halus untuk mengoleskan getah lem kanji transparan di dalam garis hati. Lem kanji itu tidak berbau menyengat dan dingin di jari tangan Melati, siap merekatkan kelopak-kelopak bunga tanpa merusak warnanya.",
                    "textEn": "Melati used a fine, soft brush to spread transparent starch paste inside the heart outline. The starch paste was gentle, odorless, and cool on her fingers, ready to bond the flower petals without dulling their radiant colors.",
                    "quote": "Bahan alami menjaga kemurnian dan keindahan karya seni.",
                    "coReading": "Mengapa Melati memilih lem kanji yang lembut?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Melati dabbing a small wooden brush into a bowl of clear paste and spreading it inside the heart outline on her card. Sunlight filtering through porch vines, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Menempel Kelopak Berlapis-Lapis",
                    "titleEn": "Layering Petals One by One",
                    "textId": "Satu per satu, Melati menempelkan kelopak mawar. Di bagian luar, ia menata kelopak merah tua yang pekat. Di bagian tengah, ia menyusun kelopak merah jambu muda yang lembut. Kelopak-kelopak itu tersusun rapi seperti sisik naga peri yang indah dan bersusun.",
                    "textEn": "One by one, Melati pressed the rose petals down. Along the outside, she arranged deep crimson petals. In the middle, she nestled soft blush-pink petals. The petals overlapped neatly like the gentle scales of a fairy-tale flower.",
                    "quote": "Ketelatenan menyusun helai demi helai melahirkan mahakarya yang menawan.",
                    "coReading": "Bagaimana Melati membedakan warna kelopak di luar dan di dalam hati?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. The card showing a gorgeous textured collage heart made entirely of overlapping real velvety rose petals. Melati placing a small pink petal in the center, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Tangkai Daun Hijau di Ujung Bawah",
                    "titleEn": "A Green Leaf Stem at the Tip",
                    "textId": "Sebagai sentuhan akhir, Melati menempelkan dua helai daun mawar hijau bergerigi di pangkal hati dan mengikat sehelai pita ungu kecil di sudut kartu. Kartu kolase itu kini tampak seperti bunga mawar abadi yang harum semerbak.",
                    "textEn": "For the finishing touch, Melati pasted two jagged green rose leaves at the heart's base and tied a tiny purple ribbon at the card's corner. The collage card now looked like an everlasting, sweet-scented rose bloom.",
                    "quote": "Sentuhan dedaunan hijau memberi kesegaran alami pada kehangatan warna merah.",
                    "coReading": "Benda apa yang ditempelkan Melati di bagian bawah gambar hati?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. The completed floral collage card lying on the table, surrounded by fallen petals and a purple ribbon bow. Melati smiling in admiration with clasped hands, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Langkah Mengendap Menuju Dapur",
                    "titleEn": "Tiptoeing Towards the Kitchen",
                    "textId": "Dengan kedua tangannya membawa kartu yang sudah kering, Melati berjingkat masuk ke dapur. Ibu sedang merapikan teko teh madu hangat. Melati menyembunyikan kartu di balik punggungnya sambil tersenyum lebar: 'Selamat ulang tahun, Ibu tercinta!'",
                    "textEn": "Holding the dried card carefully with both hands, Melati tiptoed into the kitchen. Mother was preparing a pot of warm honey tea. Melati hid the card behind her back with a beaming grin: 'Happy birthday, dearest Mother!'",
                    "quote": "Kejutan yang tulus menghadirkan kebahagiaan manis di hati keluarga.",
                    "coReading": "Di mana Melati menyembunyikan kartunya sebelum diberikan pada Ibu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Melati standing in the cozy rustic kitchen with hands behind her back, grinning up at her mother who turns from the counter with surprised joy. Bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Air Mata Haru dan Pelukan Hangat",
                    "titleEn": "Tears of Joy and a Warm Embrace",
                    "textId": "Ibu menerima kartu itu dan mencium aroma mawar semerbak yang menguar dari kelopak-kelopak kolase. Mata Ibu berkaca-kaca penuh keharuan. Ibu memeluk Melati erat-erat dan mencium kedua pipinya. 'Ini kado paling harum dan terindah di dunia, Melati sayang,' bisik Ibu bergetar bahagia.",
                    "textEn": "Mother received the card, inhaling the sweet rose scent rising from the collage petals. Mother's eyes misted with happy tears. She scooped Melati into a tight hug, kissing both cheeks. 'This is the most fragrant and precious gift in the entire world, my sweet Melati,' Mother whispered.",
                    "quote": "Kasih sayang anak adalah perhiasan paling mulia bagi seorang ibu.",
                    "coReading": "Mengapa Ibu merasa sangat bahagia menerima kartu mawar Melati?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Mother kneeling down hugging Melati tightly against her chest, holding the rose-petal card in one hand. Warm sunlight streaming through the kitchen window, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Kartu Mawar di Meja Rias",
                    "titleEn": "The Rose Card on the Vanity Table",
                    "textId": "Malam itu kartu kolase kelopak mawar diletakkan di samping cermin meja rias Ibu, menebarkan wangi mawar ke seluruh kamar tidur. Di kamarnya, Melati tidur lelap dipeluk selimut ungu hangatnya, bermimpi tentang padang mawar pelangi yang tak pernah layu.",
                    "textEn": "That night, the rose petal card stood beside the mirror on Mother's vanity table, wafting sweet rose fragrance through the bedroom. In her own room, Melati slept deeply tucked under her warm purple quilt, dreaming of rainbow rose meadows that would never fade.",
                    "quote": "Tidurlah dalam keharuman cinta, kebaikan hatimu mekar abadi di hati ibumu.",
                    "coReading": "Mari pejamkan mata dan rasakan pelukan hangat ibumu sebelum tidur.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Melati sleeping serenely in bed with a gentle smile. In the adjoining room visible through the door, the rose card glows on a wooden vanity table under soft moonlight. Starry sky outside window, serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 86: Kayuhan Sepeda Roda Dua Pertama ---
        {
            "id": "story86",
            "storyNumber": 86,
            "title": "Kayuhan Sepeda Roda Dua Pertama",
            "englishTitle": "First Two-Wheeled Bicycle Pedals",
            "category": "perseverance",
            "categoryLabel": "🐢 Ketekunan & Rasa Percaya Diri",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kemandirian, keseimbangan diri, & rasa percaya pada proses",
            "cover": "covers/story86_cover.jpg",
            "synopsis": "Hari ini roda bantu kecil di sepeda Bima dilepas oleh Ayah. Dengan helm oranye dan pelindung lutut, Bima sempat merasa goyah dan takut jatuh. Dengan bimbingan sabar Ayah yang memegangi sadel, Bima akhirnya menemukan keseimbangan dan meluncur bebas di jalan taman berumput.",
            "protagonist": "Bima (Anak laki-laki berhelm pelindung oranye)",
            "companion": "Ayah Bima (Ayah memegang sadel sepeda dengan sabar)",
            "setting": "Jalanan Taman Berumput",
            "pages": [
                {
                    "number": 1,
                    "title": "Pelepasan Roda Bantu Kecil",
                    "titleEn": "Removing the Little Training Wheels",
                    "textId": "Di jalan setapak taman desa yang berumput hijau, Ayah menggunakan kunci inggris untuk membuka baut dua roda bantu kecil di sepeda biru Bima. 'Kring!' roda-roda kecil itu terlepas. Kini sepeda biru Bima berdiri hanya dengan dua roda yang ramping.",
                    "textEn": "On the grassy village park trail, Dad used an adjustable wrench to unfasten the two little training wheels from Bima's blue bicycle. 'Clink!' the small wheels came off. Now Bima's blue bicycle stood on just two slender tires.",
                    "quote": "Setiap langkah kemandirian baru dimulai dari keberanian melepas pegangan lama.",
                    "coReading": "Pernahkah kamu belajar naik sepeda roda dua?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Bima, an energetic boy in an orange safety helmet, knee pads, and red t-shirt, watching Dad unbolt the training wheels of a blue bicycle on a grassy park path. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Rasa Goyah di Sadel Sepeda",
                    "titleEn": "A Wobbly Feeling on the Saddle",
                    "textId": "Bima menaiki sadel dan memegang stang erat-erat. Tanpa roda bantu, sepeda itu terasa bergoyang ke kiri dan ke kanan seperti perahu di atas ombak. Jantung Bima berdegup kencang dan kakinya ragu-ragu menginjak pedal.",
                    "textEn": "Bima climbed onto the saddle and gripped the handlebars tight. Without training wheels, the bike tilted left and right like a dinghy on sea swells. Bima's heart thudded and his sneakers hesitated on the pedals.",
                    "quote": "Rasa cemas adalah hal yang wajar ketika kita menghadapi hal yang baru.",
                    "coReading": "Bagaimana perasaanmu saat pertama kali duduk di atas sepeda tanpa roda bantu?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Bima sitting nervously on the two-wheel bicycle with feet hovering near the ground, handlebars wobbling slightly. Dad standing right behind him smiling with steady posture, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Tangan Ayah yang Menopang Sadel",
                    "titleEn": "Dad's Hand Supporting the Saddle",
                    "textId": "Ayah memegang bagian belakang sadel sepeda Bima dengan kedua tangannya yang kokoh. 'Jangan khawatir, Bima. Ayah memegangimu rapat-rapat. Tataplah lurus ke depan, ke arah pohon rindang di ujung jalan, dan mulailah mengayuh pelan-pelan.'",
                    "textEn": "Dad gripped the back of Bima's bicycle saddle with both strong hands. 'Do not worry, Bima. Dad is holding you steady. Look straight ahead toward the big shady tree at the path's end, and begin pedaling gently.'",
                    "quote": "Dukungan penuh cinta memberi rasa aman untuk melangkah maju.",
                    "coReading": "Ke mana Bima harus mengarahkan pandangannya saat bersepeda?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Dad jogging gently behind the bicycle, holding the back of the saddle with both hands. Bima looking ahead with focused determination, green park path, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Kayuhan Pertama yang Berat",
                    "titleEn": "The Heavy First Pedals",
                    "textId": "Bima menekan pedal kanan ke bawah: 'Gowes!' Rantai sepeda berdesir pelan. Sepeda meluncur maju selangkah. Bima menyusul dengan pedal kiri. Dengan bantuan dorongan tangan Ayah, sepeda bergerak maju membelah angin semilir pagi.",
                    "textEn": "Bima pushed the right pedal down: 'Push!' The bike chain hummed softly. The bicycle rolled one pace forward. Bima followed with the left pedal. With Dad's supportive guidance, the bicycle moved ahead parting the gentle morning breeze.",
                    "quote": "Langkah pertama selalu terasa paling berat, namun membuka jalan menuju kebebasan.",
                    "coReading": "Bisakah kamu menirukan gerakan mengayuh pedal dengan kakimu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Bima pedaling with concentration, sneakers pushing pedals, wheels rolling along a smooth asphalt park path bordered by wildflower grass. Dad jogging alongside, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Mencari Titik Keseimbangan",
                    "titleEn": "Finding the Point of Balance",
                    "textId": "'Jangan kaku, Bima. Ikuti irama gerakan sepedamu seperti menari,' bisik Ayah sambil berlari kecil di sampingnya. Bima mengendurkan genggaman tangannya yang tegang. Tiba-tiba ia merasakan sesuatu yang ajaib: sepeda itu seolah berdiri tegak dengan sendirinya!",
                    "textEn": "'Do not be stiff, Bima. Follow the bike's motion just like dancing,' Dad whispered, jogging lightly beside him. Bima relaxed his tense grip on the bars. Suddenly he felt something magical: the bike seemed to stand upright all on its own!",
                    "quote": "Keseimbangan sejati lahir saat kita berhenti melawan dan mulai mengalir bersama keadaan.",
                    "coReading": "Apa yang dirasakan Bima saat tangannya tidak lagi tegang?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Bima riding smoothly with balanced posture, a bright smile appearing on his face beneath the orange helmet. Dad smiling proudly as he eases his grip, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Lepasan Tangan yang Halus",
                    "titleEn": "The Gentle Letting Go",
                    "textId": "Tanpa disadari Bima, Ayah perlahan melepaskan pegangan tangannya dari sadel. Ayah membiarkan Bima meluncur sendiri. Sepeda biru itu melaju lurus dan tenang, membelah bayangan dedaunan di atas jalan taman.",
                    "textEn": "Without Bima noticing, Dad gently loosened his grip from the saddle, stepping back. He let Bima glide forward on his own. The blue bicycle rolled straight and steady, cruising through dappled tree shadows across the park lane.",
                    "quote": "Melepaskan pada saat yang tepat adalah wujud tertinggi dari kepercayaan.",
                    "coReading": "Apakah Bima tahu bahwa Ayah sudah melepaskan pegangannya?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Bima riding forward independently down the sunlit park trail, while Dad stands a few paces behind clapping with proud joy. Naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Sorak Bangga dari Kejauhan",
                    "titleEn": "Proud Cheers from Behind",
                    "textId": "'Hebat, Bima! Kamu bersepeda sendiri!' seru Ayah dari kejauhan. Bima menoleh sedikit dan terkejut melihat Ayah sudah tertinggal lima langkah di belakang. Menyadari dirinya terbang sendiri, Bima tertawa gembira: 'Ayah, aku bisa! Aku terbang!'",
                    "textEn": "'Wonderful, Bima! You are riding all by yourself!' Dad cheered from behind. Bima glanced back and gasped to see Dad five paces behind. Realizing he was flying on his own, Bima burst into laughter: 'Dad, I did it! I am flying!'",
                    "quote": "Kemenangan terbesar adalah ketika kita membuktikan bahwa kita mampu.",
                    "coReading": "Apa yang dikatakan Bima saat menyadari ia mengayuh sepeda sendiri?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Bima pedaling with wide open smile, wind blowing through his clothes, looking back briefly with triumphant joy. Park trees and blooming shrubs on both sides, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Rem Lembut di Bawah Pohon Beringin",
                    "titleEn": "Gentle Brakes Under the Banyan Tree",
                    "textId": "Mendekati pohon rindang, Bima menarik tuas rem karet di stangnya perlahan: 'Sssht!' Sepeda melambat dengan mulus dan Bima menurunkan kaki kanannya menjejak rumput tebal. Bima berhenti dengan sempurna tanpa terjatuh sama sekali.",
                    "textEn": "Approaching the shady tree, Bima gently squeezed the brake levers on the handlebars: 'Ssshh!' The bicycle slowed smoothly and Bima rested his right sneaker on the thick grass. He came to a perfect stop without falling at all.",
                    "quote": "Tahu cara berhenti dengan aman melengkapi keterampilan mengemudi.",
                    "coReading": "Bagaimana cara Bima menghentikan sepedanya dengan aman?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Bima successfully stopped under a leafy banyan tree, one foot planted firmly on green grass, one hand raised high in a victory fist. Orange helmet glowing, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Pelukan Hangat Ayah",
                    "titleEn": "Dad's Warm Embrace",
                    "textId": "Ayah berlari menghampiri Bima dan mengangkat putranya tinggi-tinggi ke udara. 'Ayah sangat bangga padamu, Bima. Hari ini kamu membuktikan bahwa dengan ketekunan, kamu bisa mengalahkan rasa takut.' Bima memeluk leher Ayah dengan hati yang mekar bahagia.",
                    "textEn": "Dad dashed over, scooping his son high into the air. 'I am so proud of you, Bima. Today you proved that with patience, you can conquer any fear.' Bima wrapped his arms around Dad's neck, his heart blooming with pure joy.",
                    "quote": "Kebanggaan orang tua adalah hadiah paling berharga bagi perjuangan seorang anak.",
                    "coReading": "Mengapa Ayah mengangkat Bima tinggi-tinggi ke udara?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Dad lifting Bima high in the air in a triumphant celebratory embrace in the sunny park. Blue bicycle resting on kickstand nearby, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Mengayuh Menembus Awan",
                    "titleEn": "Dreams of Pedaling Through the Clouds",
                    "textId": "Malam itu kaki Bima terasa pegal namun hatinya sangat ringan dan damai. Sepeda birunya terparkir rapi di samping pintu garasi. Bima tidur pulas di bawah selimut hangatnya, bermimpi mengayuh sepedanya melintasi jembatan pelangi di langit malam bertabur bintang.",
                    "textEn": "That night Bima's legs felt pleasantly tired, but his heart was light and serene. His blue bicycle was parked neatly beside the garage door. Bima slept soundly beneath his warm blanket, dreaming of pedaling his bike across rainbow bridges through starlit skies.",
                    "quote": "Tidurlah dalam kebanggaan yang manis, esok dunia baru siap kau jelajahi.",
                    "coReading": "Mari pejamkan mata dan rasakan semilir angin yang menerpa wajahmu saat bersepeda.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Bima sleeping peacefully in bed with a bicycle poster on the wall and his orange helmet sitting proudly on the nightstand. Moonbeams streaming through the window, crescent moon outside. Serene bedtime atmosphere, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 87: Simpul Telinga Kelinci Tali Sepatu ---
        {
            "id": "story87",
            "storyNumber": 87,
            "title": "Simpul Telinga Kelinci Tali Sepatu",
            "englishTitle": "Bunny Ears Shoelace Knot",
            "category": "perseverance",
            "categoryLabel": "🐢 Ketekunan & Rasa Percaya Diri",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kemandirian merawat diri, ketelitian simpul, & kesabaran belajar",
            "cover": "covers/story87_cover.jpg",
            "synopsis": "Tari selalu kesulitan mengikat tali sepatu kanvas merahnya; tali itu sering terlepas dan membuatnya tersandung. Nenek mengajari Tari jurus dongeng 'Dua Telinga Kelinci yang Saling Berpelukan'. Dengan ketelatenan dan senyuman, Tari akhirnya bisa mengikat sepatunya sendiri dengan kuat dan rapi.",
            "protagonist": "Tari (Gadis cilik bersepatu kanvas merah)",
            "companion": "Kucing Tari (Kucing memperhatikan ujung tali sepatu)",
            "setting": "Undakan Teras Rumah",
            "pages": [
                {
                    "number": 1,
                    "title": "Sepatu Kanvas Merah Berbintik Putih",
                    "titleEn": "Red Canvas Shoes with White Polka Dots",
                    "textId": "Di undakan teras rumah berpapan jati, Tari duduk mengenakan sepatu kanvas merah barunya. Sepatu itu sangat cantik dengan tali putih panjang yang menjuntai di lantai. Namun setiap kali Tari mencoba mengikatnya, tali itu selalu lepas menjadi simpul kusut yang rumit.",
                    "textEn": "On the teakwood steps of the porch, Tari sat wearing her brand-new red canvas sneakers. The shoes were lovely with long white laces trailing on the floor. But every time Tari tried to tie them, the laces slipped into a frustrating, tangled knot.",
                    "quote": "Kemandirian belajar hal baru membutuhkan waktu dan kesabaran yang lapang.",
                    "coReading": "Apakah sepatumu memakai tali atau perekat velkro?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Tari, a cute young girl in overalls and a knit sweater, sitting on wooden porch steps looking down at her untied red canvas sneakers. White pet kitten sitting beside her watching the laces, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Kucing Usil dan Ujung Tali",
                    "titleEn": "The Playful Kitten and the Lace Ends",
                    "textId": "Mimi, anak kucing belang tiga milik Tari, mengira ujung tali sepatu itu adalah ekor tikus putih yang bergerak. Mimi menepuk-nepuk tali itu dengan cakar berbulunya sambil berguling-guling lucu. Tari menghela napas cemberut, 'Tali sepatu ini membingungkan sekali, Mimi!'",
                    "textEn": "Mimi, Tari's calico kitten, thought the lace tips were twitching white mouse tails. Mimi batted playfully at the aglets with soft furry paws, rolling on her back. Tari sighed with a pouting frown, 'These shoelaces are so confusing, Mimi!'",
                    "quote": "Bila merasa bingung, berhentilah sejenak dan tersenyumlah melihat sekeliling.",
                    "coReading": "Mengapa anak kucing suka bermain dengan tali sepatu?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Mimi the cute calico kitten playfully swatting at the white shoelace dangling from Tari's red sneaker. Tari sitting on the steps with cheek resting in hand, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Dongeng Rahasia Nenek",
                    "titleEn": "Grandma's Secret Tale",
                    "textId": "Nenek melangkah keluar membawa sepiring pisang goreng hangat. Nenek berjongkok di samping Tari dan tersenyum ramah. 'Tali sepatu itu tidak membingungkan jika kau tahu rahasianya, Tari. Ada dongeng tentang dua ekor kelinci di dalam setiap simpul sepatu.'",
                    "textEn": "Grandma stepped outside carrying a plate of warm fried bananas. She knelt beside Tari, smiling warmly. 'Shoelaces are not confusing once you learn their secret, Tari. There is a fairy tale about two little bunnies inside every shoe knot.'",
                    "quote": "Cerita yang indah membuat pelajaran sulit menjadi mudah dipahami.",
                    "coReading": "Dongeng tentang hewan apa yang akan diceritakan Nenek?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Kind grandmother kneeling beside Tari on the porch steps, pointing gently at the shoe laces. Sunny porch garden in background, warm family moment, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Langkah Pertama: Menyilangkan Batang Pohon",
                    "titleEn": "Step One: Crossing the Tree Trunks",
                    "textId": "Nenek memegang kedua ujung tali putih. 'Langkah pertama: silangkan kedua tali membentuk huruf X, seperti dua pohon yang bersandar. Lalu selipkan satu tali ke kolong bawah dan tarik kencang: sreeet!' Di atas lidah sepatu terbentuk dasar simpul yang kokoh.",
                    "textEn": "Grandma held both white lace ends. 'Step one: cross both laces into an X, like two trees leaning together. Then tuck one lace through the tunnel underneath and pull tight: swish!' At the base of the shoe tongue sat a firm starting knot.",
                    "quote": "Setiap simpul kuat bertumpu pada fondasi pertama yang rapi.",
                    "coReading": "Bisakah kamu membuat huruf X dengan dua helai tali?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Close-up of Grandma's hands showing Tari how to cross the white laces into an X and pull the first overhand knot snug against the red shoe tongue. Simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Membentuk Dua Telinga Kelinci",
                    "titleEn": "Forming Two Bunny Ears",
                    "textId": "'Sekarang bagian ajaibnya,' bisik Nenek. Nenek melipat masing-masing tali menjadi dua lengkungan bulat yang berdiri tegak. 'Lihat, ini Telinga Kelinci Kiri dan ini Telinga Kelinci Kanan! Lucu sekali kan bentuknya?' Tari mengangguk kagum.",
                    "textEn": "'Now comes the magic part,' whispered Grandma. She folded each lace into two upright rounded loops. 'Look, here is the Left Bunny Ear and here is the Right Bunny Ear! Aren't they adorable?' Tari nodded in delight.",
                    "quote": "Menghubungkan tugas dengan gambar imajinasi mempermudah ingatan kita.",
                    "coReading": "Berapa banyak telinga kelinci yang dibuat dari tali sepatu itu?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Grandma holding up two neat loops of white shoelaces that look exactly like upright bunny ears above the red sneaker. Tari watching with wide fascinated eyes, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Dua Kelinci Saling Berpelukan",
                    "titleEn": "Two Bunnies Hugging Each Other",
                    "textId": "'Kelinci Kiri dan Kelinci Kanan adalah sahabat karib,' lanjut Nenek. 'Mereka saling bersilang, lalu Kelinci Kiri menyusup masuk ke dalam lubang pelukan di bawahnya. Tarik kedua telinga ke kiri dan ke kanan: zzzp!' Terbentuklah pita kupu-kupu yang sangat rapi dan manis.",
                    "textEn": "'Left Bunny and Right Bunny are best pals,' Grandma continued. 'They cross each other, and Left Bunny ducks into the hug-hole underneath. Now pull both ears left and right: snap!' There formed a sweet, perfectly neat butterfly bow.",
                    "quote": "Pelukan yang erat menjaga ikatan persahabatan tidak mudah terlepas.",
                    "coReading": "Bagaimana dua telinga kelinci itu membuat ikatan simpul?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. The completed shoelace bow forming two neat rounded loops like bunny ears tied firmly on the red sneaker. Mimi the kitten sniffing the tidy knot, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Giliran Jemari Tari Mempraktikkan",
                    "titleEn": "Tari's Fingers Try It Out",
                    "textId": "Kini giliran sepatu sebelah kiri. Tari menarik napas dalam-dalam. Ia menyilangkan tali membentuk huruf X, menyelipkannya ke kolong, lalu membuat dua telinga kelinci mungil. Jemari kecilnya bekerja pelan-pelan penuh kehati-hatian.",
                    "textEn": "Now came the turn of the left shoe. Tari took a deep breath. She crossed the laces into an X, tucked under the tunnel, then shaped two cute bunny loops. Her little fingers moved slowly with patient care.",
                    "quote": "Keberhasilan datang dari ketelatenan mencoba dengan tangan sendiri.",
                    "coReading": "Apakah Tari ingat urutan cerita dongeng kelinci Nenek?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Tari concentrating intently on tying the laces of her left red sneaker on the porch step. Tongue peeking out in sweet focus, Grandma watching encouragingly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Tarik Kencang: Simpul Berhasil!",
                    "titleEn": "Pull Tight: The Knot is Tied!",
                    "textId": "Tari menyelipkan satu telinga kelinci ke lubang bawah, memegang kedua ujung lengkungan, lalu menariknya ke samping: 'Sreeet!' Simpul pita kelinci itu mengunci erat dan indah. Tidak kusut, tidak longgar. Tari melompat berdiri: 'Nenek, aku bisa! Aku berhasil mengikatnya sendiri!'",
                    "textEn": "Tari slipped one bunny ear through the hole beneath, gripped both loops, and pulled outward: 'Swiiish!' The bunny bow snapped snug and beautiful. Not tangled, not loose. Tari sprang to her feet: 'Grandma, I did it! I tied it all by myself!'",
                    "quote": "Rasa bangga saat bisa mandiri adalah hadiah terindah dari kesabaran.",
                    "coReading": "Bagaimana perasaan Tari setelah berhasil mengikat sepatunya sendiri?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Tari jumping up on the porch steps with hands raised in triumph, displaying both neatly tied red canvas shoes. Grandma clapping happily, Mimi the kitten purring by her feet, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Lari Ringan Mengelilingi Pekarangan",
                    "titleEn": "A Light Jog Around the Yard",
                    "textId": "Tari berlari melintasi halaman rumput mengitari pohon mangga dan pot-pot bunga. Simpul tali sepatunya tetap terikat kokoh tanpa terlepas sedikit pun. Langkah kakinya terasa begitu ringan dan penuh rasa percaya diri.",
                    "textEn": "Tari jogged across the grassy yard around the mango tree and flower pots. Her shoelace knots stayed tight and firm, not loosening in the least. Her footsteps felt so light and brimming with newfound confidence.",
                    "quote": "Kemandirian memberi sayap pada setiap langkah anak yang sedang bertumbuh.",
                    "coReading": "Apakah tali sepatu Tari lepas saat ia berlari?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Tari running happily across the green lawn in her red sneakers, red shoes kicking up merrily, pigtails swinging. Golden afternoon sunlight, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Sepatu Rapi di Bawah Ranjang",
                    "titleEn": "Tidy Shoes Beneath the Bed",
                    "textId": "Malam tiba dan sepatu kanvas merah tersimpan rapi berjejer di bawah ranjang kamar tidur Tari. Di atas kasur empuknya, Tari tidur pulas berselimut kain perca, dengan Mimi si anak kucing melingkar di samping kakinya. Di dalam mimpi manisnya, dua kelinci putih sahabat simpul sepatunya menemaninya bermain di padang pelangi.",
                    "textEn": "Night fell and the red canvas sneakers rested neatly paired beneath Tari's bedroom bed. On her plush mattress, Tari slept deeply wrapped in a patchwork quilt, with Mimi the kitten curled by her feet. In sweet dreams, the two white knot-bunnies played with her in rainbow meadows.",
                    "quote": "Tidurlah dalam rasa damai, setiap hari baru membawamu tumbuh semakin mandiri.",
                    "coReading": "Mari pejamkan mata dan bayangkan dua kelinci lucu menjaga tidur lelapmu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Tari sleeping peacefully in bed with a quilt, kitten curled at her feet. Red canvas shoes neatly parked under the bed on polished wood floor. Soft moonlight and twinkling stars outside window, serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
