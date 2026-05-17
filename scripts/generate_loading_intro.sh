#!/usr/bin/env bash
set -euo pipefail

mkdir -p assets/video

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "Error: ffmpeg is required to generate assets/video/loading_intro.mp4" >&2
  exit 1
fi

ffmpeg -y \
  -f lavfi -i color=c=black:s=1920x1080:d=30:r=30 \
  -vf "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='ROOKIE QUEST: RINGMASTER':fontcolor=white:fontsize=76:x=(w-text_w)/2:y=h*0.35:enable='between(t,0.5,6)',drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='Every decision writes history':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=h*0.55:enable='between(t,4,10)',drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='Build stars. Survive chaos. Own the business.':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=h*0.62:enable='between(t,12,21)',drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='Loading Universe...':fontcolor=white:fontsize=58:x=(w-text_w)/2:y=h*0.78:enable='between(t,24,30)'" \
  -c:v libx264 -pix_fmt yuv420p -movflags +faststart assets/video/loading_intro.mp4

echo "Generated assets/video/loading_intro.mp4"
