from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Teste para nova aula"

if __name__ == '__main__':
    app.run()
