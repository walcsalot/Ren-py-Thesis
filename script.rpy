    # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define father = Character("Ama", color="#c8ffc8")
define mother = Character("Ina", color="#ffc8c8")
define lola = Character("Lola Rosa", color="#ffc8ff")
define miguel = Character("Miguel", color="#c8c8ff")
define ana = Character("Ana", color="#c8ffff")
define maria = Character("Maria", color="#ffffc8")
define pedro = Character("Pedro", color="#c8ffff")
define guro = Character("Guro", color="#ffcc99")

# Filipino Story
label scenario1:
    $ moral_score = 0

    scene bg home_day
    with fade

    "Sa maliit na bayan ng San Isidro, nakatira ang pamilya Santos sa isang simpleng tahanan."
    "Sila ay binubuo nina Juan (ama), Maria (ina), Miguel (14 na taong gulang), Ana (12 na taong gulang), at Lola Rosa."

    show father at center
    father "Mga anak, ang buhay ay puno ng hamon, ngunit ang pamilyang nagmamahalan ay kayang lampasan ang anumang pagsubok."

    show mother at right
    mother "Tandaan ninyo, ang kayamanan ay hindi nasusukat sa pera kundi sa pagmamahal at respeto sa isa't isa."

    show lola at left
    lola "At huwag ninyong kalilimutan ang pananampalataya sa Diyos. Siya ang ating gabay sa lahat ng pagsubok."

    "Ang Pamilya Santos ay kilala sa kanilang kabutihan at pagtutulungan sa kanilang maliit na komunidad."
    "Bagamat hindi sila mayaman, puno ng pagmamahal at mga aral sa buhay ang kanilang tahanan."

    jump act1

# ------------------ ACT 1: ANG UMAGA ------------------
label act1:
    scene bg home_morning
    with fade

    "Maagang umaga sa tahanan ng mga Santos. Ang araw ay nagsisimula na at may mga gawaing naghihintay."

    show miguel at center
    miguel "Naku, alas-sais na pala ng umaga! Muntik na akong mahuli sa paggising."

    menu:
        "Umaga na. Ano ang gagawin ni Miguel?"
        
        "Bumangon nang maaga at tumulong sa mga gawaing bahay":
            $ moral_score += 1
            miguel "Tutulungan ko si Nanay sa paghahanda ng almusal. Mahalaga ang pagtulong sa pamilya."
            "Tumulong si Miguel sa paghahanda ng pagkain at pag-aayos ng bahay. Ikinatuwa ito ng kanyang mga magulang."
            
        "Magpahinga pa at ipagpaliban ang pagtulong":
            $ moral_score -= 1
            miguel "Limang minuto pa... antok na antok pa ako."
            "Natulog pa si Miguel at nahuli sa pagtulong sa mga gawaing bahay. Ikinagalit ito ng kanyang ama."

    "Pagkatapos ng almusal, naghanda na si Ana para pumasok sa eskwelahan."

    show ana at right
    ana "Paalam po! Mag-iingat po kayo."

    jump act2

# ------------------ ACT 2: PAGKAKAMALI NI MIGUEL ------------------
label act2:
    scene bg playground
    with fade

    "Pagkatapos ng klase, naglaro si Miguel at ang kanyang mga kaibigan sa palaruan."

    show miguel at left
    miguel "Tara, laruin natin ang bagong laruan ni Pedro!"

    "Masayang naglaro ang mga bata hanggang sa may nangyari ng di inaasahan."

    "*CRACK*"

    show pedro at right
    pedro "Naku! Ang laruan ko! Nabasag!"

    "Aksidenteng nabasag ni Miguel ang mamahaling laruan na regalo kay Pedro sa kanyang kaarawan."

    menu:
        "Ano ang gagawin ni Miguel?"
        
        "Itago at itanggi ang pagkakamali":
            $ moral_score -= 1
            miguel "Hindi ko sinasadya... baka hindi niya malaman na ako ang may gawa."
            "Itinago ni Miguel ang totoo, ngunit siya ay nabagabag at hindi makatulog sa gabi."
            "Nakaramdam ng guilt at takot na malaman ang katotohanan."
            
        "Umamin at humingi ng tawad nang taos-puso":
            $ moral_score += 1
            miguel "Pedro, ako ang nakabasag. Pasensya na talaga. Hahanap ako ng paraan para mapagawa ito."
            "Bagamat nalungkot si Pedro, hinangaan niya ang katapatan ni Miguel."
            "Nagkasundo silang ayusin ang laruan at naging mas matibay ang kanilang pagkakaibigan."

    jump act3

