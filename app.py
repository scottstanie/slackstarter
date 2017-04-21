from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


# Example of dict format sent by slack:
# Use this info if you want to do fancier stuff!

# request.form
# ImmutableMultiDict([
#     ('user_id', u'UAAAAAAAA'),
#     ('response_url', u'https://hooks.slack.com/commands/AAAAA9BR3/AAAAAA369701/5AAAAAAApWyijzLi0eRmlAiW'),
#     ('text', u'@scott hey'),
#     ('token', u'IAAAAAAAAAAAATJdVv4e6r92'),
#     ('channel_id', u'CAAAAAAA0'),
#     ('team_id', u'TAAAAAAR3'),
#     ('command', u'/robot'),
#     ('team_domain', u'funteam'),
#     ('user_name', u'scott'),
#     ('channel_name', u'bot-test')]
# )

@app.route("/slack", methods=["POST"], strict_slashes=False)
def hello():
    print("Request sent by: %s" % request.form['user_name'])
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
