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
                "mensaje": f"Correo verificado. Te enviamos un codigo, espera un momento {resultado[0]}",
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

    