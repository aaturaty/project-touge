[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/springs.md)

# Springs

## In short

The biggest spring lever is length, because in this game it is the ride height. In our experience a few millimetres more front spring length has been worth seconds on a twisty road ●. Stiffness is a medium lever: clearly softer or stiffer than the car likes costs 2–4 s ◐. The front/rear ratio matters less than the bar split.

The game's springs have two special features compared with a real car. The spring rate is the wheel rate directly, with no motion ratio, and a stiffer spring lifts the body, because the length is the spring's free length.

Markers: ● confirmed in game or in the game code, ◐ native simulation or inferred, not tested in game.

## Length

**How the game calculates it:**

1. Spring Length is the spring's free length in millimetres ●. At rest the spring is compressed by the load: sag = wheel load / spring rate ●.
2. The spring's top mount sits at the wheel, not at the length. The body and the centre of gravity therefore rise exactly 1 mm for every millimetre of length ●. In the game, length is a ride-height adjustment.
3. Length also sets the travel: the suspension hits the bump stop when the wheel load exceeds static + k · (length − sag) ●. On a bumpy road the front load can briefly reach about 3.6 × static, so travel without bottoming is about 3.6 × sag ◐.
4. Camber changes with length: camber = setting − 3° + 8° · length / stroke ●. A longer spring makes the resting camber more upright, but camber's grip effect is small ◐.
5. On a flat circle, ride height 70–120 mm did not change grip ◐. The difference comes from bumps, kerbs and whether the suspension hits the bump stop.

**When you raise:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Front length | The nose gets travel: less bottoming and less throttle understeer in fast corners. | A high nose and centre of gravity, more roll and lazier transitions. | ● +4 on the front was worth over two seconds on a twisty road; the next +4 was even. ◐ Lowering both ends by 15 cost about 1 s. |
| Rear length | The rear gets travel and calms down over bumps. | A high rear moves weight forward under braking and makes the rear light. | ◐ A large rear length change was within noise on the lap. |
| Length down (both) | A lower centre of gravity and less load transfer. | The suspension hits the bump stop and the car feels stiff. | ◐ More travel cut bump-stop time by three quarters. The game's own tuning help warns about losing control on bumpy roads with too short springs. |

## Stiffness

**How the game calculates it:**

1. Spring force F = k · (length − current length) goes straight to the wheel ●. Game value × 1000 = wheel rate in N/m, with no motion ratio ●. Spring rates of different cars can therefore be compared directly against mass.
2. A stiffer spring sags less, so with the same length the body rises ●. When you stiffen, shorten the length by the same amount if you want to keep the height.
3. Springs do not change total load transfer (m · a · h / t sideways, m · a · h / L lengthways), because the roll centre is at ground level ●. They decide how much the body moves and how well the wheel follows bumps.
4. In roll the spring pair gives k · t² / 2 and a bar k · t² ●. The same number in a bar stiffens roll twice as much as in a spring.
5. Natural frequency f = √(k / m) / 2π, where m is the mass per wheel ◐. Frequency is the easiest way to carry a working stiffness over to another car.
6. Helper is a progressive helper spring, not a driving aid ●. The slider limits come from the suspension part, and the game can limit more than the data says ●.

**When you raise:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Both springs up | Less body movement, a sharper response, and the body rises (see point 2). | The wheels do not follow bumps, and the car bounces on kerbs and gutters. Very stiff combinations were unstable in the simulation. | ◐ Clearly stiffer than the car likes cost about 2 s. ● A moderately stiffer spring gave "attack and grip into corners" in game. |
| Both springs down | The wheels follow the road and the car calms down over bumps. | The body sinks and hits the bump stop; roll and pitch grow. | ◐ A much softer spring cost up to 4 s. |

## Front/rear ratio

**How the game calculates it:**

1. The spring pair is part of axle roll stiffness (k · t² / 2), so the spring ratio moves the load-transfer split in the same direction as the bars ●. A stiffer front spring moves the limit to the nose, a stiffer rear spring to the tail.
2. The effect is smaller than with the bars, because the spring pair counts half of the same number in a bar ●. In our experience changing springs did not cure a nervous rear; the bars did ◐.
3. Under braking and acceleration the longitudinal transfer m · a · h / L is the same whatever the springs ●. The spring ratio decides how much the nose dives and the rear lifts, and with that the travel and camber.
4. Frequency describes the ratio better than the plain number: a front-heavy car needs a stiffer front spring for the same frequency ◐.

