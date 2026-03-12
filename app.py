# .\bastixs\Scripts\Activate.ps1
# cd Clase_db
# Python tilin.py
# deactivate

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# --- LÓGICA DEL CHATBOT ---
def responder(mensaje):
    msg = mensaje.lower().strip()

    respuestas = {
        "hola": "¡Hola! 🤖 Soy CoyoBot, el asistente futurista de CECyTE. ¿En qué dimensión puedo ayudarte hoy?",
        "anuncio": "Los comunicados intergalácticos (y oficiales) están en la sección de Anuncios. 📢",
        "calendario": "El continuo espacio-tiempo escolar está en la sección de Calendario. 📅",
        "cafeteria": "¡Energía necesaria! 🍕 El menú de la estación de combustible está en Cafetería.",
        "menu": "El combustible de hoy ya está listado en la sección de Cafetería. 🥤",
        "evento": "Hay anomalías divertidas próximamente. Revísalas en Eventos. 🎈",
        "horario": "Tu cronograma de actividades está en la sección de Horarios. 🕒",
        "profesor": "Los maestros Jedi de la institución están en la sección de Profesores. 👨‍🏫",
        "mapa": "Si te perdiste en el cuadrante, el mapa del plantel está en la sección Mapa. 📍",
    }

    for clave, respuesta in respuestas.items():
        if clave in msg:
            return respuesta

    return "Lo siento, mi base de datos no reconoce esa consulta. 😕 Intenta con 'cafetería', 'eventos' o 'horario'."


# --- RUTA DE LA API DEL CHATBOT ---
@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        datos = request.get_json()
        mensaje_usuario = datos.get("mensaje", "")
        respuesta_bot = responder(mensaje_usuario)
        return jsonify({"respuesta": respuesta_bot})
    except Exception as e:
        return jsonify({"respuesta": "Error en mi núcleo de procesamiento."}), 500


# --- RUTAS DE LA REVISTA (VISTAS) ---
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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
