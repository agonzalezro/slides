from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return '<img width="100%" src="{}" />'.format(
        url_for('static', filename='grumpy.gif')
    )

if __name__ == "__main__":
    app.run()
