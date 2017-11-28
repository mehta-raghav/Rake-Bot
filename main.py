from imap import mailer
from smtp import sender
from crawler import
from rake  import rake



"""mailer[0]=MailID  ,,, mailer[1]= BODY ,,, mailer[2]= NAME"""
""""""

def looper():
    fromaddr = mailer()[0]
    body = mailer()[1]
    fromname = mailer()[2]


    sender(fromaddr, """get body from rake""", fromname)






if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            looper()
    except:
