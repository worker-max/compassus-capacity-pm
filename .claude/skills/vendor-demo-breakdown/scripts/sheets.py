# 4x4 contact sheets of keep.json candidates -> sheets/sNN.jpg, labelled #index h:mm:ss. Read these to pick screens.
import json
from PIL import Image,ImageDraw
k=json.load(open("keep.json"));mkdir=__import__("os").makedirs;mkdir("sheets",exist_ok=True)
W,Hh=480,270;C=4;R=4
for s in range(0,len(k),C*R):
    im=Image.new("RGB",(W*C,(Hh+22)*R),"white");d=ImageDraw.Draw(im)
    for j,x in enumerate(k[s:s+C*R]):
        c,r=j%C,j//C;t=x["t"]
        im.paste(Image.open("samp/"+x["f"]).resize((W,Hh)),(c*W,r*(Hh+22)+22))
        d.text((c*W+4,r*(Hh+22)+5),f"#{s+j} {t//3600}:{t%3600//60:02d}:{t%60:02d} (hold {x['to']-x['from']}s)",fill="black")
    im.save(f"sheets/s{s//16:02d}.jpg",quality=80)
