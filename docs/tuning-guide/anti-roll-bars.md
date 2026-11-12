[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/anti-roll-bars.md)

# Anti-roll bars

## In short

In this game the anti-roll bars are the biggest chassis lever, and the front/rear split matters more than the total stiffness. In our experience the split alone can move a lap by several seconds ◐, and moving the split towards the front has cured a nervous rear in game ●. A bar only works when the left and right wheels move differently: in roll and over one-sided bumps.

Markers: ● confirmed in game or in the game code, ◐ native simulation or inferred, not tested in game.

## Stiffness and roll

**How the game calculates it:**

1. The bar is a spring between the left and right wheel: F = k · (x_right − x_left) ●. When both wheels move the same amount (straight braking, acceleration, a flat bump), the bar does nothing.
2. Game value × 2000 = bar stiffness in N/m ●. One slider step doubles the value; the minimum is half of the stock value ●.
3. Axle roll stiffness = bar k·t² + spring pair k·t²/2, and the tyre's vertical stiffness is in series with these ● (t = track width). The same bar is stiffer on a wider track, by the square.
4. The roll centre is at ground level ●. Total load transfer in a corner is therefore always m · a · h / t, and the bars do not reduce it. They only decide how much the body rolls and which axle carries the transfer.
5. Roll changes camber through spring travel ●, but camber's effect on grip is small ◐.

**When you raise both by the same ratio (split stays):**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Both bars up | Less body roll and a quicker steering response. The limit hardly changes, because total transfer stays the same. | One-sided bumps and gutters throw the car; the inside wheel unloads and spins. | ● A very stiff rear bar makes the car sensitive to bumps. ◐ Both very soft was slower and unstable. |
| Both bars down | More roll, and the car calms down over bumps. | Transitions (S-bends) get lazy and the car wallows. | ◐ The native flat circle does not show bump sensitivity; the game decides. |

## Front/rear split

**How the game calculates it:**

1. The front axle's share of roll stiffness (LLTD) equals its share of the cornering load transfer ●. LLTD 0.40 = the nose carries 40 % of the transfer and the rear 60 %.
2. The axle that carries more transfer loses grip relative to the other: its inside wheel unloads, and the tyre's lateral stiffness does not grow at the same rate on the outside wheel ● formula, ◐ interpretation. A stiffer front moves the limit to the nose, a stiffer rear to the tail.
3. The split changes the car's whole limit: in the simulator the same car ran 1.08–1.64 g by the bar split alone ◐. Where the limit sits depends on the car and its centre of gravity.
4. In our experience a longer wheelbase wants a more front-biased split than a short car ●. A split that works on a short roadster does not carry over to a longer car as such.
5. In normal driving (0.8 g) the steering angle is the same with every split ◐. The split is felt near the limit and in the braking and throttle transitions.

**When you raise:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Front bar | The nose carries more transfer. The rear calms down in fast corners and the limit comes from the nose. On a long car, braking and trail-brake understeer also drop. | The nose pushes in steady corners and on throttle in fast corners. | ● Moving the split forward cured a nervous rear and braking understeer in game. ● A too-stiff front bar has cost almost two seconds. |
| Rear bar | The rear rotates the car: sharper turn-in and less throttle understeer. Faster on a short car. | The rear lets go "like a switch" in side load, a long car understeers on the brakes, and mid-corner throttle spins it. | ● A soft front and a stiff rear has been fastest on short cars. ◐ Softening a stiff rear bar a lot cost several seconds. |

The direction is the same as in a real car, but the limit is car-specific. Start from the car's wheelbase, not from a general "stiffer front" rule.

## Effect on other settings

Set the split first, then the total stiffness. Springs and track also change roll stiffness, so check the split after changing them.

| Setting | How it links to the bars in the game physics |
| --- | --- |
| Wheelbase | A longer car needs a more front-biased split ●. |
| Centre of gravity height | Load transfer is directly proportional to height ●, so the split matters more on a tall car. |
| Front weight | LLTD is compared with the front weight share. More front weight and a front-biased split move the same balance ◐. |
| Springs | The spring pair is part of roll stiffness, so a stiffer rear spring is also a stiffer rear ●. In our experience the bars cure balance better than the springs ◐. |
| Track and offset | Roll stiffness grows with the square of track width ●. A wider rear track takes more roll moment but changes wheel load less, and adds rear grip ◐. |
| Tyres | The tyre's vertical stiffness is in series with the bar ●. A soft or low-pressure tyre softens the axle slightly. |
| Differential | A stiff rear unloads the inside wheel, which spins, and the throttle lock engages earlier ◐. A stiff rear bar needs a throttle lock of at least about 0.3 ◐. |
| Dampers | The bar decides how much load moves, the slow dampers how fast. A soft front rebound reduces throttle understeer in the same direction as a soft front bar ◐. |

## Symptoms

First find the corner phase where the symptom appears. Change one bar at a time by about 10–15 % and drive the same corner in the same gear.

| Phase | Symptom | What happens in the game | Change |
| --- | --- | --- | --- |
| Braking into the corner | The car will not turn on the brakes; trail braking needs force | On a long car a rear-biased split puts the limit at the wrong end ◐ ● | Raise the front bar and lower the rear. |
| Turn-in | The rear steps out right at turn-in | The rear carries too much transfer | Lower the rear bar one step (10–15 %). |
| Mid-corner | The nose pushes in a steady corner | The nose carries too much transfer | Lower the front bar ●. |
| Mid-corner | In a fast corner the rear lets go "like a switch" | The limit comes from the rear ◐ | Raise the front bar or lower the rear. |
| Exit, full throttle | The nose pushes on throttle in a fast corner | The front is too stiff relative to the rear ◐ | Lower the front bar. If it is already low, soften the front rebound. |
| Exit, opening the throttle | The rear spins mid-corner on throttle | A stiff rear unloads the inside wheel and the diff locks | First lower diff preload and throttle lock ◐, then the rear bar. |
| Bumps, kerbs and gutters | A one-sided bump or gutter throws the rear | The bar passes one wheel's hit to the other | Lower the rear slow rebound, then the rear bar ◐. |

## Final tip

Find the split first and the total stiffness after it. Start from a split that suits the car's wheelbase and refine by symptom, one bar at a time. A short car tolerates a stiff rear and gets faster with it; a long car needs front ≥ rear.

A working bar setup is only valid with that car's own springs and tyres, because springs and track are part of the same roll stiffness. If you change springs, move the bars so the split stays.

**Simulation experience ◐ (native model, not tested in game):** a soft front and a stiff rear was fastest. Softening the rear bar from the stiff end cost 1–4 s, stiffening the front 0.7–1.2 s. Make a soft front with the bar, not the spring: a stiff front bar with a soft front spring was 1.7 s slower. Balance changes saturate: five changes in the same direction gave −2.3 s one by one but only −1.2 s together.

## Not yet confirmed

- Why a rear-biased split causes braking understeer on a long car is seen in the simulation, but the mechanism is open ◐.
- The bars' effect over bumps and gutters: the flat simulation circle does not show it, so the game decides.

---

← [Springs](springs.md) · [Contents](README.md) · [Dampers](dampers.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
