# Changelog
All notable changes to this project will be documented in this file (tags: Added, Changed, Deprecated, Removed, Fixed, Security).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.20] - 2025-07-04

### Added
- Tageslichtdaten ergänzt
- Design Teleskop 2 ergänzt, 

### Changed
- Navigationsbuttons geändert,
- 'NoneType' object has no attribute 'width' fixed,  

## [2.19] - 2025-07-03

### Added
- Chinesisch ergänzt,

### Changed
- Navigationsbuttons geändert,
- Reihenfolge Designs geändert,
- lang_create creates lang_cont from lang directory,
- androidapi 35,
- gradle_dependencies angepasst,
- LocationManager angepasst, 

## [2.18-public] - 2025-06-29

### Added
- Anzeige vergangener Neumond ergänzt
- OSM Email ergänzt

### Changed
- Teleskop-Mondschatten aufgehellt
- Teleskop: Unter-Horizont gefärbt

## [2.16] - 2025-06-26

### Added
- Französisch ergänzt
- Sprachwähler ergänzt

### Changed
- Teleskop: Größenrelation geändert
- Teleskop: Unter-Horizont dunkleres Grau

## [2.15-public] - 2025-06-24

### Added/Removed
- Designs aufgeräumt (Teleskop ergänzt in de, Testdesigns entfernt)

### Fixed
- Zeitzone wurde ggf. nicht gespeichert

## [2.14] - 2025-06-23

### Added
- Designwähler ergänzt (mit testweisen Designs)
- Fehlermeldungen werden gemeldet

### Changed
- Texte neu übersetzt
- Logo neu

### Fixed
- gelegentl. Fehler beim Speichern der Einstellungen behoben

## [2.13] - 2025-06-18

### Added
- Merkur ergänzt
- O/W im Horizont ergänzt
- Planetenhelligkeiten ersetzen Planetengrößen 

### Changed
- Mondschatten war etwas zu groß

### Removed
- ISS entfernt

## [2.12] - 2025-06-16

### Added
- Option „Objekte größer zeichnen“ ergänzt
- Planetengrößen in "Mehr Details" ergänzt
- ISS hinzugefügt

### Changed
- Neuzeichnen des Ziffernblatts bei gleichen Koordinaten beschleunigt
- Ortsabfragen beschleunigt (Zwischenspeicher)

## [2.11] - 2025-06-14

### Added
- Abschnitt "Mehr Details" ergänzt

### Changed
- Texte auf drei Seiten aufgeteil wegen Renderproblemen

## [2.10] - 2025-06-12

### Changed
- Vorabskizze bei langsamen Geräten noch schneller

### Fixed
- GPS-Hinweis Schriftart korrigiert

## [2.9] - 2025-06-11

### Fixed
- Anleitung wurde nicht gerendert
- lokale Sonnendaten wurden nach Update gelöscht

## [2.8] - 2025-06-11

### Added
- Startet nun schneller (zeigt Vorabskizze bis alle Berechnungen durchgeführt)
- dritte Seite eingeführt wegen gelegentl. Darstellungsfehler mit Fließtext

### Changed
- Sonne war auf verschiedenen Geräten zu groß/klein

### Fixed
- Mondstruktur war 1 Pixel zu klein

## [2.7] - 2025-06-09

### Changed
- "Mehr Rand" verschiebt nun auch die Texte
- Schriftart gewechselt

### Fixed
- Ziffernstriche von Mond waren z.T. falsch herum
- fehlende Digitalzeit korrigiert

## [2.6] - 2025-06-08

### Fixed
- "Mehr Rand" funktioniert nun auch beim Start
- Mondschatten war 1 Pixel zu klein

## [2.5] - 2025-06-07

### Added
- Einstellung "Blickrichtung" ergänzt für fixe Blickrichtung
- Einstellung "mehr Rand" ergänzt für randlose Geräte

### Changed
- Texte aktualisiert

## [2.4] - 2025-06-06

### Changed
- Texte aktualisiert

### Fixed
- Mondstruktur 1 Pixel zu groß

## [2.3] - 2025-06-05

### Changed
- Rechts-links-Wischen-Abfrage wurde verbessert
- Mondkreis heller
- Texte aktualisiert
- clock_timing verbessert

### Fixed
- Einstellungen wurden beim Update überschrieben

## [2.2] - 2025-06-04

### Changed
- Schriftformatierung verbessert

### Fixed
- Farbschema flackerte

## [2.1] - 2025-06-03

### Added
- OSM-Ortssuche für GPS-Koordinaten ergänzt, Anzeige derselben auf dem Ziffernblatt

### Changed
- Checkboxen besser sichtbar

### Fixed
- Speichern der Auto-GPS-Einstellung funktionierte nicht

## [2.0] - 2025-06-01

### Added
- Erstveröffentlichung Androidversion
- Sonnen- und Mondkreis ergänzt
- Horizont, Höhenlinien, Uhrzeiten ergänzt

## [alpha.0.1 - alpha.0.7] - 2025-05-21..2025-06-01

### Added
- Framework erstellt
- 2 Seiten erstellt (Ziffernblatt, Einstellungen)
- Uhrzeitanzeige
- Sonne, Mond und Sirius hinzugefügt
- GPS-Abfrage ergänzt

## [1.0] - 2019-11

### Added
- Erste Version auf Raspberry Pi
