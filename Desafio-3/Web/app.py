from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
cache_host = os.getenv("CACHE_HOST")

# Conexão PostgreSQL
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_pass
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mensagens (id SERIAL PRIMARY KEY, texto TEXT);")
conn.commit()

# Conexão Redis
cache = redis.Redis(host=cache_host, port=6379, db=0)

@app.route("/")
def home():
    # Testa Redis
    cache.set("ping", "pong")
    pong = cache.get("ping").decode()

    # Testa Postgres
    cur.execute("INSERT INTO mensagens (texto) VALUES ('Olá banco!')")
    conn.commit()

    return f"Flask OK → Redis: {pong} | Postgres: mensagem salva!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
