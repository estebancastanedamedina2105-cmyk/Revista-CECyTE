from flask import Flask, render_template , request

app = Flask(__name__)


@app.route("/")
def SitioWeb():
    return "¡Hola desde el chatbot!"


@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.form ['message']
    bot_reponse  process_text(user_message)
    


if __name__ == "__main__":
    app.run(debug=True)
