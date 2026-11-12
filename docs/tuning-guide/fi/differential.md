[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../differential.md)

# Diffi: kaasulukko, moottorijarrulukko ja preload

## Mitä kukin säätö tekee

Tämä luku perustuu pelin omaan diffikoodiin ja natiivimallin ajoihin. Oikean diffin teoriaa käytetään vain siellä, missä peli toimii samoin.

**Näin pelin kytkindiffi laskee:**

1. Voimansiirron vääntö T jaetaan ensin tasan, T/2 kummallekin vetopyörälle ●.
2. Lukko siirtää sen jälkeen vääntöä nopeammin pyörivältä pyörältä hitaammalle, enintään lukkovääntö T_lukko ●.
3. Kaasulla T_lukko = preload + kaasulukko × T. Moottorijarrulla T_lukko = preload + moottorijarrulukko × |T| ●.
4. Pyörien vääntöero voi olla 2 × T_lukko, joten suurin jako on (1 + 2L) : (1 − 2L). Lukko 0,25 = 3 : 1, 0,30 = 4 : 1, ja 0,50 tai enemmän = koko vääntö voi mennä yhdelle pyörälle ●.
5. T on voimansiirron vääntö. Jarrupolkimen jarrut eivät kulje diffin läpi, eikä kytkin pohjassa välity vääntöä. Silloin ainoa lukko on preload ●.

| Säätö | Mikä se on pelissä | Missä se vaikuttaa | Mitä se tekee |
| --- | --- | --- | --- |
| Kaasulukko (Lock on acceleration) | Osuus moottorin väännöstä, joka lukitsee pyörät | Kaasulla, eniten ulostulossa | Kun sisäpyörä alkaa sutia, vääntö siirtyy ulkopyörälle. Enemmän vetoa ja perä työntää. Liikaa: perä lähtee täydellä kaasulla. |
| Moottorijarrulukko (Lock on deceleration) | Osuus moottorijarrun väännöstä, joka lukitsee pyörät | Kaasu pois, mutkaan tulo | Ulkopyörä jarruttaa enemmän, joten auto vakautuu. Enemmän = vakaampi mutta laiskempi kääntymään. |
| Preload | Vakiolukko newtonmetreinä (Ultimate 0–520) | Aina, myös kytkin pohjassa | Ei kasva väännön mukana. Siksi se hallitsee, kun vääntöä on vähän: kevyt kaasu, kaasun ensimmäinen avaus, moottorijarru ja vaihtaminen. |

**Diffiosa määrää säätövälin ●:**

| Diffiosa | Kaasulukko | Moottorijarrulukko | Preload | Tarkkuus (lukko / preload) |
| --- | --- | --- | --- | --- |
| Ultimate (taso 5) | 0–1,0 | 0–1,0 | 0–520 | 0,005 / 3,25 Nm |
| Prototype (taso 6) | 0,6–1,6 | 0,3–1,3 | 0–100 | 0,0125 / 1,25 Nm |

Prototype-diffillä kaasulukko on aina vähintään 0,6, ja natiivikoodissa lukko 0,5 tai enemmän on täysi lukko. Kaasupuoli on siis aina täysin lukossa. Säädettävä kaasulukko (esimerkiksi 0,24–0,30) vaatii Ultimate-diffin.

**Suuruusluokka (◐, oletettu moottorin vääntö 250 Nm):** kakkosvaihteella akselin vääntö on noin 250 × 2,00 × 4,00 = 2000 Nm. Kaasulukko 0,3 antaa täydellä kaasulla noin 600 Nm lukkoa, ja preload 100 on siitä vain 1/6. Moottorijarrun vääntö on paljon pienempi, joten moottorijarrulukko 0,15 antaa vain kymmeniä newtonmetrejä. Silloin preload 100 voi olla suurempi kuin koko moottorijarrulukko.

