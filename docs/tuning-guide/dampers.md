[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/dampers.md)

# Dampers

## In short

In the native model the dampers are a small lever for lap time but a big one for feel. In our experience stock, current and maximum damping were within half a second of each other, while minimum damping made the car unstable or undrivable ◐. Springs and bars decide how much load finally moves, the dampers decide how fast. That is why dampers act in transitions (braking, turn-in, opening the throttle, bumps), not in the middle of a long corner.

The game's knee is high (0.1 m/s), so the slow values do almost all of the handling work and the fast values only bumps, kerbs and gutters.

Markers: ● confirmed in game or in the game code, ◐ native simulation or inferred, not tested in game, ○ real-car background.

## How the game calculates it

1. Damper force depends on the wheel's speed v, not its position. Below 0.1 m/s: F = slow · v. Above 0.1 m/s: F = slow · 0.1 + fast · (v − 0.1) ●. Fast is the slope of the curve after the knee, not a separate force.
2. Bump (compression) acts when the wheel rises towards the body. Rebound acts when the wheel drops away from the body ●.
3. The values act directly at the wheel; there is no motion ratio ●. The slider multiplies the value by 1.65 per step, ±3 steps ●. On one car the displayed number is 2 × the native coefficient, but this has not been checked on other cars ◐.
4. The knee is fixed at 0.1 m/s ●. Real dampers typically have their knee at 0.025–0.075 m/s ○, so in the game the slow range also covers much of the road's unevenness.
5. The roll centre is at ground level, so all lateral load transfer goes through springs, bars and dampers ●. The dampers' share in transitions is therefore probably larger than in a real car ◐.
6. The bump stop is rigid and not adjustable. Travel = spring length − sag ●, and the damper affects how close to the stop the suspension drifts over bumps.

**What each range handles:**

| Wheel speed | Driving event | Which value |
| --- | --- | --- |
| Below 0.1 m/s | Roll at turn-in (about 0.03 m/s ◐), dive under braking, squat on throttle, gentle waves | slow bump and slow rebound |
| Above 0.1 m/s | Bumps, kerbs, gutters, driving over the verge | fast bump and fast rebound (slow acts up to the knee) |
| Middle of a long corner | The motion has stopped | none: the dampers do nothing |

## Slow and fast bump

**What it does.** Bump slows the wheel rising towards the body. As long as the motion continues, it adds load to that corner's tyre ● (force from speed). The axle with stiffer compression takes a larger share of the load transfer in transitions and briefly loses grip relative to the other ○.

- **Front slow bump** acts under braking and at turn-in, when the nose dives and the outer front wheel compresses.
- **Rear slow bump** acts when opening the throttle and on exit, when the rear squats.
- **Fast bump** acts only when the wheel hits a bump, kerb or gutter.

**Ratio.** When fast is lower than slow, the curve flattens after the knee (digressive), as in racing dampers ○. The game also allows fast > slow (progressive) ●. In setups that have worked in game, fast bump is about 0.6–0.7 × slow bump ●.

**When you raise:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Front slow bump | The nose dives more slowly under braking and the car is calmer at turn-in. | Understeer on corner entry; the nose does not take load. | ○ Sources agree on the direction. ● A 10 % change was within noise in game. |
| Rear slow bump | The rear squats more slowly on throttle. | On exit the rear goes light for a moment: oversteer and weaker traction ○. | ◐ Both ×0.7 and ×1.3 were slower than the stock value. |
| Fast bump | The body is supported over bumps and does not sink as deep. | A bump or kerb throws the car up and the tyre leaves the road for a moment. | ● Fast bump ×1.5 felt very good in game. ◐ Native effect only −0.05 s. |
| All bump down | The wheel follows the road and soaks up bumps. | The body sinks fast and hits the bump stop. | ◐ Bump at minimum was about two seconds slower. |

## Slow and fast rebound

**What it does.** Rebound slows the wheel dropping away from the body, so it holds the body down ●. It affects the neighbouring and diagonal corners more than its own ○.

- **Front slow rebound** acts when opening the throttle, as the nose rises, and on the inner front wheel at turn-in.
- **Rear slow rebound** acts under braking, as the rear rises, and on the inner rear wheel at turn-in.
- **Fast rebound** decides how fast the wheel returns to the road after a bump or kerb.

**Ratio.** In setups that have worked in game, slow rebound is about 3.6 × slow bump at the front and 4.5 × at the rear ●. Fast rebound is about half of slow rebound at the front and a third at the rear ●. Real cars often use rebound 2–3 × bump ○. When rebound grows far above bump, the suspension packs down towards the bump stop over a series of bumps: the wheel drops in fast but returns slowly ◐. In our experience halving a very high rebound cut the time on the bump stop by almost half ◐.

**When you raise:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Front slow rebound | The nose rises more slowly on throttle and stays loaded, so throttle understeer drops. | The car feels hard and packs down; the inner front goes light at turn-in. | ● Halving front rebound made the car more predictable, but brought slight throttle understeer in fast corners. ◐ The native model showed the opposite direction (conflict). |
| Rear slow rebound | The rear rises more slowly under braking and helps rotate the car at turn-in. | The inner rear goes light; the rear bounces and steps out over bumps. | ◐ Lowering it about 25 % has calmed a bouncing rear. ● +20 % on the rear dampers felt good in game. |
| Fast rebound | The body stays calm after bumps. | The wheel does not return to the road in time and grip breaks over a series of bumps. | ◐ Fast rebound ×0.6 was 0.14–0.18 s slower, so too low was slower. |
| All rebound down | The wheels return quickly and the car does not pack down. | The body wallows and pitches. | ◐ All rebound at minimum: the car did not finish the native run. |

