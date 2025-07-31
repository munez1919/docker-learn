from flask import Flask
import redis
import os

app = Flask(__name__)

# Подключаемся к Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def index():
    r.incr("visits")  # Увеличиваем счётчик
    count = r.get("visits")
    with open("logs/app.log", "a") as log:
        log.write(f"Кто-то зашёл! Всего посещений: {count}\n")
    return f"Привет! Ты заходил {count} раз(а)."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

