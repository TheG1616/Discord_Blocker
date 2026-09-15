from sightengine.client import *
import requests

client = SightengineClient('1393980510', 'AP3cfd36TcKGPdnSYhVgqLaZBmtTdEvC')

image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyXFMQzRyE2LqDn0oExz_UBWlhUXOQphdRsbRb9J-7rQ&s=10'

categories = ["nudity", "violence", "weapon", "offensive", "gore", "self-harm"]
prob_lst = ["violence", "offensive", "self-harm", "gore"]


def get_keys(d, threshold=0.3):
    keys = []

    for k, v in d.items():
        if isinstance(v, dict):
            keys.extend(get_keys(v, threshold))
        elif v > threshold:
            keys.append(k)
    return keys


def check_image(image):
    output_lst = []

    for category_name in categories:
        output = client.check(category_name).set_url(image)

        if category_name == "nudity":
            for key, value in output[category_name].items():
                if type(value) == float and value > 0.3 and key == "raw":
                    output_lst.append("nudity")
        elif category_name in prob_lst:
            label = output[category_name]["prob"]
            if label > 0.3:
                output_lst.append(category_name)
        elif category_name == "weapon":
            result = get_keys(output[category_name])
            if len(result) > 0 and "firearm_toy" not in result:
                output_lst.append("weapon")

    if len(output_lst) > 0:
        return True, ", ".join(output_lst)
    return False


print(check_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5GSeVcWT0zo0hbcrcDf8WQINo5Gj7tJ-WrMfGzvo-mQ&s"))

