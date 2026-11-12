[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/differential.md)

# Differential: throttle lock, decel lock and preload

## What each setting does

This guide is based on the game's own differential code and on native simulation runs. Real-diff theory is used only where the game works the same way.

**How the game's clutch diff calculates it:**

1. The driveline torque T is first split evenly, T/2 to each driven wheel ●.
2. The lock then moves torque from the faster-spinning wheel to the slower one, up to the lock torque T_lock ●.
3. On throttle T_lock = preload + throttle lock × T. On engine braking T_lock = preload + decel lock × |T| ●.
4. The wheel torque difference can be 2 × T_lock, so the largest split is (1 + 2L) : (1 − 2L). Lock 0.25 = 3 : 1, 0.30 = 4 : 1, and 0.50 or more = all torque can go to one wheel ●.
5. T is the driveline torque. The pedal brakes do not pass through the diff, and with the clutch pressed no torque is transmitted. Then the only lock is the preload ●.

| Setting | What it is in the game | Where it acts | What it does |
| --- | --- | --- | --- |
| Throttle lock (Lock on acceleration) | Share of engine torque that locks the wheels | On throttle, most on exit | When the inner wheel starts to spin, torque moves to the outer wheel. More traction and the rear pushes. Too much: the rear steps out at full throttle. |
| Decel lock (Lock on deceleration) | Share of engine-braking torque that locks the wheels | Off throttle, corner entry | The outer wheel brakes more, so the car stabilises. More = more stable but lazier to turn. |
| Preload | Constant lock in newton-metres (Ultimate 0–520) | Always, also with the clutch pressed | Does not grow with torque. So it dominates when there is little torque: light throttle, the first opening of the throttle, engine braking and shifting. |

**The diff part sets the range ●:**

| Diff part | Throttle lock | Decel lock | Preload | Resolution (lock / preload) |
| --- | --- | --- | --- | --- |
| Ultimate (tier 5) | 0–1.0 | 0–1.0 | 0–520 | 0.005 / 3.25 Nm |
| Prototype (tier 6) | 0.6–1.6 | 0.3–1.3 | 0–100 | 0.0125 / 1.25 Nm |

With the Prototype diff the throttle lock is always at least 0.6, and in the native code a lock of 0.5 or more is a full lock. The throttle side is therefore always fully locked. An adjustable throttle lock (for example 0.24–0.30) needs the Ultimate diff.

**Order of magnitude (◐, assumed engine torque 250 Nm):** in 2nd gear the axle torque is about 250 × 2.00 × 4.00 = 2000 Nm. Throttle lock 0.3 gives about 600 Nm of lock at full throttle, and preload 100 is only 1/6 of that. Engine-braking torque is much smaller, so decel lock 0.15 gives only tens of newton-metres. Then preload 100 can be larger than the whole decel lock.

**When you raise:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Throttle lock | On exit the inner wheel spins less, the car pulls better, and the rear starts to push. | The rear steps out at full throttle in a tight hairpin. | ◐ In a tight hairpin 0.15 was about 0.4 s quicker than 0.25, and 0.40 spun. Over a full lap 0.10–1.0 was within noise and 0 clearly slowest. ● Values around 0.25–0.30 have worked in game on several cars. |
| Decel lock | Corner entry stabilises, and the rear calms down under braking and on downshifts. | The nose pushes off throttle, and the lock fights rotation on the brakes. | ◐ In a tight hairpin 0–0.8 differed by under 0.1 s; only the rear wheel speed difference changed. ● In our experience a low value suits a style that rotates the car on the brakes. |
| Preload | Transitions smooth out: the inner wheel spins less and the rear calms down with the clutch pressed. | The rear jerks as the throttle opens, and the car understeers on light throttle. A tight hairpin spun at 150 or more. | ◐ 0–520 was within noise over a lap; the rear wheel speed difference dropped from 0.58 to 0.27. ◐ Lowering preload and lock slowed the growth of a slide (55 → 42–44 °/s). ● Preload 0 has also felt good in game. |

## Setup order and what else matters

Set the throttle lock first, the decel lock second and the preload last. Each has its own phase, and the preload refines the transitions between them.

1. **Throttle lock** decides the exit. In the native model 0 is clearly slowest; in a tight hairpin lower values (about 0.15) were quicker, in a medium corner about 0.25. Over a lap 0.10–1.0 is within noise.
2. **Decel lock** decides the entry. In a tight hairpin 0–0.8 differed by under 0.1 s. Corner angle and rotation stayed the same; only the rear wheel speed difference changed. When pumping the brakes, the lock calms the rear.
3. **Preload** refines the transitions. In the native model 0–520 was within noise for time, but the rear wheel speed difference on throttle dropped from 0.58 to 0.27. Inner-wheel spin fell from about 45 % to 23 %. In a tight hairpin 150 or more spun at full throttle.

