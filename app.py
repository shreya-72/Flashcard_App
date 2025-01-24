# app.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# # Flashcards data
# decks = {
#     "Group1": [
#         {
#             "word": "Equivocate",
#             "info": "<b>Part of Speech:</b> Verb<br><b>Definition:</b> To use ambiguous language to conceal the truth or avoid committing to a position.<br><b>Example:</b> The politician equivocated when asked about his stance on the issue."
#         },
#         {
#             "word": "Loquacious",
#             "info": "<b>Part of Speech:</b> Adjective<br><b>Definition:</b> Tending to talk a great deal; talkative.<br><b>Example:</b> She was so loquacious that meetings lasted twice as long as necessary."
#         }
#     ],
#     "Group2": [
#         {
#             "word": "Obfuscate",
#             "info": "<b>Part of Speech:</b> Verb<br><b>Definition:</b> To render obscure, unclear, or unintelligible.<br><b>Example:</b> The professor's lengthy explanation only served to obfuscate the main point."
#         }
#     ]
# }

# Load deck data from the JSON file
with open("deck_data.json", "r") as file:
    decks = json.load(file)

@app.route("/")
def index():
    return render_template("templates\index.html", decks=decks)

# @app.route("/get_card", methods=["POST"])
# def get_card():
#     data = request.json
#     deck_name = data.get("deck")
#     card_index = data.get("index", 0)

#     if deck_name in decks and 0 <= card_index < len(decks[deck_name]):
#         card = decks[deck_name][card_index]
#         return jsonify({"success": True, "card": card})
#     return jsonify({"success": False, "message": "Invalid deck or card index"})
    
@app.route("/group/<group_name>")
def group(group_name):
    """Page for a specific group."""
    if group_name in decks:
        return render_template("group.html", group_name=group_name, cards=decks[group_name])
    else:
        return f"Group '{group_name}' not found!", 404


if __name__ == "__main__":
    app.run(debug=True)
