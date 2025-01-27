# app.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load deck data from the JSON file
with open("deck_data.json", "r") as file:
    decks = json.load(file)

@app.route("/")
def index():
    return render_template("index.html", decks=decks)

    
@app.route("/group/<group_name>")
def group(group_name):
    """Page for a specific group."""
    if group_name in decks:
        return render_template("group.html", group_name=group_name, cards=decks[group_name])
    else:
        return f"Group '{group_name}' not found!", 404


if __name__ == "__main__":
    app.run()
