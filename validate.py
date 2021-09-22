#!/usr/bin/env python
"""
Simple validation for the sections.json file.
-> Make sure it is valid JSON
-> Make sure we have at least one instrument
"""

import os
import sys
import json

defns = {}
def reverse_mapping_for_section(section):
    return { x["name"]: {"section" : section["SECTION"], "title": section["TITLE"], "pv": x["name"]} for x in section["PARAMS"] }
with open("sections.json", 'r') as f:
    isdefs = json.load(f)
    for instrument, sections in isdefs.items():
        defns[instrument] = {}
        for section in sections:
            defns[instrument].update(reverse_mapping_for_section(section))
    if len(defns) < 2:
        print("We should have at least one instrument")
        sys.exit(-1)
