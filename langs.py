## Gordon Sonnenuhr 
##
# langs.py
# 
# define('MISL', '–'); // en dash - Halbgeviertstrich
# define('MISXL', '—'); // em dash - Geviertstrich
# define('MISXXL', '⸺'); // 2em dash - Doppelgeviertstrich

#import datetime
import cf
import fns

code_version='[-VERSIONNR-]'
code_year='[-VERSIONYEAR-]'

# kategorien: 
# astronomie, gesundheit, lernen,
# keywords: 
# Gordons Sonnenuhr nennt sich auch Astronomische Uhr, Astronomie App, Horologium, Horologion, orloj, Astrolabium, Astrolabiumsuhr, Sternenuhr, Himmelsuhr, Einzeigeruhr, Solar Uhr

# prgname = {
#     'de': 'Gordons Sonnenuhr',
#     'en': 'Gordon’s Sun Clock',
#     'es': 'Reloj de sol de Gordon',
#     'zh': 'Gordon-日晷',
# }

#  (dazu gibt es ein [ref=https://youtu.be/J_tu_dMVSbY][u]Zeitraffervideo[/u][/ref])

leninfospalte=24

width_map = { ' ': 0.45, '!': 0.41, '"': 0.68, '#': 0.88, '$': 0.91, '%': 1.41, '&': 1.24, "'": 0.37, '(': 0.55, ')': 0.55, '*': 0.75, '+': 0.85, ',': 0.41, '-': 0.69, '.': 0.41, '/': 0.89, '0': 0.95, '1': 0.74, '2': 0.84, '3': 0.85, '4': 0.91, '5': 0.86, '6': 0.91, '7': 0.76, '8': 0.94, '9': 0.9, ':': 0.41, ';': 0.41, '<': 0.85, '=': 0.85, '>': 0.85, '?': 0.78, '@': 1.74, 'A': 0.98, 'B': 1.04, 'C': 0.96, 'D': 1.1, 'E': 0.91, 'F': 0.84, 'G': 1.08, 'H': 1.16, 'I': 0.5, 'J': 0.52, 'K': 1.01, 'L': 0.85, 'M': 1.33, 'N': 1.17, 'O': 1.18, 'P': 0.99, 'Q': 1.18, 'R': 1.03, 'S': 0.93, 'T': 0.88, 'U': 1.13, 'V': 0.95, 'W': 1.41, 'X': 0.92, 'Y': 0.94, 'Z': 0.89, '[': 0.55, '\\': 0.89, ']': 0.55, '^': 0.92, '_': 0.89, '`': 0.51, 'a': 0.93, 'b': 1.01, 'c': 0.82, 'd': 1.02, 'e': 0.93, 'f': 0.57, 'g': 0.89, 'h': 1.0, 'i': 0.48, 'j': 0.48, 'k': 0.87, 'l': 0.5, 'm': 1.46, 'n': 1.0, 'o': 1.0, 'p': 1.01, 'q': 1.02, 'r': 0.66, 's': 0.8, 't': 0.62, 'u': 0.99, 'v': 0.84, 'w': 1.22, 'x': 0.83, 'y': 0.84, 'z': 0.75, '{': 0.55, '|': 0.69, '}': 0.55, '~': 0.83, '¡': 0.41, '£': 0.89, '¥': 0.91, '§': 0.91, '©': 1.38, '«': 0.98, '®': 1.09, '°': 0.89, '±': 0.85, 'µ': 1.0, '¶': 1.25, '»': 0.97, '¿': 0.78, 'Á': 0.98, 'Ä': 0.98, 'É': 0.91, 'Í': 0.5, 'Ñ': 1.17, 'Ó': 1.18, 'Ö': 1.18, '×': 0.85, 'Ú': 1.13, 'Ü': 1.13, 'ß': 1.01, 'á': 0.93, 'ä': 0.93, 'é': 0.93, 'í': 0.48, 'ñ': 1.0, 'ó': 1.0, 'ö': 1.0, '÷': 0.85, 'ú': 0.99, 'ü': 0.99, '–': 0.89, '—': 1.35, '‘': 0.39, '’': 0.39, '‚': 0.39, '“': 0.69, '”': 0.69, '„': 0.69, '†': 0.87, '‡': 0.87, '•': 0.55, '…': 1.26, '€': 0.98, '™': 1.5, '≈': 0.83, '≠': 0.85, '≤': 0.85, '≥': 0.85 }

width_sp=width_map[' ']
width_hy=width_map['-']
# """+chr(173)+""" geht nicht - softhyphen

showtrennung=False
# showtrennung=True


def est_width(text: str) -> float:
    return sum(width_map.get(ch, 1.0) for ch in text)


vowels = 'aeiouyäöüáéíóúÄÖÜÁÉÍÓÚ'  # Vokale inkl. Umlaute und Akzente
consonants = 'bcdfghjklmnpqrstvwxyzñÑ'  # Konsonanten
splitafter = '.,;:!?“‘”-—)]}%&*+=/\\|>@#_×÷≈≠≤≥°¶•…”’»`' # µ
splitbefore = '„‚([{<$~^€£¥±©®™§†‡“”‘«¿¡' # "
no_split = {
    'de': [ "sch", "ch", "ck", "tz", "pf", "qu", "st", "sp", ],
    'en': [ "th", "sh", "ph", "wh", "qu", "ck", "tr", "dr", ],
    'es': [ "ll", "rr", "ch", "qu", ],
    'fr': [ "ll", "rr", "ch", "qu", ], # einfach aus es kopiert(!)    
}
dontsplitbefore = [ "nd", "hn", "rn", "rg", "nb", "sz", "sw", "rd", "lg", "nü", "fh", "ng", "rl", "hl", "lk", "nw", "tz", "fb", "cht", "mb", "sl", "ck", "ld", "nf", "ns", "ht", "rz", "mp", "nt", "lt", "zb", "rm", "gl", "nuh"]
dontsplitafter = [ "nb", ]
# dosplitafter = [ "ge", ]

def find_hyphenation_points(word, lang=False):
    if lang==False: lang=curr_lang
    lasttr=-1
    points = [] # zeigt auf ersten Buchstaben, der in die neue Zeile gehört word[:2]
    pointsinfo = [] # zeigt auf ersten Buchstaben, der in die neue Zeile gehört word[:2]
    lw = word.lower()
    L = len(word)
    if L < 5: return [points, pointsinfo]
    for i in range(2, L - 2): # beginnt beim 3. Buchstaben - word[2] ist der 3. Buchstabe
        if showtrennung: print(points)
        
        if i==lasttr+1: 
            if showtrennung: print("Trennung blockieren bei", i)
            blocked = True
            for nosp in no_split[lang]:
                # print(lw[i:], nosp)
                if lw.startswith(nosp, i):
                    if showtrennung: print("- Nein, Trennung verhindert:", nosp)
                    blocked = False
                    break
            if blocked:
                continue
 
        if any(word[i-1] in group for group in splitafter):
            lasttr=i
            points.append(i)
            pointsinfo.append(False)
            continue

        if any(word[i-1] in group for group in splitafter):
            lasttr=i
            points.append(i)
            pointsinfo.append(False)
            continue

        if i+2<=L and lw[i:i+2]=='ck':
            lasttr=i+1
            points.append(i+1)
            pointsinfo.append(True)
            continue

        # for dosp in dosplitafter:
        #     # Prüfe, ob lw an Position i - len(dosp) mit dosp startet
        #     # (Stelle sicher, dass i - len(dosp) >= 0, sonst Indexfehler)
        #     start_pos = i - len(dosp)
        #     if start_pos >= 0 and lw.startswith(dosp, start_pos):
                # lasttr=i
        #         points.append(i)
        #         pointsinfo.append(False)
        #         continue

        # if any(lw[i-1:i+1] in group for group in no_split[lang]) : # or any(lw[i:i+2] in group for group in no_split[lang])
        #     continue
        blocked = False
        for nosp in no_split[lang]:
            if i >= 1 and lw.startswith(nosp, i - 1):
                blocked = True
                break
            if len(nosp) > 2 and i >= 2 and lw.startswith(nosp, i - 2):
                blocked = True
                break            
        if blocked:
            continue

        if lw.startswith("ei") and i==2: # kein ei- trennen
            continue
        
        blocked = False
        for nosp in no_split[lang]:
            if i + len(nosp) +1 <= L and lw.startswith(nosp, i) and lw[i+len(nosp)] in vowels and lw[i] in consonants: 
                if showtrennung: print("SONDERTRENNUNG")
                lasttr=i
                points.append(i)
                pointsinfo.append(True)
                blocked = True
                break
        if blocked:
            continue
        
        if any(lw.startswith(nosp, i-len(nosp)) for nosp in dontsplitafter if i >= len(nosp)):
            if showtrennung: print("TRENNUNG verhindert", i, word[i:])
            continue            

        if any(lw.startswith(nosp, i) for nosp in dontsplitbefore if i + len(nosp) <= L):
            if showtrennung: print("TRENNUNG verhindert", i, word[i:])
            continue            

        # if (lw[i-1] in vowels and lw[i] in consonants) or (lw[i-1] in consonants and lw[i] in consonants and lw[i-2] in vowels):
        if (lw[i-1] in vowels and lw[i] in consonants) or (lw[i-1] in consonants and lw[i] in consonants and lw[i-2] in vowels) or (lw[i-1] in consonants and lw[i] in consonants and lw[i+1] in vowels):
            if any(c in vowels for c in word[i:]) and lw[i]!=lw[i+1]:
                if lang=='en' and  L - i == 3 and word[L-2:] == "ed":
                    # pass # wollen wir fix- ed trennen?
                    lasttr=i+1
                    points.append(i+1)
                    pointsinfo.append(True)
                else: 
                    lasttr=i
                    points.append(i)
                    pointsinfo.append(True)
    return [points,pointsinfo]

