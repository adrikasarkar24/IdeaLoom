from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MOOD_PROMPTS = {
    "Mysterious": "shrouded in secrets and half-spoken truths",
    "Whimsical": "filled with delightful absurdities and unexpected magic",
    "Romantic": "woven through with longing, connection, and tender feeling",
    "Adventurous": "driven by daring choices and uncharted horizons",
    "Melancholic": "tinged with beautiful sadness and quiet reflection",
    "Playful": "bursting with humor, mischief, and lighthearted twists",
}


@app.route("/")
def index():
    moods = list(MOOD_PROMPTS.keys())
    return render_template("index.html", moods=moods)


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    mood = data.get("mood", "").strip()
    theme = data.get("theme", "").strip()

    if not mood or mood not in MOOD_PROMPTS:
        return jsonify({"error": "Please select a valid mood."}), 400
    if not theme:
        return jsonify({"error": "Please enter a theme."}), 400

    mood_flavor = MOOD_PROMPTS[mood]
    idea = (
        f"In a world {mood_flavor}, a story about \"{theme}\" unfolds. "
        f"At its heart, a protagonist grappling with {theme.lower()} must navigate "
        f"a landscape {mood_flavor} — where every choice echoes further than expected "
        f"and the truth about {theme.lower()} is never quite what it seems. "
        f"Themes of identity, consequence, and wonder thread through the narrative, "
        f"leaving the reader with a lingering sense of the {mood.lower()}."
    )

    return jsonify({"idea": idea})


if __name__ == "__main__":
    app.run(debug=True)
