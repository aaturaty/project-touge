[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../anti-roll-bars.md)

# Vakaajat

## Lyhyesti

Tässä pelissä vakaajat ovat alustan suurin vipu, ja etu–taka-jako ratkaisee enemmän kuin kokonaisjäykkyys. Kokemuksemme mukaan pelkkä jako voi muuttaa kierrosta useita sekunteja ◐, ja jaon siirto eteenpäin on rauhoittanut herkän perän pelissä ●. Vakaaja toimii vain, kun vasen ja oikea pyörä liikkuvat eri tavalla: kallistuksessa ja toispuoleisissa kuopissa.

Merkit: ● vahvistettu pelissä tai pelin koodissa, ◐ natiivimalli tai päätelty, ei pelissä testattu.

## Jäykkyys ja kallistus

**Näin peli laskee:**

1. Vakaaja on jousi vasemman ja oikean pyörän välissä: F = k · (x_oikea − x_vasen) ●. Kun molemmat pyörät liikkuvat yhtä paljon (suora jarrutus, kiihdytys, tasainen kuoppa), vakaaja ei tee mitään.
2. Pelin arvo × 2000 = vakaajan jäykkyys N/m ●. Yksi liukuriaskel kaksinkertaistaa arvon; minimi on puolet vakioarvosta ●.
3. Akselin kallistusjäykkyys = vakaaja k·t² + jousipari k·t²/2, ja renkaan pystyjäykkyys on näiden kanssa sarjassa ● (t = raideleveys). Sama vakaaja on leveämmällä raiteella jäykempi, neliössä.
4. Kallistuskeskiö on maan tasolla ●. Kaarteen kokonaiskuormansiirto on siksi aina m · a · h / t, eivätkä vakaajat pienennä sitä. Ne päättävät vain, kuinka paljon kori kallistuu ja kumpi akseli siirron kantaa.
5. Kallistus muuttaa camberia jousen liikkeen kautta ●, mutta camberin vaikutus pitoon on pieni ◐.

**Kun nostat molempia samassa suhteessa (jako pysyy):**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Molemmat vakaajat ylös | Vähemmän kallistusta ja nopeampi ohjausvaste. Raja tuskin muuttuu, koska kokonaissiirto pysyy samana. | Toispuoleiset kuopat ja gutterit heittävät autoa; sisäpyörä kevenee ja sutii. | ● Hyvin jäykkä takavakaaja tekee autosta kuoppaherkän. ◐ Molemmat hyvin pehmeinä oli hitaampi ja epävakaa. |
| Molemmat vakaajat alas | Enemmän kallistusta, ja auto rauhoittuu kuopissa. | Siirtymät (S-mutkat) laiskistuvat ja auto huojuu. | ◐ Natiivin tasainen ympyrä ei näytä kuoppaherkkyyttä; peli ratkaisee. |

## Etu–taka-jako

**Näin peli laskee:**

1. Etuakselin osuus kallistusjäykkyydestä (LLTD) on sama kuin sen osuus kaarteen kuormansiirrosta ●. LLTD 0,40 = keula kantaa 40 % siirrosta ja perä 60 %.
2. Akseli, joka kantaa enemmän siirtoa, menettää pitoa suhteessa toiseen: sen sisäpyörä kevenee, eikä renkaan sivujäykkyys kasva ulkopyörällä samassa suhteessa ● kaava, ◐ tulkinta. Jäykempi etu siirtää rajan keulaan, jäykempi taka perään.
3. Jako muuttaa koko auton rajaa: simulaattorissa sama auto ajoi pelkällä vakaajajaolla 1,08–1,64 g ◐. Rajan paikka riippuu autosta ja sen painopisteestä.
4. Kokemuksemme mukaan pidempi akseliväli haluaa etupainotteisemman jaon kuin lyhyt auto ●. Lyhyellä roadsterilla toimiva jako ei siirry sellaisenaan pidempään autoon.
5. Tavallisessa ajossa (0,8 g) ohjauskulma on sama kaikilla jaoilla ◐. Jako tuntuu rajalla sekä jarrutus- ja kaasusiirtymissä.

**Kun nostat:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Etuvakaaja | Keula kantaa enemmän siirtoa. Perä rauhoittuu nopeissa mutkissa ja raja tulee keulasta. Pitkällä autolla myös jarrutuksen ja trail brake -vaiheen aliohjaus vähenee. | Keula työntää tasaisissa mutkissa ja kaasulla nopeissa mutkissa. | ● Jaon siirto eteen korjasi herkän perän ja jarrutusaliohjauksen pelissä. ● Liian jäykkä etuvakaaja on maksanut lähes kaksi sekuntia. |
| Takavakaaja | Perä kääntää autoa: terävämpi sisäänohjaus ja vähemmän kaasu-aliohjausta. Nopeampi lyhyellä autolla. | Perä irtoaa "kuin katkaisijasta" sivukuormassa, pitkä auto aliohjaa jarrulla ja keskikohdan kaasu pyöräyttää sen. | ● Pehmeä etu ja jäykkä taka on ollut nopein lyhyillä autoilla. ◐ Jäykän takavakaajan reilu pehmennys maksoi useita sekunteja. |

Suunta on sama kuin oikeassa autossa, mutta raja on autokohtainen. Aloita auton akselivälistä, älä yleisestä "jäykempi etu" -säännöstä.

## Vaikutus muihin

