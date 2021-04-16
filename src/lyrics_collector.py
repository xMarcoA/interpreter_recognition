import pandas as pd 
from bs4 import BeautifulSoup
import time
from requests.exceptions import ConnectionError
import requests
import os

base_url = 'https://www.lyrics.com/artist/'
def song_links(artist):
    ''' get the song links of an artist without: 'https://www.lyrics.com' '''
    artist_link = base_url + artist 
    resp = requests.get(artist_link)
    soup = BeautifulSoup(resp.text)
    with open('../lyrics/' + artist + '.html','w') as file:
        file.write(resp.text)
    links = [link.get('href') for link in soup.find(class_='tdata-ext').find_all('a')]
    clean_links=[]
    for link in links:
        if "/album" not in link:
            clean_links.append(link)
    return clean_links

def lyrics_collector(song_link):
    ''' to get the lyrics of the song links '''
    time.sleep(0.5)
    print(song_link)
    resp = requests.get('https://www.lyrics.com'+ song_link)
    lyric = ""
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text)
        with open('../lyrics/' + song_link[700:] + '.html','w') as file:   
                    file.write(resp.text)
        lyric = soup.find(id='lyric-body-text').text.replace('\n'," ")
    return lyric

def get_artist(artist):
    ''' create a list with x-times the artist in it / x = song lyrics '''
    artist_link =  base_url+artist
    resp = requests.get(artist_link)
    soup = BeautifulSoup(resp.text)
    links = [link.get('href')for link in soup.find(class_='tdata-ext').find_all('a')]
    clean_artists=[]
    for link in links:
        if "/album" not in link:
            clean_artists.append(artist)
    return clean_artists



# input= Interpret, output list with lyrics  

def fill_list_with(interpret):
    ''' fills the list songs and artists up with interpret names and lyrics '''
    interpret_song_links = song_links(interpret)
    for link in interpret_song_links[:600]:           # set here how many lyrics you want from one artist max    
        songs.append(lyrics_collector(link))
        artists.append(interpret)
    return "filled up"


# # Pick some Artists (execute only one time)

songs = []       
artists = []

fill_list_with('Eminem')
fill_list_with('Michael-Jackson')
fill_list_with('Linkin-Park')   
fill_list_with('AC-DC')
fill_list_with('The-Beatles')


data ={'Artist':[], 'Lyric':[]}

for i in range(len(songs)):    
    data['Artist'].append(artists[i])
    data['Lyric'].append(songs[i])
df =pd.DataFrame(data)
df

# saves the the dataframe as a csv file in lyrics

df.to_csv('../lyrics/lyrics.csv', index=False)
