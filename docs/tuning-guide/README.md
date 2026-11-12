[![Project Touge Tuning guide](banner.png)](README.md)

[Suomeksi](fi/README.md)

**PDF:** [Project-Touge-Tuning-Guide.pdf](Project-Touge-Tuning-Guide.pdf)

# Tuning guide

## About this guide

This is the long read behind Touge's Tune tab. The Tune tab tells you which setting to try for a symptom; this guide explains why it works in CarX Street, what happens when you go too far, and how the settings affect each other. Read it from start to finish if you want the whole picture, or open one chapter when a setting puzzles you.

Everything here is about how this game calculates the car, not how a real car works. Where the game behaves like a real car, the guide says so. Where it does not, the game wins.

## Where the knowledge comes from

- **The game's own physics code and data.** The formulas in the "How the game calculates it" sections come from the game's driving physics and its part data.
- **The native model.** The game's physics engine, run outside the game with a computer driver on a real route. It drives the same car with the same settings many times, so it can compare settings far more evenly than a person can.
- **Experience in game.** Setups driven and timed in the game itself, on touge routes, by a real driver.

Markers: ● confirmed in game or in the game code, ◐ native model or inferred, not tested in game, ○ real-car theory, used only as background.

When the guide says "in our experience", the result comes from game tests or native runs on a handful of cars. Treat the numbers as an order of magnitude for your car, not a promise.

## How the game differs from a real car

A few things in the game physics change the usual tuning advice. They come up again in the chapters.

| In the game | What it means for tuning |
| --- | --- |
| The roll centre is at ground level ● | All cornering load transfer goes through springs, bars and dampers. The bars do not reduce total transfer, they only decide which axle carries it. |
| Spring length is ride height and travel ● | Spring length is one of the biggest levers: it sets how much travel is left before the bump stop. |
| The damper knee is high, 0.1 m/s ● | The slow values do almost all of the handling work; the fast values act only on bumps, kerbs and gutters. |
| The game adds −3…+5° to the camber you set ● | Camber on screen is not the tyre's real camber; at rest it is about 2–3° more positive. |
| The diff lock is a share of driveline torque ● | The same lock locks much more in a low gear. Preload is the only lock with the clutch pressed. |
| Tyre grip grows with width to the power 0.41 ●, and the rim part sets the friction bonus ● | Width and the right rim part matter more than diameter. |

## How to use it with Touge

1. **Build** the car on Touge's Build tab, or enter it from your screenshots.
2. **Start** from a preset such as touge weapon, then drive a few laps in the game.
3. **Find the phase** where the car does not do what you want: braking, turn-in, mid-corner, exit, straight, or bumps and gutters.
4. **Pick the symptom** in the Symptom view on the Tune tab. It shows the change to try first and second, and links to the chapter of this guide that explains it.
5. **Change one thing at a time** and drive the same corner in the same gear. Move the setting into the game with the To game view.

## How to read a chapter

Every chapter follows the same pattern:

1. **In short:** how big the lever is and the one thing to remember.
2. **How the game calculates it:** the formula or mechanism, with markers.
3. **When you raise:** what to expect, what happens when you go too far, and the experience behind it.
4. **Effect on other settings:** what else changes when you touch this one.
5. **Symptoms:** phase, symptom, what happens in the game, and what to change.
6. **Final tip:** how to approach it on a new car.
7. **Not yet confirmed:** what is still open. Read this before you trust a number.

## Chapters

1. [The whole chassis](whole-chassis.md): the biggest levers, setup order, how to test, and a symptom index.
2. [Tyres](tyres.md): width, rim part, pressure, diameter and track.
3. [Springs](springs.md): spring length, stiffness and the front/rear balance.
4. [Anti-roll bars](anti-roll-bars.md): stiffness, roll and the front/rear split.
5. [Dampers](dampers.md): slow and fast bump and rebound, and how they work together.
6. [Camber and toe](camber-and-toe.md): tyre angle and wheel direction.
7. [Differential](differential.md): lock on acceleration, lock on deceleration and preload.
8. [Body dimensions](body-dimensions.md): wheelbase, track, centre of gravity and mass as a starting point.
9. [Glossary](glossary.md): the guide's words and the game's setting names.

## A word of caution

The fastest setup depends on the driver. When two options are within about half a second, keep the one that feels easier to control. Nothing in this guide replaces driving the change in the game.

---

[Contents](README.md) · [The whole chassis](whole-chassis.md) →

<sub>Project Touge is an unofficial fan-made tool for CarX Street. It is not a CarX Technologies product.</sub>
