# Project Touge 峠

**Build, tune and improve your driving. One gutter away from being the fastest on the touge.**

Project Touge is a companion app for CarX Street on Windows. It helps you build a car for a class, tune its setup from what you feel on the road, and time your runs with splits and telemetry.

> Project Touge is an unofficial fan-made tool. It is not a CarX Technologies product and is not affiliated with or endorsed by them. It never reads, changes or injects anything into the game: time and telemetry are read from the screen, the same way you see them.

## Download

Get the latest zip from **[Releases](../../releases/latest)**.

1. Unzip the **Project Touge** folder anywhere you like, for example Documents or a game drive. Keep the folder together.
2. Double-click **Project Touge.exe**. Touge opens in its own window.
3. Close the window to quit.

No installation and no Python needed. 
Requires Windows 10 or 11 with Microsoft Edge WebView2 (built into Windows 11 and every up-to-date Windows 10). If SmartScreen warns about an unknown publisher, choose **More info → Run anyway**.

## What it does

- **Build**: enter your car from screenshots or start from the model: engine, gearbox and diff, aero and body, suspension, tyres and route model. Values use the game's own names, order and units so you can type them straight into the game.
- **Tune**: pick a symptom, adjust, check the effect, then copy the setup to the game. Each change explains why it helps.
- **Time**: timing with splits, telemetry and run analysis. Speed, gear and minimap are read from the screen; controller buttons work while the game is focused.

Values come from the game's own data and are checked in game. Anything not yet verified is marked as an estimate.

## Timing and telemetry

- Run the game borderless or full screen. A window works if the whole HUD is visible.
- Tested resolutions: 3440×1440 (recommended), 2560×1440, 2560×1080, 1920×1440 and 1920×1080.
- Open the **Time** tab, pick a route and press **Start**. Touge finds the speedometer, gear display and minimap by itself on the first run.

## Your data

Everything you save stays inside the Project Touge folder:

| Folder | Contents |
|---|---|
| `Tunes` | setups, presets, notes, route calibrations and settings |
| `Runs` | timed runs and their telemetry |
| `Routes` | your own routes |
| `Logs` | program logs; attach these when reporting a problem |

**Update:** replace `App` and `Project Touge.exe`, keep your data folders.
**Move:** copy the whole folder. 
**Uninstall:** delete the folder.

## Feedback

Found a bug or a value that is off in game? Open an [issue](../../issues) with your Touge version (shown in the header), what you did, and the files from `Logs`.

## Licence

© aaturaty. All rights reserved. You may download and use Project Touge for free; please do not redistribute it or its code as your own.
Game images and data are © CarX Technologies and included with their permission to the Project Touge community. Third-party fonts and libraries are listed in `Licenses.txt` inside the download.

