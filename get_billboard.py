import pandas as pd
import requests
from bs4 import BeautifulSoup
def get_billboard():
    resp = requests.get("https://www.billboard.com/charts/hot-100/")
    soup = BeautifulSoup(resp.text, 'html.parser')
    chart = soup.find_all('div', class_='o-chart-results-list-row-container')
    temp=""
    song_df = pd.DataFrame({'SongName':[], 'Artist': []})
    for i in chart:
        songname = i.findChildren()[0].findChildren()[0].find_next_siblings("li")[2].findChildren()[0].findChildren()[0].findChildren()[0]
        artist = songname.find_next_siblings('span')[0]
        song_df=song_df.append({'SongName': songname.text, 'Artist': artist.text}, ignore_index=True)
    song_df = song_df.replace(r'\n',' ', regex=True) 
    song_df = song_df.replace(r'\t',' ', regex=True)
    return song_df
print(get_billboard())