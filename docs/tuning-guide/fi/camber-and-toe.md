[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../camber-and-toe.md)

# Camber ja toe

## Lyhyesti

Camber ja toe ovat tässä pelissä pieniä vipuja. Natiivimallissa camber muuttaa sivupitoa enintään noin 3,5 % ja vie jarrutus- ja vetopitoa 0,5 % astetta kohti ●. Kokemuksemme mukaan camber −2 vs −5 oli usealla autolla kohinaa ◐, mutta lähellä nollaa oleva etucamber on maksanut yli sekunnin ◐. Toe on hieman isompi vipu: takatoe-in rauhoittaa perää ja takatoe-out vie pitoa, mutta koko kierroksella ero jää alle sekunnin ◐. Hio ensin vakaajat, jouset ja diffi, ja viimeistele camberilla ja toella.

Pelissä on kaksi eroa oikeaan autoon. Säätämäsi camber ei ole renkaan todellinen camber, koska peli lisää siihen −3…+5° jousen avautuman mukaan ●. Lisäksi natiivikoodissa on jäykän akselin jousitustyyppi, jolla camber-säätö ei tee mitään ●. Sitä, kumpi pelin jousitustyypeistä (Mcferson vai Doublewishbone) vastaa jäykkää akselia, ei vielä tiedetä.

Merkit: ● vahvistettu pelissä tai pelin koodissa, ◐ natiivimalli tai päätelty, ei pelissä testattu, ○ oikean auton teoria.

## Camber: renkaan kallistus

**Näin peli laskee:**

1. Camber koriin nähden = säätö − 3° + 8° · x, missä x = jousen nykyinen pituus / isku (0 = pohjassa, 1 = täysin auki) ●. Levossa todellinen camber on siksi noin 2–3° positiivisempi kuin säätö. Tyypillinen etupyörä on levossa noin säätö + 2,4°, joten −3,5 on levossa noin −1,1° ◐ laskettu.
2. Camber muuttuu jouston mukana 8° / isku, eli 100 mm:n iskulla 0,8° negatiivisemmaksi jokaista painumasenttiä kohti ●. Mutkassa ulkopyörä painuu ja muuttuu negatiivisemmaksi, mutta kori kallistuu ulos ja vie sitä positiivisemmaksi. Yhdellä testiautolla nämä lähes kumosivat toisensa: rajalla ulkopyörä oli maahan nähden noin säätö + 3,4° ◐.
3. Renkaassa camber ei nosta sivupidon huippua. Se jäykistää pidon kasvua: −5° antaa 14 % enemmän sivujäykkyyttä, mikä tuntuu terävämpänä alkuvasteena ●. Sivuvoimaan tulee myös pieni siirtymä (−3° → +0,15°), jolla ei ole käytännön merkitystä ●.
4. Pitkittäispito (jarrutus ja veto) kerrotaan luvulla 1 − 0,005 · |camber|, eli se laskee 0,5 % astetta kohti ●. Edessä iso camber pidentää jarrutusta, takana se heikentää vetoa.
5. Natiivin jousitustyyppi 1 on jäykkä akseli: pyörät seuraavat akselin kallistusta, ja camber-säätö sekä camber-käyrä nollataan ●. Peli välittää autodatan tyypin natiivikoodille sellaisenaan, mutta sitä, onko Doublewishbone tyyppi 1, ei tiedetä ◐. Jos on, camber ei tee mitään autoissa, joissa siinä päässä on Doublewishbone.
6. Säätöalue tulee tukivarsiosista. Perusosa antaa camberiksi −4,5°, säädettävä osa ±3,5°. Prototype-varsilla raja on noin −21,5° edessä ja −22,5° takana ●.

**Kun lisäät negatiivista camberia:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Etucamber negatiivisemmaksi | Hieman terävämpi alkuvaste ja muutama prosentti lisää keskikohdan pitoa. | Jarrutus pitenee eikä kääntyminen enää parane. | ◐ Etu 0 → −15: sivupito +1,1 %. ◐ Etu −3,5 → −2 oli kahdella autolla 0,4–0,6 s hitaampi, −5 kohinaa. |
| Takacamber negatiivisemmaksi | Perä pitää keskikohdassa hieman paremmin. Takacamber auttaa pitoa enemmän kuin etucamber. | Takapyörät sutivat ulostulossa, koska veto heikkenee. | ◐ Taka −13: sivupito +3,4 %. ● Taka −3,3 yhdessä muiden muutosten kanssa on toiminut pelissä. |
| Camber kohti nollaa | Jarrutus- ja vetopito paranevat hieman. | Sivupito laskee ja alkuvaste laiskistuu. Positiivinen camber haittaa selvästi. | ● Taka −4,3 → −3,5 yhdessä toisen muutoksen kanssa oli pelissä tasoissa. ◐ +10° −6,5 % (vanha ajo, vain suunta luotettava). |

