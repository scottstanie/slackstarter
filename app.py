from flask import Flask, jsonify
import requests

app = Flask(__name__)


# Example of dict format sent by slack:
# Use this info if you want to do fancier stuff!
# {token=gIkuvaNzQIHg97ATvDxqgjtO
# team_id=T0001
# team_domain=example
# channel_id=C2147483705
# channel_name=test
# user_id=U2147483697
# user_name=Steve
# command=/weather
# text=94070
# response_url=https://hooks.slack.com/commands/1234/5678}

def get_quote():
    url = 'http://quotes.rest/qod.json'
    response = requests.get(url).json()
    try:
        quote_of_day = response['contents']['quotes'][0]['quote']
    except:
        quote_of_day = "Some days are just bad days... That's all"

    return quote_of_day


@app.route("/slack", methods=["POST"], strict_slashes=False)
def hello():
    qod = get_quote()
    response = {
        "text": "Your quote of the day!",
        "attachments": [{"text": qod}]
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=8000)
