import psycopg2

connection = psycopg2.connect(
    host="193.203.191.79",
    port="32001",
    database="testdb",
    user="postgres",
    password="1234"
)

cursor = connection.cursor()

cursor.execute("SELECT version();")

ver = cursor.fetchone()

print(ver)

cursor.execute("Select * from users;")

users = cursor.fetchall()

for row in users:
    print(f"User id: {row[0]} Name: {row[1]}")

connection.close()