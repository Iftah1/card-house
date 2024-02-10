import json
from requests import post, delete


add_card_json = {
    "content": "hello world",
    "type": "answer",
}

remove_card_json = {

}

get_cards_json = {
    "type": "answer",
}


add_response = post(url="http://127.0.0.1:5000/add_card", json=add_card_json)
card_id = add_response.text

remove_card_json["card_id"] = card_id

first_get_response = post(url="http://127.0.0.1:5000/filter_cards", json=get_cards_json)
cards_first_get_response = json.loads(first_get_response.text)

remove_response = delete(url="http://127.0.0.1:5000/remove_card", json=remove_card_json)

second_get_response = post(url="http://127.0.0.1:5000/filter_cards", json=get_cards_json)
cards_second_get_response = json.loads(second_get_response.text)

assert len(cards_second_get_response["cards"]) == len(cards_first_get_response["cards"]) - 1

print("tests has been run successfully")
