[![Project Touge Säätöopas](../banner.png)](README.md)

[In English](../springs.md)

# Jouset

## Lyhyesti

Jousien suurin vipu on pituus, koska tässä pelissä se on ajokorkeus. Kokemuksemme mukaan muutama millimetri lisää etujousen pituutta on ollut mutkaisella tiellä sekunteja ●. Jäykkyys on keskikokoinen vipu: selvästi pehmeämpi tai jäykempi kuin auto haluaa maksaa 2–4 s ◐. Etu–taka-suhde ratkaisee vähemmän kuin vakaajajako.

Pelin jousissa on kaksi erikoisuutta oikeaan autoon verrattuna. Jousiluku on suoraan pyöräjäykkyys ilman välityssuhdetta, ja jäykempi jousi nostaa koria, koska pituus on jousen vapaa pituus.

Merkit: ● vahvistettu pelissä tai pelin koodissa, ◐ natiivimalli tai päätelty, ei pelissä testattu.

## Pituus

**Näin peli laskee:**

1. Spring Length on jousen vapaa pituus millimetreinä ●. Levossa kuorma painaa jousta: painuma = pyöräkuorma / jousiluku ●.
2. Jousen yläkiinnitys on pyörän kohdalla, ei pituuden. Kori ja painopiste nousevat siksi täsmälleen 1 mm jokaista pituusmillimetriä kohti ●. Pelissä pituus on ajokorkeuden säätö.
3. Pituus määrää myös joustovaran: jousitus lyö rajoittimeen, kun pyöräkuorma ylittää staattisen + k · (pituus − painuma) ●. Kuoppaisella tiellä etukuorma voi hetkellisesti nousta noin 3,6 × staattiseen, joten joustovara ilman pohjaan lyöntiä on noin 3,6 × painuma ◐.
4. Camber muuttuu pituuden mukana: camber = säätö − 3° + 8° · pituus / isku ●. Pidempi jousi tekee lepocamberista pystymmän, mutta camberin pitovaikutus on pieni ◐.
5. Tasaisella ympyrällä ajokorkeus 70–120 mm ei muuttanut pitoa ◐. Ero tulee kuopista, reunoista ja siitä, lyökö jousitus rajoittimeen.

**Kun nostat:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Etupituus | Keula saa joustovaraa: vähemmän pohjaan lyöntiä ja vähemmän kaasu-aliohjausta nopeissa mutkissa. | Korkea keula ja painopiste, enemmän kallistusta ja laiskemmat siirtymät. | ● +4 edessä oli mutkaisella tiellä yli kaksi sekuntia; seuraava +4 oli tasoissa. ◐ Molempien päiden lasku 15:llä maksoi noin 1 s. |
| Takapituus | Perä saa joustovaraa ja rauhoittuu kuopissa. | Korkea perä siirtää painoa eteen jarrutuksessa ja keventää perää. | ◐ Iso takapituuden muutos oli kierroksella kohinaa. |
| Pituus alas (molemmat) | Matalampi painopiste ja vähemmän kuormansiirtoa. | Jousitus lyö rajoittimeen ja auto tuntuu kovalta. | ◐ Lisää joustovaraa vähensi rajoitinaikaa kolme neljäsosaa. Pelin oma säätöohje varoittaa hallinnan menetyksestä kuoppaisilla teillä liian lyhyillä jousilla. |

## Jäykkyys

**Näin peli laskee:**

1. Jousivoima F = k · (pituus − nykyinen pituus) menee suoraan pyörälle ●. Pelin arvo × 1000 = pyöräjäykkyys N/m ilman välityssuhdetta ●. Eri autojen jousilukuja voi siksi verrata suoraan massaan.
2. Jäykempi jousi painuu vähemmän, joten samalla pituudella kori nousee ●. Kun jäykistät, lyhennä pituutta saman verran, jos haluat pitää korkeuden.
3. Jouset eivät muuta kokonaiskuormansiirtoa (m · a · h / t sivuttain, m · a · h / L pitkittäin), koska kallistuskeskiö on maan tasolla ●. Ne päättävät, kuinka paljon kori liikkuu ja kuinka hyvin pyörä seuraa kuoppia.
4. Kallistuksessa jousipari antaa k · t² / 2 ja vakaaja k · t² ●. Sama luku vakaajassa jäykistää kallistusta kaksi kertaa enemmän kuin jousessa.
5. Ominaistaajuus f = √(k / m) / 2π, missä m on massa pyörää kohti ◐. Taajuus on helpoin tapa siirtää toimiva jäykkyys toiseen autoon.
6. Helper on progressiivinen apujousi, ei ajoavustin ●. Liukurin rajat tulevat jousitusosasta, ja peli voi rajata enemmän kuin data kertoo ●.

