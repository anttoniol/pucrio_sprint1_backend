class Book:
    def __init__(self, title, author, publication_date, id = None):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date

    def __dict__(self):
        return {
            "id": self.__id,
            "título": self.__title,
            "autor": self.__author,
            "data de publicação": self.__publication_date
        }

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_date(self):
        return self.__publication_date

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date