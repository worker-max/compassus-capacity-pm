# Split transcript.jsonl into two ~60k-char files (txA.txt, txB.txt) sized for reading in full.
import json, sys
W = sys.argv[1]
L = [json.loads(l) for l in open(W + "/transcript.jsonl")]
out, buf, t0 = [], "", None
for s in L:
    if t0 is None: t0 = s["start"]
    buf += " " + s["text"]
    if len(buf) > 700:
        t = int(t0); out.append(f"[{t//3600}:{t%3600//60:02d}:{t%60:02d}]" + buf); buf, t0 = "", None
out.append(buf); n = len(out) // 2
open(W + "/txA.txt", "w").write("\n".join(out[:n])); open(W + "/txB.txt", "w").write("\n".join(out[n:]))
