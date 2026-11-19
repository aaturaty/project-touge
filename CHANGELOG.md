# Changelog

## 0.12.2 beta (2026-11-19)

- **Easier to read:** text is in IBM Plex Sans and numbers, units and value columns in Plex Mono. Grey filled buttons, selects and panels are gone, and secondary actions are plain links.
- **Things where you look for them:** chassis stiffness sits under Preset mix, Play and Compact on the situation timeline, Import and Share and import under Save as, the stopwatch and manual entry under Import, timing Settings inside the timer section, and Refresh and Open report under Target. Splits come before Ghosts, and the Overview's share, read and copy actions sit above the page navigation.
- **Setup card:** shows class, engine, gearbox, weight, route, best run and whether the setup is modified, with Open as the main action.
- **Clearer wording:** Enter pre-existing build, Changed / Show all, Average of last 5, and the controller actions listed as key chips. Changes to try now shows in every mode, so the Try changes link is gone.
- **Steadier turning data from the timer:** the minimap rotation is now measured on the inner part of the map. A tilted minimap was read about 15 % low before (measured on circle runs in the game). Run analysis corrects older runs too, so lateral g and the symptoms in run analysis change slightly.
- Polish: update notice, Getting started strip, Overview tabs and buttons, timing settings layout, leaderboard header and Enter build fields.
- The user guide uses the new names.

## 0.12.1 beta (2026-11-19)

- **Your own car in the pictures:** Build shows each car's real side outline, drawn from the game's own car model, in the side view with axle loads, the suspension picture, the Aero by speed picture and the Tune situation view. Tall cars such as vans are scaled to fit.
- **Suspension situation view and damper response:** now model tire compliance and the unsprung mass at each corner, and use the damper values as the game's own numbers (no fitted factor). Damper changes now move the front load share by 0.6 to 0.9 times as much as in game physics tests (◐).
- **Game physics test is steadier:** sections where the test driver does not repeat itself are now left out of the comparison, measured for each car and setup on every run. The noise floor drops by about half (AE86 0.3–0.4 s → 0.1 s, FD 0.33 → 0.20 s, ◐).
- **Tuning Bible pictures:** the Springs, Anti-roll bars and Dampers chapters now show Touge's own pictures (situation view, damper curve, roll and spring compression) with a before/after change and a caption.
- **Your run on the Tune page:** after you time the first run with a setup, the Symptom view shows what the telemetry saw in each corner phase (braking, turn-in, mid corner, exit): understeer at full lock, oversteer (slide or countersteer), wheel lockups and wheelspin. Symptoms that repeat in at least two corners get a card with what the bars and dampers do in that phase and the first changes the symptom rule would make (◐: suspension travel and wheel loads are not measured). With an earlier run on different values, it also shows how much more or less the car turned in the same corners.
- **Runs record more about your steering and car:** the timer now also stores the stick's average, smallest and largest position between screen readings (the controller is read about 125 times a second, the screen 26–30 times) and the stick's up/down axis. Run analysis checks the run's measured gearing against the setup Touge had selected: when they do not match, the run is marked "gearing does not match the selected setup, car uncertain" instead of being filed under the wrong car or setup.
- **More driving tips after a run:** tips now compare your line and slide with the reference run: how wide the arc was (use more road), how much the car slid at the apex, lateral g at the apex (grip left unused or a tighter arc at the same grip), rear lockups under braking, throttle on and off mid-corner and downshifts in the corner (◐).
- **Run comparison:** the map is full width and can be coloured by gap to B, speed, gear or your speed against the model (◐). The throttle, brake and steering charts are now one Inputs row: throttle and brake as bands for both runs, steering only where the stick is at the limit or countersteering. On the whole route only corners where the runs differ by 10 m or more stand out; zoomed into a corner, the difference is written out. The whole comparison fits on a 1080 px screen.
- **Route statistics:** without its own map, in the order Splits, All corners, then Model and game (closed by default).
- **Share and import:** one window with Share and Import tabs. Pick what to share, rename the shared copy without touching your saved setup, and copy the share text straight from the field. Import takes a dropped file or pasted text.
- **Share image:** your own banner picture can be moved and zoomed in the share image, and the photo band is taller. The Routes list now shows the background through it.
- **Calmer pages:** the Tune page header takes less room (view level is a small menu, preset notes in the preset tooltip), longer explanations use IBM Plex Sans while values and tables stay mono, part tier rows show colour only on the chosen tier, the Overview timeline sits below the content, and a game timer that stops answering is shown once in the top bar instead of in several places.
- **Guides:** the user guide and the Tuning Bible have new screenshots and text for the current interface.
- Fixed: the situation view no longer says "neutral than mid-corner" when the front share equals the mid-corner value.
- Fixed: a symptom card could move the anti-roll bars the wrong way when your own setup was already outside the bar ratio range (for example the AE86). The rule now steps your own game value instead, within the game's slider limits.
- Fixed: small layout issues found in a visual review (setup menu cut off, route editor fuel stations in the "changed" colour, mixed button and badge styles).

## 0.12 beta (2026-11-18)

