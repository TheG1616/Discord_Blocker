import requests

def is_safe_picture(url):
    picture = requests.get(url).content
    classification = model_classification(picture)
    return classification == "offensive"