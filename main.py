from imap import mailer
from smtp import sender
from crawler import *
from rake import rake

def looper():
    fromaddr = mailer()[0]
    query = mailer()[1]
    fromname = mailer()[2]

    list = rake(query)
    body = func_calling(list, query)
    sender(fromaddr, body, fromname)


if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            looper()
    except:
        print 'The server is at rest.'