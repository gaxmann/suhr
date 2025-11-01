# Gordon's Sun Clock - Translation Guide

## Language Files

The German language file (`de.json`) is the **original language**. It is recommended to start translations from German if possible. 

English is the fallback language and will be used if your local translation does not exist.

---

## Translation Guidelines

When translating, please **keep all control codes unchanged**:

- `[XXXXXX]` and `{xxxxxx}` are variables that will be replaced at runtime
- `[:LF]` represents linefeeds (like `\n`). You can replace them with actual linefeeds if needed
- `[DF]` and `[SP]` are control codes for design layout

---

## Dictionary Entries

### Quotation Marks
The `"quotes"` entry defines the local quotation marks used in your language, e.g.:
- German: „Hello“  
- French: «Hello»
- English: ‘Hello’

### Word Separation Rules

The language dictionary contains entries to help with correct word separation in your language. If you're unsure what to enter, leave them empty `[]`.

Example entries:

```json
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
```

---

## Contributing

If you'd like to contribute a translation:

1. Copy one of the existing language files, preferrably `de.json` or `en.json`, as a starting point
2. Rename it to your language code (e.g., `hindi.json`)
3. Translate all string values while keeping control codes intact. The most important ones are at the beginning 
4. Submit your translation via pull request or email (see last page on app) 

Or correct an existing translation:
1. Copy the language file you want to improve
2. Keep only the entries you wish to change – delete all other entries
3. Make your corrections while preserving the original tone and keeping control codes intact
4. Submit your corrections via email (see last page on app) or pull request 

Thank you for helping make Gordon's Sun Clock accessible to more people!
