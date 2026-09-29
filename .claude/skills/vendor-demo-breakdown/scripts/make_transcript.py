# transcript.jsonl -> transcript.md (paragraphs of ~1 min, bulk mis-hearing fixes).
#   make_transcript.py <workdir> <out.md> "<Vendor>" "<date, time>" "<h:mm:ss length>" "<Drive file title>"
import json, re, sys
W, OUT, VENDOR, DATE, LEN, SRC = sys.argv[1:7]
FIX = [(r"[Hh]ome ?[Cc]are[ -][Hh]ome[ -]?[Bb]a(se|sed|ys|sis)\b", "HomeCare HomeBase"),
       (r"\block ?ship", "log ship"), (r"\blupas?\b", "LUPA"), (r"\bsocks\b", "SOCs"),
       (r"[Cc]ompass(es|ive)\b", "Compassus"), (r"\bSIP code", "ZIP code"), (r"point care|Point Care", "PointCare")]
L = [json.loads(l) for l in open(W + "/transcript.jsonl")]
out = [f"# {VENDOR} demo — full transcript", "",
       f"**Meeting:** Compassus Home Health Capacity & Scheduling — {VENDOR} vendor demo  ",
       f"**Date:** {DATE} (recording length {LEN})  ", f"**Source:** Teams recording, Drive file `{SRC}`", "",
       "> Machine transcript (Whisper small.en, CPU) with no speaker labels. Common mis-hearings were corrected "
       "in bulk; names and some words may still be wrong. Timestamps are `h:mm:ss` into the recording and match "
       "the screen filenames in `screens/` (HHMMSS).", ""]
buf, t0 = [], None
def flush():
    global buf, t0
    if buf:
        t = int(t0); txt = " ".join(buf)
        for a, b in FIX: txt = re.sub(a, b, txt)
        out.append(f"**[{t//3600}:{t%3600//60:02d}:{t%60:02d}]** {txt}\n")
    buf, t0 = [], None
for s in L:
    if t0 is None: t0 = s["start"]
    buf.append(s["text"])
    if s["start"] - t0 > 55 and s["text"].rstrip()[-1:] in ".?!": flush()
flush()
open(OUT, "w").write("\n".join(out))
