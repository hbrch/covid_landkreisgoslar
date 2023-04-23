import os
import smtplib, ssl
from email.message import EmailMessage

msg_from = os.environ.get('EMAIL_USER')
msg_to = os.environ.get('EMAIL_LIST')
email_pass = os.environ.get('EMAIL_PASS')

def email_excel():
    msg = EmailMessage()
    msg['Subject'] = 'Aktualisierte COVID-Daten im Landkreis Goslar'
    msg['From'] = msg_from
    msg['To'] = msg_to
    msg.set_content('Daten zum Corona Virus für den Landkreis Goslar')

    with open('covid19_goslar.csv', 'rb') as f:
        file_data = f.read()

    msg.add_attachment(file_data, maintype="application", subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename='covid19_goslar.csv')

    context=ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg_from, email_pass)

        smtp.send_message(msg)
