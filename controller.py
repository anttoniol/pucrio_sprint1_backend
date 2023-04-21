import json

import flask
from flask import Flask, request

from database.initializer import initialize_database
from services.book_service import BookService

app = Flask(__name__)

book_service = BookService()

def format_objects(objects):
    formatted_objects = list()
    for object in objects:
        formatted_objects.append(object.__dict__())
    return formatted_objects

def create_response(body, status_code):
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    return flask.Response(status = status_code, response = json.dumps(body), headers = headers, mimetype = "application/json")

@app.route('/', methods = ['GET'])
def hello():
    body = {"mensagem": 'Olá! Esta aplicação está no ar!'}
    return create_response(body, 200)

@app.route('/book', methods = ['POST'])
def save_book():
    json_request = request.get_json()
    success = book_service.save_book(json_request)
    if success:
        body = {"mensagem": "Livro inserido com sucesso!"}
        return create_response(body, 200)

    body = {"mensagem": "Erro ao inserir livro!"}
    return create_response(body, 500)

@app.route('/book', methods = ['GET'])
def search_book():
    search_params = request.args.to_dict()
    result = book_service.multiple_search(search_params)

    books = result[0]
    success = result[1]

    formatted_books = format_objects(books)
    body = {"livros": formatted_books}

    if success:
        return create_response(body, 200)

    return create_response(body, 500)

@app.route('/book/all', methods = ['GET'])
def search_all_books():
    result = book_service.search_all_books()

    books = result[0]
    success = result[1]

    formatted_books = format_objects(books)
    body = {"livros": formatted_books}

    if success:
        return create_response(body, 200)

    return create_response(body, 500)

@app.route('/book', methods = ['DELETE'])
def delete_book():
    book_id = request.args.get("id")
    success = book_service.delete_book(book_id)

    if success:
        body = {"mensagem": "Livro removido com sucesso!"}
        return create_response(body, 200)

    body = {"mensagem": "Erro ao remover livro!"}
    return create_response(body, 500)

if __name__ == '__main__':
    initialize_database()
    app.run(host = '127.0.0.1', port = 5000)