# Changelog

## 0.11 beta (2026-11-16)

0.10.3 was not released; its changes are included here.

- **Share tunes, routes and runs:** export one as a file and send it to a friend. Files dropped onto Touge or into `Shared\Inbox` show up with a preview, and a shared run can be raced as a ghost.
- **Faster calculations:** the builder and tuning calculations run inside the program instead of the page.
- **Game physics (Experimental):** Touge can test a setup with CarX Street's own physics from your game installation. Off by default: turn it on in Settings > Game physics. Results are differences between setups, not lap times. The game's files stay in your game folder; Touge never copies or shares them. Slow (several minutes per check) and still being calibrated.
- **Calibrate to your driving:** game physics can be calibrated against your own timed runs.
- **Smarter tuning:** the model now knows front-wheel drive, all-wheel drive and mid- and rear-engine cars (camber, diff, aero, tyres and tyre pressures).
- Gearbox list includes every gearbox in the game (130), grouped by gear count, with search by name or gear count. Game readings also recognise gearboxes from other cars.
- Engine power can be typed in under Game readings if the shown value differs from your car.
- Quick guide in Tune it yourself, and the spacer shows the resulting Wheel Offset.
- About has a **Check for updates** button that shows the result right in the window. Shut down button in the top bar.
- **Signed updates:** every update is signed, and Touge checks the signature before installing it. Only the program, README, licenses and tuning guide are replaced (never your data folders), and if the new version fails to start, the previous one is put back.

Fixes

- All six included routes have their start and finish images, also for players whose routes were copied from an earlier version.
- Gearing graph updates while it calculates; its comparison lines are fainter.
- Best splits and theoretical time only use runs split the same way.
- The timer follows a route change, also right after finishing a run, and the timer window no longer goes dark.
- Closing Touge's main window closes the whole program, timer window included.
- Power is shown without race fuel; race fuel is shown as info.
- Status texts no longer appear in Finnish in the English view.
- About lists the program's current (Rust) licenses.

Updating: on 0.10.1 or later, press **Update now** in the update notice (or About > Check for updates).

## 0.10.2 beta (2026-11-15)

- The user guide is built in: open it from Help (F1), in English and Finnish, updated for 0.10.

## 0.10.1 beta (2026-11-15)

- One-click updates: when a new version is out, the notice has an **Update now** button. Touge downloads the release from GitHub, checks it against GitHub's checksum, replaces itself and restarts. Tunes, runs and routes are not touched.
- If a timed run is going on, Touge asks before updating.
- Coming from 0.10 or 0.9: update this one time by hand. From 0.10.1 on, the button does it.

## 0.10 beta (2026-11-15)

- One program file: no App folder and no Python, 24 MB download. Timer, automatic splits, run analysis and screen reader are built in.
- The six included routes are written to Routes on the first start.
- Updating from 0.9: copy the new exe over the old one, or unzip into a new folder and Touge finds your earlier Project Touge and copies your data.
- Routes: start and finish pinned more precisely, with their own names.

## 0.9.2 beta (2026-11-15)

- Screen reader: works with HDR screen capture, where the speedometer has a white background and turquoise outlined digits.
- Routes: an overview map of all routes, with start and finish pins and the start and finish names on each route.
- Route editor: short help on which start and finish images to take.
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
