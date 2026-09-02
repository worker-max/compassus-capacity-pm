# -*- coding: utf-8 -*-
"""Export the reviewed content to JSON so the Word build reads the same source as the HTML."""
import json
import pathlib

from review_content import (FRAMING, LEVERS, FUTURE, DATA, FUTURE_DATA, CLOSING)

payload = {
    "framing": FRAMING,
    "levers": [
        {
            "id": l["id"],
            "name": l["name"],
            "def": l["def"],
            "points": [{"kind": k, "text": t} for k, t in l["points"]],
        }
        for l in LEVERS
    ],
    "future": FUTURE,
    "data": DATA,
    "futureData": FUTURE_DATA,
    "closing": CLOSING,
}

out = pathlib.Path("content.json")
out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
print("exported", len(payload["levers"]), "levers,",
      len(payload["data"]) + len(payload["futureData"]), "data groups")
