import os
import time

from flask import Flask
import mysql.connector

TITLE = "SP22-BCS-108 Registry"
REGISTRATION = "SP22-BCS-108"

app = Flask(__name__)


def connect():
    last_error = None
    for _ in range(30):
        try:
            return mysql.connector.connect(
                host=os.environ.get("DB_HOST", "db"),
                port=int(os.environ.get("DB_PORT", "3306")),
                database=os.environ.get("DB_NAME", "sp22bcs108"),
                user=os.environ.get("DB_USER", "appuser"),
                password=os.environ.get("DB_PASSWORD", "AppUser108"),
            )
        except Exception as exc:
            last_error = exc
            time.sleep(2)
    raise last_error


def load_record():
    connection = connect()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT registration, full_name, title FROM registry ORDER BY id LIMIT 1"
        )
        return cursor.fetchone()
    finally:
        connection.close()


@app.get("/")
def home():
    record = load_record()
    registration = record["registration"] if record else REGISTRATION
    full_name = record["full_name"] if record else "Abidurahman shinwari"
    title = record["title"] if record else TITLE
    return f"""<!doctype html>
<html>
<head><title>{title}</title></head>
<body>
  <h1>{title}</h1>
  <p>Registration Number: {registration}</p>
  <p>Name: {full_name}</p>
  <p>This page is read from the MySQL database.</p>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
