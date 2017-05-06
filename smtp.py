import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "subscribe.ai.client@gmail.com"
toaddr = "prakhar.d9@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "PLEASE REPLY"

body = "This is a smtp server generated mail. Please reply to confirm it has been received"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "Algoproject")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
