# Summarize vendor-demos/variable-coverage-by-vendor.csv (S = shown, D = discussed, - = not covered).
# To add a vendor: append a column to the CSV, score all 79 rows from the transcript, rerun.
#   coverage.py <csv>
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1])))
vendors = [c for c in rows[0] if c not in ("ID", "Category", "Variable", "MVP")]
for cat in ["Capacity", "Scheduling", "Engagement", None]:
    rs = [r for r in rows if cat is None or r["Category"] == cat]
    for label, sub in [(cat or "TOTAL", rs), ("  MVP", [r for r in rs if r["MVP"] == "Yes"])]:
        n = len(sub)
        print(f"{label:11} n={n:2} " + " | ".join(
            f"{v}: spoken {round(100*sum(r[v]!='-' for r in sub)/n)}% shown {round(100*sum(r[v]=='S' for r in sub)/n)}%"
            for v in vendors))
never = [r["ID"] + " " + r["Variable"] for r in rows if all(r[v] == "-" for v in vendors)]
print("Not covered by any vendor:", never)