# ------------------ ACT 3: PAGSUBOK SA TRABAHO ------------------
label act3:
    scene bg home_evening
    with fade

    "Isang linggo ang lumipas, may mas malaking pagsubok ang dumating sa pamilya Santos."

    show father at center with dissolve
    father "Maria, may masama akong balita. Nawalan ako ng trabaho sa pabrika."

    show mother at right with dissolve
    mother "Ano? Paano na tayo? Paano na ang mga anak natin?"

    "Biglang bumigat ang kapaligiran sa maliit nilang tahanan. Ang kita ni Juan ang pangunahing pinagkukunan ng pamilya."

    show lola at left with dissolve
    lola "Huwag kayong mawalan ng pag-asa. Sa lahat ng unos, ang pananampalataya at pagtutulungan ang ating sandigan."

    menu:
        "Paano tutugon ang pamilya sa pagsubok na ito?"
        
        "Magreklamo at magsisihan":
            $ moral_score -= 1
            father "Bakit palaging ganito ang buhay? Hindi ko na alam ang gagawin!"
            mother "Wala na tayong pera para sa pagkain at upa! Paano na ang mga bata?"
            "Nagaway ang mag-asawa at lumala ang tensyon sa bahay. Nadama ng mga bata ang bigat ng problema."
            
        "Magkaisa at humanap ng solusyon nang magkasama":
            $ moral_score += 1
            father "Laban tayo! Maghahanap ako ng bagong trabaho. Samantala, magtipid tayo."
            mother "Tama ka. Magtutulong-tulong tayo. Ako'y magluluto ng mga pagkaing pwedeng ibenta."
            "Nagkaisa ang pamilya at naghanap ng mga paraan para makaraos sa kahirapan."

    jump act4

# ------------------ ACT 4: MGA TUksO ------------------
label act4:
    scene bg street
    with fade

    "Dahil sa kahirapan, naging vulnerable si Miguel sa mga tukso."

    "Isang araw, inaya siya ng mga batang lansangan na magnakaw sa malaking tindahan."

    show miguel at center
    miguel "Hindi, ayaw ko. Mali ang magnakaw."

    "Ngunit patuloy silang nambubuyo..."

    menu:
        "Ano ang gagawin ni Miguel?"
        
        "Sumama at magnakaw para may maibigay sa pamilya":
            $ moral_score -= 2
            miguel "Siguro... kailangan naming kumain. Baka makatulong ito."
            "Sumama si Miguel, ngunit nahuli sila ng guwardiya. Dinala sila sa pulisya at napahiya ang buong pamilya."
            
        "Tumanggi at manindigan sa tama":
            $ moral_score += 1
            miguel "Hindi ko ito gagawin! Kahit gaano kami kahirap, hindi magnanakaw ang pamilya namin!"
            "Umalis si Miguel at imbes na magnakaw, naghanap siya ng mga parol na pwede niyang gawin at ibenta."

    "Samantala, may nag-alok kay Juan ng trabaho..."

    show father at center
    father "May nag-alok sa akin ng trabaho. Malaki ang sahod, ngunit ilegal ang gagawin."

    menu:
        "Ano ang gagawin ni Juan?"
        
        "Tanggapin ang ilegal na trabaho para sa pamilya":
            $ moral_score -= 2
            father "Kahit paano, may pagkain na sa mesa. Wala na akong choice."
            "Ngunit nagdulot ito ng pangamba at kahihiyan sa pamilya. Lalong naging mahirap ang sitwasyon."
            
        "Tanggihan at manatiling tapat sa prinsipyo":
            $ moral_score += 1
            father "Hindi ko ipagpapalit ang dangal ng pamilya sa pera. May ibang paraan."
            "Bagamat naghirap sila nang sandali, nanatili ang kanilang dignidad at respeto ng komunidad."

    jump act5

