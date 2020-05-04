import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Iniciando el proceso...')
def get_headlines(url):
    logging.info('Leyendo URL '  +  url)
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import re
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html, "html.parser")
    s=soup.find_all(class_="headline")
    for i in s:
        i=str(i)
        j=i.split(">")
        m=j[2]
        final=m.split("</a")
        text=final[0]
        post='"'+text+'"'+" . "+"El País"
        return post
url="https://elpais.es"
titular=get_headlines(url)
import tweepy
auth = tweepy.OAuthHandler("BtHNJMURBTjLgq5WTBJqKRZ92","MZfyrMJKeriYZu7vufZOZrwklmNYfZ2gaGuqUTGzBR6xcXt7vD")
auth.set_access_token("2766462103-gSIyudYqMhYNIfwFZS82Dm5tXqtCrf2opkj0kmP","UkEr4QKUjVIOTEBmF7iBoNNjFnTk4e3eHR4M6bTruOdVK")
api = tweepy.API(auth)
try:
    result=api.update_status(titular)
except Exception as e:
    logging.error("Titular duplicado, no se pudo publicar", exc_info=False)
logging.info('proceso Finalizado.')

  
