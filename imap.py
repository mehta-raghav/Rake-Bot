import imaplib
import email
import email.header

EMAIL_ACCOUNT = "subscribe.ai.client@gmail.com"
EMAIL_FOLDER = "Inbox"

def mailer():
    M = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        M.login(EMAIL_ACCOUNT, 'Algoproject')
    except:
        print ("LOGIN FAILED!!! ")
    #print(rv, data)
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        mailstuff = mailReader(M)
        M.close()
    else:
        print("ERROR: Unable to open mailbox ", rv)
    M.logout()
    return mailstuff


def mailReader(M):
    rv, data = M.search(None, '(UNSEEN)')
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return
        rawEmail = data[0][1]
        email_message = email.message_from_string(rawEmail)
        mail = getBody(email_message)
        fromAddrTotal = email.utils.parseaddr(email_message['From'])
        fromname = fromAddrTotal[0]
        fromAddr = fromAddrTotal[1]
        argument = [fromAddr, mail]
        return argument, fromname

def getBody(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()


mailer()