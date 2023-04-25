import json

import flask
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

from base_models.book_body import BookBody
from base_models.book_path import BookPath
from base_models.book_query import BookQuery
from database.initializer import initialize_database
from services.book_service import BookService

info = Info(title = "Library API", version = "1.0.0")
app = OpenAPI(__name__, info = info)
book_tag = Tag(name = "book", description = "Some book")

book_service = BookService()

def format_objects(objects):
    formatted_objects = list()
    for object in objects:
        formatted_objects.append(object.__dict__())
    return formatted_objects

def create_response(body, status_code):
    headers = {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST, GET, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': '*'
    }
    return flask.Response(status = status_code, response = json.dumps(body),
                          headers = headers, mimetype = "application/json", content_type = "application/json")

@app.get("/book/", summary = "Search books", tags = [book_tag])
def get_books(query: BookQuery):
    filled_params = query.get_filled_params()

    if len(list(filled_params.keys())) == 0:
        result = book_service.search_all_books()
    else:
        result = book_service.multiple_search(filled_params)

    books = result[0]
    success = result[1]

    formatted_books = format_objects(books)
    body = {"livros": formatted_books}

    if success:
        return create_response(body, 200)
    return create_response(body, 500)

@app.post("/book/", summary = "Save a book", tags = [book_tag])
def save_book(body: BookBody):
    result = book_service.save_book(body.dict())
    success = result[1]

    if success:
        id = result[0]
        body = {"mensagem": "Livro salvo com sucesso!", "id": id}
        return create_response(body, 200)
    body = {"mensagem": "Erro ao salvar livro!"}
    return create_response(body, 500)

@app.delete('/book/<id>', summary = "Delete a book", tags = [book_tag])
def delete_book(path: BookPath):
    success = book_service.delete_book(path.id)

    if success:
        body = {"mensagem": "Livro removido com sucesso!"}
        return create_response(body, 200)

    body = {"mensagem": "Erro ao remover livro!"}
    return create_response(body, 500)

if __name__ == '__main__':
    initialize_database()
    app.run(host = 'localhost', port = 5000)
