# import twitter
import tweepy
from google_images_search import GoogleImagesSearch
import requests
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')
GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')
GOOGLE_API_CX= os.getenv('GOOGLE_API_CX')

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
gis = GoogleImagesSearch(GOOGLE_API_KEY, GOOGLE_API_CX)

search_terms = ["el bicho gritando siuuu","cr7 tomando jugo", "El bicho memes 2023"]
search_term = random.choice(search_terms)

gis.search(search_params={'q': search_term, 'num': 10})
img_url = gis.results()[random.randint(0, 9)].url

text_tweets = [
    # "La experiencia te hace entender que jugando en equipo y siendo solidario se alcanzan mayores objetivos.",
    # "No soy un perfeccionista, pero me gusta sentir que las cosas se hacen bien. Más que eso, siento una necesidad interminable de aprender, de mejorar, de involucrarme, no solo para agradar al entrenador y a los aficionados, sino para sentirme satisfecho conmigo mismo.",
    # "El talento no lo es todo. Lo puedes tener desde la cuna, pero es necesario aprender el oficio para ser el mejor.",
    # "Prácticamente no tengo vida privada. Ya estoy acostumbrado a ello. Si, a veces es duro, pero es la elección que tomé.",
    # "Soy consciente de que sean cuales sean las circunstancias, siempre habrá especulaciones sobre mi.",
    # "Se que soy un buen profesional, se que nadie es tan duro conmigo como yo mismo y eso nunca va a cambiar.",
    "SIUUUUUU!"
    "Quizás me odian porque soy muy bueno.",
    "Tu amor me hace fuerte, tu odio me hace imparable.",
    "Quizás me odian porque soy muy bueno.",
    "Yo sé que al que le gusta el fútbol, le gusto yo.",
    "¿Por qué mentir? No voy a ser un hipócrita y decir lo opuesto a lo que pienso, como hacen otros.",
    "Demasiada humildad es un defecto.",
    "Nunca he escondido el hecho de que es mi intención ser el mejor.",
    "Què hace una belleza como tú en un lugar tan sucio como mi mente?",
    "No soy Cristobal Colón, pero sí hay 1492 razones para quererte.",
    "Un iPhone to te puede quitar lo barrio, pero un barrio sí te puede quitar el iPhone.",
    "De día me gustaria jugar con Messi... Y de noche con el bicho. -Kylian Mbappe",
    "Muchas gracias afición esto es para vosotros, SIIIIUUUUUUUU!",
    "Si no sueltas tu pasado, con qué mano vas a agarrarme esta?",
    "Quieres ser el siii de mi uuuuu?",
    "Si Dios no exiscte por qué el bicho se llama Cristiano Ronaldo y no Ateo Ronaldo?",
]

if (search_term == 'cr7 tomando jugo'):
    tweet = [random.choice(text_tweets), img_url]
else:
    tweet = ["",img_url]

print(tweet[0])
print(tweet[1])

# download image
filename = 'temp.jpg'
request = requests.get(tweet[1], stream=True)
if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)

    media = api.media_upload(filename)
    api.update_status(status=tweet[0], media_ids=[media.media_id])
    os.remove(filename)
else:
    print("Unable to download image")
