import requests
import json
import datetime

URL="https://api.github.com/"
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def check_user_exists(username):
    url = URL + "users/" + username
    js = get_json_from_url(url)
    try:
        if ("Not Found" in js["message"]):
            return False
    except KeyError:
        return True

def check_commit(username):
    time = (datetime.datetime.today()-datetime.timedelta(days=1)).replace(microsecond=0).isoformat()
    url = URL + "repos/" + username + '/HDOC/commits?since="' +  time + '"'
    js = get_json_from_url(url)
    try:
        if ("Not Found" in js["message"]):
            return "no-repo"
    except TypeError:
        pass
    if (len(js) > 0):
        return "committed"
    else:
        return "not-committed"
