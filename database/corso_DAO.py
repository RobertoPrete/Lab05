# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


class CorsoDAO:
    @staticmethod
    def get_Allcorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from corso c"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cnx.close()
        return res

    @staticmethod
    def get_studenti_corso(codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select matricola from iscrizione i where i.codins=%s"""
        cursor.execute(query, codins)
        res = []
        for row in cursor:
            res.append(row["matricola"])
        return res
