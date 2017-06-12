import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from imap import auth
from rake import func_calling
from rake import rake

name = rake()[1]
final = func_calling(name)
toID = auth()[0]
fromaddr = "subscribe.ai.client@gmail.com"
toaddr = toID
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Response to your query"


body = u'\n'.join(final).encode('utf-8').strip()


msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "Algoproject")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()