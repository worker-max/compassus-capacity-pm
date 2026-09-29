#!/usr/bin/env bash
# Download a Drive demo recording and prepare it: audio, background transcription, frame samples,
# de-duplicated screen candidates and contact sheets.
#   prepare.sh <drive_file_id> <workdir>
# The Drive file must be shared "anyone with the link" while this runs (ask the owner; remind them
# to restrict it again afterwards).
set -euo pipefail
ID="$1"; W="$2"; HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$W" && cd "$W"
pip install -q imageio-ffmpeg faster-whisper imagehash pillow pypdf cffi pymupdf pypdfium2 2>/dev/null || true
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
if [ ! -s demo.mp4 ]; then
  curl -sS -L --retry 4 "https://drive.usercontent.google.com/download?id=${ID}&export=download&confirm=t" -o demo.mp4
fi
if ! file demo.mp4 | grep -q "ISO Media"; then
  echo "NOT A VIDEO: the Drive link is probably not shared. Ask the owner to set 'Anyone with the link'." >&2; exit 2
fi
"$FF" -hide_banner -i demo.mp4 2>&1 | grep -E "Duration|Stream" || true
"$FF" -hide_banner -loglevel error -y -i demo.mp4 -vn -ac 1 -ar 16000 audio.wav
nohup python3 "$HERE/transcribe.py" > transcribe.log 2>&1 &
mkdir -p samp
"$FF" -hide_banner -loglevel error -threads 1 -i demo.mp4 -vf "fps=1/3,scale=480:-1" -q:v 4 samp/%05d.jpg
python3 "$HERE/dedupe.py"
python3 "$HERE/sheets.py"
echo "Contact sheets in $W/sheets/. Transcription running (tail $W/transcribe.log; done when it prints 'done')."
