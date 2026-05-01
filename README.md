# PDF-Rechnungen-Werte-Extrahieren-
Liest PDF Rechunen aus und extrahiert die Werte in eine CSV Datei

Dieses Python-Skript automatisiert die Extraktion spezifischer Rechnungsdaten aus PDF-Dokumenten und exportiert diese gesammelt in eine übersichtliche CSV-Datei. Es ist besonders nützlich, um wiederkehrende Informationen aus Spesenabrechnungen oder Quittungen schnell und ohne manuellen Aufwand zu digitalisieren.  
So sieht das Resultat aus:
<img width="416" height="170" alt="Unbenannt" src="https://github.com/user-attachments/assets/c2170f9f-c303-48a8-a955-94cd90cef052" />

🚀 Funktionen
Das Skript verarbeitet alle PDF-Dateien im Ausführungsverzeichnis und extrahiert gezielt folgende Daten:  

Bezahlt von: Sucht nach dem Begriff und extrahiert den zugehörigen numerischen Geldbetrag.  

Trinkgeld: Sucht nach dem Begriff und extrahiert den zugehörigen numerischen Geldbetrag.  

Flughafengebühr: Prüft, ob der Begriff im Dokument vorkommt, und markiert dies bei einem Treffer mit einem x.  

Balance: Prüft, ob der Begriff im Dokument vorkommt, und markiert dies bei einem Treffer mit einem x.  

Zusätzliche Features:

Textnormalisierung: Für eine fehlerunanfälligere Suche wandelt das Skript den gesamten Text in Kleinbuchstaben um und entfernt Umlaute sowie diakritische Zeichen (z. B. wird "ü" zu "u").  

Live-Feedback & Zusammenfassung: Das Skript gibt in der Konsole in Echtzeit aus, welche Dateien erfolgreich verarbeitet oder übersprungen wurden, und liefert am Ende eine übersichtliche Zusammenfassung der Ergebnisse.  

📋 Voraussetzungen
Stelle sicher, dass Python auf deinem System installiert ist. Das Skript nutzt überwiegend Python-Standardbibliotheken (os, re, csv, unicodedata), benötigt aber zusätzlich das Paket pdfplumber zum Auslesen der PDFs.



