from bs4 import BeautifulSoup
import requests
import re

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all('span',class_='secondaryInfo')
year_sum = 0
for movie in movies:
    year_txt = movie.text
    year = ''
    for i in range(1,len(year_txt)-1):
        year += year_txt[i]
    year_sum += int(year)
    # index = movies.index(movie)
    # item = str(movie.a.text)+str(movie.span.text)+ " Rating : " +str(ratings[index].strong.text) + ", Actors: " + str(movie.a.attrs.get('title')) 
    # movie_name.append(item)
print(year_sum//250)

# for index in range(50):
#     print(f"{index+1}. {movie_name[index]}")