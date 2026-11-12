[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/tyres.md)

# Tyres

## In short

The tyre is a big lever, and the most important choices are the width and the rim part. In our experience going from 265 mm to 285–325 mm has been worth about two seconds on a long touge run ◐. The same size often comes with two rim parts, and only the one with the lower base profile gives the full friction bonus of +0.08 ● game data. Diameter matters through wheel mass and ride height, and spacers add a little grip.

Rule: tyres must not stick out of the fenders, even though the game allows it.

Markers: ● confirmed in game or in the game code, ◐ native simulation or inferred, not tested in game.

## Choosing the size

**How the game calculates it:**

1. Tyre friction = 1 + the rim part's friction bonus (fric_add), and it scales the tyre's peak force directly ●. The game shows this as the grip value (for example 1.08).
2. The same size often has two rim parts. The one with the lower base profile gives +0.08, the higher one +0.03–0.05 ●. For example 265 R16: base profile 40 = +0.08, base profile 45 = +0.03.
3. The full +0.08 starts at 265 mm. 245–255 mm gets at most +0.05 and 225–235 mm +0.04 ●.
4. Width adds grip with a power of 0.41: grip factor = (width / 185)^0.41 × friction ● (route model, matches the native code).
5. Tyre grip peaks at 2.0 bar. 1.0 or 3.0 bar costs about 1–2.5 % grip ●.

| Width | Highest friction bonus | Grip factor | Difference to 265 |
| --- | --- | --- | --- |
| 225 mm | +0.04 | 1.13 | −10 % |
| 245 mm | +0.05 | 1.18 | −6 % |
| 265 mm | +0.08 | 1.25 | 0 |
| 285 mm | +0.08 | 1.29 | +3 % |
| 325 mm | +0.08 | 1.36 | +9 % |
| 345 mm | +0.08 | 1.39 | +11 % |

**When you go wider:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Wider tyre | More corner speed and braking grip, most in slow corners. | A heavier wheel slows acceleration, and the tyre may stick out of the fender. | ◐ 265 → 285 was worth almost two seconds, 285 → 325 only about half a second more. ◐ In a tight corner the gain was about ten times larger than in a fast one. |
| Lower base profile in the same size | Friction +0.08 instead of +0.03–0.05. | — | ● Rim part data. ◐ Worth close to a second on a full run. |

By the grip factor the gain would keep growing evenly, but in the native model the width gain shrinks above 285 mm. The reason is still open ◐.

## Small vs large tyre

**How the game calculates it:**

1. Diameter = rim × 25.4 + 2 × width × profile / 100 mm ●. The game's Tire profile −10…+10 is profile percentage points (285/35 → 285/25…285/45) ●.
2. Wheel mass comes from the size: m = 1000 · r² · width kg, and inertia I = 0.7 · m · r² ●. Under acceleration each wheel also weighs 0.7 × its own mass extra because it spins ●.
3. A larger tyre raises the body by the radius change: on a 285 mm tyre 2.85 mm per profile point ●.
4. In the native model only the total ratio (gear × final drive × radius) matters ●. A larger radius makes the gearing longer, which the final drive can correct: FD_new = FD × r_new / r_old. The wheel rolls on radius r − load / vertical stiffness ●.
5. Profile also changes the tyre's vertical stiffness and its Pacejka defaults ●, but with ride height held constant the grip difference stayed within −0.7…+1.2 % ◐.

| Tyre | Radius | Wheel mass |
| --- | --- | --- |
| 185/50 R14 | 0.27 m | 13.5 kg |
| 265/30 R16 | 0.28 m | 21.2 kg |
| 325/25 R17 | 0.30 m | 28.7 kg |
| 285/35 R18 | 0.33 m | 30.7 kg |

**When you go larger (diameter up):**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Larger rim or profile | The body rises, the gearing gets longer and the wheel weighs more. | Weaker acceleration, a higher centre of gravity, and too long gears without an FD correction. | ◐ Same radius, heavy wheel 30.7 vs 13.5 kg: 0–100 km/h +5 %. ◐ Three rim sizes with the same radius gave the same result. |
| Profile up (Tire profile +) | The body rises about 2.8 mm per step and the tyre flexes more. | A high body if the spring length is not shortened. | ◐ Profile ±10 with ride height held constant: at most ±2 s on a ten-minute run. |

A smaller and lighter wheel accelerates better, but the difference is small, so a heavy wheel is no reason to avoid a wide tyre ◐. Choose the size by grip, then correct the radius with the final drive and the height with the spring length.

## Spacers and track width

**How the game calculates it:**

1. Wheel offset (cm) = the body kit's fender part offset + the spacer value ●. The game rounds the white number in Part Setup to an integer; the exact value is only visible in the tyre component view ●.
2. The wheels sit at x = ∓ track / 2 ●, and track = the car's base track + offset (factor 1 is inferred ◐). Spacers do not change mass ●.
3. Tyre width does not move the wheel ●. A wider tyre does not widen the track; it fills the fender in both directions.
4. A wider track lowers the whole car's load transfer m · a · h / t ● and stiffens the axle in roll with the square (k · t²) ●. The widened axle takes a larger share of the roll moment, so track also works as a balance setting, like a bar.
5. The body kit's only physics stat is track width: it does not change drag or downforce ●.

