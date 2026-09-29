# Machine transcript of audio.wav (cwd) -> transcript.jsonl. ~35-40 min per 2 h on 4 CPUs.
from faster_whisper import WhisperModel
import json
m = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=3)
segs, info = m.transcribe("audio.wav", vad_filter=True, beam_size=1, condition_on_previous_text=False)
out = open("transcript.jsonl", "w")
for s in segs:
    out.write(json.dumps({"start": round(s.start, 1), "end": round(s.end, 1), "text": s.text.strip()}) + "\n")
    out.flush()
print("done")
