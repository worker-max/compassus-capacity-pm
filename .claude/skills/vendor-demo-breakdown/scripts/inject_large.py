# Insert (or refresh) reference/large-screens.css inside an index.html <style> block, between markers.
#   inject_large.py <index.html> [...]
import sys, re, os
css = open(os.path.join(os.path.dirname(__file__), "..", "reference", "large-screens.css")).read()
block = "/*LARGE-SCREENS*/\n" + css + "/*/LARGE-SCREENS*/\n"
for f in sys.argv[1:]:
    h = open(f).read()
    if "/*LARGE-SCREENS*/" in h:
        h = re.sub(r"/\*LARGE-SCREENS\*/.*?/\*/LARGE-SCREENS\*/\n", lambda m: block, h, flags=re.S)
    else:
        h = h.replace("</style>", block + "</style>", 1)
    open(f, "w").write(h); print("large screens ->", f)
