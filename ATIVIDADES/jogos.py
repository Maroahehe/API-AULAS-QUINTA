from flask import Flask, jsonify
import os

app = Flask(__name__)

jogos = [
    {"id":1,"nome":"Minecraft","plataforma":"PC"},
    {"id":2,"nome":"Devil may cry 5","plataforma":"PlayStation"}
]

@app.route("/")
def home():
    return (jogos)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(jogos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)