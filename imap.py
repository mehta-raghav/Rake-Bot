
import sys
import imaplib
import getpass
import email
import email.header
import datetime
from email.message import Message

EMAIL_ACCOUNT = "subscribe.ai.client@gmail.com"

EMAIL_FOLDER = "Inbox"

def getBody(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()

def mailReader(M):
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

    msg = email.message_from_bytes(data[0][1])
    hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
    #subject = str(hdr)
    rawEmail = data[0][1]
    email_message = email.message_from_bytes(rawEmail)
    mail = getBody(email_message)
    fromAddrTotal = email.utils.parseaddr(email_message['From'])
    fromAddr = fromAddrTotal[1]
    argument = [fromAddr , mail]
    return argument
    
def auth():
    M = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        rv, data = M.login(EMAIL_ACCOUNT, 'Algoproject')
    except imaplib.IMAP4.error:
        print ("LOGIN FAILED!!! ")
        sys.exit(1)

    print(rv, data)

    rv, mailboxes = M.list()

    rv, data = M.select(EMAIL_FOLDER)
    mailstuff=[]
    if rv == 'OK':
        mailStuff=mailReader(M)
        M.close()
    else:
        print("ERROR: Unable to open mailbox ", rv)
    M.logout()
    return mailstuff
auth()
