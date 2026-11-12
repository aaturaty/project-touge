[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/glossary.md)

# Glossary

## Settings: the guide's words and the game's names

The guide uses short everyday words. This table shows the name of each setting in the game's own menus, as Touge also shows them in the To game view.

| In this guide | Name in the game | What it is |
| --- | --- | --- |
| Anti-roll bar, bar | Anti-roll bar: Stiffness | A torsion spring between the left and right wheel of one axle. Game value × 2000 = N/m. |
| Spring length | Spring Length | Ride height and suspension travel in millimetres. |
| Spring, spring rate | Spring Stiffness | Wheel rate. Game value × 1000 = N/m. |
| Slow bump, slow rebound | Slow Bump, Slow Rebound | Damping below the 0.1 m/s knee: body motion in braking, turn-in and on throttle. |
| Fast bump, fast rebound | Fast Bump, Fast Rebound | Damping above the knee: bumps, kerbs and gutters. |
| Camber | Camber | Tyre angle; the game adds −3…+5° depending on spring extension. |
| Toe | Wheel Toe | Wheel direction in degrees; + = toe-in. |
| Caster | Caster Angle | Steering axis tilt; changes camber when steering. |
| Ackermann | Ackermann Angle | 0 = full Ackermann, 100 = parallel wheels. |
| Throttle lock | Lock on acceleration | Share of driveline torque that locks the diff on throttle. |
| Decel lock | Lock on deceleration | Share of engine-braking torque that locks the diff off throttle. |
| Preload | Preload | Constant diff lock in newton-metres, also with the clutch pressed. |
| Brake balance | Front Brake Balance | Share of brake torque on the front axle. |
| Offset, spacer | Front / Rear Wheel Offset | Wheel position outwards; track = base track + offset. |
| Tyre pressure | Pressure | Grip peaks at 2.0 bar; higher pressure lowers rolling resistance. |
| Tyre profile | Tire profile | Sidewall height in percentage points (±10). |
| Final drive, FD | Final drive | The last ratio; total ratio = gear × final drive × tyre radius. |
| Centre of gravity | Center of Mass Height (Part Setup) | A percentage of the body box height, not inches. |
| Front weight | Weight Distribution in Front | Share of the car's weight on the front axle. |

## Driving phases

| Phase | What is happening |
| --- | --- |
| Braking into the corner | Braking in a straight line and trail braking towards the apex. Weight moves to the front. |
| Turn-in | Off the brakes and turning in. Weight moves to the outer wheels. |
| Mid-corner | A steady corner; the body has stopped moving. Springs and bars decide the balance. |
| Exit | Opening the throttle and straightening. Weight moves to the rear; the diff works. |
| Straight | Acceleration and top speed. Gearing and drag decide. |
| Bumps, kerbs and gutters | Fast suspension movements, verges and gutters. Travel and fast damping decide. |

## Terms

| Term | Meaning |
| --- | --- |
| Understeer | The front gives up first; the car goes wider than you steer. "The nose pushes." |
| Oversteer | The rear gives up first; the car rotates more than you steer. "The rear steps out." |
| Load transfer | Weight moving between wheels under braking, acceleration and cornering: m · a · h / track (or wheelbase). |
| Roll stiffness | How strongly an axle resists body roll: bars + springs, both × track². |
| Bar split, LLTD | The front axle's share of roll stiffness. The axle with the larger share carries more of the cornering load transfer and lets go first. |
| Travel | How far the suspension can still compress before the bump stop: spring length − sag. |
| Bump stop | The rigid end of travel. Hitting it throws the car and costs grip. |
| Sag | How much the spring is compressed by the car's weight at rest. |
| Natural frequency | √(spring / mass) / 2π. Keeping it equal moves a spring setup to a heavier or lighter car. |
| Damping ratio, ζ | Damping relative to the spring and mass; Touge uses it to move dampers between cars. |
| Knee | The wheel speed (0.1 m/s) where damping changes from the slow to the fast value. |
| Total ratio | Gear × final drive × tyre radius; the only gearing number the physics uses. |
| Rim part | The wheel part chosen for a tyre size; it sets the tyre's friction bonus (+0.03…+0.08). |
| Native model | The game's physics engine run outside the game with a computer driver, used to compare settings evenly. |
| Within noise | A difference smaller than the normal run-to-run spread, about 0.8 s on a six-minute run. |

## Markers

| Marker | Meaning |
| --- | --- |
| ● | Confirmed in game or in the game code. |
| ◐ | Native model or inferred, not tested in game. |
| ○ | Real-car theory, used only as background. |

---

← [Body dimensions](body-dimensions.md) · [Contents](README.md)

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
