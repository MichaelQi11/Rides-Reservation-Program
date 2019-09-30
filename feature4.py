import sqlite3
import datetime


def feature4(conn, email):
    '''
    Post ride requests.The member should be able to post a ride request by
    providing a date, a pick up location code, a drop off location code, and
    the amount willing to pay per seat. The request rid is set by your system
    to a unique number and the email is set to the email address of the member.
    '''
    # rid, email, date, pickup lcode, dropoff lcode, amount
    c = conn.cursor()

    # find a unique rid
    c.execute('''
        select coalesce(max(rid),0)+1
        from requests;
        ''')
    rid = c.fetchone()[0]

    # input the ride request date
    while True:
        date = input('Please enter the ride request date in format yyyy-mm-dd: ')
        # validate the date format
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print('invalid date format!')
            choice = input('Enter y to try enter the date again, else quit adding: ')
            if choice == 'y' or choice == 'Y':
                continue
            else:
                return

    # input the pickup lcode
    while True:
        plcode = input('Please enter the pickup location lcode: ')
        c.execute('''
            select lcode
            from locations
            where lcode = ? COLLATE NOCASE;
            ''', (plcode,))
        plcode = c.fetchone()
        # allLcode = [lcode for subtuples in c.fetchall() for lcode in subtuples]
        # check if the lcode is valid and exists
        if plcode is not None:
            plcode = plcode[0]
            break
        else:
            print('this lcode does not exist!')
            choice = input('Enter y to try enter the lcode again, else quit booking: ')
            if choice == 'y' or choice == 'Y':
                continue
            else:
                return

    # input the dropoff lcode
    while True:
        dlcode = input('Please eneter the dropoff location lcode: ')
        c.execute('''
            select lcode
            from locations
            where lcode = ? COLLATE NOCASE;
            ''', (dlcode,))
        dlcode = c.fetchone()
        # allLcode = [lcode for subtuples in c.fetchall() for lcode in subtuples]
        # check if the lcode is valid and exists
        if dlcode is not None:
            dlcode = dlcode[0]
            break
        else:
            print('this lcode does not exist!')
            choice = input('Enter y to try enter the lcode again, else quit booking: ')
            if choice == 'y' or choice == 'Y':
                continue
            else:
                return

    # input the amount per seat
    while True:
        amount = input('Please enter the amount you are willing to pay per seat: ')
        # amount should be non-negative int
        try:
            amount = int(amount)
            if amount < 0:
                print('invalid amount')
                choice = input('Enter y to try enter the amount again, else quit adding: ')
                if choice == 'y' or choice == 'Y':
                    continue
                else:
                    return
            else:
                break

        except ValueError:
            print('invalid amount')
            choice = input('Enter y to try enter the amount again, else quit adding: ')
            if choice == 'y' or choice == 'Y':
                continue
            else:
                return

    # insert the request into database
    c.execute('''
        insert into requests
        values (?,?,?,?,?,?);
        ''', (rid,email,date,plcode,dlcode,amount))
    conn.commit()

    print('you successfully posted a request, rid: %s!'%(rid))


if __name__ == '__main__':
    # feature4 test
    conn = sqlite3.connect('./project1.db')
    email = 'whatever@e.com'
    feature4(conn, email)
