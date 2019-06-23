import json 
import requests
import time
import urllib
from demo_db import DBHelper
import github
import datetime

db = DBHelper()

TOKEN = "877535563:AAE6YASygZ3ua9YYylWVH-1Sx0NGXbFsbHo"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
GROUP_ID=-1001190092036

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

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
    for update in updates["result"]:
        if ((int(datetime.datetime.now().timestamp())-update["message"]["date"]) < 300):
            try:
                chat = update["message"]["chat"]["id"]
                try:
                    if(update["message"]["group_chat_created"]):
                        message = "Hello! World. I'm @git_checker_bot. I will help you keep track of your challenge commits. Everyone is requested to please send me your GitHub usernames as '@git_checker_bot <username>'. Happy coding."
                        send_message(message, chat)
                except KeyError:
                    pass        
                try:
                    if (update["message"]["new_chat_participant"]):
                        name = update["message"]["new_chat_participant"]["first_name"]
                        message = "Welcome " + name + " to the group. Please register your GitHub username by sending '@git_checker_bot <username>'"
                        send_message(message, chat)
                except KeyError:
                    pass
                text = update["message"]["text"]
                if "@git_checker_bot" in text:
                    username =  text.replace('@git_checker_bot ','')
                    username.strip()
                    if(github.check_user_exists(username)):
                        user = str(update["message"]["from"]["id"])
                        name = update["message"]["from"]["first_name"]
                        if (user_present(user)):
                            message = "You are already registered and progress is already being tracked."
                        else:
                            db.add_user(str(user),name,username)
                            message = "You have been added to the list. Your progress will be recorded."
                        send_message(message, chat)
            except KeyError:
                pass
        else:
            pass

def main():
    last_update_id = None
    db.setup()
    check_date=datetime.datetime.strptime('2019-06-23T17:50:10','%Y-%m-%dT%H:%M:%S')
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        if (((datetime.datetime.now().replace(microsecond=0))-check_date).total_seconds() > 0):
            check_date = check_date + datetime.timedelta(days=1)
            usernames = db.get_username()
            for username in usernames:
                result = github.check_commit(username)
                user_fname = str(db.get_fname(username))
                if ( "no-repo" in result):
                    message = user_fname + " you've not yet created the public repository named HDOC. Please create it soon."
                elif ( "committed" in result):
                    message = user_fname + " has committed today."
                elif ( "not-committed" in result):
                    message = user_fname + " has not committed today."
                send_message(message, GROUP_ID)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
