from flask import Flask, render_template, redirect, url_for, request, g, session, abort, send_file
import os
import logging

app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))

@app.route("/")
def index():
    return render_template('map.html')

@app.route('/hidden_login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'Elandia':
            session['logged_in'] = True
            return redirect(url_for('secret_page'))
        else:
            return redirect(url_for('index.html'))
    return render_template('index.html')

@app.route('/secret_page', methods=['POST'])
def secret_page():
    login()
    if not session.get('logged_in'):
        abort(401)
    return "UiTHack22{secret_poolparty_at_Coruscant}"

if __name__ == "__main__":
    app.run()