# ------------------ ACT 5: ANG BAGYO ------------------
label act5:
    scene bg storm
    with fade

    "Habang patuloy na humaharap sa pagsubok ang pamilya, dumating ang mas malaking hamon."

    "Isang malakas na bagyo ang tumama sa kanilang bayan. Malakas ang ulan at hangin."

    show mother at right
    mother "Naku! Bumabaha na! Kailangan nating lumikas!"

    "Biglang may narinig silang sigaw mula sa kapitbahay."

    "TULONG! NASUSUNOG ANG BAHAY NAMIN! MAY NASA LOOB PA!"

    menu:
        "Ano ang gagawin ng pamilya?"
        
        "Tumulong sa kapitbahay kahit may panganib":
            $ moral_score += 1
            father "Juan, samahan mo akong tumulong! Maria, ilikas mo ang mga bata!"
            "Tumulong ang pamilya Santos sa pagliligtas ng kanilang kapitbahay. Nakaligtas ang buong pamilya mula sa nasusunog na bahay."
            
        "Iligtas lamang ang sarili at ang kanilang gamit":
            $ moral_score -= 1
            father "Unahin natin ang sarili natin! Hindi tayo puwedeng magpanganib!"
            "Nakaligtas ang pamilya Santos, ngunit nasunog ang bahay ng kapitbahay at may nasugatan."

    "Pagkatapos ng bagyo, may isa pang mahalagang pagpapasya si Ana."

    show ana at center
    ana "May scholarship exam ako bukas. Makakapag-aral ako nang libre kung papasa ako."
    ana "Ngunit kailangan ng pamilya ng tulong ko sa pag-aayos ng bahay at paghahanap-buhay."

    menu:
        "Desisyon ni Ana"
        
        "Tumulong muna sa pamilya at isakripisyo ang exam":
            $ moral_score += 1
            ana "Pamilya muna. Maaari akong sumubok muli sa susunod na taon."
            "Tumulong si Ana sa pamilya at nakahanap ng mga paraan para kumita. Ikinagalak ito ng kanyang mga magulang."
            
        "Magpokus sa pagsusulit at ipagpaliban muna ang pagtulong":
            $ moral_score += 0
            ana "Kailangan kong magsikap para sa pamilya. Ang edukasyon ang sagot sa aming kahirapan."
            "Nag-aral si Ana at pumasa sa exam. Nakatulong ito sa kanila sa pangmatagalan."

    jump filipino_ending

# ------------------ MGA WAKAS ------------------
label filipino_ending:
    if moral_score <= -2:
        jump bad_ending
    elif moral_score in [-1, 0, 1]:
        jump neutral_ending
    elif moral_score >= 2:
        jump good_ending

label bad_ending:
    scene bg home_dark
    with fade
    "Dahil sa mga maling desisyon, unti-unting nagkawatak-watak ang pamilyang Santos."
    "Ang kawalan ng respeto, pananampalataya, at pagtutulungan ay nagpatunay na ang mga maling pagpili ay nagdudulot ng kapahamakan."
    "Nawala ang init at pagmamahalan sa kanilang tahanan."
    "Ngunit hindi pa huli ang lahat. May pag-asa pa ring magbago at magsimula muli."
    return

