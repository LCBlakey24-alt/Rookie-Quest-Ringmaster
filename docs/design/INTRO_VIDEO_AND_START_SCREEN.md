# Intro Video + Start Screen Implementation

This repository now includes a practical starter for your requested flow:

1. "Rookie Quest Game Presents..."
2. Title/logo reveal
3. Start button to enter game

## Added Assets
- `assets/branding/ringmaster_logo.svg` — title/logo artwork.
- `ui/intro_screen.html` — interactive intro/start screen prototype.

## How to Preview
Open `ui/intro_screen.html` in a browser.

## Next Integration Step
When your engine shell exists (Unity/Godot/web), connect the Start button callback to your real scene loader.

## Video Version Notes
If you want a true rendered intro video next, we can produce:
- MP4 with fade-in title sequence
- logo reveal
- final frame with “Press Start”

and then play that video before showing this start screen.


## Added Navigation Prototype
- `ui/main_menu.html` has been added and `START GAME` now routes there from `ui/intro_screen.html`.

- `ui/select_brand.html` adds brand selection with region filters and selection persistence via `localStorage`.

- `ui/brand_creator.html` adds brand/show logo upload plus primary/secondary theme colors with live preview and local profile save.
- Brand creator now includes starting cash, weekly shows, and monthly PPV cadence controls with live overbooking penalty preview.
