[![Project Touge choriso's Tuning Bible](../banner.png)](README.md)

[In English](../whole-chassis.md)

# Alusta kokonaisuutena

## Lyhyesti

Tämä luku kokoaa aiheluvut yhdeksi työtavaksi. Tässä pelissä isoimmat vivut ovat vakaajajako, jousen pituus, rengaskoko ja diffin kaasulukko: kokemuksemme mukaan jokainen niistä on ollut pitkällä touge-reitillä sekunteja. Vaimentimet, camber, toe ja painopiste ovat viimeistelyä, joiden vaikutus aikaan on usein kohinan alla, mutta ne muuttavat tuntumaa.

Etene isosta pieneen, yksi muutos kerrallaan, ja ratkaise oire sillä vivulla, joka vaikuttaa siihen vaiheeseen eniten. Kun kaksi vaihtoehtoa ovat noin puolen sekunnin sisällä, pidä se, joka tuntuu hallittavammalta.

Merkit: ● vahvistettu pelissä tai pelin koodissa, ◐ natiivimalli tai päätelty, ei pelissä testattu, ○ oikean auton teoria.

Aiheluvut: [Vakaajat](anti-roll-bars.md) · [Jouset](springs.md) · [Renkaat](tyres.md) · [Vaimentimet](dampers.md) · [Camber ja toe](camber-and-toe.md) · [Korin dimensiot](body-dimensions.md) · [Diffi](differential.md)

## Isoimmat vivut

Vivun koko on suurin mitattu ero pitkällä touge-reitillä natiivimallissa tai pelikellolla. Luvut tulevat eri autoista ja lähtökohdista, joten ne kertovat suuruusluokan, eivät lupausta.

| Säätö | Vivun koko | Kokemus | Vaikuttaa eniten |
| --- | --- | --- | --- |
| Vakaajajako | Iso | ◐ Jopa noin viisi sekuntia. ● Hyvin takapainotteisen jaon siirto eteen korjasi pitkän auton herkän perän pelissä. | Tasapaino koko mutkan läpi |
| Diffin kaasulukko | Iso alapäässä, sitten tasainen | ◐ 0 selvästi hitain ja avoin diffi paljon hitaampi. Sen yläpuolella tulokset ovat ristiriitaisia (ks. Varmistamatta). ● 0,24–0,30 on toiminut pelissä. | Ulostulo |
| Jousen pituus | Iso | ● Muutama millimetri lisää etupituutta on ollut pelissä yli kaksi sekuntia nopeampi. | Joustovara, kuopat, kaasu-aliohjaus |
| Rengaskoko | Iso | ◐ 285–325 mm vs 265 mm noin kaksi sekuntia. | Pito ja välityksen pituus |
| Loppuvälitys | Keskikokoinen | ◐ Lyhyet autot hyötyivät 5–10 %:n muutoksella lähes kaksi sekuntia. | Kiihtyvyys mutkista |
| Jousen jäykkyys | Keskikokoinen | ◐ Ääripäät olivat 2–4 s hitaampia kuin alueen keskikohta. | Korin liike ja kuopat |
| Jarrujako | Keskikokoinen | ◐ 40 % edessä oli useimmilla autoilla 0,5–0,7 s nopeampi. ● Etupainotteinen jako on tehnyt sisäänmenosta turvallisen pelissä. ◐ 50 → 55–58 on tehokkain säädin perän vakauteen jarrulla. | Jarrutus ja sisääntulo |
| Vaimentimet | Pieni ajalle, iso tuntumalle | ◐ Lähes neutraaleja natiivimallissa. ● Takavaimentimet +20 % tuntui pelissä erittäin hyvältä. | Siirtymien nopeus |
| Raide ja offset | Pieni | ◐ +0,10 m molemmilla akseleilla +1,4 % pitoa; leveillä renkailla ±10 cm alle 1 %. | Tasapaino jarrulla |
| Camber ja toe | Pieni | ◐ Camber ≤ 3,5 % sivupitoa. Takatoe +0,2…+0,3 ja takacamber −5 nopeissa mutkissa +5…+10 % ◐, takatoe on toiminut pelissä ●. | Nopeat mutkat |
| Painopiste, rengaspaine, caster, Ackermann | Ei mitattavaa | ◐ Kierros kohinaa. Paine muutti pitoa alle 1–2 %. | – |

## Säätöjärjestys

Järjestys etenee isosta pieneen niin, ettei myöhempi säätö kumoa aiempaa. Jos palaat aiempaan vaiheeseen, tarkista sen jälkeiset vaiheet uudelleen.

1. **Renkaat ja kori:** rengaskoko, vanneosa ja offset lokasuojan sisällä. Rengas määrää pidon ja säteen, joten se on kaiken muun pohja.
2. **Välitykset:** vasta renkaan jälkeen, koska vain kokonaisvälitys (FD × renkaan säde) ratkaisee ●.
3. **Jousen pituus:** tarpeeksi joustovaraa, ettei jousitus lyö rajoittimeen (touge weapon: etu ×1,07, taka ×0,90 oletuksesta).
4. **Jouset:** jäykkyys massan mukaan, sitten pituus uudelleen, koska jäykempi jousi nostaa koria ●.
5. **Vakaajat:** jako akselivälin mukaan ja kokonaisjäykkyys kallistuksen mukaan. Tämä on tärkein tasapainosäätö.
6. **Diffi:** ensin kaasulukko, sitten preload ja moottorijarrulukko ulostuloon ja sisääntuloon.
7. **Jarrujako:** kierto ja vakaus sisääntulossa. Tavallinen lähtöalue on 48–50 % edessä, ja jos perä on levoton jarrulla, 55–58 ◐.
8. **Vaimentimet:** slow bump ja slow rebound siirtymien nopeuteen. Fast-arvot vain kuoppiin ja guttereihin.
9. **Camber ja toe:** viimeistely.

Tougen presetit antavat lähtöarvot vaiheille 2–8 auton dimensioista. Malli-laskenta on laskettu lähtökohta ◐, ei pelissä testattu setup. Touge weapon -preset on toiminut pelissä ●. Varsinainen hionta alkaa sitten oireista.

## Näin testaat

1. **Yksi muutos kerrallaan.** Kun muutat kahta asiaa, et tiedä, kumpi teki eron. Poikkeus on pari, joka kuuluu yhteen, kuten jousi ja sen pituus samaan korkeuteen.
2. **Riittävän iso askel.** Yksi liukuriaskel jakautuu välityksissä, jousissa, vaimentimissa, camberissa, toessa ja diffin lukoissa 20 pykälään ●, joten välityksen voi asettaa 0,4 %:n tarkkuudella. Pelin näyttämä välitys on fysiikan välitys ●. Pieni askel häviää silti kohinaan. Hyödylliset askeleet: vakaaja noin 10 % kokonaisjäykkyydestä tai 2–4 %-yksikköä jakoa, jousen pituus 4 mm, jousi noin 10 %, vaimennin noin 20 %, diffi 0,05, jarrujako 2 %-yksikköä, camber 0,5° ja toe 0,1°.
3. **Sama testipaikka.** Aja sama mutka tai osuus samalla vaihteella. Koko kierros kertoo tuloksen, yksittäinen mutka kertoo, mitä muutos teki.
4. **Tunne kohina.** Kokemuksemme mukaan saman setupin ajot hajoavat noin 0,8 s kuuden minuutin reitillä ●. Alle sekunnin eroa ei voi osoittaa yhdellä ajolla.
5. **Kirjaa tuntuma ajan lisäksi.** Kirjaa, mitä auto teki jarrutuksessa, sisääntulossa, keskikohdassa ja ulostulossa, ei pelkkää aikaa. Tougen Säädä-välilehden Oire-näkymä käyttää samoja neljää vaihetta.
6. **Koko kierros ratkaisee.** Muutos on parempi vain, jos se lyhentää kierrosta tai tekee autosta selvästi hallittavamman. Yhden mittarin, kuten tasaisen ympyrän pidon, parannus voi hidastaa kierrosta: taka-aeron lisäys nosti nopeiden mutkien pitoa, mutta yksin lisättynä kierros hidastui ◐, koska se maksaa nopeutta suorilla ja lisää aliohjausta keskinopeissa mutkissa.

**Ohjaimella ohjausavustin on aina päällä ●.** Ohjausavustimen Off-taso ei anna suoraa ohjausta ohjaimella eikä näppäimistöllä. Peli käyttää silti avustinta tiukimmalla etuluistorajallaan (105 %). Suora ohjaus on vain ratilla. Ohjaimella käytetään täyttä avustintasoa (Standard) ja Stabilization-liukuria ●. Stabilization 100 lisää aliohjausta hitaissa mutkissa ja vakautta nopeissa ●, ja pelissä on toiminut väliarvo, esimerkiksi Stabilization 50 ja Angle Stabilization in Drift 0 ●. Aiempi neuvo Off/Gamepad-profiilista oli väärä. Natiivikokeessa avustin muutti pitoa vain vähän (−1,2 % tiukassa mutkassa, 0 nopeassa) ◐, joten se ei selitä natiivimallin ja pelin eroja. Tuntumaan se voi silti vaikuttaa, koska se pitää etupyörät lähellä huippupitoa ◐.

## Halutusta muutoksesta lähtien

Nämä taulukot lähtevät siitä, mitä haluat muuttaa. Säädöt ovat vaikutuksen koon mukaisessa järjestyksessä. Vaikutus on natiivimallin ajoista yhdellä takavetoisella autolla (noin 900 kg, painojako 50/50) ◐, ellei toisin merkitty, joten se kertoo suunnan ja suuruusluokan, ei tarkkaa hyötyä omalla autollasi. Ympyräkoe porrastaa pidon 2–5 %:n askeliin, ja sitä pienemmät erot ovat kohinaa.

### Lisää kiihtyvyyttä

| Säätö | Suunta | Vaikutus | Huomio |
| --- | --- | --- | --- |
| Teho | Ylös | Iso | Suurin vipu. |
| Massa | Alas | Iso | Lisämassa hidastaa saman verran. |
| Ilmanvastus (Cx) | Alas | Iso kovassa vauhdissa, pieni hitaassa | Näkyy vasta suurella nopeudella. |
| Vaihtoviive (vaihteisto-osa) | Lyhyemmäksi | Keskikokoinen | |
| Voimansiirron häviö | Alas | Pieni | |
| Rengaspaine | Ylös | Pieni | Vierintävastus pienenee. |
| Renkaan leveys | Kapeammaksi | Pieni | Leveä rengas maksaa suoralla, mutta tuo pitoa mutkiin. |
| Takatoe | Kohti nollaa | Hyvin pieni | |
| Diffi ja alusta | – | Ei vaikutusta | Ei vaikutusta suoralla. |

### Lisää pitoa mutkaan

| Säätö | Suunta | Vaikutus | Huomio |
| --- | --- | --- | --- |
| Alavoima molemmille akseleille | Ylös | Iso, eniten nopeissa mutkissa | Hintana ilmanvastus. |
| Taka-aero etua suuremmaksi | Ylös | Iso nopeissa mutkissa, hitaat laskevat | Maksaa nopeutta suorilla. Isompi siipiosa kasvattaa ilmanvastuksen pinta-alaa ●; alavoimaliukuri samalla osalla maksaa vähän (120–200 km/h noin 0,05 s hitaampi selvästi suuremmalla arvolla ◐). Tarkista kierrosajalla. |
| Rengaspito (rengasluokka, vanneosa) | Ylös | Iso hitaissa, pieni nopeissa | |
| Renkaan leveys | Leveämmäksi | Keskikokoinen kaikissa mutkissa | Hidastaa suoralla. |
| Takatoe yhdessä takacamberin −5 kanssa | +0,2…+0,3 | Keskikokoinen nopeissa, ei hitaissa | Takatoe on toiminut pelissä ●. |
| Vakaajajako | Eteen | Keskikokoinen keskinopeissa | Hitaat mutkat kärsivät. |
| Takacamber | Kohti −5 | Pieni | Vetopito ulostulossa laskee hieman. |
| Jouset | Jäykemmiksi | Pieni, pito laskee | |
| Rengaspaine, raide ±10 cm | – | Ei vaikutusta | Alle 1–2 %. |

### Lyhyempi jarrutusmatka

Yksi metri jarrutusmatkaa on noin 0,03–0,04 s, joten jarrutusmatka on pieni aikavipu. ABS on pelissä aina päällä ●.

| Säätö | Suunta | Vaikutus | Huomio |
| --- | --- | --- | --- |
| Rengaspito | Ylös | Iso | |
| Etupaino | Alas | Iso | Takapainoisempi auto jarruttaa lyhyemmin. Tulee buildista. |
| Alavoima | Ylös | Keskikokoinen | |
| Massa | Alas | Keskikokoinen | |
| Jarruvoima (jarruosa) | Riittäväksi | Pieni | Liian heikko jarru pidentää matkaa, lisä riittävän päälle ei auta. |
| Jarrujako | Eteen | Pieni | |
| Vaimentimet, jousen pituus, toe, takacamber, diffi | – | Ei vaikutusta | |

### Vakaampi perä jarrulla

| Säätö | Suunta | Vaikutus | Huomio |
| --- | --- | --- | --- |
| Jarrujako | Eteen noin 5 %-yks. (50 → 55–58) | Iso | Tehokkain säädin. Etupainotteinen jako on tehnyt sisäänmenosta turvallisen pelissä ●. |
| Etuvakaaja | Ylös 20–40 % | Iso | Toiseksi tehokkain. |
| Moottorijarrulukko | Ylös | Keskikokoinen | |
| Takavakaaja | Alas | Pieni | Auttaa vähemmän kuin etuvakaaja. |
| Takatoe, preload, taka slow rebound, etu slow bump, takajousi | – | Ei vaikutusta | Näistä ei ollut apua jarrulla. |

## Oireesta säätöön

Tämä hakemisto kokoaa aihelukujen oiretaulukot. Kokeile ensin ensisijaista muutosta ja vasta sitten toissijaista. Aiheluvuissa on lisää yksityiskohtia.

| Vaihe | Oire | Ensisijainen muutos | Toissijainen |
| --- | --- | --- | --- |
| Jarrutus mutkaan | Auto aliohjaa jarrulla ja sitä joutuu kääntämään väkisin | Jarrujakoa 2–5 %-yks. taakse, sitten moottorijarrulukko alas ◐ | Etuvakaaja alas tai takavakaaja ylös ◐. Etupainotteinen jako kiersi jarrulla vähiten kaikilla akseliväleillä. Poikkeus pelistä ●: jos jako on hyvin takapainotteinen ja perä on pitkällä autolla levoton, tuo jako ensin lähemmäs tasaa. |
| Jarrutus mutkaan | Perä vaeltaa tai yrittää ohi | Jarrujakoa noin 5 %-yks. eteen, 50 → 55–58 (etupainotteinen jako ●, 55–58 ◐) | Etuvakaaja ylös 20–40 %, sitten moottorijarrulukko ylös. Takatoe, preloadin lasku, taka slow rebound ja etu slow bump eivät auttaneet ◐. |
| Jarrutus mutkaan | Keula sukeltaa ja lyö pohjaan | Etujousen pituus +4 mm | Etujousi tai etu slow bump ylös |
| Sisääntulo | Auto kääntyy laiskasti | Etuvakaaja alas tai takavakaaja ylös | Etu slow bump alas, etucamber −0,5° |
| Sisääntulo | Perä lähtee heti käännössä | Jos jarru on vielä päällä: jarrujako eteen ja etuvakaaja ylös ◐. Ilman jarrua: takavakaaja alas | Taka slow rebound alas (ei auttanut jarrulla ◐) |
| Keskikohta | Tasainen aliohjaus pitkässä mutkassa | Siirrä vakaajajakoa taakse | Rengaskoko tai etuakselin raide |
| Keskikohta, kova vauhti | Perä irtoaa yllättäen | Siirrä vakaajajakoa eteen akselivälin mukaan ● | Takatoe +0,2…+0,3 ja takacamber −5 ◐ (takatoe toiminut pelissä ●) |
| Ulostulo | Keula työntää kaasulla nopeassa mutkassa | Lisää etujousen pituutta ● | Etujousi alas ◐ |
| Ulostulo | Perä pyörähtää kaasulla | Diffin preload ja kaasulukko alas (varovasti alle 0,2) | Takavakaaja alas |
| Ulostulo | Sisäpyörä sutii | Kaasulukko ylös | Takajousi tai takapituus ylös, takacamber kohti nollaa |
| Suora | Rajoitin tulee ennen jarrutuspistettä tai auto ei kiihdy | Loppuvälitys | Rengaskoko (säde muuttaa välitystä) |
| Kuopat, reunat ja gutterit | Auto pomppii tai heittää pientareen yli | Lisää jousen pituutta | Fast bump alas, jousi alas |
| Kuopat, reunat ja gutterit | Auto jää huojumaan kuopan jälkeen | Slow rebound ylös | Fast rebound ylös |

Jos sama oire näkyy useassa vaiheessa, syy on yleensä vakaajajako tai diffi, ei yksittäinen vaimennin.

## Oman tuntuman haku

Nopein setup ei ole kaikille sama, koska kuljettaja ajaa sitä rajalla. Hae ensin tasapaino, jossa auto ei yllätä, ja säädä sitten tuntuma omaan tyyliisi. Kun kaksi vaihtoehtoa ovat noin 0,5 s:n sisällä, pidä hallittavampi: vähemmillä virheillä se on rajalla nopeampi.

**Tuntuman säätimet:**

| Haluat | Muuta | Hinta |
| --- | --- | --- |
| Enemmän kiertoa jarrulla | Jarrujako taakse, moottorijarrulukko alas | Perä voi lähteä jarrutuksessa. |
| Vakaamman sisäänmenon | Jarrujako eteen, etuvakaaja ylös, moottorijarrulukko ylös | Auto aliohjaa jarrulla. |
| Terävämmän vasteen | Slow-vaimentimet ylös, vakaajat jäykemmiksi samalla jaolla | Auto on kuopissa hermostuneempi. |
| Pehmeämmän ja ennustettavamman | Slow-vaimentimet ja jouset alas, enemmän joustovaraa | Siirtymät laiskistuvat. |
| Ulostulon, jossa perä auttaa kääntämään | Kaasulukko ja preload ylös | Perä lähtee helpommin kaasulla. |
| Suoran ulostulon | Preload alas, vakaajajako eteen | Auto työntää enemmän kaasulla. |

**Jos jarrutat syvälle mutkaan, käytät on/off-kaasua ja ajat pientareiden ja guttereiden yli:** jarrujako on silloin tärkein kiertosäädin, ja matala moottorijarrulukko estää sitä taistelemasta jarrukiertoa vastaan ●. Vakaus tulee silloin vakaajajaosta, ei diffistä. Jätä jousitukseen joustovaraa pientareille ja guttereille ja pidä fast-vaimennus maltillisena. On/off-kaasulla maltillinen preload ja kaasulukko hidastavat luiston kasvua ◐.

## Loppuvinkki

Aloita uusi auto Tougen presetistä. Touge weapon -preset on toiminut pelissä kymmenellä autolla ●. Malli-laskenta (takavetoisella takatoe +0,3, diffi 0,30 / 0,20 ja laskettu preload, pehmeämpi vaimenninpohja) on laskettu lähtökohta auton mitoista ◐, eikä sitä ole testattu pelissä kokonaisena setuppina. Aja muutama kierros ja kirjaa vaihe, jossa auto ei tee mitä haluat. Korjaa yksi oire kerrallaan hakemiston ensisijaisella muutoksella, ja kun auto on tasapainossa, siirry tuntumaan.

Kolme asiaa on toistunut jokaisessa kokeessa:

1. **Vakaajajako tulee ennen kaikkea muuta.** Kokemuksemme mukaan yksi jaon korjaus ratkaisi yhdeksän auton ongelmat kerralla.
2. **Joustovara tulee ennen matalaa koria.** Lisää jousen pituutta on tehnyt autosta sekunteja nopeamman, vaikka painopiste nousi.
3. **Kaasulukko ei saa olla liian matala.** Natiivimallissa 0 oli selvästi hitain, ja 0,24–0,30 on toiminut pelissä. Sen yläpuolella ero on lähinnä tuntumaa.

**Simulaatiokokemus ◐ (natiivimalli, ei pelissä testattu):** build ratkaisi eniten, sitten tasapaino ja viimeisenä diffi. Alavoima, massa ja rengaskoko muuttivat kierrosta 2–18 s, kun taas alustasäädöt järkevästä lähtökohdasta jäivät alle sekunnin (poikkeus oli hyvin pehmeä takavakaaja, 3,7 s hitaampi). Enemmän alavoimaa molemmille akseleille oli 2,8 s nopeampi; enemmän vain taakse 1,4 s hitaampi (aliohjaus keskinopeissa mutkissa) ja vain eteen 0,6 s nopeampi. 50 kg vähemmän massaa oli 2,1 s nopeampi. Tasapainomuutokset kyllästyvät eivätkä summaudu. Noin 15 %:n loppuvälitysalue pysyi 0,3 s:n sisällä.

## Varmistamatta

- Pelikoetta odottavat: etu slow reboundin suunta kaasulla (ks. vaimentimet), jarrujako 55 ja etuvakaaja ylös herkälle perälle samassa setupissa sekä takatoe +0,2…+0,3 yhdessä takacamberin −5 kanssa.
- Taka-aero etua suuremmaksi nosti natiivimallin ympyräkokeessa nopeiden mutkien pitoa, mutta yksin lisättynä kierros hidastui (aliohjaus keskinopeissa mutkissa). Selitys: taka-aero nostaa pitoa mutta maksaa nopeutta suorilla, lähinnä siipiosan ilmanvastuksen kautta, ja iso ero taakse lisää aliohjausta. Valitse siipiosa suorien mukaan ja säädä liukurilla pitoa ja tasapainoa ◐.
- Halutusta muutoksesta lähtien -taulukot ovat yhdellä autolla ◐. Muilla painojaoilla ja vetotavoilla järjestys voi muuttua.
- Vivun koot tulevat eri autoista, eri lähtösetupeista ja osin natiivimallista. Ne kertovat järjestyksen, eivät sitä, paljonko juuri sinun autosi hyötyy.
- Kaasulukon alaraja on ristiriitainen: yksi malli piti alle 0,25:ttä hitaana, neulakoe ei, toinen koe piti 0,10:tä hitaana, ja uudempi luistokykyinen kuljettaja näki 0,10–1,0 kierroksella kohinana ja tiukimmassa neulassa 0,15 nopeimpana. Pelissä toiminut 0,24–0,30 on turvallinen alue.
- Vaimentimien vaikutus aikaan on natiivimallissa pieni mutta tuntumaan iso. Natiivimalli ei mallinna kuljettajan luottamusta.
- Tuntuman säätimet on johdettu aiheluvuista ja oikean auton teoriasta. Niitä ei ole testattu yhtenä kokonaisuutena.
- 0,8 s:n ajojen välinen hajonta on yhdestä sarjasta yhdellä autolla ja reitillä. Muualla se voi olla erilainen.

---

← [Johdanto](README.md) · [Sisältö](README.md) · [Renkaat](tyres.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
