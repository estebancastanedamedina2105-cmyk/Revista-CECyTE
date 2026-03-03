from flask import Flask

app = Flask(__name__)


@app.route("/SitioWeb")
def SitioWeb():
    return "¡Hola desde el chatbot!"


if __name__ == "__main__":
    app.run(debug=True)