**Kun nostat:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Molemmat jouset ylös | Vähemmän korin liikettä, terävämpi vaste, ja kori nousee (ks. kohta 2). | Pyörät eivät seuraa kuoppia, ja auto pomppii reunoilla ja guttereissa. Hyvin jäykät yhdistelmät olivat simulaatiossa epävakaita. | ◐ Selvästi jäykempi kuin auto haluaa maksoi noin 2 s. ● Maltillisesti jäykempi jousi antoi pelissä "hyökkäävyyttä ja pitoa mutkaan". |
| Molemmat jouset alas | Pyörät seuraavat tietä ja auto rauhoittuu kuopissa. | Kori painuu ja lyö rajoittimeen; kallistus ja nyökkäys kasvavat. | ◐ Paljon pehmeämpi jousi maksoi jopa 4 s. |

## Etu–taka-suhde

**Näin peli laskee:**

1. Jousipari on osa akselin kallistusjäykkyyttä (k · t² / 2), joten jousisuhde siirtää kuormansiirron jakoa samaan suuntaan kuin vakaajat ●. Jäykempi etujousi siirtää rajan keulaan, jäykempi takajousi perään.
2. Vaikutus on pienempi kuin vakaajilla, koska jousipari laskee puolet samasta luvusta vakaajassa ●. Kokemuksemme mukaan jousien vaihto ei korjannut herkkää perää, vakaajat korjasivat ◐.
3. Jarrutuksessa ja kiihdytyksessä pitkittäinen siirto m · a · h / L on sama jousista riippumatta ●. Jousisuhde päättää, kuinka paljon keula sukeltaa ja perä nousee, ja sitä kautta joustovaran ja camberin.
4. Taajuus kuvaa suhdetta paremmin kuin pelkkä luku: etupainoinen auto tarvitsee jäykemmän etujousen samaan taajuuteen ◐.

**Kun nostat:**

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| Etujousi (taka ennallaan) | Keula sukeltaa jarrutuksessa vähemmän ja sisäänohjaus terävöityy hieman. | Kaasu-aliohjaus nopeissa mutkissa, ja keula pomppii kuopissa. | ◐ Pieni vaikutus kierrokseen; pehmeämpi etu vähensi kaasu-aliohjausta. |
| Takajousi (etu ennallaan) | Perä kääntää autoa ja kaasu-aliohjaus vähenee. | Perä kevenee, sisäpyörä sutii ja perä pomppii kuopissa. | ● Pehmeämpi takajousi yhdessä vakaaja- ja diffimuutosten kanssa oli pelissä yli sekunnin nopeampi. ◐ Selvästi pehmeämpi taka oli hitaampi. |

Korjaa tasapaino ensin vakaajilla. Muuta jousisuhdetta vain, kun oire liittyy kuoppiin tai nyökkäykseen jarrutuksessa ja kaasulla.

## Vaikutus muihin

Järjestys: ensin pituus (joustovara ja korkeus), sitten jäykkyys, ja tasapaino vakaajilla. Jokainen jousimuutos siirtää myös ajokorkeutta, joten tarkista pituus jäykkyysmuutoksen jälkeen.

