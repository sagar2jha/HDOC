import json 
import requests
import time
import urllib
from demo_db import DBHelper
import github
import datetime

db = DBHelper()

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
    for update in updates["result"]:
        if ((int(datetime.datetime.now().timestamp())-update["message"]["date"]) < 300):
            try:
                chat = update["message"]["chat"]["id"]
                try:
                    if(update["message"]["group_chat_created"]):
                        message = "Hello! World. I'm @git_checker_bot. I will help you keep track of your challenge commits. Everyone is requested to please send me your GitHub usernames as '@git_checker_bot <username>'. Happy coding."
                        global GROUP_ID 
                        GROUP_ID = update["message"]["chat"]["id"]
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
                #Bot Commands to be handled here.
                try:
                    if( update["message"]["entities"] ):
                        if ("bot_command" in (update["message"]["entities"][0]["type"])):
                            command = update["message"]["text"]
                            chat = update["message"]["chat"]["id"]
                            if ("/status" in command):
                                user = str(update["message"]["from"]["id"])
                                username = db.get_username(user)
                                result = github.check_commit(username)
                                try:
                                    if ( "no-repo" in result):
                                        message = update["message"]["from"]["first_name"] + ", you've not yet created the repo."
                                    elif ( "not-committed" in result):
                                        message = update["message"]["from"]["first_name"] + ", you've not yet committed today. You still have time, make use of it."
                                    elif ( "committed" in result):
                                        message = update["message"]["from"]["first_name"] + ", you've committed today."
                                    send_message(message, chat)
                                except TypeError:
                                    pass
                                return True
                except KeyError:
                    pass
                #Code for adding username goes here.
                text = update["message"]["text"]
                if "@git_checker_bot" in text:
                    username =  text.replace('@git_checker_bot ','')
                    username.strip()
                    print(GROUP_ID)
                    if(github.check_user_exists(username)):
                        user = str(update["message"]["from"]["id"])
                        name = update["message"]["from"]["first_name"]
                        if (user_present(user)):
                            message = name + ", you are already registered and progress is being tracked."
                        else:
                            db.add_user(str(user),name,username)
                            message = name + " has been added to the list. Your progress will be recorded."
                        send_message(message, chat)
                    else:
                        message = username + " does not exist on GitHub."
                        send_message(message, chat)
            except KeyError:
                pass
        else:
            pass

def main():
    last_update_id = None
    db.setup()
    check_date=datetime.datetime.strptime('2019-06-25T23:50:10','%Y-%m-%dT%H:%M:%S')
    while True:
        updates = get_updates(last_update_id)
        try:
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                handle_updates(updates)
        except TypeError:
            pass
        except:
            pass
        if (((datetime.datetime.now().replace(microsecond=0))-check_date).total_seconds() > 0):
            check_date = check_date + datetime.timedelta(hours=12)
            no_repo_fname = ""
            commit_fname = ""
            no_commit_fname = ""
            usernames = db.get_usernames()
            for username in usernames:
                result = github.check_commit(username)
                user_fname = str(db.get_fname(username))
                try:
                    if ( "no-repo" in result):
                        no_repo_fname = no_repo_fname + user_fname + ", "
                    elif ( "not-committed" in result):
                        no_commit_fname = no_commit_fname + user_fname + ", "
                    elif ( "committed" in result):
                        commit_fname = commit_fname + user_fname + ", "
                except TypeError:
                    pass
            if(len(no_repo_fname) > 0):
                no_repo_message = no_repo_fname + "have not yet added the public HDOC repo. Please do it soon."    
                send_message(no_repo_message, GROUP_ID)
            if(len(no_commit_fname) > 0):
                no_commit_message = no_commit_fname + "have not committed on " + datetime.datetime.today().date().isoformat()
                send_message(no_commit_message, GROUP_ID)
            if(len(commit_fname) > 0):
                commit_message = commit_fname + "have committed on " + datetime.datetime.today().date().isoformat()
                send_message(commit_message, GROUP_ID)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
