from flask import Flask, request
from lexi_growth.application.lexi_flow_handler import handle_lexi_flow, handle_lexi_merge_to_known

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"


@app.route("/filter", methods=["POST"])
def filter():
    text = request.json["text"]
    word_items = handle_lexi_flow(text)
    return [
        {
            "word": word_item.word,
            "count": word_item.count,
            "definition": word_item.definition,
            "translation": word_item.translation,
        }
        for word_item in word_items
    ]

@app.route("/merge-to-known", methods=["POST"])
def merge_to_known():
    word = request.json["word"]
    handle_lexi_merge_to_known(word)
    return "OK"