| Säätö | Miten liittyy jousiin pelin fysiikassa |
| --- | --- |
| Vakaajat | Jouset ja vakaajat muodostavat yhdessä kallistusjäykkyyden ●. Jos vaihdat jouset, siirrä vakaajia niin, että jako pysyy. |
| Vaimentimet | Sopiva vaimennustaso riippuu jousesta. Liian suuri rebound pakkaa jousituksen rajoittimelle ◐. Kun jäykistät jousta, nosta vaimennusta suunnilleen samassa suhteessa. |
| Painopiste | Pituus nostaa painopistettä 1 mm / mm ●. Korkeus lisää kuormansiirtoa, mutta tasaisella ympyrällä pito ei muuttunut ◐. |
| Camber | Camber riippuu jousen pituudesta ●. Jäykän akselin autossa camberilla ei ole vaikutusta ●. |
| Rengasprofiili | Profiili nostaa koria ●. Isompi rengas tarvitsee lyhyemmän jousen samaan korkeuteen. |
| Diffi | Pehmeä tai korkea perä kallistuu ja keventää sisäpyörää, joten kaasulukko kytkeytyy aiemmin ◐. |
| Kuopat ja gutterit | Tien kuopat ovat pieniä ja tiheitä sekä isompia ja pitkiä ●. Liian jäykkä tai lyhyt jousi ei seuraa niitä, mikä näkyy pomppimisena reunoilla. |

## Oireet

Muuta yhtä asiaa kerrallaan: pituutta 4, jäykkyyttä noin 10 %. Aja sama mutka samalla vaihteella.

| Vaihe | Oire | Mitä pelissä tapahtuu | Muutos |
| --- | --- | --- | --- |
| Jarrutus mutkaan | Keula sukeltaa ja auto tuntuu kovalta tai työntää jarrutuksen lopussa | Etujousitus lyö rajoittimeen, kun joustovara loppuu | Pidennä etua 4. Jos keula sukeltaa yhä paljon, nosta etujousta noin 10 %. |
| Sisääntulo | Auto kääntyy laiskasti ja kallistuu paljon | Kori liikkuu enemmän kuin rengas ehtii seurata | Nosta jousia noin 10 % tai lyhennä pituutta, jos joustovaraa on ylimäärin. |
| Keskikohta | Auto on hermostunut ja pomppii mutkan kuopissa | Liian jäykkä jousi; pyörä irtoaa tiestä | Laske jousta noin 10 % ja pidä korkeus pituudella. |
| Ulostulo, täysi kaasu | Keula työntää kaasulla nopeassa mutkassa | Keula nousee ja kevenee; etujousitus ei liiku | Pidennä etua ● tai pehmennä etujousta ◐. |
| Ulostulo, kaasun avaus | Perä kyykkää ja sisäpyörä sutii | Pehmeä tai lyhyt perä painuu, ja kallistus keventää sisäpyörää | Nosta takajousta noin 10 % tai takapituutta 4. |
| Kuopat, reunat ja gutterit | Auto pomppii tai heittää pientareen yli | Jousitus lyö pohjaan tai jousi on liian jäykkä seuraamaan | Pidennä ensin. Jos auto pomppii yhä, laske jousta. |

## Loppuvinkki

Aloita pituudesta: anna jousitukselle tarpeeksi joustovaraa, ettei se lyö rajoittimeen, ja pidä kori silti matalana. Muuta sitten jäykkyyttä ja korjaa korkeus pituudella. Hieman vakiota pidempi etu ja hieman lyhyempi taka on toiminut pelissä usealla autolla ●.

Jousiluku on pyöräjäykkyys, joten raskaampi auto tarvitsee jäykemmän jousen samaan tuntumaan.

**Simulaatiokokemus ◐ (natiivimalli, ei pelissä testattu):** matalampi oli hitaampi: molemmat pituudet −15 maksoi noin 1 s, ja etu +15 toi noin 0,5 s, samaan suuntaan kuin pelissä. Jäykempi takajousi toi vähän ja pehmeämpi vei lähes sekunnin. Pehmeä etujousi jäykällä etuvakaajalla oli huono yhdistelmä (+1,7 s).

## Varmistamatta

- Simulaation tasainen ympyrä ei näytä kuoppia ja guttereita, joissa jousi ja pituus tuntuvat eniten. Peli ratkaisee.
- Taajuus- ja painumaluvut on laskettu, ei mitattu.

---

← [Renkaat](tyres.md) · [Sisältö](README.md) · [Vakaajat](anti-roll-bars.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
