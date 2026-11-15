# Changelog

## 0.9.1 beta (2026-11-15)

- Import a tune: a new **Import a tune** start on the Build tab and in the setup menu. Reads the CarX Street Tuning Template (xlsx or a CSV export), other tune tables, pasted text and screenshots of tables or the game's Part Setup screens.
- The template's MODEL picks the car, and its part rows set the part tiers: engine and engine parts, gearbox, body stage (STG1–4), weight reduction, fuel tank, aero, springs, anti-roll bars, arms, dampers, brakes, spacers and body kit. Text values such as Stock, N/A or ranges are skipped, so those rows keep the car's own value.
- Body stage (STG1–4) is now part of the model: each stage has its own body mass and drag from the game data.
- Start-up fix: if Windows has blocked the downloaded files, Touge clears the block on its own files. If its window still cannot open, Touge opens in your web browser with a short note instead of an error.
- README: how to unblock the zip if Touge does not start.

## 0.9 beta (2026-11-15)

First public release. Download the zip from Releases, unpack it anywhere and run Project Touge.exe.

- Build: enter your car the way the game shows it. Gear ratios are kept exactly as typed, tyres are picked as width, rim and profile side by side, and front and rear values sit next to each other.
- Tune: symptom, advice and check are one path. Presets are picked at the top of the page, sliders show their limits, and terms have short explanations.
- Trail braking understeer advice corrected: brake balance to the rear, less decel lock, softer front bar or stiffer rear bar.
- On a route that is not calibrated yet, the model time is shown as a difference to your starting point instead of a total time.
- Saving tells you when the file was not written, and changing the car no longer overwrites a saved setup.
- First start is empty: choose your car first, the numbers appear after that. The language choice is kept between starts.
- Time: the timer window shows when no game is detected and can be hidden with F8 or the X button.
- Split rows now compare against the reference run at the same point on the route, so they match the live gap.
- The screen reader rejects a wrong gauge match and searches again if it stops getting readings.
- User guide and choriso's Tuning Bible updated for the new layout.
- Smaller download (about 80 MB).

Known limits: the timer reads the speedometer and minimap from the screen, so both must be visible while driving. Tested on a 3440x1440 display; report other resolutions that do not work in Issues.

## 0.9 beta test build (2026-11-12)

First test version.

- Runs as its own Windows app (Project Touge.exe), no installation or Python needed.
- Build, Tune and Time tabs; English by default, Finnish selectable.
- Timing, splits and telemetry read from the screen; controller buttons for start, split and pause.
- Setups, runs and routes saved as files inside the Project Touge folder.
- Settings: language, text size, view level (Simple / Advanced / Setup only), reduced animations, movable panels.
