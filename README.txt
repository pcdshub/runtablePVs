The file sections.json here is used in the logbook to generate the combobox dropdowns for the user run tables.
Please edit with care; always check that this is valid json
The location of this file is picked up from the environment variable RUNTABLE_SECTIONS_JSON

This JSON is a dict of instrument (for example, "AMO") pointing to an array of dict's; each of which has "TITLE", "SECTION" and "PARAMS".
-->  "TITLE" and "SECTION" are strings.
-->  "PARAMS" is in turn an array of dicts with "name" and "descr" string attributes
