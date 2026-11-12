[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../body-dimensions.md)

# Korin dimensiot säädön apuna

## Lyhyesti

Korin dimensioita voi tuskin säätää, mutta ne kertovat, mistä setup kannattaa aloittaa. Isoin opetus on akseliväli: lyhyen roadsterin takapainotteinen vakaajajako ei siirtynyt pidempiin autoihin, ja akselivälin mukaan korjattu jako on toiminut pelissä yhdeksällä autolla ●. Raideleveys ja painopisteen korkeus päättävät, kuinka paljon kuormaa siirtyy, ja massa päättää, kuinka jäykät jouset tarvitaan samaan tuntumaan.

Ainoat säädettävät dimensiot ovat raideleveys (lokasuojaosa ja spacerit), painopiste (korin Stage, kevennys ja jousen pituus) ja massa. Kaikki muu tulee auton valinnan mukana.

Merkit: ● vahvistettu pelissä tai pelin koodissa, ◐ natiivimalli tai päätelty, ei pelissä testattu, ○ oikean auton teoria.

## Akseliväli

**Näin peli laskee:**

1. Pitkittäinen kuormansiirto on m · a · h / L ●. Lyhyt auto siirtää jarrutuksessa enemmän painoa eteen ja keventää perää enemmän kuin pitkä.
2. Lyhyt auto kiertyy helpommin, koska renkaiden vipuvarsi auton pystyakselin ympäri on lyhyempi ○. Siksi lyhyt auto kääntyy pienelläkin perän liikkeellä, ja pitkä auto tarvitsee enemmän keulaa.
3. Akseliväli on mukana Ackermann-geometriassa (pyöräkulma riippuu L:stä ja raiteesta) ●, mutta Ackermannilla ei ollut pitovaikutusta ◐.
4. Kokemuksemme mukaan etuakselin osuus kallistusjäykkyydestä (LLTD) miinus etupainon osuus siirtyy eteenpäin akselivälin kasvaessa ●. Lyhyt auto on toiminut takapainotteisella jaolla, pitkä tasaisella tai etupainotteisella.

**Mikä on toiminut pelissä akselivälin mukaan:**

| Akseliväli | Etuosuus kallistusjäykkyydestä − etupainon osuus |
| --- | --- |
| noin 2,3 m | noin −0,13 (selvästi takapainotteinen) |
| 2,4–2,5 m | noin −0,09…−0,06 |
| 2,5–2,6 m | noin −0,05…−0,02 |
| 2,7 m | noin +0,02…+0,03 (etupainotteinen) |

Vakaajalukuja ei voi verrata autosta toiseen, koska niihin vaikuttavat myös jouset, raide, massa ja painopiste. Vertaa jakoa, älä lukua.

Välityksissä lyhyet autot hyötyivät eniten noin 10 % pidemmästä loppuvälityksestä ◐. Tätä ei voi erottaa rajoittimesta, koska lyhyillä autoilla oli myös korkein rajoitin.

## Raideleveys ja offset

**Näin peli laskee:**

1. Sivuttainen kuormansiirto on m · a · h / t ●. Leveämpi raide siirtää vähemmän kuormaa ulkopyörälle, ja koska rengas menettää kitkaa kuorman kasvaessa, pito nousee.
2. Raide = auton perusleveys + offset, ja offset = korisarjan lokasuojaosa + spacer (cm) ●. Korisarja ei muuta fysiikassa mitään muuta, ei esimerkiksi ilmanvastusta ●. Part Setupin valkoinen offset-luku on pyöristetty kokonaisluvuksi ●.
3. Renkaan leveys ei siirrä pyörän kiinnityspistettä ●. Offsetin hyöty pienenee leveällä renkaalla: +0,20 m molemmilla akseleilla antoi 185 mm:llä +2,6 %, 245 mm:llä +1,9 % ja 285 mm:llä +1,6 % ◐.
4. Leveämpi akseli on kallistuksessa jäykempi (jousi- ja vakaajajäykkyys × t²), joten se ottaa suuremman osan kallistusmomentista ●. Sen pito silti nousee: taka +0,20 m siirsi etuosuuden 0,555 → 0,520 ja lisäsi pitoa 2,7 %, etu +0,20 m vain 0,5 % ◐.
5. Sääntö: renkaat eivät saa törröttää lokasuojan ulkopuolelle. Käytännössä tämä rajaa offsetia.

**Kun levennät:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Molemmat akselit | Pito nousee hieman kaikissa mutkissa. | Rengas lokasuojan ulkopuolella (säännön vastaista). | ◐ +0,10 m +1,4 %, +0,26 m +3,2 %. ◐ Koko reitillä hyöty näkyi vain kapeilla renkailla; muuten se oli kohinaa. |
| Vain taka | Perä pitää paremmin ja ulostulo rauhoittuu. | Auto alkaa aliohjata, jos keula on jo rajalla. | ◐ Taka +0,20 m +2,7 %. |
| Vain etu | Pieni pitovaikutus; keula ottaa osuutta perältä. | Keula on raskaampi kääntää. | ◐ Etu +0,20 m +0,5 %. ◐ Toisella autolla leveä raide vei etupitoa: −4 % tiukoissa mutkissa ja +3 % nopeissa. |

