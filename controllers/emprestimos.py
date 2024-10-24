from flask import Flask, render_template, url_for, request, Blueprint, redirect
from models.user import User
from models.book import Book
from models.emprestimo import *

bp = Blueprint('emprestimo', __name__, url_prefix='/emprestimo')

@bp.route('/emprestimo', methods=['POST', 'GET'])
def emprestimo():
    if request.method == 'POST':
        emprestimo = request.form['id']
        titulo = request.form['titulo']
        user = request.form['user']

        emp = Emprestados(titulo,user)
        emp.emprestar_livro()
        emp.deletar_livro()
        


        return ''