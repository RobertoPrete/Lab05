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

    @staticmethod
    def get_studenti_corso(codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select s.nome, s.cognome, s.matricola 
                    from iscrizione i inner join studente s on i.matricola=s.matricola 
                    where i.codins=%s"""
        cursor.execute(query, (codins,))
        res = []
        for row in cursor:
            res.append((row["nome"], row["cognome"], row["matricola"]))
        cnx.close()
        return res

    @staticmethod
    def get_num_studenti_corso(codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select count(matricola) 
                    from iscrizione i 
                    where i.codins = %s"""
        cursor.execute(query, (codins,))
        res = []
        for row in cursor:
            res.append(row["count(matricola)"])
        cnx.close()
        return res


if __name__ == "__main__":
    res = StudenteDAO.get_num_studenti_corso("02CIXPG")
    print(res)
    print(type(res))
    print(res[0])

