import sqlite3
from datetime import datetime

# Crear/conectar base de datos
conn = sqlite3.connect('sql_simulado/resultados_tests.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS resultados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        test_name TEXT,
        status TEXT,
        duracion TEXT
    )
''')

# Insertar resultados de ejemplo
tests = [
    (datetime.now().strftime("%Y-%m-%d %H:%M"), "POST - Crear post exitosamente", "PASSED", "0.3s"),
    (datetime.now().strftime("%Y-%m-%d %H:%M"), "GET - Obtener post por ID valido", "PASSED", "0.1s"),
    (datetime.now().strftime("%Y-%m-%d %H:%M"), "GET - ID no existe", "PASSED", "0.1s"),
    (datetime.now().strftime("%Y-%m-%d %H:%M"), "PUT - Actualizar post", "PASSED", "0.2s"),
    (datetime.now().strftime("%Y-%m-%d %H:%M"), "DELETE - Eliminar post", "PASSED", "0.1s"),
]

cursor.executemany('INSERT INTO resultados (fecha, test_name, status, duracion) VALUES (?,?,?,?)', tests)
conn.commit()

# Mostrar resultados
print("\n RESULTADOS DE TESTS")
print("=" * 60)
for row in cursor.execute('SELECT * FROM resultados'):
    print(f"[{row[2]}] {row[3]} | {row[4]} | {row[1]}")

conn.close()
print("=" * 60)
print(" Base de datos actualizada!")