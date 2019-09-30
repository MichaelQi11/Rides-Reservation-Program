import sqlite3
import re

# Hongru Qi
# search rides by up to 3 keywords
def searchRide(conn, email):
    print("Search location by keywords")
    c = conn.cursor()
    keyword = input("Please enter up to 3 location keywords (seperated by space) or (quit) to quit: ")
    # quit
    if keyword == "(quit)":
        return False
    keywords = keyword.split()
    findRides = ""
    # counter of keywords
    tmp1 = 0
    # more than one keyword
    if len(keywords) > 1:
        for keyword in keywords:
            findRides += "select * from ("
            # get the lcodes for each keyword
            lcodes = locationSearch(conn, keyword)
            lcodes = [x for subtuples in lcodes for x in subtuples]
            # counter of lcode of each keyword
            tmp = 0
            # get the union of rides which satisfies any one of the lcode that the keyword matches
            for lcode in lcodes:
                if tmp < len(lcodes) - 1:
                    findRides += (rideSearch(lcode) + " union ")
                else:
                    findRides += rideSearch(lcode)
                tmp += 1
            # get the intersection of each union (result matches all three keywords)
            if tmp1 < len(keywords) - 1:
                findRides += ") intersect "
            else:
                findRides += ")"
            tmp1 += 1
    # only one keyword
    else:
        # get the lcodes
        lcodes = locationSearch(conn, keywords[0])
        lcodes = [x for subtuples in lcodes for x in subtuples]
        # counter of lcode
        tmp = 0
        for lcode in lcodes:
            if tmp < len(lcodes) - 1:
                findRides += (rideSearch(lcode) + " union ")
            else:
                findRides += rideSearch(lcode) + ";"
            tmp += 1
    c.execute(findRides)
    rides = c.fetchall()
    # let the user to make selection to send message
    while True:
        selection = displayAndSelect(rides)
        if selection is True:
            break
        if selection is "":
            break
        sendMsg(conn, selection, email)
        ano = input("Message sent, enter y to send another message or enter any key to quit: ")
        if ano == "y":
            break

# main operational function
def mainOp(conn, email):
    while True:
        result = searchRide(conn, email)
        if result is False:
            break

# construct the search command
def rideSearch(keyword):
    findRide = '''
                select distinct(r.rno), r.price, r.rdate, r.seats, r.lugDesc, r.src, r.dst, r.driver, r.cno, t1.make, t1.model, t1.year, t1.seats, t1.owner
                from rides r, enroute e
                left outer join (select c.cno, c.make, c.model, c.year, c.seats, c.owner
                from cars c, rides r1, enroute e1 where c.cno = r1.cno
                and r1.cno is not null and (r1.dst = '{0}' COLLATE NOCASE or r1.src = '{0}' COLLATE NOCASE or (r1.rno = e1.rno and e1.lcode= '{0}' COLLATE NOCASE))) t1 on t1.cno = r.cno
                where r.dst = '{0}' COLLATE NOCASE or r.src = '{0}' COLLATE NOCASE or (r.rno = e.rno and e.lcode= '{0}' COLLATE NOCASE)
              '''.format(keyword)

    return findRide

# search the lcodes by keyword
def locationSearch(conn, keyword):
    #global conn, cur
    cur = conn.cursor()
    #find
    findLoc = '''
                SELECT lcode
                FROM locations
                WHERE lcode = '{0}' COLLATE NOCASE
                OR city like '%{0}%' COLLATE NOCASE
                OR prov like '%{0}%' COLLATE NOCASE
                OR address like '%{0}%'
                COLLATE NOCASE;
              '''.format(keyword)
    cur.execute(findLoc)

    #get all the matches and return
    return cur.fetchall()

# show the seached rides and let the user to make selection
def displayAndSelect(results):
    if len(results) == 0:
        print('no results found')
        return ''
    #print title
    print("ride no | price | ride date | seats | luggage Description | source | destination | driver | car no | car make | car model | year of car | seats of car | car owner")
    for i in range(0, len(results), 5):
        # more than 5 results, only print 5
        if len(results) <= i+5:
            for j in range(i, len(results)):
                print(results[j])
            while 1: #promtinput
                print("To contact the ride publisher select one to send message.")
                selection = input('select options: 1-{0} or ''q'' to quit:'.format(len(results)-i))
                if selection == 'q':
                    return True
                if re.match('^[1-{0}]$'.format(len(results)-i), selection):
                    break
                print('invalid selection')
        # less than 5 results, print all
        else:
            for j in range(i, i+5):
                print(results[j])
            while 1:
                print("To contact the ride publisher select one to send message.")
                selection = input(' select options: 1-5, ''y'' to view more, ''q'' to quit:')
                if selection == 'q':
                    return True
                if re.match('^[1-5y]$', selection):
                    break
                print('invalid selection')
            if selection == 'y':
                continue
            else: break

    return results[i+int(selection)-1]

# send message to the selected driver
def sendMsg(conn, selection, email):
    c = conn.cursor()
    msg = input("Please enter your messagesg or (quit) to go to the previous page: ")
    # quit
    if msg == "(quit)":
        return
    c.execute('INSERT into inbox values (?, datetime("now", "localtime"), ?, ?, ?, ?);', (selection[7], email, msg, selection[0], 'n'))
    conn.commit()
