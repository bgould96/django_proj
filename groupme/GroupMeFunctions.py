import requests, json, string

def gm_post(url, json_data):
    resp = requests.post("https://api.groupme.com/v3" + url + "?token=b1580fb0ec9401334a16001f5a739d7d", json=json.dumps(json_data))

def gm_get(url):
    resp = requests.get("https://api.groupme.com/v3" + url + "?token=b1580fb0ec9401334a16001f5a739d7d")

    printable = set(string.printable)

    emoji_clear = filter(lambda x: x in printable, resp.text)

    json_array = json.loads(emoji_clear)

    return json_array["meta"], json_array["response"]

def get_group_members(group_id):
    meta, group = gm_get("/groups/" + group_id)

    return group["members"]

def send_bot_message_to_group(bot_id, message):
    json_data = {'bot_id' : bot_id, 'text' : message}

    requests.post(
        "https://api.groupme.com/v3/bots/post",
        data=json.dumps(json_data)
    )

def send_user_message_to_group(group_id, message):
    json_data = {"source_guid" : "GUID", "text" : message}

    gm_post(
        "/groups/" + group_id + "/messages",
        json_data
    )

    return "/groups/" + group_id + "/messages"