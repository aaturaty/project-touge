# Changelog

## 0.20.1 beta (unreleased)

**0.16 → 0.20.1 in short.** 0.18 and 0.20.0 were never published on their own, so 0.20.1 carries them all:

| Area | What changed |
|---|---|
| **Build** | 01 Build starts with two paths: enter the build you already have (screenshots, a table or by hand), or let the **Build Wizard** build the car step by step. The result shows an estimated time gain between builds, not a lap-time prediction. |
| **Setup model** | A car character model for 125 cars (◐) shows how your setup changes balance, rotation, wheelspin, roll, inner-wheel load and bump-stop travel. **Base setup** solves chassis and diff from each car's own physics, and keeps the settings you made yourself. |
| **Tune** | The symptom advisor gives up to three concrete changes for your exact car (◐), and the race engineer tells after your next run whether the change helped. Chassis and Gearing have a new layout, and **My view** is a cockpit with widgets and an Auto-Focus Lens. |
| **Presets** | The built-in chassis presets are **Model** and **CalcX by StepUnique**; the old touge weapon and choriso presets are gone, and setups saved with them open on Model with their own values kept. A setup keeps its preset version until you update it. |
| **Engine and physics** | Stat power is shown without race fuel, and race fuel no longer raises engine inertia. Game physics (Experimental) runs on Touge's own Rust implementation of the game's car physics and no longer needs the game's files. |

