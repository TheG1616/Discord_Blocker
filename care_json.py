import json



def ret_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def add_new_event(user_id, time, event_type):
    data = ret_json()
    if str(user_id) not in data:
        data[user_id] = []
    data[str(user_id)].append({"time": time, "event_type": event_type})
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


