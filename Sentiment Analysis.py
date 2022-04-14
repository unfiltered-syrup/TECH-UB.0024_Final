from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

import nltk
import pandas as pd
#  link to emotions_short.csv: https://drive.google.com/file/d/1Is6VaVft6BuL438byJQbePDA_Ys19v5W/view?usp=sharing
#emotion_train = pd.read_csv('emotions_short.csv')


from textblob.classifiers import NaiveBayesClassifier

with open('emotion_short.csv',) as fp:
    cl = NaiveBayesClassifier(fp, format="csv")

blob = TextBlob("I'm waiting for my friend", classifier=cl)
for s in blob.sentences:
     print(s)
     print(s.classify())


#Emotions- Song Mood Map:
emotion_lst= [ "happiness",
              "anger",
              "sadness",
              "Heartbroken",
              "Working",
              "worry",
              "boredom",
              "fun",
              "love"

]

song_mood_lst=[ "Happy",
              "Angry",
              "Sad",
              "Heartbreak",
              "Focus",
              "Self-Love",
              "Inspiration",
              "Party",
              "Love"

]

Emotion_Song_Map=pd.DataFrame({"User Emotion":emotion_lst, "Song Mood":song_mood_lst})
print(Emotion_Song_Map)