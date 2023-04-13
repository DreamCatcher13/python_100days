from bs4 import BeautifulSoup
import requests

date = input("Please, enter the date in the format YYYY-MM-DD: ")

responce = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
web_page = responce.text
soup = BeautifulSoup(web_page, "html.parser")
all_div = soup.select(".o-chart-results-list-row-container")
all_names = [div.find(name="h3", id="title-of-a-story").getText().strip() for div in all_div]
#all_artist = [div.select_one('li span')  for div in all_div]
print('\n'.join(all_names))