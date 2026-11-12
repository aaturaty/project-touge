[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/body-dimensions.md)

# Body dimensions as a setup aid

## In short

You can hardly adjust the body dimensions, but they tell you where to start your setup. The biggest lesson is the wheelbase: a rear-biased bar split from a short roadster did not carry over to longer cars, and a split corrected for wheelbase has worked in game on nine cars ●. Track width and centre of gravity height decide how much load moves, and mass decides how stiff the springs must be for the same feel.

The only adjustable dimensions are track width (fender part and spacers), centre of gravity (body Stage, weight reduction and spring length) and mass. Everything else comes with the choice of car.

Markers: ● confirmed in game or in the game code, ◐ native simulation or inferred, not tested in game, ○ real-car theory.

## Wheelbase

**How the game calculates it:**

1. Longitudinal load transfer is m · a · h / L ●. A short car moves more weight forward under braking and unloads the rear more than a long one.
2. A short car rotates more easily, because the tyres' lever arm around the car's vertical axis is shorter ○. That is why a short car turns with only a little rear movement, and a long car needs more front.
3. Wheelbase is part of the Ackermann geometry (wheel angle depends on L and track) ●, but Ackermann had no grip effect ◐.
4. In our experience the front share of roll stiffness (LLTD) minus the front weight share moves forward as the wheelbase grows ●. A short car has worked with a rear-biased split, a long one with an even or front-biased split.

**What has worked in game, by wheelbase:**

| Wheelbase | Front share of roll stiffness − front weight share |
| --- | --- |
| about 2.3 m | about −0.13 (clearly rear-biased) |
| 2.4–2.5 m | about −0.09…−0.06 |
| 2.5–2.6 m | about −0.05…−0.02 |
| 2.7 m | about +0.02…+0.03 (front-biased) |

Bar numbers do not compare from one car to another, because springs, track, mass and centre of gravity also affect them. Compare the split, not the number.

In the gearing, short cars gained most from an about 10 % longer final drive ◐. This cannot be separated from the rev limiter, because the short cars also had the highest limiter.

## Track width and offset

**How the game calculates it:**

1. Lateral load transfer is m · a · h / t ●. A wider track moves less load to the outer wheel, and since the tyre loses friction as load grows, grip rises.
2. Track = the car's base width + offset, and offset = the body kit's fender part + spacer (cm) ●. The body kit changes nothing else in the physics, for example not drag ●. The white offset number in Part Setup is rounded to an integer ●.
3. Tyre width does not move the wheel's mounting point ●. The offset gain shrinks with a wide tyre: +0.20 m on both axles gave +2.6 % on 185 mm, +1.9 % on 245 mm and +1.6 % on 285 mm ◐.
4. A wider axle is stiffer in roll (spring and bar stiffness × t²), so it takes a larger share of the roll moment ●. Its grip still rises: rear +0.20 m moved the front share 0.555 → 0.520 and added 2.7 % grip, front +0.20 m only 0.5 % ◐.
5. Rule: tyres must not stick out of the fenders. In practice this limits the offset.

**When you widen:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Both axles | Grip rises slightly in all corners. | Tyre outside the fender (against the rule). | ◐ +0.10 m +1.4 %, +0.26 m +3.2 %. ◐ On a full run the gain showed only with narrow tyres; otherwise it was within noise. |
| Rear only | The rear holds better and the exit calms down. | The car starts to understeer if the nose is already at its limit. | ◐ Rear +0.20 m +2.7 %. |
| Front only | Small grip effect; the nose takes share from the rear. | The nose is heavier to turn. | ◐ Front +0.20 m +0.5 %. ◐ On another car a wide track cost front grip: −4 % in tight corners and +3 % in fast ones. |

The results differ between cars, so the offset gain is not certain on every car ◐.

## Centre of gravity height

**How the game calculates it:**

1. Centre of mass = body box floor + mass_up_percent × box height ●. "Center of Mass Height" in Part Setup is this percentage, not inches ●. The game shows it mass-weighted, because the engine and gearbox stay at the body's stock value ◐.
2. The centre of gravity changes with the body Stage, weight reduction (×0.99 / 0.97 / 0.95), body reinforcement (×1.007–1.015) and the weight reduction's own slider (step ×1.05) ●. Spring length raises the body and the centre of gravity 1 mm per mm ●.
3. Load transfer is directly proportional to the height h, both laterally (m · a · h / t) and longitudinally (m · a · h / L) ●. Lower is always better, but the range is small: the whole weight-reduction slider moves it about 2.8 cm, and the lap time did not stand out from noise ◐.
4. A tall car needs more roll stiffness for the same roll, a low car less. The "touge weapon (real CoG)" preset scales roll stiffness by the car's centre of gravity: a tall car gets about 30 % stiffer bars, low cars 17–21 % softer ◐ (not tested in game). The older touge weapon uses the same reference height for all cars, and the setups that worked in game were made with it.
5. Aero has no ride-height dependence ●, so a low body does not add downforce.

**When you lower the centre of gravity:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Weight reduction or slider down | Slightly less roll and load transfer. | No physics penalty. The slider also shifts weight distribution by ±1.6 points. | ◐ The whole slider range: lap within noise. |
| Spring length down | Lower centre of gravity and less transfer. | The suspension hits the bump stop, which costs far more than the centre of gravity gives. | ◐ +20 mm length = transfer +16 %, but grip in fast corners did not change. ● A slightly longer front spring has been more than two seconds quicker in game. |

