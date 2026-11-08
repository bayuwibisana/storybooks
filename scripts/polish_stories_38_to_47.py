# scripts/polish_stories_38_to_47.py
import json

def get_stories_38_to_47():
    stories = []

    # =========================================================================
    # STORY 38: Pohon Brokoli Mini Ajaib
    # =========================================================================
    s38 = {
        "id": "pohon-brokoli-mini",
        "storyNumber": 38,
        "title": "Pohon Brokoli Mini Ajaib",
        "englishTitle": "The Magic Little Broccoli Tree",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 3–6 Tahun",
        "moralTheme": "Memberanikan diri mencicipi sayuran hijau pertama kali lewat imajinasi menyenangkan",
        "cover": "images/story38_cover.jpg",
        "coverImage": "images/story38_cover.jpg",
        "synopsis": "Rian tidak menyukai sayuran hijau di mangkuknya. Bersama Mama dan topi koki kecilnya, Rian menjelajahi 'Hutan Brokoli Ajaib' di atas piring dan menemukan bahwa sayuran hijau terasa renyah manis seperti pohon kurcaci mentega.",
        "synopsisEn": "Little Rian avoids the green vegetables on his plate. With Mama and his paper chef hat, Rian explores a magical 'Broccoli Forest' on his dinner plate, discovering that green florets are crunchy, buttery, and surprisingly delicious.",
        "protagonist": "Rian (Anak laki-laki 4 tahun bertopi koki kertas putih)",
        "companion": "Mama Rian (Ibu penyayang bercelemek bunga matahari)",
        "setting": "Meja Makan Berlampu Hangat & Hutan Sayur Imajinasi",
        "pages": [
            {
                "number": 1,
                "title": "Mangkuk Keramik dan Sayuran Hijau",
                "titleEn": "The Ceramic Bowl and Green Vegetables",
                "textId": "Malam itu, di meja makan keluarga yang hangat, sepiring sup hangat mengepul lembut. Namun, dahi Rian berkerut. Di samping kentang panggang keemasannya, ada tiga kuntum brokoli hijau tua yang tampak begitu asing dan mencurigakan.",
                "textEn": "That evening, warm soup steamed gently upon the cozy family table. But little Rian's brow furrowed. Resting next to his golden baked potatoes were three deep-green broccoli florets, looking entirely unfamiliar and suspicious.",
                "quote": "🥦 'Sesuatu yang belum pernah kita coba memang selalu terasa sedikit menakutkan.'",
                "coReading": "💡 Tanya si Kecil: Sayuran apa yang warnanya paling hijau di mejamu?",
                "imagePrompt": "A charming children's book illustration of toddler boy Rian in a striped yellow pyjama and small paper chef hat sitting at a wooden dining table, looking dubiously at a bowl with small steamed broccoli florets. Soft warm lantern glow, naive folk-art style, handcrafted wax crayon and oil pastel smudges on textured cream paper, simple black dot bead eyes, 4:3 landscape, completely text-free."
            },
            {
                "number": 2,
                "title": "Topi Koki Rahasia Mama",
                "titleEn": "Mama's Secret Chef Hat",
                "textId": "Mama tersenyum lembut lalu memakaikan topi koki kertas di kepala Rian. \"Tahukah kamu, Koki Rian? Piring ini bukan sekadar piring biasa. Ini adalah Lembah Rahasia tempat tumbuhnya pohon-pohon mini para peri kurcaci!\"",
                "textEn": "Mama smiled gently and adjusted the paper chef hat upon Rian's head. \"Did you know, Chef Rian? This dinner plate isn't just an ordinary plate. It's a Secret Valley where miniature trees of the forest gnomes grow!\"",
                "quote": "👩 'Imajinasi yang ceria bisa mengubah makan malam biasa menjadi petualangan ajaib.'",
                "coReading": "💡 Aktivitas Seru: Pasang mahkota atau topi imajinasi di kepala si kecil sebelum makan malam!",
                "imagePrompt": "A heartwarming storybook scene of Mama wearing a floral apron gently placing a cute folded paper chef hat on Rian's head. On the plate, the broccoli florets look like miniature mossy bonsai trees. Cozy kitchen setting, honey-amber lighting, waxy crayon texture, soft watercolor paper grain, 4:3 landscape, completely text-free."
            },
            {
                "number": 3,
                "title": "Pohon Rindang Para Kurcaci",
                "titleEn": "The Little Gnome's Shade Tree",
                "textId": "Rian mendekatkan wajahnya. Benar saja! Tangkai brokoli itu kokoh seperti batang pohon oak mini, dan daun-daun kecilnya bergumpal rimbun seperti awan hijau zamrud. Aroma mentega gurih mulai menyapa hidungnya.",
                "textEn": "Rian leaned in close. Sure enough! The broccoli stem stood firm like a tiny oak trunk, and its lush crown curled softly like an emerald cloud. A gentle buttery aroma wafted up to greet his nose.",
                "quote": "🌳 'Saat kita mengamati lebih dekat, alam menyimpan bentuk-bentuk yang begitu menakjubkan.'",
                "coReading": "💡 Tanya si Kecil: Mirip pohon apa sayuran brokoli menurut matamu?",
                "imagePrompt": "Whimsical children's picture book close-up of a steaming little broccoli tree sitting on a rustic ceramic plate, surrounded by tiny mashed potato hills. Rian inspects it with wide, curious black bead eyes. Handcrafted wax crayon scribbles, chalky pastel textures, warm bedtime tones, 4:3 landscape, completely text-free."
            },
            {
                "number": 4,
                "title": "Salju Keju Parmesan",
                "titleEn": "The Parmesan Cheese Snowfall",
                "textId": "Mama mengambil mangkuk kecil lalu menaburkan parutan keju tipis. Gerimis butiran putih jatuh perlahan di atas dahan-dahan brokoli. \"Lihat, salju keju gurih baru saja turun di hutan kurcacimu!\" bisik Mama ceria.",
                "textEn": "Mama picked up a tiny ceramic bowl and sprinkled finely grated cheese. A gentle dusting of white fell softly over the broccoli branches. \"Look, savory cheese snow has just fallen upon your gnome forest!\" whispered Mama merrily.",
                "quote": "🧀 'Sedikit keju dan sentuhan kasih membuat segalanya terasa lebih lezat.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu membayangkan keju parut sebagai salju di piring makanmu?",
                "imagePrompt": "Charming illustration of Mama's hands gently grating golden parmesan cheese over the broccoli floret like tiny snowflakes falling on a miniature winter pine. Warm kitchen glow, soft oil pastel blending, tactile crayon marks on heavy paper, 4:3 landscape, completely text-free."
            },
            {
                "number": 5,
                "title": "Gigitan Pertama yang Ragu",
                "titleEn": "The Hesitant First Nibble",
                "textId": "Dengan garpu kecilnya, Rian menusuk satu dahan pohon brokoli bersalju itu. Tangannya sempat ragu di depan bibir. Tetapi melihat senyum Mama yang menenangkan, Rian menutup matanya dan menggigit ujung daun kecilnya.",
                "textEn": "With his little fork, Rian speared one snowy branch of the broccoli tree. His hand hesitated right in front of his lips. But seeing Mama's reassuring smile, Rian closed his eyes and took the tiniest nibble.",
                "quote": "🌟 'Keberanian dimulai dari satu langkah kecil yang berani mencoba.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana caramu mengumpulkan keberanian sebelum mencicipi makanan baru?",
                "imagePrompt": "Heartwarming bedtime story illustration of toddler Rian holding a fork with a small broccoli tree up to his mouth, eyes squeezed shut in brave anticipation. Mama smiles warmly beside him. Soft crayon strokes, naive folk art, cozy kitchen lamplight, 4:3 landscape, completely text-free."
            },
            {
                "number": 6,
                "title": "Kriuk Manis di Ujung Lidah",
                "titleEn": "A Sweet Crunch on the Tongue",
                "textId": "KRIUK! Bunyi renyah yang merdu terdengar di mulut Rian. Tidak ada rasa pahit seperti yang ia takuti. Yang ada hanyalah rasa gurih mentega, gurih keju, dan manis segar sayuran hijau yang renyah.",
                "textEn": "CRUNCH! A delightful crisp sound echoed in Rian's mouth. There was no bitter taste as he had feared. Instead, there was rich butter, savory cheese, and the fresh, naturally sweet crunch of garden greens.",
                "quote": "😋 'Kadang ketakutan kita jauh lebih besar daripada rasa aslinya.'",
                "coReading": "💡 Aktivitas Seru: Tirukan bersama suara 'Kriuk-kriuk' saat mengunyah sayuran renyah!",
                "imagePrompt": "Joyful children's illustration of toddler Rian chewing happily with round cheeks and wide sparkling bead eyes, pleasantly surprised by the taste. Little sparkles and music notes float in the air. Wax crayon and soft oil pastel textures, warm terracotta and butter yellow tones, 4:3 landscape, completely text-free."
            },
            {
                "number": 7,
                "title": "Piring Bersih Sang Koki Cilik",
                "titleEn": "The Little Chef's Empty Plate",
                "textId": "\"Nyam-nyam!\" Rian melahap dahan kedua dan ketiga sampai habis tak bersisa. Piring keramiknya kini bersih berkilau. Rian menepuk perut kecilnya yang kenyang dengan bangga.",
                "textEn": "\"Yum-yum!\" Rian munched through the second and third little trees until nothing was left. His ceramic plate was now squeaky clean. Rian patted his satisfied tummy with great pride.",
                "quote": "🍽️ 'Menghabiskan makanan sehat adalah hadiah terbaik untuk tubuh kita sendiri.'",
                "coReading": "💡 Tanya si Kecil: Bagaimana rasanya jika piring makanmu bisa bersih dan habis dimakan?",
                "imagePrompt": "Charming illustration of Rian holding up his clean ceramic plate with a big triumphant grin, wearing his paper chef hat tilted jauntily. Mama claps with joy. Handcrafted wax crayon scribbles, deckle edge watercolor paper texture, 4:3 landscape, completely text-free."
            },
            {
                "number": 8,
                "title": "Segelas Susu Hangat dan Pelukan",
                "titleEn": "A Glass of Warm Milk and a Hug",
                "textId": "Mama menuangkan segelas susu putih hangat untuk menutup petualangan makan malam. Sambil memeluk Rian erat, Mama berbisik, \"Mama sangat bangga padamu. Hari ini kamu membuktikan bahwa kamu anak yang berani.\"",
                "textEn": "Mama poured a small cup of warm white milk to conclude their dinner adventure. Hugging Rian tightly, Mama whispered, \"I am so very proud of you. Today you proved what a brave little boy you are.\"",
                "quote": "🥛 'Pelukan hangat ibu adalah penutup paling manis setelah petualangan yang hebat.'",
                "coReading": "💡 Peluk si Kecil: Berikan pelukan hangat dan katakan kamu bangga atas keberaniannya hari ini.",
                "imagePrompt": "Tender children's book illustration of Mama hugging toddler Rian at the dining table, with a small mug of steaming milk resting nearby. Soft golden ambient light, cozy home atmosphere, crayon texture on cream paper, 4:3 landscape, completely text-free."
            },
            {
                "number": 9,
                "title": "Sikat Gigi Sebelum Masuk Selimut",
                "titleEn": "Brushing Teeth Before Bedtime",
                "textId": "Di cermin wastafel kamar mandi, Rian menyikat giginya dengan riang. Busa putih membersihkan sisa-sisa petualangan hutan brokoli. Giginya putih berkilau, siap mengantarnya ke peraduan malam.",
                "textEn": "In the bathroom sink mirror, Rian brushed his teeth merrily. Soft white lather cleaned away every trace of the broccoli forest adventure. His teeth gleamed bright, ready to carry him off to slumber.",
                "quote": "🪥 'Gigi yang bersih membuat tidur malam terasa begitu nyaman dan segar.'",
                "coReading": "💡 Tanya si Kecil: Sudahkah kamu menyikat gigimu malam ini sebelum naik ke ranjang?",
                "imagePrompt": "Cute illustration of toddler boy Rian standing on a wooden step stool at the bathroom sink, enthusiastically brushing his teeth with foamy white bubbles. Warm soft lamplight, naive storybook style, textured paper, 4:3 landscape, completely text-free."
            },
            {
                "number": 10,
                "title": "Mimpi Hutan Kurcaci Hijau",
                "titleEn": "Dreams of the Green Gnome Forest",
                "textId": "Lampu kamar meredup. Di balik selimut kotak-kotak biru, Rian memeluk bantalnya. Dalam tidurnya yang pulas, ia bermimpi terbang bersama kupu-kupu di atas kanopi hutan brokoli mini yang ramah. Selamat malam, Koki Cilik.",
                "textEn": "The bedroom lamp dimmed soft and low. Tucked under his blue plaid quilt, Rian hugged his pillow tight. In peaceful slumber, he dreamed of flying with butterflies over the friendly canopy of mini broccoli trees. Goodnight, brave little Chef.",
                "quote": "🌙 'Anak yang berani mencoba hal baru akan dihadiahi mimpi-mimpi yang paling indah.'",
                "coReading": "💡 Bisikkan ke si Kecil: Selamat tidur anak hebat, besok ada petualangan baru yang lezat menunggumu.",
                "imagePrompt": "A tranquil bedtime illustration of toddler Rian sleeping deeply in his cozy wooden bed under a blue plaid blanket, a faint dream bubble above showing friendly little green broccoli trees and yellow butterflies. Crescent moon outside the window, soft wax crayon and oil pastel, 4:3 landscape, completely text-free."
            }
        ]
    }
    stories.append(s38)

    # =========================================================================
    # STORY 39: Jembatan Bambu Goyang
    # =========================================================================
    s39 = {
        "id": "jembatan-bambu-goyang",
        "storyNumber": 39,
        "title": "Jembatan Bambu Goyang",
        "englishTitle": "The Wobbly Bamboo Bridge",
        "category": "petualangan",
        "categoryLabel": "⛵ Petualangan & Keberanian",
        "ageGroup": "Usia 4–7 Tahun",
        "moralTheme": "Belajar percaya diri, tenang, dan melangkah hati-hati bersama teman",
        "cover": "images/story39_cover.jpg",
        "coverImage": "images/story39_cover.jpg",
        "synopsis": "Tegar merasa lututnya gemetar saat harus melintasi jembatan gantung bambu di atas sungai berbatu. Bersama Bono si monyet kecil penunjuk jalan, Tegar belajar bernapas tenang, menatap lurus ke depan, dan menemukan keberanian di setiap ayunan langkahnya.",
        "synopsisEn": "Little Tegar's knees tremble as he faces a swaying bamboo suspension bridge over a rocky river. With Bono the agile little monkey as his guide, Tegar learns to breathe calm, keep his eyes ahead, and discover courage in every careful step.",
        "protagonist": "Tegar (Anak desa berkulit sawo matang bersandal jepit merah)",
        "companion": "Bono (Monyet kecil lincah bertopi caping mini)",
        "setting": "Jurang Sungai Berbatu & Hutan Bambu Berdesir",
        "pages": [
            {
                "number": 1,
                "title": "Gemercik Air di Bawah Jurang",
                "titleEn": "The Rushing Water Down Below",
                "textId": "Di tepi jurang Hutan Bambu, angin bertiup kencang membuat daun-daun berbisik. Di bawah sana, air sungai yang jernih mengalir deras membentur batu-batu kali yang hitam dan licin. Tegar menelan ludah pelan.",
                "textEn": "At the edge of the Bamboo Forest gorge, a brisk breeze made the green leaves rustle and whisper. Far down below, clear river water rushed forcefully against shiny black river stones. Tegar swallowed hard.",
                "quote": "🌊 'Suara derasnya sungai kadang membuat hati kecil kita berdegup lebih kencang.'",
                "coReading": "💡 Tanya si Kecil: Pernahkah kamu melihat sungai yang airnya mengalir sangat cepat?",
                "imagePrompt": "Charming children's book illustration of village boy Tegar standing nervously on a grassy cliffside overlooking a rocky river below, next to a tall bamboo forest. Handcrafted wax crayon and oil pastel style, textured cream watercolor paper, naive folk-art charm, simple bead eyes, 4:3 landscape, completely text-free."
            },
            {
                "number": 2,
                "title": "Jembatan yang Berayun Pelan",
                "titleEn": "The Gently Swaying Bridge",
                "textId": "Satu-satunya jalan menuju kebun buah kakek di seberang adalah sebuah jembatan gantung tua yang terbuat dari bilah-bilah bambu kuning. Setiap kali angin bertiup, jembatan itu berderit dan berayun ke kiri dan ke kanan seperti ayunan raksasa.",
                "textEn": "The only path across to Grandpa's orchard was an old suspension bridge fashioned from yellow bamboo slats. With every gust of wind, the bridge creaked and swayed left and right like an enormous playground swing.",
                "quote": "🎋 'Jembatan bambu itu tampak begitu panjang dan berayun di udara bebas.'",
                "coReading": "💡 Tanya si Kecil: Menurutmu mengapa jembatan bambu bisa bergoyang saat ditiup angin?",
                "imagePrompt": "A picture book illustration of a traditional rustic bamboo suspension bridge tied with thick coconut fibers stretching across a ravine between two lush bamboo hills. The bridge curves gracefully, swaying softly in the breeze. Wax crayon textures, earthy greens and honey bamboo tones, 4:3 landscape, completely text-free."
            },
            {
                "number": 3,
                "title": "Lompatan Lincah Bono",
                "titleEn": "Bono's Nimble Leap",
                "textId": "\"Uuk-aak! Jangan takut, kawan!\" celoteh Bono si monyet kecil bertopi caping. Dengan kaki-kaki lincahnya, Bono melompat ke atas tali pegangan jembatan dan bergelantungan santai tanpa rasa takut sedikit pun.",
                "textEn": "\"Ooh-aah! Fear not, my friend!\" chattered Bono the little monkey in a miniature conical farmer's hat. With nimble paws, Bono hopped onto the thick rope handrail and balanced with joyful ease, completely unafraid.",
                "quote": "🐵 'Melihat teman yang tenang dan percaya diri bisa menularkan keberanian ke dalam hati kita.'",
                "coReading": "💡 Aktivitas Seru: Tirukan suara monyet lincah Bono: 'Uuk-aak!' sambil tersenyum!",
                "imagePrompt": "Whimsical children's book illustration of Bono the mischievous little monkey wearing a tiny woven straw hat, balancing playfully on the rope railing of the bamboo bridge, gesturing warmly for Tegar to follow. Warm crayon scribbles, textured paper, 4:3 landscape, completely text-free."
            },
            {
                "number": 4,
                "title": "Langkah Pertama yang Bergetar",
                "titleEn": "The Trembling First Step",
                "textId": "Tegar memegang erat tali tambang sabut kelapa di sisi jembatan. Keringat dingin membasahi telapak tangannya. Perlahan, ia meletakkan sandal jepit merahnya di atas bilah bambu pertama. Kreek... bambu itu melengkung menopang berat badannya.",
                "textEn": "Tegar gripped the thick coconut-fiber handrail tightly. Cool sweat beaded on his little palms. Very slowly, he set his red flip-flop onto the very first bamboo slat. Creak... the bamboo bowed gently beneath his weight.",
                "quote": "🦶 'Langkah pertama selalu terasa paling berat, tetapi itulah awal dari setiap pencapaian.'",
                "coReading": "💡 Tanya si Kecil: Apa yang kamu lakukan saat kakimu merasa ragu untuk melangkah?",
                "imagePrompt": "Storybook illustration of boy Tegar gripping the rope railings with both hands, gingerly placing his foot onto the wooden bamboo bridge deck. His posture is hesitant but focused. Handcrafted wax crayon on textured paper, soft natural lighting, 4:3 landscape, completely text-free."
            },
            {
                "number": 5,
                "title": "Rahasia Menatap ke Depan",
                "titleEn": "The Secret of Looking Straight Ahead",
                "textId": "Saat Tegar melihat ke bawah jurang, kepalanya berputar pusing. Bono segera meloncat ke pundaknya dan berbisik, \"Tutup mata sebentar, tarik napas panjang, lalu tatap pohon mangga besar di ujung seberang. Jangan lihat ke bawah!\"",
                "textEn": "When Tegar glanced down at the churning river, his head spun with dizzy spells. Bono hopped swiftly onto his shoulder and whispered, \"Close your eyes for a moment, take a deep breath, then look straight at the big mango tree on the other side. Don't look down!\"",
                "quote": "🍃 'Tataplah tujuan di depan, jangan biarkan rasa takut di bawah menghentikan langkahmu.'",
                "coReading": "💡 Latihan Bersama: Tarik napas dalam-dalam lewat hidung... lalu hembuskan perlahan lewat mulut bersama si kecil.",
                "imagePrompt": "Touching illustration of little monkey Bono sitting lovingly on Tegar's shoulder, pointing forward with a tiny paw toward the green opposite bank. Tegar takes a deep breath with determination in his eyes. Crayon and oil pastel, warm bedtime colors, 4:3 landscape, completely text-free."
            },
            {
                "number": 6,
                "title": "Menari Bersama Ayunan Bambu",
                "titleEn": "Dancing with the Bamboo's Sway",
                "textId": "Tegar menarik napas sejuk hutan. Satu langkah... dua langkah... Bilah bambu itu bergoyang mengikuti irama langkahnya. Tegar menyadari bahwa jembatan ini tidak akan patah; jembatan ini hanya sedang menari lentur menyambutnya.",
                "textEn": "Tegar drew in the forest's cool, fragrant air. One step... two steps... The bamboo slats swayed to the rhythm of his walk. Tegar realized the bridge would not snap; it was merely dancing flexibly with every stride.",
                "quote": "🎋 'Kadang kita tidak perlu melawan ayunan, cukup menyesuaikan diri dengan iramanya.'",
                "coReading": "💡 Tanya si Kecil: Bisakah kamu menyeimbangkan tubuhmu dengan berdiri dengan satu kaki seperti bangau?",
                "imagePrompt": "Charming illustration of Tegar walking steadily across the middle of the bamboo bridge, holding the rope rails with growing confidence. Below, the river glistens peacefully with teal and aqua crayon strokes. Naive folk art, 4:3 landscape, completely text-free."
            },
            {
                "number": 7,
                "title": "Titik Tengah Jembatan",
                "titleEn": "Midway Over the Ravine",
                "textId": "Di tengah-tengah jurang, angin berhembus lembut membelai pipi Tegar. Dari atas sini, pemandangan lembah ternyata sangat indah! Capung-capung jarum biru menari di atas riak air, dan bunga hutan bermekaran ungu di tebing.",
                "textEn": "Right in the middle of the gorge, a gentle breeze caressed Tegar's cheeks. From up here, the valley view was surprisingly magnificent! Blue damselflies danced over the ripples, and purple mountain orchids bloomed along the mossy cliffs.",
                "quote": "🌸 'Di balik rasa takut yang kita lewati, selalu ada keindahan baru yang menunggu.'",
                "coReading": "💡 Tanya si Kecil: Apa hal indah yang pernah kamu temukan setelah kamu berani mencoba hal baru?",
                "imagePrompt": "Vibrant and serene illustration from high angle showing Tegar pausing at the center of the suspension bridge, looking around in awe at wild purple flowers and flying blue dragonflies above the sparkling river. Handcrafted wax crayon and oil pastel, 4:3 landscape, completely text-free."
            },
            {
                "number": 8,
                "title": "Mendarat di Tanah Seberang",
                "titleEn": "Landing on Solid Ground",
                "textId": "Lima langkah terakhir... dan HUP! Kaki Tegar menjejak tanah berumput empuk di seberang sungai. Bono bersorak gembira sambil melompat ke dahan pohon. Tegar menoleh ke belakang dan memandangi jembatan itu. \"Aku berhasil!\" serunya bangga.",
                "textEn": "Five final careful steps... and HUP! Tegar's feet landed firmly upon the soft, solid earth of the opposite bank. Bono cheered in triumph, doing a celebratory backflip on a tree branch. Tegar looked back at the long bridge. \"I did it!\" he cried proudly.",
                "quote": "🎉 'Rasa bangga yang paling manis adalah saat kita berhasil menaklukkan ketakutan diri sendiri.'",
                "coReading": "💡 Berikan Tos: Berikan tepukan tangan atau tos ceria kepada si kecil untuk merayakan keberaniannya!",
                "imagePrompt": "Joyous children's picture book scene of boy Tegar standing proudly on the green grassy bank with arms raised in victory, while monkey Bono claps happily from a nearby mango tree branch. Golden afternoon sunlight, warm crayon textures, 4:3 landscape, completely text-free."
            },
            {
                "number": 9,
                "title": "Makan Buah Mangga Manis Kakek",
                "titleEn": "Grandpa's Sweet Mango Treat",
                "textId": "Kakek menyambut mereka dengan sekeranjang mangga madu yang manis dan berair. Sambil duduk di bale-bale bambu di bawah pohon rindang, Tegar dan Bono menikmati buah mangga bersama hembusan angin senja yang damai.",
                "textEn": "Grandpa welcomed them with a basket heaped with sweet, juicy honey mangoes. Resting together on a bamboo pavilion beneath shady branches, Tegar and Bono savored the sweet fruit as peaceful dusk drifted in.",
                "quote": "🥭 'Setiap perjalanan penuh keberanian akan bermuara pada manisnya rasa syukur.'",
                "coReading": "💡 Tanya si Kecil: Buah apa yang paling kamu sukai saat bersantai bersama keluarga?",
                "imagePrompt": "Warm, peaceful illustration of Tegar, little monkey Bono, and a kind elderly grandfather with a straw hat sitting on a rustic bamboo porch, sharing golden slices of mango. Sunset gradient in apricot and lavender, waxy crayon scribbles, 4:3 landscape, completely text-free."
            },
            {
                "number": 10,
                "title": "Tidur Nyenyak di Pondok Bambu",
                "titleEn": "Sound Sleep in the Bamboo Cottage",
                "textId": "Malam tiba dengan suara jangkrik yang bernyanyi berirama. Di atas ranjang bambu yang beralaskan tikar pandan harum, Tegar merebahkan tubuhnya. Hatinya kini tenang dan penuh keberanian. Besok, jembatan bergoyang itu bukan lagi rintangan, melainkan sahabat petualangannya. Selamat tidur, Tegar.",
                "textEn": "Night descended accompanied by the gentle, rhythmic lullaby of crickets. Upon a bamboo cot laid with fragrant woven pandan mats, Tegar rested his weary head. His heart was now calm and brave. Tomorrow, that wobbly bridge would no longer be an obstacle, but a dear companion in adventure. Goodnight, brave Tegar.",
                "quote": "🌙 'Tidurlah dengan hati yang kuat, karena kamu lebih berani dari yang kamu bayangkan.'",
                "coReading": "💡 Bisikkan ke si Kecil: Tidurlah yang nyenyak anak pemberani, esok hari selalu siap menyambut langkah hebatmu.",
                "imagePrompt": "A serene, cozy bedtime scene inside a traditional bamboo cottage. Tegar sleeps soundly under a woven blanket with a calm smile, while little monkey Bono is curled up asleep at the foot of the bed. Moonlight streams through the bamboo slats, oil pastel and wax crayon on textured cream paper, 4:3 landscape, text-free."
            }
        ]
    }
    stories.append(s39)

    return stories

print("Story module 38-39 defined successfully")
