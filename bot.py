import twitter
import random
api = twitter.Api(
    consumer_key='Zefk6DzixmX6NPv7MDIU0cpDK',
    consumer_secret='1SsyR1T3yRwh25hVgYWjGKQb7bLvEUWS9n5RIOGCG7uZG5Gwzo',
    access_token_key='1584892427801747456-43M5XUCqa62Fm1JhWOJ3dRhADXAHvQ',
    access_token_secret='a8tVY7gigSmowiPaTNT0OjDu7aRhoCFWEht1FqG5hShdC'          
)
tweets = [
    "SIUUUUUU!"
    "Quizás me odian porque soy muy bueno.",
    # "La experiencia te hace entender que jugando en equipo y siendo solidario se alcanzan mayores objetivos.",
    "Tu amor me hace fuerte, tu odio me hace imparable.",
    "Quizás me odian porque soy muy bueno.",
    # "No soy un perfeccionista, pero me gusta sentir que las cosas se hacen bien. Más que eso, siento una necesidad interminable de aprender, de mejorar, de involucrarme, no solo para agradar al entrenador y a los aficionados, sino para sentirme satisfecho conmigo mismo.",
    "Yo sé que al que le gusta el fútbol, le gusto yo.",
    # "El talento no lo es todo. Lo puedes tener desde la cuna, pero es necesario aprender el oficio para ser el mejor.",
    # "Prácticamente no tengo vida privada. Ya estoy acostumbrado a ello. Si, a veces es duro, pero es la elección que tomé.",
    "¿Por qué mentir? No voy a ser un hipócrita y decir lo opuesto a lo que pienso, como hacen otros.",
    # "Soy consciente de que sean cuales sean las circunstancias, siempre habrá especulaciones sobre mi.",
    "Demasiada humildad es un defecto.",
    # "Se que soy un buen profesional, se que nadie es tan duro conmigo como yo mismo y eso nunca va a cambiar.",
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
# Choose a random tweet
tweet = random.choice(tweets)
# Post the tweet
api.PostUpdate(tweet)
