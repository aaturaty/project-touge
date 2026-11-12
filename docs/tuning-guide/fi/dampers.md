[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../dampers.md)

# Vaimentimet

## Lyhyesti

Natiivimallissa vaimentimet ovat pieni vipu kierrosajalle mutta iso tuntumalle. Kokemuksemme mukaan vakio-, nykyinen ja maksimivaimennus olivat puolen sekunnin sisällä toisistaan, kun taas minimivaimennus teki autosta epävakaan tai ajokelvottoman ◐. Jouset ja vakaajat päättävät, kuinka paljon kuormaa lopulta siirtyy, vaimentimet kuinka nopeasti. Siksi vaimentimet vaikuttavat siirtymissä (jarrutus, sisäänohjaus, kaasun avaus, kuopat), eivät pitkän mutkan keskellä.

Pelin polvi on korkealla (0,1 m/s), joten slow-arvot tekevät lähes kaiken ajettavuustyön ja fast-arvot vain kuopat, reunat ja gutterit.

Merkit: ● vahvistettu pelissä tai pelin koodissa, ◐ natiivimalli tai päätelty, ei pelissä testattu, ○ oikean auton tausta.

## Näin peli laskee

1. Vaimenninvoima riippuu pyörän nopeudesta v, ei asennosta. Alle 0,1 m/s: F = slow · v. Yli 0,1 m/s: F = slow · 0,1 + fast · (v − 0,1) ●. Fast on käyrän jyrkkyys polven jälkeen, ei erillinen voima.
2. Bump (puristus) toimii, kun pyörä nousee koria kohti. Rebound (paluu) toimii, kun pyörä laskee korista poispäin ●.
3. Arvot vaikuttavat suoraan pyörällä; välityssuhdetta ei ole ●. Liukuri kertoo arvon 1,65:llä per askel, ±3 askelta ●. Yhdellä autolla näytetty luku on 2 × natiivin kerroin, mutta tätä ei ole tarkistettu muilla autoilla ◐.
4. Polvi on kiinteästi 0,1 m/s ●. Oikeissa vaimentimissa polvi on tyypillisesti 0,025–0,075 m/s ○, joten pelissä slow-alue kattaa myös suuren osan tien epätasaisuuksista.
5. Kallistuskeskiö on maan tasolla, joten koko sivuttainen kuormansiirto kulkee jousien, vakaajien ja vaimentimien kautta ●. Vaimentimien osuus siirtymissä on siksi luultavasti suurempi kuin oikeassa autossa ◐.
6. Rajoitin on jäykkä eikä säädettävä. Joustovara = jousen pituus − painuma ●, ja vaimennin vaikuttaa siihen, kuinka lähelle rajoitinta jousitus ajautuu kuopissa.

**Mitä kumpikin alue hoitaa:**

| Pyörän nopeus | Ajotapahtuma | Mikä arvo |
| --- | --- | --- |
| Alle 0,1 m/s | Kallistus sisääntulossa (noin 0,03 m/s ◐), sukellus jarrutuksessa, kyykky kaasulla, loivat aallot | slow bump ja slow rebound |
| Yli 0,1 m/s | Kuopat, reunat, gutterit, pientareen yli ajo | fast bump ja fast rebound (slow vaikuttaa polveen asti) |
| Pitkän mutkan keskikohta | Liike on pysähtynyt | ei mikään: vaimentimet eivät tee mitään |

## Slow ja fast bump

**Mitä se tekee.** Bump hidastaa pyörän nousua koria kohti. Niin kauan kuin liike jatkuu, se lisää kuormaa sen kulman renkaalle ● (voima nopeudesta). Akseli, jonka puristus on jäykempi, ottaa siirtymissä suuremman osan kuormansiirrosta ja menettää hetkeksi pitoa suhteessa toiseen ○.

- **Etu slow bump** toimii jarrutuksessa ja sisääntulossa, kun keula sukeltaa ja ulompi etupyörä puristuu.
- **Taka slow bump** toimii kaasun avauksessa ja ulostulossa, kun perä kyykkää.
- **Fast bump** toimii vain, kun pyörä osuu kuoppaan, reunaan tai gutteriin.

