import json

import requests
from flask import Flask, request
from oauth_hook import OAuthHook


app = Flask(__name__)
consumer_key = None
consumer_secret = None
access_token = None
access_token_secret = None


def get_fon_url(url):
    '''Generate a small URL with the fon.gs service.'''
    response = requests.get('http://fon.gs/create.php?url={url}'.format(url=url))
    return response.content.split('OK: ')[-1]


@app.route('/image', methods=['POST'])
def image():
    '''If `post_to_twitter` field is sent, the image will be posted on
    twitter using requests-oauth.'''
    message = None

    def _json_encoder(message='Posted and JSON returned!'):
        return json.dumps({'message': message})

    def _raw_encoder(message='I\'m sure that this is not JSON :)'):
        return message

    if request.form.get('post_to_twitter'):
        hook = OAuthHook(access_token, access_token_secret,
                         consumer_key, consumer_secret)
        client = requests.session(hooks={'pre_request': hook})
        status = 'Pygrunn #5 example: {url}'.format(
                     url=get_fon_url(request.form.get('url'))
                 )
        response = client.post('http://api.twitter.com/1/statuses/update.json',
                               {'status': status})
        message = response.content

    if request.headers.get('Accept') == 'application/json':
        encoder = _json_encoder
    else:
        encoder = _raw_encoder
    return encoder(*[message] if message else [])

if __name__ == '__main__':
    app.run()
