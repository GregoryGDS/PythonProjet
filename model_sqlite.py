from string import ascii_letters, digits
from itertools import chain
from random import choice
import sqlite3


def create_uid(n=9):
    '''Génère une chaîne de caractères alétoires de longueur n
    en évitant 0, O, I, l pour être sympa.'''
    chrs = [c for c in chain(ascii_letters, digits)
            if c not in '0OIl']
    return ''.join((choice(chrs) for i in range(n)))

def save_doc_as_file(uid=None, code=None, langage=None, idCode = None):
    '''Crée/Enregistre le document sous la forme d'un fichier
    data/uid. Return the file name.
    '''
    if langage is None:
        langage = ''
    if uid is None:
        uid = create_uid()
        code = '# Write your code here...'
        with sqlite3.connect('BDD/data.db') as co:
            curs = co.cursor()
            print('langage : '+langage)
            curs.execute('INSERT INTO projet(nom,langage,code) VALUES(?,?,?)',(uid,langage,code))
            co.commit()
    else:
        with sqlite3.connect('BDD/data.db') as co:
            curs = co.cursor()
            curs.execute('UPDATE projet SET langage= ?, code= ? WHERE id= ? ',(langage, code,int(idCode)))
            co.commit()
    return {'idCode':curs.lastrowid,'uid':uid}

def read_doc_as_file(idCode):
    '''Lit le document data/idCode'''
    try:
        with sqlite3.connect('BDD/data.db') as co:
            curs = co.cursor()
            curs.execute('SELECT code, langage, nom, id FROM projet WHERE id = ? LIMIT 1', (int(idCode),))
            info = curs.fetchone()
        return {'code': info[0], 'langage': info[1], 'uid': info[2], 'idCode': info[3]}

    except FileNotFoundError:
        return None

def get_last_entries_from_files(n=10, nlines=10):
    d = []
    with sqlite3.connect('BDD/data.db') as co:
        curs = co.cursor()
        curs.execute('SELECT nom, langage, code, id FROM projet')
        for data in curs.fetchall():
            d.append({'uid': data[0], 'langage': data[1], 'code': data[2], 'idCode': data[3]})
    return d