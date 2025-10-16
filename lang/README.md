# Gordon's Sun Clock

The German language file ("de.json") IS THE ORIGINAL LANGUAGE. It is best to start a translation from German (if possible). English is the fallback language, that will be chosen if your local translation does not exist. 

When translating, please keep all control codes unchanged: 

- [XXXXXX] and {xxxxxx} are variables that will be replaced during run time
- [-LF-] are linefeeds (as in "\n"). You can replace them with real linefeeds
- [DF] and [SP] are control codes for distances in the design


About entries in the local language dictionary:

- "quotes" define the local quotation marks (e.g., „Hello" or «Hello»)


The dictionary also contains entries to help with correct word separation in your language. If you're unsure what to enter, leave them empty "[]":

    "char_vowels": "aeiouyäöüáéíóúÄÖÜÁÉÍÓÚ",
    "char_consonants": "bcdfghjklmnpqrstvwxyzñÑ",
    "char_splitafter": ".,;:!?“‘”-—)]}%&*+=/\\|>@#_×÷≈≠≤≥°¶•…”’»`",
    "char_splitbefore": "„‚([{<$~^€£¥±©®™§†‡“”‘«¿¡",
    "graph_dontseparatebetween": [
        "sch",
        "ch",
        "ck",
        "tz",
        "pf",
        "qu",
    ],
    "graph_dontseparatebefore": [
        "nd",
        "hn",
        "rn",
        "rg",
        "nb",
        "sz",
        "sw",
        "rd",
        "lg",
        "nü",
    ],
    "graph_dontseparateafter": [
        "nb",
    ],
    "graph_separateafter": [],



