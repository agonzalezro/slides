import json

import requests
from flask import Flask, request
from oauth_hook import OAuthHook


app = Flask(__name__)
consumer_key = 'NXHvC4EaYKpDLpHHPy4G9Q'
consumer_secret = 'aJ4YaGHB46dtZfyYynPadoaKXUth5DdzA1ZrUCXPEqI'
access_token = '14273689-eCkfaZiij2RK9ctBlJGGr3CPNEOULSesBCdHA032w'
access_token_secret = 'ZfYvOBrzjA6e22V17Qdoxc9If3kjbZSkOJngvaXbNnQ'


def get_fon_url(url):
    response = requests.get('http://fon.gs/create.php?url={url}'.format(url=url))
    return response.content.split('OK: ')[-1]


@app.route('/image', methods=['POST'])
def image():
    if request.form.get('post_to_twitter'):
        hook = OAuthHook(access_token, access_token_secret, consumer_key, consumer_secret)
        client = requests.session(hooks={'pre_request': hook})
        status = 'Pygrunn #5 example: {url}'.format(
                     url=get_fon_url(request.form.get('url'))
                 )
        response = client.post('http://api.twitter.com/1/statuses/update.json',
                               {'status': status})
        import pdb;pdb.set_trace()

    if request.headers.get('Accept') == 'application/json':
        return json.dumps({'message': 'Posted and JSON returned!'})
    return 'I\'m sure that this is not JSON :)'

if __name__ == '__main__':
    app.run()
