import sqlite3

conn = sqlite3.connect('sql_simulado/resultados_tests.db')
cursor = conn.cursor()

print("\n TODOS LOS RESULTADOS:")
print("=" * 60)
for row in cursor.execute('SELECT * FROM resultados'):
    print(row)

print("\n SOLO PASSED:")
print("=" * 60)
for row in cursor.execute("SELECT * FROM resultados WHERE status = 'PASSED'"):
    print(row)

print("\n TOTAL TESTS PASADOS:")
print("=" * 60)
for row in cursor.execute("SELECT COUNT(*) as total FROM resultados WHERE status = 'PASSED'"):
    print(f"Total: {row[0]}")

conn.close()
