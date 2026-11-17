[![Project Touge choriso's Tuning Bible](banner.png)](README.md)

[Suomeksi](fi/gearing.md)

# Gearing and gearbox

## In short

Gearing decides which rpm the engine is at in each corner and on each straight. The choice of gearbox (mass and shift time) and the overall ratio are a medium-sized lever, about a second on a North lap ◐. Fine-tuning the gear steps is a small lever, under 0.5 s ◐. Tyre diameter changes the overall ratio, so changing tyre size always needs an FD correction ●.

## How the game calculates it

1. Wheel torque = engine torque × gear × FD, and speed = rpm / (gear × FD) × tyre radius ●.
2. The tyre radius comes from its size: diameter = rim × 25.4 + 2 × width × profile / 100 (mm) ●. A larger diameter lengthens every gear by the same proportion.
3. The gearbox upgrade level (gearbox_1…6) multiplies FD by 0.98 / 0.95 / 0.92 / 0.90 / 0.87 / 0.84. At levels 3–6 every gear and the FD get a slider with a step of ×1.04 / 1.05 / 1.08 / 1.08, and the slider has 20 ticks per step ●.
4. Gearboxes can be swapped between all cars ●. Gearboxes have their own mass and shift delay ●:

| Gearbox (game name) | Gears | Mass | Shift delay |
| --- | --- | --- | --- |
| T50S (transmission_t50) | 6 | 35 kg | 0.25 s |
| T50 (transmission_t40) | 5 | 39 kg | 0.35 s |
| T60 (transmission_t40a) | 6 | 50 kg | 0.35 s |
| T70 (transmission_t50a) | 7 | 55 kg | 0.28 s |
| Cars' own 8-speeds (e.g. Lexus RC F, Alfa Giulia GTAm, M2 G87) | 8 | 50 kg | 0.3–0.5 s |
| Cars' own 6-speeds | 6 | 50 kg | 0.3–0.5 s |

## When you raise it

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| FD up (shorter) | Better acceleration in every gear, and more shifts. | Top gear runs out mid-straight and the car hits the limiter. | ◐ Supra A90 FD 3.98 → 4.14: −1.0 ± 0.4 s (8 repetitions). |
| Wider or taller tyre | Diameter grows and every gear gets longer. | The car feels lazy out of corners. | ◐ Integra 285/40: +0.9 s; same with FD corrected −1.4 s; profile chosen so the diameter stays the same: −8.4 s. |
| Lower profile | Diameter shrinks and the gears get shorter. | Same as FD too high. | ◐ Correct FD = old FD × new diameter / old diameter, so only the tyre changes. |
| Longer top gear | Top speed rises. | The gear goes unused and the other gears spread apart. | ● Size the top gear to the route's real top speed (North about 250 km/h) so every gear is used. |

## How it interacts and setup order

1. **Gearbox first.** In the simulation model the T50S won with every build, and the gap came mostly from mass (35 vs 50 kg) and shift delay ◐. In the native simulation gearbox mass cost 0.04–0.07 s per kg on a North lap, so 15 kg is about 0.6–1.0 s ◐. The best 8-speed (Lexus RC F) was about 1 s behind the T50S in the model ◐. In the native simulation (17 Nov, 8 repetitions, S15 and AE86) the 8-speeds were 1.1–2.9 s and the T70 0.8–2.2 s slower than the T50S, with all ratios searched to the route's top speed ◐. So the 8-speed advantage does not show in C3 on North v2.
2. **Top gear to the route's top speed.** Every gear in use, and top gear runs out just above the route's top speed ●.
3. **Gear steps.** Sets proven good in the game are progressive: the lowest steps may stretch to 1.55, steps 3→4 and 4→5 at most about 1.30, and the last at most 1.35 ◐. An even 1.34 on every step made the upper gear steps too long ●.
4. **FD last**, to suit the engine curve. A wide power band tolerates a wider gearbox: on the Mini the 5-speed T50 was as good as the T50S in the model ◐.

| Factor | How it relates to gearing |
| --- | --- |
| Engine curve | A narrow power band needs close ratios so the engine is still in the band after a shift. |
| Tyre size | Diameter multiplies every ratio. Keep the driven axle's diameter within ±2 % or correct FD. |
| Tyre width | Width does not move the wheel's centre line. Only spacers and offset change track width ●. |
| Shift time | A short shift time favours close ratios and a long one wider ratios. In the native simulation the effect of shift time was within the noise ◐. |

## Symptoms

| Phase | Symptom | Adjustment |
| --- | --- | --- |
| Straight | Top gear runs out before braking | FD down or longer top gear |
| Straight | Top gear is never used | FD up or shorter top gear |
| Exit | After a shift the engine drops below the power band | Close up that step (≤ 1.30) |
| Exit | The limiter arrives just before braking | Lengthen this gear or shift up earlier |
| All | The car feels lazy after new tyres | Diameter grew: correct FD |
| All | An engine swap did not bring the expected gain | Search FD again for the new curve. In the game 17 Nov ●: AE86 PV2 FD 4.52 → 4.35 −2.1 s; Supra FD 3.98 → 4.14 route record; S15 ND FD 4.59 → 4.40 6:08.76 (was 6:11.25). The native simulation predicted the direction in all three |

## Final tip

Pick a light gearbox (T50S), size the top gear to the route's top speed and correct FD every time the tyre size changes. Only then fine-tune the steps.

## Not yet confirmed and sources

- The 8-speeds' shift time in the native simulation is scaled from the game's delay (0.16 s × delay / 0.25), so the result is not confirmed in the game ◐.
- The wide spread the model favoured (short first, long sixth) did not show up in the game, so it is not recommended ◐.
- Sources: analyysi/valityslaskin, analyysi/north_c3 (130 gearboxes), analyysi/optimointi_1111/tulokset/haku_1611.

---

← [Engine](engine.md) · [Contents](README.md) · [Glossary](glossary.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
