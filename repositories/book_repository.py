from database.manager import DatabaseManager
from models.book_model import Book


class BookRepository:
    def convert_into_book_objects(self, query_result):
        books = list()

        for tuple in query_result:
            id = tuple[0]
            title = tuple[1]
            author = tuple[2]
            publication_date = tuple[3]
            book = Book(title, author, publication_date, id)
            books.append(book)

        return books
    def save(self, book):
        database_manager = DatabaseManager("library.db")
        insertion_command = f"INSERT INTO book (title, author, publication_date) VALUES ('{book.get_title()}', '{book.get_author()}', '{book.get_publication_date()}')"
        return database_manager.insert_into_table(insertion_command)

    def multiple_search(self, search_params):
        formatted_params = [f"{field} = '{value}'" for field, value in search_params.items()]

        database_manager = DatabaseManager("library.db")
        multiple_search_command = "SELECT * FROM book WHERE " + " AND ".join(formatted_params)
        result = database_manager.select_from_table(multiple_search_command)
        return (self.convert_into_book_objects(result[0]), result[1])

    def search_all_books(self):
        database_manager = DatabaseManager("library.db")
        search_all_command = f"SELECT * FROM book"
        result = database_manager.select_from_table(search_all_command)

        return (self.convert_into_book_objects(result[0]), result[1])

    def delete(self, id):
        database_manager = DatabaseManager("library.db")
        deletion_command = f"DELETE FROM book WHERE id = {id}"
        return database_manager.delete_from_table(deletion_command)
