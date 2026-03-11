import random
import os
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3

# Diccionario temporal para guardar los códigos (Clave: correo, Valor: código)
codigos_temporales = {}
# --- LÓGICA DEL CHATBOT ---
def responder(mensaje):
    msg = mensaje.lower().strip()
    respuestas = {
        "hola": "¡Hola! 🤖 Soy CoyoBot...",
        "anuncio": "Los comunicados están en la sección de Anuncios. 📢",
        "cafeteria": "¡Energía necesaria! 🍕",
        # ... todas las respuestas que tiene el app.py de tu amigo
    }
    for clave, respuesta in respuestas.items():
        if clave in msg:
            return respuesta
    return "Lo siento, mi base de datos no reconoce esa consulta. 😟"


# Esto detecta la carpeta "Clase_db"
base_dir = os.path.abspath(os.path.dirname(__file__))

# Esto apunta a las carpetas que están UN NIVEL ARRIBA de Clase_db
template_dir = os.path.join(base_dir, '..', 'templates')
static_dir = os.path.join(base_dir, '..', 'static')

app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)
@app.route("/")
def anuncios():
    return render_template("1_Anuncios.html")

@app.route('/login.html')
def index():
    return render_template('5_Login.html')
   
@app.route('/verificar_correo', methods=['POST'])
def verificar_correo():
    datos = request.get_json()
    correo_usuario = datos.get('correo')
    
    MI_CORREO = "codigorevistacecyte@gmail.com" 
    MI_PASSWORD = "kpvncfnhbzupioqc"
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
        cursor = conexion.cursor()
        
        # Buscar el nombre del alumno
        cursor.execute("SELECT nombre FROM Estudiantes WHERE correo = ?", (correo_usuario,))
        resultado = cursor.fetchone()

        if resultado:
            nombre_alumno = resultado[0]
            codigo = str(random.randint(1000, 9999))
            codigos_temporales[correo_usuario] = codigo

            # --- PREPARAR EL CORREO ---
            msg = EmailMessage()
            msg['Subject'] = f"Tu Código: {codigo} - Revista CECyTE"
            msg['From'] = MI_CORREO
            msg['To'] = correo_usuario
            
            # Texto plano (por si el correo no carga el HTML)
            msg.set_content(f"Hola {nombre_alumno}, tu código es: {codigo}")

            # Insertar el diseño HTML
            cuerpo_final = HTML_DISENO.format(nombre=nombre_alumno, codigo=codigo)
            msg.add_alternative(cuerpo_final, subtype='html')

            # --- ENVÍO POR SMTP ---
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(MI_CORREO, MI_PASSWORD)
                smtp.send_message(msg)

            print(f"Correo enviado a {correo_usuario} exitosamente.")
            return jsonify({"mensaje": "Código enviado", "codigo_enviado": True}), 200
            
        else:
            return jsonify({"mensaje": "El correo no está registrado"}), 404

    except Exception as ex:
        print(f"Error detectado: {ex}")
        return jsonify({"mensaje": "Error al procesar la solicitud"}), 500
    finally:
        if 'conexion' in locals():
            conexion.close()


HTML_DISENO = """
<html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; padding: 20px;">
        <div style="max-width: 450px; margin: auto; background: #ffffff; padding: 30px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-align: center; border-top: 5px solid #004581;">
            <h1 style="color: #004581; margin-bottom: 10px;">Revista CECyTE</h1>
            <p style="color: #555; font-size: 16px;">Hola <strong>{nombre}</strong>,</p>
            <p style="color: #777; line-height: 1.5;">Has solicitado un código para ingresar al sistema. Copia y pega el siguiente código en la página:</p>
            
            <div style="background-color: #e8f0fe; padding: 20px; margin: 25px 0; border-radius: 10px; border: 1px dashed #1a73e8;">
                <span style="font-size: 35px; font-weight: bold; color: #1a73e8; letter-spacing: 12px;">
                    {codigo}
                </span>
            </div>
            
            <p style="font-size: 12px; color: #999; margin-top: 25px;">Este es un mensaje automático. Por favor no respondas a este correo.</p>
            <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
            <p style="font-size: 11px; color: #bbb;">© 2026 Prototipo de Informática - Revista Estudiantil</p>
        </div>
    </body>
</html>
"""

@app.route('/comprobar_codigo', methods=['POST'])
def comprobar_codigo():
    datos = request.get_json()
    correo = datos.get('correo')
    codigo_usuario = datos.get('codigo')

    # Verificamos si el código coincide con el que guardamos antes
    if correo in codigos_temporales and codigos_temporales[correo] == codigo_usuario:
        # Si es correcto, lo borramos para que no se use de nuevo
        del codigos_temporales[correo] 
        return jsonify({"mensaje": "Acceso concedido"}), 200
    else:
        return jsonify({"mensaje": "Código incorrecto o expirado"}), 400

@app.route('/publicar_comentario', methods=['POST'])
def publicar_comentario():
    datos = request.json
    texto = datos.get('contenido')
    
    conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Comentarios (contenido) VALUES (?)", (texto,))
    conexion.commit()
    conexion.close()
    return jsonify({"status": "success"}), 200

@app.route('/dar_like', methods=['POST'])
def dar_like():
    datos = request.get_json()
    id_comentario = datos.get('id') # Necesitamos el ID del comentario
    
    try:
        conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
        cursor = conexion.cursor()
        # Aquí sumamos 1 al contador de esa fila específica
        cursor.execute("UPDATE Comentarios SET likes = likes + 1 WHERE id = ?", (id_comentario,))
        conexion.commit()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

@app.route('/obtener_comentarios', methods=['GET'])
def obtener_comentarios():
    try:
        conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
        cursor = conexion.cursor()
        # Seleccionamos id, contenido y likes (importante para el contador)
        cursor.execute("SELECT id, contenido, likes FROM Comentarios ORDER BY id DESC")
        filas = cursor.fetchall()
        
        # Convertimos a una lista de diccionarios
        comentarios = [
            {"id": f[0], "contenido": f[1], "likes": f[2] if f[2] else 0} 
            for f in filas
        ]
        return jsonify(comentarios), 200
    except Exception as e:
        print(f"Error en Python: {e}")
        return jsonify([]), 500
    finally:
        conexion.close()

        # --- RUTA DEL CHATBOT ---
@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        datos = request.get_json()
        mensaje_usuario = datos.get("mensaje", "")
        respuesta_bot = responder(mensaje_usuario)
        return jsonify({"respuesta": respuesta_bot})
    except Exception as e:
        return jsonify({"respuesta": "Error en mi núcleo."}), 500

# --- RUTAS DE LA REVISTA ---


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

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    