# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class StudenteDAO:

    @staticmethod
    def get_all_students():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from studente s"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cnx.close()
        return res
