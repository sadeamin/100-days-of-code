import requests
from requests.api import delete, put
from requests.models import Response
from datetime import datetime
USERNAME = "sadeamin"
TOKEN = "782489eamiN"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
	"token":TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes", 
	"notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
	"id": GRAPH_ID,
	"name": "Codeing Graph",
	"unit": "H",
	"type": "int",
	"color": "sora"
}

headers = {
	"X-USER-TOKEN": TOKEN
}



# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=7, day=11)
print(today.strftime("%Y%m%d"))


pixel_post_body = {
	"date": today.strftime("%Y%m%d"),
	"quantity": input("How many hour do you read today ? ")
}



response = requests.post(url=pixel_creation_endpoint, json=pixel_post_body, headers=headers)
print(response.text)

put_day = datetime(year=2021, month=7, day=23)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{put_day.strftime('%Y%m%d')}"

new_pixel_data = {
	"quantity": "12"
}

# response = requests.put(url=update_endpoint, headers=headers, json=new_pixel_data)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{put_day.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)