from flask import Flask, request
from chatbot import chatbot
app = Flask(__name__)

@app.route("/message", methods=["POST"])
def message():
    incoming_msg = request.values["body"]
    print(incoming_msg)
    answer = chatbot.ask(incoming_msg)
    return str(answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)