**Kun nostat:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Kaasulukko | Ulostulossa sisäpyörä sutii vähemmän, auto vetää paremmin ja perä alkaa työntää. | Perä lähtee täydellä kaasulla tiukassa neulassa. | ◐ Tiukassa neulassa 0,15 oli noin 0,4 s nopeampi kuin 0,25, ja 0,40 pyörähti. Koko kierroksella 0,10–1,0 oli kohinaa ja 0 selvästi hitain. ● Noin 0,25–0,30 on toiminut pelissä usealla autolla. |
| Moottorijarrulukko | Mutkaan tulo vakautuu, ja perä rauhoittuu jarrutuksessa ja alas vaihdettaessa. | Keula työntää kaasu pois, ja lukko taistelee jarrulla kiertämistä vastaan. | ◐ Tiukassa neulassa 0–0,8 erosivat alle 0,1 s; vain takapyörien nopeusero muuttui. ● Kokemuksemme mukaan matala arvo sopii tyyliin, joka kiertää autoa jarrulla. |
| Preload | Siirtymät tasaantuvat: sisäpyörä sutii vähemmän ja perä rauhoittuu kytkin pohjassa. | Perä nykäisee kaasun avautuessa, ja auto aliohjaa kevyellä kaasulla. Tiukka neula pyörähti 150:llä tai enemmällä. | ◐ 0–520 oli kierroksella kohinaa; takapyörien nopeusero putosi 0,58:sta 0,27:ään. ◐ Preloadin ja lukon lasku hidasti luiston kasvua (55 → 42–44 °/s). ● Myös preload 0 on tuntunut pelissä hyvältä. |

## Säätöjärjestys ja mikä muu vaikuttaa

Säädä ensin kaasulukko, toisena moottorijarrulukko ja viimeisenä preload. Jokaisella on oma vaiheensa, ja preload hioo siirtymät niiden välillä.

1. **Kaasulukko** päättää ulostulon. Natiivimallissa 0 on selvästi hitain; tiukassa neulassa pienemmät arvot (noin 0,15) olivat nopeampia, keskinopeassa mutkassa noin 0,25. Kierroksella 0,10–1,0 on kohinaa.
2. **Moottorijarrulukko** päättää mutkaan tulon. Tiukassa neulassa 0–0,8 erosivat alle 0,1 s. Mutkan kulma ja kierto pysyivät samoina; vain takapyörien nopeusero muuttui. Jarrua pumpatessa lukko rauhoittaa perää.
3. **Preload** hioo siirtymät. Natiivimallissa 0–520 oli ajallisesti kohinaa, mutta takapyörien nopeusero kaasulla putosi 0,58:sta 0,27:ään. Sisäpyörän sutiminen laski noin 45 %:sta 23 %:iin. Tiukassa neulassa 150 tai enemmän pyörähti täydellä kaasulla.

**Mikä muu vaikuttaa diffin tuntumaan:**

| Säätö | Miten liittyy diffiin pelin fysiikassa |
| --- | --- |
| Välityssuhde ja vaihde | Lukko on osuus akselin väännöstä. Pieni vaihde kertoo väännön, joten sama kaasulukko lukitsee kakkosella paljon enemmän kuin nelosella. Tiukat neulat ajetaan pienellä vaihteella, joten siellä lukko tuntuu eniten. Preload ei muutu vaihteen mukana. |
| Kaasutekniikka | On/off-kaasulla vääntö hyppää heti täyteen, joten kaasulukko päättää käytöksen ja preload näkyy vain avauksen alussa. Osakaasulla preload painaa enemmän. |
| Kytkin ja vaihtaminen | Kytkin pohjassa T on nolla, joten ainoa lukko on preload. Kytkinvaihdoissa ja jarrutuksen alasvaihdoissa preload on ainoa lukko. |
| Jarrujako | Jarrut eivät kulje diffin läpi, mutta takapainotteinen jako hidastaa takapyöriä. Natiivimallissa etu 40 antoi 10–15 % enemmän kiertoa ja 1–2° enemmän tulokulmaa kuin 60. Takapainotteinen jarru ja matala moottorijarrulukko kiertävät autoa yhdessä eniten. |
| ABS | ABS rajaa takapyörien lukkiutumisen, joten jarrujaon ääripäät eivät muuttaneet kierrosaikaa natiivimallissa. |
| Takavakaaja ja takajouset | Jäykkä perä keventää sisäpyörää, joten se sutii helpommin ja kaasulukko kytkeytyy aiemmin. Pehmeämpi perä tarvitsee vähemmän lukkoa. |
| Moottorin vääntö | Enemmän vääntöä = enemmän kaasulukkoa newtonmetreinä samalla asetuksella. Preload on kiinteä, joten tehokkaassa autossa sen suhteellinen osuus pienenee. |

