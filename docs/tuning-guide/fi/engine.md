[![Project Touge choriso's Tuning Bible](../banner.png)](README.md)

[In English](../engine.md)

# Moottori: osat, Part Setup -liukurit ja osakertoimet

## Lyhyesti

Luokka lasketaan huipputehosta, joten luokan rajalla nopein moottori on se, joka pitää lähes huipputehon laajimmalla kierrosalueella ◐. Moottorin säätö on iso vipu. Sama moottori sai simulaatiomallissa 1–10 s nopeamman North-kierroksen, kun osat ja liukurit haettiin reittiajalle eikä pelkälle keskiteholle ◐. Osien vaikutus vaihtelee moottorista toiseen piilotetun osakertoimen mukaan, jota peli ei näytä ●.

## Näin peli laskee

1. Jokaisella moottorilla on vääntökäyrä ja viisi solmua: alku, Low, Mid, High ja loppu. Osat ja liukurit lisäävät solmuihin newtonmetrejä, ja käyrä interpoloidaan suoraan solmujen välillä ●.
2. Osat ja liukurit summautuvat, eivät kerro: statti = perusarvo × (1 + Σ (osan kerroin − 1) × f + Σ askeleet × (askeleen kerroin − 1) × f) ●. Sama pätee massaan ●.
3. f on moottorin **osakerroin** (part_stat_factors). Se on jokaisella moottorilla oma ja paikkakohtainen, eikä peli näytä sitä missään ●. Taulukko on tämän luvun lopussa.
4. Teho voi laskea vakiosta vain Prototype-osien liukureilla. Muiden osien liukurit menevät vain plussalle ●.
5. Luokka lasketaan huipputehosta vakiopolttoaineella (hv / tonni, C3 = 200–250). Huipputeho luetaan käyräpisteistä rajoittimeen asti ●.
6. Kilpapolttoaine venyttää käyrää kierrosakselilla (vääntö ×1,10 ja rajoitin ×1,05). Se ei muuta luokkaa, mutta tuo lisää tehoa korkeille kierroksille ●.
7. Turbon ahto on täysi noin 3150–5400 rpm ja hiipuu sen yläpuolella ●. Tehdasturbon ahtoa voi laskea vain Prototype-ECU:lla ●.

**Prototype-osien liukurit ● (askeleet: miinus / plus):**

| Osa | Liukuri | Askel | Alue |
| --- | --- | --- | --- |
| ECU [P] | Rajoitin | +2,2 % × f | −6 … +6 |
| ECU [P] | Ahto (vain turbo) | +6 % × f | −14 … +6 |
| Lohko [P] | Low-vääntö | +3 % × f | −12 … +6 |
| Kansi [P] | Mid-vääntö | +4,5 % × f | −14 … +4 |
| Nokka [P] | High-vääntö | +5 % × f | −16 … +3 |
| Imusarja [P] | Peak RPM (käyrän taittuma) | +2,4 % × f | −6 … +6 |

## Kun nostat

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Low ylös, High alas | Käyrä tasoittuu: sama huipputeho, mutta enemmän tehoa mutkista ulos. | Huippu siirtyy alas ja yläpää loppuu ennen vaihtoa. | ◐ Kaikkien parhaiden C3-buildien liukurit olivat tätä muotoa, esim. Mini S15:ssä Low +5,6, Mid −8,4, High −16. |
| Rajoitin | Vaihde pitenee ja vaihtoja tulee vähemmän. | Jos käyrä on jo taittunut, rajoittimen lisäkierroksilla ei ole tehoa. | ◐ Haku nosti rajoitinta useimmilla koneilla (Mini +3,6, ND +3,4, Lotus ja 4A-GE +6), mutta Datsunilla ja S02:lla laski. |
| Ahto alas | Keskikierrosten huippu laskee, ja luokkaan mahtuu kevyempänä. | Alapää tyhjenee. | ◐ RDA ja Mini käyttivät 0,35–0,63 bar. |
| Peak RPM | Taittuma siirtyy ylös, ja yläpää kantaa pidempään. | Huipputeho nousee ja luokka ylittyy. | ◐ Parhaissa buildeissa usein alas (−6), jotta huipputeho pysyy rajalla. |

## Vaikutus muihin ja hakujärjestys

| Tekijä | Miten liittyy moottoriin |
| --- | --- |
| Osakerroin | Isompi kerroin liikuttaa käyrää enemmän per askel, joten käyrää saa muokattua tasaisemmaksi. Pieni kerroin rajaa sekä nostoa että laskua. |
| Massa ja luokka | Liian vahva moottori pakottaa lisäämään massaa (säiliö, kevennysliukuri), ja se maksaa enemmän kuin vahvempi käyrä tuo. |
| Prototype-imusarja | Imusarjan kerroin on muita suurempi, ja se nostaa tehoa. Vahvalla koneella sen jättäminen vakioksi voi olla nopeampaa kuin [P] ja liukuri miinuksella ◐. |
| Välitykset | Tasainen ja leveä käyrä sietää harvemman laatikon. Kapea käyrä tarvitsee tiheät välit (katso Välitykset). |

**Min-max-järjestys (◐, haku North v2:lla):**

1. Prototype-ECU, -nokka, -kansi ja -lohko, koska vain niillä saa tehoa alas. Imusarja [P] vain, jos moottori ei ole valmiiksi liian vahva.
2. Low ylös, Mid ja High alas, ja Peak RPM niin, että huipputeho osuu juuri luokan rajalle.
3. Rajoitin niin korkealle kuin käyrä kantaa, turbokoneilla ahto alas, kunnes keskikierrosten kyttyrä tasoittuu.
4. Kevennys täysin päälle ja säiliö vakio. Jos teho ei mahdu, laske ensin liukureita ja lisää massaa vasta viimeisenä.

## Moottorit luokan rajalla (◐, alustava)

Haku 17.11. Tougen reittimallilla North v2:lla C3:ssa (S15 ja AE86). Jokaisella moottorilla haettiin osat, liukurit, kevennys ja säiliö 12 lähtöpisteestä, ja tulosta verrattiin Tougen omaan sovitukseen. Simulaatiomallin tulos, ei vielä natiivissa tai pelissä ajettu.

| Moottori | Vakiona autossa | S15 ero kärkeen | AE86 ero kärkeen | Ero Tougen omaan sovitukseen | Natiivi S15 / AE86 vs nykyinen |
| --- | --- | --- | --- | --- | --- |
| N14B | MCS | 0,0 | 0,0 | −6…−8 s | +1,7 ± 0,3 / −0,2 ± 0,3 |
| PV2 | MX-5 ND | +0,6 | +0,6 | −3…−5 s | +0,4 ± 0,3 / −0,9 ± 0,1 |
| DL20 | DTS | +1,6 | +1,6 | −6…−8 s | +3,3 ± 0,2 / +1,0 ± 0,2 |
| RDA | FST | +0,7 | +1,2 | −0,1…−0,4 s | +1,4 ± 0,2 / +0,1 ± 0,2 |
| GE4 | E86 | +2,0 | +1,6 | −1…−3 s | – / +1,1 ± 0,2 |
| 2ZG | LTS | +2,2 | +2,6 | −5…−7 s | – |
| B13 | FX7 | +2,3 | +2,5 | −9…−10 s | – |
| S02 | 20R | +2,9 | +2,8 | −4…−6 s | – |
| BM13 | DX8 | +2,4 | +4,1 | −0,2…−0,4 s | – |

**Natiivi 17.11. (8 toistoa, ◐):** malli ja natiivi eivät ole samaa mieltä. S15:ssä nykyinen ND-säätö oli nopein, ja Mini oli 1,7 s hitaampi. AE86:ssa ND-moottori mallin säädöillä oli 0,9 ± 0,1 s nykyistä 4A-GE-säätöä nopeampi, ja Mini oli kohinan sisällä. Mallin kärkijärjestystä ei siis voi vielä käyttää; varmin löydös on ND-moottori (PV2) kevyessä takavetoisessa. Uusinta AE86:n nykyisellä setupilla (välitykset 2,91/2,04/1,51/1,15/0,97/0,86, jarrulukko 0,28) antoi FD 4,50:llä ±0, FD 4,35:llä −1,0 ± 0,1 s ja muilla FD:illä −0,3…−0,4 s, joten etu riippuu välityksistä eikä ole vielä varma. **Pelikoe 17.11. (●, AE86, North v2):** GE4 ajot 43–44 371,36 / 371,20 s. PV2 pelaajan omalla säädöllä (rajoitin 8687 ja Peak RPM 9742 täysillä, High 218, Medium 281, Low 332): FD 4,52 ajot 45–46 372,97 / 370,97 s, **FD 4,35 ajot 47–48 369,03 / 369,22 s (−2,1 s GE4:ään, toistui)**. Natiivi ennusti FD 4,35:lle −1,0 ± 0,1 s, eli suunta osui. Mallin Part Setup -arvoja ei ajettu pelissä. Pelaaja vaihtaa ylös noin 8800–9000 rpm:ssä ja ajaa 15–25 % kierroksesta yli 8500 rpm:n, joten rajoittimen laskeminen on todennäköisesti haitallista, vaikka mallit eivät sitä näe ◐. Toistaiseksi luotettavin linja: rajoitin ja Peak RPM ylös, Low ylös, Mid ja High alas, kunnes luokka täyttyy. Mallin mukaan korkean osakertoimen moottorit (Mini 0,84 + turbo 1,6, ND ja Datsun 0,89) hyötyvät liukureista eniten. Tougen nykyinen sovitus jättää niistä 3–10 s.

## Miksi sama luokka, eri aika (Supra-testi 17.11., ◐)

Luokka mittaa huipputehoa painoon nähden (hv/t), mutta Northilla aika ratkeaa mutkista ulos kiihdytettäessä. Testissä 30 suosittua moottoria (kaksi erää) Supra A90:ssä (paino riittää kaikille), jokainen säädetty mallissa luokan rajalle omilla välityksillään ja ajettu natiivissa (8 toistoa, North v2) sekä suoralla kiihdytyskokeella tasaisella tiellä.

| Moottori | Vakiona autossa | North ero (s) | 60–150 km/h (s) | 100–200 km/h (s) | Huippunopeus (km/h) | Massa (kg) | Turbo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2TS | V7G | −3,8 | 5,04 | 8,90 | 257 | 903 | tehdas |
| G1E6 | YRS | −3,4 | 5,09 | 8,99 | 255 | 889 | tehdas |
| GU4 | R86 | −3,0 | 5,15 | 8,95 | 259 | 952 | – |
| DL20 | DTS | −3,0 | 5,07 | 8,93 | 259 | 925 | kit |
| N14B | MCS | −2,8 | 5,15 | 9,09 | 255 | 894 | tehdas |
| S02 | 20R | −2,7 | 5,22 | 8,85 | 260 | 947 | – |
| B1A6 | V45 | −2,6 | 5,12 | 9,20 | 257 | 914 | kit |
| RS20T | S13 | −2,6 | 5,23 | 9,03 | 259 | 945 | tehdas |
| E25 | SFR | −2,6 | 5,06 | 8,99 | 256 | 891 | tehdas |
| RS20 | Swap | −2,5 | 5,23 | 8,98 | 260 | 959 | kit |
| RS20T | S15 | −2,4 | 5,40 | 9,37 | 256 | 953 | tehdas |
| 4A-GE | Swap | −2,2 | 5,30 | 9,44 | 254 | 908 | kit |
| 46G3 | EV6 | −2,0 | 5,32 | 9,20 | 257 | 944 | tehdas |
| DA15 | HC6 | −1,9 | 5,36 | 9,28 | 256 | 903 | kit |
| GE4 | E86 | −1,7 | 5,28 | 9,10 | 257 | 908 | – |
| S1B4 | M30 | −1,3 | 5,28 | 9,30 | 256 | 905 | – |
| 2ZG | LTS | −1,2 | 5,36 | 9,10 | 257 | 904 | – |
| RDA | FST | −1,2 | 5,18 | 8,80 | 262 | 1009 | tehdas |
| G64 | ECL | −0,9 | 5,38 | 9,26 | 258 | 941 | – |
| PV2 | MX-5 ND | −0,6 | 5,32 | 9,33 | 255 | 898 | – |
| GE3 | 2MR | −0,4 | 5,37 | 9,11 | 256 | 902 | – |
| BR13 | DX7 | −0,3 | 5,44 | 9,48 | 260 | 966 | tehdas |
| KA20 | HCR | +0,3 | 5,07 | 8,57 | 266 | 1041 | – |
| BM13 | DX8 | +0,4 | 5,47 | 9,70 | 256 | 961 | – |
| F2C0 | HS2 | +0,5 | 5,37 | 9,21 | 260 | 955 | – |
| 4G63 | Swap | +0,8 | 5,25 | 8,85 | 264 | 1067 | tehdas |
| ME10 | B19 | +0,8 | 5,58 | 9,74 | 253 | 923 | – |
| B13 | FX7 | +0,9 | 5,55 | 10,14 | 253 | 911 | tehdas |
| B1B6 | HC9 | +1,5 | 5,40 | 9,44 | 260 | 943 | – |
| B411T | EVX | +3,6 | 5,21 | 8,72 | 269 | 1113 | tehdas |

North-ero on verrattu pelissä ajettuun S02-säätöön (975 kg); mallin säädöt ovat ~28 kg kevyempiä (säiliö 0, kevennys täysi), joten moottorien keskinäinen järjestys on luotettavampi kuin ero nollaan. Massa on auton kokonaismassa mallin säädöllä; 60–150 on paras mallin välityksistä ja pitkän kutosen sarjasta.

**Mitä tästä seuraa:**

1. **60–150 km/h ennustaa Northin ajan, kun moottori ei lihota autoa** (alle 1000 kg: korrelaatio 0,85; 0,1 s nopeampi 60–150 ≈ 0,9 s nopeampi kierros). Raskaat koneet (RDA, Civic Type R, 4G63, Evo X, 1009–1113 kg) ovat suoralla kärjessä mutta Northilla hitaita: kaikilla 30:llä korrelaatio on vain 0,53, ja 60–150 + massa yhdessä 0,83 (10 kg ≈ 0,2 s kierroksella). 100–200 km/h ennustaa heikosti (0,25) ja huippunopeus ei lainkaan: ilmanvastus rajaa kaikki 253–269 km/h:iin.
2. **Turbo antaa keskikierroksilla vääntöä, jota luokka ei laske täysimääräisesti.** Kymmenen kärjestä kahdeksan on turbollisia (tehdasturbo tai haun valitsema turbokit). Turbo ei pelasta raskasta konetta: RDA, 4G63 ja Evo X maksavat massallaan mutkissa.
3. **Vapaasti hengittävillä ratkaisee käyrän tasaisuus vaihtovälillä** (70–100 % rajoittimesta): S02 ja GE4 (keskiteho 96 % huipusta) parhaat, EK9 (81 %), 190E (89 %) ja Eclipse (90 %) hitaimmat.
4. **Moottorijarru ja inertia eivät selitä eroja**: pelin datassa ne ovat samat kaikilla moottoreilla ●.
5. **Auto ratkaisee.** S15:ssä sama natiivi antoi päinvastaisen tuloksen (DL20 +3,3, Mini +1,7 vs ND). Kevyempi auto ei mahdu luokkaan yhtä vahvalla turbokoneella. Testaa kärkiehdokkaat omalla autollasi, ja hae FD uudelleen vaihdon jälkeen.

Touge käyttää tätä moottorivalinnassa 0.12.0:sta alkaen ◐. Malli vaihtaa ylös noin 0,90 × rajoitin, kuten pelaaja ja natiivi, ja osat ja liukurit sovitetaan luokkaan pienimmän kiihdytysajan ja massan mukaan eikä enää suurimman keskitehon mukaan. Natiivissa paras ennustaja on natiivin oma 60–150, mutta mallissa 50–120 km/h + massa seuraa natiivin North-aikaa parhaiten (Supra 90 buildia r 0,85, S15 r 0,92; mallin 60–150 r 0,73), koska malli ja natiivi eroavat 1. vaihteen kiihtyvyydessä. Natiivitarkistus North v2:lla: Suprassa uudet buildit olivat keskimäärin 0,4 s nopeampia kuin aiemman haun, ja natiivin 8 parhaasta moottorista 6 on valinnan 12 kärjessä (ennen 2). S15:ssä valinnan neljä parasta olivat keskimäärin 0,35 s nopeampia kuin ennen, mutta paras yksittäinen (Forester, vanha sovitus) jäi uudesta 0,5 s. Mikään ehdokas ei ollut nykyistä S15-säätöä (ND-moottori) nopeampi.

Kaksi tarkennusta 18.11. ◐. **Kierrosrajaa ei lasketa valinnassa:** 50–120-sovitus laski turbomoottoreilla rajoittimen liukuria (Forester 7432 → 6630 rpm) ja osti sillä vähän vääntöä, mutta natiivissa matala raja hävisi nopeissa osioissa: Forester AE86 −1,8 s ja S15 −0,4 s, kun rajaa ei lasketa, ja Suprassa korkean rajan build oli 4,0 s nopeampi. **Viimeistely:** kolme parasta ehdokasta hiotaan lopuksi reittiajalla käyttäjän kevennys- ja säiliöasetuksilla, ja build lukitaan. Natiivissa viimeistelty Forester oli S15:ssä 3,9 s ja Suprassa 4,0 s nopeampi kuin viimeistelemätön. Suprassa Tougen suositus (ND tai Forester) oli natiivissa 2,6–2,8 s nykyistä säätöä (GT-R-moottori) nopeampi. AE86:ssa ja S15:ssä nykyinen ND-moottori pysyi nopeimpana: mallin ehdotukset jäivät siitä natiivissa 0,7–2,8 s. Malli siis löytää hyvät moottorit, mutta alle 1 s:n erot sen ennusteissa eivät ole luotettavia. Kokeile suositusta pelissä ennen kuin vaihdat toimivan moottorin.

Pelissä varmistamatta.

## Osakertoimet moottoreittain ●

Kaikki 137 moottoria pelidatasta (part_stat_factors), suurimmasta pienimpään. Osakerroin on sama ECU:lle, nokalle, kannelle, lohkolle ja polttoainejärjestelmälle. Mediaani on 0,74, pienin 0,20 ja suurin 1,09. Turbo-osa = Turbo Kitin tai tehdasturbon osan kerroin. Moottori on pelin moottorikoodi (nimen alku, esim. RDA nimessä "RDA 2.0L L4 T (FST)"), Vakiona autossa on sen auton pelikoodi, jossa moottori on vakiona, ja Swap tarkoittaa swap-moottoria. – Moottori-sarakkeessa: pelidatassa ei vielä ole moottorin nimeä sille autolle.

| Moottori | Vakiona autossa | Tehdasturbo | Massa kg | Rajoitin | Osakerroin (ECU, nokka, kansi, lohko, polttoaine) | Imusarja | Pakosarja ja pakoputki | Turbo-osa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B13 | FX7 | ● | 157 | 8500 | 1,09 | 1,38 | 1 | 1,5 |
| DT 18 | S18 | ● | 268 | 7200 | 1,09 | 1,38 | 1 | 1,5 |
| DT 18 (Spirit) | – | ● | 268 | 7200 | 1,09 | 1,38 | 1 | 1,5 |
| DA15 | HC6 |  | 140 | 7800 | 1 | 1,3 | 0,9 | 1 |
| L08 | L08 |  | 127 | 6000 | 1 | 1,3 | 0,9 | 0,5 |
| VGD3 | 30Z | ● | 220 | 6800 | 0,98 | 1,28 | 0,88 | 1,5 |
| VGD3 | 30ZC | ● | 220 | 6800 | 0,98 | 1,28 | 0,88 | 1,5 |
| RS20T | S14 | ● | 180 | 7500 | 0,95 | 1,25 | 0,85 | 1,5 |
| B70 | MF1 |  | 275 | 7600 | 0,95 | 1,16 | 0,78 | 0,5 |
| RS20T | S13 | ● | 180 | 7500 | 0,91 | 1,25 | 0,81 | 1,5 |
| 46G3 | EV6 | ● | 170 | 7600 | 0,9 | 1,24 | 0,8 | 1,5 |
| 97M1 | P91 | ● | 230 | 7300 | 0,9 | 0,86 | 0,8 | 1,5 |
| BL58 | S90C | ● | 140 | 7000 | 0,9 | 1,2 | 0,8 | 1,5 |
| – | Ferrari F40 | ● | 210 | 7500 | 0,9 | 1,2 | 0,8 | 0,5 |
| B1A6 | V45 |  | 140 | 6500 | 0,9 | 1,2 | 0,8 | 0,5 |
| C2L | BGX |  | 200 | 6200 | 0,89 | 1,19 | 0,79 | 1,5 |
| PV2 | MX-5 ND |  | 130 | 7200 | 0,89 | 1,19 | 0,79 | 1,5 |
| DT20 | 31R | ● | 230 | 7600 | 0,89 | 1,19 | 0,79 | 1,5 |
| E25 | SFR | ● | 120 | 6500 | 0,89 | 1,18 | 0,79 | 1,5 |
| 4A-GE | Swap |  | 145 | 7400 | 0,89 | 0,89 | 0,89 | 0,89 |
| 4G63 | Swap | ● | 175 | 7500 | 0,89 | 0,89 | 0,89 | 0,89 |
| D15B | Swap |  | 150 | 7700 | 0,89 | 0,89 | 0,89 | 0,89 |
| GE4 | E86 |  | 154 | 7400 | 0,89 | 1,19 | 0,79 | 0,5 |
| DL20 | DTS |  | 160 | 6200 | 0,89 | 1,19 | 0,79 | 0,5 |
| PF1 | NX5 |  | 155 | 7200 | 0,89 | 1,19 | 0,79 | 0,5 |
| PF1 | NX5C |  | 155 | 7200 | 0,89 | 1,19 | 0,79 | 0,5 |
| ME10 | B19 |  | 170 | 6600 | 0,89 | 1,19 | 0,79 | 0,5 |
| GE3 | 2MR |  | 143 | 7000 | 0,89 | 1,19 | 0,79 | 0,5 |
| DT20 | 32R | ● | 230 | 7400 | 0,86 | 1,2 | 0,8 | 1,5 |
| E25 | WRS | ● | 125 | 7400 | 0,86 | 1,14 | 0,77 | 1,5 |
| LL1 | CC3 |  | 280 | 6200 | 0,85 | 1,04 | 0,81 | 1,5 |
| RV30 | IF6 | ● | 195 | 6800 | 0,85 | 1,19 | 0,75 | 1,5 |
| G1E6 | YRS | ● | 120 | 7200 | 0,85 | 1,04 | 0,81 | 1,5 |
| M17 | AMV | ● | 209 | 8000 | 0,85 | 1,2 | 0,75 | 1,5 |
| G64 | ECL |  | 185 | 6500 | 0,85 | 1,14 | 0,75 | 0,5 |
| N14B | MCS | ● | 130 | 6500 | 0,84 | 1,14 | 0,74 | 1,6 |
| RS20T | S15 | ● | 180 | 7500 | 0,83 | 1,11 | 0,74 | 1,5 |
| RS20T (Spirit) | – | ● | 180 | 7500 | 0,83 | 1,11 | 0,74 | 1,5 |
| 30S | FLD |  | 249 | 7000 | 0,83 | 1,12 | 0,73 | 0,5 |
| JAZ22 | S80 | ● | 230 | 7000 | 0,82 | 1,1 | 0,73 | 1,5 |
| TF25 | TTR | ● | 160 | 6800 | 0,81 | 1,07 | 0,72 | 1,5 |
| DT25 | 34R | ● | 250 | 7000 | 0,81 | 1,08 | 0,72 | 1,5 |
| GU4 | G86 |  | 200 | 7400 | 0,81 | 1,08 | 0,72 | 0,5 |
| 6T9 | ARG | ● | 240 | 7200 | 0,8 | 0,91 | 0,57 | 1,5 |
| – | B8I | ● | 210 | 6500 | 0,8 | 1,05 | 0,72 | 1,5 |
| 2TS | V7G | ● | 140 | 6000 | 0,8 | 1,1 | 0,7 | 1,5 |
| – | S65 | ● | 186 | 7500 | 0,8 | 1,06 | 0,7 | 1,5 |
| S02 | 20R |  | 199 | 7300 | 0,8 | 1,06 | 0,7 | 1,5 |
| MT64 | P64 | ● | 150 | 7100 | 0,8 | 1,07 | 0,71 | 1,5 |
| L1R | LFL |  | 160 | 9000 | 0,8 | 1,15 | 0,7 | 0,5 |
| RS20 | Swap |  | 190 | 7200 | 0,79 | 1,09 | 0,69 | 0,5 |
| RDA | FST | ● | 109 | 6500 | 0,78 | 1,06 | 0,68 | 1,5 |
| E20J7 | WST | ● | 204 | 8000 | 0,78 | 1,06 | 0,68 | 1,5 |
| PV8 | PF7 |  | 270 | 5000 | 0,78 | 1,08 | 0,68 | 0,5 |
| BR13 | DX7 | ● | 120 | 8300 | 0,77 | 1,03 | 0,68 | 1,5 |
| BR13 (Spirit) | – | ● | 120 | 8300 | 0,77 | 1,03 | 0,68 | 1,5 |
| BL58 | S90 | ● | 140 | 7000 | 0,765 | 1,02 | 0,68 | 1,5 |
| CV6 | 6RS | ● | 190 | 6700 | 0,75 | 1 | 0,66 | 1,5 |
| E82A | 7RS | ● | 190 | 6700 | 0,75 | 1 | 0,66 | 1,5 |
| S58 | BM2R | ● | 160 | 6800 | 0,75 | 1,15 | 0,66 | 1,5 |
| S58 | M3G | ● | 160 | 6800 | 0,75 | 1,15 | 0,66 | 1,5 |
| EBT | FGT | ● | 205 | 7000 | 0,75 | 0,99 | 0,67 | 1,5 |
| 2ZG | LTS |  | 140 | 8200 | 0,75 | 1,15 | 0,66 | 1,5 |
| DE27 | 63C | ● | 367 | 6800 | 0,75 | 1 | 0,67 | 1,5 |
| GT63 | EV9 | ● | 195 | 7500 | 0,75 | 1,02 | 0,66 | 1,5 |
| FA6 | SZK |  | 100 | 7800 | 0,75 | 1,15 | 0,66 | 1,5 |
| BM13 | DX8 |  | 120 | 8300 | 0,75 | 1,05 | 0,65 | 0,5 |
| B30 | M92C | ● | 135 | 6800 | 0,74 | 1 | 0,66 | 1,5 |
| B30 | M92 | ● | 135 | 6800 | 0,74 | 1 | 0,66 | 1,5 |
| B411T | EVX | ● | 134 | 7800 | 0,74 | 1,02 | 0,64 | 1,5 |
| RV38 | 35R | ● | 276 | 7500 | 0,73 | 0,97 | 0,65 | 1,5 |
| U2R | LRC |  | 222 | 7600 | 0,73 | 0,97 | 0,65 | 0,5 |
| B28 | M36 |  | 180 | 6600 | 0,72 | 1 | 0,63 | 0,5 |
| CPTAV10 | AR8 | ● | 250 | 7800 | 0,7 | 1,05 | 0,6 | 1,5 |
| B55N | BM2 | ● | 194 | 7500 | 0,7 | 0,95 | 0,62 | 1,5 |
| FSP | LMH | ● | 250 | 8000 | 0,7 | 1,05 | 0,6 | 1,5 |
| LL1 | CMR |  | 193 | 6400 | 0,7 | 0,96 | 0,6 | 0,5 |
| F2C0 | HS2 |  | 147 | 8300 | 0,7 | 1 | 0,6 | 0,5 |
| FUZ 1 | CRN |  | 195 | 7200 | 0,7 | 1,05 | 0,6 | 0,5 |
| B58 | M4R | ● | 140 | 7000 | 0,69 | 0,94 | 0,61 | 1,5 |
| M7GT | S70 | ● | 270 | 6800 | 0,68 | 1,08 | 0,59 | 1,5 |
| B1B6 | HC9 |  | 184 | 8500 | 0,66 | 0,92 | 0,57 | 0,5 |
| KA20 | HCR |  | 145 | 8100 | 0,66 | 0,92 | 0,57 | 0,5 |
| 2JZ-GTE | – | ● | 310 | 7000 | 0,65 | 0,87 | 0,55 | 1,5 |
| – | TAL |  | 240 | 7100 | 0,65 | 0,95 | 0,55 | 1,5 |
| FC3 | HRD | ● | 195 | 7200 | 0,65 | 0,94 | 0,61 | 1,5 |
| – | Z40 | ● | 240 | 6800 | 0,65 | 1 | 0,55 | 1,5 |
| JAZ11 | CRT | ● | 210 | 7000 | 0,65 | 0,95 | 0,55 | 1,5 |
| JAZ11 | TM2 | ● | 210 | 7000 | 0,65 | 0,95 | 0,55 | 1,5 |
| JAZ11 | TSR | ● | 240 | 7100 | 0,65 | 0,95 | 0,55 | 1,5 |
| S1B4 | M30 |  | 136 | 6750 | 0,65 | 0,9 | 0,57 | 0,65 |
| BS38 | BZ4 |  | 220 | 8000 | 0,65 | 0,94 | 0,61 | 0,5 |
| BS38 | M34 |  | 151 | 6900 | 0,65 | 0,91 | 0,55 | 0,5 |
| GU4 | R86 |  | 171 | 7200 | 0,65 | 0,9 | 0,56 | 0,5 |
| GCTM1 | C70 |  | 242 | 7500 | 0,64 | 0,94 | 0,54 | 0,5 |
| MDA | MGTC | ● | 209 | 7000 | 0,6 | 0,85 | 0,52 | 1,5 |
| 15M7 | GLW | ● | 220 | 6500 | 0,6 | 0,65 | 0,5 | 1,5 |
| MDA | MGT | ● | 209 | 7000 | 0,6 | 0,84 | 0,52 | 1,5 |
| V30G | Z31 | ● | 178 | 6000 | 0,6 | 0,85 | 0,51 | 1,5 |
| KA20 | HI5 |  | 180 | 8000 | 0,6 | 0,9 | 0,5 | 0,5 |
| BC32 | HSX |  | 200 | 8000 | 0,59 | 0,84 | 0,5 | 0,5 |
| BV8 | CHR |  | 281 | 6400 | 0,59 | 0,86 | 0,5 | 0,5 |
| LMV12 | LMD |  | 232 | 7300 | 0,58 | 0,96 | 0,48 | 0,5 |
| SB53 | M46 |  | 149 | 7000 | 0,57 | 0,855 | 0,475 | 0,5 |
| S58 | M4G | ● | 160 | 6800 | 0,55 | 0,8 | 0,46 | 1,5 |
| – | MLN | ● | 170 | 8500 | 0,55 | 0,79 | 0,47 | 1,5 |
| – | M39 |  | 208 | 7000 | 0,55 | 0,8 | 0,45 | 0,5 |
| A12J6 | JGR |  | 240 | 7500 | 0,55 | 0,81 | 0,47 | 0,5 |
| SCHM | HSS |  | 240 | 6500 | 0,55 | 0,79 | 0,47 | 0,5 |
| – | Ford Mustang S197 |  | 245 | 7000 | 0,55 | 0,76 | 0,38 | 0,5 |
| QH37 | Z37 |  | 174 | 6800 | 0,55 | 0,81 | 0,46 | 0,5 |
| VV53 | VP1 |  | 230 | 6300 | 0,55 | 0,79 | 0,47 | 0,5 |
| ES8 | STR |  | 245 | 7250 | 0,53 | 0,78 | 0,45 | 0,5 |
| FV8 | F69 |  | 290 | 6200 | 0,52 | 0,77 | 0,43 | 0,5 |
| S6B34T | M90 | ● | 229 | 8250 | 0,5 | 0,75 | 0,4 | 1,5 |
| S6B34 | BX5 | ● | 229 | 7200 | 0,5 | 0,75 | 0,42 | 1,5 |
| BR26 | 33R | ● | 280 | 7800 | 0,5 | 0,76 | 0,4 | 1,5 |
| – | PGT | ● | 230 | 9000 | 0,5 | 0,65 | 0,52 | 1,5 |
| RD26TT | – | ● | 300 | 7800 | 0,5 | 0,76 | 0,4 | 1,5 |
| SB70 | B31 |  | 155 | 6400 | 0,5 | 0,8 | 0,4 | 0,5 |
| 85S | B60 |  | 240 | 8250 | 0,5 | 0,65 | 0,52 | 0,5 |
| LL4 | CC7 |  | 267 | 6400 | 0,5 | 0,7 | 0,42 | 0,5 |
| HEM5 | DC2 |  | 254 | 5800 | 0,5 | 0,78 | 0,41 | 0,5 |
| QD35 | Z35 |  | 205 | 6800 | 0,5 | 0,76 | 0,41 | 0,5 |
| – | TSL |  | 300 | 10000 | 0,5 | 0,65 | 0,52 | 0,5 |
| VF52 | F35 |  | 195 | 7200 | 0,49 | 0,75 | 0,41 | 0,5 |
| LL2 | CC8 |  | 230 | 7100 | 0,48 | 0,62 | 0,4 | 0,7 |
| LL6S | CVL |  | 270 | 6200 | 0,47 | 0,61 | 0,39 | 0,5 |
| SS2 | CC6 |  | 201 | 7000 | 0,46 | 0,7 | 0,38 | 0,5 |
| VQ37VHR | – |  | 320 | 6800 | 0,43 | 0,69 | 0,35 | 0,5 |
| – | LMA |  | 235 | 8500 | 0,4 | 0,64 | 0,32 | 0,5 |
| LSS | Swap |  | 315 | 7000 | 0,4 | 0,68 | 0,36 | 0,5 |
| M3G6 | VAN |  | 199 | 4800 | 0,4 | 0,7 | 0,3 | 0,5 |
| B38S | M24 |  | 161 | 7000 | 0,35 | 0,61 | 0,25 | 0,5 |
| L5L39 | LMM |  | 270 | 8200 | 0,35 | 0,59 | 0,27 | 0,5 |
| VV54 | VPR |  | 323 | 6200 | 0,35 | 0,59 | 0,27 | 0,5 |
| R41Y | HNG |  | 220 | 8000 | 0,2 | 0,34 | 0,12 | 0,4 |

## Varmistamatta ja lähteet

- Moottorivertailu on Tougen reittimallista (◐). Natiivi (17.11., 8 toistoa) ei vahvistanut mallin järjestystä; ND-moottori AE86:ssa (−0,9 s) kannattaa pelikokeeseen.
- Selittääkö osakerroin pelaajien kokemuksen Minin ja S02:n "piilostatistiikasta", on päätelmä (◐). S02:n kerroin 0,80 on keskitason yläpuolella, mutta mallissa se jäi kärjestä 2,8 s raskaan massansa (199 kg) vuoksi.
- Lähteet: Tougen moottorihaut ja pelin moottorikomponenttien data.

---

← [Korin dimensiot](body-dimensions.md) · [Sisältö](README.md) · [Välitykset](gearing.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
