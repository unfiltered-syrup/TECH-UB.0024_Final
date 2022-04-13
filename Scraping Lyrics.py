
import pandas as pd
vl = pd.read_csv (r"file path for vent library")
from lyricsgenius import Genius
genius = Genius("3sHE7Z5PlLxXnFCzrYkhXWN4Ce69C7_Vxu-lfR7H3ZXIBc_gVUIDdLBOr4EqifT7")

lyrics=[]
def getlyrics(song_name):
    song = genius.search_song(song_name)
    song_lyrics=song.lyrics
    lst=song_lyrics.split(" ")
    for a in lst:
        if "\n" in a:
            a=a.replace("\n", " ")
    song_lyrics=" ".join(lst)
    lyrics.append(song_lyrics)

for i in range(0,len(vl)):
    getlyrics(vl["Track"].iloc[i])

vl["Lyrics"]=lyrics

#saves the csv to your computer 
vl.to_csv(r'specify file path', index = False, header=True)