## Oireet

Etsi ensin vaihe, jossa oire tulee. Vaihe kertoo, mikä lukko on päällä. Muuta yhtä säätöä kerrallaan: kaasu- ja moottorijarrulukkoa 0,05, preloadia noin 50.

| Vaihe | Oire | Mitä pelissä tapahtuu | Muutos |
| --- | --- | --- | --- |
| Mutkaan tulo, kaasu pois | Keula työntää eikä auto käänny | Ulkopyörä pyörii nopeammin ja lukko jarruttaa sitä, mikä tekee oikaisevan momentin | Laske moottorijarrulukkoa. Jos se on jo matala, laske preloadia. |
| Mutkaan tulo, kaasu pois | Perä liikkuu tai potkaisee jarrutuksessa ja alasvaihdoissa | Takapyörät pyörivät eri tahtia eikä lukko tasaa niitä | Nosta moottorijarrulukkoa tai preloadia. Siirrä jarrujakoa eteen. |
| Kytkin pohjassa (vaihto, jarrutus) | Perä on levoton vain kytkin pohjassa | Ainoa lukko on preload | Nosta preloadia. |
| Keskikohta, kevyt kaasu | Auto aliohjaa ja haluaa suoraan | Ulkopyörä on nopeampi, joten lukko siirtää vääntöä sisäpyörälle. Tässä lukko on enimmäkseen preloadia. | Laske preloadia. |
| Kaasun avaus | Sisäpyörä sutii, kierrokset nousevat mutta auto ei vedä | Lukkoa ei ole tarpeeksi siirtämään vääntöä ulkopyörälle | Nosta preloadia (avauksen alku) tai kaasulukkoa (täysi kaasu). |
| Kaasun avaus | Perä nykäisee heti kun kaasu tulee | Preload sitoo pyörät yhteen ennen kuin vääntö nousee | Laske preloadia. |
| Ulostulo, täysi kaasu | Perä lähtee ja auto pyörähtää tiukassa neulassa | Lukko vie lähes kaiken väännön ulkopyörälle | Laske kaasulukkoa tai preloadia. |
| Ulostulo, täysi kaasu | Auto ei vedä ulos ja sisäpyörä sutii loivemmassa mutkassa | Lukko ei ehdi tasata pyöriä | Nosta kaasulukkoa 0,05. |

## Loppuvinkki

Natiivimallissa diffisäädöt tuskin muuttivat kierrosaikaa; vain kaasulukko 0 oli selvästi hidas. Valitse arvot sen mukaan, mikä on helpointa hallita. Tasainen drifti oli natiivimallissa hitaampi kuin pito (tiukassa mutkassa −15 %, keskinopeassa −6 %), mutta noin 20°:n luisto ulostulossa täydellä kaasulla oli nopein.

- Testaa aina samassa mutkassa samalla vaihteella, koska vaihde määrää lukon voiman.
- Jos auto pyörähtää täydellä kaasulla, katso ensin kaasulukkoa ja sitten preloadia. Molemmat työntävät perää ulos.
- Kokemuksemme mukaan kaasulukko 0,25–0,30, moottorijarrulukko 0,12–0,20 ja preload 45–100 on ollut pelissä helposti ajettava lähtöalue ●. Tougen diffipresetit kattavat tämän alueen sekä pehmeämmät ja jäykemmät sen ympärillä.

**Simulaatiokokemus ◐ (natiivimalli, ei pelissä testattu):** kun kaasulukko on yli 0, lukot ja preload ovat tuntumasäätöjä: kaasulukko 0,15–1,0, moottorijarrulukko 0–0,5 ja preload 0–250 pysyivät kaikki 0,4 s:n sisällä. Avoin diffi (kaasulukko 0) oli 2,4 s hitaampi, eniten hitaissa mutkissa. Poikkeus on jäykkä takavakaaja, joka halusi vähintään noin 0,3:n kaasulukon (ks. vakaajaluku).

## Varmistamatta

- Vääntö T on päätelty koko akselin väännöksi, ei todennettu.
- Natiivikuljettaja ajaa luiston eri tavalla kuin ihminen, joten tuntuma on varmistettava pelissä.

---

← [Camber ja toe](camber-and-toe.md) · [Sisältö](README.md) · [Korin dimensiot](body-dimensions.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