label neutral_ending:
    scene bg home_evening
    with fade
    "Nakaraos ang pamilyang Santos sa mga pagsubok, ngunit may mga sugat na hindi agad gumaling."
    "Natutunan nilang magtulungan at magtiwala sa isa't isa, ngunit may mga pagkakataong nagkakaroon pa rin ng alitan."
    "Patuloy silang nagsusumikap at umaasa na sa hinaharap, mas magiging maayos ang kanilang buhay."
    "Ang kahirapan ay hindi hadlang sa pagmamahalan, ngunit nangangailangan ito ng tibay ng loob at pagtitiis."
    return

label good_ending:
    scene bg home_day
    with fade
    "Sa kabila ng mga pagsubok, lumakas at tumibay ang pamilyang Santos."
    "Ang kanilang pagtitiwala sa isa't isa, pananampalataya sa Diyos, at pagiging matatag sa harap ng hamon ay nagbunga ng magandang kinabukasan."
    "Natuto si Juan at Maria na magnegosyo ng maliit na carinderia, si Miguel ay naging responsable at masunuring anak,"
    "at si Ana ay nakapag-aral nang mabuti at nakatulong sa pamilya."
    "Napatunayan nilang ang tunay na kayamanan ay nasa puso't isipan, hindi sa pera o materyal na bagay."
    "Ang kanilang kuwento ay naging inspirasyon sa buong komunidad."
    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define maestro = Character("Maestro Aurelio", color="#c8ffc8")
define miguel = Character("Miguel", color="#c8c8ff")
define isabel = Character("Isabel", color="#ffc8c8")
define benjo = Character("Benjo", color="#c8ffff")
define carla = Character("Carla", color="#ffcc99")
define liza = Character("Liza", color="#ffffc8")
define diego = Character("Diego", color="#c8c8ff")
define leo = Character("Leo", color="#ffc8ff")

# Initialize moral score
default moral_score = 0

# Ang Hardin ng Pagpapahalaga: Isang Kuwento Para sa Linggo ng Wika
label scenario2:
    scene bg classroom_day
    with fade

    "Pahilis na humigop ang sikat ng araw sa mga bintana ng silid-aralan ni Maestro Aurelio, na nagliliwanag sa mga partikulo ng alikabok na sumasayaw sa hangin."
    "Unang araw iyon ng pagdiriwang ng Linggo ng Wika, at ang buong silid ay buzz ng sabik at kabang pagsasalu-salo."
    "Sa gitna ng lahat ay naroon ang kanilang guro, si Maestro Aurelio, isang lalaking mabait ang mata na naniniwalang ang mga aralin ay lumalawak nang higit pa sa mga textbook."

    show maestro at center
    maestro "Class, ang aming proyekto para sa linggong ito ay hindi simpleng report lamang. Ito ay isang puno."
    maestro "Ang bawat isa sa inyo ay kakatawan sa isang pangunahing pagpapahalaga, isang ugat na nagpapatibay sa ating bansa."
    maestro "Magtutulungan tayong magtayo ng isang 'Hardin ng Pagpapahalaga' para sa ating school fair."

    "Itinakda niya ang mga pagpapahalaga, at ang isang grupo ng pitong magkakaaibigan ay natagpuang magkakadugtong na dahil sa iisang layunin."

    "Si Miguel, isang konsideradong batang laging nakikita ang mabuti sa bawat sitwasyon, ay tinanggap ang Mapagpasalamat."
    "Si Isabel, palaging magalang at maalalahanin, ang sagisag ng Magalang."
    "Si Benjo, ang president ng klase, ang halatang pinili para sa Mapanagutan."
    "Si Carla, na kilala sa kanyang tahimik na lakas ng loob, ang puso ng Pananampalataya."
    "Si Liza, na laging may imaculadong uniporme at organisadong mga note, siya ang Malinis."
    "Si Diego, na may pagmamalaking nagkukuwento tungkol sa kasaysayan at mga bayani ng Pilipinas, siya ang Nasyonalismo."
    "At panghuli, si Leo, ang matalik na kaibigan ni Miguel. Si Leo, na kamakailan lamang ay muling nanirahan sa probinsya pagkatapos ng mga taon sa abroad, ay nahihirapan sa kanyang pagka-Pilipino."

    show leo at left
    show maestro at right
    "Nagulat ang lahat, pati na siya mismo, nang ibigay din sa kanya ni Maestro Aurelio ang Mapagpasalamat."
    maestro "Minsan, kailangan nating matutong makita kung ano ang dapat nating pasalamatan bago tayo tunay na mamukadkad."

    "Ang kanilang gawain ay gumawa ng isang display: isang malaking kahoy na puno kung saan ang bawat pagpapahalaga ay isang dahon, na kasama ng isang maikling kuwento kung paano nila ito isinabuhay."

    jump sc2_act1

