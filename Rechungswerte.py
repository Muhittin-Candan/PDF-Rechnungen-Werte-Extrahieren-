import os
import re
import csv
import pdfplumber
import unicodedata

def normalize_text(text):
    """Normalisiere Text für zuverlässigere String-Vergleiche."""
    # Entferne diakritische Zeichen (z.B. ü -> u)
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return text.lower().strip()

def extract_values_from_pdf(pdf_path):
    """
    Extrahiert die Werte aus einer PDF-Rechnung gemäß den Anforderungen:
    - "Bezahlt von": Extrahiert den numerischen Wert
    - "Trinkgeld": Extrahiert den numerischen Wert  
    - "Flughafengebühr": Markiert mit 'x' wenn Begriff vorkommt
    - "Balance": Markiert mit 'x' wenn Begriff vorkommt
    """
    bezahlt_von = ""
    trinkgeld = ""
    flughafengebuehr = ""
    balance = ""
    has_values = False

    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"

    # Normalisiere den gesamten Text für die Suche
    normalized_text = normalize_text(full_text)
    
    # Zerlege in Zeilen für die detaillierte Suche
    lines = full_text.split('\n')
    
    for line in lines:
        # Normalisiere die aktuelle Zeile
        normalized_line = normalize_text(line)
        
        # Suche nach "Bezahlt von" und extrahiere den Wert
        if "bezahlt von" in normalized_line:
            numbers = re.findall(r'[-]?\d+[.,]\d{2}', line.replace(',', '.'))
            if numbers:
                bezahlt_von = numbers[0]
                has_values = True
        
        # Suche nach "Trinkgeld" und extrahiere den Wert
        if "trinkgeld" in normalized_line:
            numbers = re.findall(r'[-]?\d+[.,]\d{2}', line.replace(',', '.'))
            if numbers:
                trinkgeld = numbers[0]
                has_values = True
    
    # Prüfe auf "Flughafengebühr" im gesamten Text
    if "flughafengebuhr" in normalized_text:
        flughafengebuehr = "x"
        has_values = True
    
    # Prüfe auf "Balance" im gesamten Text
    if "balance" in normalized_text:
        balance = "x"
        has_values = True
    
    return bezahlt_von, trinkgeld, flughafengebuehr, balance, has_values

def main():
    pdf_dir = "."
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    
    results = []
    processed_count = 0
    skipped_count = 0
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        try:
            bezahlt_von, trinkgeld, flughafengebuehr, balance, has_values = extract_values_from_pdf(pdf_path)
            
            if has_values:
                file_name_without_ext = os.path.splitext(pdf_file)[0]
                results.append([file_name_without_ext, bezahlt_von, trinkgeld, flughafengebuehr, balance])
                processed_count += 1
                print(f"✓ Verarbeitet: {pdf_file}")
            else:
                skipped_count += 1
                print(f"✗ Übersprungen: {pdf_file} (keine relevanten Werte gefunden)")
                
        except Exception as e:
            skipped_count += 1
            print(f"✗ Fehler bei {pdf_file}: {str(e)[:50]}...")
    
    # CSV-Datei schreiben
    if results:
        csv_file = "rechnungen_werte.csv"
        with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(["PDF-Datei", "Bezahlt von", "Trinkgeld", "Flughafengebühr", "Balance"])
            writer.writerows(results)
        
        print(f"\n✅ CSV-Datei '{csv_file}' wurde erfolgreich erstellt!")
        print(f"📊 Verarbeitet: {processed_count} Dateien")
        print(f"⏭️  Übersprungen: {skipped_count} Dateien")
        
        # Zeige eine Zusammenfassung
        print("\n📋 Zusammenfassung der erfassten Werte:")
        
        # Zähle die verschiedenen Werte
        bezahlt_count = sum(1 for row in results if row[1])
        trinkgeld_count = sum(1 for row in results if row[2])
        flughafen_count = sum(1 for row in results if row[3] == "x")
        balance_count = sum(1 for row in results if row[4] == "x")
        
        print(f"  Bezahlt von: {bezahlt_count} Dateien")
        print(f"  Trinkgeld: {trinkgeld_count} Dateien")
        print(f"  Flughafengebühr (x): {flughafen_count} Dateien")
        print(f"  Balance (x): {balance_count} Dateien")
            
        # Zeige erste 5 Einträge als Beispiel
        print("\n📄 Beispiel (erste 5 Einträge):")
        for i, row in enumerate(results[:5]):
            print(f"  {i+1}. {row[0]}: "
                  f"Bezahlt={row[1] if row[1] else '-'}, "
                  f"Trinkgeld={row[2] if row[2] else '-'}, "
                  f"Flughafen={row[3] if row[3] else '-'}, "
                  f"Balance={row[4] if row[4] else '-'}")
    else:
        print("\n❌ Keine PDF-Dateien mit relevanten Werten gefunden.")

if __name__ == "__main__":
    main()