Tulokset eroavat autojen välillä, joten offsetin hyöty ei ole varma kaikilla autoilla ◐.

## Painopisteen korkeus

**Näin peli laskee:**

1. Massakeskiö = korilaatikon pohja + mass_up_percent × laatikon korkeus ●. Part Setupin "Center of Mass Height" on tämä prosentti, ei tuumia ●. Peli näyttää sen massapainotettuna, koska moottori ja vaihteisto pysyvät korin vakioarvossa ◐.
2. Painopiste muuttuu korin Stagen, kevennyksen (×0,99 / 0,97 / 0,95), korin vahvistuksen (×1,007–1,015) ja kevennyksen oman liukurin (askel ×1,05) mukana ●. Jousen pituus nostaa koria ja painopistettä 1 mm / mm ●.
3. Kuormansiirto on suoraan verrannollinen korkeuteen h, sekä sivuttain (m · a · h / t) että pitkittäin (m · a · h / L) ●. Matalampi on aina parempi, mutta säätövara on pieni: kevennysliukurin koko alue siirtää sitä noin 2,8 cm, eikä kierrosaika erottunut kohinasta ◐.
4. Korkea auto tarvitsee enemmän kallistusjäykkyyttä samaan kallistukseen, matala vähemmän. "touge weapon (oikea CoG)" -preset skaalaa kallistusjäykkyyttä auton painopisteen mukaan: korkea auto saa noin 30 % jäykemmät vakaajat, matalat 17–21 % pehmeämmät ◐ (ei pelissä testattu). Vanhempi touge weapon käyttää kaikille samaa vertailukorkeutta, ja pelissä toimineet setupit tehtiin sillä.
5. Aerolla ei ole ajokorkeusriippuvuutta ●, joten matala kori ei lisää alavoimaa.

**Kun lasket painopistettä:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Kevennys tai liukuri alas | Hieman vähemmän kallistusta ja kuormansiirtoa. | Ei fysiikkahaittaa. Liukuri siirtää samalla painojakaumaa ±1,6 %-yks. | ◐ Liukurin koko alue: kierros kohinaa. |
| Jousen pituus alas | Matalampi painopiste ja vähemmän siirtoa. | Jousitus lyö rajoittimeen, mikä maksaa paljon enemmän kuin painopiste antaa. | ◐ +20 mm pituutta = siirto +16 %, mutta pito nopeissa mutkissa ei muuttunut. ● Hieman pidempi etujousi on ollut pelissä yli kaksi sekuntia nopeampi. |

Ota siis painopiste huomioon vakaajien kokonaisjäykkyydessä, mutta älä tavoittele matalaa koria joustovaran kustannuksella.

## Massa ja painojakauma

**Näin peli laskee:**

1. Rengas menettää kitkakerrointa kuorman kasvaessa, joten raskaampi auto pitää suhteessa vähemmän: noin −2 % pitoa / 100 kg ●. Täysi Prototype-kevennys kertoo korin massan 0,805:llä ●, ja polttoainesäiliö lisää korin massaa 1–4 % ●.
2. Jousiluku on suoraan pyöräjäykkyys, joten raskaampi auto tarvitsee jäykemmän jousen samaan tuntumaan ●. Ominaistaajuus f = √(k / m) / 2π, missä m on massa yhdellä pyörällä ◐ laskettu. Samaan taajuuteen tarvittava jousi kasvaa suoraan pyörämassan mukana.
3. Sopiva vaimennus kasvaa suhteessa √(k · m) ○. Touge siirtää vaimentimet toiseen autoon vaimennussuhteella ζ, joten raskaampi auto saa automaattisesti suuremmat luvut ◐.
4. Painojakauma (etupaino) jakaa staattisen kuorman. Akselivälin suhde (etuosuus kallistusjäykkyydestä − etupaino) on suhteessa etupainoon, joten etupainoinen auto tarvitsee etupainotteisemman vakaajajaon samaan tasapainoon ●. Kevennysliukuri siirtää jakaumaa ±1,6 %-yks. ●.

**Mitä se tarkoittaa:**

| Tekijä | Mitä odottaa | Kokemus |
| --- | --- | --- |
| Raskaampi auto | Jäykemmät jouset ja suuremmat vaimentimet samaan tuntumaan, ja hieman vähemmän pitoa. | ● Noin 25 % raskaampi auto on toiminut noin 35 % jäykemmillä jousilla. |
| Etupaino ylös | Perä rauhoittuu kaasulla ja keula työntää helpommin. | ◐ Etupainoisempi auto ei pyörähtänyt täydellä kaasulla tiukassa mutkassa, jossa 50/50-auto pyörähti. ◐ Enemmän etupainoa oli vakiovakaajilla kaksi sekuntia nopeampi, korjatulla jaolla ei eroa. |
| Kevyempi auto | Enemmän pitoa suhteessa massaan ja lyhyempi jarrutus. | ● Kaava −2 % / 100 kg. |

