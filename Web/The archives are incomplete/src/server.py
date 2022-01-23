from flask import Flask, render_template, redirect, url_for, request, g, session, abort, send_file
import os
import logging

app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/w/<q1>/<q2>")
def wiki_redirect2(q1, q2):
    query_string = request.query_string.decode()
    redir_string = "https://en.wikipedia.org/w/" + q1 + q2 + "?" + query_string
    return redirect(redir_string)

@app.route("/w/<q1>")
def wiki_redirect(q1):
    query_string = request.query_string.decode()
    redir_string = "https://en.wikipedia.org/w/" + q1 + "?" + query_string
    return redirect(redir_string)


@app.route("/wiki/<wi>")
def wiki_art_redir(wi):
    redir_string = f"https://en.wikipedia.org/wiki/{wi}"
    return redirect(redir_string)

@app.route("/api/rest_v1/page/summary/<q1>")
def summary_redirect(q1):
    redir_string = "https://en.wikipedia.org/api/rest_v1/page/summary/" + q1
    return redirect(redir_string)

if __name__ == "__main__":
    app.run()