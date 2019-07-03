import json 
import requests
import urllib

TOKEN = "<bot_api_token>"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
GROUP_ID = <your_group_id>

def get_url(url):
    try:
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content
    except requests.exceptions.RequestException as err:
        print(err)
        return False


def get_json_from_url(url):
    try:
        content = get_url(url)
        js = json.loads(content)
        return js
    except TypeError:
        return False
        

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    try:
        js = get_json_from_url(url)
        return js
    except TypeError:
        return False

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    print(get_url(url))

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def user_present(userid):
    users = db.get_users()
    if userid in users:
        return True
    else:
        return False

def handle_updates(updates):
    
def main():
    lif __name__ == '__main__':
    main()
