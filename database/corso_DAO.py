# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


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
        cursor.execute(query, (codins,))
        res = []
        for row in cursor:
            res.append(row["matricola"])
        cnx.close()
        return res

    @staticmethod
    def get_all_codins():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select codins from corso c"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row["codins"])
        cnx.close()
        return res

    @staticmethod
    def get_codins(nome_corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select codins from corso c where c.nome=%s"""
        cursor.execute(query, (nome_corso,))
        res = []
        for row in cursor:
            res.append(row["codins"])
        cnx.close()
        return res

    @staticmethod
    def get_corsi_from_matricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.codins, c.crediti, c.nome, c.pd 
                    from corso c 
                    inner join iscrizione i 
                    on i.codins = c.codins 
                    where i.matricola = %s
                """
        cursor.execute(query, (matricola,))
        res = []
        for row in cursor:
            res.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cnx.close()
        return res


if __name__ == "__main__":
    print(CorsoDAO().get_Allcorsi())
    print(type(CorsoDAO().get_Allcorsi()))
