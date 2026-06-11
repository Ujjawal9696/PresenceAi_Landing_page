from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5002,
        use_reloader=True,
        reloader_type='stat'   # watchdog ki jagah stat use karo — fix for infinite reload
    )