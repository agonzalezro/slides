import requests
import settings

from flask import Flask, request, jsonify
from oauth_hook import OAuthHook


app = Flask(__name__)


def get_fon_url(url):
    '''Generate a small URL with the fon.gs service.'''
    fon_url = 'http://fon.gs/create.php?url={url}'
    response = requests.get(fon_url.format(url=url))
    return response.content.split('OK: ')[-1]


def post_to_twitter(url):
    hook = OAuthHook(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET,
                     settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    client = requests.session(hooks={'pre_request': hook})
    status = 'Pygrunn #5 example: {url}'.format(url=url)
    response = client.post('http://api.twitter.com/1/statuses/update.json',
                           {'status': status})
    return response.content


@app.route('/image', methods=['POST', 'GET'])
def image():
    '''If `post_to_twitter` field is sent, the image will be posted on
    twitter using requests-oauth.'''
    message = None

    if request.form.get('post_to_twitter'):
        url = get_fon_url(request.form.get('url'))
        message = post_to_twitter(url)

    if request.headers.get('Accept') == 'application/json':
        return jsonify(message=message or 'This is JSON')
    return message or 'I am sure that this is not a JSON'


if __name__ == '__main__':
    app.run()