**Suhde.** Kun fast on pienempi kuin slow, käyrä loivenee polven jälkeen (digressiivinen), kuten kilpavaimentimissa ○. Peli sallii myös fast > slow (progressiivinen) ●. Pelissä toimineissa setupeissa fast bump on noin 0,6–0,7 × slow bump ●.

**Kun nostat:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Etu slow bump | Keula sukeltaa jarrutuksessa hitaammin ja auto on sisääntulossa rauhallisempi. | Aliohjaus mutkaan tullessa; keula ei ota kuormaa. | ○ Lähteet ovat suunnasta yksimielisiä. ● 10 %:n muutos oli pelissä kohinaa. |
| Taka slow bump | Perä kyykkää kaasulla hitaammin. | Ulostulossa perä kevenee hetkeksi: yliohjaus ja heikompi veto ○. | ◐ Sekä ×0,7 että ×1,3 olivat vakioarvoa hitaampia. |
| Fast bump | Kori tukeutuu kuopissa eikä painu yhtä syvälle. | Kuoppa tai reuna heittää autoa ylös ja rengas irtoaa tiestä hetkeksi. | ● Fast bump ×1,5 tuntui pelissä erittäin hyvältä. ◐ Natiivivaikutus vain −0,05 s. |
| Kaikki bump alas | Pyörä seuraa tietä ja imee kuopat. | Kori painuu nopeasti ja lyö rajoittimeen. | ◐ Bump minimissä oli noin kaksi sekuntia hitaampi. |

## Slow ja fast rebound

**Mitä se tekee.** Rebound hidastaa pyörän laskua korista poispäin, joten se pitää koria alhaalla ●. Se vaikuttaa enemmän viereisiin ja vastakkaisiin kulmiin kuin omaansa ○.

- **Etu slow rebound** toimii kaasun avauksessa, kun keula nousee, ja sisäetupyörällä sisääntulossa.
- **Taka slow rebound** toimii jarrutuksessa, kun perä nousee, ja sisätakapyörällä sisääntulossa.
- **Fast rebound** päättää, kuinka nopeasti pyörä palaa tiehen kuopan tai reunan jälkeen.

**Suhde.** Pelissä toimineissa setupeissa slow rebound on noin 3,6 × slow bump edessä ja 4,5 × takana ●. Fast rebound on noin puolet slow reboundista edessä ja kolmasosa takana ●. Oikeissa autoissa rebound on usein 2–3 × bump ○. Kun rebound kasvaa paljon bumpia suuremmaksi, jousitus pakkautuu kuoppasarjassa kohti rajoitinta: pyörä painuu nopeasti mutta palaa hitaasti ◐. Kokemuksemme mukaan hyvin suuren reboundin puolitus vähensi rajoitinaikaa lähes puoleen ◐.

**Kun nostat:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Etu slow rebound | Keula nousee kaasulla hitaammin ja pysyy kuormitettuna, joten kaasu-aliohjaus vähenee. | Auto tuntuu kovalta ja pakkautuu; sisäetupyörä kevenee sisääntulossa. | ● Etu-reboundin puolitus teki autosta ennustettavamman, mutta toi lievää kaasu-aliohjausta nopeisiin mutkiin. ◐ Natiivimalli näytti päinvastaista suuntaa (ristiriita). |
| Taka slow rebound | Perä nousee jarrutuksessa hitaammin ja auttaa kääntämään autoa sisääntulossa. | Sisätakapyörä kevenee; perä pomppii ja lähtee kuopissa. | ◐ Noin 25 %:n lasku on rauhoittanut pomppivan perän. ● Takavaimentimet +20 % tuntui pelissä hyvältä. |
| Fast rebound | Kori pysyy rauhallisena kuoppien jälkeen. | Pyörä ei palaa tiehen ajoissa ja pito katkeaa kuoppasarjassa. | ◐ Fast rebound ×0,6 oli 0,14–0,18 s hitaampi, eli liian pieni oli hitaampi. |
| Kaikki rebound alas | Pyörät palaavat nopeasti eikä auto pakkaudu. | Kori huojuu ja nyökkii. | ◐ Kaikki rebound minimissä: auto ei päässyt natiiviajoa loppuun. |

