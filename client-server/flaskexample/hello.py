from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/", methods=['POST'])
def handleResult():
    val = request.form['input']
    if val == 'freedom':
        return 'yay'
    else:
        return 'nooo'

