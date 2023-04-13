from bs4 import BeautifulSoup
import requests

responce = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = responce.text
soup = BeautifulSoup(web_page, "html.parser")

all_title = [title.getText() for title in soup.find_all(name='h3', class_='title')]
all_title = all_title[::-1]
all_title = '\n'.join(all_title)
with open("movies.txt", "w", encoding='utf-8') as f:
    f.write(all_title)