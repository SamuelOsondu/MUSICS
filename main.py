from bs4 import BeautifulSoup

import requests

date = input ("which date would you like to travel to? type the date in this format (YYYY-MM-DD): ")
print (date)
response = requests.get("https://www.billboard.com/charts/hot-100/"+date)
musics = response.text
soup = BeautifulSoup(musics, "html.parser")
texts = soup.find_all( name ="span", class_="chart-element__information__song text--truncate color--primary")
music_names = [music.getText() for music in texts]
a = "\n".join(music_names [0:])
print  (a)