Painojakauman tulos näyttää, että vakaajajako ja painojakauma tekevät samaa työtä. Kun jako on kohdallaan, jakauman muutos ei enää näy ◐.

## Dimensioista lähtöarvoihin

Näin siirrät toimivan setupin uuteen autoon sen dimensioiden avulla. Touge weapon -preset tekee vaiheet 2–6 automaattisesti, ja näin tehdyt setupit ovat toimineet pelissä ●.

1. **Kirjaa auton tiedot:** akseliväli, etu- ja takaraide, massa, etupaino ja Center of Mass Height (Part Setup).
2. **Jouset massasta:** pidä sama ominaistaajuus kuin toimivassa autossa. Noin 30 % raskaampi pyörä tarvitsee noin 30 % jäykemmän jousen ◐ laskettu.
3. **Jousen pituus auton oletuksesta:** etu ×1,07 ja taka ×0,90, kuten touge weaponissa ●.
4. **Vakaajajako akselivälistä:** käytä Akseliväli-osion taulukkoa. Kokonaisjäykkyys tulee halutusta kallistuksesta, ja korkea painopiste tarvitsee enemmän ◐.
5. **Raide lokasuojan sisällä:** offset niin leveäksi kuin lokasuoja sallii. Takavetoisessa takaraiteen levennys auttaa enemmän kuin etu ◐.
6. **Vaimentimet vaimennussuhteella:** sama ζ kuin toimivassa autossa, jolloin luvut kasvavat √(k · m):n mukana ◐.
7. **Välitykset:** lyhyellä autolla kokeile noin 10 % pienempää loppuvälitystä (FD × 0,90) ◐.

Hio tämän jälkeen oireiden mukaan: ensin vakaajat, sitten diffi, sitten jouset ja vaimentimet.

## Oireet

Nämä oireet tulevat setupista, joka on tehty erikokoiselle autolle. Korjaa ne vakaajilla, jousilla tai diffillä, koska dimensioita voi tuskin muuttaa.

| Vaihe | Oire | Mitä pelissä tapahtuu | Muutos |
| --- | --- | --- | --- |
| Jarrutus mutkaan | Pitkä auto aliohjaa jarrulla ja sitä joutuu kääntämään väkisin | Lyhyen auton takapainotteinen vakaajajako ei kierrä pitkää autoa | Siirrä vakaajajakoa eteen akselivälin mukaan ●. |
| Keskikohta, kova vauhti | Pitkä auto: perä irtoaa yllättäen isossa mutkassa | Raja tulee perästä, kun jako on liian takapainotteinen | Sama korjaus: jakoa eteen ●. |
| Ulostulo | Lyhyt, kevytperäinen auto pyörähtää kaasulla | Pieni etupaino ja lyhyt akseliväli tekevät perästä herkän | Laske diffin preloadia ja kaasulukkoa ◐, tai levennä takaraidetta. |
| Jarrutus | Lyhyt auto sukeltaa ja perä kevenee | Pitkittäinen siirto m · a · h / L on lyhyellä autolla suurempi | Siirrä jarrujakoa taakse ja lisää etujousen pituutta. |
| Sisääntulo | Korkea auto kallistuu ja on laiska | Korkea painopiste lisää sivuttaista siirtoa | Nosta vakaajien kokonaisjäykkyyttä samalla jaolla. |
| Kuopat ja reunat | Raskas auto lyö pohjaan ja huojuu | Jouset ja vaimentimet ovat massaan nähden liian pehmeät | Jouset taajuuden mukaan, vaimentimet samassa suhteessa. |

## Loppuvinkki

Katso uudesta autosta ensin akseliväli. Se kertoo, kuinka paljon toimivan setupin vakaajajakoa pitää siirtää, ja kokemuksemme mukaan pelkkä tämä korjasi herkän perän ja jarrutusaliohjauksen jokaisella touge weapon -sarjan autolla ●. Massa kertoo jousien ja vaimentimien tason, painopiste vakaajien kokonaisjäykkyyden.

Kokemuksemme mukaan jokainen 10 cm lisää akseliväliä on siirtänyt toimivaa kallistusjäykkyyden jakoa noin 4 %-yksikköä eteen, kunnes jako on noin 5 %-yksikköä etupainon osuutta edellä ●.

## Varmistamatta

- Akselivälin suhde sovitettiin kolmeen autoon ja testattiin pelissä yhdeksällä. Yli 2,7 m:n autoja ei ole kokeiltu, joten yläpää on arvio.
- Taajuus- ja vaimennussuhde-esimerkit on laskettu. Jousittamatonta massaa ei ole vähennetty pyörämassasta.
- Offsetin hyöty oli yhdellä autolla positiivinen ja toisella negatiivinen, ja syy on auki.
- Korjattu painopistelaskenta (touge weapon, oikea CoG) on testaamatta pelissä.
- Lyhyen akselivälin ja pidemmän välityksen yhteys voi johtua rajoittimesta.

---

← [Diffi](differential.md) · [Sisältö](README.md) · [Sanasto](glossary.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
