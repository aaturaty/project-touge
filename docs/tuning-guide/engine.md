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

| Engine | S15 gap to best | AE86 gap to best | Gain over Touge's own fit | Native S15 / AE86 vs current |
| --- | --- | --- | --- | --- |
| mini (N14B) | 0.0 | 0.0 | −6…−8 s | +1.7 ± 0.3 / −0.2 ± 0.3 |
| mazdamx5 (PV2) | +0.6 | +0.6 | −3…−5 s | +0.4 ± 0.3 / −0.9 ± 0.1 |
| datsun620 (DL20) | +1.6 | +1.6 | −6…−8 s | +3.3 ± 0.2 / +1.0 ± 0.2 |
| fordfocusst2019 (RDA) | +0.7 | +1.2 | −0.1…−0.4 s | +1.4 ± 0.2 / +0.1 ± 0.2 |
| 4a-ge / ae86 | +2.0 | +1.6 | −1…−3 s | – / +1.1 ± 0.2 |
| lotuselise | +2.2 | +2.6 | −5…−7 s | – |
| mazdarx7_fc | +2.3 | +2.5 | −9…−10 s | – |
| nissanskyline2000gtx (S02) | +2.9 | +2.8 | −4…−6 s | – |
| mazdarx8 | +2.4 | +4.1 | −0.2…−0.4 s | – |

**Native 17 Nov (8 repetitions, ◐):** the model and the native simulation disagree. In the S15 the current ND tune was fastest and the Mini was 1.7 s slower. In the AE86 the ND engine with the model's tune was 0.9 ± 0.1 s faster than the current 4A-GE tune, and the Mini was within the noise. So the model's ranking cannot be used yet; the most robust finding is the ND engine (PV2) in a light RWD car. A rerun with the AE86's current setup (ratios 2.91/2.04/1.51/1.15/0.97/0.86, decel lock 0.28) gave ±0 at FD 4.50, −1.0 ± 0.1 s at FD 4.35 and −0.3…−0.4 s at other FDs, so the gain depends on gearing and is not yet certain. **In-game test 17 Nov (●, AE86, North v2):** GE4 runs 43–44 371.36 / 371.20 s. PV2 with the player's own tune (limiter 8687 and Peak RPM 9742 at max, High 218, Medium 281, Low 332): FD 4.52 runs 45–46 372.97 / 370.97 s, **FD 4.35 runs 47–48 369.03 / 369.22 s (−2.1 s vs the GE4, repeated)**. The native simulation predicted −1.0 ± 0.1 s for FD 4.35, so the direction was right. The model's Part Setup values were not run in the game. The player shifts up at about 8800–9000 rpm and spends 15–25 % of the lap above 8500 rpm, so lowering the limiter is probably harmful even though the models do not see it ◐. For now the most reliable line: limiter and Peak RPM up, Low up, Mid and High down until the class is filled. According to the model, engines with a high part factor (Mini 0.84 + turbo 1.6, ND and Datsun 0.89) gain the most from the sliders. Touge's current fit leaves 3–10 s on them.

## Part factors by engine ●

All 137 engines from the game data (part_stat_factors), largest first. The part factor is the same for the ECU, camshaft, head, block and fuel system. Median 0.74, smallest 0.20, largest 1.09. Turbo part = the multiplier of the Turbo Kit or factory turbo part.

