[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../README.md)

**PDF:** [Project-Touge-Saatoopas.pdf](Project-Touge-Saatoopas.pdf)

# Säätöopas

## Tästä oppaasta

Tämä on Tougen Säädä-välilehden taustalla oleva pitkä luku. Säädä-välilehti kertoo, mitä säätöä kokeilla oireeseen. Tämä opas selittää, miksi se toimii CarX Streetissä, mitä tapahtuu kun menet liian pitkälle ja miten säädöt vaikuttavat toisiinsa. Lue se alusta loppuun, jos haluat kokonaiskuvan, tai avaa yksi luku, kun jokin säätö askarruttaa.

Kaikki tässä koskee sitä, miten tämä peli laskee auton, ei sitä, miten oikea auto toimii. Kun peli toimii kuten oikea auto, opas kertoo sen. Kun ei toimi, peli voittaa.

## Mistä tieto tulee

- **Pelin oma fysiikkakoodi ja data.** "Näin peli laskee" -osioiden kaavat tulevat pelin ajofysiikasta ja osadatasta.
- **Natiivimalli.** Pelin fysiikkamoottori ajettuna pelin ulkopuolella tietokonekuljettajalla oikealla reitillä. Se ajaa saman auton samoilla säädöillä monta kertaa, joten se vertaa säätöjä paljon tasaisemmin kuin ihminen.
- **Kokemus pelissä.** Pelissä ajetut ja kellotetut setupit touge-reiteillä, oikean kuljettajan ajamina.

Merkit: ● vahvistettu pelissä tai pelin koodissa, ◐ natiivimalli tai päätelty, ei pelissä testattu, ○ oikean auton teoria, vain taustaksi.

Kun opas sanoo "kokemuksemme mukaan", tulos tulee pelikokeista tai natiiviajoista muutamalla autolla. Pidä luvut suuruusluokkana omalle autollesi, älä lupauksena.

## Miten peli eroaa oikeasta autosta

Muutama pelin fysiikan piirre muuttaa tavallisia säätöneuvoja. Ne toistuvat luvuissa.

| Pelissä | Mitä se tarkoittaa säädölle |
| --- | --- |
| Kallistuskeskiö on maan tasolla ● | Koko kaarteen kuormansiirto kulkee jousien, vakaajien ja vaimentimien kautta. Vakaajat eivät vähennä kokonaissiirtoa, ne vain päättävät, kumpi akseli sen kantaa. |
| Jousen pituus on ajokorkeus ja joustovara ● | Jousen pituus on yksi suurimmista vivuista: se määrää, paljonko joustoa on jäljellä ennen rajoitinta. |
| Vaimentimen polvi on korkealla, 0,1 m/s ● | Slow-arvot tekevät lähes kaiken ajettavuustyön, fast-arvot vaikuttavat vain kuoppiin, reunoihin ja guttereihin. |
| Peli lisää säätämääsi camberiin −3…+5° ● | Ruudun camber ei ole renkaan todellinen camber: levossa se on noin 2–3° positiivisempi. |
| Diffin lukko on osuus voimansiirron väännöstä ● | Sama lukko lukitsee pienellä vaihteella paljon enemmän. Preload on ainoa lukko kytkin pohjassa. |
| Renkaan pito kasvaa leveyden potenssilla 0,41 ●, ja vanneosa määrää kitkalisän ● | Leveys ja oikea vanneosa ratkaisevat enemmän kuin halkaisija. |

## Näin käytät sitä Tougen kanssa

1. **Rakenna** auto Tougen Rakenna-välilehdellä tai syötä se kuvakaappauksistasi.
2. **Aloita** presetistä, kuten touge weapon, ja aja pelissä muutama kierros.
3. **Etsi vaihe**, jossa auto ei tee mitä haluat: jarrutus, sisääntulo, keskikohta, ulostulo, suora tai kuopat ja gutterit.
4. **Valitse oire** Säädä-välilehden Oire-näkymässä. Se näyttää ensin ja sitten kokeiltavan muutoksen ja linkittää tämän oppaan lukuun, joka selittää sen.
5. **Muuta yhtä asiaa kerrallaan** ja aja sama mutka samalla vaihteella. Siirrä säätö peliin Peliin-näkymällä.

## Näin luet luvun

Jokainen luku etenee samalla tavalla:

1. **Lyhyesti:** kuinka iso vipu on ja yksi asia muistettavaksi.
2. **Näin peli laskee:** kaava tai mekanismi merkkeineen.
3. **Kun nostat:** mitä odottaa, mitä tapahtuu kun menet liian pitkälle, ja kokemus taustalla.
4. **Vaikutus muihin:** mikä muu muuttuu, kun kosket tähän.
5. **Oireet:** ajovaihe, oire, mitä pelissä tapahtuu ja mitä muuttaa.
6. **Loppuvinkki:** miten lähestyä uutta autoa.
7. **Varmistamatta:** mikä on vielä auki. Lue tämä ennen kuin luotat lukuun.

## Luvut

1. [Alusta kokonaisuutena](whole-chassis.md): isoimmat vivut, säätöjärjestys, testaaminen ja oirehakemisto.
2. [Renkaat](tyres.md): leveys, vanneosa, paine, halkaisija ja raide.
3. [Jouset](springs.md): jousen pituus, jäykkyys ja etu–taka-tasapaino.
4. [Vakaajat](anti-roll-bars.md): jäykkyys, kallistus ja etu–taka-jako.
5. [Vaimentimet](dampers.md): slow ja fast bump ja rebound sekä niiden yhteistoiminta.
6. [Camber ja toe](camber-and-toe.md): renkaan asento ja pyörän suunta.
7. [Diffi](differential.md): kaasulukko, moottorijarrulukko ja preload.
8. [Korin dimensiot](body-dimensions.md): akseliväli, raide, painopiste ja massa lähtökohtana.
9. [Sanasto](glossary.md): oppaan sanat ja pelin säätöjen nimet.

## Lopuksi

Nopein setup riippuu kuljettajasta. Kun kaksi vaihtoehtoa ovat noin puolen sekunnin sisällä, pidä se, joka tuntuu hallittavammalta. Mikään tässä oppaassa ei korvaa muutoksen ajamista pelissä.

---

[Sisältö](README.md) · [Alusta kokonaisuutena](whole-chassis.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
