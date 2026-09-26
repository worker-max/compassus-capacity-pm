# Pull full-resolution frames for chosen keep.json indices and crop to the shared window.
#   extract_screens.py <workdir> <outdir> <crop> <idx> [idx ...]
# crop: "auto"   -> detect the browser's light area below the top black bar (works for most Teams shares)
#       "x0,y0,x1,y1" -> fixed crop box in 1920x1080 pixels (measure one frame first; e.g. 0,18,1674,1048
#                        removed the participant strip on the right in the Axle recording)
# Files are named HHMMSS.jpg (time into the recording) so captions and transcript line up.
import json, subprocess, sys, os
from PIL import Image
import numpy as np, imageio_ffmpeg
W, OUT, CROP = sys.argv[1], sys.argv[2], sys.argv[3]
idx = [int(x) for x in sys.argv[4:]]
FF = imageio_ffmpeg.get_ffmpeg_exe()
k = json.load(open(os.path.join(W, "keep.json")))
os.makedirs(OUT, exist_ok=True)
for i in idx:
    t = k[i]["t"] + 1
    raw = os.path.join(W, "raw.png")
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-ss", str(t), "-i",
                    os.path.join(W, "demo.mp4"), "-frames:v", "1", raw], check=True)
    im = Image.open(raw).convert("RGB")
    if CROP == "auto":
        a = np.asarray(im).astype(int)
        col = a[:, 300].sum(1)
        light = [y for y in range(20, 300) if col[y] > 600]
        top = light[0] if light else 60
        im = im.crop((0, top + 72, 1672, min(1080, top + 72 + 830)))   # skip tab + URL bar, keep app
    else:
        im = im.crop(tuple(int(v) for v in CROP.split(",")))
    im.thumbnail((1600, 1600))
    im.save(os.path.join(OUT, "%02d%02d%02d.jpg" % (t // 3600, t % 3600 // 60, t % 60)), quality=82, optimize=True)
os.remove(os.path.join(W, "raw.png"))
print(len(idx), "screens ->", OUT)
