from flask import Flask, jsonify
import os

app = Flask(__name__)

alunos = [
    {"id":1,"nome":"Maria Luisa","Curso":"INFONET"},
    {"id":2,"nome":"Joao Pedro","Curso":"INFONET"}
]

@app.route("/")
def home():
    return (livros)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(livros)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)