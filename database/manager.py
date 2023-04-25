import logging
import sqlite3

class DatabaseManager:
    def __init__(self, database_name):
        try:
            self.__connection = sqlite3.connect(database_name)
            self.__cursor = self.__connection.cursor()
        except sqlite3.Error as error:
            logging.error("Erro ao conectar com o banco de dados: ", error)

    def create_table(self, creation_command):
        success = False
        try:
            self.__cursor.execute(creation_command)
            success = True
        except sqlite3.Error as error:
            logging.error("Erro ao criar tabela: ", error)
        finally:
            return self.close_connection() and success

    def select_from_table(self, selection_command):
        success = False
        search_result = list()
        try:
            search_result = self.__cursor.execute(selection_command).fetchall()
            success = True
        except sqlite3.Error as error:
            logging.error("Erro ao obter dados da tabela: ", error)
        finally:
            return (search_result, self.close_connection() and success)

    def insert_into_table(self, insertion_command):
        id = None
        success = False
        try:
            self.__cursor.execute(insertion_command)
            self.__connection.commit()
            id = self.__cursor.lastrowid
            success = True
        except sqlite3.Error as error:
            logging.error("Erro ao inserir dados na tabela: ", error)
        finally:
            return (id, self.close_connection() and success)

    def delete_from_table(self, deletion_command):
        success = False
        try:
            self.__cursor.execute(deletion_command)
            self.__connection.commit()
            success = True
        except sqlite3.Error as error:
            logging.error("Erro ao remover dados da tabela: ", error)
        finally:
            return self.close_connection() and success

    def close_connection(self):
        try:
            self.__connection.close()
            return True
        except sqlite3.Error as error:
            logging.error("Erro ao desconectar do banco de dados: ", error)
            return False
