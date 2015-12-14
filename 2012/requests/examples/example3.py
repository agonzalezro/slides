# -*- coding: utf-8 -*-

import json
import requests
import settings

from oauth_hook import OAuthHook


hook = OAuthHook(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET,
                 settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
client = requests.session(hooks={'pre_request': hook})
response = client.post('https://stream.twitter.com/1/statuses/filter.json',
                       data={'track': 'euro2012'})

for line in response.iter_lines():
    data = json.loads(line)
    user = data['user']['screen_name']
    text = data['text']
    print u'@{user}: {text}'.format(user=user, text=text)
