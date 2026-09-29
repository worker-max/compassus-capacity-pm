# Group 3-second samples (samp/) into runs of the same screen; keep one frame per run -> keep.json
import imagehash,os,json
from PIL import Image
fs=sorted(os.listdir("samp"))
H=[imagehash.dhash(Image.open("samp/"+f),hash_size=16) for f in fs]
# segment into runs of similar frames; keep the middle of each run lasting >=2 samples
runs=[];start=0
for i in range(1,len(H)+1):
    if i==len(H) or H[i]-H[start]>18:
        runs.append((start,i-1)); start=i
keep=[]
for a,b in runs:
    if b-a>=1:
        m=(a+b)//2
        if not keep or H[m]-H[keep[-1]["i"]]>12:
            keep.append({"i":m,"t":m*3,"from":a*3,"to":b*3+3,"f":fs[m]})
json.dump(keep,open("keep.json","w"))
print(len(runs),len(keep))
