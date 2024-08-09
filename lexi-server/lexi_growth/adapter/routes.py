from flask import Flask, request
from lexi_growth.application.lexi_flow_handler import handle_lexi_flow, handle_lexi_merge_to_known, handle_lexi_revert_word
from lexi_growth.application.auto_text_extractor import auto_extract_text

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

@app.route("/filter", methods=["POST"])
def filter():
    text = request.json["text"]
    extractd_text = auto_extract_text(text)
    word_items = handle_lexi_flow(extractd_text)
    return [
        {
            "word": word_item.word,
            "count": word_item.count,
            "definition": word_item.definition,
            "translation": word_item.translation,
            "difficulty": word_item.difficulty
        }
        for word_item in word_items
    ]

@app.route("/merge-to-known", methods=["POST"])
def merge_to_known():
    word = request.json["word"]
    handle_lexi_merge_to_known(word)
    return "OK"

@app.route("/revert-word", methods=["POST"])
def revert_word():
    word = request.json["word"]
    handle_lexi_revert_word(word)
    return "OK"

@app.route("/extract-text", methods=["POST"])
def extract_text():
    resource_locator = request.json["resourceLocator"]
    text = auto_extract_text(resource_locator)
    return {"text": text}