**When you raise:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Front spring (rear unchanged) | The nose dives less under braking and turn-in gets slightly sharper. | Throttle understeer in fast corners, and the nose bounces over bumps. | ◐ A small effect on the lap; softer front reduced throttle understeer. |
| Rear spring (front unchanged) | The rear rotates the car and throttle understeer drops. | The rear gets light, the inside wheel spins and the rear bounces over bumps. | ● A softer rear spring together with bar and diff changes was over a second faster in game. ◐ Clearly softer rear was slower. |

Fix the balance with the bars first. Change the spring ratio only when the symptom is about bumps or about pitch under braking and throttle.

## Effect on other settings

Order: length first (travel and height), then stiffness, and balance with the bars. Every spring change also moves the ride height, so check the length after a stiffness change.

| Setting | How it links to the springs in the game physics |
| --- | --- |
| Anti-roll bars | Springs and bars form the roll stiffness together ●. If you change springs, move the bars so the split stays. |
| Dampers | The right damping level depends on the spring. Too much rebound packs the suspension down onto the bump stop ◐. When you stiffen the spring, raise damping in roughly the same ratio. |
| Centre of gravity | Length raises the centre of gravity 1 mm per mm ●. More height adds load transfer, but on a flat circle grip did not change ◐. |
| Camber | Camber depends on spring length ●. On a rigid-axle car camber has no effect ●. |
| Tyre profile | Profile raises the body ●. A bigger tyre needs a shorter spring for the same height. |
| Differential | A soft or high rear rolls and unloads the inside wheel, so the throttle lock engages earlier ◐. |
| Bumps and gutters | Road bumps are small and frequent plus larger and long ●. A too stiff or too short spring cannot follow them, which shows as bouncing on kerbs. |

## Symptoms

Change one thing at a time: length by 4, stiffness by about 10 %. Drive the same corner in the same gear.

| Phase | Symptom | What happens in the game | Change |
| --- | --- | --- | --- |
| Braking into the corner | The nose dives and the car feels hard or pushes at the end of braking | The front suspension hits the bump stop when travel runs out | Lengthen the front by 4. If the nose still dives a lot, raise the front spring about 10 %. |
| Turn-in | The car is lazy to turn and rolls a lot | The body moves more than the tyre can follow | Raise the springs about 10 % or shorten the length if there is travel to spare. |
| Mid-corner | The car is nervous and bounces over bumps in the corner | Too stiff a spring; the wheel leaves the road | Lower the spring about 10 % and keep the height with length. |
| Exit, full throttle | The nose pushes on throttle in a fast corner | The nose rises and unloads; the front suspension does not move | Lengthen the front ● or soften the front spring ◐. |
| Exit, opening the throttle | The rear squats and the inside wheel spins | A soft or short rear sinks, and roll unloads the inside wheel | Raise the rear spring about 10 % or the rear length by 4. |
| Bumps, kerbs and gutters | The car bounces or is thrown over the verge | The suspension bottoms or the spring is too stiff to follow | Lengthen first. If the car still bounces, lower the spring. |

## Final tip

Start with length: give the suspension enough travel not to hit the bump stop, and still keep the body low. Then change stiffness and correct the height with length. A slightly longer front and slightly shorter rear than stock has worked in game on several cars ●.

The spring value is the wheel rate, so a heavier car needs a stiffer spring for the same feel.

**Simulation experience ◐ (native model, not tested in game):** lower was slower: both lengths −15 cost about 1 s, and +15 on the front gained about 0.5 s, the same direction as in game. A stiffer rear spring gained a little and a softer one lost almost a second. A soft front spring with a stiff front bar was a poor combination (+1.7 s).

## Not yet confirmed

- The flat simulation circle does not show bumps and gutters, which is exactly where spring and length are felt most. The game decides.
- Frequency and sag figures are calculated, not measured.

---

← [Tyres](tyres.md) · [Contents](README.md) · [Anti-roll bars](anti-roll-bars.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
