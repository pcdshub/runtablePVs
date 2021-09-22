#!/usr/bin/env python
"""
Use an API call to update the logbook caches for the sections.json file
Use a conda environment that contains krtc; for example, the controls conda environment.
"""

import os
import sys
import json
import requests

from krtc import KerberosTicket

krbheaders = KerberosTicket("HTTP@pswww.slac.stanford.edu").getAuthHeaders()
resp = requests.get("https://pswww.slac.stanford.edu/ws-kerb/lgbk/lgbk/ws/reload_named_cache?cache_name=instrument_scientists_run_table_defintions", headers=krbheaders)
resp.raise_for_status()
print("Done")

