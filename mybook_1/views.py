# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
#
# def first_1(request):
#     html = """
#     <h1>first page</h1>
#     <h2>Asosiy bo'lim xush kelibsiz.</h2>
#     <a href="secound">  secound page >> </a><br>
#     <a href="book_pages/Quronni karim"> Quronni karim kitobi page >> </a> <br>
#     <a href="book_pages/Iymon sari qadam kitobi">Iymon sari qadam kitobi  page >> </a> <br>
#     <a href="book_pages/Mohiramazon kitobi"> Mohiramazon kitobi page >> </a> <br>
#     <a href="book_pages/Ramazon taqvimi kitobi"> Ramazon taqvimi kitobi page >> </a> <br>
#     <a href="book_pages/Tajvid qoidalar kitobi"> Tajvid qoidalar kitobi page >> </a> <br>
#     <a href="book_pages/Iymon sari qadam"> Iymon sari qadam kitobi page >> </a> <br>
#     <a href="book_pages/Umar ibni xattob kitobi"> Umar ibni xattob kitobi page >> </a> <br>
#     <a href="book_pages/Saodat asri kitobi"> Saodat asri kitobi page >> </a> <br>
#     <a href="book_pages/'Otgan knunlar kitobi"> 'Otgan knunlar kitobi page >> </a> <br>
#     <a href="nook_pages/Allohni mo'jizalari kitobi"> Allohni mo'jizalari kitobi page >> </a>
#     """
#     return HttpResponse(html)
#
# def secound(request):
#     html = """
#     <h1>first page</h1>
#     <h2>Ikkinchi bo'lim </h2>
#     <a href="../">, << first page </a>
#     """
#     return HttpResponse(html)
#
#
# def book_pages(request, page):
#     if page == 'Quronni karim':#1
#         html = f"""
#         <h1>{page} bo'limi:</h1>
#         <p>Qur’oni karim – Аlloh tarafidan 23 yilga yaqin muddat mobaynida Muhammad paygʼambarga (a.s.) Jabroil farishta (a.s.) orqali baʼzan oyat–oyat, baʼzan esa toʼliq sura tarzida nozil qilingan ilohiy kitobdir. Bu kitob islom dinining muqaddas manbasi hisoblanadi.  </p>
#         <a href="../"><< main page </a>
#         """
#
#     elif page == 'Iymon sari qadam kitobi':#2
#         html = f"""
#            <h1>{page} bo'limi: </h1>
#            <p>Ushbu kitob 1991-yil ilk bor nashrdan chiqqan bo'lib, kitobxonlar tomonidan qizg'in kutib olingan. Bunga sabab o'sha davrda yurtimizda islom diniga qarshi harakatlar ta'sirida ko'plab insonlarning islom haqida to'g'ri tushunchaga ega bo'lmagani va islom haqida bilim olishga bo'lgan ishtiyoqdir. Iymon kitobiga hozirgi kunda ham ko'plab taklif va ehtiyoj bo'lganligi sababli 2021-yil yana qayta nashrdan chiqarildi.
#
# Ushbu kitobda islom diniga qarshi otilgan bo'xtonlarga diniy, ilmiy va dunyoviy tomondan go'zal javoblar, Yagona Allohga e'tiqod qilishga oid g'arb olimlarining fikrlari, islomdagi ayollar va erkaklar teng huquqliligi to'grisidagi ma'lumotlar, farishtalarga, qiyomat kuniga va payg'ambarlarga iymon keltirish va boshqa ko'plab masalalar haqida ma'lumotlar keltirilib o'tilgan.
#
# Manbalar
# https://hilolnashr.uz/iymon
#
#            </p>
#            <a href="../">,<< main page </a>
# """
#
#     elif page == 'Mohiramazon kitobi':#3
#         html=f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Бу китоб ўзи бежиримгина бўлишига қарамай, жуда кўп мавзуларни қамраб олган. Жумладан, Рамазон ойининг фазилатлари, бу ойда эътикоф ўтиришнинг аҳамияти, рўзадорга бериладиган мукофотлар, минг ойдан яхши бўлган Қадр кечасидаги ибодатлар, хатми Қуръонга тарғиб, фитр садақаси, фидя масалалари, таровеҳ намозининг фазилатлари каби мавзулар қисқа ва лўнда жумлалар орқали ёритиб берилган. Айниқса рисоладан ўрин олган Рамазон кечаларида ўқиладиган набавий дуоларни, қалбларга ором бағишловчи тасбеҳларни ёд олиб, тилимизга ва дилимизга жо қилсак, албатта, икки дунёмиз учун фойдали бўлажак.
#         </p>
#         <a href="../">,<< main page </a>
#
# """
#     elif page == 'Ramazon taqvimi kitobi':#4
#         html=f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Ramazon (arabcha: رَمَضَان , Ramaḍān) Islom taqvimining to'qqizinchi oyi bo'lib, Islom dini payg'ambari Muhammad (s.a.v) ga Qur'onda nozil qilingan deb ishoniladi .
#
# Ramazon oyida ro'za tutish Islomning besh arkonidan biridir. Ramazon oyini musulmonlar kunduzi tongdan quyosh botguncha ro'za tutishadi. Islomga ko'ra, Qur'on bu oyda osmondan yerga tushirilgan va shu tariqa Jabroil tomonidan Muhammad(s.a.v)ga asta-sekin vahiy qilish uchun tayyorlangan. Shuning uchun Muhammad (s.a.v)o'z izdoshlariga jannat eshiklari butun oy davomida ochiq bo'lishini va do'zax ( Jahannam ) eshiklari yopilishini aytgan. Keyingi oyning birinchi uch kuni Shavvol bayrami nishonlanadi va "Iftar bayrami" yoki Iyd al-Fitr sifatida nishonlanadi.  </p>
#         <a href="../"><< main page </a>
# """
#
#     elif page == 'Tajvid qoidalar kitobi':#5
#         html=f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Tajvid ilmini o‘rganibgina Qurʼoni karimni Alloh taolo payg‘ambarimiz Muhammad sollallohu alayhi vasallamga nozil qilganidek har bir harfiga maxraj, sifat, g‘unna, mad va boshqalardan haqqini berib tilovat qila olamiz.
#
# Tajvid ilmiga bag‘ishlangan bu kitobcha savol-javob shaklida bo‘lib, unda faqat boshlang‘ich maʼlumotlar taqdim etilgan. Kerakli o‘rinda arab harflarini talaffuz qilishda yordamchi o‘laroq rangli suratlar va Musʼhafi sharifda ishlatilgan vaqf va boshqa alomatlar uchun izohlar berilgan. O‘quvchi tajvid qoidalariga muvofiq holda bo‘yalgan Musʼhafi sharifni tilovat qilishi oson bo‘lishi uchun kitobcha xotimasida maxsus qo‘llanma ilova qilingan. </p>
#         <a href="../">,<< main page </a>
# """
#
#     elif page == 'Iymon sari qadam':#6
#         html=f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Allohning borligiga eng ulkan dalillardan biri galaktikamizdir. O‘zimiz yashab turgan Yer va uning atrofidagi son-sanoqsiz yulduzlar haqida fikr yuritib, o‘ylab ko‘rsak, kishini hayratga soladigan darajada ajoyibotlarni ko‘ramiz. Ularga insof bilan nazar solgan kishining qalbida yaratuvchining ulug‘ligiga bo‘lgan iymon-ishonch ziyoda bo‘lmasdan iloji yo‘q. Qurʼoni Karimdagi ko‘pgina oyatlar ham insonni mana shu borliqning yaratilishiga, osmonu yerga nazar solib, fikr yuritishga va ularning sirlarini bilib, o‘zining iymonini baquvvat qilib, shak-shubhalarini o‘zidan yiroqlashtirishga chaqiradi.  </p>
#         <a href="../">,<< main page </a>
# """
#
#     elif page == 'Umar ibni xattob kitobi':#7
#         html=f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Умар ибн Хаттоб иккинчи рашид ҳалифа бўлиб, ислом динини ер юзига ёйиш мақсадида Расулуллоҳ (с.а.в) томонларидан олиб борилган тавхидий курашда ул зоти шарифга энг эқин бўлган саҳобалардан бири ҳисобланади. Ҳазрат Умар р.а. машҳур Фил воқеасидан ўн уч йил кейин Маккада дунёга келган. Ҳазрат Умар р.а.нинг ўзидан нақл қилинган бир ривоятга кўра, Катта Фижор жангидан тўрт йил кейин дунёга келган. Отаси Ҳаттоб ибн Нуфайл бўлиб, насаби Каъбда Расулуллоҳ (с.а.в)нинг насаблари билан бирлашади. Қурайшнинг Одий қабиласига мансуб бўлиб, онаси Абу Жаҳлнинг синглиси ёки амакиваччаси бўлган Хантамадир. Ислом манбаларида Хазрат Умар р.а.нинг мусулмон бўлишидан олдинги хаёти ҳақида кўп маълумот келтирилмаган. Фақатгина болалик пайти отасига тегишли бўлган сурувга чўпонлик қилгани, кейинчалик эса тижорат қилгани ҳақидаги маълумотларни учратишимиз мумкин. У Сурия томонларга борадиган тижорат карвонларида иштирок этарди. Жоҳилия даврида Қурайшнинг обрўли кишиларидан бўлиб, Макка шаҳрининг элчилик вазифаси унинг қўлида эди. Агар бирор қабила билан Қурайш ўртасида жанг чиқиш эҳтимоли юзага келса, қарши томонга элчи сифатида Умар жўнатилар ва қайтишда у келтирган маълумот ва унинг фикрига кўра ҳаракат қилинар эди. Умар қабилалар ўртасидаги турли англашилмовчиликларнинг олдини олишга ва қабилалар орасидаги адоватни кўтариб, бир бирлари билан яраштириб, ўртадаги вазиятни қўлдан келганча тинч йўл билан ҳал этишга ҳаракат қиларди.  </p>
#         <a href="../">,<< main page </a>
# """
#
#     elif page == 'Saodat asri kitobi':#8
#         html=f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Аhmad Lutfiy hozirgi zamon adibi, tarixchi olim. Biz eʼtiboringizga havola etayotgai «Saodat asri qissalari» kitobi Saodat asridan hikoya qiluvchi asardir. Kitob toʼla holida Janobi Paygʼambarimiz alayhissalomning tugʼilishlaridan to vafotlariga qadar muborak hayotlarini kamrab oladi. Xuddi shu mavzuga bagʼishlangan boshqa asarlardan farqi muallif aniq tarixiy voqea-hodisalarni oʼziga xos badiiy yoʼsinda aks ettirganidir. Natijada u gʼoyat oʼqishli chiqqan. Bu kitoblarning mashhur boʼlib ketganini shundan ham bilsa boʼladiki, asar toʼrt marta nashr kilingandir. Inshaalloh, sizlarga ham yoqadi, degan umiddamiz.  </p>
#         <a href="../">,<< main page </a>
# """
#
#     elif page == "'Otgan knunlar kitobi":  #9
#         html = f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Oʻtkan kunlar, baʼzi manbalarda Oʻtgan kunlar – oʻzbek yozuvchisi Abdulla Qodiriy qalamiga mansub oʻzbek adabiyotidagi ilk roman[1]. 1969-yil „Oʻzbekfilm“ kinostudiyasida ushbu roman asosida „Oʻtgan kunlar“ nomli film suratga olingan. Adib romanni yozishda arab yozuvchisi Jurji Zaydon asarlaridan ilhomlangan[2]. Roman 1920-yillar boshida yozilgan boʻlib, 1922-yil ilk bor „Inqilob“ jurnalida chop etilgan va 1926-yilda alohida kitob holida nashr etilgan[3].  </p>
#         <a href="../">,<< main page </a>
# """
#
#     elif page == "Allohni mo'jizalari kitobi":  # 10
#         html = f"""
#         <h1> {page} bo'lim:</h1>
#         <p>Мазкур китобда Қуръондаги математик, физик, тиббий, астрономик ва бошқа мўъжизалар тўғрисида баҳс юритилади. Муаллиф ушбу асари орқали мусулмон киши шак-шубҳасиз билиши шарт бўлган Қуръоннинг ҳақиқий сир-асрорларини намоён этишга ва шу орқали унинг илоҳий калом эканини ўқувчига чин маънода ҳис эттиришга интилади.
#
#         </p>
#         <a href="../">,<< main page </a>
# """
#
#     else:
#         html = f"""
#            <h1>{page} siz kitob tanlamadingiz!!!</h1>
#            """
#
#     return HttpResponse(html)