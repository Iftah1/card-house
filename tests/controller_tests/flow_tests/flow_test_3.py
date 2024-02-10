import json
from requests import post

add_card_json = {
    "content": "hello world",
    "type": "answer",
}

remove_card_json = {

}

get_cards_json = {
    "content": "hello world",
}


first_get_response = post(url="http://127.0.0.1:5000/filter_cards", json=get_cards_json)
cards_first_get_response = json.loads(first_get_response.text)

add_response = post(url="http://127.0.0.1:5000/add_card", json=add_card_json)

second_get_response = post(url="http://127.0.0.1:5000/filter_cards", json=get_cards_json)
cards_second_get_response = json.loads(second_get_response.text)

assert len(cards_second_get_response["cards"]) == len(cards_first_get_response["cards"]) + 1

print("tests has been run successfully")
