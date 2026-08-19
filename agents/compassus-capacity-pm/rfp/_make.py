# -*- coding: utf-8 -*-
"""Driver — assembles both workbooks."""
from openpyxl import Workbook
import _build_workbook as B

try:
    import _overview as OV
except ImportError:
    OV = None


def build(vendor_facing):
    wb = Workbook()
    wb.remove(wb.active)
    instr = B.build_instructions(wb, vendor_facing)
    qs, answer_rows = B.build_questionnaire(wb)
    B.set_progress(instr, answer_rows)
    if OV:
        OV.build_overview(wb)
    B.add_lists(wb)
    B.attach_status_validation(qs, getattr(qs, "_status_rows", []))
    B.protect(qs)

    if not vendor_facing:
        exp, exp_rows = B.build_expanded(wb)
        B.attach_status_validation(exp, exp_rows)
        B.build_additional(wb)
        B.build_vetting(wb)
    B.build_meta(wb, "vendor" if vendor_facing else "internal")

    name = ("Compassus-Vendor-Questionnaire.xlsx" if vendor_facing
            else "Compassus-Vendor-Questionnaire-MASTER.xlsx")
    wb.save(name)
    print(f"wrote {name}  sheets={[w.title for w in wb.worksheets]}")
    return name


if __name__ == "__main__":
    build(True)
    build(False)