## Yhteistoiminta: miten säätää

**Mikä vaimennin liikkuu missäkin vaiheessa** (tasainen tie ○, sama mekaniikka pelissä ●):

| Vaihe | Etu | Taka | Hallitseva pari |
| --- | --- | --- | --- |
| Suora jarrutus | bump | rebound | etu bump + taka rebound |
| Jarrutus mutkaan (trail brake) | ulko bump, sisä rebound | ulko bump, sisä rebound | ulkoetu bump + sisätaka rebound |
| Sisääntulo, jarru pois | ulko bump, sisä rebound | ulko bump, sisä rebound | sisäetu rebound + ulkotaka bump |
| Keskikohta | — | — | ei vaikutusta |
| Ulostulo, kaasu | rebound | bump | etu rebound + taka bump |
| Kuoppa, reuna, gutteri | fast bump, sitten fast rebound | sama | pyörä, joka osuu |

**Säätöjärjestys:**

1. Ensin jouset ja vakaajat. Ne päättävät, mihin kuormansiirto asettuu; vaimentimet vain kuinka nopeasti.
2. Taso: muuta kaikkia neljää samalla kertoimella (yksi liukuriaskel = ×1,65). Natiivimallissa vakiosta maksimiin oli kohinaa, mutta minimi oli liian vähän ◐.
3. Bump/rebound-suhde: jos auto tuntuu kovalta ja lyö rajoittimeen kuopissa, rebound on liian suuri bumpiin nähden.
4. Etu/taka: korjaa siirtymien tasapaino oireen mukaan (alla).
5. Fast-arvot viimeisenä, kuoppiin ja guttereihin.

**Muista:**

- Kallistuksessa ulkopyörä puristuu ja sisäpyörä palaa samalla nopeudella. Akselin hetkellinen kuormansiirto on silloin noin (bump + rebound) / 2 × nopeus, ja jos rebound on suurempi, erotus (rebound − bump) × nopeus vetää koria alas ◐ johdettu.
- Kun jäykistät jousta mutta et vaimentimia, jousitus on suhteessa vähemmän vaimennettu, koska kriittinen vaimennus kasvaa jousen neliöjuuren mukana ○ (sama kaava pelissä). Nosta vaimennusta suunnilleen √(uusi jousi / vanha jousi).
- Yllä olevat suhteet (rebound 3,6–4,5 × bump, fast noin 0,6 × slow) tulevat presetistä, joka on toiminut pelissä usealla autolla. Ne ovat lähtökohta, eivät haettu arvo ◐.
- Oikean auton nyrkkisäännöt, kuten vaimennussuhde 0,5–0,7, ovat vain taustaa ○. Pelissä toimiva etu-rebound on niitä yhä selvästi suurempi.

## Vaikutus muihin

| Säätö | Miten liittyy vaimentimiin pelin fysiikassa |
| --- | --- |
| Jouset | Sopiva vaimennus riippuu jousesta (kriittinen vaimennus ∝ √(jousi · massa)). Pehmeä jousi ja jämäkkä slow-vaimennus antavat nopean tuen siirtymissä ja pehmeän tuntuman kuopissa ○. |
| Jousen pituus | Joustovara = pituus − painuma ●. Liian suuri rebound pakkaa auton rajoittimelle, ja lyhyt jousi tuo rajoittimen vielä lähemmäs. Kokemuksemme mukaan pidempi jousi vähensi rajoitinaikaa kolme neljäsosaa, reboundin puolitus lähes puolet ◐. |
| Vakaajat | Vakaajalla ei ole omaa vaimennusta ●. Jäykempi vakaaja samoilla vaimentimilla tekee kallistuksesta suhteessa vähemmän vaimennetun ○. |
| Diffi | Kaasun avaus kyykyttää perää (taka bump) samalla kun diffi lukitsee. Taka slow bump ja kaasulukko vaikuttavat molemmat perään ulostulossa, joten muuta vain toista kerrallaan ◐. |
| Camber | Camber muuttuu jousen liikkeen mukana ●, ja vaimennin hidastaa tätä muutosta. Vaikutus on pieni, koska camberin pitovaikutus on pieni ◐. |
| Renkaat | Renkaan pystyjousto on sarjassa jousituksen kanssa; renkaan omaa vaimennusta ei ole löydetty natiivikoodista ◐. |
| Kuopat ja gutterit | Asfaltin kuoppakuvio on −0,0035…0 m (toisto 20 m) ja ±0,025 m (toisto 200 m) ●. Gutterit ja pientareen yli ajo ovat fast-alueen päätapahtumat linjalla, joka käyttää niitä. |

