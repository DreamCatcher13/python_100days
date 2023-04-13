from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
all_anchor_tags = soup.find_all(name="a")  #all elements
h1 = soup.find(name="h1", id="name") #looking for one element
section_heading = soup.find(name="h3", class_="heading")  #because 'class' is reserved !
company_url = soup.select_one(selector="p a")  #first match by CSS selector
items = soup.select(selector=".heading")  #by CSS class;  "#id" -- by id
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href")) #get value of attribute
    print(h1.getText())
    print(company_url)

