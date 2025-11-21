#!/usr/bin/env python3
import json
import os
import shutil
from copy import deepcopy
from textwrap import shorten

hasdiff=False # sic(!)

# === Konfiguration (fest) ===
defaultlang = 'de'
langdir = './lang'
print()

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def flatten(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

def pretty_val(v, maxlen=112):
    s = repr(v)
    return shorten(s, width=maxlen, placeholder='...')

def compare_and_print(src_path, old_path, lcode):
    global hasdiff, langnr

    langnr+=1

    if not os.path.exists(src_path):
        hasdiff=True
        print(f"ERROR: Source file not found: {src_path}")
        print()
        return

    if not os.path.exists(old_path):
        shutil.copy2(src_path, old_path)
        print(f"Info: '{old_path}' nicht gefunden. Eine Kopie von '{src_path}' wurde angelegt.")
        return

    src = load_json(src_path)
    old = load_json(old_path)

    src_flat = flatten(src)
    old_flat = flatten(old)

    src_keys = set(src_flat.keys())
    old_keys = set(old_flat.keys())

    added = sorted(src_keys - old_keys)
    removed = sorted(old_keys - src_keys)
    possibly_changed = sorted(src_keys & old_keys)

    changed = [k for k in possibly_changed if old_flat.get(k) != src_flat.get(k)]

    print(f"=== Vergleich: {langnr}:{lcode} ===") # {old_path}  <->  {src_path}
    print(f"Gesamt Keys (alt): {len(old_keys)}   (neu): {len(src_keys)}")
    print(f"Neu: {len(added)}   Geändert: {len(changed)}   Gelöscht: {len(removed)}")

    einruecken="   "

    if added:
        print(">>> NEU (vorher nicht vorhanden):")
        for k in added:
            print(f"{einruecken} + {k}  -> {pretty_val(src_flat[k])}")
        print()
        hasdiff=True

    if changed:
        print(">>> GEÄNDERT (alte -> neue Werte):")
        for k in changed:
            oldv = pretty_val(old_flat.get(k))
            newv = pretty_val(src_flat.get(k))
            print(f"{einruecken} * {k}")
            print(f"{einruecken}     old: {oldv}")
            print(f"{einruecken}     new: {newv}")
        print()
        hasdiff=True

    if removed:
        print(">>> GELÖSCHT (in alt vorhanden, in neu entfernt):")
        for k in removed:
            print(f"{einruecken} - {k}  -> {pretty_val(old_flat[k])}")
        print()
        hasdiff=True

    if not (added or changed or removed): 
        # print("Keine Unterschiede gefunden. (Dateien inhaltlich identisch)")
        print()

def main():
    global langnr
    langnr=1
    # langdir & defaultlang are globalvars
    src_file = os.path.join(langdir, f'{defaultlang}.json')

    for fn in os.listdir(langdir):
        if not fn.endswith(".json"):
            continue
        code = fn[:-5]
        if code == defaultlang:
            continue

        cmp_file = os.path.join(langdir, f'{defaultlang}.CMP_{code}-json')
        compare_and_print(src_file, cmp_file, code)

    if hasdiff:
        print("======================================================================")
        print("=== ACHTUNG: Fehlende Übersetzungen! NICHT ZUR PRODUKTION FREIGEBEN! ")
        print("======================================================================")
        print()

# if __name__ == '__main__':
main()



