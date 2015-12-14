PyGrunn #5 "slides"
===================

Simple examples to show how to use requests & request-oauth on the PyGrunn
monthly meeting #5.


Usage
-----

    mkvirtualenv slides
    pip install -r requeriments.txt


API
---

The example API is a very simple API that will help us to keep track of the data
and headers that we are posting.

If the API receives the argument `post_to_twitter=True` it will post a message
on the social network. **Be aware, that to perform this action you need to
change the `settings.py` file**.


Examples
--------

- `example1.py`: it shows how to use request to perform a GET that consums
  from the Google Images API.
- `example2.py`: it posts to the API (`examples/api.py`) with different
  headers and data.
- `example3.py`: it shows how to use requests and request-oauth to keep a socket
  to the twitter streaming API open.


Thanks!
-------

- [requests](https://github.com/kennethreitz/requests)
- [requests-oauth](https://github.com/maraujop/requests-oauth)
- [Flask](http://flask.pocoo.org/)
