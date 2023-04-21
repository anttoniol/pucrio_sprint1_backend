from database.manager import DatabaseManager


def initialize_database():
    database_manager = DatabaseManager("library.db")
    creation_command = "CREATE TABLE IF NOT EXISTS book" \
                       "(" \
                           "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                           "title TEXT NOT NULL, " \
                           "author TEXT NOT NULL, " \
                           "publication_date TEXT NOT NULL" \
                       ")"
    return database_manager.create_table(creation_command)
