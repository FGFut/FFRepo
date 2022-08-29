from flask import Flask, render_template

#usar python 3.8

app = Flask(__name__)

@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/partidas.html')
def partidas():
    return render_template('partidas.html')

if __name__ == "__main__":
    app.run(debug=True)
