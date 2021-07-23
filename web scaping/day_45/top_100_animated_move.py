from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")

move_site = response.text

soup = BeautifulSoup(move_site, "html.parser")

move_site_list = soup.find_all(name="a", class_="unstyled articleLink")


move_list = []

move_site_list = move_site_list[43:]

for move_tag in move_site_list:
    move_name = move_tag.getText()
    move_list.append(move_name.strip())

move_list.pop()
move_list.pop()

# print(move_list)

move_like_percent_list_tag = soup.find_all(name="span", class_="tMeterScore")

move_like_list = []

for like_tag in move_like_percent_list_tag:
    like_percent = like_tag.getText()
    move_like_list.append(like_percent)

# print(move_list)
# print(move_like_list)
with open('movie_list.txt', 'a+') as file:
    for index in range(len(move_list)):
        file.write(f'{move_list[index]} { move_like_list[index]}\n')