#importo flask
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
@app.route('/verificar', methods=['POST'])
def verificar():
    #se recibe el correo del usuario desde el login.js
    datos = request.get_json()
    correo_usuario = datos.get('correo')
try:
    conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
    print("Conexión exitosa")

    cursor = conexion.cursor()
    #se busca en la base de datos el correo del usuario para verificar si existe
    cursor.execute("SELECT nombre FROM Estudiantes WHERE correo = ?", (correo_usuario,))
    resulado = cursor.fetchone()
    if resultado:
        nombre_alumno = resultado[0]
        # aqui en donde luego se pondra la fucion para mandar el correo al alumno real --de tilin para goodman
        return jsonify ({
            "status": "success",
            "mensaje": f"Correo verificado para el alumno: {nombre_alumno} te enviamos un correo, espera un momento"
        }), 200
    else:
        return jsonify ({
            "status": "error",
            "mensaje": "El correo ingresado no pertenece a ningun alumno del Cecyte Morelos"
        }), 404
    if __name__ == '__main__':
        app.run(debug=True, port=5000)

except Exception as ex:
    print(f"Error al conectar o ejecutar consulta: {ex}")

finally:
    if 'conexion' in locals():
        conexion.close()
    