**When you widen (offset up):**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Both axles | A little more lateral grip and less roll. | The tyre sticks out of the fender (not allowed). | ◐ +0.10 m +1.4 % grip, +0.26 m +3.2 %. ◐ On a full run the gain showed only with narrow tyres and stock bars; otherwise it was within noise. |
| Rear only | The rear gains grip and the car understeers slightly more. | The nose pushes. | ◐ Rear +0.20 m: grip +2.7 %, front share of roll stiffness 0.555 → 0.520. |
| Front only | The nose gains a little grip. | The rear gets relatively lighter. | ◐ Front +0.20 m: grip +0.5 %, front share → 0.587. |

The widening gain shrinks with tyre width: +0.20 m gave +2.6 % on a 185 mm tyre, +1.9 % on 245 mm and +1.6 % on 285 mm ◐. With a wide tyre, use offset first of all to fit the tyre inside the fender.

## Effect on other settings

Setup order: choose the tyre size and rim part first, then the offset so the tyre fits, then the final drive and spring length for the new radius.

| Setting | How it links to the tyres in the game physics |
| --- | --- |
| Gearing | Only the total ratio matters ●, so a radius change is corrected with the final drive. |
| Spring length | A larger radius raises the body by the same amount ●. Shorten the spring if you want the same height. |
| Bars and springs | The tyre's vertical stiffness (p + 30 kPa) · (10 · width + 1) · r · 0.8 is in series with the suspension ●. A wide tyre is stiffer, and track stiffens roll with the square. Width and bar split overlapped by about a second in our experience ◐. |
| Tyre pressure | Grip peaks at 2.0 bar ●. Pressure lowers rolling resistance (∝ 1 / pressure) ●, so 3.0 bar is fastest on a straight (0–150 km/h about 7 % quicker than at 2.0 bar). Tyre type does not change the pressure effect, and wear does not cost grip before condition reaches 0 ●. |
| Mass | A wide and large wheel weighs more. Mass costs about 2 % grip per 100 kg ◐, but the extra wheel mass is small next to the width gain. |
| Camber | Camber costs 0.5 % longitudinal grip per degree and does not raise the lateral peak ●. |
| Kerbs and gutters | Leaning on the rising outer edge of a corner added +14…+55 % grip in the native model, and an inside gutter +26 % ◐. The effect is larger than the tyre size. |

## Symptoms

A tyre choice changes the grip level of the whole car, so symptoms usually show at the end with the narrower tyre or the lower-friction rim part.

| Phase | Symptom | What happens in the game | Change |
| --- | --- | --- | --- |
| Braking into the corner | Long braking distance and ABS working hard | The tyre's peak force is low | Check the rim part's friction (+0.08?) and the width. |
| Mid-corner | The whole car slides out evenly in slow corners | The grip level is low and neither end stands out | Wider tyres, 265 mm or more. Width helps most in tight corners ◐. |
| Mid-corner | The nose or the rear clearly gives up first | The axles differ in tyre width or friction | Even out the friction (same rim part type front and rear) and correct the rest with the bars. |
| Exit, full throttle | The car accelerates lazily onto the straight | The total ratio got longer with the larger radius, or the wheels are heavy | Correct the final drive: FD × r_new / r_old. |
| Straight and top speed | Top speed changed after a tyre change | The total ratio changed | Correct the final drive. |
| Bumps, kerbs and gutters | The body hits the ground or the car sits too high | The radius changed the ride height | Correct with the spring length. |

## Final tip

The widest tyre that fits inside the fender, with the lower-base-profile rim part (friction +0.08), gives the most grip. After choosing it, correct the final drive for the radius and the ride height with the spring length. Above 285 mm the native model shows only a small further gain.

**Simulation experience ◐ (native model, not tested in game):** pressures 2.5 and 3.0 bar were equally fast. 3.0 → 2.0 bar was 1.2 s slower and 1.5 bar 2.6 s slower, because rolling resistance outweighed the grip gain. Lowering the rear pressure cost more than lowering the front. 265/30 R16 was 1.9 s and 285/30 R16 1.1 s slower than 325/25 R17.

## Not yet confirmed

- Why the width gain shrinks above 285 mm in the native model is open ◐.
- The track factor 1 (offset 10 cm = track +10 cm) is inferred, not read from the code ◐.
- Tyre wear lowers friction (up to 40–60 % depending on the tyre series), but the exact formula is unverified and is not modelled in Touge or in native runs.
- That width helps most in tight corners rests on a single native comparison.

---

← [The whole chassis](whole-chassis.md) · [Contents](README.md) · [Springs](springs.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
