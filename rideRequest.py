import sqlite3
import re

# Hongru Qi
# search user's requests
def userSearch(conn, email, type):
    c = conn.cursor()
    c.execute('SELECT * from requests where email=? COLLATE NOCASE;', (email,))
    requests = c.fetchall()
    makeSelection(conn, email, requests, type)

# delete request
def delete(conn, rid, email):
    c = conn.cursor()
    c.execute('DELETE from requests where rid=? and email=? COLLATE NOCASE;', (rid,email))
    conn.commit()
    print("Request deleted")

# search requests by lcode
def searchByLcode(conn, email, lcode, type):
    c = conn.cursor()
    c.execute('SELECT * from requests where pickup=? COLLATE NOCASE;', (lcode,))
    requests = c.fetchall()
    makeSelection(conn, email, requests, type)

# search requests by city
def searchByCity(conn, email, city, type):
    c = conn.cursor()
    c.execute('SELECT * from requests where pickup in (SELECT lcode from locations where city=? COLLATE NOCASE);', (city,))
    requests = c.fetchall()
    makeSelection(conn, email, requests, type)

# send message to user who posted requests
def sendMessage(conn, email, receiver, content):
    c = conn.cursor()
    c.execute('INSERT into inbox (email, msgTimestamp, sender, content, seen) values (?, datetime("now"), ?, ?, ?);', (receiver,  email, content, 'n'))
    conn.commit()

# print the searched requests and let user to select to delete or send message
def makeSelection(conn, email, requests, type):
    while True:
        if type == "1":
            selection = displayAndSelect(requests, "delete request")
        else:
            selection = displayAndSelect(requests, "send message")
        # quit
        if selection is True:
            return
        # no results found
        elif selection is "":
            return
        # send message
        else:
            if type == "1":
                confirm = input("Do you want to delete this request? Enter y to confirm or any key to quit: ")
                if confirm != "y":
                    return
                else:
                    delete(conn, selection[0], email)
                    break
            else:
                content = input("Please enter the message content or q to quit: ")
                if content == "q":
                    return
                sendMessage(conn, email, selection[1], content)
                ano = input("Message sent, enter y to send another message or enter any key to quit: ")
                if ano != "y":
                    break
    return

# display the searched results and make selections
def displayAndSelect(results, arg):
    if len(results) == 0:
        print('no results found')
        return ''
    #print
    print("request ID | request date | pickup location | dropoff location | amount")
    for i in range(0, len(results), 5):
        # more than 5, only print 5
        if len(results) <= i+5:
            for j in range(i, len(results)):
                print(results[j])
            while 1: #promtinput
                selection = input("select one to " + arg + ' (options: 1-{0}) or ''q'' to quit:'.format(len(results)-i))
                if selection == 'q':
                    return True
                if re.match('^[1-{0}]$'.format(len(results)-i), selection):
                    break
                print('invalid selection')
        # less than 5, print all
        else:
            for j in range(i, i+5):
                print(results[j])
            while 1:
                selection = input('select one to ' + arg + ' (options: 1-5), ''y'' to view more, ''q'' to quit:')
                if selection == 'q':
                    return True
                if re.match('^[1-5y]$', selection):
                    break
                print('invalid selection')
            if selection == 'y':
                continue
            else: break

    return results[i+int(selection)-1]

# search requests (main search operation)
def search(conn, email):
    searchOp = input("Enter 1 to search your requests and 2 to search by location or q to go to the main page: ")
    # search user's requests
    if searchOp == '1':
        userSearch(conn, email, searchOp)
    # search by location
    elif searchOp == '2':
        isLcode = input("Enter 1 to search by lcode or 2 by city: ")
        # seach by lcode
        if isLcode == '1':
            lcode = input("Please enter the lcode: ")
            searchByLcode(conn, email, lcode, searchOp)
        # search by city
        elif isLcode == '2':
            city = input("Please enter the city: ")
            searchByCity(conn, email, city, searchOp)
        else:
            print("Invalid input")
    # quit
    elif searchOp == "q":
        return False
    else:
        print("Invalid input")

# main opeational function
def searchAndDelete(conn, email):
    while True:
        command = search(conn, email)
        if command == False:
            break
