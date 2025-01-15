import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

def get_dynamic_response(user_input):
    responses = [
        (re.compile(r'(hallo|hi|guten tag|hey|moin|servus|guten morgen|guten abend|guten mittag)', re.IGNORECASE),
         "Hallo! Wie kann ich Ihnen helfen?"),
        (re.compile(r'(login|passwort|anmeldung|konto|zugang)', re.IGNORECASE),
         "Haben Sie versucht, Ihr Passwort mithilfe der Passwort-Vergessen-Funktion zurückzusetzen? Falls Sie weiterhin Probleme haben, leite ich das Anliegen an unsere höhere technische Abteilung weiter."),
        (re.compile(r'(software|app|programm|installation|update|fehler)', re.IGNORECASE),
         "Können Sie mir bitte mehr Details zu dem Problem geben? Zum Beispiel, welche Software betroffen ist und welche Fehlermeldung angezeigt wird."),
        (re.compile(r'(hardware|gerät|pc|drucker|scanner|usb)', re.IGNORECASE),
         "Prüfen Sie bitte, ob das Gerät eingeschaltet und korrekt angeschlossen ist. Falls das Problem weiterhin besteht, müssen wir eventuell einen Techniker hinzuziehen."),
        (re.compile(r'(netzwerk|internet|verbindung|router|wlan)', re.IGNORECASE),
         "Ist Ihre Netzwerkverbindung stabil? Haben Sie den Router neu gestartet? Falls das Problem weiterhin besteht, kontaktieren Sie bitte Ihren Internetanbieter."),
        (re.compile(r'(email|e-mail|postfach|outlook|smtp|imap|server|post|posteingang|postausgang|versenden|applemail|thunderbird)', re.IGNORECASE),
         "Prüfen Sie bitte, ob Ihre Postfach-Einstellungen korrekt sind. Falls Sie keinen Zugriff haben, wenden Sie sich an Ihren Administrator bezüglich der Zugangsdaten, wie Passwort und Benutzername. Falls Sie Zugriff haben, aber keine E-Mail abrufen und verschicken können, kann es sein, dass eine IP-Sperre vorliegt. Gerne kann ich diese für Sie aufheben. Bitte teilen Sie mir hierzu Ihre aktuelle IPv4 mit. Mithilfe Ihrer IP kann ich im Log nachvollziehen, weshalb diese IP-Sperre aufgetreten ist. Meist liegt dies an fehlerhaften Servereinstellungen. Zur Überprüfung bitte ich Sie, dass Sie mir Ihre Servereinstellungen zuschicken."),
        (re.compile(r'(drucker|druck|drucken|papier)', re.IGNORECASE),
         "Ist der Drucker eingeschaltet und mit dem Netzwerk verbunden? Prüfen Sie bitte auch, ob ausreichend Papier vorhanden ist. Teilen Sie mir ansonsten gerne genauere Informationen mit, damit ich Ihnen zielführend helfen kann."),
        (re.compile(r'(sicherheit|virus|malware|hacker|phishing|schadcode)', re.IGNORECASE),
         "Falls Sie den Verdacht auf einen Sicherheitsvorfall haben, trennen Sie Ihr Gerät vom Netzwerk und informieren Sie umgehend einen Sicherheitsexperten."),
        (re.compile(r'(privat|persönlich|spiel|unterhaltung|spiele|familie|freund|freunde)', re.IGNORECASE),
         "Leider können wir keine Unterstützung für private oder nicht-arbeitsbezogene Anliegen bieten."),
        (re.compile(r'(fehler|problem|störung|hilfe)', re.IGNORECASE),
         "Könnten Sie mir bitte mehr Informationen geben? Was genau funktioniert nicht oder welche Fehlermeldung wird angezeigt?"),
        (re.compile(r'(danke|vielen dank|dankeschön)', re.IGNORECASE),
         "Sehr gerne! Kann ich Ihnen ansonsten noch anderweitig behilflich sein?"),
        (re.compile(r'(wie|was|warum|kann|frage)', re.IGNORECASE),
         "Damit ich Ihr Anliegen/Ihre Frage genauer analysieren kann, benötige ich weitere Informationen."),
        (re.compile(r'(vertrag|verträge|kündigung|geld|bezahlungen|bezahlen|paket|tarif)', re.IGNORECASE),
         "Falls Sie Fragen bezüglich Ihres Tarifs/Ihrer Rechnungen haben, wenden Sie sich bitte an unsere Buchhaltung. Unsere Buchhaltung erreichen Sie per E-Mail unter der E-Mail-Adresse buchhaltung@itsupport.de"),
        (re.compile(r'(backup|sicherung|datenverlust|wiederherstellung)', re.IGNORECASE),
         "Haben Sie versucht, ein Backup einzuspielen? Falls Sie kein Backup erstellt haben, bieten wir Ihnen an, dass wir ein Backup für Sie einspielen. Dieser Dienst ist mit Kosten in der Höhe von 1€ je angefangene Minute zu berechnen."),
    ]

    for pattern, response in responses:
        if pattern.search(user_input):
            return response

    return "Ich werde mein Bestes tun, Ihnen zu helfen! Bitte beschreiben Sie Ihr Problem genauer!"

def send_message():
    user_input = user_entry.get()
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "Sie: " + user_input + "\n")
        response = get_dynamic_response(user_input)
        
        if response == "Sehr gerne! Kann ich Ihnen ansonsten noch anderweitig behilflich sein?":
            global follow_up
            follow_up = True
        elif follow_up:
            if re.search(r'ja', user_input, re.IGNORECASE):
                response = "Wie kann ich Ihnen weiter helfen?"
                follow_up = False
            elif re.search(r'nein', user_input, re.IGNORECASE):
                response = "Wenn Sie weitere Hilfe brauchen, kommen Sie wieder!"
                chat_log.insert(tk.END, "Bot: " + response + "\n")
                root.after(5000, root.quit)
                return

        chat_log.insert(tk.END, "Bot: " + response + "\n")
        chat_log.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)

def on_closing():
    if messagebox.askokcancel("Beenden", "Möchten Sie den Chatbot wirklich beenden?"):
        root.destroy()

follow_up = False

root = tk.Tk()
root.title("IT-Support-Chatbot")

chat_log = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20)
chat_log.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=(0, 10))
user_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Senden", command=send_message)
send_button.pack(pady=(0, 10))

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()