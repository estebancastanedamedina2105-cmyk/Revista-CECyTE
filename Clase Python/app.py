from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")


def responder(mensaje):

    mensaje = mensaje.lower()

    if "hola" in mensaje:
        return "Hola 👋 soy el asistente de CECyTE. ¿En qué puedo ayudarte?"

    elif "anuncio" in mensaje:
        return "Puedes ver los anuncios en la sección de anuncios."

    elif "calendario" in mensaje:
        return "El calendario escolar está en la sección calendario."

    elif "cafeteria" in mensaje or "menu" in mensaje:
        return "El menú de la cafetería está en la sección cafetería."

    elif "evento" in mensaje:
        return "Los eventos están en la sección eventos."

    elif "horario" in mensaje:
        return "El horario escolar está en la sección horario."

    else:
        return "No entendí tu pregunta. Intenta preguntar sobre anuncios, eventos o cafetería."


@app.route("/")
def inicio():
    return render_template("1_Anuncios.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    datos = request.get_json()
    mensaje = datos["mensaje"]

    respuesta = responder(mensaje)

    return jsonify({"respuesta": respuesta})


if __name__ == "__main__":
    app.run(debug=True)
