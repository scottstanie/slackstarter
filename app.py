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


@app.route("/slack", methods=["POST"], strict_slashes=False)
def hello():
    url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'
    response = requests.get(url).json()
    try:
        quote_of_day = response[0]['content']
        # For formatting info, see https://api.slack.com/docs/message-formatting
        quote_of_day = quote_of_day.replace('&', '&amp;',).replace('<p>', '').replace('</p>', '')
    except:
        quote_of_day = "Some days are just bad days... That's all"

    response = {
        "text": "Your quote of the day!",
        "attachments": [{"text": quote_of_day}]
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=8000)