So take the centre of gravity into account in the total bar stiffness, but do not chase it at the cost of travel.

## Mass and weight distribution

**How the game calculates it:**

1. The tyre loses friction coefficient as load grows, so a heavier car grips relatively less: about −2 % grip per 100 kg ●. Full Prototype weight reduction multiplies body mass by 0.805 ●, and the fuel tank adds 1–4 % to body mass ●.
2. The spring rate is the wheel rate directly, so a heavier car needs a stiffer spring for the same feel ●. Natural frequency f = √(k / m) / 2π, where m is the mass on one wheel ◐ calculated. The spring needed for the same frequency grows directly with wheel mass.
3. Suitable damping grows with √(k · m) ○. Touge moves dampers to another car by damping ratio ζ, so a heavier car automatically gets larger numbers ◐.
4. Weight distribution (front weight) splits the static load. The wheelbase relation (front share of roll stiffness − front weight) is relative to front weight, so a nose-heavy car needs a more front-biased bar split for the same balance ●. The weight-reduction slider moves the distribution by ±1.6 points ●.

**What it means:**

| Factor | What to expect | Experience |
| --- | --- | --- |
| Heavier car | Stiffer springs and larger dampers for the same feel, and slightly less grip. | ● A car about 25 % heavier has worked with springs about 35 % stiffer. |
| Front weight up | The rear calms down on throttle and the nose pushes more easily. | ◐ A nose-heavier car did not spin at full throttle in a tight corner where a 50/50 car did. ◐ More front weight was two seconds quicker with stock bars, no difference with a corrected bar split. |
| Lighter car | More grip relative to mass and shorter braking. | ● Formula −2 % per 100 kg. |

The weight distribution result shows that the bar split and the weight distribution do the same job. Once the split is right, a change in distribution no longer shows ◐.

## From dimensions to starting values

This is how to move a working setup to a new car using its dimensions. The touge weapon preset does steps 2–6 automatically, and setups made this way have worked in game ●.

1. **Note the car's data:** wheelbase, front and rear track, mass, front weight and Center of Mass Height (Part Setup).
2. **Springs from mass:** keep the same natural frequency as on the working car. A wheel about 30 % heavier needs a spring about 30 % stiffer ◐ calculated.
3. **Spring length from the car's default:** front ×1.07 and rear ×0.90, as in touge weapon ●.
4. **Bar split from wheelbase:** use the table in the Wheelbase section. The total stiffness comes from the roll you want, and a high centre of gravity needs more ◐.
5. **Track inside the fender:** offset as wide as the fender allows. On a rear-drive car widening the rear track helps more than the front ◐.
6. **Dampers by damping ratio:** the same ζ as on the working car, so the numbers grow with √(k · m) ◐.
7. **Gearing:** on a short car, try an about 10 % lower final drive (FD × 0.90) ◐.

After this, refine by symptom: bars first, then the diff, then springs and dampers.

## Symptoms

These symptoms come from a setup made for a car of different size. Correct them with bars, springs or the diff, because the dimensions can hardly be changed.

| Phase | Symptom | What happens in the game | Change |
| --- | --- | --- | --- |
| Braking into the corner | A long car understeers on the brakes and has to be forced to turn | A short car's rear-biased bar split does not rotate a long car | Move the bar split forward by wheelbase ●. |
| Mid-corner, high speed | Long car: the rear lets go suddenly in a big corner | The limit comes from the rear when the split is too rear-biased | Same fix: split forward ●. |
| Exit | A short car with a light rear spins on throttle | Low front weight and a short wheelbase make the rear sensitive | Lower diff preload and throttle lock ◐, or widen the rear track. |
| Braking | A short car dives and the rear goes light | Longitudinal transfer m · a · h / L is larger on a short car | Move brake balance rearwards and add front spring length. |
| Turn-in | A tall car rolls and is lazy | A high centre of gravity adds lateral transfer | Raise total bar stiffness with the same split. |
| Bumps and kerbs | A heavy car bottoms out and wallows | Springs and dampers are too soft for its mass | Springs by frequency, dampers in the same ratio. |

## Final tip

On a new car, look at the wheelbase first. It tells you how far to move the bar split of a working setup, and in our experience this alone cured a nervous rear and braking understeer on every car of the Touge weapon set ●. Mass tells you the level of springs and dampers, and the centre of gravity the total bar stiffness.

In our experience every 10 cm of extra wheelbase has moved the working roll-stiffness split about 4 points forward, up to about 5 points ahead of the front weight share ●.

## Not yet confirmed

- The wheelbase relation was fitted on three cars and tested in game on nine. Cars over 2.7 m have not been tried, so the upper end is an estimate.
- The frequency and damping ratio examples are calculated. Unsprung mass has not been subtracted from the wheel mass.
- The offset gain was positive on one car and negative on another, and the reason is open.
- The corrected centre of gravity calculation (touge weapon, real CoG) is untested in game.
- The link between a short wheelbase and longer gearing may come from the rev limiter.

---

← [Differential](differential.md) · [Contents](README.md) · [Glossary](glossary.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
