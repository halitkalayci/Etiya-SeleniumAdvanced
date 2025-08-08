import psycopg2

connection = psycopg2.connect(
    host="193.203.191.79",
    port="32001",
    database="testdb",
    user="postgres",
    password="1234"
)

print(connection.info.status)

connection.close()