# ------------------ ACT 1: MGA PAGPAPAHALAGA ------------------
label sc2_act1:
    scene bg classroom_day
    with fade

    "Nagsimula nang maayos ang linggo."

    show isabel at center
    isabel "Mga kaibigan, magsimula tayo sa pagpaplano. Bawat isa ay magkakaroon ng pagkakataong magsalita."
    "Si Isabel (Magalang) ay nagsaayos ng kanilang mga pagpupulong nang may malinis na paggalang, tinitiyak na ang bawat isa ay nabigyan ng pagkakataong magsalita."

    show benjo at right
    benjo "Gumawa ako ng checklist at timeline. Miguel, ikaw ang bahala sa mga dahon. Liza, ikaw sa mga materyales."
    "Si Benjo (Mapanagutan) ay gumawa ng checklist at timeline, na nagde-delegate ng mga gawain nang patas."

    show liza at left
    liza "Panatilihin nating malinis ang workspace. Magtapon ng basura sa tamang lalagyan."
    "Si Liza (Malinis) ang namahala sa mga kagamitan, pinapanatiling malinis ang kanilang workspace, nangongolekta ng mga scrap, at paalala sa lahat na maglinis."

    show diego at center
    diego "Magandang ideya na gumamit tayo ng mga katutubong materyales—mga dahon ng anahaw para sa puno at banig para sa background."
    "Si Diego (Nasyonalismo) ay nagmungkahi na gumamit sila ng mga katutubong materyales."

    "Subalit may problemang umusbong kay Leo. Siya ay nanlulumo at tahimik."

    show leo at left
    leo "Bakit ko kailangang maging mapagpasalamat? Papasalamat ba ako na umalis ako sa dati kong school? Ni hindi ko nga ramdam na Pilipino ako. Hindi ako makakasulat ng kuwento tungkol dito."

    menu:
        "Ano ang dapat gawin ni Miguel?"
        
        "Hayaan muna si Leo at mag-focus sa sariling gawain":
            $ moral_score -= 1
            show miguel at right
            miguel "Sige, pag-isipan mo muna yan Leo. Ako muna ang magtatrabaho sa mga dahon."
            "Hindi na nakialam si Miguel at nag-focus sa kanyang sariling gawain. Mas lalong naging malungkot si Leo."
            
        "Kausapin at bigyan ng suporta si Leo":
            $ moral_score += 1
            show miguel at right
            miguel "Nagpapasalamat ako sa proyektong ito dahil pinagsama-sama tayo nito. At nagpapasalamat ako na kaibigan kita, Leo. Malulutas natin ito."
            "Naramdaman ni Leo na may nagmamalasakit sa kanya at bahagyang gumaan ang kanyang pakiramdam."

    show carla at center
    carla "Magkaroon ka ng pananampalataya, Leo. Hindi lang sa Diyos, kundi sa sarili mo at sa amin. Darating din ang sagot."

    jump sc2_act2

