from flask import Flask, jsonify, request
import datetime, json

date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
day = datetime.datetime.now().strftime("%A")
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/api/")
def getUser():
    userData = {
        "slack_name": "",
        "current_day": day,
        "utc_time": date,
        "track": "",
        "github_file_url": "https://github.com/ndigitals04/HNG-TASK1-API/API.py",
        "github_repo_url": "https://github.com/ndigitals04/HNG-TASK1-API",
        "status_code": 200
    }

    extra = request.args.get("extra")
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")
    if extra:
        userData["extra"] = extra

    if slack_name:
        userData["slack_name"] = slack_name

    if track:
        userData["track"] = track
    return jsonify(userData), 200

#@app.route("/create-user", methods=["POST"])
#def createUser():
#    data = request.get_json()
#    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
