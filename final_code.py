import re
import string
import spotipy as sp
import pandas as pd
import requests
import json

#Replaces split sentences
def split(vent):
    return(re.split('[?.!]', vent))

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

import nltk
import pandas as pd
#  link to emotions_short.csv: https://drive.google.com/file/d/1Is6VaVft6BuL438byJQbePDA_Ys19v5W/view?usp=sharing

#Makes the classifier
from textblob.classifiers import NaiveBayesClassifier
with open('emotion_complete.csv',) as fp:
  cl = NaiveBayesClassifier(fp, format="csv")

#Gets the user string and outputs a list of their emotions
def get_string():
  string=input("How are you feeling?")
  emotion_list=[]
  sents=split(string)
  for sent in sents:
    if len(sent)!=0:
        blob=TextBlob(sent,classifier=cl)
        emotion_list.append(blob.classify())
  return emotion_list

#Splits songs up by mood
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

#Code gets track
def create_playlist():
    tracks = []
    string=get_string()
    for x in string:
        if x == 'happiness':
            tracks+=happy_songs.sample(30//len(string))['Track'].to_list()
        if x == 'anger':
            tracks+=angry_songs.sample(30//len(string))['Track'].to_list()
        if x == 'sadness':
            tracks+=sad_songs.sample(30//len(string))['Track'].to_list()
        if x == 'heartbroken':
            tracks+=heartbreak_songs.sample(30//len(string))['Track'].to_list()
        if x == 'working':
            tracks+=focus_songs.sample(30//len(string))['Track'].to_list()
        if x == 'worry':
            tracks+=selflove_songs.sample(30//len(string))['Track'].to_list()
        if x == 'boredom':
            tracks+=inspiration_songs.sample(30//len(string))['Track'].to_list()
        if x == 'fun':
            tracks+=party_songs.sample(30//len(string))['Track'].to_list()
        if x == 'love':
            tracks+=love_songs.sample(30//len(string))['Track'].to_list()
        if x == 'lonely':
            tracks+=friendship_songs.sample(30//len(string))['Track'].to_list()
    #Gets access code to grant access to the api
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': "213bd88d2dc74e808f362031c8ecb51d",
        'client_secret': "b09c834ecb4b47638048cbbc08ed4f8d",
    })

    auth_response_data = auth_response.json()
    # GIVES ME MY ACCESS TOKEN
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    id_list=[]
    for song in tracks:
        r = requests.get(BASE_URL + 'search?' + "q=" + song, "type=track", headers=headers)
        r = r.json()
        if len(r["tracks"]["items"]) == 0:
            pass
        else:
            id_list.append(r["tracks"]["items"][0]["id"])
    # user info
    client_ID = 'd39c2f2f44284bda99c32b8c897f5f04'
    client_SECRET = 'f332a98be03143cdad37f764d90fddf0'
    redirect_url = "http://localhost:8888/callback/"
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    scope = "playlist-modify-public"
    spot = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret=client_SECRET,
                                                     redirect_uri=redirect_url, scope=scope))
    results = spot.user_playlist_create(user="sakhikamal", name="New Vent", public=True, collaborative=False)
    spot.playlist_add_items(results["id"], id_list, position=None)
    return ("Check your Spotify Account...")

#To test
#print(create_playlist())





