import json
import os

LANGUAGES = {
    "1": ("Dwarvish", "Dwarvish.json"),
    "2": ("Elvish", "Elvish.json"),
    "3": ("Draconic", "Draconic.json"),
    "4": ("Infernal", "Infernal.json")
}

def load_alphabet(language):
    filename = None
    for key, (lang_name, lang_file) in LANGUAGES.items():
        if lang_name == language:
            filename = lang_file
            break
    
    if not filename:
        raise ValueError(f"Lingua non supportata: {language}")
    
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def translate(text, language):
    alphabet = load_alphabet(language)
    result = []
    for char in text:
        upper_char = char.upper()
        if upper_char in alphabet:
            translated = alphabet[upper_char]
            if char.islower():
                translated = translated.lower()
            result.append(translated)
        else:
            result.append(char)
    return ''.join(result)

def show_menu():
    print("\n" + "="*30)
    print("TRADUTTORE D&D")
    print("="*30)
    print("Scegli la lingua :")
    print()
    for key, (lang_name, _) in LANGUAGES.items():
        print(f"{key}. {lang_name}")
    print("0. Esci")
    print("-" * 50)

def get_language_choice():
    while True:
        try:
            choice = input("Inserisci il numero della lingua (0 per uscire): ").strip()
            if choice == "0":
                return None
            elif choice in LANGUAGES:
                return LANGUAGES[choice][0]
            else:
                print("Scelta non valida")
        except KeyboardInterrupt:
            print("\n Ă̷̢̧͕̟̠̣̗̜͉̠̝̜̼̫ͅḑ̷̛̬̞̟͎̪͇̭̗̫̹͎̒̐͗͒d̴̢̹̤̹̪̣͐̒̌̅́̈̋̄̂̂͗͘͠ͅì̵͇͉̮͕̹̭̠̩͓̜̖̗̙̮̉͌́͐̆̔̂͒̌͑̔͛̋͠ǫ̸͍͖̲̝̼̗̹̜̯͎̦̩̻͆̍̿̈́̅̔̑̈́̀̃̇̌͘")
            return None

def main():
    while True:
        show_menu()
        language = get_language_choice()
        
        if language is None:
            print("Ă̷̢̧͕̟̠̣̗̜͉̠̝̜̼̫ͅḑ̷̛̬̞̟͎̪͇̭̗̫̹͎̒̐͗͒d̴̢̹̤̹̪̣͐̒̌̅́̈̋̄̂̂͗͘͠ͅì̵͇͉̮͕̹̭̠̩͓̜̖̗̙̮̉͌́͐̆̔̂͒̌͑̔͛̋͠ǫ̸͍͖̲̝̼̗̹̜̯͎̦̩̻͆̍̿̈́̅̔̑̈́̀̃̇̌͘")
            break

        print("\nInserisci il testo da tradurre (o 'back' per tornare al menu):")

        text = input("➤ ")
        
        if text.lower() == 'back':
            continue
        
        if not text.strip():
            print("Nessun testo inserito!")
            continue
        
        try:
            translated = translate(text, language)
            print(f"\n traduzione in {language}:")
            print("─" * 30)
            print(f"Traduzione Frase : {translated}")

            input("\nPremi INVIO per continuare")
            
        except Exception as e:
            print(f"Errore durante la traduzione: {e}")
            input("\nPremi INVIO per continuare")

if __name__ == "__main__":
    main()