## Toe: pyörän suunta

**Näin peli laskee:**

1. Toe annetaan asteina. Plus on toe-in (pyörien etureunat osoittavat sisäänpäin) ja miinus toe-out ●. Peli lisää toen pyöräkulmaan, vasemmalle −toe ja oikealle +toe, edessä ja takana ●.
2. Edessä toe tulee Ackermann-kulman päälle ●. Ackermann on oma säätönsä (0 = täysi Ackermann, 100 = rinnakkaiset pyörät), eikä sillä ollut natiivimallissa mitattavaa pitovaikutusta ◐.
3. Mutkassa takatoe-in kääntää kuormitettua ulkopyörää hieman mutkan sisään, joten perä tekee enemmän sivuvoimaa ja auto vakautuu ○ teoria, joka sopii natiivitulokseen (takatoe-in nosti tasaisen mutkan pitoa).
4. Suoralla toe tarkoittaa, että pyörät vierivät pienellä luistokulmalla vastakkaisiin suuntiin. Sivuvoimat kumoavat toisensa, mutta pieni vastus jää ◐ päätelty, ei mitattu.

**Kun lisäät:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Takatoe-in (+) | Perä rauhoittuu mutkaan jarruttaessa ja pitkissä mutkissa, ja pito nousee isoissa mutkissa. | Auto aliohjaa eikä kierry tiukoissa mutkissa, ja kierros hidastuu. | ◐ +0,2 vähensi sivuluistoa mutkaan jarruttaessa 4–8 %, mutta +0,4 jo aliohjasi. ◐ +0,3 / +0,6: pito nopeissa mutkissa +2…+4 %, mutta kierros 0,5–1,1 s hitaampi useimmilla autoilla. |
| Takatoe-out (−) | Auto kiertyy herkemmin. | Perä päästää irti jarrutuksessa ja mutkissa, ja pito laskee. | ◐ −0,3: pito tiukoissa mutkissa −3,6 %, nopeissa −3 %. Koko kierroksella neutraalista 1,5 s hitaampaan, vakaajista riippuen. |
| Etutoe (±) | Vaikutus on pieni. Toe-out terävöittää sisäänohjausta ○. | Auto vaeltaa suoralla ja tuntuu hermostuneelta ○. | ◐ ±0,3 oli useimmilla autoilla 0,2–0,8 s hitaampi molempiin suuntiin ja yhdellä nopeampi. |

## Vaikutus muihin

Camber riippuu jousituksesta, joten säädä se jousien ja vakaajien jälkeen. Toe on lähes riippumaton muista säädöistä, mutta takatoe-in tekee samaa työtä kuin perää vakauttavat säädöt.

| Säätö | Miten liittyy camberiin ja toehen pelin fysiikassa |
| --- | --- |
| Jouset (pituus ja jäykkyys) | Lepocamber riippuu painumasta. Jäykempi jousi tai pidempi pituus tekee camberista positiivisemman: paljon jäykempi etujousi noin +0,8°, +8 mm pituutta noin +0,2° ◐ laskettu. Tarkista camber isojen jousimuutosten jälkeen. |
| Vakaajat ja kallistus | Kori kallistuu ulos ja vie ulkopyörää kohti positiivista camberia. Jäykempi kallistus pitää camberin lähempänä säätöä ◐. Tasapaino haetaan silti vakaajilla, ei camberilla. |
| Caster | Ohjattaessa ulkopyörä saa negatiivista camberia noin caster · sin(pyöräkulma) ja sisäpyörä positiivista ●. Caster 8,4 ja 30°:n pyöräkulma antavat noin 4°. Casterilla ei ollut natiivimallissa pitovaikutusta ◐. |
| Ackermann | Etutoe lisätään Ackermann-kulman päälle ●, joten muuta niitä yksi kerrallaan. |
| Diffi ja jarrut | Camber vie pitkittäispitoa 0,5 % / aste ●. Takacamber heikentää ulostulon vetoa samaan suuntaan kuin liian suuri kaasulukko, ja etucamber pidentää jarrutusta. Takatoe-in rauhoittaa trail brake -vaihetta samaan suuntaan kuin etupainotteisempi jarrujako ◐. |
| Renkaat | Camberkerroin on sama kaikilla renkailla ●. Pelin kaavassa leveys ei muuta camberin vaikutusta ◐. |
| Jousitustyyppi | Jäykkä akseli (natiivin tyyppi 1) nollaa camberin ●. Tarkista autosi jousitustyyppi ennen camberin hiomista (ks. Varmistamatta). |

