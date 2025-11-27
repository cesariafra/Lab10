from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione
from model.tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """

    @staticmethod
    def get_all_sped():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Spedizione"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            sped = Spedizione(row['id'],
                              row['id_compagnia'],
                              row['numero_tracking'],
                              row['id_hub_origine'],
                              row['id_hub_destinazione'],
                              row['data_ritiro_programmata'],
                              row['distanza'],
                              row['data_consegna'],
                              row['valore_merce'])
            result.append(sped)
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_all_comp():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Compagnia"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            cp = Compagnia(row['id'], row['codice'], row['nome'])
            result.append(cp)
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_all_hub():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Hub"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            hb = Hub(row['id'],
                              row['codice'],
                              row['nome'],
                              row['citta'],
                              row['stato'],
                              row['latitudine'],
                              row['longitudine'])
            result.append(hb)
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_all_tratte():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Spedizione"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            tt = Tratta({row['id_hub_origine'], row['id_hub_destinazione']},
                        row['id_compagnia'],
                        row['distanza'],
                        row['valore_merce'],
                        row['valore_merce'],
                        1)
            if tt not in result:
                result.append(tt)
            else:
                for el in result:
                    if el == tt:
                        el.percorsa += 1
                        el.guadagno_totale += tt.guadagno_totale
                        el.guadagno_medio = el.guadagno_totale/el.percorsa
        cursor.close()
        cnx.close()
        return result


if __name__ == '__main__':
    print(DAO.get_all_sped())
    print(DAO.get_all_comp())
    print(DAO.get_all_hub())
    print(DAO.get_all_tratte())