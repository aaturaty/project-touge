[![Project Touge choriso's Tuning Bible](../banner.png)](README.md)

[In English](../gearing.md)

# Välitykset ja vaihdelaatikko

## Lyhyesti

Välitykset päättävät, millä kierroksilla moottori on kussakin mutkassa ja suoralla. Laatikon valinta (massa ja vaihtoaika) ja kokonaisvälitys ovat keskikokoinen vipu, sekunnin luokkaa North-kierroksella ◐. Porrastuksen hiominen on pieni vipu, alle 0,5 s ◐. Renkaan halkaisija muuttaa kokonaisvälitystä, joten rengaskoon vaihto vaatii aina FD:n korjauksen ●.

## Näin peli laskee

1. Pyörän vääntö = moottorin vääntö × vaihde × FD, ja nopeus = kierrokset / (vaihde × FD) × renkaan säde ●.
2. Renkaan säde tulee koosta: halkaisija = vanne × 25,4 + 2 × leveys × profiili / 100 (mm) ●. Isompi halkaisija pidentää kaikkia vaihteita samassa suhteessa.
3. Laatikon viritystaso (gearbox_1…6) kertoo FD:tä 0,98 / 0,95 / 0,92 / 0,90 / 0,87 / 0,84. Tasoilla 3–6 jokaisella vaihteella ja FD:llä on liukuri, jonka askel on ×1,04 / 1,05 / 1,08 / 1,08, ja liukurissa on 20 tickiä per askel ●.
4. Laatikot käyvät ristiin kaikkien autojen välillä ●. Laatikoilla on oma massa ja vaihtoviive ●:

| Laatikko (pelinimi) | Vaihteita | Massa | Vaihtoviive |
| --- | --- | --- | --- |
| T50S (transmission_t50) | 6 | 35 kg | 0,25 s |
| T50 (transmission_t40) | 5 | 39 kg | 0,35 s |
| T60 (transmission_t40a) | 6 | 50 kg | 0,35 s |
| T70 (transmission_t50a) | 7 | 55 kg | 0,28 s |
| Autojen 8-vaihteiset (esim. Lexus RC F, Alfa Giulia GTAm, M2 G87) | 8 | 50 kg | 0,3–0,5 s |
| Autojen omat 6-vaihteiset | 6 | 50 kg | 0,3–0,5 s |

## Kun nostat

| Muutos | Odota | Liikaa | Kokemus |
| --- | --- | --- | --- |
| FD ylös (lyhyempi) | Kiihtyvyys paranee joka vaihteella, ja vaihtoja tulee enemmän. | Ylin vaihde loppuu kesken suoran ja auto hakkaa rajoitinta. | ◐ Supra A90 FD 3,98 → 4,14 −1,0 ± 0,4 s (8 toistoa). |
| Leveämpi tai korkeampi rengas | Halkaisija kasvaa ja kaikki vaihteet pitenevät. | Auto tuntuu tehottomalta mutkista ulos. | ◐ Integra 285/40: +0,9 s, sama FD korjattuna −1,4 s, ja profiili niin, että halkaisija pysyy: −8,4 s. |
| Matalampi profiili | Halkaisija pienenee ja vaihteet lyhenevät. | Sama kuin FD liian ylhäällä. | ◐ Korjaa FD = vanha FD × uusi halkaisija / vanha halkaisija, niin vain rengas muuttuu. |
| Ylin vaihde pidemmäksi | Huippunopeus nousee. | Vaihde jää käyttämättä, ja muut vaihteet harvenevat. | ● Ylin vaihde mitoitetaan reitin todelliseen huippuun (North noin 250 km/h), ja kaikki vaihteet ovat käytössä. |

## Vaikutus muihin ja säätöjärjestys

1. **Laatikko ensin.** Simulaatiomallissa T50S voitti kaikilla buildeilla, ja ero tuli lähinnä massasta (35 vs 50 kg) ja vaihtoviiveestä ◐. Natiivissa laatikon massa maksoi 0,04–0,07 s / kg North-kierroksella, joten 15 kg on noin 0,6–1,0 s ◐. Paras 8-vaihteinen (Lexus RC F) oli mallissa noin 1 s T50S:n takana ◐. Natiivissa (17.11., 8 toistoa, S15 ja AE86) 8-vaihteiset olivat 1,1–2,9 s ja T70 0,8–2,2 s T50S:ää hitaampia; kaikilla välitykset haettu reitin huippuun ◐. 8-vaihteisen etu ei siis näy C3:ssa North v2:lla.
2. **Ylin vaihde reitin huippuun.** Kaikki vaihteet käyttöön ja ylin vaihde loppuu juuri reitin huippunopeuden yli ●.
   Versiosta 0.20.1 alkaen Tougen tuottamat välitykset päättävät ylimmän vaihteen reittikohtaiseen rajoitinkaistaan: North Touge, Full Touge Run, Lighthouse Run ja Touge Loop 255–260 km/h, Fujiwara Run 236–240 km/h, Sunset Speedwaylla ei kaistaa ◐.
3. **Porrastus.** Pelissä hyviksi todetut sarjat ovat progressiivisia: alimmat välit saavat venyä 1,55:een, portaat 3→4 ja 4→5 enintään noin 1,30 ja viimeinen enintään 1,35 ◐. Tasainen 1,34 joka välissä teki ylävaihteista liian pitkät portaat ●.
4. **FD viimeisenä** moottorin käyrän mukaan. Leveä tehoalue sietää harvemman laatikon: Minillä 5-vaihteinen T50 oli mallissa yhtä hyvä kuin T50S ◐.

| Tekijä | Miten liittyy välityksiin |
| --- | --- |
| Moottorin käyrä | Kapea tehoalue vaatii tiheät välit, jotta vaihdon jälkeen ollaan yhä tehoalueella. |
| Renkaan koko | Halkaisija kertoo kaikki välitykset. Pidä vetävän akselin halkaisija ±2 %:n sisällä tai korjaa FD. |
| Renkaan leveys | Leveys ei siirrä pyörän keskilinjaa. Raideleveyttä muuttavat vain spacerit ja offset ●. |
| Vaihtoaika | Lyhyt vaihtoaika suosii tiheää sarjaa ja pitkä harvaa. Natiivissa vaihtoajan vaikutus oli kohinan sisällä ◐. |

## Oireet

| Ajovaihe | Oire | Säätö |
| --- | --- | --- |
| Suora | Ylin vaihde loppuu ennen jarrutusta | FD alas tai ylin vaihde pidemmäksi |
| Suora | Ylintä vaihdetta ei koskaan käytetä | FD ylös tai ylin vaihde lyhyemmäksi |
| Ulostulo | Vaihdon jälkeen moottori putoaa tehoalueen alle | Tihennä kyseistä porrasta (≤ 1,30) |
| Ulostulo | Rajoitin tulee vastaan juuri ennen jarrutusta | Pidennä tätä vaihdetta tai vaihda ylös aiemmin |
| Kaikki | Uusien renkaiden jälkeen auto tuntuu laiskalta | Halkaisija kasvoi: korjaa FD |
| Kaikki | Moottorinvaihto ei tuonut odotettua etua | Hae FD uudelleen uudelle käyrälle. Pelissä 17.11. ●: AE86 PV2 FD 4,52 → 4,35 −2,1 s; Supra FD 3,98 → 4,14 reitin ennätys; S15 ND FD 4,59 → 4,40 6:08,76 (ent. 6:11,25). Natiivi osui suuntaan kaikissa kolmessa |

## Loppuvinkki

Valitse kevyt laatikko (T50S), mitoita ylin vaihde reitin huippuun ja korjaa FD aina, kun rengaskoko muuttuu. Hio vasta sen jälkeen portaat.

## Varmistamatta ja lähteet

- 8-vaihteisten vaihtoaika natiivissa on skaalattu pelin viiveestä (0,16 s × viive / 0,25), joten tulos ei ole pelissä varmistettu ◐.
- Mallin suosima laaja porrastus (lyhyt ykkönen, pitkä kuutonen) ei näkynyt pelissä, joten sitä ei suositella ◐.
- Lähteet: Tougen välityslaskin ja haku 130 vaihdelaatikolla North Tougella C3:ssa.

---

← [Moottori](engine.md) · [Sisältö](README.md) · [Sanasto](glossary.md) →

<sub>Project Touge on epävirallinen, fanien tekemä työkalu CarX Streetiin. Se ei ole CarX Technologiesin tuote.</sub>
