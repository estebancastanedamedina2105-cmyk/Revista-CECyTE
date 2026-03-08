from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ---------------- CHATBOT ----------------


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
        return "No entendí tu pregunta."


# ---------------- PAGINA PRINCIPAL ----------------


@app.route("/")
def inicio():
    return render_template("1_Anuncios.html")


# ---------------- PAGINAS REVISTA ----------------


@app.route("/anuncios")
def anuncios():
    return render_template("1_Anuncios.html")


@app.route("/profesores")
def profesores():
    return render_template("2_Profesores.html")


@app.route("/calendario")
def calendario():
    return render_template("3_Calendario.html")


@app.route("/cafeteria")
def cafeteria():
    return render_template("4_Cafeteria.html")


@app.route("/login")
def login():
    return render_template("5_Login.html")


@app.route("/perfil")
def perfil():
    return render_template("6_Perfil.html")


@app.route("/chismografo")
def chismografo():
    return render_template("7_Chismografo.html")


@app.route("/eventos")
def eventos():
    return render_template("8_Eventos.html")


@app.route("/alumnos_destacados")
def alumnos_destacados():
    return render_template("9_AlumnosDesta.html")


@app.route("/convocatorias")
def convocatorias():
    return render_template("10_Convocatoria.html")


@app.route("/mapa")
def mapa():
    return render_template("11_Mapa.html")


@app.route("/horario")
def horario():
    return render_template("12_Horario.html")


# ---------------- CHATBOT API ----------------


@app.route("/chatbot", methods=["POST"])
def chatbot():
    datos = request.get_json()
    mensaje = datos["mensaje"]

    respuesta = responder(mensaje)

    return jsonify({"respuesta": respuesta})


# ---------------- EJECUTAR SERVIDOR ----------------

if __name__ == "__main__":
    app.run(debug=True)
