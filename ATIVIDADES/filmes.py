from flask import Flask, jsonify
import os

app = Flask(__name__)

filmes = [
    {"id":1,"nome":"Death proof"},
    {"id":2,"nome":"Pulp Fiction"},
    {"id":3,"nome":"Home"}
]

@app.route("/")
def home():
    return (filmes)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(filmes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)