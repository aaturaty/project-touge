[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../glossary.md)

# Sanasto

## Säädöt: oppaan sanat ja pelin nimet

Opas käyttää lyhyitä arkisanoja. Taulukko näyttää kunkin säädön nimen pelin omissa valikoissa (englanninkielinen peli), samoin kuin Touge näyttää ne Peliin-näkymässä.

| Oppaassa | Nimi pelissä | Mikä se on |
| --- | --- | --- |
| Vakaaja | Anti-roll bar: Stiffness | Kiertojousi akselin vasemman ja oikean pyörän välissä. Pelin arvo × 2000 = N/m. |
| Jousen pituus | Spring Length | Ajokorkeus ja joustovara millimetreinä. |
| Jousi, jousen jäykkyys | Spring Stiffness | Pyöräjäykkyys. Pelin arvo × 1000 = N/m. |
| Slow bump, slow rebound | Slow Bump, Slow Rebound | Vaimennus alle 0,1 m/s:n polven: korin liike jarrutuksessa, sisääntulossa ja kaasulla. |
| Fast bump, fast rebound | Fast Bump, Fast Rebound | Vaimennus polven yläpuolella: kuopat, reunat ja gutterit. |
| Camber | Camber | Renkaan kallistus; peli lisää −3…+5° jousen avautuman mukaan. |
| Toe | Wheel Toe | Pyörän suunta asteina; + = toe-in. |
| Caster | Caster Angle | Ohjausakselin kallistus; muuttaa camberia ohjattaessa. |
| Ackermann | Ackermann Angle | 0 = täysi Ackermann, 100 = rinnakkaiset pyörät. |
| Kaasulukko | Lock on acceleration | Osuus voimansiirron väännöstä, joka lukitsee diffin kaasulla. |
| Moottorijarrulukko | Lock on deceleration | Osuus moottorijarrun väännöstä, joka lukitsee diffin kaasu pois. |
| Preload | Preload | Diffin vakiolukko newtonmetreinä, myös kytkin pohjassa. |
| Jarrujako | Front Brake Balance | Etuakselin osuus jarruväännöstä. |
| Offset, spacer | Front / Rear Wheel Offset | Pyörän paikka ulospäin; raide = perusraide + offset. |
| Rengaspaine | Pressure | Pito on suurimmillaan 2,0 barissa; korkeampi paine pienentää vierintävastusta. |
| Rengasprofiili | Tire profile | Kyljen korkeus prosenttiyksikköinä (±10). |
| Loppuvälitys, FD | Final drive | Viimeinen välitys; kokonaisvälitys = vaihde × loppuvälitys × renkaan säde. |
| Painopiste | Center of Mass Height (Part Setup) | Prosentti korilaatikon korkeudesta, ei tuumia. |
| Etupaino | Weight Distribution in Front | Etuakselin osuus auton painosta. |

## Ajovaiheet

| Vaihe | Mitä tapahtuu |
| --- | --- |
| Jarrutus mutkaan | Suora jarrutus ja jarrutus kohti apexia. Paino siirtyy eteen. |
| Sisääntulo | Jarru pois ja käännös. Paino siirtyy ulkopyörille. |
| Keskikohta | Tasainen mutka; kori on lakannut liikkumasta. Jouset ja vakaajat päättävät tasapainon. |
| Ulostulo | Kaasun avaus ja suoristus. Paino siirtyy taakse, diffi työskentelee. |
| Suora | Kiihdytys ja huippunopeus. Välitykset ja ilmanvastus ratkaisevat. |
| Kuopat, reunat ja gutterit | Nopeat jousitusliikkeet, pientareet ja gutterit. Joustovara ja fast-vaimennus ratkaisevat. |

## Termit

| Termi | Merkitys |
| --- | --- |
| Aliohjaus | Keula antaa periksi ensin; auto menee leveämmälle kuin ohjaat. "Keula työntää." |
| Yliohjaus | Perä antaa periksi ensin; auto kiertyy enemmän kuin ohjaat. "Perä lähtee." |
| Kuormansiirto | Painon siirtyminen pyörien välillä jarrutuksessa, kiihdytyksessä ja mutkassa: m · a · h / raide (tai akseliväli). |
| Kallistusjäykkyys | Kuinka voimakkaasti akseli vastustaa korin kallistusta: vakaajat + jouset, molemmat × raide². |
| Vakaajajako, LLTD | Etuakselin osuus kallistusjäykkyydestä. Akseli, jonka osuus on suurempi, kantaa enemmän kaarteen kuormansiirrosta ja antaa periksi ensin. |
| Joustovara | Kuinka paljon jousitus voi vielä painua ennen rajoitinta: jousen pituus − painuma. |
| Rajoitin | Joustovaran jäykkä pää. Siihen lyöminen heittää autoa ja vie pitoa. |
| Painuma | Kuinka paljon auton paino painaa jousta levossa. |
| Ominaistaajuus | √(jousi / massa) / 2π. Kun se pidetään samana, jousisetup siirtyy raskaampaan tai kevyempään autoon. |
| Vaimennussuhde, ζ | Vaimennus suhteessa jouseen ja massaan; Touge siirtää sillä vaimentimet autosta toiseen. |
| Polvi | Pyörän nopeus (0,1 m/s), jossa vaimennus vaihtuu slow-arvosta fast-arvoon. |
| Kokonaisvälitys | Vaihde × loppuvälitys × renkaan säde; ainoa välitysluku, jota fysiikka käyttää. |
| Vanneosa | Rengaskokoon valittu vanneosa; se määrää renkaan kitkalisän (+0,03…+0,08). |
| Natiivimalli | Pelin fysiikkamoottori ajettuna pelin ulkopuolella tietokonekuljettajalla säätöjen tasaiseen vertailuun. |
| Kohinaa | Ero, joka on pienempi kuin tavallinen ajojen välinen hajonta, noin 0,8 s kuuden minuutin ajossa. |

## Merkit

| Merkki | Merkitys |
| --- | --- |
| ● | Vahvistettu pelissä tai pelin koodissa. |
| ◐ | Natiivimalli tai päätelty, ei pelissä testattu. |
| ○ | Oikean auton teoria, vain taustaksi. |

---

← [Korin dimensiot](body-dimensions.md) · [Sisältö](README.md)

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
