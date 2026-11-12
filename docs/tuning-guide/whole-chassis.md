[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/whole-chassis.md)

# The chassis as a whole

## In short

This guide pulls the topic guides together into one way of working. In this game the biggest levers are the bar split, spring length, tyre size and the diff's throttle lock: in our experience each has been worth seconds on a long touge run. Dampers, camber, toe and centre of gravity are finishing touches whose effect on time is often below the noise, but they change the feel.

Work from big to small, one change at a time, and solve a symptom with the lever that acts most on that phase. When two options are within about half a second, keep the one that feels easier to control.

Markers: ● confirmed in game or in the game code, ◐ native simulation or inferred, not tested in game, ○ real-car theory.

Topic guides: [Anti-roll bars](anti-roll-bars.md) · [Springs](springs.md) · [Tyres](tyres.md) · [Dampers](dampers.md) · [Camber and toe](camber-and-toe.md) · [Body dimensions](body-dimensions.md) · [Differential](differential.md)

## The biggest levers

Lever size is the largest difference measured on a long touge run, in the native model or with the in-game timer. The figures come from different cars and starting points, so they show an order of magnitude, not a promise.

| Setting | Lever size | Experience | Acts most on |
| --- | --- | --- | --- |
| Bar split | Large | ◐ Up to about five seconds. ● Moving the split forward cured braking understeer and a nervous rear on a long car in game. | Balance through the whole corner |
| Diff throttle lock | Large at the bottom, then flat | ◐ 0 clearly slowest and an open diff far slower. Above that the results conflict (see Not yet confirmed). ● 0.24–0.30 has worked in game. | Exit |
| Spring length | Large | ● A few millimetres more front length has been more than two seconds quicker in game. | Travel, bumps, throttle understeer |
| Tyre size | Large | ◐ 285–325 mm vs 265 mm about two seconds. | Grip and gearing length |
| Final drive | Medium | ◐ Short cars gained up to almost two seconds with a 5–10 % change. | Acceleration out of corners |
| Spring rate | Medium | ◐ The extremes were 2–4 s slower than the middle of the range. | Body motion and bumps |
| Brake balance | Medium | ◐ 40 % front was 0.5–0.7 s quicker on most cars. ● A front-biased balance has made corner entry safe in game. | Braking and turn-in |
| Dampers | Small for time, large for feel | ◐ Nearly neutral in the native model. ● +20 % on the rear dampers has felt very good in game. | Speed of transitions |
| Track and offset | Small | ◐ +0.10 m on both axles +1.4 % grip; on a full run often within noise. | Cornering grip |
| Camber and toe | Small | ◐ Camber ≤ 3.5 % lateral grip, toe under a second. | Finishing |
| Centre of gravity, caster, Ackermann | Not measurable | ◐ Lap within noise. | – |

## Setup order

The order goes from big to small, so that a later setting does not undo an earlier one. If you go back to an earlier step, check the steps after it again.

1. **Tyres and body:** tyre size, rim part and offset inside the fender. The tyre sets grip and radius, so it is the base for everything else.
2. **Gearing:** only after the tyre, because only the total ratio (FD × tyre radius) matters ●.
3. **Spring length:** enough travel that the suspension does not hit the bump stop (touge weapon: front ×1.07, rear ×0.90 of the default).
4. **Springs:** rate by mass, then length again, because a stiffer spring raises the body ●.
5. **Bars:** split by wheelbase and total stiffness by roll. This is the main balance setting.
6. **Differential:** throttle lock first, then preload and decel lock for exit and entry.
7. **Brake balance:** rotation and stability on entry.
8. **Dampers:** slow bump and slow rebound for the speed of transitions. Fast values only for bumps and gutters.
9. **Camber and toe:** finishing.

The touge weapon preset in Touge gives starting values for steps 2–8 from the car's dimensions, and they have worked in game ●. The real refining then starts from symptoms.

## How to test

1. **One change at a time.** When you change two things you do not know which one made the difference. The exception is a pair that belongs together, such as a spring and its length for the same height.
2. **A big enough step.** One slider step splits into 20 ticks for gearing, springs, dampers, camber, toe and diff locks ●, so a gear ratio can be set to 0.4 %. The ratio the game shows is the physics ratio ●. A small step still disappears into noise. Useful steps: bar about 10 % of total stiffness or 2–4 points of split, spring length 4 mm, spring about 10 %, damper about 20 %, diff 0.05, brake balance 2 points, camber 0.5° and toe 0.1°.
3. **The same test spot.** Drive the same corner or section in the same gear. The full lap tells you the result, a single corner tells you what the change did.
4. **Know the noise.** In our experience runs of the same setup spread by about 0.8 s on a six-minute run ●. A difference under a second cannot be shown with one run.
5. **Note the feel as well as the time.** Write down what the car did under braking, at turn-in, mid-corner and on exit, not only the time. The Symptom view on Touge's Tune tab uses the same four phases.
6. **The whole lap decides.** A change is better only if it shortens the lap or makes the car clearly easier to control. Improving one measure, such as steady-circle grip, can slow the lap: rear toe-in raised circle grip 2–4 % but the lap got slower ◐.

