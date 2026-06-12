import os
from flask import Flask, render_template

app = Flask(__name__)

APP_URL = os.environ.get("APP_URL", "https://presenceaiproject-ckz6jmjs33upmemmqwmbyq.streamlit.app/")

@app.route('/')
def index():
    return render_template('index.html', app_url=APP_URL)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5002,
        use_reloader=True,
        reloader_type='stat'
    )