## Oireet

Muuta yhtä arvoa kerrallaan noin 15–20 % (puoli liukuriaskelta) ja aja sama mutka. Vaimenninoireet tulevat siirtymissä: jos oire on mutkan tasaisessa keskikohdassa, katso ensin jousia ja vakaajia.

| Vaihe | Oire | Mitä pelissä tapahtuu | Muutos |
| --- | --- | --- | --- |
| Jarrutus mutkaan | Keula sukeltaa nopeasti ja perä kevenee | Etu painuu ja taka nousee liian nopeasti | Nosta etu slow bumpia ja taka slow reboundia. |
| Jarrutus mutkaan | Auto ei käänny trail brake -vaiheessa | Ulkoetu ottaa siirtymässä liikaa kuormaa | Laske etu slow bumpia ○. |
| Sisääntulo | Perä lähtee heti käännössä | Sisätaka kevenee; perä ottaa siirtymässä liikaa | Laske taka slow reboundia ◐. |
| Ulostulo, kaasun avaus | Keula työntää kaasulla nopeissa mutkissa | Keula nousee nopeasti ja menettää kuormaa | Nosta etu slow reboundia ●. |
| Ulostulo, kaasun avaus | Perä kevenee ja lähtee, kun kaasu tulee | Perä puristuu hitaasti samalla kun diffi lukitsee | Laske taka slow bumpia, tai ensin diffin preloadia. |
| Kuopat ja gutterit | Auto tuntuu kovalta ja pomppii kuoppasarjassa | Rebound ei päästä pyörää takaisin; jousitus pakkautuu rajoittimelle | Laske slow reboundia ● tai pidennä jousta. |
| Kuopat ja gutterit | Gutteri tai reuna heittää auton ilmaan | Fast bump liian suuri | Laske fast bumpia. |
| Kuopat ja gutterit | Auto huojuu ja nyökkii kuopan jälkeen | Fast rebound liian pieni | Nosta fast reboundia. |

## Loppuvinkki

Pidä vaimentimet aluksi lähellä vakiota tai touge weapon -presetiä: natiivimallissa vakio ja maksimi erosivat vähän, mutta liian vähäinen vaimennus pilasi auton. Hio sitten yksi vaihe kerrallaan: rebound kuopissa pakkautumiseen, etu slow rebound kaasu-aliohjaukseen ja fast-arvot guttereihin. Jos auto tuntuu kovalta, katso bump/rebound-suhdetta ja jousen pituutta ennen jousta.

Kokemuksemme mukaan rebound on jokaisessa toimivassa setupissa selvästi bumpia suurempi, ja takana suhteessa suurempi kuin edessä. Raskaampi auto käyttää suurempia lukuja samoilla suhteilla.

## Varmistamatta

- Etu slow reboundin suunta kaasulla on ristiriitainen: peli ja kirjallisuus sanovat, että vähemmän reboundia lisää kaasu-aliohjausta, natiivimalli näytti päinvastaista ◐. Tämä opas seuraa peliä.
- Näytetyn luvun ja natiivikertoimen suhde (2 × yhdellä autolla) on tarkistamatta muilla autoilla, joten opas ei laske vaimennussuhteita.
- Kuoppia, guttereita ja pientareita ei ole ajettu natiivimallissa, joten fast-arvojen neuvot perustuvat yhteen pelikokeeseen ja yleiseen mekaniikkaan.
- Vaihetaulukon suunnat tulevat oikean auton lähteistä (○). Pelin vaimenninkaava on sama, mutta jokaista suuntaa ei ole ajettu natiivimallissa.

---

← [Vakaajat](anti-roll-bars.md) · [Sisältö](README.md) · [Camber ja toe](camber-and-toe.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
