from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    with open('data/projetos.json', 'r', encoding='utf-8') as f:
        projetos = json.load(f)
    return render_template('projetos.html', projetos=projetos)

@app.route('/saibamais')
def saibamais():
    return render_template('saibamais.html')

if __name__ == '__main__':
    app.run(debug=True)