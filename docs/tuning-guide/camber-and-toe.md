[![Project Touge choriso's Tuning Bible](banner.png)](README.md)

[Suomeksi](fi/camber-and-toe.md)

# Camber and toe

## In short

Camber and toe are small levers in this game. In the native model camber changes lateral grip by at most about 3.5 % and costs braking and traction grip 0.5 % per degree ●. In our experience camber −2 vs −5 was within noise on several cars ◐, but a front camber close to zero has cost more than a second ◐. Toe is a slightly bigger lever: on a rear-drive car rear toe-in raises grip in fast corners and rear toe-out costs grip ◐. Rear toe +0.2…+0.3 has worked in game ●, and its cost on the straight is small ◐. Refine bars, springs and the diff first, and use camber and toe to finish.

The game has two differences from a real car. The camber you set is not the tyre's actual camber, because the game adds −3…+5° to it depending on spring extension ●. And the native code has a rigid-axle suspension type on which the camber setting does nothing ●. Which of the game's suspension types (Mcferson or Doublewishbone) maps to the rigid axle is not yet known.

Markers: ● confirmed in game or in the game code, ◐ native simulation or inferred, not tested in game, ○ real-car theory.

## Camber: tyre angle

**How the game calculates it:**

1. Camber to the body = setting − 3° + 8° · x, where x = current spring length / stroke (0 = bottomed, 1 = fully extended) ●. At rest the actual camber is therefore about 2–3° more positive than the setting. A typical front wheel at rest sits at about setting + 2.4°, so −3.5 is about −1.1° at rest ◐ calculated.
2. Camber changes with travel by 8° / stroke, so with a 100 mm stroke it goes 0.8° more negative for every centimetre of compression ●. In a corner the outer wheel compresses and goes more negative, but the body rolls outwards and takes it more positive. On one test car these almost cancelled: at the limit the outer wheel was at about setting + 3.4° to the ground ◐.
3. In the tyre, camber does not raise the lateral peak. It stiffens the grip build-up: −5° gives 14 % more cornering stiffness, which feels like a sharper initial response ●. Lateral force also gets a small offset (−3° → +0.15°) with no practical effect ●.
4. Longitudinal grip (braking and traction) is multiplied by 1 − 0.005 · |camber|, so it drops 0.5 % per degree ●. At the front a large camber lengthens braking, at the rear it weakens traction.
5. Native suspension type 1 is a rigid axle: the wheels follow the axle's roll, and the camber setting and camber curve are zeroed ●. The game passes the car data's type to the native code as such, but whether Doublewishbone is type 1 is not known ◐. If it is, camber does nothing on cars with Doublewishbone at that end.
6. The adjustment range comes from the control arm parts. The base part gives −4.5° camber, and an adjustable part gives ±3.5°. With Prototype arms the limit is about −21.5° front and −22.5° rear ●.

**When you add negative camber:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Front camber more negative | A slightly sharper initial response and a few percent more mid-corner grip. | Braking gets longer and turning no longer improves. | ◐ Front 0 → −15: lateral grip +1.1 %. ◐ Front −3.5 → −2 was 0.4–0.6 s slower on two cars, −5 within noise. |
| Rear camber more negative | The rear holds slightly better mid-corner. Rear camber helps grip more than front camber. | The rear wheels spin on exit, because traction drops. | ◐ Rear −13: lateral grip +3.4 %. ● Rear −3.3 together with other changes has worked in game. |
| Camber towards zero | Braking and traction grip improve slightly. | Lateral grip drops and the initial response gets lazy. Positive camber clearly hurts. | ● Rear −4.3 → −3.5 together with another change was even in game. ◐ +10° −6.5 % (old run, only the direction is reliable). |

## Toe: wheel direction

**How the game calculates it:**

1. Toe is set in degrees. Plus is toe-in (the front edges of the wheels point inwards) and minus is toe-out ●. The game adds toe to the wheel angle, −toe on the left wheel and +toe on the right, front and rear ●.
2. At the front, toe comes on top of the Ackermann angle ●. Ackermann is its own setting (0 = full Ackermann, 100 = parallel wheels), and it had no measurable grip effect in the native model ◐.
3. In a corner, rear toe-in turns the loaded outer wheel slightly into the corner, so the rear makes more lateral force and the car stabilises ○ theory that fits the native result (rear toe-in raised steady cornering grip).
4. On a straight, toe means the wheels roll at a small slip angle in opposite directions. The lateral forces cancel, but a small drag remains ◐ inferred, not measured.

**When you add:**

| Change | Expect | Too much | Experience |
| --- | --- | --- | --- |
| Rear toe-in (+) | The rear calms down in long and fast corners, and grip in fast corners rises, most together with rear camber. No effect in slow corners. | Above +0.3 grip did not rise, but drag on the straight grows. The car starts to understeer in tight corners. | ● +0.2…+0.3 has worked in game on a rear-drive car. ◐ On a rear-drive car +0.2…+0.3 with rear camber −5: fast corners +5…+10 %, slow corners 0. ◐ On the straight +0.3 slowed 60–140 km/h acceleration by 0.015 s. |
| Rear toe-out (−) | The car rotates more readily. | The rear lets go under braking and in corners, and grip drops. | ◐ −0.3: grip in tight corners −3.6 %, in fast corners −3 %. On a full lap anything from neutral to 1.5 s slower, depending on the bars. |
| Front toe (±) | The effect is small. Toe-out sharpens turn-in ○. | The car wanders on the straight and feels nervous ○. | ◐ ±0.3 was 0.2–0.8 s slower in both directions on most cars and faster on one. |

## Effect on other settings

Camber depends on the suspension, so set it after springs and bars. Toe is nearly independent of other settings, but rear toe-in does the same job as settings that stabilise the rear.

| Setting | How it links to camber and toe in the game physics |
| --- | --- |
| Springs (length and rate) | Rest camber depends on sag. A stiffer spring or a longer length makes camber more positive: a much stiffer front spring about +0.8°, +8 mm length about +0.2° ◐ calculated. Check camber after big spring changes. |
| Bars and roll | The body rolls out and takes the outer wheel towards positive camber. Stiffer roll keeps camber closer to the setting ◐. Balance is still found with the bars, not with camber. |
| Caster | When steering, the outer wheel gains negative camber of about caster · sin(wheel angle) and the inner wheel positive ●. Caster 8.4 and a 30° wheel angle give about 4°. Caster had no grip effect in the native model ◐. |
| Ackermann | Front toe is added on top of the Ackermann angle ●, so change them one at a time. |
| Differential and brakes | Camber costs 0.5 % longitudinal grip per degree ●. Rear camber weakens exit traction in the same direction as a too-high throttle lock, and front camber lengthens braking. Rear toe did not change rotation or braking distance under braking in the native model ◐, so the rear under braking is handled with brake balance. |
| Tyres | The camber coefficient is the same on all tyres ●. In the game formula, width does not change the camber effect ◐. |
| Suspension type | A rigid axle (native type 1) zeroes camber ●. Check your car's suspension type before refining camber (see Not yet confirmed). |

## Symptoms

Change camber by 0.5° and toe by 0.1° at a time, and drive the same corner in the same gear. If the symptom responds to bars, springs or the diff, use those first.

| Phase | Symptom | What happens in the game | Change |
| --- | --- | --- | --- |
| Braking into the corner | The rear wanders or tries to overtake when you brake into the corner | Weight moves forward and the rear wheels' lateral force is not enough | Brake balance forward and front bar up. Rear toe did not change rotation or braking distance under braking in the native model ◐, so toe does not help here. |
| Braking into the corner | The front wheels lock or braking gets long | Large front camber costs longitudinal grip | Front camber 0.5–1° towards zero. |
| Turn-in | The car is lazy to turn | The front tyre's cornering stiffness is low | Front camber −0.5°. Front toe −0.1 helps in theory ○, not in the native model. Try the bars first. |
| Mid-corner | The rear slides in a long corner | The rear wheels run out of lateral force | Rear toe +0.2…+0.3 and rear camber towards −5. On a rear-drive car fast corners +5…+10 % ◐, and rear toe +0.3 has worked in game ●. No effect in slow corners. |
| Mid-corner | The car understeers in a long corner even though the bars are set | Rear toe-in holds the rear too much | Rear toe towards zero. |
| Exit | The rear wheels spin as you straighten and open the throttle | Rear camber costs traction | Rear camber 0.5° towards zero ●. |
| Straight and top speed | The car wanders or feels nervous | Toe-out at either end ○ | Front toe 0, rear toe 0…+0.3. Rear toe-in costs little on the straight: +0.3 slowed 60–140 km/h acceleration by 0.015 s ◐. |
| Bumps, kerbs and gutters | The feel changes as the suspension compresses | Camber changes with travel by 8° / stroke ● | Do not correct with camber; use the suspension. |

## Final tip

Camber −3.5 / −3.5 has been in every working setup of the touge weapon preset in game ●. On screen it looks like a lot, but at rest it is about 2–3° more positive than the number. Keep front toe at zero. On a rear-drive car rear toe +0.2…+0.3 has worked in game as a starting value ● and raised grip in fast corners in the native model ◐. The gain starts at less toe when rear camber is larger: with rear camber −5 even +0.1 showed, with −3.9 only about +0.3. Above +0.3 added nothing ◐.

If you do not know whether camber affects your car, do a quick test: front camber −3.5 → −8 and drive the same corner. If the feel does not change at all, the front axle is probably the native rigid axle.

**Simulation experience ◐ (native model, not tested in game):** front camber −4.6 → 0 was 1.4 s slower, mostly in medium-speed corners, and with a stiff front bar even more (2.3 s together). −6.5 brought nothing over −4.6. So front camber is more than a finishing touch when it starts near zero. Rear camber and front toe did not show in lap time.

## Not yet confirmed

- The suspension type is the main open question: is Doublewishbone native type 1, the rigid axle? The game metadata is encrypted, so a game test decides it (front camber −3.5 vs −8).
- The rest camber examples assume the stroke equals the spring length. That is inferred from the bottoming formula, not read from the native code.
- The grip results are from the native model. There is no separate game test of camber or toe alone; the game tests changed another setting at the same time.
- Toe drag on the straight has been measured in the native model: rear toe +0.3 slowed 60–140 km/h by 0.015 s and +0.5 by 0.025 s ◐. The effect is small.
- The rear toe grip figures are from one rear-drive 50/50 car ◐. The circle test steps grip in 2–5 % increments, so a single step is a direction, not an exact figure. The direction repeated with two rear cambers.
- The front toe effect on turn-in is real-car theory ○, and the native model did not support it.

---

← [Dampers](dampers.md) · [Contents](README.md) · [Differential](differential.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
