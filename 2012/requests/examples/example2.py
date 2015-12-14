'''
Post to our demo API method
'''
import json
import requests

from example1 import get_random_image


url = 'http://127.0.0.1:5000/image'


def post_image(headers=None, post_to_twitter=False):
    data = {'url': get_random_image()}
    if post_to_twitter:
        data.update({'post_to_twitter': True})
    response = requests.post(url, data=data, headers=headers)
    if headers and headers.get('Accept') == 'application/json':
        return json.loads(response.content)['message']
    return response.content

if __name__ == '__main__':
    print post_image()
    print post_image(headers={'Accept': 'application/json'})
    print post_image(post_to_twitter=True)
