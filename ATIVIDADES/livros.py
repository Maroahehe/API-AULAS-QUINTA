from flask import Flask, jsonify
import os

app = Flask(__name__)

livros = [
    {"id":1,"nome":"O gato preto","escritor":"Edgar Allan Poe"},
    {"id":2,"nome":"Annabel Lee","plataforma":"Edgar Alla"}
]

@app.route("/")
def home():
    return (livros)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(jogos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)