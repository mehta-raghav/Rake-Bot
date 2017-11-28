import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sender(toID, body, name):
    emailaddr = "subscribe.ai.client@gmail.com"
    toaddr = toID
    msg = MIMEMultipart()
    msg['From'] = emailaddr
    msg['To'] = toaddr
    msg['Subject'] = "Hi! " + name + ",here is a response to your query."

    body = u'\n'.join(body).encode('utf-8').strip()

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()   #transport-layer-security
    server.login(emailaddr, "Algoproject")
    text = msg.as_string()
    server.sendmail(emailaddr, toaddr, text)
    server.quit()

