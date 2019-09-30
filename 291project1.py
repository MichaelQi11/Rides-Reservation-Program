import sys
import sqlite3
# modules implemented by us
import login
import rideRequest
import offer_a_ride
import searchRides
import feature3
import feature4


def main():
    # take input from command line
    dbName = sys.argv[1]
    # make a connection to the db
    conn = sqlite3.connect('./%s'%(dbName))
    while True:
        # login function
        email = login.login(conn)
        # email = 'paul@a.com' # test mode
        if email is False:
            break
        # the main menu
        while True:
            print()
            print('''Select your operation: ''')
            op = input("1 Offer a ride.\
                        \n2 Search for rides.\
                        \n3 Book members or cancel bookings.\
                        \n4 Post ride requests.\
                        \n5 Search and delete ride requests.\
                        \n6 Logout\n")
            # call functions that user choosed
            if op == '1':
                offer_a_ride.postOffer(email, conn)
            elif op == '2':
                searchRides.mainOp(conn, email)
            elif op == '3':
                # add or cancel booking, listing rides and bookings
                feature3.feature3(conn, email)
            elif op == '4':
                # post ride request
                feature4.feature4(conn, email)
            elif op == '5':
                rideRequest.searchAndDelete(conn, email)
            elif op == '6':
                # logging out
                break
            else:
                print("invalid input!, please try again")
                continue


if __name__ == "__main__":
    main()
