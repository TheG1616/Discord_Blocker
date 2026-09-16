import json
import nextcord


def ret_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


def add_new_event(user, time, event_type, opreation):
    data = ret_json()
    if "operations" not in data:
        data["operations"] = []

    data["operations"].append({"time": time, "event_type": event_type, "operation": opreation, "avatar_url": user.avatar.url, "username": user.name})

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def get_user_history(username):
    data = ret_json()
    if "operations" not in data:
        return []

    user_history = []

    for i in data["operations"]:
        if i["username"] == username:
            user_history.append(i)

    return user_history


def get_history():
    data = ret_json()
    if "operations" not in data:
        return []

    return data["operations"]


def get_count_of_offence(username):
    data = ret_json()
    if "operations" not in data:
        return 0

    user_count = 0

    for i in data["operations"]:
        if i["username"] == username:
            user_count += 1

    return user_count


def default_setting():
    data = ret_json()
    if "settings" not in data:
        data["settings"] = {}
        data["settings"]["timeout_duration"] = 1
        data["settings"]["kick_amount"] = 5
        data["settings"]["ban_amount"] = 10

    return data


def save_timeout_duration(timeout_duration):
    if not timeout_duration:
        return
    timeout_duration = int(timeout_duration)
    data = default_setting()
    data["settings"]["timeout_duration"] = timeout_duration

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def save_kick_amount(kick_amount):
    if not kick_amount:
        return
    kick_amount = int(kick_amount)
    data = default_setting()
    data["settings"]["kick_amount"] = kick_amount

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def save_ban_amount(ban_amount):
    if not ban_amount:
        return
    ban_amount = int(ban_amount)
    data = default_setting()
    data["settings"]["ban_amount"] = ban_amount

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
