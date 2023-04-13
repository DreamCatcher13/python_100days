from bs4 import BeautifulSoup
import requests

responce = requests.get(url="https://news.ycombinator.com/")
web_page = responce.text
soup = BeautifulSoup(web_page, 'html.parser')
all_span = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for span in all_span:
    a = span.find("a")
    article_texts.append(a.getText())
    article_links.append(a.get("href"))

for i in range(len(article_links)):
    print(f"{article_texts[i]}\nLink: {article_links[i]}")