# ------------------ ACT 2: ANG SAKUNA ------------------
label sc2_act2:
    scene bg classroom_day
    with fade

    "Kalagitnaan ng linggo, dumating ang malaking sakuna."
    "Habang tanghalian, isang malakas na hanging umihip sa kanilang nakabukas na bintana sa silid-aralan."
    "Ang kanilang halos tapos nang puno, kasama ang maingat na nilikha nilang mga dahon, ay pinagpag ng hangin."
    "Ang mga pots ng pintura ay tumapon, nagkalat ng maliwanag na kulay sa kanilang backdrop na banig at sa mga kuwentong kanilang sinulat."
    "Ang magandang hardin ay naging isa nang madungis, makulay na gulo."

    "Nakatayo ang grupo sa pagkagimbal."

    show benjo at center
    benjo "Kasalanan ko ito. Dapat ay mas secure ko ang base. Ako ang may pananagutan dito."

    show liza at right
    liza "Nasira ito. Lahat ng ating pinaghirapan..."

    menu:
        "Paano dapat tumugon si Diego sa sitwasyon?"
        
        "Sumama sa pagkabigo at sisihin ang iba":
            $ moral_score -= 1
            show diego at left
            diego "Bakit hindi natin sinara ang bintana? Dapat may nag-isip niyan!"
            "Nagkaroon ng tensyon sa grupo at mas lalong nawalan ng pag-asa ang mga mag-aaral."
            
        "Magpakita ng bayanihan at magbigay ng inspirasyon":
            $ moral_score += 1
            show diego at left
            diego "Mas malalaking problema ang hinarap ng ating mga bayani kaysa dito! Hindi sila sumuko. Spirit ng bayanihan, everyone! Maayos natin ito."
            "Nagkaroon ng bagong lakas ng loob ang grupo sa mga sinabi ni Diego."

    show isabel at center
    isabel "Tama si Diego. Huwag nating sisihin ang sinuman. Magtulungan tayo nang magalang."

    jump sc2_act3

# ------------------ ACT 3: PAGBABAGONG-LOOB NI LEO ------------------
label sc2_act3:
    scene bg classroom_afternoon
    with fade

    "Mabilis silang kumilos."

    show liza at center
    liza "Ako na ang bahala sa paglilinis. May alam akong paraan para matanggal ang mga batik ng pintura."
    "Pinangunahan ni Liza (Malinis) ang operasyon ng paglilinis nang mahusay, ipinakita na ang tunay na kalinisan ay tungkol sa pagpapanumbalik ng kaayusan, hindi lamang pagpapanatili nito."

    show benjo at right
    benjo "Gagawin kong mas matatag ang base ng puno. Hindi na ito matutumba."
    "Buong-pananagutang pinamunuan ni Benjo (Mapanagutan) ang pagsisikap na muling itayo ang base ng puno, ginawa itong mas matatag ngayon."

    show carla at left
    carla "Kaya natin ito! Magtulungan lang tayo."
    "Si Carla (Pananampalataya) ay lumibot sa kanila, nag-aalok ng mga salita ng pag-encourage."

    menu:
        "Ano ang dapat gawin ni Miguel?"
        
        "Mag-focus lang sa sariling gawain at hindi isipin ang iba":
            $ moral_score -= 1
            show miguel at center
            miguel "Ako na lang ang magpapatuloy sa mga dahon. Sana matapos ko ito sa oras."
            "Nag-focus si Miguel sa kanyang sarili at hindi niya napansin na nangangailangan ng tulong ang kanyang mga kaibigan."
            
        "Magpakita ng pasasalamat at magbigay ng suporta sa lahat":
            $ moral_score += 1
            show miguel at center
            miguel "Nagpapasalamat ako na magkakasama tayong team. Nag-uwi ako ng meryenda para sa lahat."
            "Tumakbo si Miguel (Mapagpasalamat) sa canteen at nag-uwi ng meryenda para sa lahat, na nagpapasalamat sa kanilang pagsusumikap."

    "Lahat maliban kay Leo, na nakaupo sa sulok, nanonood. Nakita niya ang kanyang mga kaibigan, na puno ng pintura at pawis, ngumingiti ngayon habang ginagawa nilang hamon ang sakuna."

    menu:
        "Ano ang dapat gawin ni Leo?"
        
        "Manatili sa sulok at hintayin matapos ang lahat":
            $ moral_score -= 1
            "Nanatili si Leo sa kanyang kinaroroonan, nakikita ang kanyang mga kaibigan na nagtutulungan habang siya ay nanonood lamang."
            "Naramdaman niyang hindi siya kabilang at mas lalong nawalan ng pag-asa."
            
        "Sumali at tumulong sa paggawa ng proyekto":
            $ moral_score += 1
            show leo at center
            leo "Gagawin ko. Isusulat ko ang aking kuwento. At tutulong akong magrepaint."
            "Nakahanap siya ng bago, malinis na dahon at brush. Habang itinutayo ng kanyang mga kaibigan ang puno, nagsimulang magpinta at sumulat si Leo."

    jump sc2_ending