**Your folder is the same as in 0.16**, and Touge writes nothing outside it except the WebView2 browser cache ([details](README.md#where-your-files-live)):

```text
Project Touge\
├─ Project Touge.exe
├─ README.txt
├─ Shared\        what you share; Inbox\ for files from friends
└─ Data\          settings, tunes, routes, runs, logs
```

**New**
- **Build Wizard progress bar:** while the model builds your car, the wizard shows a progress bar with the current stage (stock run, then your build) and the time left, learned from your previous build (about 7 seconds by default); when a build takes longer it counts the seconds instead of saying almost done.
- **Build Wizard:** 01 Build starts with two paths. **Enter pre-existing build** takes your car from Part Setup screenshots, a table or by hand. **Build with the model** walks through target (car, class, route), body and aero, engine, drivetrain and tyres; at each step you let the model decide, keep the defaults or choose yourself, or press **Build now** for the whole car at once. The result shows the estimated time gain against stock, your saved build or the previous result. It is a difference between builds, not a lap-time prediction, and the screen says so.
- **Car character model (all 125 playable cars, ◐):** Tune → Chassis shows how your setup changes the car across measured character traits: mid-corner balance, entry rotation, exit wheelspin, body roll, inner-wheel load and bump-stop travel, with live bars that follow your drag and an entry/mid/exit corner-phase chart.
- **Base setup from the car's own physics (◐):** the default chassis and diff are solved for each car from its physics model with a bump-stop floor and a preload cap of 3 % of drive torque, instead of general rules. It keeps the settings you made yourself, leaves the values of a saved setup locked unless you allow changes, and scales springs and dampers to the build's weight, so a heavy and a light build of the same car keep the same handling character.
- **Symptom advisor for your car (◐):** pick a handling symptom and corner phase, and Tune shows up to three concrete changes for your exact car and setup, one per group (springs and bars, geometry, diff, tyres/brakes/aero, dampers), each one game step, with its side effects. **Apply** follows a one-change-at-a-time rule and can be undone.
- **Race engineer: "Did it help?" (◐):** after you apply a suggested change, Touge compares up to five timed runs before and after it, and Tune → Symptom → **From your run** says **Helped**, **Trade-off** or **Did not help**, with **Keep the change**, **Keep and take another step**, **Undo**, or **Undo and try option #2**. A symptom that repeats shows in how many corners it happened; a one-corner symptom points you to your line in Analyse instead.
- **Race engineer: what costs you the most (◐):** symptoms are sorted by the seconds they cost, and the most expensive one is marked **Start here**. Understeer is judged against your own runs in that car, and corners lost to a driver error (a touch, a late brake, a tighter line) are listed separately instead of counting as a car symptom. Suggestions weigh the corner phase and speed: mechanical grip and diff in slow corners, bars and springs in fast ones, no dampers at the apex, no brake bias on exit.
- **Race engineer: tried changes and hints (◐):** a **Tried changes** list remembers the changes you rejected, also after a restart, and can be cleared with one button. Tune shows a bottoming chip when bump-stop margin is under 10 mm, and a run that sits on the limiter in top gear or at low revs in corners suggests a gearing change.
- **My view cockpit:** add widgets (character, balance and numbers, a low sawtooth chart, a diff card with draggable arcs) and a monitor strip (time, LLTD, roll, ride frequency, top speed, acceleration). The **Auto-Focus Lens** follows the last slider you touched. Final drive and diff sliders can be added to My view.
- **Presets keep their version:** a setup stays on the preset version it was made with. **Update preset to newest version** shows what would change before you apply it. **Preset mix** now changes only the chassis.

**Changed**
- **Tune layout:** Chassis opens with springs and anti-roll bars, General folds into a one-line summary, and the right column has tabs **Character ◐** and **Balance & numbers** with your monitors on top. Gearing has a **Gear / Range** slider that drags the sawtooth chart, a wide Final drive and a compact shift time. The bottom navigation runs Symptom → Parts → Chassis → Gearing → Other → Overview, and **Done · save** is on Overview.
- **Built-in presets:** the chassis presets are **Model** and **CalcX by StepUnique** (plus your own presets). The old touge weapon and choriso presets and their gearing profiles are removed; a setup saved with them opens on Model and keeps its own values. The diff characters (Forgiving, Touge, Precise, Track) and Old Meta gearing stay.
- **Sliders follow the game:** slider steps and limits come from the game's own tick tables, the stock diff comes from the game data for all 125 playable cars, spring-length sliders show the bump-stop zone, and diff preload shows the 3 % torque ceiling.
- **Engine figures:** stat power and torque are shown without race fuel, with the race fuel effect shown separately. Race fuel no longer raises engine inertia, and peak power is in metric PS throughout.
- **Tyres:** the tyre pressure effect is capped at 3.0 bar, and the wizard applies the tyre rule (width at least 285, 3.0 bar) to the saved build.
- **No LLTD route setting:** the LLTD target and its route-time scenario are gone. The table behind it disagreed with later physics tests, so the route time no longer depends on it.
- **Game physics without the game's files:** Game physics (Experimental, off by default) now runs on Touge's own Rust implementation of the game's car physics. It gives the same results as the game's physics library on every car in the game data (the 125 playable cars and one hidden placeholder), and runs as fast. You no longer need the game installed in a findable folder, and the readiness check and Settings no longer ask for it.
- **Analyse → Tune:** the Next card in Analyse shows one setup change for a recurring car symptom, the same one the symptom advisor gives, and **Open in Tune** opens that symptom.
- **choriso's Tuning Bible** tells you to start a new car from **Base setup** instead of a removed preset.
- **Maps face north** like the game's map, in Routes and in the route editor.
- **Faster and smoother:** fixed the gear downshift lock-out and shift-cut interpolation in the route model, sped up hot loops, and moved the Build, Engine and Route charts to one accessible chart module (keyboard navigation, focus styles, reduced motion); the run comparison in Analyse keeps its own synchronised chart.
- **Live timing:** current-run distance is scaled like saved runs, so live split gaps compare at the same place on the route.
- **Local server hardening:** requests that change data need a per-session token and must come from Touge's own page.

**Fixed**
- Generated gearing ends the top gear at a route-specific limiter speed (255–260 km/h on North Touge, Full Touge Run, Lighthouse Run and Touge Loop, 236–240 km/h on Fujiwara Run ◐, none on Sunset Speedway), so you no longer sit on the limiter at the end of fast straights. The Game physics Optimizer skips final-drive candidates that move the top gear out of that band.
- Game physics (Experimental): race-fuel builds now top out in each gear at the same speed as in the game (the limiter came from the race-fuel multiplier instead of the base limiter), and the tyre profile setting counts in the tyre size (ADR 0029). Cached Game physics reference speeds are recalculated after updating.
- Autosplit no longer slides on long full-speed sections (for example North Touge's Full speed downhill): the live gap could jump by 8–10 s around a split and the split itself could land seconds off. The alignment now also follows the distance you have driven (◐ checked on 101 recorded North Touge runs).
- Opening an older saved setup no longer shows unsaved changes before you touch anything.
- Drive → latest runs and the Tune timeline show only runs made with the selected car.
- The run report says the apex gear as a whole number ("at apex 3rd"), also in English.
- The race clock's minute digit no longer flickers, and panels no longer flash when they redraw.
- The Situation chart no longer repeats the same value on its axis, and the anti-roll bar legend keeps each percentage on one line.
- Drive labels its two gaps: the big number is the gap now (against the record or your chosen run), and the clock line names the split it compares at.
- The Drive map hides the "appear here when the game is found" note once your position shows.
- My view offers **Restore default monitors** when the monitor strip is empty.
- Game physics simulated double-wishbone axles as a solid axle, so camber had no effect on those cars in Game physics runs. They now run as double wishbone, and the car character model behind Base setup and the symptom advisor is refitted on the fixed physics, so camber now counts in its results (◐). On the S15 the new Base setup is about 0.2 s slower on the test routes than before (◐).
- The symptom advisor no longer refuses every spring change on a car whose stock setup already sits below the bump-stop margin (for example the RX-7), and never suggests a diff lock under 0.22 or a step cut off at a slider limit.
- Copy list no longer prints "undefined", and the change list names presets by name and version.
- Tune spring lengths, and changes made in Tune, survive a tyre, engine or parts change on the Build tab.
- Part Setup sliders no longer miss their data when the page loads before the calculation is ready.
- Slider knobs no longer jump sideways on hover, and quick double-taps on + / − no longer drop steps.
- The Recalculate basis and the selected route no longer count as unsaved changes.
- Number keys no longer switch tabs on the Build page, and the Build tab returns to an unfinished build.
- Start new build no longer carries the previous car's tuning into the new build.
- Corner radius sign in segment analysis, and the standard error of Game physics runs that stop early.
- Build Wizard: the engine step shows the engine's own weight (it read 0 kg on a stock engine), and power uses the car's own engine brake value.
- Build page: the Differential card's lock values no longer overlap their labels (short labels, the full name shows on hover).
- Build Wizard: engine power, torque and weight changes are measured against the stock engine (they could show a huge time loss or 0 kg), weights follow imperial units, **Build now** starts the later steps fresh, and saving a model build checks that the file was written.
- Saving a setup backup that clashes with another one says so, instead of saying Touge is not running.
- The engine card's peak power and Component Features show the game menu values (without race fuel), also while you drag a part slider; the race fuel value is shown beside them.
- Model preset: the chassis now stays inside the game's slider limits and uses the car's drivetrain, the same limits Base setup uses.
- Race engineer: the median of an even number of runs is the mean of the middle two, the gearing hint ignores neutral and very low speeds, and **Did it help?** no longer calls a change helpful or unclear on too little evidence.
- Run analysis no longer stops when a run has no time or no speed data; the report is written anyway.
- The screen reader reports a repeating capture error (HDR or 10-bit desktop, lost display) to the readiness check instead of waiting silently, and survives a lower screen resolution.
- Links inside Touge open only web pages in your browser, and closing Touge stops a running Game physics job.
- Keyboard focus rings are clearly visible, warnings carry a ⚠ sign instead of colour only, and screen readers hear confirmations and chart values.

## 0.16.0 beta (2026-11-22)

**0.15 → 0.16 in short.** Four releases (0.15.1, 0.15.2, 0.15.3 and 0.16.0) changed most of what you see and a good part of what happens underneath:

| Area | What changed |
|---|---|
| **Interface** | Tune sliders follow your drag in real time and work from the keyboard; the page is updated in place instead of redrawn. **My view** keeps your own sliders and monitors in one place. Wide screens are used up to about 2400 px, and **Compact** density fits more sliders. The top bar keeps your setup's name with a count of unsaved changes and a list of what changed, each line with its own revert. One icon set, one set of button and panel rules. |
| **Setups and presets** | The Setups window has a **Presets** tab: your own presets and gearing profiles with what each covers, apply, rename, duplicate, share and delete with undo. **Save current as preset** lets you choose chassis, diff and gears, and a partial preset changes only those parts. |
| **Calculation** | The optimiser runs on all processor cores (a full optimisation about four times faster, 22.5 s → 5.8 s on 4 cores, same result). A new result shows about five times faster, because only the page you look at is redrawn. Gearing and Chassis show which tyres, engine, mass and front weight the model used, turn yellow when the parts have changed since, and **Recalculate** brings them up to date. |
| **Timing** | Drive fits on one screen with the clock, the map with named split points, your latest runs and the readiness check. A session row shows route, opponent, car, record, median and runs. During a run the gap follows the car and the map shows you and your opponent. Abort can be undone for 10 seconds, a result card stays after the finish, and **Discard run** removes a test run with its data. |
| **Analyse and Routes** | Analyse has one corner table with tabs (Practice, This run, All corners, Splits, Model and game, Leaderboard), a right column with the verdict and the losses, and charts and map that follow each other. Routes is one screen in three columns with search, filters and game routes grouped by type. |
| **Speed and housekeeping** | Run analysis is about three times faster, the page starts faster, settings are saved per key instead of rewriting one large file, and the game timer no longer uses network ports. **Settings · Data** can remove the 0.12 run folder that nothing reads any more. |

**Your folder is the same as in 0.13**, and Touge writes nothing outside it except the WebView2 browser cache ([details](README.md#where-your-files-live)):

```text
Project Touge\
├─ Project Touge.exe
├─ README.txt
├─ Shared\        what you share; Inbox\ for files from friends
└─ Data\          settings, tunes, routes, runs, logs
```

**New**
- Setups window: a **Presets** tab lists your own presets and gearing profiles with what each one covers, and lets you apply, rename, duplicate, share and delete them (with undo). Built-in presets, diff characters and gearing profiles are listed too and can be duplicated as your own.
- **Save current as preset** lets you choose which parts it covers (chassis, diff, gears). Applying a partial preset changes only those parts.
- Settings · Data: **Old run files** shows the size of the Touge 0.12 run folder (`Data\Legacy\Runs`) and removes it after you confirm.

**Changed**
- Tune: Gearing and Chassis show which tyres, engine, mass and front weight the model used. They turn yellow when the parts have changed since, and **Recalculate** runs the calculation again with the current parts.
- Calculations run on all processor cores: a full optimisation takes about a quarter of the time (22.5 s → 5.8 s on 4 cores), with the same result.
- Run analysis is about three times faster (94 runs: 40 s instead of 117 s), and the analysis folder is a third smaller.
- The page starts faster, settings are saved per key, and the game timer runs inside Touge without its own network ports (8766 and 30777 are no longer used).
- Map matching fits itself to each run, so split points land closer to where you passed them. The screen reader asks Windows for the colour format it expects.

**Fixed**
- Gears and chassis no longer keep stale values without telling after a tyre, engine or parts change.
- Done in input mode no longer says "Saving failed" after switching to a car with no own build (since 0.12.1).
- Picking a car right after start, two quick Game physics runs, the leaderboard progress chart, routes saved only in the browser, route editor Delete, Esc zoom reset, runs that failed to load and Analyse on a run with no corners.

## 0.15.3 beta (2026-11-21)

- **Drive on one screen:** the clock and its splits, the route map with named split points and your latest runs, and the readiness check sit side by side, so Start is in view without scrolling.
- **Session row** on Drive and Analyse: route, what you race against (your record with this car, the route record, your median or the model), car and setup, record, median and number of runs.
- **During a run** the big gap follows the car between splits and the map shows you and your opponent. **Abort** can be undone for 10 seconds; an aborted run never becomes a record.
- **Result card** after the finish: time, gap to record and median, each split's gain or loss, and Analyse this run, Drive again and **Discard run**.
- **Routes** in three columns: a searchable, filtered route list with game routes grouped by type; the route with Drive, Analyse, Edit, Share and Delete; and its splits, ghosts and start and finish images. Long sections get a note, and **Suggest** shows extra split points.
- **Analyse:** one corner table with tabs (Practice, This run, All corners, Splits, Model and game, Leaderboard; the leaderboard moved here from Drive), a right column with the verdict, Next, the losses and Target, comparison charts on one distance axis under the corner strip, and hover and zoom that link the charts and the map. Median is a new comparison option.
- Header: the slogan is gone and the version tag sits where the FI/EN switch was (language is in Settings · General).
- Fixed: own routes' split distances after editing, finish times faster than 250 km/h on average no longer become records, and aborted runs get the car of the runs around them.

## 0.15.2 beta (2026-11-20)

- Top bar: **New build** takes the place of the model reference time, and Save is a disk icon that turns yellow when something is not saved.
- Tune · Adjust: the tabs and Advice for this build are back on their own rows. On a wide window Time's map and speed chart grow with it.
- Fixed: "No changes yet" after the first save, a leftover "1 unsaved change" after saving during a calculation, cut-off values in the change list, and sliders that froze when a calculation stopped answering (it is now restarted after 90 seconds).

## 0.15.1 beta (2026-11-20)

- **Real-time sliders:** while you drag a chassis, diff, Other or engine slider, its value and the panel around it follow the drag; nothing is saved or added to undo until you let go. The final drive slider redraws the sawtooth and tractive force as you drag.
- **No redraws:** letting go updates the panels in place, and a new result appears about five times faster because only the page you look at is redrawn.
- **Every slider the same:** Tab, arrows, Shift + arrow, Home, End and Enter; a yellow dot and the difference to the saved value, click it to go back; the mouse wheel only after a click.
- **Change list:** the top bar keeps your setup's name with the number of unsaved changes; click it for saved → now with the game's names, each line with its own revert.
- **My view:** your own sliders and monitors in one place, the same for every car.
- **Wide screens and Compact density:** the page grows to about 2400 px, Chassis sliders flow in two columns from 1700 px, and Compact fits more sliders.
- Tune · Chassis: the three balance meters are one chart on a shared Front–Rear axis. One chart style, one icon set, and short motion that tells what changed (left out with Animations: Reduced).

## 0.15.0 beta (2026-11-20)

- **Ready to time?** Drive checks the game timer, screen reader, window mode, controller, disk space and the game file before you start, with a button for each row that needs work.
- **Next step:** a slim bar under the tabs says what to do next in the loop Build, Tune, Drive and Analyse.
- **Where this run lost time:** Analyse names the two corners where your latest run lost most and why, with one click to the matching symptoms on Tune.
- **What changed between A and B:** the run comparison lists the game values that differ between the two runs' setups.
- **choriso's reference run** (6:07.36, RX-7 FD) comes with Touge as a ghost on North Touge v2.
- **What's new** opens once after an update. **Report a problem** saves a diagnostics file and opens a GitHub issue.
- **Shorter share codes** (`TOUGE2:`, about 1 100 characters for a tune). 0.13.0 and older cannot read them.
- Narrow window support (about 480 px beside the game), shared start and finish markers on every map, and a skip link and larger targets for the keyboard.

## 0.13.0 beta (2026-11-19)

- **A tidy folder:** the Project Touge folder now holds only the program, the README, `Shared` (what you export or get from friends) and `Data` (everything Touge keeps for itself). Files have English names, the loose settings files are one `settings.json`, and each route keeps its runs and analysis in one folder. The first start moves your old files into `Data`, lists every move in `Data\Logs\migration.txt` and deletes nothing. An older version cannot read the new folder.
- **Lighter while you drive:** the main window no longer redraws its timer on every display frame when the game is the active window, and the screen reader runs just above normal priority instead of the highest one.
- **Less clutter over time:** a dated copy of your tunes only when they changed (one per day, 14 days), very short unfinished runs are not stored and other unfinished runs are removed after 14 days. Finished runs are always kept.
- **Preview versions:** About > **Offer preview versions too**. New versions are released as a preview first.
- The Tuning Guide files left the folder: the guide is inside the program and on the guide pages.
- Tune · Chassis: Preset mix is a row of blocks in 10 % steps; preset pickers look the same everywhere.
- Fixed: brake balance fallback in Game physics, "has to close" dialogs from a caught analysis error, a deleted calibration coming back, exe file version.

## 0.12.2 beta (2026-11-19)

- **Easier to read:** text is in IBM Plex Sans and numbers, units and value columns in Plex Mono. Grey filled buttons, selects and panels are gone, and secondary actions are plain links.
- **Things where you look for them:** chassis stiffness sits under Preset mix, Play and Compact on the situation timeline, Import and Share and import under Save as, the stopwatch and manual entry under Import, timing Settings inside the timer section, and Refresh and Open report under Target. Splits come before Ghosts, and the Overview's share, read and copy actions sit above the page navigation.
- **Setup card:** shows class, engine, gearbox, weight, route, best run and whether the setup is modified, with Open as the main action.
- **Clearer wording:** Enter pre-existing build, Changed / Show all, Average of last 5, and the controller actions listed as key chips. Changes to try now shows in every mode, so the Try changes link is gone.
- **Steadier turning data from the timer:** the minimap rotation is now measured on the inner part of the map. A tilted minimap was read about 15 % low before (measured on circle runs in the game). Run analysis corrects older runs too, so turning rates and lateral g in run analysis are about 15 % higher than before on a tilted minimap (◐).
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
