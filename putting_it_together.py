import re
import string
import spotipy as sp
import pandas as pd
import xlrd
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
def check_punctuation(text):
  if text[len(text)-1] in string.punctuation:
    print('yes')
    return text
  else:
    return text+'.'

def split_into_sentences(text):
    text = check_punctuation(text)
    print(text)
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

import nltk
import pandas as pd
#  link to emotions_short.csv: https://drive.google.com/file/d/1Is6VaVft6BuL438byJQbePDA_Ys19v5W/view?usp=sharing


from textblob.classifiers import NaiveBayesClassifier
with open('emotion_complete.csv',) as fp:
  cl = NaiveBayesClassifier(fp, format="csv")

def get_string(string):
  emotion_list=[]
  sents=split_into_sentences(string)
  for sent in sents:
    blob=TextBlob(sent,classifier=cl)
    emotion_list.append(blob.classify())
  return emotion_list

v2=pd.read_csv("vent_library_utf8.csv")
happy_df = v2[v2['Mood'] == 'Happy']
angry_df = v2[v2['Mood'] == 'Angry']
sad_df = v2[v2['Mood'] == 'Sad']
heartbreak_df = v2[v2['Mood'] == 'Heartbreak']
focus_df = v2[v2['Mood'] == 'Focus']
selflove_df = v2[v2['Mood'] == 'Self Love']
inspiration_df = v2[v2['Mood'] == 'Inspiration']
party_df = v2[v2['Mood'] == 'Party']
love_df = v2[v2['Mood'] == 'Love']
friendship_df = v2[v2['Mood'] == 'Friendship']

happy_songs = happy_df[['Track']]
angry_songs = angry_df[['Track']]
sad_songs = sad_df[['Track']]
heartbreak_songs = heartbreak_df[['Track']]
focus_songs = focus_df[['Track']]
selflove_songs = selflove_df[['Track']]
inspiration_songs = inspiration_df[['Track']]
party_songs = party_df[['Track']]
love_songs = love_df[['Track']]
friendship_songs = friendship_df[['Track']]

def create_playlist(user_string):
    tracks = []
    for x in get_string(user_string):
        if x == 'happiness':
            tracks+=happy_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'anger':
            tracks+=angry_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'sadness':
            tracks+=sad_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'heartbroken':
            tracks+=heartbreak_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'working':
            tracks+=focus_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'worry':
            tracks+=selflove_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'boredom':
            tracks+=inspiration_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'fun':
            tracks+=party_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'love':
            tracks+=love_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
        if x == 'lonely':
            tracks+=friendship_songs.sample(30//len(get_string(user_string)))['Track'].to_list()
    track_ids=[]
    for track in tracks:
        track_ids.append(sp)
    return track_ids

us_string=input("How do you feel?")
print(create_playlist(us_string))