Säädä jako ensin, sitten kokonaisjäykkyys. Myös jouset ja raide muuttavat kallistusjäykkyyttä, joten tarkista jako niiden muuttamisen jälkeen.

| Säätö | Miten liittyy vakaajiin pelin fysiikassa |
| --- | --- |
| Akseliväli | Pidempi auto tarvitsee etupainotteisemman jaon ●. |
| Painopisteen korkeus | Kuormansiirto on suoraan verrannollinen korkeuteen ●, joten jako ratkaisee korkealla autolla enemmän. |
| Etupaino | LLTD:tä verrataan etupainon osuuteen. Enemmän etupainoa ja etupainotteinen jako siirtävät samaa tasapainoa ◐. |
| Jouset | Jousipari on osa kallistusjäykkyyttä, joten jäykempi takajousi on myös jäykempi perä ●. Kokemuksemme mukaan vakaajat korjaavat tasapainon paremmin kuin jouset ◐. |
| Raide ja offset | Kallistusjäykkyys kasvaa raideleveyden neliössä ●. Leveämpi takaraide ottaa enemmän kallistusmomenttia mutta muuttaa pyöräkuormaa vähemmän ja lisää perän pitoa ◐. |
| Renkaat | Renkaan pystyjäykkyys on sarjassa vakaajan kanssa ●. Pehmeä tai matalapaineinen rengas pehmentää akselia hieman. |
| Diffi | Jäykkä perä keventää sisäpyörää, joka sutii, ja kaasulukko kytkeytyy aiemmin ◐. Jäykkä takavakaaja tarvitsee vähintään noin 0,3:n kaasulukon ◐. |
| Vaimentimet | Vakaaja päättää, kuinka paljon kuormaa siirtyy, slow-vaimentimet kuinka nopeasti. Pehmeä etu-rebound vähentää kaasu-aliohjausta samaan suuntaan kuin pehmeä etuvakaaja ◐. |

## Oireet

Etsi ensin mutkan vaihe, jossa oire tulee. Muuta yhtä vakaajaa kerrallaan noin 10–15 % ja aja sama mutka samalla vaihteella.

| Vaihe | Oire | Mitä pelissä tapahtuu | Muutos |
| --- | --- | --- | --- |
| Jarrutus mutkaan | Auto ei käänny jarrulla; trail brake vaatii voimaa | Pitkällä autolla takapainotteinen jako vie rajan väärään päähän ◐ ● | Nosta etuvakaajaa ja laske takavakaajaa. |
| Sisääntulo | Perä lähtee heti käännössä | Perä kantaa liikaa siirtoa | Laske takavakaajaa yksi askel (10–15 %). |
| Keskikohta | Keula työntää tasaisessa mutkassa | Keula kantaa liikaa siirtoa | Laske etuvakaajaa ●. |
| Keskikohta | Nopeassa mutkassa perä irtoaa "kuin katkaisijasta" | Raja tulee perästä ◐ | Nosta etuvakaajaa tai laske takavakaajaa. |
| Ulostulo, täysi kaasu | Keula työntää kaasulla nopeassa mutkassa | Etu on liian jäykkä suhteessa takaan ◐ | Laske etuvakaajaa. Jos se on jo matala, pehmennä etu-reboundia. |
| Ulostulo, kaasun avaus | Perä pyörähtää keskellä mutkaa kaasulla | Jäykkä perä keventää sisäpyörää ja diffi lukitsee | Laske ensin diffin preloadia ja kaasulukkoa ◐, sitten takavakaajaa. |
| Kuopat, reunat ja gutterit | Toispuoleinen kuoppa tai gutteri heittää perää | Vakaaja välittää yhden pyörän iskun toiselle | Laske taka slow reboundia, sitten takavakaajaa ◐. |

## Loppuvinkki

Etsi ensin jako ja vasta sitten kokonaisjäykkyys. Aloita auton akseliväliin sopivasta jaosta ja hio oireiden mukaan, yksi vakaaja kerrallaan. Lyhyt auto sietää jäykän perän ja nopeutuu sillä; pitkä auto tarvitsee etu ≥ taka.

Toimiva vakaajasetup pätee vain sen auton omilla jousilla ja renkailla, koska jouset ja raide ovat osa samaa kallistusjäykkyyttä. Jos vaihdat jouset, siirrä vakaajia niin, että jako pysyy.

**Simulaatiokokemus ◐ (natiivimalli, ei pelissä testattu):** pehmeä etu ja jäykkä taka oli nopein. Takavakaajan pehmennys jäykästä päästä maksoi 1–4 s, etuvakaajan jäykistys 0,7–1,2 s. Tee pehmeä keula vakaajalla, älä jousella: jäykkä etuvakaaja pehmeällä etujousella oli 1,7 s hitaampi. Tasapainomuutokset kyllästyvät: viisi samansuuntaista muutosta antoi yksitellen −2,3 s mutta yhdessä vain −1,2 s.

## Varmistamatta

- Miksi takapainotteinen jako aiheuttaa pitkälle autolle jarrutusaliohjausta, näkyy simulaatiossa, mutta mekanismi on auki ◐.
- Vakaajien vaikutus kuopissa ja guttereissa: simulaation tasainen ympyrä ei näytä sitä, joten peli ratkaisee.

---

← [Jouset](springs.md) · [Sisältö](README.md) · [Vaimentimet](dampers.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
