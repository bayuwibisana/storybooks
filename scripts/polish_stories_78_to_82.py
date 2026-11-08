# scripts/polish_stories_78_to_82.py
import json

def get_stories_78_to_82():
    stories = [
        # --- STORY 78: Lukisan Cap Daun Warna Pelangi ---
        {
            "id": "story78",
            "storyNumber": 78,
            "title": "Lukisan Cap Daun Warna Pelangi",
            "englishTitle": "Rainbow Leaf Print Painting",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kreativitas dengan unsur alam & menghargai pola-pola unik",
            "cover": "covers/story78_cover.jpg",
            "synopsis": "Lilis mengumpulkan aneka bentuk daun di kebun—daun pepaya menjari, daun sirih berbentuk hati, dan daun mangga memanjang. Dengan mengoleskan cat air warna-warni pada urat-urat daun dan mengecapnya di kertas gambar, Lilis menciptakan hutan pelangi yang memukau.",
            "protagonist": "Lilis (Gadis bercelemek penuh bercak warna)",
            "companion": "Kelinci Putih (Kelinci menemani di samping kertas gambar)",
            "setting": "Meja Gambar Kayu",
            "pages": [
                {
                    "number": 1,
                    "title": "Keranjang Bambu Penuh Daun",
                    "titleEn": "Bamboo Basket Full of Leaves",
                    "textId": "Pagi yang cerah di kebun belakang, Lilis menenteng keranjang anyaman bambu kecil. Bersama Mochi, kelinci putih peliharaannya yang berhidung merah muda, Lilis memungut daun-daun berguguran: daun sirih berujung lancip, daun pakis bergerigi halus, dan daun mangga yang berurat tebal.",
                    "textEn": "On a bright morning in the backyard garden, Lilis carried a small woven bamboo basket. Beside Mochi, her pet white bunny with a twitchy pink nose, Lilis gathered fallen leaves: heart-shaped betel leaves, finely serrated ferns, and thick-veined mango leaves.",
                    "quote": "Setiap helai daun memiliki bentuk dan cerita unik dari alam.",
                    "coReading": "Berapa banyak bentuk daun berbeda yang bisa kamu temukan di kebun?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Lilis, a sweet girl with braided pigtails wearing a colorful paint-splattered apron, kneeling in the garden beside Mochi the fluffy white bunny, collecting fallen leaves into a basket. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Urat-Urat Daun yang Menonjol",
                    "titleEn": "Prominent Leaf Veins",
                    "textId": "Di atas meja kayu teras, Lilis meraba punggung daun mangga. Urat-urat daun itu menonjol seperti jembatan-jembatan kecil yang mengalirkan kehidupan. 'Urat daun inilah yang akan menjadi cap alami lukisan kita, Mochi,' bisik Lilis pada kelincinya.",
                    "textEn": "At her wooden porch table, Lilis traced the back of a mango leaf. Its veins stood out like tiny ridges carrying life's pulse. 'These leaf veins will be our natural stamp, Mochi,' Lilis whispered to her bunny.",
                    "quote": "Hal yang paling tersembunyi sering kali menyimpan pola terindah.",
                    "coReading": "Coba raba punggung daun, apakah terasa bergaris-garis?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Close-up of Lilis's finger gently tracing the raised veins on the underside of a green mango leaf on a rustic wooden table. White bunny peeking curiously beside her, simple bead dot eyes, naive folk art, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Palet Warna Pelangi",
                    "titleEn": "Rainbow Paint Palette",
                    "textId": "Lilis membuka wadah cat airnya. Di atas palet keramik putih, ia menuang warna merah delima, kuning matahari, biru laut, dan hijau apel. Dengan kuas spons lembutnya, ia siap melukis di punggung dedaunan.",
                    "textEn": "Lilis opened her watercolor set. On a white ceramic palette, she poured ruby red, sunshine yellow, ocean blue, and apple green. With a soft sponge brush, she was ready to paint the leaf backs.",
                    "quote": "Keceriaan warna membawa semangat bagi setiap jiwa yang berkreasi.",
                    "coReading": "Warna apa yang paling kamu sukai di atas palet cat Lilis?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A colorful paint palette with bright puddles of paint, paintbrushes, and fresh leaves arranged on paper. Lilis smiling happily with paint spots on her cheeks, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Sapuan Cat pada Punggung Daun",
                    "titleEn": "Strokes of Paint on the Leaf Back",
                    "textId": "Lilis mengoleskan cat kuning cerah di ujung daun sirih dan warna merah menyala di pangkalnya. Kedua warna itu berbaur manis di tengah urat daun membentuk gradasi jingga yang hangat. Mochi mengendus aroma cat yang segar tanpa bersin.",
                    "textEn": "Lilis brushed sunny yellow on the betel leaf tip and fiery red at its stem. The two shades blended softly in the center into a warm orange gradient. Mochi sniffed the fresh paint scent without sneezing.",
                    "quote": "Memadukan warna adalah seni mendengarkan harmoni keindahan.",
                    "coReading": "Kuning dicampur merah menjadi warna apa ya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Detailed view of Lilis holding a paintbrush coating a leaf with blended yellow and orange watercolors. Bunny sitting peacefully near her elbow, bead dot eyes, naive storybook style, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Tekanan Lembut di Atas Kertas",
                    "titleEn": "A Gentle Press on the Paper",
                    "textId": "Lilis meletakkan daun bercat itu menghadap ke bawah di atas selembar kertas gambar tebal. Ia menaruh selembar kertas koran di atasnya dan menekannya perlahan dengan telapak tangannya: 'Satu... dua... tiga... tekan dengan rata!'",
                    "textEn": "Lilis laid the painted leaf face-down on a thick sheet of drawing paper. She placed a scrap of newspaper over it, pressing down gently with her palm: 'One... two... three... press nice and even!'",
                    "quote": "Sentuhan yang mantap namun lembut memberikan hasil terbaik.",
                    "coReading": "Bisakah kamu menekan telapak tanganmu ke meja seperti Lilis?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Lilis gently pressing her small hands down on paper to stamp the leaf print. Focused expression, simple black bead dot eyes, colorful art studio setting on sunny porch, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Keajaiban Urat-Urat Emas",
                    "titleEn": "The Wonder of Golden Veins",
                    "textId": "Ketika Lilis mengangkat daun itu perlahan, 'Wah!' serunya takjub. Di atas kertas putih tercetak gambar daun sempurna dengan seluruh urat-urat halusnya yang bergradasi merah jingga berkilauan. Setiap cabang urat tampak seperti pohon kecil yang indah.",
                    "textEn": "When Lilis peeled the leaf away, 'Wow!' she gasped in wonder. On the white sheet was a perfect leaf impression, its delicate veins stamped in shimmering red-orange gradients. Each vein branch looked like a magnificent miniature tree.",
                    "quote": "Keajaiban alam terungkap saat kita memberinya ruang untuk bersinar.",
                    "coReading": "Bagaimana bentuk cap daun yang tercetak di kertas?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. The paper revealing a gorgeous leaf print in vibrant red, orange, and yellow veins. Lilis holding up the painted leaf with a beaming smile, white bunny watching closely, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Hutan Pelangi yang Rimbun",
                    "titleEn": "A Lush Rainbow Forest",
                    "textId": "Lilis semakin bersemangat. Ia mengecap daun pakis dengan warna hijau zamrud dan biru laut, serta daun mangga dengan warna ungu lembayung. Satu demi satu cap daun berjajar di atas kertas, menjelma menjadi hutan pelangi yang penuh keajaiban.",
                    "textEn": "Lilis's joy bubbled over. She stamped ferns in emerald green and ocean blue, and mango leaves in deep twilight violet. One after another, the leaf prints lined across the page, transforming into a magical rainbow forest.",
                    "quote": "Kreativitas tanpa batas mampu menciptakan dunia baru dari selembar kertas.",
                    "coReading": "Warna apa saja yang ada di hutan pelangi buatan Lilis?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A wide sheet of paper filled with beautiful multi-colored leaf prints creating an enchanting magical forest collage. Lilis adding a tiny green dot, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Kupu-Kupu dari Cap Jemari",
                    "titleEn": "Butterflies from Fingerprints",
                    "textId": "Untuk melengkapi hutannya, Lilis mencelupkan jempolnya ke cat merah jambu dan mengecapkannya dua kali di atas ranting daun: jadilah sepasang sayap kupu-kupu! Mochi si kelinci melompat ke pangkuan Lilis, mengelus dagunya dengan telinga berbulu seolah memberi selamat.",
                    "textEn": "To complete her forest, Lilis dipped her thumb in bright pink paint and stamped it twice above a leafy branch: creating a pair of fluttering butterfly wings! Mochi hopped onto Lilis's lap, brushing his soft furry ears under her chin in joyful congratulations.",
                    "quote": "Sentuhan pribadi membuat sebuah karya seni bernyawa dan penuh kehangatan.",
                    "coReading": "Pernahkah kamu membuat kupu-kupu dari cap jempol tanganmu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Lilis laughing delightfully as white bunny Mochi snuggles into her lap. The finished colorful painting displayed proudly on an easel behind them, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Bingkai Ranting di Dinding Kamar",
                    "titleEn": "Twig Frame on the Bedroom Wall",
                    "textId": "Ayah membantu membuatkan bingkai dari empat batang ranting kayu lurus yang diikat tali rami. Lukisan hutan cap daun pelangi itu digantung di dinding kamar Lilis. Ruangan tidur Lilis terasa seperti pondok di tengah taman dongeng yang semarak.",
                    "textEn": "Dad helped craft a frame from four straight wooden twigs tied with rustic hemp twine. The rainbow leaf-print forest was hung on Lilis's bedroom wall. Her bedroom felt like a cottage in a vibrant fairy-tale garden.",
                    "quote": "Karya yang dipajang dengan bangga menumbuhkan rasa percaya diri.",
                    "coReading": "Di mana lukisan cap daun Lilis dipajang?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Lilis's cozy bedroom with the colorful framed leaf painting hanging above her wooden nightstand. Dad smiling proudly at the door, Lilis admiring her artwork, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tertidur di Bawah Naungan Pelangi",
                    "titleEn": "Sleeping Beneath Rainbow Shades",
                    "textId": "Malam tiba dan angin semilir berhembus melalui tirai jendela. Mochi tidur mendengkur halus di samping kaki ranjang Lilis. Lilis memejamkan mata di bawah selimut hangatnya, membayangkan dirinya berjalan-jalan di tengah hutan cap daun pelangi yang menyejukkan hati.",
                    "textEn": "Night fell and a gentle breeze whispered through the window curtains. Mochi slept purring softly at the foot of Lilis's bed. Lilis closed her eyes beneath her warm duvet, imagining herself strolling through the comforting rainbow forest of her dreams.",
                    "quote": "Tidurlah dalam warna-warni yang damai, esok adalah kanvas baru untuk berbahagia.",
                    "coReading": "Mari pejamkan mata dan bayangkan kamu tidur di bawah naungan pohon warna-warni.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Lilis sleeping peacefully in bed with a cozy floral quilt, bunny curled up sleeping at the foot of the bed. Moonbeams shining softly on the rainbow leaf painting on the wall. Serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 79: Topeng Rubah dari Kantong Belanja ---
        {
            "id": "story79",
            "storyNumber": 79,
            "title": "Topeng Rubah dari Kantong Belanja",
            "englishTitle": "Fox Mask from a Paper Grocery Bag",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Daur ulang kertas, bermain peran imajinatif, & kebersamaan saudara",
            "cover": "covers/story79_cover.jpg",
            "synopsis": "Fahri dan adik kecilnya memanfaatkan kantong belanja kertas cokelat tebal untuk membuat topeng rubah dan topeng tupai berbulu jingga. Dengan gunting tumpul dan krayon warna-warni, mereka menjelma menjadi hewan rimba yang bersahabat di atas karpet kamar.",
            "protagonist": "Fahri (Anak laki-laki bergunting ujung tumpul)",
            "companion": "Adik Fahri (Adik kecil memakai topeng tupai)",
            "setting": "Lantai Karpet Kamar",
            "pages": [
                {
                    "number": 1,
                    "title": "Kantong Kertas Cokelat Tebal",
                    "titleEn": "Thick Brown Paper Bags",
                    "textId": "Sehabis Ibu pulang berbelanja dari pasar desa, dua kantong kertas cokelat tebal bertali rami tergeletak di lantai dapur. Alih-alih melipatnya dan menyimpannya di gudang, Fahri, anak laki-laki berpipi tembam, melihat telinga runcing rubah tersembunyi pada lipatan kertas cokelat itu.",
                    "textEn": "After Mother returned from shopping at the village market, two thick brown paper grocery bags lay on the kitchen floor. Instead of tucking them into a dark cupboard, chubby-cheeked Fahri saw pointy fox ears hidden within the brown paper folds.",
                    "quote": "Imajinasi melihat wajah-wajah ramah pada benda-benda tak bernyawa.",
                    "coReading": "Pernahkah kamu melihat kantong belanja kertas cokelat di rumah?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Fahri, a curious boy in a striped t-shirt and shorts, sitting on the wooden kitchen floor with his toddler little sister, examining two large brown paper grocery bags. Simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Gunting Tumpul dan Garis Pola",
                    "titleEn": "Blunt Scissors and Pattern Lines",
                    "textId": "Dengan pensil hitamnya, Fahri menggambar dua segitiga runcing untuk telinga rubah dan dua lingkaran sebesar koin untuk lubang mata. Dengan gunting ujung tumpul yang aman, Fahri memotong kertas dengan hati-hati sementara adiknya bertepuk tangan riang.",
                    "textEn": "With his pencil, Fahri sketched two pointy triangles for fox ears and two coin-sized circles for eye holes. With child-safe blunt scissors, Fahri carefully cut the paper while his baby sister clapped with glee.",
                    "quote": "Bermain dengan aman adalah kunci kegembiraan yang tenang.",
                    "coReading": "Bagaimana bentuk telinga rubah yang digambar Fahri?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Fahri carefully cutting eye holes out of the flat brown paper with round-tipped child scissors. Little sister sitting beside him holding a crayon, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Goresan Krayon Jingga dan Putih",
                    "titleEn": "Strokes of Orange and White Crayons",
                    "textId": "Fahri mewarnai bagian pipi dan dahi topeng rubah dengan krayon jingga cerah. Di bagian moncong dan ujung telinga, ia mengoleskan krayon putih salju tebal-tebal agar tampak berbulu lebat. Garis-garis lilin krayon itu membuat topeng tampak hidup.",
                    "textEn": "Fahri shaded the fox mask's cheeks and forehead with bright orange crayon. Across the muzzle and ear tips, he layered thick snowy white crayon to look fluffy and soft. The waxy crayon strokes brought the mask to life.",
                    "quote": "Warna-warna cerah memberi jiwa pada setiap karakter cerita.",
                    "coReading": "Warna apa saja yang dimiliki seekor rubah di hutan dongeng?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Close-up of the paper bag mask transforming into a cute friendly fox face with bright orange and white crayon shading. Fahri coloring with steady hands, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Kumis Panjang dari Benang Hitam",
                    "titleEn": "Long Whiskers of Black Thread",
                    "textId": "Dari laci mesin jahit Ibu, Fahri mengambil seutas benang hitam tebal. Ia memotongnya menjadi enam helai dan menempelkannya di samping hidung bulat hitam topeng. Tiga kumis di kiri dan tiga di kanan bergoyang lucu setiap kali tertiup napas.",
                    "textEn": "From Mother's sewing basket, Fahri took sturdy black thread. Cutting it into six strands, he glued them beside the round black nose. Three whiskers on the left and three on the right twitched playfully with every puff of air.",
                    "quote": "Detail-detail kecil menyempurnakan keajaiban sebuah mainan.",
                    "coReading": "Berapa jumlah kumis pada topeng rubah itu?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Fahri gluing black thread whiskers onto the paper fox mask. Little sister watching with big round eyes, cozy living room floor, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Topeng Tupai untuk Adik",
                    "titleEn": "Squirrel Mask for Little Sister",
                    "textId": "Tidak lupa pada sang adik, dari kantong kertas kedua Fahri membuat topeng tupai dengan telinga bulat dan pipi tembam. Adik tertawa geli saat Fahri memakaikan topeng tupai itu di wajahnya dan mengikat tali rami lembut di belakang kepalanya.",
                    "textEn": "Not forgetting his sister, Fahri used the second bag to create a cute squirrel mask with round ears and chubby cheeks. Sister giggled as Fahri slipped the squirrel mask over her face, tying soft strings behind her head.",
                    "quote": "Kasih sayang kakak tercermin dari kesediaannya berbagi kebahagiaan.",
                    "coReading": "Hewan apakah yang menjadi topeng adik Fahri?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Fahri gently tying the soft string of a cute brown squirrel mask around his toddler sister's head. Both smiling happily, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Penjelajah Rimba di Atas Karpet",
                    "titleEn": "Jungle Explorers on the Carpet",
                    "textId": "Kini di atas karpet kamar bermotif daun, berdirilah seekor rubah yang bijak dan seekor tupai yang lincah. Fahri melangkah mengendap-endap dengan empat kakinya sambil mendengus pura-pura, sementara adik melompat-lompat menirukan tupai mencari biji kenari.",
                    "textEn": "Now upon the leaf-patterned carpet stood a clever friendly fox and a sprightly little squirrel. Fahri crept playfully on hands and knees sniffing the air, while his sister bounced like a squirrel hunting for acorns.",
                    "quote": "Bermain peran melatih empati untuk memahami kehidupan makhluk lain.",
                    "coReading": "Bisakah kamu berjalan merangkak seperti rubah atau tupai?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Fahri wearing the cute orange fox paper mask and sister wearing the round-eared squirrel mask crawling playfully on a green rug in their bedroom. Whimsical storybook mood, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Pohon Sofa dan Jurang Selimut",
                    "titleEn": "Sofa Trees and Blanket Canyons",
                    "textId": "Sofa ruang tamu berubah menjadi dahan pohon beringin tempat tupai bersembunyi. Tumpukan selimut wol biru menjadi sungai berarus deras yang harus diseberangi bersama. Rubah dan tupai saling bergandengan tangan agar tidak ada yang terpeleset.",
                    "textEn": "The living room sofa turned into a giant banyan bough where the squirrel hid. Piles of blue quilts became a roaring river they had to cross together. Fox and squirrel held hands tightly so neither would slip.",
                    "quote": "Kerja sama di dunia khayalan melatih persaudaraan di dunia nyata.",
                    "coReading": "Bagaimana cara rubah dan tupai menyeberangi sungai selimut?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Fahri in his fox mask helping his little sister in her squirrel mask step carefully across blue folded blankets. Living room setting transformed by childhood imagination, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Pesta Buah Hutan dari Ibu",
                    "titleEn": "Forest Fruit Feast from Mother",
                    "textId": "'Kuk-kuruyuk!' Ibu berseru menirukan suara burung rimba sambil membawakan piring berisi potongan apel merah dan pisang manis. 'Makanan lezat untuk rubah dan tupai yang baik hati,' senyum Ibu. Kedua hewan kecil itu melahap buah dengan lahap di atas lantai.",
                    "textEn": "'Chirp, squawk!' Mother called, imitating a jungle bird while delivering a plate of sliced red apples and sweet bananas. 'A delicious feast for my kind-hearted fox and squirrel,' Mother smiled. The two little critters munched happily on the rug.",
                    "quote": "Dukungan orang tua membuat dunia imajinasi anak semakin berwarna.",
                    "coReading": "Buah apa yang dimakan rubah dan tupai pada pesta hutan?",
                    "imagePrompt": "Warm oil pastel illustration on heavy cream paper. Mother setting down a bowl of apple slices on the carpet beside Fahri and his sister who have their paper masks tilted up on their foreheads, smiling with simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Topeng yang Digantung di Sandaran Kursi",
                    "titleEn": "Masks Hanging on the Chair",
                    "textId": "Matahari sore meredup dan waktu bermain selesai. Fahri melepaskan topeng mereka dan menggantungnya dengan rapi di sandaran kursi kayu. Topeng rubah dan tupai itu tampak tersenyum menatap ruangan yang kini kembali tenang dan rapi.",
                    "textEn": "The evening sun faded and playtime drew to a close. Fahri gently untied their masks, hanging them neatly over the wooden chair back. The fox and squirrel masks seemed to smile across the now peaceful and tidy room.",
                    "quote": "Merapikan kembali tempat bermain adalah tanda kedewasaan anak baik.",
                    "coReading": "Di mana Fahri menyimpan topeng buatannya setelah selesai bermain?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. The two paper grocery bag masks (fox and squirrel) hanging neatly on a wooden chair back beside a made bed. Warm golden twilight light streaming through the window, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi di Hutan Dongeng",
                    "titleEn": "Dreams in the Storybook Forest",
                    "textId": "Malam tiba dan adik sudah terlelap di kamar sebelah memeluk boneka beruangnya. Fahri menarik selimutnya hingga ke dagu. Di dalam mimpi indahnya, ia berlari bebas menembus hutan pinus keemasan bersama kawan-kawan binatang rimba yang ramah.",
                    "textEn": "Night arrived and his baby sister was already asleep in her room hugging her teddy bear. Fahri pulled his blanket up to his chin. In sweet dreams, he ran freely through golden pine woods alongside friendly woodland animals.",
                    "quote": "Tidurlah dalam ketenangan, petualangan baru selalu menantimu esok hari.",
                    "coReading": "Mari pejamkan mata dan bayangkan kamu berlari riang di hutan bersama sahabatmu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Fahri sleeping peacefully in his cozy bedroom tucked under blankets. Dream bubble above his head showing friendly cartoon fox and squirrel playing under starlit canopy. Peaceful bedtime scene, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 80: Cangkir Tanah Liat Mini ---
        {
            "id": "story80",
            "storyNumber": 80,
            "title": "Cangkir Tanah Liat Mini",
            "englishTitle": "Mini Clay Cup",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Ketelatenan tangan, belajar dari kegagalan, & warisan tradisi",
            "cover": "covers/story80_cover.jpg",
            "synopsis": "Nanda mengunjungi bengkel tembikar Nenek di desa. Di sana, Nanda belajar memijat tanah liat basah di atas roda putar kayu. Meskipun cangkir pertamanya miring dan roboh, dengan kesabaran dan bimbingan lembut tangan Nenek, Nanda berhasil membuat cangkir teh mungil bermotif bunga.",
            "protagonist": "Nanda (Gadis cilik bertangan belepotan lumpur)",
            "companion": "Nenek Nanda (Nenek tersenyum mengajari memutar tanah)",
            "setting": "Bengkel Tembikar Desa",
            "pages": [
                {
                    "number": 1,
                    "title": "Aroma Tanah Basah di Bengkel Nenek",
                    "titleEn": "Scent of Damp Earth in Grandma's Workshop",
                    "textId": "Di ujung desa terdapat bengkel tembikar milik Nenek yang bernaung di bawah atap genting tanah liat tua. Udara di dalam ruangan beraroma segar seperti tanah sehabis hujan lebat. Di rak-rak bambu berjajar guci, kendi, dan mangkuk yang sedang diangin-anginkan.",
                    "textEn": "At the edge of the village lay Grandma's pottery workshop beneath an old clay-tiled roof. The air inside smelled fresh like rich earth after a thunderstorm. Along bamboo shelves sat drying jars, jugs, and bowls.",
                    "quote": "Bumi menyediakan bahan mentah yang luar biasa untuk disentuh tangan manusia.",
                    "coReading": "Pernahkah kamu memegang tanah liat basah yang lembut dan dingin?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Nanda, a young girl with twin buns and an indigo work apron, entering Grandma's rustic pottery shed. Rows of handcrafted clay pottery on bamboo racks, sunbeams through roof slats, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Gumpalan Lumpur Lembut",
                    "titleEn": "Lump of Soft Clay",
                    "textId": "Nenek memotong segumpal tanah liat abu-abu gelap dengan kawat tembaga. Tanah itu dingin, padat, dan sangat lentur. Nenek meletakkannya di atas meja batu di depan Nanda. 'Remaslah seperti menguleni adonan kue, Nanda, agar gelembung udara di dalamnya keluar,' senyum Nenek.",
                    "textEn": "Grandma sliced a lump of dark grey clay with a wire cutter. The clay felt cool, dense, and wonderfully pliable. Grandma placed it on the stone table before Nanda. 'Knead it like bread dough, Nanda, so all the little air bubbles press out,' Grandma smiled.",
                    "quote": "Mempersiapkan bahan dengan sabar menentukan kekuatan hasil akhir.",
                    "coReading": "Bisakah kamu menirukan gerakan menekan dan menguleni adonan?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Nanda pressing both hands into a soft lump of clay on a wooden table, her hands delightfully muddy. Kind grandmother in batik apron smiling beside her, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Roda Putar Kayu yang Berputar",
                    "titleEn": "The Spinning Wooden Potter's Wheel",
                    "textId": "Nenek memindahkan gumpalan tanah yang sudah bulat ke tengah roda putar kayu. Dengan dorongan kakinya pada pedal bawah, roda mulai berputar perlahan: 'Syuuur... syuuur...' Suaranya berirama seperti dengkuran kucing besar.",
                    "textEn": "Grandma set the smoothed ball of clay onto the center of the wooden potter's wheel. With a gentle kick of her foot against the flywheel, the turntable began to spin: 'Whirrr... whirrr...' humming rhythmically like a big purring cat.",
                    "quote": "Irama yang teratur membantu kita memusatkan perhatian dan pikiran.",
                    "coReading": "Bagaimana bunyi roda putar tembikar saat digerakkan?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Grandma pushing the foot pedal of the rustic wooden potter's wheel while Nanda watches with wide curious eyes. Centered clay spinning smoothly on the wheel head, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Ibu Jari yang Menekan Lubang Tengah",
                    "titleEn": "Thumbs Pressing the Center Well",
                    "textId": "Nenek mencelupkan tangannya ke dalam mangkuk air, lalu membimbing kedua tangan kecil Nanda. 'Letakkan kedua jempolmu tepat di tengah, Nanda. Tekan pelan-pelan ke bawah.' Ketika jempol Nanda menekan tanah yang berputar, sebuah kawah kecil terbentuk seketika.",
                    "textEn": "Grandma dipped her hands into a bowl of water, then guided Nanda's small hands. 'Place your thumbs right in the center, Nanda. Press down slowly.' As Nanda's thumbs pressed into the spinning clay, a little well opened up instantly.",
                    "quote": "Bimbingan tangan yang berpengalaman memberi ketenangan bagi pemula.",
                    "coReading": "Apa yang terjadi saat jempol ditekan ke tengah tanah liat yang berputar?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Close-up of Grandma's weathered hands gently holding Nanda's small muddy hands, pressing thumbs together into the spinning clay opening. Water splashing softly, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Cangkir Pertama yang Roboh",
                    "titleEn": "The First Slumping Cup",
                    "textId": "Karena terlalu bersemangat, Nanda menekan dinding tanah terlalu keras. Tiba-tiba, tanah liat itu bergoyang oleng dan 'Pletuk!' dinding cangkir ambruk menjadi gumpalan pipih miring. Nanda terkejut dan menundukkan kepalanya, merasa bersalah.",
                    "textEn": "Overexcited, Nanda pinched the clay wall too hard. Suddenly the clay wobbled unevenly and 'Plop!' the cup walls slumped into a squished, lopsided mound. Nanda gasped, lowering her head with a discouraged frown.",
                    "quote": "Kegagalan bukanlah akhir, melainkan langkah pertama dari pemahaman.",
                    "coReading": "Mengapa cangkir pertama Nanda bisa ambruk?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Nanda looking down with a sad pensive face at the squashed lopsided clay lump on the wheel. Grandma smiling warmly and placing a comforting hand on her shoulder, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Pelukan dan Semangat Nenek",
                    "titleEn": "Grandma's Hug and Encouragement",
                    "textId": "Nenek tertawa renyah dan mengusap pipi Nanda dengan punggung tangannya yang bersih. 'Jangan berkecil hati, sayang. Dulu Nenek merobohkan seratus mangkuk sebelum bisa membuat satu kendi yang lurus. Tanah liat selalu memberi kita kesempatan kedua.'",
                    "textEn": "Grandma chuckled warmly, brushing Nanda's cheek with the clean back of her hand. 'Do not be discouraged, my dear. Long ago Grandma collapsed a hundred bowls before shaping a single straight jar. Clay always grants us a second chance.'",
                    "quote": "Kebaikan hati orang tua mengubah kegagalan menjadi keberanian baru.",
                    "coReading": "Kata-kata apa yang membuat Nanda tersenyum kembali?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Grandma comforting Nanda with a tender smile in the rustic workshop. Morning sunbeams illuminating the pottery room, reassuring atmosphere, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Membentuk Dinding yang Halus",
                    "titleEn": "Raising the Smooth Walls",
                    "textId": "Nanda menarik napas dalam-dalam dan tersenyum. Nenek memberikan gumpalan tanah liat baru. Kali ini Nanda menarik dinding cangkir dengan gerakan sangat lembut dan perlahan. Dinding cangkir naik tegak, bundar, dan anggun setinggi cangkir teh peri.",
                    "textEn": "Nanda took a deep breath and smiled. Grandma set down a fresh ball of clay. This time Nanda drew up the walls with gentle, steady patience. The cup rose upright, round, and charming, just the size of a fairy's teacup.",
                    "quote": "Kesabaran dan kelembutan selalu menghasilkan bentuk yang kokoh.",
                    "coReading": "Bagaimana bentuk cangkir kedua buatan Nanda?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. A charming, smooth miniature clay teacup standing proudly on the potter's wheel. Nanda's face beaming with triumph, muddy hands raised in celebration, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Tangkai Melengkung dan Goresan Bunga",
                    "titleEn": "Curved Handle and Carved Blooms",
                    "textId": "Setelah cangkir diangkat dari roda putar, Nanda memilin cacing tanah liat kecil untuk dijadikan pegangan melengkung. Dengan sebatang lidi bambu, Nanda menggores tiga kelopak bunga melati kecil di dinding cangkir sebagai tanda cinta untuk Nenek.",
                    "textEn": "After lifting the cup off the wheel, Nanda rolled a tiny clay coil to make a curved handle. With a bamboo stick, Nanda carved three little jasmine petals into the cup's side as a mark of love for Grandma.",
                    "quote": "Sentuhan ukiran tangan memberi tanda kehangatan cinta pembuatnya.",
                    "coReading": "Bunga apa yang digores Nanda pada dinding cangkirnya?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Nanda using a bamboo stylus to carve tiny delicate flower petals into the side of the clay cup with a cute loop handle. Grandma watching with proud eyes, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Menjemur di Bawah Naungan Angin",
                    "titleEn": "Drying in the Gentle Breezy Shade",
                    "textId": "Nanda meletakkan cangkir mininya di rak bambu paling atas. Angin sore bertiup semilir mengeringkan tanah basah menjadi gerabah yang kokoh. 'Besok kita bakar di tungku sekam, dan cangkir ini akan siap untuk minum teh madumu,' kata Nenek bangga.",
                    "textEn": "Nanda placed her mini cup on the top bamboo shelf. The evening breeze blew softly, drying the damp clay into sturdy pottery. 'Tomorrow we will fire it in the rice-husk kiln, and it will be ready for your honey tea,' said Grandma proudly.",
                    "quote": "Hasil karya yang diperjuangkan dengan sabar terasa seribu kali lebih manis.",
                    "coReading": "Untuk apa cangkir mini itu kelak akan digunakan Nanda?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Nanda placing the mini clay cup on a wooden drying rack beside other rustic pottery. Golden late afternoon sun streaming through the workshop door, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Mimpi Cangkir Ajaib Nenek",
                    "titleEn": "Dreams of Grandma's Magic Cup",
                    "textId": "Malam itu Nanda tidur lelap di pondok Nenek. Tangannya yang sudah dicuci bersih dan harum sabun melati memeluk guling kapuk dengan damai. Di dalam mimpinya, Nanda meminum teh hangat dari cangkir tanah liat buatannya sendiri di bawah taburan bintang-bintang desa.",
                    "textEn": "That night Nanda slept deeply in Grandma's cottage. Her hands, washed clean and smelling of sweet jasmine soap, hugged her kapok bolster peacefully. In her dreams, Nanda sipped warm tea from her own handmade clay cup beneath a village sky of twinkling stars.",
                    "quote": "Tidurlah dalam damai, keterampilan baru telah bersemi di jemari tanganmu.",
                    "coReading": "Mari pejamkan mata dan rasakan kebanggaan atas hal baru yang kamu pelajari hari ini.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Nanda sleeping peacefully in a rustic wooden bedroom under a batik quilt. Outside the window, a serene crescent moon and stars shining above Grandma's pottery workshop. Deep peaceful bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 81: Benteng Pasir Berparit Kerang ---
        {
            "id": "story81",
            "storyNumber": 81,
            "title": "Benteng Pasir Berparit Kerang",
            "englishTitle": "Sandcastle with a Seashell Moat",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kreativitas arsitektur pasir & menerima pasang surut alam",
            "cover": "covers/story81_cover.jpg",
            "synopsis": "Di tepi pantai berpasir putih, Aldo membangun benteng pasir megah berkubah tiga dengan parit melingkar yang dihiasi cangkang kerang mutiara. Ketika ombak senja perlahan datang membasahi bentengnya, Aldo belajar bahwa keindahan terbesar adalah saat kita menikmati proses menciptakannya.",
            "protagonist": "Aldo (Anak pesisir bertopi ember mini)",
            "companion": "Kepiting Cilik (Kepiting mengintip dari parit pasir)",
            "setting": "Tepi Pantai Pasir Halus",
            "pages": [
                {
                    "number": 1,
                    "title": "Pasir Lembap Tepi Ombak",
                    "titleEn": "Moist Sand by the Waves",
                    "textId": "Matahari sore menyinari pantai dengan cahaya keemasan yang hangat. Di batas air pasang surut, pasir terasa lembap, padat, dan dingin seperti adonan kue. Aldo, anak laki-laki bertopi ember katun kuning, menenteng ember merah dan sekop plastik birunya.",
                    "textEn": "The afternoon sun bathed the beach in warm golden light. At the edge of the receding tide, the sand felt damp, firm, and cool like cookie dough. Aldo, a little boy in a yellow cotton bucket hat, carried his red bucket and blue plastic shovel.",
                    "quote": "Alam menyediakan kanvas terluas bagi imajinasi anak-anak.",
                    "coReading": "Apakah kamu suka bermain pasir di tepi pantai?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Aldo, a young boy in a yellow bucket hat and swim shorts, walking along the beach shore carrying a red plastic bucket and blue spade. Gentle ocean waves foaming softly, simple bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Menara-Menara Cetakan Ember",
                    "titleEn": "Bucket-Molded Towers",
                    "textId": "Aldo mengisi ember merahnya dengan pasir basah, menepuk-nepuknya hingga padat, lalu membalikkan ember di atas tanah pasir. 'Satu, dua, tiga... angkat!' seru Aldo. Terbentuklah sebuah menara silinder yang kokoh dan rapi. Aldo membuat empat menara untuk sudut bentengnya.",
                    "textEn": "Aldo filled his red bucket with damp sand, patting it down firm, then flipped the bucket onto the sand. 'One, two, three... lift!' Aldo cheered. Up stood a sturdy, neat cylindrical tower. Aldo built four towers for his castle corners.",
                    "quote": "Fondasi yang padat dan kuat membuat bangunan berdiri megah.",
                    "coReading": "Berapa banyak menara yang dibuat Aldo untuk sudut bentengnya?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Aldo carefully lifting the red bucket to reveal a crisp molded sand tower on the beach. Three other sand towers standing nearby, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Dinding Penghubung yang Kokoh",
                    "titleEn": "Sturdy Connecting Walls",
                    "textId": "Dengan kedua tangannya, Aldo menumpuk pasir dan meratakannya menjadi dinding pembatas yang tebal di antara keempat menara. Ia menggunakan bilah kayu hanyut sebagai penggaris untuk membuat dinding bentengnya lurus dan berwibawa.",
                    "textEn": "With both hands, Aldo piled sand and smoothed it into thick curtain walls connecting the four towers. He used a piece of driftwood as a straightedge to make his castle walls smooth and proud.",
                    "quote": "Kerapian adalah hasil dari ketelitian dan rasa cinta pada apa yang kita buat.",
                    "coReading": "Benda apa yang digunakan Aldo untuk merapikan dinding pasir?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Aldo using a smooth piece of driftwood to scrape and flatten the walls of his sandcastle. Four corner towers rising, blue sky, simple bead dot eyes, 4 limbs, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Parit Melingkar Penangkal Air",
                    "titleEn": "Circular Moat to Guard the Castle",
                    "textId": "Di sekeliling benteng, Aldo menggali parit selebar telapak tangannya. Parit itu melingkar sempurna seperti cincin pelindung. 'Parit ini akan menampung air laut agar bentengku tidak mudah hanyut,' pikir Aldo bangga.",
                    "textEn": "Around the castle, Aldo dug a moat as wide as his palm. The trench circled in a perfect protective ring. 'This moat will hold back the sea water so my castle stays safe,' Aldo thought with pride.",
                    "quote": "Perencanaan yang baik memikirkan cara menjaga apa yang telah dibangun.",
                    "coReading": "Untuk apa parit dibuat melingkari benteng?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Aldo kneeling on damp sand using his blue spade to carve a neat circular moat around the sandcastle. Seaside horizon in background, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Tamu Kecil Bercapit Merah",
                    "titleEn": "A Tiny Red-Clawed Guest",
                    "textId": "Ketika Aldo sedang merapikan dasar parit, pasir bergerak sedikit. Muncullah seekor kepiting pantai kecil seukuran koin dengan sepasang mata bertangkai yang lucu. Kepiting itu berjalan miring dan berteduh di dalam parit buatan Aldo.",
                    "textEn": "While Aldo was smoothing the moat floor, the sand stirred gently. Up popped a tiny coin-sized ghost crab with funny stalk eyes. The crab scuttled sideways, settling cozily inside Aldo's moat.",
                    "quote": "Karya yang ramah selalu menyambut sahabat-sahabat baru dari alam.",
                    "coReading": "Bagaimana cara kepiting pantai berjalan?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Close-up of the sand moat with a cute little translucent ghost crab scuttling with round dot eyes on stalks. Aldo smiling gently watching the crab, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Hiasan Cangkang Kerang Mutiara",
                    "titleEn": "Pearlescent Shell Decorations",
                    "textId": "Aldo berlari ke garis buih ombak untuk mengumpulkan cangkang kerang putih dan merah muda. Ia menancapkan kerang-kerang berkilau itu di sepanjang puncak dinding benteng dan di tepian parit. Benteng pasir itu kini berkilauan bagai istana raja samudra.",
                    "textEn": "Aldo dashed to the frothy wave line to gather white and pink seashells. He pressed the glistening shells along the ramparts and moat edges. The sandcastle now sparkled like an ocean king's palace.",
                    "quote": "Hiasan alami menambah keanggunan tanpa merusak kesederhanaan.",
                    "coReading": "Warna apa saja cangkang kerang yang dikumpulkan Aldo?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Aldo placing shiny pink and pearl-white clamshells along the top crenellations of the sandcastle. Sparkles reflecting in evening sunlight, naive folk art, bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Bendera Daun Kelapa",
                    "titleEn": "Coconut Leaf Banner",
                    "textId": "Sebagai mahkota terakhir, Aldo menancapkan sebatang lidi berdaun kelapa hijau muda di menara tertinggi. Daun itu berkibar gagah tertiup angin pantai. 'Benteng Samudra telah berdiri tegak!' seru Aldo melompat gembira.",
                    "textEn": "As the final crown, Aldo planted a stick with a green coconut leaflet atop the highest tower. The leaflet fluttered proudly in the coastal breeze. 'The Ocean Fortress stands tall!' Aldo cheered, leaping with joy.",
                    "quote": "Kemenangan berkreasi adalah kepuasan saat melihat impian terwujud.",
                    "coReading": "Benda apa yang dijadikan bendera oleh Aldo?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. The magnificent sandcastle completed with four towers, seashell ramparts, a circular moat, and a fluttering green leaf flag on top. Aldo standing with hands on hips, beaming with joy, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Buih Ombak Pasang Senja",
                    "titleEn": "Foamy Waves of the Evening Tide",
                    "textId": "Matahari mulai menyentuh garis cakrawala laut. Air pasang senja perlahan merayap naik ke pantai. Gulungan ombak kecil berdesir membawa buih putih yang meluncur masuk dan mengisi parit benteng Aldo dengan air laut yang jernih.",
                    "textEn": "The sun touched the ocean horizon line. The evening high tide crept slowly up the shore. A rolling gentle wave hissed white seafoam that surged forward, filling Aldo's moat with clear ocean water.",
                    "quote": "Siklus alam berjalan dengan keindahan alaminya sendiri.",
                    "coReading": "Apakah air ombak mulai mendekati benteng pasir Aldo?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Gentle foamy ocean wave washing up the sand, water filling the moat around the sandcastle. Warm sunset sky in shades of peach and lavender, simple bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Mencair Kembali Menjadi Pantai",
                    "titleEn": "Melting Back into the Shore",
                    "textId": "Ombak berikutnya datang lebih tinggi, menyentuh kaki benteng. Dinding pasir perlahan luruh dengan lembut, mencair kembali menjadi pasir pantai yang rata. Aldo tidak menangis; ia tersenyum melambaikan tangan pada bentengnya. 'Terima kasih sudah menemaniku bermain sore ini,' bisik Aldo.",
                    "textEn": "The next wave rose higher, kissing the castle's base. The sand walls gently dissolved, melting softly back into the smooth beach. Aldo didn't cry; he smiled, waving goodbye to his castle. 'Thank you for playing with me this afternoon,' Aldo whispered.",
                    "quote": "Keindahan sejati ada pada kegembiraan saat menciptakannya, bukan keabadiannya.",
                    "coReading": "Mengapa Aldo tidak bersedih saat benteng pasirnya disapu ombak?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. The sandcastle gently smoothing into the rising tide water under sunset rays. Aldo standing with his father by the shore, waving affectionately at the water with a peaceful smile, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Tidur Nyenyak Berlantun Ombak",
                    "titleEn": "Sound Sleep to the Ocean's Lullaby",
                    "textId": "Malam tiba dan angin laut bertiup sejuk menembus kisi-kisi jendela pondok nelayan. Di atas meja kamarnya, tersimpan tiga cangkang kerang mutiara yang dibawa pulang dari pantai. Aldo tidur pulas, bermimpi membangun seribu benteng pasir megah di hari esok yang cerah.",
                    "textEn": "Night fell and the cool sea breeze rustled through the fisherman cottage window slats. On his bedside table rested three pearlescent seashells brought home from the shore. Aldo slept deeply, dreaming of building a thousand grand sandcastles under tomorrow's sunny skies.",
                    "quote": "Tidurlah dalam damai, laut selalu menjaga kenangan manis petualanganmu.",
                    "coReading": "Selamat tidur anak pantai yang tangguh, biarkan laut mendamaikan mimpimu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Aldo sleeping peacefully in bed with a woven blue blanket, with three shiny seashells resting on his wooden nightstand. Window overlooking the calm moonlit sea and starry sky. Serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        },

        # --- STORY 82: Selendang Sutra Penari Angin ---
        {
            "id": "story82",
            "storyNumber": 82,
            "title": "Selendang Sutra Penari Angin",
            "englishTitle": "Silk Scarf Dancer of the Wind",
            "category": "creativity",
            "categoryLabel": "🎨 Seni & Kreativitas",
            "ageGroup": "Usia 3–6 Tahun",
            "moralTheme": "Kebebasan berekspresi, gerak tubuh yang gembira, & harmoni alam",
            "cover": "covers/story82_cover.jpg",
            "synopsis": "Di puncak bukit padang ilalang yang berangin semilir, Kirana membentangkan selendang sutra kuning keemasan milik Ibunya. Bersama hembusan angin dan tarian kupu-kupu padang, Kirana menari bebas mengikuti irama alam yang menenangkan jiwa.",
            "protagonist": "Kirana (Gadis cilik berselendang kuning melambai)",
            "companion": "Kupu-kupu (Kupu-kupu terbang beriringan)",
            "setting": "Puncak Bukit Angin",
            "pages": [
                {
                    "number": 1,
                    "title": "Bukit Ilalang yang Melambai",
                    "titleEn": "The Swaying Hill of Reeds",
                    "textId": "Di puncak bukit berumput hijau, bunga-bunga ilalang putih melambai serentak mengikuti irama angin sore. Udara terasa sejuk dan harum embun pegunungan. Kirana, gadis cilik bergaun katun putih, melangkah riang menaiki undakan tanah bukit sambil memegang bungkusan kain sutra di dadanya.",
                    "textEn": "Atop the green grassy hill, white reed plumes swayed together in rhythm with the evening breeze. The air felt cool and fragrant with mountain dew. Kirana, a little girl in a white cotton dress, trotted happily up the earthen hillside steps, holding a bundle of silk against her chest.",
                    "quote": "Puncak bukit yang tinggi memberi ruang lapang bagi jiwa untuk bernapas lega.",
                    "coReading": "Pernahkah kamu berdiri di atas bukit yang banyak anginnya?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream watercolor paper. Kirana, a graceful young girl with braided dark hair in a simple white cotton dress, walking up a lush grassy hill filled with swaying white reeds. Golden afternoon sun, simple black bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 2,
                    "title": "Sutra Kuning Selembut Awan",
                    "titleEn": "Yellow Silk as Soft as Cloud",
                    "textId": "Kirana membuka lipatan kain itu. Itu adalah selendang sutra tipis berwarna kuning bunga matahari milik Ibu. Kain itu begitu ringan sehingga saat Kirana mengangkatnya sedikit saja, kain itu langsung melayang seperti helai awan yang menari.",
                    "textEn": "Kirana unfolded the cloth. It was Mother's gossamer silk scarf in sunflower yellow. The fabric was so featherlight that when Kirana lifted it gently, it floated instantly like a dancing cloud drift.",
                    "quote": "Kelembutan memiliki keindahan yang mampu terbang melintasi angkasa.",
                    "coReading": "Bagaimana rasanya memegang kain sutra yang sangat halus?",
                    "imagePrompt": "Wax crayon scribbles on heavy paper. Kirana unfurling a long, translucent golden-yellow silk scarf that billows lightly in the mountain wind. Green hilltop landscape, sunny sky, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 3,
                    "title": "Hembusan Angin Pertama",
                    "titleEn": "The First Breath of Breeze",
                    "textId": "Semilir angin lembah berhembus lembut menyapa pipi Kirana. Kirana merentangkan kedua tangannya lebar-lebar. Selendang sutra kuning itu melambai ke belakang tubuhnya seperti sepasang sayap burung kepodang emas yang siap mengarungi langit.",
                    "textEn": "A gentle valley breeze caressed Kirana's cheeks. Kirana stretched both arms wide open. The yellow silk scarf rippled behind her like the wings of a golden oriole ready to soar across the sky.",
                    "quote": "Menyambut angin adalah awal dari keberanian untuk mengekspresikan diri.",
                    "coReading": "Bisakah kamu merentangkan kedua tanganmu seperti sayap burung?",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Kirana with arms outstretched holding the edges of the long yellow silk scarf, which flutters majestically behind her like golden wings. Rolling hills in background, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 4,
                    "title": "Putaran Kaki di Atas Rumput",
                    "titleEn": "A Spin on the Grass",
                    "textId": "Kirana menjinjitkan kakinya dan berputar perlahan: satu putaran, dua putaran. Selendang kuningnya melingkari tubuhnya membentuk pusaran keemasan yang berkilau di bawah sinar matahari senja. Ujung gaun putihnya ikut mengembang manis.",
                    "textEn": "Kirana rose on her tiptoes and spun slowly: one turn, two turns. Her yellow scarf wound around her body in a shimmering golden spiral under the evening sun. The hem of her white dress flared sweetly alongside it.",
                    "quote": "Gerak tubuh yang gembira memancarkan cahaya kebahagiaan dari dalam hati.",
                    "coReading": "Coba berputar perlahan seperti Kirana menari di atas rumput!",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Kirana twirling on one foot on the grassy meadow, the golden silk swirling in a dynamic spiral around her. Swirling motion lines, dandelion seeds in the air, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 5,
                    "title": "Kawan-Kawan Bersayap Kuning",
                    "titleEn": "Yellow-Winged Companions",
                    "textId": "Melihat kibasan kain kuning yang menawan, tiga ekor kupu-kupu belerang berwarna kuning cerah terbang mendekat. Mereka meliuk-liuk di udara, menari mengitari ujung selendang Kirana seolah mengira itu adalah kelopak bunga raksasa yang mekar.",
                    "textEn": "Seeing the lovely yellow ripples, three bright yellow sulfur butterflies fluttered close. They danced through the air, circling the tips of Kirana's scarf as if mistaking it for a giant blooming flower petal.",
                    "quote": "Keindahan yang alami selalu menarik kebaikan dari alam sekitar.",
                    "coReading": "Kupu-kupu apa yang ikut menari bersama Kirana?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Three cute yellow butterflies fluttering merrily around Kirana's swirling yellow scarf. Kirana laughing in pure delight, bead dot eyes, sunny open sky, text-free, 4:3 horizontal."
                },
                {
                    "number": 6,
                    "title": "Melompat Melompati Bayangan",
                    "titleEn": "Leaping Over Shadows",
                    "textId": "Kirana melompat ringan melompati bebatuan bukit. Setiap lompatannya diikuti oleh ombak kain sutra yang melayang tinggi di udara. Kirana merasa tubuhnya seringan kapas, bebas dari segala rasa lelah dan beban.",
                    "textEn": "Kirana leapt lightly over hill pebbles. Every jump was followed by waves of silk floating high in the sky. Kirana felt as light as a dandelion seed, free from every fatigue and heavy thought.",
                    "quote": "Ketika kita menari dengan tulus, jiwa kita terbang bebas menembus batas.",
                    "coReading": "Bisakah kamu melompat seringan Kirana melompati rumput?",
                    "imagePrompt": "Wax crayon scribbles on heavy textured paper. Kirana leaping joyfully across the grassy hill with the yellow scarf streaming in an arch over her head. Flowing movement, naive folk art, simple bead dot eyes, text-free, 4:3 horizontal landscape."
                },
                {
                    "number": 7,
                    "title": "Senandung Tanpa Kata-Kata",
                    "titleEn": "Humming Without Words",
                    "textId": "Dari bibir Kirana mengalun senandung merdu tanpa kata-kata, hanya nada-nada lembut yang mengikuti hembusan angin. Burung-burung pipit di semak-semak berhenti berkicau sejenak, mendengarkan senandung manis penari cilik itu.",
                    "textEn": "From Kirana's lips flowed a sweet wordless humming, just gentle melodies dancing with the wind. The little finches in the bushes paused their chirping, listening to the sweet hum of the little dancer.",
                    "quote": "Musik yang paling tulus lahir langsung dari dalam kedamaian dada.",
                    "coReading": "Coba bersenandung pelan sebuah nada yang menenangkan hatimu.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel. Close-up of Kirana smiling with closed eyes, head tilted gently in the breeze, holding the silk scarf to her cheek. Little birds perched on fence posts listening, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 8,
                    "title": "Warna Lembayung di Puncak Bukit",
                    "titleEn": "Violet Glow on the Hilltop",
                    "textId": "Langit barat perlahan berubah warna menjadi perpaduan ungu lembayung dan jingga kemerahan. Kirana memperlambat tariannya. Selendang kuningnya kini melambai tenang, menyerap cahaya senja yang damai seperti api unggun yang mulai mereda.",
                    "textEn": "The western sky slowly shifted into a blend of soft lavender and reddish orange. Kirana slowed her dance. Her yellow scarf now waved gently, drinking in the peaceful twilight glow like a softly settling ember.",
                    "quote": "Segala keindahan yang bergerak selalu menemukan waktu untuk kembali hening.",
                    "coReading": "Warna apa yang tampak di langit saat matahari mulai tenggelam?",
                    "imagePrompt": "Soft oil pastel smudges on heavy cream paper. Kirana standing serenely at the edge of the hill with the yellow scarf draped gracefully over her arms, silhouetted against a breathtaking twilight sky of lilac, peach, and gold, bead dot eyes, text-free, 4:3 horizontal."
                },
                {
                    "number": 9,
                    "title": "Melipat Selendang dengan Penuh Cinta",
                    "titleEn": "Folding the Scarf with Love",
                    "textId": "Sebelum gelap turun, Kirana melipat selendang sutra kuningnya dengan rapi di atas pangkuannya. Ia mencium kain itu yang kini beraroma semilir angin bukit dan wangi bunga ilalang. 'Terima kasih, sahabat setiaku,' bisik Kirana tersenyum.",
                    "textEn": "Before the dark descended, Kirana neatly folded the yellow silk scarf on her lap. She kissed the cloth, which now smelled of hill breezes and wild reed blossoms. 'Thank you, my faithful friend,' Kirana whispered with a smile.",
                    "quote": "Menghargai benda yang menemani kegembiraan kita adalah tanda rasa syukur.",
                    "coReading": "Bagaimana aroma kain selendang Kirana setelah menari di bukit?",
                    "imagePrompt": "Handcrafted wax crayon on textured cream paper. Kirana sitting on a hill stone neatly folding the yellow silk scarf. Mother waiting on the path below with a warm lantern, smiling up, bead dot eyes, 4 limbs constraint, text-free, 4:3 horizontal."
                },
                {
                    "number": 10,
                    "title": "Lelap Berselimut Sutra Emas",
                    "titleEn": "Deep Slumber Beneath Golden Silk",
                    "textId": "Di rumahnya yang hangat di kaki bukit, Kirana tidur lelap di bawah selimut katunnya, dengan selendang kuning sutra diletakkan manis di samping bantalnya. Dalam lelapnya yang damai, ia bermimpi menari di atas awan-awan perak di bawah tatapan bintang malam.",
                    "textEn": "In her cozy home at the foot of the hill, Kirana slept deeply beneath her cotton quilt, with the yellow silk scarf resting sweetly beside her pillow. In her peaceful sleep, she dreamed of dancing on silver clouds under the gaze of night stars.",
                    "quote": "Tidurlah dalam tarian mimpi yang indah, hatimu selalu bebas dan bahagia.",
                    "coReading": "Selamat tidur anak penari, biarkan mimpimu menari bersama bintang-bintang.",
                    "imagePrompt": "Handcrafted wax crayon and oil pastel on heavy cream watercolor paper. Kirana sleeping serenely in bed with the folded golden scarf on her bedside chair. Moonlight streaming through the window, crescent moon and twinkling stars outside. Serene bedtime mood, text-free, 4:3 horizontal."
                }
            ]
        }
    ]
    return stories
