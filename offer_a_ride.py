import sqlite3
import re
from queries import *

#get source location
def getSource(conn):
    keyword = input('input source location keyword(q to quit): ')
    if keyword == 'q':
        return 'q'

    return displayAndSelect(locationSearch(keyword, conn), 0)

#get destination
def getDestination(conn):
    keyword = input('input destination location keyword: ')
    if keyword == 'q':
        return 'q'

    return displayAndSelect(locationSearch(keyword, conn), 0)

#get car number
#returns '' if left blank, '-1' if invalid, int of carNo if valid
def getCarNo(email, conn):
    carNo = input('input car number(optional): ')
    if carNo == '':
        return carNo
    if not re.match('[0-9]+', carNo):
        return '-1'
    if carValid(int(carNo), email, conn):
        return carNo 
    else: #car doesnt belong to user
        return '-2'
    

#get enroute
def getEnroute(conn):
    result = set()
    while 1:
        keyword = input('input enroute locations one at a time(optional): ')
        if keyword == '':
            break
        lcode = displayAndSelect(locationSearch(keyword, conn), 0)
        if lcode is not '':
            result.add(lcode)
    
    return result

#find location


#checks if user input is valid (excluding locations)
def checkValid(result):
    #make sure length is 4
    if (len(result) != 4):
        print('invalid number of arguments')
        return False

    #match date, format 'YYYY-MM-DD'
    if (re.match('[1-9][0-9]{3}-(0[1-9]|1[0-2])-[0-9]{2}', result[1]) == None):
        print('invalid date')
        return False

    #match seats
    if (re.match('[1-9][0-9]*', result[2]) == None):
        print('invalid seats')
        return False

    #match price per seat
    if (re.match('[1-9][0-9]*', result[0]) == None):
        print('invalid price')
        return False

    #match luggage description
    if (re.match('[a-zA-Z0-9]{1,10}', result[3]) == None):
        print('invalid luggage description')
        return False
    
    return True

    

#get user input
#requires user email
def postOffer(email, conn):
    #global result
    #prompt user input
    print('Input ride offer in the following format')
    print("(price per seat(no decimal), date(YYYY-MM-DD), number of seats offered, luggage description)")
        
    while(1):
        info = input('ride offer, q to exit: ')
        if (re.match("^q$", info)):
            return
        info = info[1:-1].split(', ')
        if (not checkValid(info)):
            continue
        
        #type casting to make sure seats and price are int
        info[0] = int(info[0])
        info[2] = int(info[2])

        #get sourcelocation
        while 1:
            source = getSource(conn)
            if source == '': 
                print('no source location input, try again')
            else: 
                break
        if source == 'q':
            continue 
        info += [source]

        #get destination
        while 1:
            destination = getDestination(conn)
            if destination == '': 
                print('no destination location input, try again')
            else:
                break 
        if destination == 'q':
            continue
        info += [destination]
        
        #get carnumber
        while 1:
            carNo = getCarNo(email, conn)
            if carNo == '-1':
                print('invalid input')
            if carNo == '-2':
                print('this car does not belong to you, try again')
            else:
                break 
        
        if carNo is not '':
            carNo = int(carNo)
        else: 
            carNo = None
        
        info += [email]
        info += [carNo]


        #get enroute
        enroute = getEnroute(conn)

        #print(info)
        #print(enroute)
        decision = input('proceed with values given? \'y\' to continue, anything else start over: ')
        if decision == 'y':
            break 
        else:
            continue 

    rno = getUniqueRno(conn)
    final = tuple([rno] + info)
    insertRide(final, conn)
    insertEnroute(rno, enroute, conn)

    #ride and enroute has been inserted, commit change to db
    conn.commit()
    #print(final)
    print('ride is posted')
        

def main():
    #assert(type(conn) == sqlite3.Connection)
    path = "./test.db"
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    email = 'joe@gmail.com'
    postOffer(email, conn)
    #conn.commit()
    conn.close()


if __name__ == "__main__":
    main()