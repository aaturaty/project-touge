# Project Touge – käyttöopas

**One gutter away from being the fastest on the touge.**

[In English](README.md) · [Brändätty versio (HTML)](index.html)

Tämä opas käy Project Tougen läpi sivu kerrallaan: miten autosi saadaan sisään, miten sitä säädetään sen mukaan mitä tunnet tiellä ja miten ajot kellotetaan ja analysoidaan. Kuvat on otettu suoraan Tougesta suomenkielisellä näkymällä; omat lukusi ovat erilaiset.

Sisältö

1. [Ennen kuin aloitat](#1-ennen-kuin-aloitat)
2. [Näkymä yhdellä silmäyksellä](#2-näkymä-yhdellä-silmäyksellä)
3. [Rakenna: auto sisään](#3-rakenna-auto-sisään)
4. [Setupien tallennus ja hallinta](#4-setupien-tallennus-ja-hallinta)
5. [Säädä: korjaa se mitä tunnet](#5-säädä-korjaa-se-mitä-tunnet)
6. [Ajanotto: aja, kellota ja analysoi](#6-ajanotto-aja-kellota-ja-analysoi)
7. [Asetukset ja ohje](#7-asetukset-ja-ohje)
8. [Datasi](#8-datasi)
9. [Kun jokin ei täsmää](#9-kun-jokin-ei-täsmää)

Arjen kierros on lyhyt: **Rakenna** auto kerran, **Säädä** yhtä asiaa, aja muutama ajo **Ajanotossa**, katso **Analysoi** ja palaa Säädä-välilehdelle sen kanssa, mitä ajot kertovat.

Kieli vaihtuu yläpalkin **FI / EN** -kytkimestä. Pelin omat termit (esim. Part Setup, Weight Distribution in Front, osatasot Stock … Prototype) pysyvät englanniksi, jotta ne löytyvät pelistä samoilla nimillä.

---

## 1. Ennen kuin aloitat

1. Pura **Project Touge** -kansio haluamaasi paikkaan ja pidä se kokonaisena.
2. Kaksoisnapsauta **Project Touge.exe**. Touge avautuu omaan ikkunaansa; sulje ikkuna lopettaaksesi.
3. Mitään ei tarvitse asentaa. Windows 10 tai 11 ja Microsoft Edge WebView2 riittävät. Jos SmartScreen varoittaa tuntemattomasta julkaisijasta, valitse **Lisätietoja → Suorita silti**.

Ajanottoa varten aja CarX Streetiä reunattomassa ikkunassa tai koko näytöllä niin, että koko HUD näkyy. Touge lukee nopeusmittarin, vaihteen ja minikartan näytöltä samalla tavalla kuin sinä ne näet. Se ei lue, muuta eikä syötä mitään peliin.

## 2. Näkymä yhdellä silmäyksellä

![Project Touge ensimmäisellä käynnistyksellä](img/fi/01-overview.webp)

- **Välilehdet 01 Rakenna, 02 Säädä, 03 Ajanotto** ovat työjärjestyksessä. Näppäimet **1**, **2** ja **3** vaihtavat niiden välillä.
- **Setup** (oikealla ylhäällä) näyttää avoimen setupin. Vihreä piste = tallennettu, keltainen = tallentamattomia muutoksia. Napsauttamalla saat Tallenna, Tallenna nimellä ja Kaikki setupit.
- **?** avaa ohjeen pikanäppäimineen ja säätöoppaineen. **Ratas** avaa asetukset. **FI / EN** vaihtaa kielen.
- Ensimmäisellä käynnistyksellä Touge on tyhjä: ensin **Valitse auto**, ja luvut tulevat näkyviin, kun auto on valittu. **Näin aloitat** -kaista näyttää kolme vaihetta, kunnes piilotat sen.
- Jokaisen sivun yläosassa on **Seuraavaksi**-rivi, joka kertoo, mitä tehdä seuraavaksi, ja linkki vie sinne.
- Termit, joiden vieressä on **i**-nappi, selittävät itsensä: napsauta sitä, niin saat lyhyen kuvauksen.

Kaksi merkkiä toistuu kaikkialla, ja ne kannattaa oppia ensin:

| Merkki | Tarkoittaa |
|---|---|
| ◐ | Arvio, jota ei ole vielä todennettu pelissä. Pidä sitä suuntana, ei lupauksena. |
| Keltainen luku | Muutettu, ei vielä pelissäsi. Muuttuu tavalliseksi, kun olet siirtänyt sen peliin. |

Merkitön luku tulee pelin omasta datasta. Nimet, järjestys ja yksiköt seuraavat pelin Part Setup -valikkoa, joten ne voi kirjoittaa peliin sellaisinaan.

## 3. Rakenna: auto sisään

Useimmiten autosi on jo rakennettu pelissä. Valitse silloin **Syötä pelistä**. Jos haluat Tougen ehdottavan koko buildin luokkaan, valitse **Rakenna mallilla**.

### 3.1 Auto, luokka ja reitti

Napsauta autoa ja hae koko autolistasta; luokka ja reitti valitaan samalla tavalla. Yläpuolen teho-paino-palkki näyttää, kuinka lähellä luokan rajaa olet.

![Auton haku](img/fi/02-car-picker.webp)

![Reittilista](img/fi/03-route-picker.webp)

Reittilistassa ovat ensin pelissä todennetut reitit ja omat reittisi. Valitse se reitti, jota oikeasti ajat: mallin ajat, välitysten tarkistus ja Ajanotto-välilehti seuraavat sitä.

### 3.2 Syötä pelistä

![Syötä pelistä](img/fi/04-enter-from-game.webp)

1. Avaa CarX Streetissä auton **Part Setup** ja ota kuvakaappaus jokaisesta sivusta: moottori, vaihteisto, kori ja aero, jousitus, renkaat ja Component features.
2. Liitä kuvat **Ctrl+V**:llä, pudota ne laatikkoon tai käytä **Valitse tiedostot**. Kuvat luetaan omalla koneellasi eikä niitä tallenneta. Kuvista luetut rivit korvaavat pohja-arvot; pohjana on tämän auton edellinen setup, jos sellainen on.
3. Tai syötä buildi käsin. Kaikki rivit pysyvät näkyvissä pelin järjestyksessä: moottori **Hae moottoria…** -haulla ja osat yhdellä napautuksella tasoriviltä (S Stock, St Street, Sp Sport, R Racing, E Elite, U Ultimate, P Prototype), vaihteiston välitykset sellaisinaan kuin peli ne näyttää, korisarja, jousitus etu ja taka rinnakkain sekä renkaat muodossa **leveys / profiili / vanne** edessä ja takana. Osiot, joihin et koske, pitävät mallin arvot.
4. Tarkista osien alla olevasta kohdasta **Perustiedot** **Weight**, **Weight Distribution in Front** ja **Center of Mass Height** pelistä. Ne ovat osien jälkeen, koska moottori ja vaihteisto muuttavat painoa. Nämä kolme lukemaa ratkaisevat, miten auto mallinnetaan, joten ne kannattaa kopioida tarkasti.
5. **Tarkista**-rivi listaa pelin järjestyksessä kaiken, mitä Touge ei saanut luettua tai mistä se on epävarma.
6. Anna buildille nimi ja paina alhaalla **Tallenna** (tai **Ctrl+S**). Tallennus avaa Säädä-sivun. Jos tallennus sanoo **Tallennettu vain selaimeen**, Touge-ohjelma ei ollut käynnissä: setup on tallessa tässä ikkunassa, ja **Vie kaikki setupit** siirtää sen tiedostoon.

Tästä eteenpäin Säädä-välilehti käsittelee *sinun* buildiasi, ei malliautoa.

### 3.3 Rakenna mallilla

Käytä tätä, kun haluat lähtöpisteen uudelle autolle tai luokalle.

**Vaihe 1: auto, luokka ja reitti.** Valitse auto, preset, luokka ja reitti. **Alueittain** valitsee alustan, diffin ja välitysten profiilin erikseen. *model* tarkoittaa Tougen omaa laskentaa; presetit ovat makuprofiileja sen päällä. Paina **Jatka**.

**Vaihe 2: mitä laskuri saa muuttaa.**

![Rakenna mallilla: moduulit ja tulos](img/fi/05-build-model.webp)

- **Laskuri valitsee** hakee osat ja säädöt luokan rajaan asti. **Paranna** pitää nykyisen buildisi ja näyttää jokaisen muutoksen vaikutuksen sekunneissa.
- Jokainen moduulikortti (Auto, Moottori, Voimansiirto, Aero ja kori, Jousitus, Renkaat) näyttää, mitä buildissa on nyt. Kytke **Saa muuttaa** niihin moduuleihin, joihin laskuri saa koskea, tai ruksaa **Kaikki**.

**Vaihe 3: Laske** (näppäin **L**). Laskenta kestää muutamasta sekunnista noin puoleen minuuttiin.

Oikean reunan **Tulos**-paneeli näyttää:

- **Mallin vertailuaika**: laskettu arvio tämän buildin ajasta valitulla reitillä. Kunnes reitti on kalibroitu omista ajoistasi, aika näytetään erona vertailubuildiin (esimerkiksi **−1,0 s**): malli tuntee uuden reitin mutkat vain ajolinjasta, joten kokonaisaika voi heittää sekunteja, mutta buildien väliset erot pitävät. Aja yksi ajo ja avaa Ajanotto → Analysoi, niin reitti kalibroituu. Oikeat ajat ovat Ajanotto-välilehdellä.
- **ennen / jälkeen** ja mikä muuttui, esimerkiksi vaihteiston vaihto.
- **Aikajana**: jokainen laskenta säilyy, napsauta palataksesi siihen.
- **Aseta vertailuksi** tekee tästä buildista vertailukohdan; **Peru laskurin valinnat** palaa lähtötilaan.
- Massa, teho, 0–100 km/h ja painojakauma.

![Ehdokkaat](img/fi/06-candidates.webp)

Tuloksen alla **Ehdokkaat** listaa moottori- ja vaihteistoyhdistelmät ajan mukaan, paras ensin. **Valitse** vaihtaa toiseen, jos pidät siitä enemmän. **Kokeile muutoksia** listaa yksittäiset muutokset ja niiden vaikutuksen.

### 3.4 Moduulit yksi kerrallaan

Napsauta vaiheen 2 moduulikorttia, niin se aukeaa korttien alle; **Sulje** tai toinen napsautus sulkee sen. Jokainen moduuli näyttää buildin sen osan kaikki tiedot, ja suurin osa toimii samoin tilassa **Laskuri valitsee** ja **Paranna**. Kun moduuli saa muuttua, laskuri täyttää sen; kun se on lukittu, tässä asettamasi arvot pysyvät.

**01 Automalli**

![Automalli-moduuli](img/fi/40-mod-car.webp)

Auto on tässä kiinteä; vaihda se vaiheessa 1. Näet vakiomassan, vakioetupainon, painopisteen korkeuden, akselivälin ja raideleveyden. **Kevennys** ja **Polttoainesäiliö** valitaan tasoittain, ja massan muutos näkyy vieressä. **Akselikuormat** näyttää, miten paino jakautuu akseleille paikallaan, jarrutuksessa ja kiihdytyksessä. **Pelin lukemat** ottaa painon ja etupainon pelin omasta valikosta, jotta malli vastaa autoasi.

**02 Moottori**

![Moottori-moduuli](img/fi/41-mod-engine.webp)

- Valitse **moottori**. **Rajaukset** rajaa listan moottoreihin, jotka omistat tai voit ostaa, tai näyttää kaikki; **Turbo**, **Kilpapolttoaine** ja **Polttoaineen venytys** kytkevät nämä vaikutukset päälle ja pois.
- Kaavio näyttää buildin väännön ja tehon kierrosten mukaan. **Molemmat**, **Vääntö** ja **Teho** valitsevat, mitä piirretään. Vakio-osien käyrä on katkoviivalla, ja varjostus näyttää, missä osasi voittavat (vihreä) tai häviävät (punainen) vakioon verrattuna.
- **Hienosäädä reittiajalla** ajaa osa- ja liukuriyhdistelmät reitillä ja pitää nopeimman.
- **Osat luokkaan** listaa jokaisen moottorin osapaikan ja sen tason. Kytke **Valitse itse**, niin voit valita osat käsin; paikka, jonka taso ei voi nousta luokasta putoamatta, kertoo sen. Napsauta osaa, niin näet sen **Osan säätö** -liukurit.
- **Component features** näyttää samat luvut kuin pelin moottorinäkymä: huipputeho ja -vääntö, paino, vääntö kohdissa Low, Medium ja High, rajoitin, Peak RPM ja ahto.
- **Vertaa moottoreita** avaa moottorin käyräsivun (3.5), ja **Tallenna moottoribuildi** säilyttää tämän moottorin myöhempää vertailua varten.

**03 Voimansiirto**

![Voimansiirto-moduuli](img/fi/42-mod-drivetrain.webp)

Vaihdelaatikko, vetotapa ja vaihtoaika. **Välitykset** näyttää jokaisen vaihteen ja vetopyörästön sekä niiden eron vakioon. **Välitysprofiili** valitsee valmiin välityssarjan tai omasi. **Välityskaavio** piirtää kierrokset nopeuden mukaan vaihteiden läpi vaihtopisteen ja rajoittimen kanssa, ja sen alla näet huippunopeuden reitillä sekä 0–100 ja 100–200 km/h. **Diffi**-rivi näyttää lukot ja esijännityksen; **Säädä →** vie Säädä-välilehden diffiin, jossa sitä voi raahata (5.5).

**04 Aero ja kori**

![Aero ja kori -moduuli](img/fi/43-mod-aero.webp)

Korisarja, etu- ja takasiiven taso sekä alavoimaliukurit samassa järjestyksessä kuin pelin Part Setupissa. **Aero nopeuden mukaan** näyttää kummankin akselin lisäkuorman ja ilmanvastuksen nopeuden kasvaessa, ja alla olevat kortit kertovat huippunopeuden suoralla, alavoiman 200 km/h:ssa ja akselipainot.

**05 Jousitus**

![Jousitus-moduuli](img/fi/44-mod-suspension.webp)

Jousitus on aina Prototype, koska sillä voi säätää kaiken. **Jousituksen tila** piirtää auton paikallaan, jarrutuksessa, kiihdytyksessä ja 200 km/h:ssa; **Pomppu** näyttää, kuinka nopeasti kori asettuu. Alla ovat painojakauma, kallistusjäykkyyden jako (LLTD), ominaistaajuudet, vaimennussuhteet ja kuinka paljon aero painaa autoa alas vauhdissa. Syötä pelin **etupaino** ja halutessasi oma **vakaajajako edessä** reittiaikaa varten.

**06 Renkaat**

![Renkaat-moduuli](img/fi/45-mod-tyres.webp)

Leveys, profiili ja vanne kummallekin akselille sekä spacer. Yläkuva piirtää renkaat mittakaavassa raideleveyden, akselivälin ja lokasuojan sisälle jäävän tilan kanssa. **Rengassarja** valitsee seoksen, ja sarjan pito näkyy vieressä. **Vertaa kokoja reitillä** ajaa reitin jokaisella pelin koolla nykyisellä buildilla ja listaa ajat.

### 3.5 Vertaa moottoreita: vääntö ja teho

![Moottorin käyrä -sivu](img/fi/46-engine-compare.webp)

Moottori-moduulin **Vertaa moottoreita** avaa sivun, joka on kuin pelin Component Features -graafi, ja siinä voi olla päällekkäin jopa viisi moottoria.

1. Nykyinen buildisi on aina ensimmäinen kortti. **Muokkaa kopiona** tekee siitä kortin, jota voit muuttaa koskematta buildiin; **Tallenna moottoribuildi** säilyttää sen nimellä.
2. Valitse lisää moottoreita valikosta **Lisää vertailuun…**: toinen moottori osilla **Vakio**, **Prototype** tai **Omat osat**, tallennettu moottoribuildi tai pelistä luettu käyrä. **Kilpapolttoaineen** voi kytkeä korttikohtaisesti.
3. **Molemmat**, **Vääntö** ja **Teho** valitsevat käyrät. Yhtenäinen viiva on vääntö, pisteviiva teho ja katkoviiva pelistä luettu. Napsauta nimeä selitteessä, niin käyrä piiloutuu tai tulee näkyviin, ja napsauta korttia, niin sen käyrä korostuu ja muut himmenevät.
4. Jokainen kortti listaa **Component features** -luvut ja niiden vieressä **Pelin lukema** -sarakkeen. Kirjoita siihen pelin näyttämä luku: ero malliin näkyy alla, vihreänä alle 1 %, keltaisena 3 %:iin asti ja punaisena sen yli.

Kun muutat buildia, edellinen käyrä jää harmaaksi katkoviivaksi, ja tehon, väännön ja rajoittimen muutos kirjoitetaan kaavion alle.

## 4. Setupien tallennus ja hallinta

Paina **Ctrl+S** (tai yläpalkin **Tallenna**). Ensimmäinen tallennus kysyy nimen ja ehdottaa autoa, luokkaa ja reittiä.

![Tallenna nimellä](img/fi/07-save-dialog.webp)

**Ctrl+O** avaa **Kaikki setupit**:

![Kaikki setupit](img/fi/08-all-setups.webp)

- Hae nimellä tai autolla, rajaa autolla vasemmalta ja lajittele minkä tahansa sarakkeen mukaan.
- Oikea paneeli näyttää luokan, reitin, mallin ajan ja parhaan ajosi. Siitä voit avata setupin, **Nimetä uudelleen** (F2), **Monistaa** tai **Poistaa** (Del). Poistetut menevät ensin **Roskakoriin**.
- **Tuo…**, **Liitä teksti**, **Vie valitut** ja **Vie kaikki** siirtävät setupeja koneelta toiselle tai kaverille.

Setupit tallentuvat Project Touge -kansioon tiedostoina, ja niistä jää päivätyt varmuuskopiot.

## 5. Säädä: korjaa se mitä tunnet

Säädä-välilehdellä on neljä näkymää siinä järjestyksessä, jossa niitä yleensä tarvitsee: **Oire**, **Säädä**, **Tarkista** ja **Peliin**. Säädä-näkymällä on oma näkymätason valitsin (**Vain säädöt**, **Perus**, **Laaja**), joka päättää, kuinka paljon yksityiskohtia siinä näet; Perus on hyvä alku. Muut näkymät näyttävät aina kaiken.

**Preset**-valitsin on ylhäällä: *malli* on Tougen oma tulos, ja presetin vaihto korvaa alustan ja diffin arvot. Omat presetit ovat listan lopussa. Kun Säädä toimii mallin autolla, yläreunan rivi kertoo sen, ja **Syötä buildi** vie Rakenna-välilehdelle syöttämään oman. Liukureissa on merkit pelin liukurien rajoista, joten näet, paljonko tilaa on jäljellä.

### 5.1 Oire

![Oire](img/fi/10-symptom.webp)

1. Valitse, missä kohtaa mutkaa auto käyttäytyy väärin: **Jarrutus**, **Sisääntulo**, **Keskikohta** vai **Ulostulo**.
2. Valitse oire, joka vastaa tuntumaa, esimerkiksi *Jarrutus mutkaan – aliohjaa*. Mutkakuva näyttää, missä se tapahtuu.
3. **Mitä muuttuu** aukeaa oikealle. Se alkaa Tuning Biblen neuvolla tähän oireeseen (mitä kokeilla ensin, mitä sitten), ja sen alla ovat säädöt, joita Touge siirtäisi, jokaisella yhden rivin syy ja vanha → uusi arvo.
4. **Yksi kerrallaan** on oletuksena päällä: **Käytä ensimmäinen** ottaa vain suurimman muutoksen, joten voit kellottaa ajon ennen seuraavaa. Poista ruksi, niin otat kaikki. **Peruuta** jättää setupin ennalleen.
5. Jos oireeseen on vaimenninkorjaus, perässä tulee **Jos koet tämän** -kortti, jossa ovat **Käytä** ja **Näytä säädin**, samat kortit kuin Tarkista-sivulla. Oire, neuvo ja tarkistus ovat yksi polku, joten näkymää ei tarvitse vaihtaa.

Tiedätkö jo, mitä haluat muuttaa? **Säädä setuppia itse** Ajotuntuma-otsikon vieressä vie suoraan Säädä-näkymään.

**Koko auto** kattaa oireet, jotka eivät liity yhteen mutkan vaiheeseen: yleinen ali- tai yliohjaus, pomppiminen kuopissa, reunakivissä ja guttereissa sekä rajoitin tai kiihtyvyyden puute suorilla.

**Yleisneuvot tälle buildille** (avaa **Näytä neuvot**) nostaa esiin säätöjä, jotka kannattaa katsoa juuri tässä buildissa, ja niissä on **Pienemmäksi**- ja **Suuremmaksi**-napit.

Vaikutukset ovat arvioita (◐). Yksi muutos ja yksi kellotettu ajo kerrallaan kertoo enemmän kuin viisi muutosta kerralla.

### 5.2 Säädä

Säädä näyttää jokaisen säädön liukurina. Siinä on neljä välilehteä: **Osat**, **Alusta**, **Välitykset** ja **Muut**. Näkymätason valitsin on samalla rivillä oikeassa reunassa.

**Alusta**

![Säädä: Alusta](img/fi/11-adjust-chassis.webp)

- **A · Säädöt**: paino, etupaino, jousen pituus, jouset, vakaajat, vaimentimet sekä camber ja toe pelin järjestyksessä. Avaa ryhmän alta **Miten tämä toimii**, niin näet mekanismin.
- **C · Tasapaino & KPI**: vedä palkkeja siirtääksesi etu-/takajakoa niin, että kokonaisjäykkyys säilyy. Vaimennussuhde, kallistusgradientti ja jousituksen taajuus päivittyvät samalla.
- **Alustan yleisjäykkyys**: yksi säädin koko alustan pehmentämiseen tai jäykistämiseen.
- **Tallenna presetiksi** säilyttää tämän alustan presettinä, jonka voi valita myöhemmin uudelleen. **Lue kuvasta** täyttää arvot kuvakaappauksesta.

**Välitykset**

![Säädä: Välitykset](img/fi/12-adjust-gearing.webp)

- **Sahakaavio** näyttää jokaisen vaihteen kierrokset nopeuden mukaan, kun vaihdetaan rajoittimella. Vihreä kaista on tehoalue; vihreä piste on vaihto, joka osuu sen sisään, harmaa sellainen, joka putoaa alle.
- Valitse vaihteet, joita säädät: **1–3**, **3–4**, **4–5** ja niin edelleen ylimpään vaihteeseen asti, tai **Kaikki**, tai napauta kahta vaihdetta kaavioiden alla olevalla rivillä, niin saat oman alueen.
- Raahaa **vaihteen yläpään ympyrää** vasemmalle tai oikealle, niin vaihde lyhenee tai pitenee. Nuolinäppäimet siirtävät sitä 0,01 kerrallaan.
- Raahaa **◂ 1–3 ▸ -nappia**, niin koko alue siirtyy kerralla.
- Raahaa alareunan **päätypalkkia**, niin porrastus muuttuu: se pää liikkuu ja toinen pysyy, ja välissä olevat vaihteet säilyttävät suhteensa.
- **Tiivistä** ja **Harvenna** kiristävät tai harventavat aluetta: sen ylin vaihde pysyy ja alemmat siirtyvät sitä kohti tai siitä pois. Näet muutoksen ennen kuin otat sen käyttöön.
- **Molemmat**, **Kierrokset** ja **Vetovoima** valitsevat kaaviot. Vetovoima näyttää jokaisen vaihteen vedon nopeuden mukaan pitorajan kanssa; **Kiihdytä** toistaa täyskaasukiihdytyksen vaihteiden läpi.
- Kaavion alla isot luvut ovat pelin välityssuhteet, ja niiden alla kokonaisvälitys ja kierrospudotus.
- Oikealla ovat **välitysprofiili**, **vetopyörästö** ja **vaihtoaika**. **Vaikutus** kertoo huippunopeuden, 0–100 km/h, kuinka moni vaihto osuu tehoalueelle ja kunkin vaihdon kierrospudotuksen.
- **Diffi** on alempana: kaasulukko, jarrulukko ja esijännitys. Raahaa pyöräkuvan kaaria tai käytä liukureita.
- **Käytä reittiajassa** ajaa uudet välitykset reitillä; **Nollaa** palauttaa alkuperäiset välitykset.

**Muut**

![Säädä: Muut](img/fi/13-adjust-other.webp)

Ohjaus (caster, Ackermann, ohjauskulma), jarrut, spacerit, rengaskoot ja pelistä luetut painolukemat. Autokuva näyttää raideleveyden, akselivälin ja kuinka paljon tilaa renkaalla on lokasuojan sisällä, jotta pysyt pelaajien tavallisessa säännössä: renkaat eivät törrötä lokasuojan ulkopuolelle.

Paina **Valmis**, kun olet tyytyväinen; se vie tallennukseen.

### 5.3 Tarkista

![Tarkista](img/fi/14-check.webp)

Tarkista käy koko buildin läpi ja selittää sen:

- **Välitykset**: jokaisen vaihteen loppunopeus rajoittimella ja riittääkö ylin vaihde reitille. Syötä oma huippunopeutesi reitillä, jos tiedät sen. **Laske ehdotukset** kokeilee kokonaisia välityssarjoja, joissa kaikki vaihteet ovat käytössä.
- **Vaimentimet**: vaimennussuhteet edessä ja takana ja mitä ne merkitsevät sisäänmenolle ja rauhoittumiselle. **Jos koet tämän** antaa valmiin korjauksen **Käytä**- ja **Näytä säädin** -napeilla.
- **Alusta ja diffi**: kallistusjako, kokonaisjäykkyys ja diffin säädöt sekä suunta, johon kukin vie autoa.
- **Moottori**: hae moottorin liukurit tai anna myös moottorin osien muuttua luokan sisällä.

### 5.4 Peliin

![Peliin](img/fi/15-to-game.webp)

Peliin on lista, jota seuraat peli auki Tougen vieressä.

1. Neljä sivua seuraa pelin valikoita: **Auto ja moottori**, **Voimansiirto**, **Jousitus**, **Renkaat ja aero**.
2. Jokainen rivi näyttää asetettavan arvon. Oikean reunan **Seuraavaksi**-kortti näyttää seuraavan; aseta se pelissä ja paina **Merkitse siirretyksi**. Osion **✓ Osio pelissä** merkitsee koko osion kerralla.
3. Pidä **Vain siirtämättömät** päällä, niin lista lyhenee edetessä. **Seuraava**-nappi alhaalla vie seuraavalle sivulle.
4. **Tarkista pelistä** -rivit (paino, etupaino) ovat lukemia: kirjoita pelin luku Tougeen, niin malli vastaa autoasi.

**Jaa buildi kuvana** tekee buildista kuvan jaettavaksi. **Lue kuvasta** lukee Part Setup -kuvakaappauksen takaisin. Leikepöytänappi kopioi listan tekstinä.

### 5.5 Näkymät ja raahaus

**Näkymän taso.** Säädä-näkymän välilehtirivin oikeassa reunassa oleva valitsin määrää, kuinka paljon Säädä-näkymästä näet (sama valinta on myös kohdassa Asetukset > Yleiset). Oire, Tarkista, Peliin ja Analysoi näyttävät aina kaiken.

| Taso | Näyttää |
|---|---|
| **Vain säädöt** | kaikki säädöt yhdellä ruudulla, ei kaavioita |
| **Perus** | säädöt ja tärkeimmät mittarit |
| **Laaja** | kaikki kaaviot ja lisätiedot; Alustassa säätöjen ja Tasapaino & KPI:n väliin tulee kaaviosarake **B** |

![Laaja näkymä: Alusta](img/fi/16-view-advanced.webp)

**Laaja**-tasolla sarakkeen B kaavio seuraa avaamaasi ryhmää: jouset, jousen pituus, vakaajat, vaimentimet tai camber ja toe.

**Paneelien siirto.** Paneeleja, joiden otsikossa on **⠿-kahva**, voi siirtää. Vedä kahvasta toiseen sarakkeeseen tai alas alariville, niin paneeli levenee koko leveydelle. Kahvan napsautus (tai Enter) avaa valikon, jossa ovat samat siirrot ja **Palauta oletusjärjestys**. **–** pienentää paneelin ja **×** piilottaa sen. Järjestys muistetaan näkymäkohtaisesti.

![Paneelin siirtovalikko](img/fi/18-panel-menu.webp)

**Mitä voi raahata**

| Missä | Raahaa | Tekee |
|---|---|---|
| Mikä tahansa säätöliukuri | nuppia tai rullaa hiirellä sen päällä | asettaa arvon; **Shift** + rulla siirtää 10 askelta |
| Paino, etupaino, vetopyörästö, vaihtoaika | rivin liukuria | sama kuin − ja + |
| Alusta · C Tasapaino & KPI · **LLTD** | palkkia | siirtää vakaajien etu–taka-jakoa kokonaisjäykkyys ennallaan |
| Alusta · **Tasapainomittarit** | mittaria | siirtää jousten tai vaimentimien etu–taka-jakoa akselien summa ennallaan |
| Camber ja toe -kaavio (Laaja) | pyörää | edestä-kuvassa kallistaa camberia, ylhäältä-kuvassa kääntää toeta |
| Välitykset · sahakaavio | vaihteen ympyrää, aluenappia, päätypalkkeja | ks. Välitykset yllä |
| Välitykset · diffi | kaaria | ulompi kaari kaasulukko, sisempi jarrulukko |
| Paneelit | ⠿-kahvaa | siirtää paneelin |

![Camberin ja toen raahaus](img/fi/19-camber-drag.webp)

Arvot siirtyvät pelilistaan, kun päästät irti, ja mallin aika päivittyy. Jos haluat kirjoittaa tarkan arvon, napsauta liukurin vieressä olevaa lukua.

## 6. Ajanotto: aja, kellota ja analysoi

### 6.1 Aja

![Aja](img/fi/20-drive.webp)

1. Valitse reitti oikealta. Kartta ja splitit seuraavat sitä.
2. Avaa CarX Street reunattomassa ikkunassa oletus-HUD:lla ja aja lähtöön. Touge lukee nopeusmittarin ja minikartan näytöltä, joten niiden pitää näkyä.
3. Pysähdy lähtöön ja paina **F9** (tai opettamaasi ohjaimen nappia). Kello lähtee, kun auto liikkuu, ja autosplit merkitsee osuudet.
4. **F10** splittaa käsin, **F11** on maali. **Väli** käyttää sovelluksen omaa sekuntikelloa, kun pelikello ei ole käynnissä.

Pelikello käynnistyy itsestään, kun Touge on auki, ja sen pieni ajastinikkuna pysyy pelin päällä. **F8** piilottaa ja tuo sen takaisin, **Ctrl+F8** siirtää sitä. Jos ikkunassa lukee **PELIÄ EI HAVAITTU**, Touge ei näe pelin HUD:ia; F8 tai ikkunan **X** piilottaa sen. Jos painat Käynnistä ilman peliä, saat ensin varoituksen, ja **Käynnistä silti** ottaa ajan ilman peliä.

LCD-kellon splittilista näyttää jokaisen osuuden vertailuajan, kun sinulla on ajo, johon verrata.

**Asetukset** (Ajanotto-välilehden oikeassa yläkulmassa) sisältää ajanoton valinnat:

![Ajanoton asetukset](img/fi/21-timing-settings.webp)

- **Autosplit** päälle tai pois ja **Mykistä ajastin**, kun haluat vain ajella.
- **Ohjain**: paina mitä tahansa ohjaimen nappia ja sitten **Opettele käynnistysnappi / splitti-nappi / peru-nappi**. Ne toimivat, kun peli on aktiivisena.
- **Ajonäkymä** näyttää kellon isona; **Irrota ajastin** avaa sen omaan pieneen ikkunaan.
- **Tuo** hakee vanhan kellon tiedoston tai LiveSplit-splitit tai palauttaa ajat varmuuskopiosta. **Syötä aika käsin** on muualla kellotettuja ajoja varten.

### 6.2 Tulostaulu

![Tulostaulu](img/fi/22-leaderboard.webp)

Kellon alla: ennätys, mediaani, viimeisten viiden keskiarvo ja kehitys. **Top 10** listaa ajot autoineen ja setupeineen, ja **Kehitys ajojärjestyksessä** näyttää, miten paras aikasi on parantunut. **Autot ja setupit** vertaa niitä rinnakkain.

### 6.3 Analysoi

Avaa maaliin päättyneen ajon jälkeen **Analysoi**. Se vertaa ajoa omaan ennätykseesi ja mediaaniisi mutka mutkalta.

![Analysoi](img/fi/23-analyse.webp)

- **Auto** rajaa ajot auton mukaan.
- Analysoin yläosa on yksi paneeli. **Aikanauha** näyttää viimeisimmän ajon ajan ja sen eron ennätykseen ja mediaaniin.
- **Kartta** värittää jokaisen mutkan vihreäksi (nopeampi) tai punaiseksi (hitaampi) kuin mediaanisi, ja alla oleva **mutkanauha** näyttää saman palkkeina. Hiiren rulla zoomaa karttaa, vetämällä sitä voi siirtää, ja ennätysajo kulkee mukana haamuna.
- **Ajon suurimmat erot mediaaniin** nimeää mutkat, joissa ajo hävisi eniten, ja syyn: jarrutus, sisääntulo, apex vai ulostulo.
- **Tavoite** erojen alla näyttää, paljonko aikaa on vielä otettavissa: teoreettinen parhaasi parhaista mutkistasi yhdistettynä.
- **Nopeus reitillä** paneelin alaosassa näyttää koko ajon nopeuskäyränä ennätykseesi ja mediaaniisi verrattuna. Kytke viivoja päälle ja pois napeista (ennätys, mediaani, kehityskohta, korkeus, splitit, malli) ja valitse mikä tahansa ajo kohdasta **Vertaa ajoa**. Kun liikut käyrällä, kursori liikkuu myös kartalla.

![Nopeus reitillä](img/fi/26-speed-on-route.webp)

**Zoomaa mutkaan.** Napsauta mutkaa kartalla tai sen palkkia mutkanauhassa. Kartta zoomaa mutkaan ja värittää sen nopeutesi mukaan, ja merkit näyttävät, missä jarrutus alkaa, missä on pohja ja missä kaasu aukeaa. Oikealle aukeaa **Mutkan tarkastelu**: sisääntulo-, pohja- ja ulostulonopeus mediaaniin verrattuna, todennäköinen syy sekä kaasu, jarru ja ohjaus mutkan matkalla ennätykseesi verrattuna. Napsauta toista mutkaa siirtyäksesi; **Koko reitti** tai **Esc** zoomaa takaisin. Kun viet hiiren nauhan palkin päälle, sama mutka korostuu kartalla.

![Mutkan tarkastelu](img/fi/25-analyse-zoom.webp)

**Ajovertailu** asettaa kaksi ajoa päällekkäin: nopeus, aikaero, vaihde, kierrokset, kaasu ja jarru sekä ohjaus. Valitse **Ajo A** ja **Ajo B (haamu)** tai **Vaihda A ja B**. Graafeissa vedä sivuttain zoomataksesi ja tuplaklikkaa koko reittiin; nuolinäppäimet siirtävät kursoria. Kartalla A on kursorin kohdalla ja B haamuna samalla ajan hetkellä, ja viiva on vihreä, missä A voittaa aikaa, ja punainen, missä A häviää.

![Ajovertailu](img/fi/29-run-comparison.webp)

Sen alla **viimeisimmän ajon** kortti kertoo ajon sanoin, ja **Seuraavaksi** nimeää yhden asian: yleensä mutkan, jota kannattaa harjoitella ensin (**Avaa mutka** zoomaa suoraan siihen), tai setupin muutoksen, kun sama kuvio toistuu ajoissasi (**Avaa Säädä**).

**Osioiden avaus.** Yläpaneelin alla olevat osiot voi pienentää. Napsauta osion otsikkoriviä, niin se aukeaa tai sulkeutuu; Touge muistaa, mitkä pidät auki. Jokaisessa on myös ⠿-kahva, jolla sen voi siirtää ylös tai alas.

![Harjoituslista](img/fi/24-practice.webp)

**Harjoituslista** järjestää mutkat, joissa mediaaniajosi häviää eniten parhaalle. Jokainen kertoo, mihin aika menee (jarrutus ja sisääntulo, apex vai ulostulo), ja lähikuva näyttää kaasun, jarrun ja ohjauksen ennätykseesi verrattuna. Merkitse mutka **Harjoiteltu**, kun olet työstänyt sitä.

**Ajo mutkittain** avaa valitun ajon mutkakohtaisen taulukon.

### 6.4 Reitit ja omat reitit

Aja- ja Analysoi-näkymien vieressä oleva **Reitit** listaa omat reittisi ja North Touge AP004:n; **Näytä kaikki pelin reitit** listaa myös jokaisen pelin reitin.

![Reitit](img/fi/27-routes.webp)

Valitse reitti, niin näet sen muodon, pituuden, mutkat, hiusneulat, nousun ja laskun, parhaan aikasi ja ajomäärän sekä splitit. Kirjoita **Kuvaus** (mistä lähtö alkaa, vaaralliset mutkat, missä gutterit toimivat) ja lisää **Lähtö**- ja **Maali**-kuvakaappaus, niin löydät kohdan uudelleen. **Valitse ja aja** vie reitin Aja-näkymään.

**Tee oma reitti**

![Reittieditori](img/fi/28-route-editor.webp)

1. Paina **＋ Uusi reitti** (tai omalla reitillä **Muokkaa tai poista**). Kartta näyttää jokaisen tien, jota pelin kisat käyttävät, ja maamerkkeinä bensa-asemat, kodit, kerhot ja autoliikkeet. Raahaa siirtääksesi, rullalla tai **+ / −** -napeilla zoomaat.
2. **Klikkaa lähtö** tielle. Klikkaa sitten splitit järjestyksessä ja viimeisenä maali. Reitti kulkee pisteiden välillä tietä pitkin lyhintä reittiä.
3. Klikkaus reitin päällä lisää splitin väliin, muualla klikkaus jatkaa reittiä. Raahaa pistettä siirtääksesi sitä.
4. Jos reitti oikaisee kohdasta, jota et aja, lisää **Ohjauspiste**: se ohjaa reittiä, mutta siinä ei oteta aikaa. Jokaisen pisteen voi vaihtaa **Splitiksi** tai **Ohjauspisteeksi**.
5. Reitti tarvitsee lähdön, 3–6 splittiä ja maalin. Anna reitille ja jokaiselle pisteelle nimi; paneeli näyttää pituuden, mutkat, hiusneulat ja nousun.
6. Rastita **Ajettavissa myös vastasuuntaan**, jos haluat reittilistaan myös vastakkaisen suunnan.
7. **Tallenna reitti**, tai **Tallenna ja aja**, niin voit kellottaa sen heti.

**Ensimmäinen ajo uudella reitillä.** Aja ensimmäinen ajo lähdöstä maaliin ja paina jokaisessa splitissä itse **F10**. Autosplit oppii splittien paikat tästä ajosta ja toimii itsestään seuraavasta ajosta alkaen. Sama pätee pelin reitteihin.

Omat reittisi tallentuvat `Routes`-kansioon.

## 7. Asetukset ja ohje

![Asetukset](img/fi/30-settings.webp)

- **Yleiset**: kieli, tekstin koko, Säädä-näkymän näkymätaso sekä animaatiot. Paneeleja voi siirtää vetämällä niiden otsikon kahvasta.
- **Data ja varmuuskopiot**: missä datasi on ja nappi kansion avaamiseen.
- **Ajanotto**: pelikellon ja näytönlukijan valinnat.
- **Käynnistys ja sammutus**: sammuttaa Tougen ja pelikellon yhdessä.
- **Tietoja**: versio ja lisenssit.

![Ohje](img/fi/31-help.webp)

**?** tai **F1** avaa ohjeen: kolme vaihetta, säätöoppaat (vakaajat, jouset, vaimentimet, renkaat, camber ja toe, tasauspyörästö, korin mitat, koko alusta) ja pikanäppäimet.

| Näppäin | Toiminto |
|---|---|
| 1 · 2 · 3 | Rakenna, Säädä, Ajanotto |
| L | Laske (Rakenna) |
| Ctrl+S | Tallenna setup |
| Ctrl+Shift+S | Tallenna nimellä |
| Ctrl+O | Kaikki setupit |
| F9 · F10 · F11 | Pelikello: aloita, splitti, maali |
| F8 · Ctrl+F8 | Ajastinikkuna: näytä tai piilota, siirrä |
| F1 | Ohje |

## 8. Datasi

Kaikki tallentamasi jää Project Touge -kansioon:

| Kansio | Sisältö |
|---|---|
| `Tunes` | setupit, presetit, muistiinpanot, reittien kalibroinnit ja asetukset |
| `Runs` | kellotetut ajot ja niiden telemetria |
| `Routes` | omat reitit |
| `Logs` | ohjelman lokit; liitä nämä, kun ilmoitat ongelmasta |

**Päivitys**: korvaa `App` ja `Project Touge.exe`, pidä datakansiot. **Siirto**: kopioi koko kansio. **Poisto**: poista kansio.

## 9. Kun jokin ei täsmää

- **Pelikello ei vastaa**: käynnistä Project Touge uudelleen; kello käynnistyy sen mukana. Tarkista, ettei mikään muu telemetriaohjelma käytä samaa porttia.
- **Nopeus tai minikartta ei tule**: aja peliä reunattomassa ikkunassa tai koko näytöllä niin, että HUD näkyy. Touge löytää HUDin ensimmäisellä ajolla; testatut resoluutiot ovat 3440×1440, 2560×1440, 2560×1080, 1920×1440 ja 1920×1080.
- **Luku ei vastaa peliä**: katso ensin, onko siinä ◐. Kirjoita pelin oma lukema **Tarkista pelistä** -riveille ja ilmoita ero Tougen versiolla ja `Logs`-kansion tiedostoilla.
- **Setup katosi**: katso **Kaikki setupit → Roskakori** tai palauta päivätyistä kopioista `Tunes`-kansiossa.

Löysitkö vian tai luvun, joka ei täsmää pelissä? Avaa [issue](https://github.com/aaturaty/project-touge/issues) ja kerro Tougen versio (näkyy yläpalkissa), mitä teit, ja liitä `Logs`-kansion tiedostot.

---

*Project Touge on epävirallinen fanien tekemä työkalu. Se ei ole CarX Technologiesin tuote, eikä CarX Technologies ole sidoksissa siihen tai suosittele sitä.*
