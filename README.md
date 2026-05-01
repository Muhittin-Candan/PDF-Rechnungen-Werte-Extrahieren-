# PDF-Rechnungen-Werte-Extrahieren-
Liest PDF Rechunen aus und extrahiert die Werte in eine CSV Datei

So sieht das Resultat aus:
<img width="416" height="170" alt="Unbenannt" src="https://github.com/user-attachments/assets/c2170f9f-c303-48a8-a955-94cd90cef052" />


# PDF Invoice Value Extractor (`werted.py`)

Dieses Python-Skript automatisiert die Extraktion spezifischer Rechnungsdaten und Beträge aus PDF-Dokumenten. Im Gegensatz zu einfachen Text-Suchern durchsucht dieses Tool die Rechnungen gezielt nach numerischen Werten und exportiert diese gesammelt in eine übersichtliche CSV-Datei. Es ist besonders nützlich, um Spesenabrechnungen oder Quittungen schnell und ohne manuellen Aufwand zu digitalisieren.

## 🚀 Funktionen

Das Skript verarbeitet alle PDF-Dateien im aktuellen Verzeichnis und extrahiert folgende Daten[cite: 1]:

* **Bezahlt von:** Sucht nach dem Begriff und extrahiert den direkt zugehörigen numerischen Geldbetrag (mittels Regex)[cite: 1].
* **Trinkgeld:** Sucht nach dem Begriff und extrahiert den direkt zugehörigen numerischen Geldbetrag[cite: 1].
* **Flughafengebühr:** Prüft, ob der Begriff im Dokument vorkommt, und markiert dies bei einem Treffer mit einem `x`[cite: 1].
* **Balance:** Prüft, ob der Begriff im Dokument vorkommt, und markiert dies bei einem Treffer mit einem `x`[cite: 1].

**Zusätzliche Features:**
* **Intelligente Textnormalisierung:** Um Fehler beim Auslesen zu minimieren, wandelt das Skript den gesamten Text in Kleinbuchstaben um und entfernt Umlaute sowie diakritische Zeichen (z. B. wird "ü" zu "u")[cite: 1].
* **Live-Feedback & Konsolen-Report:** Das Skript gibt in Echtzeit aus, welche Dateien erfolgreich verarbeitet oder übersprungen wurden[cite: 1]. Am Ende liefert es eine statistische Zusammenfassung der Ergebnisse inklusive einer Daten-Vorschau[cite: 1].
* **CSV-Export:** Die extrahierten Werte werden sauber formatiert (UTF-8 mit BOM, ideal für Excel) in der Datei `rechnungen_werte.csv` gespeichert[cite: 1].

## 📋 Voraussetzungen

Stelle sicher, dass Python auf deinem System installiert ist. Das Skript nutzt überwiegend Python-Standardbibliotheken, benötigt für die präzise PDF-Extraktion jedoch das externe Paket `pdfplumber`[cite: 1].

Du kannst die Abhängigkeit über pip installieren:
```bash
pip install pdfplumber
