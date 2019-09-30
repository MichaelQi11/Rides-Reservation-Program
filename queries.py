import sqlite3
import re

conn = None
cur = None

'''
insert enroute
inputs:
    rno: ride number
    enroute: a set containing enroute lcodes
    conn: connestion to db
'''
def insertEnroute(rno, enroute, conn):
    assert isinstance(rno, int), 'rno is not integer in insertEnroute'
    assert isinstance(enroute, set), 'enroute is not set in insertEnroute'
    cur = conn.cursor()
    insert = '''
                INSERT INTO enroute VALUES (?, ?);
             '''
    for lcode in enroute:
        tup = tuple([rno, lcode])
        cur.execute(insert, tup)
        conn.commit()


    return



'''
insert offer into rides
input:
    final: a tuple containing all the information to be inserted
    conn: connection to db
'''
def insertRide(final, conn):
    assert len(final) == 9, 'final is the wrong size in insertRide'
    cur = conn.cursor()
    cur.execute('INSERT INTO rides VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);', final)
    conn.commit()
    return


'''
get a unique rno, done through adding 1 to max of existing rno
'''
def getUniqueRno(conn):
    cur = conn.cursor()
    findmaxrno = '''
                    SELECT coalesce(max(rno), 0)
                    FROM rides
                 '''
    cur.execute(findmaxrno)
    result = cur.fetchall()
    return result[0][0]+1

'''
checks if car is valid
returns True or False
'''
def carValid(carNo, email, conn):
    assert isinstance(carNo, int), 'carNo is not int in carValid'
    assert isinstance(email, str), 'emails is not string in carValid'
    cur = conn.cursor()
    findcar = '''
                SELECT *
                FROM cars
                WHERE cno = ?
                AND owner = ? COLLATE NOCASE
              '''
    cur.execute(findcar, (carNo, email))
    result = cur.fetchall()
    if len(result) == 1:
        return True
    else:
        return False


'''
a function to find locations based on keyword
inputs:
    keyword: a keyword to base the search on
    conn: connection to the database

output:
    list of tuples that comes from the search
'''
def locationSearch(keyword, conn):
    #global conn, cur
    cur = conn.cursor()
    #find
    findLoc = '''
                SELECT *
                FROM locations
                WHERE lcode = ? COLLATE NOCASE
                OR city like ? COLLATE NOCASE
                OR prov like ? COLLATE NOCASE
                OR address like ? COLLATE NOCASE;
              '''
    cur.execute(findLoc, (keyword, '%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%'))

    #get all the matches and return
    return cur.fetchall()

'''
given the query results, display 5 at a time and promt selection

inputs:
    results: a list of tuples containing query results
    infoIndex: index of desired item in tuple to be returned

outputs:
    '': if no results were found or user pressed q
    item: key of item selected by user
'''
def displayAndSelect(results, infoIndex):
    if len(results) == 0:
        print('no results found')
        return ''
    print('lcode' + '  |  ' + 'city' + '  |  ' + 'prov' + '  |  ' + 'address')
    #print
    for i in range(0, len(results), 5):
        if len(results) <= i+5:
            for j in range(i, len(results)):
                print(results[j])
            while 1: #promtinput
                selection = input('select options: 1-{0} or \'q\' to quit:'.format(len(results)-i))
                if selection == 'q':
                    return ''
                if re.match('^[1-{0}]$'.format(len(results)-i), selection):
                    break
                print('invalid selection')

        else:
            for j in range(i, i+5):
                print(results[j])
            while 1:
                selection = input('select options: 1-5, \'y\' to view more, \'q\' to quit:')
                if selection == 'q':
                    return ''
                if re.match('^[1-5y]$', selection):
                    break
                print('invalid selection')
            if selection == 'y':
                continue
            else:
                break

    return results[i+int(selection)-1][infoIndex]

def main():
    global conn, cur
    path = "./test.db"
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    rno = getUniqueRno(conn)
    print(rno)

    '''
    keyword = input('keyword: ')
    result = displayAndSelect(locationSearch(keyword, conn), 0)
    print(result)
    '''
    '''
    email = 'joe@gmail.com'
    print(carValid(9, email, conn))
    '''
    conn.close()

if __name__ == '__main__':
    main()
