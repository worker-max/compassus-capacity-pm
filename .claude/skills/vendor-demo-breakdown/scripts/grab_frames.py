# Extract full-resolution frames with named crops (measured on a 1920x1080 Teams recording of a Mac screen share).
#   grab_frames.py <workdir with demo.mp4 and picks.txt> <outdir>
# picks.txt lines: 'h:mm:ss kind [x0,y0,x1,y1]'; kind = app | phone | slide. The optional box adds a 1.6x zoomed '-d' crop.
# app drops browser chrome, dock and the participant strip; phone crops a mirrored iPhone; slide trims black borders.
import subprocess, sys, os
from PIL import Image
import numpy as np, imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe(); W, OUT = sys.argv[1], sys.argv[2]; os.chdir(W)
CROPS={"app":(0,162,1668,1010),"phone":(584,0,1090,1080),"full":(0,0,1670,1080)}
def ts(s):
    h,m,x=[int(v) for v in s.split(":")]; return h*3600+m*60+x
def trim(im):
    a=np.asarray(im.convert("L")).astype(int)
    rows=np.where(a.mean(1)>14)[0]; cols=np.where(a.mean(0)>14)[0]
    return im.crop((cols[0],rows[0],cols[-1]+1,rows[-1]+1))
L=[l.split() for l in open("picks.txt") if l.strip() and not l.startswith("#")]
for p in L:
    t,kind=p[0],p[1]; s=ts(t)
    raw="raw.png"
    subprocess.run([FF,"-hide_banner","-loglevel","error","-y","-ss",str(s),"-i","demo.mp4","-frames:v","1",raw],check=True)
    im=Image.open(raw).convert("RGB")
    name="%02d%02d%02d"%(s//3600,s%3600//60,s%60)
    if kind=="slide": out=trim(im.crop(CROPS["full"]))
    else: out=im.crop(CROPS[kind])
    out.save(os.path.join(OUT,name+".jpg"),quality=90,optimize=True)
    # optional detail crop: x0,y0,x1,y1 in full-frame coords, upscaled 1.6x
    if len(p)>2:
        box=tuple(int(v) for v in p[2].split(","))
        d=im.crop(box); d=d.resize((int(d.width*1.6),int(d.height*1.6)),Image.LANCZOS)
        d.save(os.path.join(OUT,name+"-d.jpg"),quality=90,optimize=True)
print(len(L),"frames")