| Engine | Stock in | Factory turbo | Mass kg | Limiter | Part factor (ECU, cam, head, block, fuel) | Intake | Exhaust manifold and exhaust | Turbo part |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mazdarx7_fc | mazdarx7_fc | ● | 157 | 8500 | 1.09 | 1.38 | 1 | 1.5 |
| nissan180sx | nissan180sx | ● | 268 | 7200 | 1.09 | 1.38 | 1 | 1.5 |
| nissan180sx_sp1 | – | ● | 268 | 7200 | 1.09 | 1.38 | 1 | 1.5 |
| civic | civic |  | 140 | 7800 | 1 | 1.3 | 0.9 | 1 |
| vaz2108 | vaz2108 |  | 127 | 6000 | 1 | 1.3 | 0.9 | 0.5 |
| nissan300zx | nissan300zx | ● | 220 | 6800 | 0.98 | 1.28 | 0.88 | 1.5 |
| nissan300zx_cabrio | nissan300zx_cabrio | ● | 220 | 6800 | 0.98 | 1.28 | 0.88 | 1.5 |
| nissansilvias14 | nissansilvias14 | ● | 180 | 7500 | 0.95 | 1.25 | 0.85 | 1.5 |
| mclarenf1 | mclarenf1 |  | 275 | 7600 | 0.95 | 1.16 | 0.78 | 0.5 |
| nissansilvias13 | nissansilvias13 | ● | 180 | 7500 | 0.91 | 1.25 | 0.81 | 1.5 |
| mitsubishievo6 | mitsubishievo6 | ● | 170 | 7600 | 0.9 | 1.24 | 0.8 | 1.5 |
| porsche911 | porsche911 | ● | 230 | 7300 | 0.9 | 0.86 | 0.8 | 1.5 |
| supra2020_cabrio | supra2020_cabrio | ● | 140 | 7000 | 0.9 | 1.2 | 0.8 | 1.5 |
| ferrarif40 | ferrarif40 | ● | 210 | 7500 | 0.9 | 1.2 | 0.8 | 0.5 |
| volvo | volvo |  | 140 | 6500 | 0.9 | 1.2 | 0.8 | 0.5 |
| buickgnx | buickgnx |  | 200 | 6200 | 0.89 | 1.19 | 0.79 | 1.5 |
| mazdamx5 | mazdamx5 |  | 130 | 7200 | 0.89 | 1.19 | 0.79 | 1.5 |
| skyliner31 | skyliner31 | ● | 230 | 7600 | 0.89 | 1.19 | 0.79 | 1.5 |
| subaruforester | subaruforester | ● | 120 | 6500 | 0.89 | 1.18 | 0.79 | 1.5 |
| 4a-ge | – |  | 145 | 7400 | 0.89 | 0.89 | 0.89 | 0.89 |
| 4g63 | – | ● | 175 | 7500 | 0.89 | 0.89 | 0.89 | 0.89 |
| d15b | – |  | 150 | 7700 | 0.89 | 0.89 | 0.89 | 0.89 |
| ae86 | ae86 |  | 154 | 7400 | 0.89 | 1.19 | 0.79 | 0.5 |
| datsun620 | datsun620 |  | 160 | 6200 | 0.89 | 1.19 | 0.79 | 0.5 |
| mazdamx5_90 | mazdamx5_90 |  | 155 | 7200 | 0.89 | 1.19 | 0.79 | 0.5 |
| mazdamx5cabrio_90 | mazdamx5cabrio_90 |  | 155 | 7200 | 0.89 | 1.19 | 0.79 | 0.5 |
| mercedesbenz190evo2 | mercedesbenz190evo2 |  | 170 | 6600 | 0.89 | 1.19 | 0.79 | 0.5 |
| toyotamr2 | toyotamr2 |  | 143 | 7000 | 0.89 | 1.19 | 0.79 | 0.5 |
| skyliner32 | skyliner32 | ● | 230 | 7400 | 0.86 | 1.2 | 0.8 | 1.5 |
| subaruwrc2008 | subaruwrc2008 | ● | 125 | 7400 | 0.86 | 1.14 | 0.77 | 1.5 |
| corvettec3 | corvettec3 |  | 280 | 6200 | 0.85 | 1.04 | 0.81 | 1.5 |
| infinity_q60 | infinity_q60 | ● | 195 | 6800 | 0.85 | 1.19 | 0.75 | 1.5 |
| toyotayarisgr2020 | toyotayarisgr2020 | ● | 120 | 7200 | 0.85 | 1.04 | 0.81 | 1.5 |
| vantage | vantage | ● | 209 | 8000 | 0.85 | 1.2 | 0.75 | 1.5 |
| mitsubishieclipse99 | mitsubishieclipse99 |  | 185 | 6500 | 0.85 | 1.14 | 0.75 | 0.5 |
| mini | mini | ● | 130 | 6500 | 0.84 | 1.14 | 0.74 | 1.6 |
| silvias15 | silvias15 | ● | 180 | 7500 | 0.83 | 1.11 | 0.74 | 1.5 |
| silvias15_sp1 | – | ● | 180 | 7500 | 0.83 | 1.11 | 0.74 | 1.5 |
| nissans30z | nissans30z |  | 249 | 7000 | 0.83 | 1.12 | 0.73 | 0.5 |
| toyotasuprarz | toyotasuprarz | ● | 230 | 7000 | 0.82 | 1.1 | 0.73 | 1.5 |
| auditt | auditt | ● | 160 | 6800 | 0.81 | 1.07 | 0.72 | 1.5 |
| skyliner34 | skyliner34 | ● | 250 | 7000 | 0.81 | 1.08 | 0.72 | 1.5 |
| toyotagt86 | toyotagt86 |  | 200 | 7400 | 0.81 | 1.08 | 0.72 | 0.5 |
| alfaromeogiuliagtam | alfaromeogiuliagtam | ● | 240 | 7200 | 0.8 | 0.91 | 0.57 | 1.5 |
| bmw_i8 | bmw_i8 | ● | 210 | 6500 | 0.8 | 1.05 | 0.72 | 1.5 |
| golfgti | golfgti | ● | 140 | 6000 | 0.8 | 1.1 | 0.7 | 1.5 |
| mustang650 | mustang650 | ● | 186 | 7500 | 0.8 | 1.06 | 0.7 | 1.5 |
| nissanskyline2000gtx | nissanskyline2000gtx |  | 199 | 7300 | 0.8 | 1.06 | 0.7 | 1.5 |
| porschesinger | porschesinger | ● | 150 | 7100 | 0.8 | 1.07 | 0.71 | 1.5 |
| lexuslfa | lexuslfa |  | 160 | 9000 | 0.8 | 1.15 | 0.7 | 0.5 |
| sr20 | – |  | 190 | 7200 | 0.79 | 1.09 | 0.69 | 0.5 |
| fordfocusst2019 | fordfocusst2019 | ● | 109 | 6500 | 0.78 | 1.06 | 0.68 | 1.5 |
| subaruwrxsti | subaruwrxsti | ● | 204 | 8000 | 0.78 | 1.06 | 0.68 | 1.5 |
| pontiactransam77 | pontiactransam77 |  | 270 | 5000 | 0.78 | 1.08 | 0.68 | 0.5 |
| mazdarx7 | mazdarx7 | ● | 120 | 8300 | 0.77 | 1.03 | 0.68 | 1.5 |
| mazdarx7_sp1 | – | ● | 120 | 8300 | 0.77 | 1.03 | 0.68 | 1.5 |
| toyotasupra2020 | toyotasupra2020 | ● | 140 | 7000 | 0.765 | 1.02 | 0.68 | 1.5 |
| audirs6avantc7 | audirs6avantc7 | ● | 190 | 6700 | 0.75 | 1 | 0.66 | 1.5 |
| audirs7 | audirs7 | ● | 190 | 6700 | 0.75 | 1 | 0.66 | 1.5 |
| bmwm2g87 | bmwm2g87 | ● | 160 | 6800 | 0.75 | 1.15 | 0.66 | 1.5 |
| bmwm3g81_touring | bmwm3g81_touring | ● | 160 | 6800 | 0.75 | 1.15 | 0.66 | 1.5 |
| fordgt_mk2 | fordgt_mk2 | ● | 205 | 7000 | 0.75 | 0.99 | 0.67 | 1.5 |
| lotuselise | lotuselise |  | 140 | 8200 | 0.75 | 1.15 | 0.66 | 1.5 |
| mercedesbenzc63 | mercedesbenzc63 | ● | 367 | 6800 | 0.75 | 1 | 0.67 | 1.5 |
| mitsubishievo9 | mitsubishievo9 | ● | 195 | 7500 | 0.75 | 1.02 | 0.66 | 1.5 |
| suzukicarry | suzukicarry |  | 100 | 7800 | 0.75 | 1.15 | 0.66 | 1.5 |
| mazdarx8 | mazdarx8 |  | 120 | 8300 | 0.75 | 1.05 | 0.65 | 0.5 |
| bmw_m3_e92_cabrio | bmw_m3_e92_cabrio | ● | 135 | 6800 | 0.74 | 1 | 0.66 | 1.5 |
| bmw_m3_e92_gts | bmw_m3_e92_gts | ● | 135 | 6800 | 0.74 | 1 | 0.66 | 1.5 |
| mitsubishievox | mitsubishievox | ● | 134 | 7800 | 0.74 | 1.02 | 0.64 | 1.5 |
| skyliner35 | skyliner35 | ● | 276 | 7500 | 0.73 | 0.97 | 0.65 | 1.5 |
| lexusrcf | lexusrcf |  | 222 | 7600 | 0.73 | 0.97 | 0.65 | 0.5 |
| bmw_m3_e36 | bmw_m3_e36 |  | 180 | 6600 | 0.72 | 1 | 0.63 | 0.5 |
| audir8 | audir8 | ● | 250 | 7800 | 0.7 | 1.05 | 0.6 | 1.5 |
| bmwm2 | bmwm2 | ● | 194 | 7500 | 0.7 | 0.95 | 0.62 | 1.5 |
| lamborghinievo | lamborghinievo | ● | 250 | 8000 | 0.7 | 1.05 | 0.6 | 1.5 |
| chevroletcamaro2016 | chevroletcamaro2016 |  | 193 | 6400 | 0.7 | 0.96 | 0.6 | 0.5 |
| hondas2000 | hondas2000 |  | 147 | 8300 | 0.7 | 1 | 0.6 | 0.5 |
| toyotamajesta | toyotamajesta |  | 195 | 7200 | 0.7 | 1.05 | 0.6 | 0.5 |
| bmwm4 | bmwm4 | ● | 140 | 7000 | 0.69 | 0.94 | 0.61 | 1.5 |
| toyotasupraa70 | toyotasupraa70 | ● | 270 | 6800 | 0.68 | 1.08 | 0.59 | 1.5 |
| civicek9 | civicek9 |  | 184 | 8500 | 0.66 | 0.92 | 0.57 | 0.5 |
| hondacivictr2020 | hondacivictr2020 |  | 145 | 8100 | 0.66 | 0.92 | 0.57 | 0.5 |
| 2jz-gte | – | ● | 310 | 7000 | 0.65 | 0.87 | 0.55 | 1.5 |
| altezza | altezza |  | 240 | 7100 | 0.65 | 0.95 | 0.55 | 1.5 |
| hotrod | hotrod | ● | 195 | 7200 | 0.65 | 0.94 | 0.61 | 1.5 |
| nissan400z | nissan400z | ● | 240 | 6800 | 0.65 | 1 | 0.55 | 1.5 |
| toyotacresta100 | toyotacresta100 | ● | 210 | 7000 | 0.65 | 0.95 | 0.55 | 1.5 |
| toyotamark2_100 | toyotamark2_100 | ● | 210 | 7000 | 0.65 | 0.95 | 0.55 | 1.5 |
| toyotasoarer | toyotasoarer | ● | 240 | 7100 | 0.65 | 0.95 | 0.55 | 1.5 |
| bmwe30m3 | bmwe30m3 |  | 136 | 6750 | 0.65 | 0.9 | 0.57 | 0.65 |
| bmw_z4_e86 | bmw_z4_e86 |  | 220 | 8000 | 0.65 | 0.94 | 0.61 | 0.5 |
| bmwm5e34 | bmwm5e34 |  | 151 | 6900 | 0.65 | 0.91 | 0.55 | 0.5 |
| toyotagr86 | toyotagr86 |  | 171 | 7200 | 0.65 | 0.9 | 0.56 | 0.5 |
| chevycamaro70 | chevycamaro70 |  | 242 | 7500 | 0.64 | 0.94 | 0.54 | 0.5 |
| mb_gtr_cabrio | mb_gtr_cabrio | ● | 209 | 7000 | 0.6 | 0.85 | 0.52 | 1.5 |
| mbgelandewagenw463 | mbgelandewagenw463 | ● | 220 | 6500 | 0.6 | 0.65 | 0.5 | 1.5 |
| mercedesbenzamggt2019 | mercedesbenzamggt2019 | ● | 209 | 7000 | 0.6 | 0.84 | 0.52 | 1.5 |
| nissanz31 | nissanz31 | ● | 178 | 6000 | 0.6 | 0.85 | 0.51 | 1.5 |
| hondaintegra | hondaintegra |  | 180 | 8000 | 0.6 | 0.9 | 0.5 | 0.5 |
| acuransx | acuransx |  | 200 | 8000 | 0.59 | 0.84 | 0.5 | 0.5 |
| charger | charger |  | 281 | 6400 | 0.59 | 0.86 | 0.5 | 0.5 |
| lamborghinidiablo | lamborghinidiablo |  | 232 | 7300 | 0.58 | 0.96 | 0.48 | 0.5 |
| bmwe46m3 | bmwe46m3 |  | 149 | 7000 | 0.57 | 0.855 | 0.475 | 0.5 |
| bmwm4g82 | bmwm4g82 | ● | 160 | 6800 | 0.55 | 0.8 | 0.46 | 1.5 |
| mclaren720s | mclaren720s | ● | 170 | 8500 | 0.55 | 0.79 | 0.47 | 1.5 |
| bmwm5e39_vagon | bmwm5e39_vagon |  | 208 | 7000 | 0.55 | 0.8 | 0.45 | 0.5 |
| jaguar_ftype | jaguar_ftype |  | 240 | 7500 | 0.55 | 0.81 | 0.47 | 0.5 |
| maloor82015 | maloor82015 |  | 240 | 6500 | 0.55 | 0.79 | 0.47 | 0.5 |
| mustangs197 | mustangs197 |  | 245 | 7000 | 0.55 | 0.76 | 0.38 | 0.5 |
| nissan370z | nissan370z |  | 174 | 6800 | 0.55 | 0.81 | 0.46 | 0.5 |
| vipersrt10 | vipersrt10 |  | 230 | 6300 | 0.55 | 0.79 | 0.47 | 0.5 |
| dodgechallengerrt | dodgechallengerrt |  | 245 | 7250 | 0.53 | 0.78 | 0.45 | 0.5 |
| mustangrtx | mustangrtx |  | 290 | 6200 | 0.52 | 0.77 | 0.43 | 0.5 |
| bmwm5f90 | bmwm5f90 | ● | 229 | 8250 | 0.5 | 0.75 | 0.4 | 1.5 |
| bmwm5x5 | bmwm5x5 | ● | 229 | 7200 | 0.5 | 0.75 | 0.42 | 1.5 |
| nissanskyliner33vspec | nissanskyliner33vspec | ● | 280 | 7800 | 0.5 | 0.76 | 0.4 | 1.5 |
| porsche911gt3 | porsche911gt3 | ● | 230 | 9000 | 0.5 | 0.65 | 0.52 | 1.5 |
| rd26tt | – | ● | 300 | 7800 | 0.5 | 0.76 | 0.4 | 1.5 |
| bmwe31 | bmwe31 |  | 155 | 6400 | 0.5 | 0.8 | 0.4 | 0.5 |
| bmwm5e60 | bmwm5e60 |  | 240 | 8250 | 0.5 | 0.65 | 0.52 | 0.5 |
| corvettec7 | corvettec7 |  | 267 | 6400 | 0.5 | 0.7 | 0.42 | 0.5 |
| dodgecharger2020 | dodgecharger2020 |  | 254 | 5800 | 0.5 | 0.78 | 0.41 | 0.5 |
| nissan350z | nissan350z |  | 205 | 6800 | 0.5 | 0.76 | 0.41 | 0.5 |
| tesla_s_plaid | tesla_s_plaid |  | 300 | 10000 | 0.5 | 0.65 | 0.52 | 0.5 |
| mustang350 | mustang350 |  | 195 | 7200 | 0.49 | 0.75 | 0.41 | 0.5 |
| corvettec8 | corvettec8 |  | 230 | 7100 | 0.48 | 0.62 | 0.4 | 0.7 |
| chevroletchevelless1970 | chevroletchevelless1970 |  | 270 | 6200 | 0.47 | 0.61 | 0.39 | 0.5 |
| corvettec6 | corvettec6 |  | 201 | 7000 | 0.46 | 0.7 | 0.38 | 0.5 |
| vq37vhr | – |  | 320 | 6800 | 0.43 | 0.69 | 0.35 | 0.5 |
| lamborghiniaventadors | lamborghiniaventadors |  | 235 | 8500 | 0.4 | 0.64 | 0.32 | 0.5 |
| ls | – |  | 315 | 7000 | 0.4 | 0.68 | 0.36 | 0.5 |
| van | van |  | 199 | 4800 | 0.4 | 0.7 | 0.3 | 0.5 |
| bmwm6e24 | bmwm6e24 |  | 161 | 7000 | 0.35 | 0.61 | 0.25 | 0.5 |
| lamborghinimurcielago | lamborghinimurcielago |  | 270 | 8200 | 0.35 | 0.59 | 0.27 | 0.5 |
| viper | viper |  | 323 | 6200 | 0.35 | 0.59 | 0.27 | 0.5 |
| mustang_hoonigan | mustang_hoonigan |  | 220 | 8000 | 0.2 | 0.34 | 0.12 | 0.4 |

## Not yet confirmed and sources

- The engine comparison comes from the Touge route model (◐). The native simulation (17 Nov, 8 repetitions) did not confirm the model's ranking; the ND engine in the AE86 (−0.9 s) is worth an in-game test.
- Whether the part factor explains players' experience of "hidden stats" on the Mini and S02 is an inference (◐). The S02's factor of 0.80 is above average, but in the model it finished 2.8 s off the best because of its heavy mass (199 kg).
- Sources: analyysi/moottorihaku_1711, analyysi/moottorikomponentit, analyysi/c3_build_periaatteet.md, tyokalu/data/moottorit.json.

---

← [Body dimensions](body-dimensions.md) · [Contents](README.md) · [Gearing and gearbox](gearing.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
