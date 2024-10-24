from flask import Flask, render_template
from controllers import users, books

app = Flask(__name__)
app.register_blueprint(users.bp)
app.register_blueprint(books.bp)

@app.route('/')
def login():
    return '<h1>Página Inicial</h1>'