**What else affects how the diff feels:**

| Setting | How it links to the diff in the game physics |
| --- | --- |
| Gear ratio and gear | The lock is a share of axle torque. A low gear multiplies torque, so the same throttle lock locks much more in 2nd than in 4th. Tight hairpins are driven in a low gear, so that is where the lock is felt most. Preload does not change with gear. |
| Throttle technique | With on/off throttle the torque jumps straight to full, so the throttle lock decides the behaviour and the preload shows only at the start of the opening. On part throttle the preload weighs more. |
| Clutch and shifting | With the clutch pressed T is zero, so the only lock is the preload. On clutch shifts and downshifts under braking the preload is the only lock. |
| Brake balance | The brakes do not pass through the diff, but a rear-biased balance slows the rear wheels. In the native model front 40 gave 10–15 % more rotation and 1–2° more entry angle than 60. A rear-biased brake and a low decel lock rotate the car most together. |
| ABS | ABS limits rear wheel locking, so extreme brake balances did not change lap time in the native model. |
| Rear bar and rear springs | A stiff rear unloads the inner wheel, so it spins more easily and the throttle lock engages earlier. A softer rear needs less lock. |
| Engine torque | More torque = more throttle lock in newton-metres at the same setting. Preload is fixed, so on a powerful car its relative share shrinks. |

## Symptoms

First find the phase where the symptom appears. The phase tells you which lock is active. Change one setting at a time: throttle and decel lock by 0.05, preload by about 50.

| Phase | Symptom | What happens in the game | Change |
| --- | --- | --- | --- |
| Corner entry, off throttle | The nose pushes and the car will not turn | The outer wheel spins faster and the lock brakes it, making a straightening moment | Lower decel lock. If it is already low, lower preload. |
| Corner entry, off throttle | The rear moves or kicks under braking and on downshifts | The rear wheels turn at different rates and the lock does not even them out | Raise decel lock or preload. Move brake balance forward. |
| Clutch pressed (shift, braking) | The rear is restless only with the clutch pressed | The only lock is the preload | Raise preload. |
| Mid-corner, light throttle | The car understeers and wants to go straight | The outer wheel is faster, so the lock moves torque to the inner wheel. Here the lock is mostly preload. | Lower preload. |
| Opening the throttle | The inner wheel spins, revs rise but the car does not pull | Not enough lock to move torque to the outer wheel | Raise preload (start of the opening) or throttle lock (full throttle). |
| Opening the throttle | The rear jerks as soon as the throttle comes in | Preload ties the wheels together before torque rises | Lower preload. |
| Exit, full throttle | The rear steps out and the car spins in a tight hairpin | The lock sends almost all torque to the outer wheel | Lower throttle lock or preload. |
| Exit, full throttle | The car does not pull out and the inner wheel spins in a wider corner | The lock does not even out the wheels in time | Raise throttle lock by 0.05. |

## Final tip

In the native model the diff settings hardly changed lap time; only a throttle lock of 0 was clearly slow. Choose the values by what is easiest to control. A steady drift was slower than grip in the native model (−15 % in a tight corner, −6 % in a medium one), but about 20° of slide on exit at full throttle was quickest.

- Always test in the same corner in the same gear, because the gear sets the lock force.
- If the car spins at full throttle, look at the throttle lock first and then the preload. Both push the rear out.
- In our experience a throttle lock of 0.25–0.30, a decel lock of 0.12–0.20 and a preload of 45–100 has been an easy-to-drive starting range in game ●. Touge's diff presets cover this range and the softer and stiffer ones around it.

**Simulation experience ◐ (native model, not tested in game):** once the throttle lock is above 0, the locks and preload are feel settings: throttle lock 0.15–1.0, decel lock 0–0.5 and preload 0–250 all stayed within 0.4 s. An open diff (throttle lock 0) was 2.4 s slower, mostly in slow corners. The exception is a stiff rear bar, which wanted a throttle lock of at least about 0.3 (see the anti-roll bar guide).

## Not yet confirmed

- The torque T is inferred to be the whole axle torque, not verified.
- The native driver handles a slide differently from a person, so the feel has to be confirmed in game.

---

← [Camber and toe](camber-and-toe.md) · [Contents](README.md) · [Body dimensions](body-dimensions.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
