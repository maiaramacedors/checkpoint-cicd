from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Checkpoint funcionando, versão 2 :)!"

@app.route("/status")
def status ():
    return "Aplicação funcionando corretamente."

@app.route("/sobre")
def sobre():
    return "Projeto desenvolvido para atividade referente as aulas 1, 2, e 3."

if __name__ == "__main__":
    app.run(debug=True)



