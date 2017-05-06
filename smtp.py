import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from imap import auth
from rake import rake
from crawler import calling
name = rake()
msg = func_calling(name)
toID = auth()[0]
fromaddr = "subscribe.ai.client@gmail.com"
toaddr = toID
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Response to your query"

body = name
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "Algoproject")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
