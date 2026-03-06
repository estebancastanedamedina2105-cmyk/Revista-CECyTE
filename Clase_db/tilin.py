import sqlite3

try:
    # 1. Usamos la ruta completa para que siempre encuentre el archivo
    # 2. Corregimos el nombre de la variable a 'conexion' para que sea más simple
    conexion = sqlite3.connect(r"C:\sqlite\bd proyects\Rev_Cecyte.db")
    print("Conexión exitosa")

    # El cursor debe ir AQUÍ, después de conectar con éxito
    cursor = conexion.cursor()
    cursor.execute("SELECT * from Profesores") 
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

except Exception as ex:
    print(f"Error al conectar o ejecutar consulta: {ex}")

finally:
    # Es buena práctica cerrar la conexión al terminar
    if 'conexion' in locals():
        conexion.close()
    