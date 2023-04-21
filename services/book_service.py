from models.book_model import Book
from repositories.book_repository import BookRepository


class BookService:
    book_repository = BookRepository()

    def save_book(self, json_request):
        title = json_request["title"]
        author = json_request["author"]
        publication_date = json_request["publication_date"]

        book = Book(title, author, publication_date)
        return self.book_repository.save(book)

    def multiple_search(self, search_params):
        return self.book_repository.multiple_search(search_params)

    def search_all_books(self):
        return self.book_repository.search_all_books()

    def delete_book(self, id):
        return self.book_repository.delete(id)

