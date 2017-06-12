# -*- coding: utf-8 -*-
arr=[]
def crawl_twitter(username):
    import requests
    from bs4 import BeautifulSoup

    r = requests.get('https://twitter.com/' + username)

    soup = BeautifulSoup(r.content, "html.parser")

    tweet = soup.find_all('p', {'class': """TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"""})

    i = 0
    for p in tweet:
        arr.append(p.getText())
        i = i + 1
    return arr

def crawl_facebook():
    import requests
    from bs4 import BeautifulSoup

    r = requests.get('https://facebook.com/pg/'+username+'/posts/?ref=page_internal&mt_nav=1')

    soup = BeautifulSoup(r.content, "html.parser")

    fb = soup.find_all('div', {'class': """_5pbx userContent"""})

    i = 1
    for p in fb:
        arr.append(p.getText())
        i = i + 1
    return arr

def crawl_youtube(username):
    # type: (object) -> object
    import requests
    from bs4 import BeautifulSoup

    r = requests.get('https://www.youtube.com/user/' + username + '/videos')

    soup = BeautifulSoup(r.content, "html.parser")

    video = soup.find_all('h3', {'class': """yt-lockup-title"""})

    i = 0
    for p in video:
        arr.append(p.getText())
        i = i + 1
    return arr


def crawl_trend_youtube():

    import requests
    from bs4 import BeautifulSoup

    r = requests.get('https://www.youtube.com/feed/trending')

    soup = BeautifulSoup(r.content, "html.parser")

    trend = soup.find_all('h3', {'class': """yt-lockup-title"""})

    i = 0
    for p in trend:
        arr.append(p.getText())
        i = i + 1
    return arr