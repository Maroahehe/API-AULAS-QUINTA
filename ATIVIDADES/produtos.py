from flask import Flask, jsonify
import os

app = Flask(__name__)

produtos = [
    {"id":1,"Produtos":"Máscara de Tratamento Cavalo Forte Hidra Haskell 300g ","Preço":"R$56,50"},
    {"id":2,"Produtos":"Perfume Ange ou Demon Feminino Eau de Parfum 100ML GIVENCHY","Preço":"R$550,99 "}
]

@app.route("/")
def home():
    return (produtos)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(produtos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)