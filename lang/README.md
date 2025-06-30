# Gordon's Sun Clock

The German language file ("de.json") is THE ORIGINAL LANGUAGE. It is best to start a translation from German (if possible). 

The English language is the fallback language, if the local language is not available in the "lang" directory. Thus this programme will not run (as intended) without the "de.json" (and "en.json") file.


If you create new translations, please leave all the control codes unchanged: 

- [XXXXXX] are variables that will be replaced
- [-LF-] are linefeeds (as in "\n"). If you replace them while working on the language, replace them back when you are finished.
- [DF] are control codes for distance in the design


Some remarks about the entries in the local language dictionary:

- "quotes" are the local quotes, as in: „Hello“ or «Hello»

In addition, you will find entries that help the programme to separate words correctly in order to insert line breaks in the UI. These are listed below. If you don't know what to enter, just leave them blank.

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
        "nb"
    ],
    "graph_separateafter": [],



