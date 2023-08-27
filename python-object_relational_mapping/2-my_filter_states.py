import sys
import MySQLdb

if __name__ == "__main__":

    # Get MySQL credentials and search name from command-line arguments
    # and # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve states with the specified name
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # Fetch all rows and print the states
    [print(state) for state in c.fetchall()]