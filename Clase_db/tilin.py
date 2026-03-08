import random

# Diccionario temporal para guardar los códigos (Clave: correo, Valor: código)
codigos_temporales = {}

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/verificar', methods=['POST'])
def verificar():
    datos = request.get_json()
    correo_usuario = datos.get('correo')

    try:

        conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
        cursor = conexion.cursor()
        
        cursor.execute("SELECT nombre FROM Estudiantes WHERE correo = ?", (correo_usuario,))
        resultado = cursor.fetchone() 
        
        if resultado:
            # 1. Generar código de 4 dígitos
            codigo = str(random.randint(1000, 9999))
            # 2. Guardarlo en la memoria del servidor
            codigos_temporales[correo_usuario] = codigo
            
            print(f"Código para {correo_usuario}: {codigo}") # Lo verás en tu terminal

            nombre_alumno = resultado[0]
            return jsonify({
                "mensaje": f"Correo verificado. Bienvenido {resultado[0]}",
                "codigo_enviado": True 
            }), 200
        else:
            return jsonify({"mensaje": "Correo no encontrado"}), 404

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
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)

    