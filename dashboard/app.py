from flask import Flask, render_template
import json
import os

app = Flask(__name__)

LOG_FILE = "../logs/alerts.log"

def read_logs():
    events = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f.readlines()[-50:]:
                try:
                    events.append(json.loads(line))
                except:
                    pass
    return events[::-1]

@app.route("/")
def index():
    events = read_logs()
    return render_template("index.html", events=events)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
