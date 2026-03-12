import os
import configparser
import anthropic
from flask import Flask, render_template, request, jsonify
from rag import index_data, search

# Load API key: environment variable first, then config.ini fallback
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not ANTHROPIC_KEY:
    config = configparser.ConfigParser()
    config.read(os.path.join(BASE_DIR, "../config.ini"))
    ANTHROPIC_KEY = config.get("ANTHROPIC_API", "ANTHROPIC_KEY")

client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

app = Flask(__name__)

COMPANIES = ["AmazonHelp", "AppleSupport", "SpotifyCares", "Uber_Support"]

# Index data at startup
index_data()


@app.route("/")
def index():
    return render_template("index.html", companies=COMPANIES)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    company = data.get("company", "AmazonHelp")

    if not user_message:
        return jsonify({"error": "Message vide"}), 400

    # RAG: retrieve similar past interactions
    similar = search(user_message, company, n_results=3)

    # Build examples block
    examples_text = ""
    for ex in similar:
        examples_text += f'Customer: "{ex["customer_tweet"]}"\nAgent: "{ex["company_tweet"]}"\n\n'

    # Build prompt
    company_display = company.replace("Help", "").replace("Support", "").replace("Cares", "").replace("_Support", "")

    if examples_text:
        prompt = f"""You are a customer support chatbot for {company_display}.
Reply to the customer's message below. Match the tone, length and style of the examples provided.
Keep your reply concise and friendly, like a real Twitter support agent.

Examples of past interactions:
{examples_text}
Customer message: "{user_message}"
Your reply:"""
    else:
        prompt = f"""You are a customer support chatbot for {company_display}.
Reply to the customer's message below. Be concise, friendly and helpful.

Customer message: "{user_message}"
Your reply:"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    reply = response.content[0].text.strip()

    return jsonify({
        "reply": reply,
        "examples_used": len(similar),
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
