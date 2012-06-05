'''
Get a random image from the Google Images API
'''
import json
import requests
import random
import webbrowser

url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=pygrunn'

def get_random_image():
    response = requests.get(url)
    images = json.loads(response.content)['responseData']['results']
    image = images[random.randint(0, len(images) - 1)]
    return image['url']


if __name__ == '__main__':
    webbrowser.open(get_random_image())
