[![Project Touge choriso's Tuning Bible](banner.png)](README.md)

[Suomeksi](fi/engine.md)

# Engine: parts, Part Setup sliders and part factors

## In short

Class is calculated from peak power, so at the class limit the fastest engine is the one that holds close to peak power over the widest rpm range ◐. Engine tuning is a big lever. In the simulation model the same engine gained 1–10 s on a North lap when parts and sliders were searched for lap time instead of average power ◐. How much a part does varies from engine to engine through a hidden part factor that the game never shows ●.

## How the game calculates it

1. Every engine has a torque curve with five nodes: start, Low, Mid, High and end. Parts and sliders add newton-metres to the nodes, and the curve is interpolated linearly between them ●.
2. Parts and sliders add up, they do not multiply: stat = base × (1 + Σ (part multiplier − 1) × f + Σ steps × (step multiplier − 1) × f) ●. Mass works the same way ●.
3. f is the engine's **part factor** (part_stat_factors). Each engine has its own, per part slot, and the game shows it nowhere ●. The table is at the end of this chapter.
4. Power can drop below stock only with the Prototype part sliders. Sliders on other parts only go positive ●.
5. Class is calculated from peak power on standard fuel (hp per tonne, C3 = 200–250). Peak power is read from the curve points up to the rev limiter ●.
6. Racing fuel stretches the curve along the rpm axis (torque ×1.10, limiter ×1.05). It does not change the class but adds power at high rpm ●.
7. Turbo boost is full at roughly 3150–5400 rpm and fades above that ●. Factory turbo boost can only be lowered with the Prototype ECU ●.

**Prototype part sliders ● (steps: minus / plus):**

| Part | Slider | Step | Range |
| --- | --- | --- | --- |
| ECU [P] | Rev limiter | +2.2 % × f | −6 … +6 |
| ECU [P] | Boost (turbo only) | +6 % × f | −14 … +6 |
| Block [P] | Low torque | +3 % × f | −12 … +6 |
| Head [P] | Mid torque | +4.5 % × f | −14 … +4 |
| Camshaft [P] | High torque | +5 % × f | −16 … +3 |
| Intake [P] | Peak RPM (where the curve falls off) | +2.4 % × f | −6 … +6 |

## When you raise it

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Low up, High down | Flatter curve: same peak power, more power out of corners. | The peak moves down and the top end runs out before the shift. | ◐ All the best C3 builds had sliders shaped like this, e.g. Mini in the S15: Low +5.6, Mid −8.4, High −16. |
| Rev limiter | Each gear lasts longer and you shift less. | If the curve has already fallen off, the extra revs carry no power. | ◐ The search raised the limiter on most engines (Mini +3.6, ND +3.4, Lotus and 4A-GE +6) but lowered it on the Datsun and S02. |
| Boost down | The mid-range hump drops and the car fits the class at a lower weight. | The bottom end goes empty. | ◐ RDA and Mini used 0.35–0.63 bar. |
| Peak RPM | The fall-off moves up and the top end pulls longer. | Peak power rises and the class is exceeded. | ◐ Often lowered (−6) in the best builds to keep peak power on the limit. |

## How it interacts and search order

| Factor | How it relates to the engine |
| --- | --- |
| Part factor | A bigger factor moves the curve more per step, so the curve can be shaped flatter. A small factor limits both raising and lowering. |
| Mass and class | An engine that is too strong forces you to add mass (tank, lightening slider), and that costs more than the stronger curve gains. |
| Prototype intake | The intake factor is larger than the others and it adds power. On a strong engine leaving it stock can be faster than [P] with the slider at minus ◐. |
| Gearing | A flat, wide curve tolerates wider gear steps. A narrow curve needs close ratios (see Gearing and gearbox). |

**Min-max order (◐, searched on North v2):**

1. Prototype ECU, camshaft, head and block, because only they can take power down. Intake [P] only if the engine is not already too strong.
2. Low up, Mid and High down, and Peak RPM set so that peak power lands right on the class limit.
3. Rev limiter as high as the curve carries; on turbo engines lower the boost until the mid-range hump flattens.
4. Lightening fully on and stock tank. If the power does not fit, lower the sliders first and add mass only as a last resort.

## Engines at the class limit (◐, preliminary)

Search on 17 Nov with the Touge route model on North v2 in C3 (S15 and AE86). For each engine, parts, sliders, lightening and tank were searched from 12 starting points and the result was compared with Touge's own fit. These are simulation model results, not yet run in the native simulation or in the game.

| Engine | Stock in | S15 gap to best | AE86 gap to best | Gain over Touge's own fit | Native S15 / AE86 vs current |
| --- | --- | --- | --- | --- | --- |
| N14B | MCS | 0.0 | 0.0 | −6…−8 s | +1.7 ± 0.3 / −0.2 ± 0.3 |
| PV2 | MX-5 ND | +0.6 | +0.6 | −3…−5 s | +0.4 ± 0.3 / −0.9 ± 0.1 |
| DL20 | DTS | +1.6 | +1.6 | −6…−8 s | +3.3 ± 0.2 / +1.0 ± 0.2 |
| RDA | FST | +0.7 | +1.2 | −0.1…−0.4 s | +1.4 ± 0.2 / +0.1 ± 0.2 |
| GE4 | E86 | +2.0 | +1.6 | −1…−3 s | – / +1.1 ± 0.2 |
| 2ZG | LTS | +2.2 | +2.6 | −5…−7 s | – |
| B13 | FX7 | +2.3 | +2.5 | −9…−10 s | – |
| S02 | 20R | +2.9 | +2.8 | −4…−6 s | – |
| BM13 | DX8 | +2.4 | +4.1 | −0.2…−0.4 s | – |

**Native 17 Nov (8 repetitions, ◐):** the model and the native simulation disagree. In the S15 the current ND tune was fastest and the Mini was 1.7 s slower. In the AE86 the ND engine with the model's tune was 0.9 ± 0.1 s faster than the current 4A-GE tune, and the Mini was within the noise. So the model's ranking cannot be used yet; the most robust finding is the ND engine (PV2) in a light RWD car. A rerun with the AE86's current setup (ratios 2.91/2.04/1.51/1.15/0.97/0.86, decel lock 0.28) gave ±0 at FD 4.50, −1.0 ± 0.1 s at FD 4.35 and −0.3…−0.4 s at other FDs, so the gain depends on gearing and is not yet certain. **In-game test 17 Nov (●, AE86, North v2):** GE4 runs 43–44 371.36 / 371.20 s. PV2 with the player's own tune (limiter 8687 and Peak RPM 9742 at max, High 218, Medium 281, Low 332): FD 4.52 runs 45–46 372.97 / 370.97 s, **FD 4.35 runs 47–48 369.03 / 369.22 s (−2.1 s vs the GE4, repeated)**. The native simulation predicted −1.0 ± 0.1 s for FD 4.35, so the direction was right. The model's Part Setup values were not run in the game. The player shifts up at about 8800–9000 rpm and spends 15–25 % of the lap above 8500 rpm, so lowering the limiter is probably harmful even though the models do not see it ◐. For now the most reliable line: limiter and Peak RPM up, Low up, Mid and High down until the class is filled. According to the model, engines with a high part factor (Mini 0.84 + turbo 1.6, ND and Datsun 0.89) gain the most from the sliders. Touge's current fit leaves 3–10 s on them.

## Why the same class gives different lap times (Supra test 17 Nov, ◐)

The class measures peak power per weight (hp/t), but on North the lap is decided accelerating out of corners. The test put 30 popular engines (two batches) in a Supra A90 (heavy enough for all of them), each tuned in the model to the class limit with its own gearing, and ran them in the native simulation (8 repetitions, North v2) and in a straight-line test on a flat road.

| Engine | Stock in | North diff (s) | 60–150 km/h (s) | 100–200 km/h (s) | Top speed (km/h) | Mass (kg) | Turbo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2TS | V7G | −3.8 | 5.04 | 8.90 | 257 | 903 | factory |
| G1E6 | YRS | −3.4 | 5.09 | 8.99 | 255 | 889 | factory |
| GU4 | R86 | −3.0 | 5.15 | 8.95 | 259 | 952 | – |
| DL20 | DTS | −3.0 | 5.07 | 8.93 | 259 | 925 | kit |
| N14B | MCS | −2.8 | 5.15 | 9.09 | 255 | 894 | factory |
| S02 | 20R | −2.7 | 5.22 | 8.85 | 260 | 947 | – |
| B1A6 | V45 | −2.6 | 5.12 | 9.20 | 257 | 914 | kit |
| RS20T | S13 | −2.6 | 5.23 | 9.03 | 259 | 945 | factory |
| E25 | SFR | −2.6 | 5.06 | 8.99 | 256 | 891 | factory |
| RS20 | Swap | −2.5 | 5.23 | 8.98 | 260 | 959 | kit |
| RS20T | S15 | −2.4 | 5.40 | 9.37 | 256 | 953 | factory |
| 4A-GE | Swap | −2.2 | 5.30 | 9.44 | 254 | 908 | kit |
| 46G3 | EV6 | −2.0 | 5.32 | 9.20 | 257 | 944 | factory |
| DA15 | HC6 | −1.9 | 5.36 | 9.28 | 256 | 903 | kit |
| GE4 | E86 | −1.7 | 5.28 | 9.10 | 257 | 908 | – |
| S1B4 | M30 | −1.3 | 5.28 | 9.30 | 256 | 905 | – |
| 2ZG | LTS | −1.2 | 5.36 | 9.10 | 257 | 904 | – |
| RDA | FST | −1.2 | 5.18 | 8.80 | 262 | 1009 | factory |
| G64 | ECL | −0.9 | 5.38 | 9.26 | 258 | 941 | – |
| PV2 | MX-5 ND | −0.6 | 5.32 | 9.33 | 255 | 898 | – |
| GE3 | 2MR | −0.4 | 5.37 | 9.11 | 256 | 902 | – |
| BR13 | DX7 | −0.3 | 5.44 | 9.48 | 260 | 966 | factory |
| KA20 | HCR | +0.3 | 5.07 | 8.57 | 266 | 1041 | – |
| BM13 | DX8 | +0.4 | 5.47 | 9.70 | 256 | 961 | – |
| F2C0 | HS2 | +0.5 | 5.37 | 9.21 | 260 | 955 | – |
| 4G63 | Swap | +0.8 | 5.25 | 8.85 | 264 | 1067 | factory |
| ME10 | B19 | +0.8 | 5.58 | 9.74 | 253 | 923 | – |
| B13 | FX7 | +0.9 | 5.55 | 10.14 | 253 | 911 | factory |
| B1B6 | HC9 | +1.5 | 5.40 | 9.44 | 260 | 943 | – |
| B411T | EVX | +3.6 | 5.21 | 8.72 | 269 | 1113 | factory |

The North difference is against an S02 tune driven in the game (975 kg); the model tunes are ~28 kg lighter (empty tank, full weight reduction), so the order between engines is more reliable than the gap to zero. Mass is the whole car with the model tune; 60–150 is the better of the model gearing and the long-sixth gear set.

**What follows:**

1. **60–150 km/h predicts the North time when the engine does not make the car heavy** (under 1000 kg: correlation 0.85; 0.1 s quicker 60–150 ≈ 0.9 s quicker lap). Heavy engines (RDA, Civic Type R, 4G63, Evo X, 1009–1113 kg) lead on the straight but are slow on North: across all 30 the correlation is only 0.53, and 60–150 plus mass together give 0.83 (10 kg ≈ 0.2 s per lap). 100–200 km/h predicts poorly (0.25) and top speed not at all: air drag caps every engine at 253–269 km/h.
2. **A turbo gives mid-range torque that the class does not fully count.** Eight of the top ten are turbocharged (factory turbo or a turbo kit chosen by the search). A turbo does not save a heavy engine: the RDA, 4G63 and Evo X pay for their mass in corners.
3. **For naturally aspirated engines the flatness of the curve over the shift band decides** (70–100 % of the limiter): S02 and GE4 (mean power 96 % of peak) are best, EK9 (81 %), 190E (89 %) and Eclipse (90 %) slowest.
4. **Engine braking and inertia do not explain the differences**: in the game data they are the same for every engine ●.
5. **The car decides.** In the S15 the same native test gave the opposite result (DL20 +3.3, Mini +1.7 vs the ND). A lighter car cannot fit an equally strong turbo engine in the class. Test the top candidates in your own car, and search FD again after the swap.

Touge uses this in engine selection from 0.12.0 ◐. The model now shifts up at about 0.90 × the limiter, like the player and the native sim, and parts and sliders are fitted to the class for the shortest acceleration time and lowest mass instead of the highest average power. In the native sim the best predictor is the native 60–150 itself, but in the model 50–120 km/h + mass follows the native North time best (Supra 90 builds r 0.85, S15 r 0.92; the model's 60–150 r 0.73), because the model and the native sim differ in 1st-gear acceleration. Native check on North v2: in the Supra the new builds were 0.4 s faster on average than the earlier search, and 6 of the native sim's 8 best engines are in the selection's top 12 (2 before). In the S15 the selection's top four were 0.35 s faster on average than before, but the best single build (Forester, old fit) beat the new one by 0.5 s. No candidate was faster than the current S15 setup (ND engine).

Two refinements on 18.11. ◐. **The rev limiter is not lowered in selection:** the 50–120 fit lowered the limiter slider on turbo engines (Forester 7432 → 6630 rpm) to buy a little torque, but in the native sim the low limiter lost in the fast sections: keeping the limiter made the Forester 1.8 s faster in the AE86 and 0.4 s faster in the S15, and in the Supra the high-limiter build was 4.0 s faster. **Finishing:** the top three candidates are finally tuned on route time with the user's weight-reduction and fuel-tank settings, and the build is locked. In the native sim the finished Forester was 3.9 s faster in the S15 and 4.0 s faster in the Supra than the unfinished one. In the Supra, Touge's recommendation (ND or Forester) was 2.6–2.8 s faster natively than the current setup (GT-R engine). In the AE86 and S15 the current ND engine stayed fastest: the model's suggestions were 0.7–2.8 s behind it natively. So the model finds good engines, but differences under 1 s in its predictions are not reliable. Try the recommendation in the game before replacing an engine that works.

Data: analyysi/moottorihaku_1711/supra/ and supra2/ (natiivi/v.json, testi2/tulos.json, testi2/ulostulo.json). Not yet confirmed in the game.

## Part factors by engine ●

All 137 engines from the game data (part_stat_factors), largest first. The part factor is the same for the ECU, camshaft, head, block and fuel system. Median 0.74, smallest 0.20, largest 1.09. Turbo part = the multiplier of the Turbo Kit or factory turbo part. Engine is the engine code shown in the game (the start of its name, e.g. RDA in "RDA 2.0L L4 T (FST)"), Stock in is the game code of the car it comes in, and Swap marks a swap engine. – under Engine: the game data has no engine name for that car yet.

| Engine | Stock in | Factory turbo | Mass kg | Limiter | Part factor (ECU, cam, head, block, fuel) | Intake | Exhaust manifold and exhaust | Turbo part |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B13 | FX7 | ● | 157 | 8500 | 1.09 | 1.38 | 1 | 1.5 |
| DT 18 | S18 | ● | 268 | 7200 | 1.09 | 1.38 | 1 | 1.5 |
| DT 18 (Spirit) | – | ● | 268 | 7200 | 1.09 | 1.38 | 1 | 1.5 |
| DA15 | HC6 |  | 140 | 7800 | 1 | 1.3 | 0.9 | 1 |
| L08 | L08 |  | 127 | 6000 | 1 | 1.3 | 0.9 | 0.5 |
| VGD3 | 30Z | ● | 220 | 6800 | 0.98 | 1.28 | 0.88 | 1.5 |
| VGD3 | 30ZC | ● | 220 | 6800 | 0.98 | 1.28 | 0.88 | 1.5 |
| RS20T | S14 | ● | 180 | 7500 | 0.95 | 1.25 | 0.85 | 1.5 |
| B70 | MF1 |  | 275 | 7600 | 0.95 | 1.16 | 0.78 | 0.5 |
| RS20T | S13 | ● | 180 | 7500 | 0.91 | 1.25 | 0.81 | 1.5 |
| 46G3 | EV6 | ● | 170 | 7600 | 0.9 | 1.24 | 0.8 | 1.5 |
| 97M1 | P91 | ● | 230 | 7300 | 0.9 | 0.86 | 0.8 | 1.5 |
| BL58 | S90C | ● | 140 | 7000 | 0.9 | 1.2 | 0.8 | 1.5 |
| – | Ferrari F40 | ● | 210 | 7500 | 0.9 | 1.2 | 0.8 | 0.5 |
| B1A6 | V45 |  | 140 | 6500 | 0.9 | 1.2 | 0.8 | 0.5 |
| C2L | BGX |  | 200 | 6200 | 0.89 | 1.19 | 0.79 | 1.5 |
| PV2 | MX-5 ND |  | 130 | 7200 | 0.89 | 1.19 | 0.79 | 1.5 |
| DT20 | 31R | ● | 230 | 7600 | 0.89 | 1.19 | 0.79 | 1.5 |
| E25 | SFR | ● | 120 | 6500 | 0.89 | 1.18 | 0.79 | 1.5 |
| 4A-GE | Swap |  | 145 | 7400 | 0.89 | 0.89 | 0.89 | 0.89 |
| 4G63 | Swap | ● | 175 | 7500 | 0.89 | 0.89 | 0.89 | 0.89 |
| D15B | Swap |  | 150 | 7700 | 0.89 | 0.89 | 0.89 | 0.89 |
| GE4 | E86 |  | 154 | 7400 | 0.89 | 1.19 | 0.79 | 0.5 |
| DL20 | DTS |  | 160 | 6200 | 0.89 | 1.19 | 0.79 | 0.5 |
| PF1 | NX5 |  | 155 | 7200 | 0.89 | 1.19 | 0.79 | 0.5 |
| PF1 | NX5C |  | 155 | 7200 | 0.89 | 1.19 | 0.79 | 0.5 |
| ME10 | B19 |  | 170 | 6600 | 0.89 | 1.19 | 0.79 | 0.5 |
| GE3 | 2MR |  | 143 | 7000 | 0.89 | 1.19 | 0.79 | 0.5 |
| DT20 | 32R | ● | 230 | 7400 | 0.86 | 1.2 | 0.8 | 1.5 |
| E25 | WRS | ● | 125 | 7400 | 0.86 | 1.14 | 0.77 | 1.5 |
| LL1 | CC3 |  | 280 | 6200 | 0.85 | 1.04 | 0.81 | 1.5 |
| RV30 | IF6 | ● | 195 | 6800 | 0.85 | 1.19 | 0.75 | 1.5 |
| G1E6 | YRS | ● | 120 | 7200 | 0.85 | 1.04 | 0.81 | 1.5 |
| M17 | AMV | ● | 209 | 8000 | 0.85 | 1.2 | 0.75 | 1.5 |
| G64 | ECL |  | 185 | 6500 | 0.85 | 1.14 | 0.75 | 0.5 |
| N14B | MCS | ● | 130 | 6500 | 0.84 | 1.14 | 0.74 | 1.6 |
| RS20T | S15 | ● | 180 | 7500 | 0.83 | 1.11 | 0.74 | 1.5 |
| RS20T (Spirit) | – | ● | 180 | 7500 | 0.83 | 1.11 | 0.74 | 1.5 |
| 30S | FLD |  | 249 | 7000 | 0.83 | 1.12 | 0.73 | 0.5 |
| JAZ22 | S80 | ● | 230 | 7000 | 0.82 | 1.1 | 0.73 | 1.5 |
| TF25 | TTR | ● | 160 | 6800 | 0.81 | 1.07 | 0.72 | 1.5 |
| DT25 | 34R | ● | 250 | 7000 | 0.81 | 1.08 | 0.72 | 1.5 |
| GU4 | G86 |  | 200 | 7400 | 0.81 | 1.08 | 0.72 | 0.5 |
| 6T9 | ARG | ● | 240 | 7200 | 0.8 | 0.91 | 0.57 | 1.5 |
| – | B8I | ● | 210 | 6500 | 0.8 | 1.05 | 0.72 | 1.5 |
| 2TS | V7G | ● | 140 | 6000 | 0.8 | 1.1 | 0.7 | 1.5 |
| – | S65 | ● | 186 | 7500 | 0.8 | 1.06 | 0.7 | 1.5 |
| S02 | 20R |  | 199 | 7300 | 0.8 | 1.06 | 0.7 | 1.5 |
| MT64 | P64 | ● | 150 | 7100 | 0.8 | 1.07 | 0.71 | 1.5 |
| L1R | LFL |  | 160 | 9000 | 0.8 | 1.15 | 0.7 | 0.5 |
| RS20 | Swap |  | 190 | 7200 | 0.79 | 1.09 | 0.69 | 0.5 |
| RDA | FST | ● | 109 | 6500 | 0.78 | 1.06 | 0.68 | 1.5 |
| E20J7 | WST | ● | 204 | 8000 | 0.78 | 1.06 | 0.68 | 1.5 |
| PV8 | PF7 |  | 270 | 5000 | 0.78 | 1.08 | 0.68 | 0.5 |
| BR13 | DX7 | ● | 120 | 8300 | 0.77 | 1.03 | 0.68 | 1.5 |
| BR13 (Spirit) | – | ● | 120 | 8300 | 0.77 | 1.03 | 0.68 | 1.5 |
| BL58 | S90 | ● | 140 | 7000 | 0.765 | 1.02 | 0.68 | 1.5 |
| CV6 | 6RS | ● | 190 | 6700 | 0.75 | 1 | 0.66 | 1.5 |
| E82A | 7RS | ● | 190 | 6700 | 0.75 | 1 | 0.66 | 1.5 |
| S58 | BM2R | ● | 160 | 6800 | 0.75 | 1.15 | 0.66 | 1.5 |
| S58 | M3G | ● | 160 | 6800 | 0.75 | 1.15 | 0.66 | 1.5 |
| EBT | FGT | ● | 205 | 7000 | 0.75 | 0.99 | 0.67 | 1.5 |
| 2ZG | LTS |  | 140 | 8200 | 0.75 | 1.15 | 0.66 | 1.5 |
| DE27 | 63C | ● | 367 | 6800 | 0.75 | 1 | 0.67 | 1.5 |
| GT63 | EV9 | ● | 195 | 7500 | 0.75 | 1.02 | 0.66 | 1.5 |
| FA6 | SZK |  | 100 | 7800 | 0.75 | 1.15 | 0.66 | 1.5 |
| BM13 | DX8 |  | 120 | 8300 | 0.75 | 1.05 | 0.65 | 0.5 |
| B30 | M92C | ● | 135 | 6800 | 0.74 | 1 | 0.66 | 1.5 |
| B30 | M92 | ● | 135 | 6800 | 0.74 | 1 | 0.66 | 1.5 |
| B411T | EVX | ● | 134 | 7800 | 0.74 | 1.02 | 0.64 | 1.5 |
| RV38 | 35R | ● | 276 | 7500 | 0.73 | 0.97 | 0.65 | 1.5 |
| U2R | LRC |  | 222 | 7600 | 0.73 | 0.97 | 0.65 | 0.5 |
| B28 | M36 |  | 180 | 6600 | 0.72 | 1 | 0.63 | 0.5 |
| CPTAV10 | AR8 | ● | 250 | 7800 | 0.7 | 1.05 | 0.6 | 1.5 |
| B55N | BM2 | ● | 194 | 7500 | 0.7 | 0.95 | 0.62 | 1.5 |
| FSP | LMH | ● | 250 | 8000 | 0.7 | 1.05 | 0.6 | 1.5 |
| LL1 | CMR |  | 193 | 6400 | 0.7 | 0.96 | 0.6 | 0.5 |
| F2C0 | HS2 |  | 147 | 8300 | 0.7 | 1 | 0.6 | 0.5 |
| FUZ 1 | CRN |  | 195 | 7200 | 0.7 | 1.05 | 0.6 | 0.5 |
| B58 | M4R | ● | 140 | 7000 | 0.69 | 0.94 | 0.61 | 1.5 |
| M7GT | S70 | ● | 270 | 6800 | 0.68 | 1.08 | 0.59 | 1.5 |
| B1B6 | HC9 |  | 184 | 8500 | 0.66 | 0.92 | 0.57 | 0.5 |
| KA20 | HCR |  | 145 | 8100 | 0.66 | 0.92 | 0.57 | 0.5 |
| 2JZ-GTE | – | ● | 310 | 7000 | 0.65 | 0.87 | 0.55 | 1.5 |
| – | TAL |  | 240 | 7100 | 0.65 | 0.95 | 0.55 | 1.5 |
| FC3 | HRD | ● | 195 | 7200 | 0.65 | 0.94 | 0.61 | 1.5 |
| – | Z40 | ● | 240 | 6800 | 0.65 | 1 | 0.55 | 1.5 |
| JAZ11 | CRT | ● | 210 | 7000 | 0.65 | 0.95 | 0.55 | 1.5 |
| JAZ11 | TM2 | ● | 210 | 7000 | 0.65 | 0.95 | 0.55 | 1.5 |
| JAZ11 | TSR | ● | 240 | 7100 | 0.65 | 0.95 | 0.55 | 1.5 |
| S1B4 | M30 |  | 136 | 6750 | 0.65 | 0.9 | 0.57 | 0.65 |
| BS38 | BZ4 |  | 220 | 8000 | 0.65 | 0.94 | 0.61 | 0.5 |
| BS38 | M34 |  | 151 | 6900 | 0.65 | 0.91 | 0.55 | 0.5 |
| GU4 | R86 |  | 171 | 7200 | 0.65 | 0.9 | 0.56 | 0.5 |
| GCTM1 | C70 |  | 242 | 7500 | 0.64 | 0.94 | 0.54 | 0.5 |
| MDA | MGTC | ● | 209 | 7000 | 0.6 | 0.85 | 0.52 | 1.5 |
| 15M7 | GLW | ● | 220 | 6500 | 0.6 | 0.65 | 0.5 | 1.5 |
| MDA | MGT | ● | 209 | 7000 | 0.6 | 0.84 | 0.52 | 1.5 |
| V30G | Z31 | ● | 178 | 6000 | 0.6 | 0.85 | 0.51 | 1.5 |
| KA20 | HI5 |  | 180 | 8000 | 0.6 | 0.9 | 0.5 | 0.5 |
| BC32 | HSX |  | 200 | 8000 | 0.59 | 0.84 | 0.5 | 0.5 |
| BV8 | CHR |  | 281 | 6400 | 0.59 | 0.86 | 0.5 | 0.5 |
| LMV12 | LMD |  | 232 | 7300 | 0.58 | 0.96 | 0.48 | 0.5 |
| SB53 | M46 |  | 149 | 7000 | 0.57 | 0.855 | 0.475 | 0.5 |
| S58 | M4G | ● | 160 | 6800 | 0.55 | 0.8 | 0.46 | 1.5 |
| – | MLN | ● | 170 | 8500 | 0.55 | 0.79 | 0.47 | 1.5 |
| – | M39 |  | 208 | 7000 | 0.55 | 0.8 | 0.45 | 0.5 |
| A12J6 | JGR |  | 240 | 7500 | 0.55 | 0.81 | 0.47 | 0.5 |
| SCHM | HSS |  | 240 | 6500 | 0.55 | 0.79 | 0.47 | 0.5 |
| – | Ford Mustang S197 |  | 245 | 7000 | 0.55 | 0.76 | 0.38 | 0.5 |
| QH37 | Z37 |  | 174 | 6800 | 0.55 | 0.81 | 0.46 | 0.5 |
| VV53 | VP1 |  | 230 | 6300 | 0.55 | 0.79 | 0.47 | 0.5 |
| ES8 | STR |  | 245 | 7250 | 0.53 | 0.78 | 0.45 | 0.5 |
| FV8 | F69 |  | 290 | 6200 | 0.52 | 0.77 | 0.43 | 0.5 |
| S6B34T | M90 | ● | 229 | 8250 | 0.5 | 0.75 | 0.4 | 1.5 |
| S6B34 | BX5 | ● | 229 | 7200 | 0.5 | 0.75 | 0.42 | 1.5 |
| BR26 | 33R | ● | 280 | 7800 | 0.5 | 0.76 | 0.4 | 1.5 |
| – | PGT | ● | 230 | 9000 | 0.5 | 0.65 | 0.52 | 1.5 |
| RD26TT | – | ● | 300 | 7800 | 0.5 | 0.76 | 0.4 | 1.5 |
| SB70 | B31 |  | 155 | 6400 | 0.5 | 0.8 | 0.4 | 0.5 |
| 85S | B60 |  | 240 | 8250 | 0.5 | 0.65 | 0.52 | 0.5 |
| LL4 | CC7 |  | 267 | 6400 | 0.5 | 0.7 | 0.42 | 0.5 |
| HEM5 | DC2 |  | 254 | 5800 | 0.5 | 0.78 | 0.41 | 0.5 |
| QD35 | Z35 |  | 205 | 6800 | 0.5 | 0.76 | 0.41 | 0.5 |
| – | TSL |  | 300 | 10000 | 0.5 | 0.65 | 0.52 | 0.5 |
| VF52 | F35 |  | 195 | 7200 | 0.49 | 0.75 | 0.41 | 0.5 |
| LL2 | CC8 |  | 230 | 7100 | 0.48 | 0.62 | 0.4 | 0.7 |
| LL6S | CVL |  | 270 | 6200 | 0.47 | 0.61 | 0.39 | 0.5 |
| SS2 | CC6 |  | 201 | 7000 | 0.46 | 0.7 | 0.38 | 0.5 |
| VQ37VHR | – |  | 320 | 6800 | 0.43 | 0.69 | 0.35 | 0.5 |
| – | LMA |  | 235 | 8500 | 0.4 | 0.64 | 0.32 | 0.5 |
| LSS | Swap |  | 315 | 7000 | 0.4 | 0.68 | 0.36 | 0.5 |
| M3G6 | VAN |  | 199 | 4800 | 0.4 | 0.7 | 0.3 | 0.5 |
| B38S | M24 |  | 161 | 7000 | 0.35 | 0.61 | 0.25 | 0.5 |
| L5L39 | LMM |  | 270 | 8200 | 0.35 | 0.59 | 0.27 | 0.5 |
| VV54 | VPR |  | 323 | 6200 | 0.35 | 0.59 | 0.27 | 0.5 |
| R41Y | HNG |  | 220 | 8000 | 0.2 | 0.34 | 0.12 | 0.4 |

## Not yet confirmed and sources

- The engine comparison comes from the Touge route model (◐). The native simulation (17 Nov, 8 repetitions) did not confirm the model's ranking; the ND engine in the AE86 (−0.9 s) is worth an in-game test.
- Whether the part factor explains players' experience of "hidden stats" on the Mini and S02 is an inference (◐). The S02's factor of 0.80 is above average, but in the model it finished 2.8 s off the best because of its heavy mass (199 kg).
- Sources: analyysi/moottorihaku_1711, analyysi/moottorikomponentit, analyysi/c3_build_periaatteet.md, tyokalu/data/moottorit.json.

---

← [Body dimensions](body-dimensions.md) · [Contents](README.md) · [Gearing and gearbox](gearing.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
