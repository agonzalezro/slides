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
    fon_url = 'http://fon.gs/create.php?url={url}'
    response = requests.get(fon_url.format(url=url))
    return response.content.split('OK: ')[-1]


def _json_encoder(message='Posted and JSON returned!'):
    '''Very simple json encoder to use on the responses.'''
    return json.dumps({'message': message})


@app.route('/image', methods=['POST'])
def image():
    '''If `post_to_twitter` field is sent, the image will be posted on
    twitter using requests-oauth.'''
    message = None

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
        encoder = lambda x='I am sure that this is not a JSON :)': x
    return encoder(*[message] if message else [])

if __name__ == '__main__':
    app.run()
