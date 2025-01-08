import random
import re

def get_dynamic_response(user_input):
    responses = [
        # Begrüßung
        (re.compile(r'(hallo|hi|guten tag|hey|moin|servus|guten morgen|guten abend|guten mittag)', re.IGNORECASE),
         "Hallo! Wie kann ich Ihnen helfen?"),

        # Login Probleme
        (re.compile(r'(login|passwort|anmeldung|konto|zugang)', re.IGNORECASE),
         "Haben Sie versucht, Ihr Passwort mithilfe der Passwort-Vergessen-Funktion zurückzusetzen? Falls Sie weiterhin Probleme haben, leite ich das Anliegen an unsere höhere technische Abteilung weiter."),

        # Software Probleme
        (re.compile(r'(software|app|programm|installation|update|fehler)', re.IGNORECASE),
         "Können Sie mir bitte mehr Details zu dem Problem geben? Zum Beispiel, welche Software betroffen ist und welche Fehlermeldung angezeigt wird."),

        # Hardware Probleme
        (re.compile(r'(hardware|gerät|pc|drucker|scanner|usb)', re.IGNORECASE),
         "Prüfen Sie bitte, ob das Gerät eingeschaltet und korrekt angeschlossen ist. Falls das Problem weiterhin besteht, müssen wir eventuell einen Techniker hinzuziehen."),

        # Netzwerk Probleme
        (re.compile(r'(netzwerk|internet|verbindung|router|wlan)', re.IGNORECASE),
         "Ist Ihre Netzwerkverbindung stabil? Haben Sie den Router neu gestartet? Falls das Problem weiterhin besteht, kontaktieren Sie bitte Ihren Internetanbieter."),

        # E-Mail Probleme
        (re.compile(r'(email|e-mail|postfach|outlook|smtp|imap|server|post|posteingang|postausgang|versenden|applemail|thunderbird)', re.IGNORECASE),
         "Prüfen Sie bitte, ob Ihre Postfach-Einstellungen korrekt sind. Falls Sie keinen Zugriff haben, wenden Sie sich an Ihren Administrator bezüglich der Zugangsdaten, wie Passwort und Benutzername. Falls Sie Zugriff haben, aber keine E-Mail abrufen und verschicken können, kann es sein, dass eine IP-Sperre vorliegt. Gerne kann ich diese für Sie aufheben. Bitte teilen Sie mir hierzu Ihre aktuelle IPv4 mit. Mithilfe Ihrer IP kann ich im Log nachvollziehen, weshalb diese IP-Sperre aufgetreten ist. Meist liegt dies an fehlerhaften Servereinstellungen. Zur Überprüfung bitte ich Sie, dass Sie mir Ihre Servereinstellungen zuschicken."),

        # Druckerprobleme
        (re.compile(r'(drucker|druck|drucken|papier)', re.IGNORECASE),
         "Ist der Drucker eingeschaltet und mit dem Netzwerk verbunden? Prüfen Sie bitte auch, ob ausreichend Papier vorhanden ist. Teilen Sie mir ansonsten gerne genauere Informationen mit, damit ich Ihnen zielführend helfen kann."),

        # Sicherheitsnachfragen 
        (re.compile(r'(sicherheit|virus|malware|hacker|phishing|schadcode)', re.IGNORECASE),
         "Falls Sie den Verdacht auf einen Sicherheitsvorfall haben, trennen Sie Ihr Gerät vom Netzwerk und informieren Sie umgehend einen Sicherheitsexperten."),

        # Nicht gegebene Services
        (re.compile(r'(privat|persönlich|spiel|unterhaltung|spiele|familie|freund|freunde)', re.IGNORECASE),
         "Leider können wir keine Unterstützung für private oder nicht-arbeitsbezogene Anliegen bieten."),

        # Allgemeine Worte wie "fehler", "problem", etc.
        (re.compile(r'(fehler|problem|störung|hilfe)', re.IGNORECASE),
         "Könnten Sie mir bitte mehr Informationen geben? Was genau funktioniert nicht oder welche Fehlermeldung wird angezeigt?"),

        # Bedanken
        (re.compile(r'(danke|vielen dank|dankeschön)', re.IGNORECASE),
         "Sehr gerne! Kann ich Ihnen ansonsten noch anderweitig behilflich sein?"),

        # Generelle Hilfe
        (re.compile(r'(wie|was|warum|kann|frage)', re.IGNORECASE),
         "Damit ich Ihr Anliegen/Ihre Frage genauer analysieren kann, benötige ich weitere Informationen."),

        # Verträge / Buchhaltung
        (re.compile(r'(vertrag|verträge|kündigung|geld|bezahlungen|bezahlen|paket|tarif)', re.IGNORECASE),
         "Falls Sie Fragen bezüglich Ihres Tarifs/Ihrer Rechnungen haben, wenden Sie sich bitte an unsere Buchhaltung. Unsere Buchhaltung erreichen Sie per E-Mail unter der E-Mail-Adresse buchhaltung@itsupport.de"),
        
        # Backups
        (re.compile(r'(backup|sicherung|datenverlust|wiederherstellung)', re.IGNORECASE),
         "Haben Sie versucht, ein Backup einzuspielen? Falls Sie kein Backup erstellt haben, bieten wir Ihnen an, dass wir ein Backup für Sie einspielen. Dieser Dienst ist mit Kosten in der Höhe von 1€ je angefangene Minute zu berechnen."),
    ]

    for pattern, response in responses:
        if pattern.search(user_input):
            return response

    return "Ich werde mein Bestes tun, Ihnen zu helfen! Bitte beschreiben Sie Ihr Problem genauer!"

def chatbot():
    print("Willkommen beim IT-Support-Chatbot. Wie kann ich Ihnen helfen?")
    print("Bitte beschreiben Sie Ihr Problem so genau wie möglich.")

    while True:
        user_input = input("Ihre Frage oder Beschreibung (oder 'exit' zum Beenden): ").strip().lower()

        if user_input in ['exit', 'nein', 'nö', 'ne']:
            print("Vielen Dank, dass Sie den IT-Support-Chatbot genutzt haben. Auf Wiedersehen!")
            break

        response = get_dynamic_response(user_input)

        print("\nAntwort:", response)

if __name__ == "__main__":
    chatbot()