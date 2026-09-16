import json
import nextcord


def ret_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


def add_new_event(user, time, event_type, opreation):
    data = ret_json()
    user_id = user.id
    if str(user_id) not in data:
        data[str(user_id)] = []
    data[str(user_id)].append({"time": time, "event_type": event_type, "opreation": opreation, "avatar_url": user.avatar.url, "username": user.name})
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def get_list_of_event(user_id):
    data = ret_json()
    if not str(user_id) in data:
        return []
    else:
        return data[str(user_id)]


def get_count_of_offence(user_id):
    data = ret_json()
    if not str(user_id) in data:
        return 0
    return len(data[str(user_id)])