## Oireet

Muuta camberia 0,5° ja toeta 0,1° kerrallaan, ja aja sama mutka samalla vaihteella. Jos oire reagoi vakaajiin, jousiin tai diffiin, käytä niitä ensin.

| Vaihe | Oire | Mitä pelissä tapahtuu | Muutos |
| --- | --- | --- | --- |
| Jarrutus mutkaan | Perä vaeltaa tai yrittää ohi, kun jarrutat mutkaan | Paino siirtyy eteen eikä takapyörien sivuvoima riitä | Takatoe +0,1…+0,2 ◐. Kokeile ensin jarrujakoa ja moottorijarrulukkoa. |
| Jarrutus mutkaan | Etupyörät lukkiutuvat tai jarrutus pitenee | Iso etucamber vie pitkittäispitoa | Etucamber 0,5–1° kohti nollaa. |
| Sisääntulo | Auto kääntyy laiskasti | Etupyörän sivujäykkyys on pieni | Etucamber −0,5°. Etutoe −0,1 auttaa teoriassa ○, ei natiivimallissa. Kokeile ensin vakaajia. |
| Keskikohta | Perä liukuu pitkässä mutkassa | Takapyörien sivuvoima loppuu | Takatoe +0,1…+0,2 tai takacamber −0,5°. |
| Keskikohta | Auto aliohjaa pitkässä mutkassa, vaikka vakaajat ovat kohdallaan | Takatoe-in pitää perää liikaa | Takatoe kohti nollaa. |
| Ulostulo | Takapyörät sutivat, kun suoristat ja avaat kaasun | Takacamber vie vetopitoa | Takacamber 0,5° kohti nollaa ●. |
| Suora ja huippunopeus | Auto vaeltaa tai tuntuu hermostuneelta | Toe-out jommassakummassa päässä ○ | Etutoe 0, takatoe 0…+0,1. |
| Kuopat, reunat ja gutterit | Tuntuma muuttuu jousituksen painuessa | Camber muuttuu jouston mukana 8° / isku ● | Älä korjaa camberilla; käytä jousitusta. |

## Loppuvinkki

Camber −3,5 / −3,5 on ollut pelissä jokaisessa toimivassa touge weapon -presetin setupissa ●. Ruudulla se näyttää paljolta, mutta levossa se on noin 2–3° positiivisempi kuin luku. Pidä etutoe nollassa ja takatoe 0…+0,1:ssä, ja muuta niitä vain oireen mukaan.

Jos et tiedä, vaikuttaako camber autossasi, tee pikakoe: etucamber −3,5 → −8 ja aja sama mutka. Jos tuntuma ei muutu lainkaan, etuakseli on todennäköisesti natiivin jäykkä akseli.

**Simulaatiokokemus ◐ (natiivimalli, ei pelissä testattu):** etucamber −4,6 → 0 oli 1,4 s hitaampi, eniten keskinopeissa mutkissa, ja jäykällä etuvakaajalla vielä enemmän (yhdessä 2,3 s). −6,5 ei tuonut mitään −4,6:een nähden. Lähellä nollaa alkava etucamber on siis enemmän kuin viimeistely. Takacamber ja etutoe eivät näkyneet kierrosajassa. Takatoe-in +0,3 oli 0,7 s hitaampi.

## Varmistamatta

- Jousitustyyppi on tärkein avoin kysymys: onko Doublewishbone natiivin tyyppi 1, jäykkä akseli? Pelin metadata on salattu, joten pelikoe ratkaisee (etucamber −3,5 vs −8).
- Lepocamberin esimerkit olettavat, että isku on jousen pituus. Se on päätelty pohjaanlyöntikaavasta, ei luettu natiivikoodista.
- Pitotulokset ovat natiivimallista. Pelkästä camberista tai toesta ei ole erillistä pelikoetta; pelikokeissa muutettiin samalla jotain muuta.
- Toen vastus suoralla on päätelty, ei mitattu.
- Etutoen vaikutus sisäänohjaukseen on oikean auton teoriaa ○, eikä natiivimalli tukenut sitä.

---

← [Vaimentimet](dampers.md) · [Sisältö](README.md) · [Diffi](differential.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