card_newline='\u241e'

def split_with_nl(text):
    # text=text[:200]
    words = []
    for line in text.split('\n'):
        # Zerlege jede Zeile normal in Wörter
        parts = line.split()
        words.extend(parts)
        # Nach jeder Zeile (außer der letzten) ein Zeilenumbruch-Zeichen einfügen
        words.append(card_newline)
    if words and words[-1] == card_newline:
        words.pop()  # letzten Trenner entfernen, falls er auf leere letzte Zeile zurückgeht
    return words

def wrap_text(text, max_width=leninfospalte, lang=False):
    if lang==False: lang=curr_lang
    words = split_with_nl(text) # text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        if word==card_newline:
            lines.append(" ".join(current_line))
            current_line = []
            current_width = 0
            continue
        space_width = width_sp if current_line else 0
        word_width = est_width(word)
        
        # Prüfe, ob das Wort komplett passt
        if showtrennung: print(" ")
        if showtrennung: print(word)
        if showtrennung: print(current_width,space_width+word_width)
        if showtrennung: print(current_width + space_width + word_width, "<=", max_width)
        if current_width + space_width + word_width <= max_width:
            current_line.append(word)
            current_width += space_width + word_width
            continue

        if current_line and current_width>max_width-2-space_width-width_hy:
            # okay, einfach neue Zeile
            lines.append(" ".join(current_line))
            current_line = [word]
            current_width = word_width
            continue

        # Wort passt nicht: Suche Trennpunkt
        points, pointsinfo = find_hyphenation_points(word, lang=lang)
        if showtrennung: print(points)
        if points:
            cw=space_width+word_width
            lp=len(word) # lp = immer einer mehr (+1)
            for j in reversed(range(len(points))):
                point = points[j]
                info = pointsinfo[j]
                cw-=est_width(word[point:lp])
                lp=point # anfang als neues ende merken
                addhy='-' if info else ''
                if showtrennung: print(current_width+cw+(width_hy if info else 0), word[:point]+addhy, cw+width_hy, space_width+est_width(word[:point]+addhy))
                if current_width+cw+(width_hy if info else 0) <= max_width:
                    addhy='-' if info else ''
                    current_line.append(word[:point]+addhy)
                    lines.append(" ".join(current_line))
                    current_line = [word[point:]]
                    current_width = est_width(word[point:])
                    break
            else:
                # Kein Trennpunkt passt
                if current_line and current_width>max_width*0.67:
                    # okay, einfach neue Zeile
                    lines.append(" ".join(current_line))
                    current_line = [word]
                    current_width = word_width
                    continue
                else:
                    # trennen mitten im wort erzwingen
                    current_width+=space_width+width_hy
                    i=0
                    for char in word: 
                        current_width+=est_width(char)
                        if current_width>max_width: break # trenne word bei position davor word[:i]
                        i+=1
                    current_line.append(word[:i]+'-')
                    lines.append(" ".join(current_line))
                    current_line = [word[i:]]
                    current_width = est_width(word[i:])                    
                    continue
        else:
            # Kein Trennpunkt passt
            if current_line and current_width>max_width*0.67:
                # okay, einfach neue Zeile
                lines.append(" ".join(current_line))
                current_line = [word]
                current_width = word_width
                continue
            else:
                # trennen mitten im wort erzwingen
                current_width+=space_width+width_hy
                i=0
                for char in word: 
                    current_width+=est_width(char)
                    if current_width>max_width: break # trenne word bei position davor word[:i]
                    i+=1
                current_line.append(word[:i]+'-')
                lines.append(" ".join(current_line))
                current_line = [word[i:]]
                current_width = est_width(word[i:])                    
                continue

    if current_line:
        lines.append(" ".join(current_line))

    # Ausgabe mit Breiten
    if showtrennung: 
        for line in lines: 
                w = est_width(line)
                print(f"{w:04.1f} | {line}")
    
    return "\n".join(lines)



def gettx(txcode):
    # Deutsch: „Gordons Sonnenuhr” 
    # Englisch: ‘Automatic’ 
    # Spanisch: «Automático»
    t=replace_quotes(lang[fns.curr_lang][txcode].replace(code_version, fns.versiondat['full']).replace(code_year, fns.versiondat['year']).replace(" - ", " – ").replace("--", "––"), fns.curr_lang)
    return t

def replace_quotes(text, lang='de'):
    quotes = {
        'de': ('„', '”'),  # Deutsch
        'en': ('‘', '’'),  # Englisch
        'es': ('«', '»')   # Spanisch
    }

    if lang not in quotes or '"' not in text:
        return text  # Keine Anführungszeichen, Text unverändert zurückgeben

    # Ergebnis-String aufbauen
    open_quote, close_quote = quotes[lang]
    rt = []
    quote_state = 0  # 0: Erwartet eröffnendes Zeichen, 1: Erwartet schließendes Zeichen
    for char in text:
        if char == '"':
            if quote_state == 0:
                rt.append(open_quote)
                quote_state = 1
            else:
                rt.append(close_quote)
                quote_state = 0
        else:
            rt.append(char)
    return ''.join(rt)

def txupdobjdata(repl): # txupdobjdata({'moon.size': "87"})
    class DefaultDict(dict):
        def __missing__(self, key):
            return '{' + key + '}'
    default_repl = DefaultDict(repl)
    return gettx("txobjdata").format_map(default_repl)


#
#
# (!) 'de'=German IS THE ORIGINAL LANGUAGE. It is best to start a translation from German.
#
#
    
