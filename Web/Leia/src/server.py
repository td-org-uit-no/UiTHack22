from flask import Flask, render_template, redirect, url_for, request, abort, session
import os
app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))

USERNAME = 'r3b3l_Le1a'
PASSWORD = 'May the 4th be with you'

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('flag'))
        else:
            return redirect(url_for('index.html'))
    return render_template('index.html')

@app.route("/flag")
def flag():
    if not session.get('logged_in'):
        abort(401)
    return render_template('flag.html')