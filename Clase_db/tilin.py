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
        # Esto tiene DOS TABS de distancia (uno por la función, otro por el try)
        conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
        cursor = conexion.cursor()
        
        cursor.execute("SELECT nombre FROM Estudiantes WHERE correo = ?", (correo_usuario,))
        resultado = cursor.fetchone() 
        
        if resultado:
            nombre_alumno = resultado[0]
            return jsonify({
                "status": "success",
                "mensaje": f"Correo verificado para el alumno: {nombre_alumno}"
            }), 200
        else:
            return jsonify({
                "status": "error",
                "mensaje": "El correo ingresado no pertenece a ningún alumno"
            }), 404
            
    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({"status": "error", "mensaje": "Error de servidor"}), 500
    finally:
        if 'conexion' in locals():
            conexion.close()
if __name__ == '__main__':
    app.run(debug=True, port=5000)