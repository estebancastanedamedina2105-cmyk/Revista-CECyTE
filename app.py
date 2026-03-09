from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ---------------- LÓGICA DEL CHATBOT ----------------


def responder(mensaje):
    # Limpiamos el mensaje: minúsculas y quitar espacios extra
    msg = mensaje.lower().strip()

    # Diccionario de respuestas rápidas (más fácil de mantener que muchos elif)
    respuestas = {
        "hola": "¡Hola! 👋 Soy el asistente virtual de CECyTE. ¿En qué puedo apoyarte hoy?",
        "anuncio": "Puedes revisar los comunicados oficiales en la sección de Anuncios. 📢",
        "calendario": "El calendario escolar vigente lo encuentras en la sección de Calendario. 📅",
        "cafeteria": "¡Qué hambre! 🍕 El menú y los precios están en la sección de Cafetería.",
        "menu": "El menú de hoy ya está disponible en la sección de Cafetería. 🥤",
        "evento": "Hay actividades interesantes próximamente. Revísalas en la sección de Eventos. 🎈",
        "horario": "Tu horario de clases está disponible en la sección de Horarios. 🕒",
        "profesor": "La lista de docentes y sus perfiles está en la sección de Profesores. 👨‍🏫",
        "mapa": "Si estás perdido, el mapa del plantel está en la sección Mapa. 📍",
    }

    # Buscamos si alguna palabra clave está en el mensaje del usuario
    for clave in respuestas:
        if clave in msg:
            return respuestas[clave]

    # --- AQUÍ TU AMIGO DE LA BASE DE DATOS PUEDE AGREGAR ALGO COMO: ---
    # resultado = buscar_en_bd(msg)
    # if resultado: return resultado

    return "Lo siento, no tengo información sobre eso. 😕 Intenta preguntando por 'cafetería', 'eventos' o 'horarios'."


# ---------------- RUTAS DE LA REVISTA ----------------
# (Mantenemos tus rutas pero organizadas)


@app.route("/")
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


# ---------------- API DEL CHATBOT (CONEXIÓN JS) ----------------


@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        datos = request.get_json()
        if not datos or "mensaje" not in datos:
            return jsonify(
                {"respuesta": "Error: No se recibió un mensaje válido."}
            ), 400

        mensaje_usuario = datos["mensaje"]
        respuesta_bot = responder(mensaje_usuario)

        return jsonify({"respuesta": respuesta_bot})

    except Exception as e:
        return jsonify({"respuesta": "Ups, mi cerebro de robot tuvo un error."}), 500


# ---------------- EJECUCIÓN ----------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)
