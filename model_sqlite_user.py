from string import ascii_letters, digits
from itertools import chain
from random import choice
import sqlite3


def saveUser(id_user=None,ip_adresse=None, navigateur=None, date_heure=None):
    '''Crée/Enregistre un utilisateur
    '''

    if id_user is None:
        with sqlite3.connect('BDD/data.db') as co:
            curs = co.cursor()
            curs.execute('INSERT INTO user(ip_adresse,navigateur,date_heure) VALUES(?,?,?)',(ip_adresse,navigateur,date_heure))
            co.commit()
    # else:
    #     with sqlite3.connect('BDD/data.db') as co:
    #         curs = co.cursor()
    #         curs.execute('UPDATE user SET ip_adresse= ?, navigateur= ?, date_heure=? WHERE id= ? ',(ip_adresse, navigateur,date_heure,int(id_user)))
    #         co.commit()
    return True


def get_all_users():
    d = []
    with sqlite3.connect('BDD/data.db') as co:
        curs = co.cursor()
        curs.execute('SELECT id, ip_adresse, navigateur, date_heure FROM user ORDER BY date_heure DESC')
        for data in curs.fetchall():
            d.append({'id': data[0], 'ip_adresse': data[1], 'navigateur': data[2], 'date_heure': data[3]})
    return d
    