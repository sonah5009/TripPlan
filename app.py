# execute this command in the terminal on the path existing "app.py"
#  flask --app app run
# http://127.0.0.1:5000/zhfldk82/795607ba-d790-4acc-8583-4ee1b7bac10c/chat
from flask import Flask, jsonify, render_template, request

from chatbot.chatbot import Chatbot

# input 'pwd' command in the terminal
# then you can check your path:
'''
# example
(krTrip) ➜  TripPlan git: (main) ✗ pwd
/Users/sonah/Library/CloudStorage/OneDrive-ZHAW/ML2/TripPlan
'''

MYDIR = ""  # input your path
DBPATH = "database"
DBFILE = "chatbot.db"  # you can change database file name

app = Flask(__name__)


@app.route("/")
def index():
    return "Ok. Your chatbot app is running. But the URL you used is missing the type_id and user_id path variables."


@app.route("/<type_id>/<user_id>/chat")
def chatbot(type_id: str, user_id: str):
    return render_template("index.html")


@app.route("/<type_id>/<user_id>/info")
def info_retrieve(type_id: str, user_id: str):
    bot: Chatbot = Chatbot(
        database_file=MYDIR
        + "/" + DBPATH + "/" + DBFILE,
        type_id=type_id,
        user_id=user_id,
    )
    response: dict[str, str] = bot.info_retrieve()
    return jsonify(response)


@app.route("/<type_id>/<user_id>/conversation")
def conversation_retrieve(type_id: str, user_id: str):
    bot: Chatbot = Chatbot(
        database_file=MYDIR
        + "/" + DBPATH + "/" + DBFILE,
        type_id=type_id,
        user_id=user_id,
    )
    response: list[dict[str, str]] = bot.conversation_retrieve()
    return jsonify(response)


@app.route("/<type_id>/<user_id>/response_for", methods=["POST"])
def response_for(type_id: str, user_id: str):
    user_says = None
    # content_type = request.headers.get('Content-Type')
    # if (content_type == 'application/json; charset=utf-8'):
    user_says = request.json
    # else:
    #    return jsonify('/response_for request must have content_type == application/json')

    bot: Chatbot = Chatbot(
        database_file=MYDIR
        + "/" + DBPATH + "/" + DBFILE,
        type_id=type_id,
        user_id=user_id,
    )
    assistant_says_list: list[str] = bot.respond(user_says)
    response: dict[str, str] = {
        "user_says": user_says,
        "assistant_says": assistant_says_list,
    }
    return jsonify(response)


@app.route("/<type_id>/<user_id>/reset", methods=["DELETE"])
def reset(type_id: str, user_id: str):
    bot: Chatbot = Chatbot(
        database_file=MYDIR
        + "/" + DBPATH + "/" + DBFILE,
        type_id=type_id,
        user_id=user_id,
    )
    bot.reset()
    assistant_says_list: list[str] = bot.start()
    response: dict[str, str] = {
        "assistant_says": assistant_says_list,
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
