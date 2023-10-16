from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá Mundo!!!"

if __name__ == 'main':
    app.run(host='0.0.0.0', port=8000)

