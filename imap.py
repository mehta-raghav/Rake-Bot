import sys
import imaplib
import email
import email.header

EMAIL_ACCOUNT = "subscribe.ai.client@gmail.com"

EMAIL_FOLDER = "Inbox"


def process_mailbox(M):
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
    subject = str(hdr)
    return (subject)


M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    rv, data = M.login(EMAIL_ACCOUNT, 'Algoproject')
except imaplib.IMAP4.error:
    print ("LOGIN FAILED!!! ")
    sys.exit(1)

# print(rv, data)

rv, mailboxes = M.list()

rv, data = M.select(EMAIL_FOLDER)
if rv == 'OK':
    # print("Processing mailbox...\n")
    process_mailbox(M)
    M.close()
else:
    print("ERROR: Unable to open mailbox ", rv)

M.logout()