**On a controller the steering assist is always on ●.** The steering assist's Off level does not give direct steering on a controller or keyboard. The game still uses the assist, with its tightest front slip limit (105 %). Direct steering is only available on a wheel. On a controller the Off/Gamepad profile is used, which has no extra keyboard stabilisation. In a native test the assist changed grip only a little (−1.2 % in a tight corner, 0 in a fast one) ◐, so it does not explain differences between the native model and the game. It may still affect the feel, because it keeps the front tyres near peak grip ◐.

## From symptom to setting

This index collects the symptom tables of the topic guides. Try the primary change first and only then the secondary one. The topic guides have more detail.

| Phase | Symptom | Primary change | Secondary |
| --- | --- | --- | --- |
| Braking into the corner | The car understeers on the brakes and has to be forced to turn | Move the bar split forward ● | Brake balance 2 points rearwards |
| Braking into the corner | The rear wanders or tries to overtake | Brake balance 2 points forward ● | Diff decel lock up, rear toe +0.1 |
| Braking into the corner | The nose dives and bottoms out | Front spring length +4 mm | Front spring or front slow bump up |
| Turn-in | The car is lazy to turn | Front bar down or rear bar up | Front slow bump down, front camber −0.5° |
| Turn-in | The rear steps out right at turn-in | Rear bar down | Rear slow rebound down, brake balance forward |
| Mid-corner | Steady understeer in a long corner | Move the bar split rearwards | Tyre size or front track |
| Mid-corner, high speed | The rear lets go suddenly | Move the bar split forward by wheelbase ● | Wider rear track |
| Exit | The nose pushes on throttle in a fast corner | More front spring length ● | Front spring down ◐ |
| Exit | The rear spins on throttle | Diff preload and throttle lock down (careful below 0.2) | Rear bar down |
| Exit | The inner wheel spins | Throttle lock up | Rear spring or rear length up, rear camber towards zero |
| Straight | The limiter comes before the braking point, or the car does not accelerate | Final drive | Tyre size (radius changes the gearing) |
| Bumps, kerbs and gutters | The car bounces or is thrown over the verge | More spring length | Fast bump down, spring down |
| Bumps, kerbs and gutters | The car keeps wallowing after a bump | Slow rebound up | Fast rebound up |

If the same symptom shows in several phases, the cause is usually the bar split or the diff, not a single damper.

## Finding your own feel

The fastest setup is not the same for everyone, because the driver drives it at the limit. First find a balance where the car does not surprise you, then tune the feel to your own style. When two options are within about 0.5 s, keep the one that is easier to control: with fewer mistakes it is quicker at the limit.

**Feel adjusters:**

| You want | Change | Cost |
| --- | --- | --- |
| More rotation on the brakes | Brake balance rearwards, diff decel lock down | The rear may step out under braking. |
| A more stable entry | Brake balance forward, decel lock up | The car understeers on the brakes. |
| A sharper response | Slow dampers up, bars stiffer with the same split | The car is more nervous over bumps. |
| Softer and more predictable | Slow dampers and springs down, more travel | Transitions get lazier. |
| An exit where the rear helps turn | Throttle lock and preload up | The rear steps out more easily on throttle. |
| A straight exit | Preload down, bar split forward | The car pushes more on throttle. |

**If you brake deep into the corner, use on/off throttle and drive over verges and gutters:** brake balance becomes the main rotation adjuster, and a low diff decel lock keeps it from fighting the rotation on the brakes ●. Stability then comes from the bar split rather than the diff. Leave travel in the suspension for verges and gutters and keep fast damping moderate. With on/off throttle, a moderate preload and throttle lock slow the growth of a slide ◐.

## Final tip

Start a new car from the touge weapon preset, which has worked in game on ten cars ●. Drive a few laps and note the phase where the car does not do what you want. Fix one symptom at a time with the index's primary change, and once the car is balanced, move on to the feel.

Three things have repeated in every test:

1. **The bar split comes before anything else.** In our experience one split correction fixed the problems of nine cars at once.
2. **Travel comes before a low body.** More spring length has made the car seconds quicker even though the centre of gravity rose.
3. **The throttle lock should not be too low.** In the native model 0 was clearly slowest, and 0.24–0.30 has worked in game. Above that the difference is mostly feel.

**Simulation experience ◐ (native model, not tested in game):** the build mattered most, then balance, and the diff last. Downforce, mass and tyre size moved the lap by 2–18 s, while chassis settings from a sensible start stayed under a second (the exception was a very soft rear bar, 3.7 s slower). More downforce on both axles was 2.8 s quicker; more only at the rear was 1.4 s slower (understeer in medium corners) and more only at the front 0.6 s quicker. 50 kg less mass was 2.1 s quicker. Balance changes saturate and do not add up. A final drive range of about 15 % stayed within 0.3 s.

## Not yet confirmed

- The lever sizes come from different cars, different starting setups and partly the native model. They give the order, not how much your car will gain.
- The lower limit of the throttle lock conflicts: one model found below 0.25 slow, a hairpin test did not, another test found 0.10 slow, and a newer slide-capable driver saw 0.10–1.0 as noise over a lap with 0.15 quickest in the tightest hairpin. The 0.24–0.30 range that has worked in game is the safe area.
- Damper effect on time is small in the native model but large on feel. The native model does not model driver confidence.
- The feel adjusters are derived from the topic guides and real-car theory. They have not been tested together as a whole.
- The 0.8 s run-to-run spread is from one series on one car and track. It may differ elsewhere.

---

← [Introduction](README.md) · [Contents](README.md) · [Tyres](tyres.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
