import base64
from flask import Flask, render_template, redirect, url_for, request, abort
import os
app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))

JABBA_NAME = 'Jabba Desilijic Tiure'

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        res = redirect(url_for('check_authentication'))
        token = encode_access(request.form['username'])
        res.set_cookie('access_token', token)
        return res
    return render_template('index.html')

@app.route("/authenticate")
def check_authentication():
    user_id = request.cookies.get('access_token')
    if user_id == encode_access(JABBA_NAME):
        return redirect(url_for('flag'))
    else:
        return redirect(url_for('login'))

def encode_access(username):
    encode_input = username.encode('ascii')
    token_bytes = base64.b64encode(encode_input)
    token = token_bytes.decode('ascii')
    return token


@app.route("/flag")
def flag():
    if not request.cookies.get('access_token') == encode_access(JABBA_NAME):
        abort(401)
    return render_template('flag.html')