# ------------------ WAKAS ------------------
label sc2_ending:
    scene bg gymnasium
    with fade

    "Sa araw ng fair, ang kanilang 'Hardin ng Pagpapahalaga' ay proud na nakaposisyon sa gymnasium."
    "Ito ang pinakamagandang display, hindi dahil ito ay perpekto, kundi dahil ang kuwento nito ay nakaukit sa bawat stroke."

    "Pagdating ng oras ng presentasyon, binasa ng bawat miyembro ang kani-kanilang kuwento. Sa huli, turn na ni Leo."

    if moral_score >= 2:
        show leo at center
        leo "Ang aking pagpapahalaga ay Mapagpasalamat. Noong una, hindi ko alam kung ano ang ipagpapasalamat..."
        leo "Ngunit sa linggong ito, nakakita ako ng isang kamangha-manghang bagay. Nakita ko kung paano gawing kooperasyon ang sisihan ng paggalang."
        leo "Nakita ko kung paano gawing solusyon ang pagkakamali ng pananagutan. Nakita ko kung paano painugin ng pananampalataya ang daan sa isang madilim na sandali."
        leo "Nakita ko kung paano likhain ng kalinisan ang kagandahan mula sa kaguluhan. Nakita ko kung paano maging pagmamahal sa iyong grupo, sa iyong team, sa iyong mga kaibigan ang nasyonalismo."
        leo "At nakita ko ang pasasalamat sa aking matalik na kaibigan na si Miguel, na nagparamdam sa ating lahat na tayo ay mahalaga."
        leo "Kaya ngayon, ako ay nagpapasalamat. Nagpapasalamat ako sa proyektong ito na tumulong sa akin na makita kung sino ako."
        leo "Ako ay isang Pilipino, at nagpapasalamat ako sa aking mga bagong kaibigan na nagpakita sa akin kung ano talaga ang ibig sabihin nito."

        "Sumabog ang klase sa palakpakan. Ngumiti si Maestro Aurelio, may luha sa kanyang mata."

        show maestro at center
        maestro "Natutunan ninyo na ang mga pagpapahalagang ito ay hindi lamang mga salita sa isang pahina; ang mga ito ay buhay, kumikilos na mga aksyon na, kapag pinagsama-sama, ay lumikha hindi lamang ng isang magandang proyekto, kundi isang magandang komunidad."

        "Nagtanim sila ng isang hardin, at sa paggawa nito, ay hinayaan ang kanilang sariling mga diwa na mag-ugat at lumago."

    elif moral_score <= -2:
        "Ngunit sa kasamaang-palad, ang kanilang proyekto ay hindi gaanong naging maganda dahil sa kawalan ng pagtutulungan."
        "Ang mga dahon ay hindi magkakatugma at ang puno ay mukhang hindi pinag-isipan."
        "Si Leo ay hindi nakapagbahagi ng kanyang kuwento dahil hindi niya ito natapos."
        "Nagtapos ang Linggo ng Wika na may hindi magandang karanasan para sa grupo."

    else:
        "Ang kanilang proyekto ay naging maayos ngunit may mga kakulangan pa rin."
        "Nakapagbahagi si Leo ng kanyang kuwento ngunit kulang sa kumpyansa at sigla."
        "Natuto ang grupo ng mahahalagang aral ngunit may mga pagkakataong hindi sila nagkasundo."

    return