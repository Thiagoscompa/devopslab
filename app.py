from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Consegui fazer deploy no GCP com a minha conta Google - by Thiago Scompa"