# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


class CorsoDAO:
    @staticmethod
    def get_Allcorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM corso c"""
        cursor.execute(query)
        res = []
        # studenti = []
        for row in cursor:
            # codins = row["codins"]
            # new_query = """select matricola from iscrizione i where codins=%s"""
            # cursor.execute(new_query, codins)
            # for riga in cursor:
            # res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"], ))
        cnx.close()
        return res
