from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Checkpoint funcionando :)!"

@app.route("/status")
def status ():
    return "Aplicação funcionando corretamente."

if __name__ == "__main__":
    app.run(debug=True)



