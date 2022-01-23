from flask import Flask, render_template, redirect, url_for, request, g, session, abort, send_file
import os
import logging

app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()