## Working together: how to set them

**Which damper moves in each phase** (flat road ○, same mechanics in the game ●):

| Phase | Front | Rear | Dominant pair |
| --- | --- | --- | --- |
| Straight braking | bump | rebound | front bump + rear rebound |
| Braking into the corner (trail brake) | outer bump, inner rebound | outer bump, inner rebound | outer front bump + inner rear rebound |
| Turn-in, off the brakes | outer bump, inner rebound | outer bump, inner rebound | inner front rebound + outer rear bump |
| Mid-corner | — | — | no effect |
| Exit, throttle | rebound | bump | front rebound + rear bump |
| Bump, kerb, gutter | fast bump, then fast rebound | same | the wheel that hits |

**Setup order:**

1. Springs and bars first. They decide where the load transfer settles; the dampers only how fast.
2. Level: change all four by the same factor (one slider step = ×1.65). In the native model stock to maximum was within noise, but minimum was too little ◐.
3. Bump/rebound ratio: if the car feels hard and hits the bump stop over bumps, rebound is too high relative to bump.
4. Front/rear: correct the transition balance by symptom (below).
5. Fast values last, for bumps and gutters.

**Things to keep in mind:**

- In roll the outer wheel compresses and the inner wheel extends at the same speed. The axle's transient load transfer is then about (bump + rebound) / 2 × speed, and if rebound is larger, the difference (rebound − bump) × speed pulls the body down ◐ derived.
- When you stiffen a spring but not the dampers, the suspension becomes relatively less damped, because critical damping grows with the square root of the spring ○ (same formula in the game). Raise damping by roughly √(new spring / old spring).
- The ratios above (rebound 3.6–4.5 × bump, fast about 0.6 × slow) come from a preset that has worked in game on several cars. They are a starting point, not a searched-out value ◐.
- Real-car rules of thumb, such as a damping ratio of 0.5–0.7, are background only ○. Front rebound that works in game is still clearly above them.

## Effect on other settings

| Setting | How it links to the dampers in the game physics |
| --- | --- |
| Springs | Suitable damping depends on the spring (critical damping ∝ √(spring · mass)). A soft spring with firm slow damping gives quick support in transitions and a soft feel over bumps ○. |
| Spring length | Travel = length − sag ●. Too much rebound packs the car onto the bump stop, and a short spring brings the stop even closer. In our experience a longer spring cut bump-stop time by three quarters, halving rebound by almost half ◐. |
| Bars | A bar has no damping of its own ●. A stiffer bar on the same dampers makes roll relatively less damped ○. |
| Differential | Opening the throttle squats the rear (rear bump) while the diff locks. Rear slow bump and throttle lock both act on the rear on exit, so change only one at a time ◐. |
| Camber | Camber changes with spring travel ●, and the damper slows that change. The effect is small, because camber's grip effect is small ◐. |
| Tyres | The tyre's vertical compliance is in series with the suspension; no tyre damping of its own has been found in the native code ◐. |
| Bumps and gutters | The asphalt bump pattern is −0.0035…0 m (repeat 20 m) and ±0.025 m (repeat 200 m) ●. Gutters and driving over the verge are the main events in the fast range on a line that uses them. |

## Symptoms

Change one value at a time by about 15–20 % (half a slider step) and drive the same corner. Damper symptoms come in transitions: if the symptom is in the steady middle of a corner, look at springs and bars first.

| Phase | Symptom | What happens in the game | Change |
| --- | --- | --- | --- |
| Braking into the corner | The nose dives quickly and the rear goes light | The front drops and the rear rises too fast | Raise front slow bump and rear slow rebound. |
| Braking into the corner | The car will not turn while trail braking | The outer front takes too much load in the transition | Lower front slow bump ○. |
| Turn-in | The rear steps out right at turn-in | The inner rear goes light; the rear takes too much in the transition | Lower rear slow rebound ◐. |
| Exit, opening the throttle | The nose pushes on throttle in fast corners | The nose rises quickly and loses load | Raise front slow rebound ●. |
| Exit, opening the throttle | The rear goes light and steps out as the throttle comes in | The rear compresses slowly while the diff locks | Lower rear slow bump, or first the diff preload. |
| Bumps and gutters | The car feels hard and bounces over a series of bumps | Rebound does not let the wheel back; the suspension packs onto the bump stop | Lower slow rebound ● or lengthen the spring. |
| Bumps and gutters | A gutter or kerb throws the car into the air | Fast bump too high | Lower fast bump. |
| Bumps and gutters | The car wallows and pitches after a bump | Fast rebound too low | Raise fast rebound. |

## Final tip

Keep the dampers near stock or the touge weapon preset first: in the native model stock and maximum differed little, but too little damping ruined the car. Then refine one phase at a time: rebound for packing over bumps, front slow rebound for throttle understeer, and fast values for gutters. If the car feels hard, look at the bump/rebound ratio and the spring length before the spring.

In our experience rebound is clearly larger than bump in every working setup, and relatively larger at the rear than at the front. A heavier car uses larger numbers with the same ratios.

## Not yet confirmed

- The direction of front slow rebound on throttle is in conflict: the game and the literature say less rebound adds throttle understeer, the native model showed the opposite ◐. This guide follows the game.
- The ratio between the displayed number and the native coefficient (2 × on one car) is unchecked on other cars, so the guide does not compute damping ratios.
- Bumps, gutters and verges have not been run in the native model, so the fast-value advice rests on one game test and general mechanics.
- The phase table directions come from real-car sources (○). The game's damper formula is the same, but not every direction has been run in the native model.

---

← [Anti-roll bars](anti-roll-bars.md) · [Contents](README.md) · [Camber and toe](camber-and-toe.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