lang = {
    'de': {
        'txsettings': chr(10)+'Gordons Sonnenuhr',
        'txwelcome': 'Willkommen', # do not DELETE, important for checking if language pack exists 
        'wdaysh': ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"],
        'xxdays': ['{day} Tag', '{day} Tage'], # singular, plural
        'himmelsr': ["O", "S", "W", "N"],
        'txgps_label': chr(10)+'GPS-Position oder Ortsname:',
        'txgpsauto': 'Auto-GPS (grob):',
        'txgpsautosh': 'AUTO',
        'txtimezone': 'Zeitzone:',
        'txtimeformat': '24h-Format:',
        'txwelcomescr': 'GPS-Hinweis aus:',
        'txedgescreen': 'Mehr Rand:',
        'txenlargeobj': 'Große Symbole:',
        'txuhrsinn': 'Blickrichtung:',
        'txuhrsinnarr': {'auto': 'automatisch', 'nord': 'Norden', 'sued': 'Süden'},
        'txfullscr': 'Immer-an Modus:',
        'txnachtmodus': 'Dunkelmodus:',
        'txnachtmodusarr': {'auto': 'automatisch', 'auto_lang': 'auto (mehr)', 'auto_kurz': 'auto (weniger)', 'day': 'hell', 'night': 'dunkel'},
        'txfarben': 'Design:',
        'txfarbenarr': {'orig': 'Graustufen', 'c-turn': 'Farbe', 'a-gord': 'Kunst', 'a-telesk': 'Teleskop'}, # 'a-bay': 'Kunst Bayus (Test)', Graustufen Monochrom
        'txstatuslog': "[b]–– Status-Log:[/b]",
        'txgpsinstruct': wrap_text("Um Ihre GPS-Position anzupassen, wischen Sie nach links", lang='de'),
        'txgpsdeact': wrap_text("GPS ist deaktiviert. Bitte aktivieren Sie GPS in Ihrer Geräteeinstellung", lang='de'),

        'uebanleitung': 'Anleitung',
        'txanleitung': chr(10)+"""Um Ihre GPS-Position automatisch zu übernehmen, setzen Sie das Häkchen „Auto-GPS“. Während Sie die App nutzen, wird dann Ihre GPS-Position wird mit ungefährem GPS schnell und energiesparend bestimmt. - Alternativ können Sie eine feste GPS-Position kommagetrennt in das Textfeld eintragen (setzen Sie anschließend das Häkchen bei „GPS-Hinweis aus“) oder einen Ortsnamen in das Feld eingeben. Bei Änderung der Koordinaten (und anderer grundlegender Daten), macht Sonnenuhr eine Berechnung, die (je nach Gerät) zwischen 2-30 Sekunden dauern kann. Diese gilt für einen Tag.

Zeitzone und Sprache sollten automatisch von Ihrem Mobiltelefon übernommen werden. Sie können zwischen einem 12h- und 24h-Format für die Uhrzeit wählen. Unter Design können Sie verschiedene Darstellungen auswählen. Für den Dunkelmodus kann hell, dunkel und automatische Umschaltung gewählt werden. „Automatisch“ wechselt bei Sonnenuntergang auf Dunkelmodus, „automatisch (weniger)“ wechselt zum Ende der Dämmerung (-6°), „automatisch (mehr)“ wechselt bei +6°. 

„Mehr Rand“ ist für randlose Geräte. Mit „Blickrichtung“ können Sie einstellen, ob die Uhr im Uhrzeigersinn laufen soll (Süden) oder gegen ihn (Norden). (Bitte beachten Sie: Wenn Sie die Drehrichtung ändern, liegt der Teil des Sonnenkreises, der unter dem Horizont ist, dann nicht mehr hinter Ihnen, sondern vor Ihnen. Mehr Details s.u.) 

„Große Symbole“ zeichnet die Objekte auf dem Ziffernblatt größer. „Immer an“ verhindert das Ausschalten des Bildschirms. Ich habe meiner Nichte z.B. ein altes [i]Tablet[/i] mit „Sonnenuhr“ an die Wand gehängt, das immer direkt zu sehen ist.

Sollten Ihre Einstellungen einmal nicht übernommen werden, können Sie die Aktualisierungsschaltfläche unten rechts drücken. 


[b]–– Ziffernblatt:[/b]
        
Eine ausführliche Erklärung zum Lesen des Ziffernblatts finden Sie auf der nächsten Seite (bitte nach links wischen).


[b]–– Mehr Details:[/b]

Alle Berechnungen werden für Ihren lokalen Standort durchgeführt und sollten mit den Positionen des astronomischen Almanachs auf 0,0005 Bogensekunden übereinstimmen (Mond z.B. ist max. 2047 Bogensek. groß). - Voll- und Neumond (in/vor Tagen)"""+chr(10),
        'txobjdata': """Vollmond: {moon_full}
Neumond: {moon_new}
Mond beleuchtet: {moon_illum}
Mondgröße: {moon_sizep} (85-100)

Helligkeit:
Venus: {venus_magp} (83-100)
Mars: {mars_magp} (52-100)
Jupiter: {jupiter_magp} (87-100)
Merkur: {merkur_magp} (0-100)
Saturn: {saturn_magp} (77-100)


[b]–– Legende:[/b]""",
        'txlegende': chr(10)+"""☉ Sonne, ● Mond (mit Phasen)
        
♀ Venus (perlenfarben), ♂ Mars (rötlich), ♃ Jupiter (gestreift), ☿ Merkur (grau), ♄ Saturn (mit Ringen)

[s] Sirius, [k] Canopus, [f] Alpha Centauri, [a] Arktur, [w] Wega, [c] Capella, [r] Rigel, [p] Prokyon, [b] Beteigeuze, [h] Achernar""", # , [•] ISS
        'txmore': " "+chr(10)+chr(10), # chr(10)+chr(10)+""" """+chr(10)+chr(10),

        'txmanual': chr(10)+'Ziffernblatt',
        'txanleitung2': chr(10)+"""„Gordons Sonnenuhr” ist im Prinzip eine Einzeigeruhr mit einem täglich sich wandelnden Ziffernblatt, das sich an den Rhythmen der Natur und Gestirne orientiert. Es zeigt Sonnenstand und Sternenhimmel. Eine neue Art von Zeitdarstellung, die nicht künstlich ist wie unsere normale Uhr (mit Eisenbahnzeit und Zeitumstellung), sondern sich im Einklang mit den Jahreszeiten bewegt.

[i]HINWEIS: Sie können zwischen dieser Anleitung und dem Ziffernblatt hin- und herwischen.[/i]


[b]–– Ihr Blick:[/b]

In der Mitte des Bildschirms sehen Sie eine waagerechte Linie. Das ist der Horizont (die Erdoberfläche). Das spitze Dreieck in der Mitte ist ein Fichtenbaum, den Sie aus der Ferne sehen (oder eine Kirche). (Sie schauen nicht von oben auf ihn herab, sondern stehen davor.) 

Wenn Sie an den Einstellungen nichts geändert haben („Blickrichtung: automatisch“), schauen Sie auf der Nordhalbkugel nach Süden (und auf der Südhalbkugel nach Norden). Objekte, die links am Bildschirm sind, finden Sie im Osten; Objekte, die rechts am Bildschirm sind, finden Sie im Westen (umgekehrt auf der Südhalbkugel). Am Rand des Horizonts stehen die jeweiligen Himmelsrichtungen. 

Der (hell)graue Streifen unter dem Horizont zeigt die (bürgerliche) Dämmerungsphase an. Der große, dunkelgraue Bereich symbolisiert die Nacht (inkl. der nautischen Dämmerung). Objekte, die sich in diesem Bereich aufhalten, sind nicht sichtbar.

Am rechten Rand des Bildschirms sehen Sie die lokale Uhrzeit (in digital), die GPS-Position des Standortes als Zifferncode (z.B. „cri-hs“, der auf ca. 4 km genau ist) bzw. einen Ortsnamen (wenn Sie diesen eingegeben haben), sowie die momentane Höhe der Sonne in Grad am Himmel (z.B. 27,6°). 


[b]–– Sonne:[/b]

Die Sonne (am Ende des einzigen Zeigers der Uhr) wandert im Laufe des Tages von links nach rechts (umgekehrt auf der Südhalbkugel). Je weiter links die Sonne auf dem Bildschirm ist, desto mehr ist sie im Osten; je weiter rechts, desto mehr im Westen (umgekehrt auf der Südhalbkugel). Je höher die Sonne auf dem Bildschirm zu sehen ist, desto höher steht sie am Himmel. 

Die Sonne folgt der eingezeichneten Kreisbahn, auf der sie sich innerhalb eines Tages bewegt. Am Rande der Kreisbahn sind Stunden angegeben (z.B. „12“ Uhr), so dass die Kreisbahn auch als Ziffernblatt fungiert. 

Am Ziffernblatt z.B. kann man sehen, wie während der Zeitumstellung, sich die Ziffern verschieben, die Kreisbahn jedoch gleich bleibt. Oder: wie die gesetzliche Zeit an den meisten Orten von der Ortszeit abweicht, da 12 Uhr nicht genau oben auf dem Ziffernblatt ist.""",

        'txanleitung2b': chr(10)+chr(10)+"""[b]–– Mond:[/b]

Der Mond hat ebenfalls eine Umlaufbahn. Sie ist als hellgrauer Kreis gezeichnet (ohne Zeiger). Da der Mond mehr als 24 Stunden für einen Umlauf braucht, sind zwei zusätzliche Stunden (vom gestrigen Tag) in extra hellem Grau angefügt. Wenn man „mit der Uhr lebt“, sieht man schön, wie sich der Mond über Wochen periodisch höher und tiefer schraubt. Außerdem kann man beobachten, wie er zu Vollmond der Sonne in der Kreisposition gegenüber steht (fern); zu Neumond er aber auf derselben Kreisposition steht (sonnennah). Es ist meistens nicht exakt dieselbe Position, weil man ja von der Seite schaut (und nicht von oben). Exakt dieselbe Position ist es nur bei einer Sonnenfinsternis. 

Vollmond und Neumond werden (durch den eingezeichneten Schatten) angezeigt. Neumond wird für 35 Stunden dargestellt (weil das die Zeit ist, in der man den Mond keinesfalls sehen kann). Vollmond wird für 24 Stunden dargestellt. (Die Neuberechnung der Sonnen- und Mondlaufbahn findet jeweils um UTC 00:00 statt.)


[b]–– Planeten:[/b]

Es werden die fünf mit bloßem Auge sichtbaren Planten gezeigt, vertreten durch ihre astronomische Symbole (s. Legende vorherige Seite). Wenn Sie sich den echten Sternenhimmel ansehen, können Sie die Planten von den Sternen unterscheiden, indem Sie wissen, dass Planeten nicht flackern, sondern beständig leuchten, weil sie viel größer scheinen als die weit entfernten Sterne und daher von den Dichteschwankungen der Atmosphäre nicht so stark beeinflusst sind.


[b]–– Sterne:[/b]

Weiter werden die zehn hellsten Sterne gezeigt, symbolisiert durch einen Buchstaben in einem Quadrat (s. Legende vorherige Seite). Während sich die Planeten relativ geordnet, meist mehr oder weniger in der der Nähe der Sonnenlaufbahn aufhalten, ist die Laufbahn der Sterne von der Sonne unabhängig (sind sie doch ihre eigene Sonne). Bei den Sternensymbolen sind daher immer zwei Seiten des Quadrats kräftiger gezeichnet als die beiden anderen. Dies deutet die Ecke an (bzw. DEN Quadranten ihrer Laufbahn), in dem sie sich aktuell aufhalten. Ist die hervorgehobene Ecke unten rechts, so ist das (mehr oder weniger) das „Ende“ der Laufbahn nach unten und rechts, und der Stern wird sich bei seinen weiteren Bewegungen hauptsächlich nach oben und nach links hin bewegen (oft auch außerhalb des Bildschirms).


[b]–– Historie:[/b]

„Gordons Sonnenuhr” wurde 2019 für einen Raspberry Pi mit einem 10 Zoll ePaper-Display entwickelt, da ich eine Wanduhr haben wollte, die angenehm anzusehen ist und Zeit in Verbindung mit dem Sonnenlauf bringt. Mein Ziel war, eine Uhr zu bauen, die eine natürliche Zeit zeigt, nicht eine menschengemachte Zeit, wie die 12-Stunden-Analoguhr sie zeigt. Dort, wo wir leben, gibt es über das Jahr hin einen deutlichen Unterschied in den Tageslängen und auch die wiederkehrende, ungeliebte Zeitumstellung. All das sollte Sonnenuhr ins rechte Licht rücken: Sie zeigt ein organisches Ziffernblatt, das sich an den Jahreszeiten orientiert, am Rhythmus der Natur und sich mit diesem verändert. – Da heute fast jeder einen kleinen Computer in der Tasche hat, habe ich Sonnenuhr 2025 als Androidapp entwickelt. Viel Freude und Erkenntnis damit!"""+chr(10)+chr(10)+chr(10),

        'txabout': chr(10)+'Info',
        'txanleitungprg': chr(10)+"""Gordons Sonnenuhr
Version """+code_version+""" [i](zunclock)[/i]
Gordon Axmann
Copyright 2019-"""+code_year,

        'txanleitung3': chr(10)+f"""Grundsätzlich gilt: Daten werden von diesem Programm weder erhoben noch an mich gesendet. Alles bleibt auf Ihrem Gerät. Für den Betrieb von Sonnenuhr ist nicht einmal eine Internetverbindung nötig. - Dazu gibt es eine Ausnahme: Im Fall eines Programmfehlers sendet Sonnenuhr (sofern Sie Internet haben) die Fehlermeldung zusammen mit der Versionsnummer, der Betriebssystemversion und einer zufälligen UUID an meine Webpräsenz. So helfen Sie, Sonnenuhr zu verbessern. 
 
Diese Software ist ein kostenloses, privates Angebot, für das ich nur eingeschränkt Support leisten mag. Bitte nutzen Sie die Software, wie sie ist. Ich bin kein professioneller App-Entwickler. Dennoch ist eine Menge an Herzblut in diese Software über Jahre geflossen.

Wenn Sie einen Fehler gefunden haben, korrigiere ich diesen gerne, wenn ich einen klaren und vollständigen Fehlerbericht bekomme, mit Screenshot und genauer Beschreibung wo(durch) und wann der Fehler aufgetreten ist und am liebsten ein Bildschirmfoto des untenstehenden Status-Logs (Mailkontakt: {cf.owneremail}) möglichst direkt nach Auftreten des Fehlers. Hinweise zu Berechnungsfehlern, sind in 99% der Fälle Falschmeldungen. Sternenberechnung ist sehr komplex, und gibt viel zu viele Falschinformationen.

Danke an Rhodes Mill, Rolf, Greg Miller und alle Tester. Bilder der Himmelskörper: NASA/SOHO, ESA/Hubble, NASA/JPL-Caltech

„Sonnenuhr“ ist freie Software. Haben Sie einfach Freude an der Nutzung. Wenn Sie Ihre Wertschätzung für meine Arbeit ausdrücken möchten, finden Sie hier meine Webpräsenz:"""+chr(10)+chr(10),
        'txkaffee': 'Zur Webpräsenz',
        'txanleitung4': chr(10)+""" """,
    },
    'en': {
        'txsettings': chr(10)+'Gordon’s Sun Clock',
        'txwelcome': 'Welcome', # dont DELETE
        'wdaysh': ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        'xxdays': ['{day} day', '{day} days'], # singular, plural
        'himmelsr': ["E", "S", "W", "N"],
        'txgps_label': chr(10)+'GPS position or place name:',
        'txgpsauto': 'Auto GPS (coarse):',
        'txgpsautosh': 'AUTO',
        'txtimezone': 'Time zone:',
        'txtimeformat': '24h format:',
        'txwelcomescr': 'Hide GPS notice:',
        'txedgescreen': 'More edge:',
        'txenlargeobj': 'Large objects:',
        'txuhrsinn': 'View:',
        'txuhrsinnarr': {'auto': 'automatic', 'nord': 'North', 'sued': 'South'},
        'txfullscr': 'Screen stays on:',
        'txnachtmodus': 'Dark theme:',
        'txnachtmodusarr': {'auto': 'automatic', 'auto_lang': 'auto (more)', 'auto_kurz': 'auto (less)', 'night': 'dark', 'day': 'light'},        
        'txfarben': 'Design:',
        'txfarbenarr': {'orig': 'Greyscale', 'c-turn': 'Colour', 'a-gord': 'Art'}, # 'a-bay': 'Art Bayus', Greyscale Monochrome
        'txstatuslog': "[b]–– Status log:[/b]",
        'txgpsinstruct': wrap_text("To adjust your GPS position, swipe left", lang='en'),
        'txgpsdeact': wrap_text("GPS is disabled. Please enable GPS in your device settings", lang='en'),

        'uebanleitung': 'Instructions',
        'txanleitung': chr(10)+"""To automatically use your GPS position, tick the ‘Auto-GPS’ box. While you are using the app, your GPS position will be determined quickly and energy-efficiently using approximate GPS. Alternatively, you can enter a fixed GPS position separated by commas in the text field (then tick the ‘GPS notification off’ box) or enter a place name in the field. When the coordinates (and other basic data) change, Sun Clock performs a calculation that can take between 2 and 30 seconds (depending on the device). This applies for one day.

The time zone and language should be automatically transferred from your mobile phone. You can choose between a 12-hour and 24-hour format for the time. For the design scheme, you can choose between light, dark and automatic switching. ‘Automatic’ switches to dark mode at sunset, ‘automatic (less)’ switches at the end of twilight (-6°), ‘automatic (more)’ switches at +6°. 

‘More border’ is for borderless devices. With ‘View direction’ you can set whether the clock should run clockwise (south) or counterclockwise (north). (Please note: If you change the direction of rotation, the part of the sun circle that is below the horizon will no longer be behind you, but in front of you. See below for more details). 

‘Large symbols’ draws the objects on the dial larger. ‘Always on’ prevents the screen from turning off. For example, I hung an old tablet with ‘Sundial’ on the wall for my niece, which is always directly visible.

If your settings are not applied, you can press the refresh button at the bottom right. 


[b]-- Dial:[/b]
        
A detailed explanation of how to read the dial can be found on the next page (please swipe left).


[b]-- More details:[/b]

All calculations are made for your local location and should match the positions of the astronomical almanac to within 0.0005 arc seconds (comparison: moon is max. 2047 arc seconds). - Full moon and new moon (in/before days)"""+chr(10),
        'txobjdata': """Full moon: {moon_full}
New moon: {moon_new}
Moon illuminated: {moon_illum}
Moon diameter: {moon_sizep} (85-100)

Brightness:
Venus: {venus_magp} (83-100)
Mars: {mars_magp} (52-100)
Jupiter: {jupiter_magp} (87-100)
Mercury: {merkur_magp} (0-100)
Saturn: {saturn_magp} (77-100)

        
[b]–– Legend:[/b]""",
        'txlegende': chr(10)+"""☉ Sun, ● Moon (with phases)
        
♀ Venus (pearl-coloured), ♂ Mars (reddish), ♃ Jupiter (striped), ☿ Mercury (grey), ♄ Saturn (with rings)

[s] Sirius, [k] Canopus, [f] Alpha Centauri, [a] Arcturus, [w] Vega, [c] Capella, [r] Rigel, [p] Procyon, [b] Betelgeuse, [h] Achernar""",
        'txmore': " "+chr(10)+chr(10), # chr(10)+chr(10)+""" """+chr(10)+chr(10),
        
        'txmanual': chr(10)+'Dial',
        'txanleitung2': chr(10)+chr(10)+""""‘Gordon's Sun Clock’ is essentially a single-hand watch with a dial that changes daily, based on the rhythms of nature and the stars. It shows the position of the sun and the starry sky. It is a new way of displaying time that is not artificial like our normal clocks (with railway time and daylight saving time), but moves in harmony with the seasons.

[i]NOTE: You can swipe back and forth between this guide and the dial.[/i]


[b]–– Your view:[/b]

In the middle of the screen, you will see a horizontal line. This is the horizon (the surface of the Earth). The pointed triangle in the middle is a spruce tree that you see from a distance (or a church). (You are not looking down on it from above, but standing in front of it.) 

If you have not changed the settings (‘View direction: automatic’), you are looking south in the northern hemisphere (and north in the southern hemisphere). Objects on the left side of the screen are located in the east; objects on the right side of the screen are located in the west (reversed in the southern hemisphere). The cardinal directions are shown at the edge of the horizon. 

The (light) grey strip below the horizon indicates the (civil) twilight phase. The large, dark grey area symbolises night (including nautical twilight). Objects located in this area are not visible.

On the right edge of the screen, you can see the local time (in digital form), the GPS position of the location as a numerical code (e.g. ‘cri-hs’, which is accurate to approx. 4 km) or a place name (if you have entered one), as well as the current altitude of the sun in degrees in the sky (e.g. 27.6°). 


[b]–– Sun:[/b]

The sun (at the end of the clock's single hand) moves from left to right (reversed in the southern hemisphere) throughout the day. The further to the left the sun is on the screen, the further east it is; the further to the right, the further west (reversed in the southern hemisphere). The higher the sun is on the screen, the higher it is in the sky. 

The sun follows the circular path marked on the screen, which it travels along in the course of a day. The hours are indicated at the edge of the circular path (e.g. ‘12’ o'clock), so that the circular path also functions as a clock face. 

On the clock face, for example, you can see how the numbers shift during the time change, but the circular path remains the same. Or: how the legal time in most places differs from the local time, as 12 o'clock is not exactly at the top of the clock face.""",
        'txanleitung2b': chr(10)+chr(10)+"""[b]–– Moon:[/b]

The moon also has an orbit. It is drawn as a light grey circle (without a pointer). Since the moon takes more than 24 hours to complete one orbit, two additional hours (from the previous day) are added in extra light grey. If you ‘live with the clock’, you can clearly see how the moon periodically rises and falls over the course of weeks. You can also observe how it is opposite the sun in the circle position (far away) at full moon, but at the same circle position (close to the sun) at new moon. It is usually not exactly the same position because you are looking from the side (and not from above). The exact same position only occurs during a solar eclipse. 

Full moon and new moon are indicated (by the shaded area). New moon is shown for 35 hours (because that is the time during which the moon cannot be seen at all). Full moon is shown for 24 hours. (The sun and moon orbits are recalculated at UTC 00:00.)


[b]–– Planets:[/b]

The five planets visible to the naked eye are shown, represented by their astronomical symbols (see legend on previous page). When you look at the real starry sky, you can distinguish the planets from the stars by knowing that planets do not twinkle but shine steadily because they appear much larger than the distant stars and are therefore not as strongly affected by the density fluctuations of the atmosphere.


[b]–– Stars:[/b]

The ten brightest stars are also shown, symbolised by a letter in a square (see legend on previous page). While the planets are relatively orderly, mostly located more or less near the sun's orbit, the stars' orbits are independent of the sun (since they are their own suns). In the star symbols, two sides of the square are therefore always drawn more strongly than the other two. This indicates the corner (or THE quadrant of their orbit) in which they are currently located. If the highlighted corner is at the bottom right, this is (more or less) the ‘end’ of the orbit downwards and to the right, and the star will mainly move upwards and to the left in its further movements (often outside the screen).


[b]–– History:[/b]

‘Gordon's Sundial’ was developed in 2019 for a Raspberry Pi with a 10-inch ePaper display because I wanted a wall clock that was pleasant to look at and related time to the sun's path. My goal was to build a clock that shows natural time, not man-made time, as shown by the 12-hour analogue clock. Where we live, there is a significant difference in the length of the days throughout the year, as well as the recurring, unpopular time change. Sun Clock was designed to put all of this into perspective: it displays an organic dial that is oriented towards the seasons, the rhythm of nature, and changes with it. Since almost everyone has a small computer in their pocket these days, I developed Sun Clock 2025 as an Android app. I hope you enjoy it and find it insightful!"""+chr(10)+chr(10)+chr(10),
        'txabout': chr(10)+'Info',
        'txanleitungprg': chr(10)+"""Gordon's Sun Clock
Version """+code_version+""" [i](zunclock)[/i]
Gordon Axmann
Copyright 2019-"""+code_year,
        'txanleitung3': chr(10)+f"""As a general rule, this programme does not collect or send any data to me. Everything remains on your device. Sun Clock does not even require an internet connection to operate. There is one exception to this: in the event of a programme error, Sun Clock sends the error message (provided you have an internet connection) together with the version number, the operating system version and a random UUID to my website. By doing so, you help to improve Sun Clock.
 
This software is a free, private offering for which I can only provide limited support. Please use the software as is. I am not a professional app developer. Nevertheless, a lot of heart and soul has gone into this software over the years.

If you find an error, I will be happy to correct it if I receive a clear and complete error report with a screenshot and a detailed description of where (how) and when the error occurred, and preferably a screenshot of the status log below (email contact: {cf.owneremail}) as soon as possible after the error occurs. In 99% of cases, reports of calculation errors are false alarms. Star calculation is very complex and produces far too much false information.

Thanks to Rhodes Mill, Rolf, Greg Miller and all the testers. Images of celestial bodies: NASA/SOHO, ESA/Hubble, NASA/JPL-Caltech

‘Sun Clock’ is free software. Just enjoy using it. If you would like to express your appreciation for my work, you can find my website here:"""+chr(10)+chr(10),
        'txkaffee': "Visit website",
        'txanleitung4': chr(10)+""" """,
    },

    'es': {
        'txsettings': chr(10)+'Reloj de sol Gordon',
        'txwelcome': 'Bienvenido', # do not change, important for checking if language pack exists
        'wdaysh': ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        'xxdays': ['{day} día', '{day} días'], # singular, plural
        'himmelsr': ["E", "S", "O", "N"],
        'txgps_label': chr(10)+'Posición GPS o nombre del lugar:',
        'txgpsauto': 'Auto-GPS (aproximado):',
        'txgpsautosh': 'AUTO',
        'txtimezone': 'Zona horaria:',
        'txtimeformat': 'Formato 24h:',
        'txwelcomescr': 'Nota GPS desactivado:',
        'txedgescreen': 'Más borde:',
        'txenlargeobj': 'Objetos grandes:',
        'txuhrsinn': 'Dirección de vista:',
        'txuhrsinnarr': {'auto': 'automático', 'nord': 'Norte', 'sued': 'Sur'},
        'txfullscr': 'Modo siempre encendido:',
        'txnachtmodus': 'Modo oscuro:',
        'txnachtmodusarr': {'auto': 'automático', 'auto_lang': 'auto (más)', 'auto_kurz': 'auto (menos)', 'night': 'oscuro', 'day': 'claro'},
        'txfarben': 'Diseño:',
        'txfarbenarr': {'orig': 'Escala de grises', 'c-turn': 'Color', 'a-gord': 'Arte'}, # 'a-bay': 'Arte Bayus', Escala de grises Monocromo Colores
        'txstatuslog': "[b]-- Registro de estado:[/b]",
        'txgpsinstruct': wrap_text("Para ajustar tu posición GPS, desliza el dedo hacia la izquierda", lang='es'),
        'txgpsdeact': wrap_text("GPS está desactivado. Active GPS en la configuración de su dispositivo", lang='es'),

        'uebanleitung': 'Instrucciones',
        'txanleitung': chr(10)+"""Para aceptar automáticamente su posición GPS, marque la casilla «GPS automático». Mientras utiliza la aplicación, su posición GPS se determinará de forma rápida y con bajo consumo de energía mediante GPS aproximado. - Alternativamente, puede introducir una posición GPS fija separada por comas en el campo de texto (a continuación, marque la casilla «Notificación GPS desactivada») o introducir un nombre de lugar en el campo. Si se modifican las coordenadas (y otros datos básicos), Reloj de sol realiza un cálculo que puede tardar entre 2 y 30 segundos (dependiendo del dispositivo). Este cálculo es válido para un día.

La zona horaria y el idioma se deben transferir automáticamente desde su teléfono móvil. Puede elegir entre el formato de 12 o 24 horas para la hora. Para el esquema de diseño, puede elegir entre claro, oscuro y cambio automático. «Automático» cambia al modo oscuro al atardecer, «auto (menos)» cambia al final del crepúsculo (-6°), «auto (más)» cambia a +6°. 

«Más borde» es para dispositivos sin bordes. Con «Dirección de la mirada» puede configurar si el reloj debe funcionar en el sentido de las agujas del reloj (sur) o en sentido contrario (norte). (Tenga en cuenta que si cambia la dirección de giro, la parte del círculo solar que está por debajo del horizonte ya no estará detrás de usted, sino delante). Más detalles a continuación). 

«Símbolos grandes» dibuja los objetos de la esfera más grandes. «Siempre encendido» evita que se apague la pantalla. Por ejemplo, le he colgado a mi sobrina una vieja [i]tableta[/i] con «Reloj de sol» en la pared, que siempre se ve directamente.

Si alguna vez no se aplican sus ajustes, puede pulsar el botón de actualización en la parte inferior derecha. 


[b]–– Esfera:[/b]
        
Encontrará una explicación detallada sobre cómo leer la esfera en la página siguiente (deslice hacia la izquierda).


[b]-- Más detalles:[/b]

Todos los cálculos se realizan para su ubicación local y deberían coincidir con las posiciones del almanaque astronómico con una precisión de 0,0005 segundos de arco (comparación: la luna está a un máximo de 2047 segundos de arco). - Luna llena y luna nueva (en/antes de días)"""+chr(10),
        'txobjdata': """Luna llena: {moon_full}
Luna nueva: {moon_new}
Luna iluminada: {moon_illum}
Diámetro de la luna: {moon_sizep} (85-100)

Brillo:
Venus: {venus_magp} (83-100)
Marte: {mars_magp} (52-100)
Júpiter: {jupiter_magp} (87-100)
Mercurio: {merkur_magp} (0-100)
Saturno: {saturn_magp} (77-100)
      

[b]–– Leyenda:[/b]""",
        'txlegende': chr(10)+"""☉ Sol, ● Luna (con fases)
        
♀ Venus (color perla), ♂ Marte (rojizo), ♃ Júpiter (rayado), ☿ Mercurio (gris), ♄ Saturno (con anillos)

[s] Sirio, [k] Canopus, [f] Alfa Centauri, [a] Arcturus, [w] Vega, [c] Capella, [r] Rigel, [p] Procyon, [b] Betelgeuse, [h] Achernar""",
        'txmore': " "+chr(10)+chr(10), # chr(10)+chr(10)+""" """+chr(10)+chr(10),
        
        'txmanual': chr(10)+'Esfera',
        'txanleitung2': chr(10)+chr(10)+"""«El reloj de sol de Gordon» es, en principio, un reloj de una sola aguja con una esfera que cambia cada día y que se orienta según los ritmos de la naturaleza y los astros. Muestra la posición del sol y el cielo estrellado. Una nueva forma de representar el tiempo, que no es artificial como nuestro reloj normal (con hora ferroviaria y cambio de hora), sino que se mueve en armonía con las estaciones.

[i]NOTA: Puede desplazarse entre estas instrucciones y la esfera del reloj.[/i]


[b]–– Su mirada:[/b]

En el centro de la pantalla verá una línea horizontal. Esa es la línea del horizonte (la superficie de la Tierra). El triángulo puntiagudo del centro es un abeto que se ve desde lejos (o una iglesia). (No lo está mirando desde arriba, sino que está delante de él). 

Si no ha cambiado la configuración («Dirección de la mirada: automática»), mirará hacia el sur en el hemisferio norte (y hacia el norte en el hemisferio sur). Los objetos que se encuentran a la izquierda de la pantalla se encuentran al este; los objetos que se encuentran a la derecha de la pantalla se encuentran al oeste (al revés en el hemisferio sur). En el borde del horizonte se encuentran los puntos cardinales correspondientes. 

La franja gris (clara) debajo del horizonte indica la fase del crepúsculo (civil). La gran zona gris oscuro simboliza la noche (incluido el crepúsculo náutico). Los objetos que se encuentran en esta zona no son visibles.

En el borde derecho de la pantalla se muestra la hora local (en formato digital), la posición GPS del lugar en forma de código numérico (por ejemplo, «cri-hs», con una precisión de aproximadamente 4 km) o el nombre del lugar (si lo ha introducido), así como la altura actual del sol en grados en el cielo (por ejemplo, 27,6°). 


[b]–– Sol:[/b]

El sol (al final de la única aguja del reloj) se desplaza a lo largo del día de izquierda a derecha (al revés en el hemisferio sur). Cuanto más a la izquierda se encuentra el sol en la pantalla, más al este está; cuanto más a la derecha, más al oeste (al revés en el hemisferio sur). Cuanto más alto se vea el sol en la pantalla, más alto estará en el cielo. 

El sol sigue la trayectoria circular dibujada, por la que se mueve a lo largo del día. En el borde de la trayectoria circular se indican las horas (por ejemplo, «12» en punto), de modo que la trayectoria circular también funciona como esfera de reloj. 

En la esfera se puede ver, por ejemplo, cómo durante el cambio de hora se desplazan los números, pero la trayectoria circular permanece igual. O cómo la hora legal difiere de la hora local en la mayoría de los lugares, ya que las 12 en punto no se encuentran exactamente en la parte superior de la esfera.""",
        'txanleitung2b': chr(10)+chr(10)+"""[b]–– Luna:[/b]

La luna también tiene una órbita. Se representa como un círculo gris claro (sin agujas). Dado que la luna tarda más de 24 horas en completar una órbita, se añaden dos horas adicionales (del día anterior) en gris extra claro. Si «vives con el reloj», puedes ver claramente cómo la Luna se eleva y desciende periódicamente a lo largo de las semanas. Además, puedes observar cómo, en luna llena, se encuentra en posición opuesta al Sol (lejos), mientras que en luna nueva se encuentra en la misma posición (cerca del Sol). Por lo general, no es exactamente la misma posición, ya que se ve desde un lado (y no desde arriba). Solo durante un eclipse solar se encuentra exactamente en la misma posición. 

La luna llena y la luna nueva se indican (mediante la sombra dibujada). La luna nueva se representa durante 35 horas (porque ese es el tiempo durante el cual no se puede ver la luna en absoluto). La luna llena se representa durante 24 horas. (El recálculo de la órbita del sol y la luna tiene lugar a las 00:00 UTC).


[b]–– Planetas:[/b]

Se muestran los cinco planetas visibles a simple vista, representados por sus símbolos astronómicos (véase la leyenda de la página anterior). Si observa el cielo estrellado real, puede distinguir los planetas de las estrellas sabiendo que los planetas no parpadean, sino que brillan constantemente, ya que parecen mucho más grandes que las estrellas lejanas y, por lo tanto, no se ven tan afectados por las fluctuaciones de densidad de la atmósfera.


[b]–– Estrellas:[/b]

A continuación se muestran las diez estrellas más brillantes, simbolizadas por una letra dentro de un cuadrado (véase la leyenda de la página anterior). Mientras que los planetas se encuentran relativamente ordenados, en su mayoría más o menos cerca de la órbita solar, la órbita de las estrellas es independiente del Sol (ya que son su propio sol). Por lo tanto, en los símbolos de las estrellas, dos lados del cuadrado siempre están dibujados con más intensidad que los otros dos. Esto indica la esquina (o el cuadrante de su órbita) en la que se encuentran actualmente. Si la esquina resaltada está en la parte inferior derecha, eso es (más o menos) el «final» de la órbita hacia abajo y hacia la derecha, y la estrella se moverá principalmente hacia arriba y hacia la izquierda en sus movimientos posteriores (a menudo también fuera de la pantalla).


[b]–– Historia:[/b]

«El reloj de sol de Gordon» se desarrolló en 2019 para una Raspberry Pi con una pantalla ePaper de 10 pulgadas, ya que quería tener un reloj de pared que fuera agradable a la vista y que relacionara la hora con la trayectoria del sol. Mi objetivo era construir un reloj que mostrara la hora natural, no la hora artificial, como la que muestra el reloj analógico de 12 horas. Donde vivimos, hay una diferencia significativa en la duración de los días a lo largo del año, así como el recurrente y poco apreciado cambio de hora. El reloj solar debía poner todo esto en perspectiva: muestra una esfera orgánica que se orienta según las estaciones, el ritmo de la naturaleza, y cambia con él. Dado que hoy en día casi todo el mundo lleva un pequeño ordenador en el bolsillo, he desarrollado Reloj de sol 2025 como aplicación para Android. ¡Que lo disfruten y aprendan mucho con él!"""+chr(10)+chr(10)+chr(10),
        'txabout': chr(10)+'Info',
        'txanleitungprg': chr(10)+"""Reloj de sol de Gordon
Versión """+code_version+""" [i](zunclock)[/i]
Gordon Axmann
Copyright 2019-"""+code_year,
        "txanleitung3": chr(10)+f"""Por regla general, este programa no recopila ningún dato ni me lo envía. Todo permanece en tu dispositivo. Reloj de sol ni siquiera necesita conexión a Internet para funcionar. Hay una excepción: en caso de error del programa, Reloj de sol envía el mensaje de error (siempre que tengas conexión a Internet) junto con el número de versión, la versión del sistema operativo y un UUID aleatorio a mi sitio web. De este modo, contribuyes a mejorar Reloj de sol.
 
Este software es una oferta gratuita y privada, para la que solo puedo ofrecer asistencia técnica limitada. Utilice el software tal y como está. No soy un desarrollador de aplicaciones profesional. Sin embargo, he dedicado mucho esfuerzo y dedicación a este software a lo largo de los años.

Si encuentra un error, estaré encantado de corregirlo si recibo un informe claro y completo del mismo, con una captura de pantalla y una descripción detallada de dónde (por qué) y cuándo se produjo el error y, a ser posible, una captura de pantalla del registro de estado que aparece a continuación (correo electrónico de contacto: {cf.owneremail}) lo antes posible después de que se produzca el error. Las indicaciones sobre errores de cálculo son, en el 99 % de los casos, informes falsos. El cálculo de las estrellas es muy complejo y da demasiada información errónea.

Gracias a Rhodes Mill, Rolf, Greg Miller y a todos los probadores. Imágenes de los cuerpos celestes: NASA/SOHO, ESA/Hubble, NASA/JPL-Caltech

«El reloj de sol» es un software libre. Simplemente disfrute de su uso. Si desea expresar su agradecimiento por mi trabajo, aquí encontrará mi página web:"""+chr(10)+chr(10),
        'txkaffee': "Ir a la página web",
        'txanleitung4': chr(10)+""" """,

    },
    
    'fr': {
        'txsettings': chr(10)+'Cadran solaire de Gordon',
        'txwelcome': 'Bienvenue', # ne pas SUPPRIMER, important pour vérifier si le pack de langue existe
        'wdaysh': ["Lu", "Ma", "Me", "Je", "Ve", "Sa", "Di"],
        'xxdays': ['{day} jour', '{day} jours'], # singulier, pluriel
        'himmelsr': ["E", "S", "O", "N"],
        'txgps_label': chr(10)+'Position GPS ou nom de lieu:',
        'txgpsauto': 'GPS auto (grossier):',
        'txgpsautosh': 'AUTO',
        'txtimezone': 'Fuseau horaire:',
        'txtimeformat': 'Format 24h:',
        'txwelcomescr': 'Désactiver l\'indication GPS:',
        'txedgescreen': 'Plus de bordure:',
        'txenlargeobj': 'Grands symboles:',
        'txuhrsinn': 'Direction du regard:',
        'txuhrsinnarr': {'auto': 'automatique', 'nord': 'Nord', 'sued': 'Sud'},
        'txfullscr': 'Toujours actif:',
        'txnachtmodus': 'Mode sombre:',
        'txnachtmodusarr': {'auto': 'automatique', 'auto_lang': 'auto (plus)', 'auto_kurz': 'auto (moins)', 'day': 'clair', 'night': 'sombre'},
        'txfarben': 'Design:',
        'txfarbenarr': {'orig': 'Nuances de gris', 'c-turn': 'Couleur', 'a-gord': 'Art', 'a-telesk': 'Télescope'},
        'txstatuslog': "[b]–– Journal d'état:[/b]",
        'txgpsinstruct': wrap_text("Pour ajuster votre position GPS, balayez vers la gauche", lang='fr'),
        'txgpsdeact': wrap_text("Le GPS est désactivé. Veuillez activer le GPS dans les paramètres de votre appareil", lang='fr'),
        'uebanleitung': 'Instructions',
        'txanleitung': chr(10)+"""Pour adopter automatiquement votre position GPS, cochez la case «GPS automatique». Pendant que vous utilisez l'application, votre position GPS sera déterminée rapidement et de manière économe en énergie avec une approximation. - Alternativement, vous pouvez entrer une position GPS fixe séparée par des virgules dans le champ de texte (puis cochez «Désactiver l'indication GPS») ou entrer un nom de lieu dans le champ. Lorsque les coordonnées (et d'autres données de base) sont modifiées, l'application effectue un calcul qui peut prendre entre 2 et 30 secondes selon l'appareil. Ce calcul est valable pour une journée.

Le fuseau horaire et la langue devraient être automatiquement repris de votre téléphone mobile. Vous pouvez choisir entre un format 12h et 24h pour l'heure. Sous Design, vous pouvez choisir différentes représentations. Pour le mode sombre, vous pouvez choisir clair, sombre ou commutation automatique. «Automatique» passe en mode sombre au coucher du soleil, «auto (moins)» passe à la fin du crépuscule (-6°), «auto (plus)» passe à +6°.

«Plus de bordure» est pour les appareils sans bord. Avec «Direction du regard», vous pouvez définir si l'horloge doit tourner dans le sens des aiguilles d'une montre (Sud) ou dans le sens inverse (Nord). (Veuillez noter: si vous changez le sens de rotation, la partie du cercle solaire qui est sous l'horizon ne sera plus derrière vous, mais devant vous. Plus de détails ci-dessous.)

«Grands symboles» dessine les objets sur le cadran plus grands. «Toujours actif» empêche l'écran de s'éteindre. J'ai par exemple accroché une ancienne [i]tablette[/i] avec «Cadran solaire» au mur pour ma nièce, afin qu'elle soit toujours visible.

Si vos paramètres ne sont pas pris en compte, vous pouvez appuyer sur le bouton de mise à jour en bas à droite.


[b]–– Cadran:[/b]

Une explication détaillée de la lecture du cadran se trouve sur la page suivante (veuillez balayer vers la gauche).


[b]–– Plus de détails:[/b]

Tous les calculs sont effectués pour votre emplacement local et devraient correspondre aux positions de l'almanach astronomique à 0,0005 seconde d'arc près (la lune, par exemple, est au maximum de 2047 secondes d'arc). - Pleine lune et nouvelle lune (dans/avant jours)"""+chr(10),
        'txobjdata': """Pleine lune: {moon_full}
Nouvelle lune: {moon_new}
Lune éclairée: {moon_illum}
Taille de la lune: {moon_sizep} (85-100)

Luminosité:
Vénus: {venus_magp} (83-100)
Mars: {mars_magp} (52-100)
Jupiter: {jupiter_magp} (87-100)
Mercure: {merkur_magp} (0-100)
Saturne: {saturn_magp} (77-100)


[b]–– Légende:[/b]""",
        'txlegende': chr(10)+"""☉ Soleil, ● Lune (avec phases)

♀ Vénus (couleur perle), ♂ Mars (rougeâtre), ♃ Jupiter (rayé), ☿ Mercure (gris), ♄ Saturne (avec anneaux)

[s] Sirius, [k] Canopus, [f] Alpha Centauri, [a] Arcturus, [w] Véga, [c] Capella, [r] Rigel, [p] Procyon, [b] Bételgeuse, [h] Achernar""",
        'txmore': " "+chr(10)+chr(10),
        'txmanual': chr(10)+'Cadran',
        'txanleitung2': chr(10)+"""«Cadran solaire de Gordon» est en principe une horloge à une aiguille avec un cadran qui change quotidiennement, s'orientant sur les rythmes de la nature et des astres. Il montre la position du soleil et le ciel étoilé. Une nouvelle forme de représentation du temps, qui n'est pas artificielle comme notre horloge habituelle (avec l'heure ferroviaire et le changement d'heure), mais qui évolue en harmonie avec les saisons.

[i]REMARQUE: Vous pouvez naviguer entre ce guide et le cadran en balayant.[/i]


[b]–– Votre regard:[/b]

Au centre de l'écran, vous voyez une ligne horizontale. C'est l'horizon (la surface de la Terre). Le triangle pointu au centre est un sapin vu de loin (ou une église). (Vous ne le regardez pas de haut, mais vous vous tenez devant.)

Si vous n'avez rien modifié dans les paramètres («Direction du regard: automatique»), vous regardez vers le sud dans l'hémisphère nord (et vers le nord dans l'hémisphère sud). Les objets à gauche de l'écran se trouvent à l'est ; ceux à droite, à l'ouest (inversé dans l'hémisphère sud). Les directions cardinales sont indiquées au bord de l'horizon.

La bande (gris clair) sous l'horizon indique la phase de crépuscule (civil). La grande zone gris foncé symbolise la nuit (y compris le crépuscule nautique). Les objets dans cette zone ne sont pas visibles.

À droite de l'écran, vous voyez l'heure locale (en numérique), la position GPS de l'emplacement sous forme de code numérique (par ex. «cri-hs», précis à environ 4 km) ou un nom de lieu (si vous l'avez saisi), ainsi que la hauteur actuelle du soleil en degrés dans le ciel (par ex. 27,6°).


[b]–– Soleil:[/b]

Le soleil (à l'extrémité de l'unique aiguille de l'horloge) se déplace de gauche à droite au cours de la journée (inversé dans l'hémisphère sud). Plus le soleil est à gauche sur l'écran, plus il est à l'est ; plus il est à droite, plus il est à l'ouest (inversé dans l'hémisphère sud). Plus le soleil est haut sur l'écran, plus il est élevé dans le ciel.

Le soleil suit la trajectoire circulaire dessinée, sur laquelle il se déplace en une journée. Des heures (par ex. «12») sont indiquées sur le bord de cette trajectoire, qui sert également de cadran.

Sur le cadran, par exemple, on peut voir comment, lors du changement d'heure, les chiffres se décalent, mais la trajectoire reste la même. Ou encore: comment l'heure légale diffère de l'heure locale dans la plupart des endroits, car midi n'est pas exactement en haut du cadran.""",
        'txanleitung2b': chr(10)+chr(10)+"""[b]–– Lune:[/b]

La lune a également une orbite. Elle est dessinée en cercle gris clair (sans aiguille). Comme la lune met plus de 24 heures pour un tour, deux heures supplémentaires (de la veille) sont ajoutées en gris très clair. En «vivant avec l'horloge», on peut observer comment la lune monte et descend périodiquement sur des semaines. De plus, on peut voir qu'à la pleine lune, elle est à l'opposé du soleil sur le cercle (loin) ; à la nouvelle lune, elle est à la même position (proche du soleil). Ce n'est généralement pas exactement la même position, car on regarde de côté (et non de dessus). Elle est exactement identique uniquement lors d'une éclipse solaire.

Pleine lune et nouvelle lune sont indiquées (par l'ombre dessinée). La nouvelle lune est représentée pendant 35 heures (temps pendant lequel la lune est invisible). La pleine lune est représentée pendant 24 heures. (Le recalcul des orbites du soleil et de la lune a lieu chaque jour à 00:00 UTC.)


[b]–– Planètes:[/b]

Les cinq planètes visibles à l'œil nu sont affichées, représentées par leurs symboles astronomiques (voir légende page précédente). En observant le vrai ciel étoilé, vous pouvez distinguer les planètes des étoiles, car les planètes brillent constamment sans scintiller, semblant beaucoup plus grandes que les étoiles lointaines et donc moins affectées par les variations de densité de l'atmosphère.


[b]–– Étoiles:[/b]

Les dix étoiles les plus brillantes sont également affichées, symbolisées par une lettre dans un carré (voir légende page précédente). Alors que les planètes restent relativement ordonnées, souvent près de l'orbite solaire, les étoiles ont une trajectoire indépendante du soleil (étant elles-mêmes des soleils). Pour les symboles des étoiles, deux côtés du carré sont toujours plus épais que les autres, indiquant le coin (ou le quadrant de leur orbite) où elles se trouvent actuellement. Si le coin mis en évidence est en bas à droite, cela marque (plus ou moins) la «fin» de leur trajectoire vers le bas et la droite, et l'étoile se déplacera ensuite principalement vers le haut et la gauche (souvent hors de l'écran).


[b]–– Historique:[/b]

«Cadran solaire de Gordon» a été développé en 2019 pour un Raspberry Pi avec un écran ePaper de 10 pouces, car je voulais une horloge murale agréable à regarder et qui relie le temps au mouvement du soleil. Mon objectif était de créer une horloge montrant un temps naturel, pas un temps artificiel comme celui de l'horloge analogique 12 heures. Là où nous vivons, il y a une différence notable dans la longueur des jours au fil de l'année, et aussi le changement d'heure récurrent et peu apprécié. Le cadran solaire devait mettre tout cela en perspective: il affiche un cadran organique, orienté sur les saisons, en rythme avec la nature et évoluant avec elle. – Comme presque tout le monde a aujourd'hui un petit ordinateur dans sa poche, j'ai développé Cadran solaire en 2025 comme une application Android. Beaucoup de plaisir et de découvertes avec !"""+chr(10)+chr(10)+chr(10),
        'txabout': chr(10)+'Info',
        'txanleitungprg': chr(10)+"""Cadran solaire de Gordon
Version """+code_version+""" [i](zunclock)[/i]
Gordon Axmann
Copyright 2019-"""+code_year,
        'txanleitung3': chr(10)+f"""En principe: aucune donnée n'est collectée ou envoyée par ce programme. Tout reste sur votre appareil. Pour utiliser Cadran solaire, une connexion Internet n'est même pas nécessaire. - Il y a une exception: en cas d'erreur du programme, Cadran solaire (si vous avez Internet) envoie le message d'erreur avec le numéro de version, la version du système d'exploitation et un UUID aléatoire à mon site web (voir politique de confidentialité). Cela aide à améliorer les erreurs dans Cadran solaire.

Ce logiciel est une offre gratuite et privée, pour laquelle je ne peux fournir qu'un support limité. Veuillez utiliser le logiciel tel quel. Je ne suis pas un développeur d'applications professionnel. Néanmoins, beaucoup de cœur a été investi dans ce logiciel au fil des années.

Si vous trouvez une erreur, je la corrigerai volontiers si je reçois un rapport d'erreur clair et complet, avec une capture d'écran et une description précise de où, comment et quand l'erreur s'est produite, et idéalement une capture du journal d'état ci-dessous (contact par e-mail: {cf.owneremail}) dès que possible après l'erreur. Les signalements d'erreurs de calcul sont, dans 99 % des cas, des fausses alertes. Le calcul des étoiles est très complexe et génère trop d'informations erronées.

Merci à Rhodes Mill, Rolf, Greg Miller et tous les testeurs. Images des corps célestes: NASA/SOHO, ESA/Hubble, NASA/JPL-Caltech

«Cadran solaire» est un logiciel libre. Profitez simplement de son utilisation. Si vous souhaitez exprimer votre appréciation pour mon travail, voici mon site web:"""+chr(10)+chr(10),
        'txkaffee': 'Accéder au site web',
        'txanleitung4': chr(10)+""" """,
    }

}

