import time
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Iniciando el proceso...')
hora=time.strftime("%X")
hour="La Hora en Madrid es: " + hora
import tweepy
auth = tweepy.OAuthHandler("BtHNJMURBTjLgq5WTBJqKRZ92","MZfyrMJKeriYZu7vufZOZrwklmNYfZ2gaGuqUTGzBR6xcXt7vD")
auth.set_access_token("2766462103-gSIyudYqMhYNIfwFZS82Dm5tXqtCrf2opkj0kmP","UkEr4QKUjVIOTEBmF7iBoNNjFnTk4e3eHR4M6bTruOdVK")
api = tweepy.API(auth)
result=api.update_status(hour)
logging.info('proceso finalizado')