- **Shift time from game data:** gear changes now take as long as in the game: gearbox shift delay × clutch part × clutch slider. New **Clutch** and **Clutch slider** choices under Build > Drivetrain. The default is the Prototype clutch with the slider fully left. Lap estimates move a little because of this (the old fixed shift time was about twice too long), and the gearing search now prefers the T50S.
- **Gear shifting like real driving:** the lap model now holds each gear until about 90 % of the rev limiter instead of shifting up early. Lap time estimates change slightly, usually by −1 to +1 s on North Touge v2, and engine and gearing comparisons follow in-game acceleration more closely.
- **Engine selection by acceleration and weight:** when the engine or its parts are free, Touge now fits parts and Part Setup sliders to the class for the best mid-range acceleration plus the lowest total weight, instead of the highest average power, and ranks engines the same way. In game physics checks on North Touge v2 (◐) this kept far more of the genuinely fast engines in the shortlist (Supra: 6 of the top 8, before 2), and the new builds were about 0.4 s faster on average. The fit keeps the rev limiter where it is, and the optimiser finishes the top three engine candidates on route time (parts, sliders and gearing). Suggested engines, parts and lap estimates change.
- **Shift points in every run:** Analyze > Run by corner shows each run's full-throttle upshifts per gear (median and range) next to the model's best shift point for the loaded setup, with an estimate of the time each shift costs. The best shift point is only shown when the run was driven with the loaded car.
- **Two top speeds:** the gearing view shows the estimated top speed on your route (the fastest full-throttle stretch, downhills included) and the top speed on an endless flat straight, with which one limits it (drag or the rev limiter in top gear). New: time to top speed.
- **North Touge v2 comes calibrated:** lap estimates on North Touge v2 use a ready calibration from real runs until you calibrate it with your own runs. Shown as "Pre-calibrated".
- **Presets per area:** Chassis: Model, CalcX by StepUnique and choriso's. Diff: Model, Forgiving, Touge, Precise and Track. Gearing: Model and Old Meta (formerly Step's go-to). Presets you have saved still work.
- **Aero follows the wing:** the downforce slider's maximum now follows the wing part you have chosen, as in the game. The rear wing is preselected at the cheapest level that matches the front.
- **Two diffs on all-wheel-drive cars:** Tune > Gears shows the front and rear diff side by side on AWD cars, and Overview lists the FRONT DIFFERENTIAL rows. The front diff starts from the game's AWD values (0.30 / 0.00 / 0), is saved with your setup and is read when you import a screenshot or a tuning template. Diff presets change only the rear diff. On AWD cars the diff symptom fixes under Handling now also adjust the front diff, and the Tuning Bible symptom cards and diff chapter cover the front diff (directions inferred from the diff physics, ◐).
- **Game physics (Experimental):** front-wheel-drive and all-wheel-drive cars now use your front diff settings (before, the game's default front diff was used, so front diff changes had no effect). On AWD cars the check also tries the front diff's throttle lock. The check also tries the final drive 4 % up and down. Each check now also runs three copies of your current setup, compares against their average and shows that spread as the uncertainty, so a single lucky or unlucky run of your setup no longer shifts every result (the check takes a little longer). Differences calibrated to your own runs use the same reference.
- **Timer reading settings:** Settings > Timing has two new choices for the screen reader: **Minimap reading rate** (15 or 30 Hz; 30 Hz gives finer turning and slide data but uses more CPU) and **Save minimap images** (for more precise driving-line analysis; about 10 MB per run, kept for one day and at most 200 MB in Logs\naytonlukija). Below them Touge shows the rate the reader actually reaches and how much CPU it uses. Defaults are unchanged (15 Hz, no images), and changes take effect the next time the game timer starts.
- Clearer Tune page: Check is now **Advice** and To game is now **Overview** everywhere. The Tuning Bible link sits next to Handling and presets, and the symptom view puts the suggested changes right under the symptoms.
- Faster optimiser: with a free engine and gearbox, fitting the engines and comparing engine and gearbox combinations is several times faster, and it uses more of your processor cores. The results are the same. While Touge calculates, the progress bar now moves instead of standing still.
- **Suspension situation view (◐):** Tune has a new view under springs, anti-roll bars and dampers covering braking, braking into a corner, turn-in, mid-corner and power on. It shows the whole car (pitch, roll, wheel loads), the front share of load transfer over time and the damper operating point. It updates live while you drag a slider and has a compact table mode, and the symptom preview shows the suggested change in the symptom's corner phase. The model was checked against the game physics engine, but its values are estimates.
- Build charts are now lighter and update live: the aero chart follows the downforce slider while you drag it.
- One calculation engine: all of Touge's calculations, including the optimiser, engine fitting, route building and shift points, now run on the same Rust code. The program uses it directly and the page falls back to the same code as WebAssembly, so the page and the program always give the same numbers. The old JavaScript copy of the model is gone.

### choriso's Tuning Bible: two new chapters (in Touge and on the [guide pages](https://aaturaty.github.io/project-touge/), English and Finnish)
- **Engine:** how parts and Part Setup sliders shape the torque curve, why class is decided by peak power, what each Prototype slider does and a min-max order for engines at the class limit, and a Supra engine test on why engines in the same class give different lap times (◐). Includes the hidden part factor of all 137 engines, which decides how far each engine's curve moves per slider step.
- **Gearing and gearbox:** how ratios, final drive and tyre size combine, the shift delay and mass of every gearbox type, a setup order and a symptom table.
- Confirmed in the game (North Touge v2, C3): **search the final drive again after an engine swap.** AE86 with the PV2 engine FD 4.52 → 4.35 was 2.1 s faster, Supra FD 3.98 → 4.14 set a route record, and S15 with the ND engine FD 4.59 → 4.40 went from 6:11.25 to 6:08.76. On the RX-7 FD a stiffer rear anti-roll bar (58 → 66) set a route record.
- Still estimates (◐): engine rankings at the class limit come from the simulation model, and the game physics disagree with it, so treat the engine table as a shortlist to test. The 7- and 8-speed gearboxes were no faster than the T50S on North Touge v2.

### Fixes
- The first page load no longer hangs on a stylesheet now and then.
- A ghost from a shared route now finds the route it belongs to (before it said the route was not in your routes). Runs shared from 0.11 still carry the old route mark, so share them again from 0.12.
- Saved data is written to disk before files are replaced, so a crash or power cut cannot leave a half-written file.

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
