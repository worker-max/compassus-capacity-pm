# Collision checklist — what actually goes wrong

Every one of these shipped broken at least once and was caught only by rendering the PNG and looking
at it. Run this list against the screenshot before you call a sheet done.

## Connectors

- [ ] **A drop line starting in mid-air.** A dashed line that begins below a block's sublist looks
      detached from it. Branch off the **connector between two blocks** (in the gap, `x = block_right
      + 14`) rather than from a block's underside — it reads as "the flow splits here" and never
      crosses a sublist.
- [ ] **A connector crossing a panel or a text block.** Route around: down the outside of the band
      (`W-140`), or down the left margin (`BX-30`), then across.
- [ ] **An 8pt final segment.** A connector whose last leg is shorter than ~30pt renders an
      arrowhead pointing at nothing legible. Land on a block's **edge** with a real run-in, or enter
      its bottom at an x clear of its sublist text.
- [ ] **Two dashed verticals nearly collinear.** Separate them by at least 40pt or they read as one
      broken line.
- [ ] **A `Yes` / `No` label sitting on a block.** Anchor it away from the destination
      (`anchor="end"` on the left side, `"start"` on the right), or move it along the run.

## Text

- [ ] **Sublist overrunning its column.** At `.sub` 13.5px, budget ~6.7px per character. A 250-wide
      block holds ~36 characters. Longer items must be split or shortened.
- [ ] **A note line running past the band edge** into a neighbouring column's connector. Split it
      onto two lines rather than shrinking the type.
- [ ] **Block text leaving its box.** `block()` centres but does not wrap. Pass the line breaks
      yourself, and keep to ~26 characters per line at `.bt` 16px in a 250-wide block.
- [ ] **A badge colliding with an incoming connector.** Badges sit 14pt *above* the block's top edge;
      nothing else may occupy that strip.
- [ ] **Text fill overridden by a CSS class.** `fill="..."` on a `<text>` loses to the class rule —
      use `style="fill:..."`. This is why a white oval's label vanished once.

## Layout

- [ ] **A band with a long empty tail.** Size each band to its own content (`slots=`, `pad=`).
- [ ] **Content past the footer rule.** Print the last content y from the generator and compare it
      with `H-72`; leave 30–40pt of air.
- [ ] **A block running off the canvas** — check the right-most element against `W-50`.
- [ ] **Two exception blocks touching.** Keep 40pt between blocks in the same strip.
- [ ] **A legend colliding with the title** — start it past x≈1100, and wrap to two rows past five
      actors.

## Semantics — the ones a renderer can't catch

- [ ] **Is every purple block genuinely the system acting alone?** Most aren't.
- [ ] **Does an arrow between two blocks imply a sequence that doesn't exist?** If they're
      alternatives, use the `OR` divider (`breaks=`), not an arrow.
- [ ] **Does the main path land on the common case?** Routing the spine into an exception makes the
      exception look like the norm.
- [ ] **Is a dead end really a dead end?** The missed-visit oval was a terminus for months; it is
      actually a 48-hour compliance chain.
- [ ] **Does a badge or note contradict a corrected fact?** e.g. rapid reschedule belongs to
      clinicians moving their own visits, not to call-out coverage.

## Process

- [ ] Rendered the PNG and **actually opened it** — not just checked that the command succeeded.
- [ ] Cropped and re-read any region that was edited (`PIL` crop + `Read`).
- [ ] PDF is **one page**, and its MediaBox matches the canvas.
- [ ] Generator copied next to the sheet as `_<name>.gen.py`.
- [ ] Decision recorded in `flow-map-redraw-assessment.md`; durable facts in
      `knowledge/process-facts-2026-08.md`.
- [ ] Artifact **republished** after the last edit — a PDF refresh alone leaves the link stale.
