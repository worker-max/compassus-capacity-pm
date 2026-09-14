# Vendor research dossiers

One file per vendor, in the template from `../handoff/10-VENDOR-RESEARCH-BRIEF.md`. Public sources
only; every fact dated and sourced; *not found* is written, never inferred; a source behind a login
or a paywall is written as **gated**, not as not found.

Starting a new research session? Read `00-SESSION-HANDOFF.md` first, then `00-ROSTER.md`.

**Never research a vendor that does not have a row in `00-ROSTER.md`.** The roster fixes the slug
and pins the legal entity before anyone spends an hour on the wrong company.

| File | What it is |
|---|---|
| `00-ROSTER.md` | The vendor list, the fixed slugs, the identity pins, and the names that are *not* these vendors |
| `00-SESSION-HANDOFF.md` | State of play and the first job for the next session |
| `<slug>.md` | One dossier per vendor. Each opens with an `## At a glance` block of twenty-six facts, which `../_research-matrix.gen.py` reads to build the matrix |
| `00-FIELD-NOTES.md` | **Generated.** One line per vendor, the commonplaces, where the field splits. Rebuild it; do not hand-edit |
