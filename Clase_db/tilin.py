import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_gmail(correo_destino, codigo_secreto):
    mi_correo = "codigorevistacecyte@gmail.com" 
    mi_llave = "kpvncfnhbzupioqc" 
    # --- CREAR EL MENSAJE ---
    mensaje = MIMEMultipart()
    mensaje['From'] = mi_correo
    mensaje['To'] = correo_destino
    mensaje['Subject'] = "🔐 Código de Acceso - CECYTE"

    cuerpo_html = f"""
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #e0e0e0; padding: 40px; border-radius: 8px; max-width: 600px; margin: auto; background-color: #ffffff;">
        <div style="text-align: center; border-bottom: 2px solid #800020; padding-bottom: 20px; margin-bottom: 20px;">
            <h2 style="color: #800020; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Sistema de Gestión Escolar - CECyTE</h2>
        </div>
        
        <p style="color: #333; font-size: 16px; line-height: 1.6;">Estimado(a) estudiante,</p>
        
        <p style="color: #333; font-size: 16px; line-height: 1.6;">Se ha solicitado un acceso para el portal institucional. Para completar su ingreso, por favor utilice el siguiente código de verificación:</p>
        
        <div style="background-color: #f4f4f4; padding: 25px; text-align: center; border-radius: 6px; margin: 30px 0; border: 1px dashed #800020;">
            <span style="font-size: 36px; font-weight: bold; color: #800020; letter-spacing: 8px;">{codigo_secreto}</span>
        </div>
        
        <p style="color: #555; font-size: 14px; font-style: italic;">Nota: Este código es personal e intransferible. Si usted no solicitó este acceso, por favor ignore este mensaje o repórtelo al departamento de soporte técnico.</p>
        
        <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; text-align: center; color: #777; font-size: 12px;">
            <p>© 2026 CECyTE - Dirección General<br>Excelencia Educativa para el Desarrollo Tecnológico</p>
        </div>
    </div>
    """
    mensaje.attach(MIMEText(cuerpo_html, 'html'))

    try:
        # --- CONEXIÓN AL SERVIDOR DE GOOGLE ---
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Encriptación necesaria
        server.login(mi_correo, mi_llave)
        server.send_message(mensaje)
        server.quit()
        print(f"✅ Correo enviado con éxito a {correo_destino}")
        return True
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
        return False
import random

# Diccionario temporal para guardar los códigos (Clave: correo, Valor: código)
codigos_temporales = {}

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/verificar', methods=['POST'])
def verificar():
    datos = request.get_json()
    correo_usuario = datos.get('correo') # Asegúrate que tu JS mande 'correo'

    try:
        conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre FROM Estudiantes WHERE correo = ?", (correo_usuario,))
        resultado = cursor.fetchone()

        if resultado:
            # 1. Generar código
            codigo = str(random.randint(1000, 9999))

            codigos_temporales[correo_usuario] = codigo
            
            # 2. MANDAR EL CORREO (Adiós terminal, hola Gmail)
            enviar_gmail(correo_usuario, codigo)

            return jsonify({
                "mensaje": f"Qué onda {resultado[0]}, revisa tu correo.",
                "codigo_enviado": True
            }), 200
        else:
            return jsonify({"mensaje": "Ese correo no está en el CECyTE"}), 404
        

    except Exception as ex:
        print(f"Error: {ex}")
        
        return jsonify({"status": "error", "mensaje": "Error de servidor"}), 500
    finally:
        if 'conexion' in locals():
            conexion.close()

# NUEVA RUTA para verificar el código que ingrese el usuario
@app.route('/verificar_codigo', methods=['POST'])
def verificar_codigo():
    datos = request.json
    correo = datos.get('correo')
    codigo_ingresado = datos.get('codigo')

    if codigos_temporales.get(correo) == codigo_ingresado:
        return jsonify({"mensaje": "¡Código Correcto! Entrando..."}), 200
    else:
        return jsonify({"mensaje": "Código incorrecto. Intenta de nuevo."}), 401

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)

    