from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Checkpoint funcionando :)!"

if __name__ == "__main__":
    app.run(debug=True)
