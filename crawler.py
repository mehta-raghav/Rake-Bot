# -*- coding: utf-8 -*-
def crawl_twitter(username):
    arr = []
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
    arr = []
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
    arr = []
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

def crawl_youtube_search(query):
    arr = []
    import requests
    from bs4 import BeautifulSoup

    r = requests.get('https://www.youtube.com/results?search_query=' + query)

    soup = BeautifulSoup(r.content, "html.parser")

    trend = soup.find_all('a', {'class': "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})

    i = 0
    for p in trend:
        arr.append(p.getText())
        i = i + 1
    return arr



list_trending = ['trend','trending','popular','famous','top']
list_fb = ['facebook','fb','timeline','post']
list_twit = ['twitter','tweet']
list_you = ['youtube','video']
def func_calling(name, list):
    for x in list.split():
        if x in list_trending:
            return crawl_youtube_search(name[0])

        elif x in list_fb:
            return crawl_facebook(name[0])

        elif x in list_you:
            return crawl_youtube(name[0])

        elif x in list_twit:
            return crawl_twitter(name[0])

        else:
            return crawl_youtube_search(list)
