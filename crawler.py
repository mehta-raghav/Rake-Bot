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

def crawl_facebook(username):
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

    trend = soup.find_all('a', {'id': """video-title"""})

    i = 0
    for p in trend:
        arr.append(p.getText())
        i = i + 1
    return arr



def func_calling(name, list):
    if filter(lambda x: 'trend' in x, list):
        return crawl_trend_youtube()
    elif filter(lambda x: 'facebook' in x, list):
        return crawl_facebook(name[0])
    elif filter(lambda x: 'video' in x, list):
        return crawl_youtube(name[0])
    elif filter(lambda x: 'tweet' in x, list):
        return crawl_twitter(name[0])
    else:
        return "We couldn't fulfill your query at the moment!"
