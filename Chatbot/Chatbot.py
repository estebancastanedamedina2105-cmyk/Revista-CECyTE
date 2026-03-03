from flask import Flask, render_template, request
from chatbot import process_text

app = Flask(__name__)


@app.route("/")
def SitioWeb():
    return render_template("1-Anuncios.html")


@app.route("/chatbot", methods=["POST"])  # type: ignore
def chatbot():
    user_message = request.form["message"]
    bot_reponse = process_text(user_message)
    return jsonify({"response": bot_reponse})  # type: ignore


if __name__ == "__main__":
    app.run(debug=True)
