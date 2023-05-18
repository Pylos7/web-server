from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello!!</p>"

@app.route("/blog")
def blog():
    return "<pThese are my thoughts on blogs</p>"