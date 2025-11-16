# Gordon's Sun Clock - Translation Guide

## Language Files

The **German language file** (`de.json`) is the original source language. It is recommended to start translations from German if possible.

**English** serves as the fallback language and will be used whenever a language or translation entry is missing.

---

## Types of Language Support

Sun Clock provides three types of language support:

### (a) Fully Supported Languages
All entries are translated, including:
- Settings page (UI elements, buttons, labels, explanations)
- Data overview page (explanations and legend)
- Tutorial pages ("How to read the dial", conceptual explanations)
- About page

**Currently fully supported:** English (en), Deutsch (de), Español (es), Français (fr), Русский (ru), 中文 (zh)

### (b) Partially Supported Languages
Translations include all entries up to `"txlegende"` in the language file. This covers:
- **Settings page:** UI elements, buttons, labels, and explanations
- **Data overview page:** Including explanations and legend

**Not translated** (defaults to English):
- Tutorial pages
- About page

### (c) Minimally Supported Languages
At least all labels of the settings page are translated (all entries up to `"txpartsupport"` in the language file).

---

### Language Support Goals

My long-term goal is to provide **full support** only for the most widely used languages (roughly the global top ten: ✓English, ✓Simplified Chinese, ✓Spanish, Hindi, Arabic, ✓French, Bengali, Portuguese, ✓Russian, Indonesian, ✓German). Maintaining a larger number of fully translated languages would create more ongoing work than I can realistically support.

Full translations require significant effort, not only for the initial translation but also for ongoing maintenance as new features and content are added. **Contributions are always welcome!**

---

## Translation Guidelines

When translating, please **keep all control codes unchanged**:

- `[XXXXXX]` and `{xxxxxx}` are variables that will be replaced by the program
- `[~LF]` represents line breaks (like `\n`). You can replace them with actual line breaks if needed
- `[NDASH]` is the en dash character (–)
- `[DF]` and `[SP]` are control codes for design layout

---

## Plural Rules for "Day(s)"

Some languages use different words for "day" depending on the number (e.g., 1 day, 2 days). The entry `"xxdays"` defines these forms. Use `{day}` where the number should appear.

### Examples

**Chinese** (minimal working example):
```json
"xxdays": {
    "*": "{day} 天"
}
```

**Russian**:
```json
"xxdays": {
    "1": "{day} день",
    "2-4": "{day} дня",
    ".": "{day} дня",
    "*": "{day} дней"
}
```

### Key Meanings
- `"1"` → applies when the number is exactly 1 (e.g., `1` → `{day} day`)
- `"2-4"` → applies for whole numbers from 2 to 4 inclusive (e.g., `2`, `3`, `4`)
- `"."` → applies to decimal numbers (e.g., `1.5`, `2.7`)
- `"*"` → fallback for all other cases **(mandatory)**

---

## Dictionary Entries

### Quotation Marks
The `"quotes"` entry defines the local quotation marks used in your language:
- German: „Hello"
- French: «Hello»
- English: 'Hello'

### Word Separation Rules

The language dictionary contains entries to help with correct word separation in your language. **If you're unsure what to enter, leave them empty `[]`.**

Example entries:
```json
"char_vowels": "aeiouyäöüáéíóúÄÖÜÁÉÍÓÚ",
"char_consonants": "bcdfghjklmnpqrstvwxyzñÑ",
"char_splitafter": ".,;:!?"'"-—)]}%&*+=/\\|>@#_×÷≈≠≤≥°¶•…"'»`",
"char_splitbefore": "„‚([{<$~^€£¥±©®™§†‡""'«¿¡",
"graph_dontseparatebetween": [
    "sch",
    "ch",
    "ck",
    "tz",
    "pf",
    "qu"
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
    "nü"
],
"graph_dontseparateafter": [
    "nb"
],
"graph_separateafter": []
```

---

## Contributing

If you'd like to contribute a translation:

1. Copy one of the existing language files, preferably `de.json` or `en.json`, as a starting point
2. Rename it to your language code (e.g., `hi.json` for Hindi)
3. Translate all string values while keeping control codes intact. The most important entries are at the beginning
4. Submit your translation via pull request or email (see last page of the app)

Or correct an existing translation:

1. Copy the language file you want to improve
2. Keep only the entries you wish to change – delete all other entries
3. Make your corrections while preserving the original tone and keeping control codes intact
4. Submit your corrections via email (see last page of the app) or pull request

**Important notes:**
- Preserve all control codes (e.g., `[~LF]` for line breaks, `[DF]` for spacing, `[b]...[/b]` for bold text)
- Maintain the original tone: informative, personal, and approachable
- For partial contributions, only include the entries you've modified – this makes merging easier

Thank you for helping make Gordon's Sun Clock accessible to more people!