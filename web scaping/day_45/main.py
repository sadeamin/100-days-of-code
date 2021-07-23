from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

scores = soup.find_all(name="span", class_="score")
article_upvotes = [int(score.getText().split()[0]) for score in scores]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])













# import lxml
#
# with open("website.html" , encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)

# all_anchor_tag = soup.find_all(name="a")

# for tag in all_anchor_tag:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_ulr = soup.select_one(selector="#name")
# print(company_ulr)

# headings = soup.select(".heading")
# print(headings)