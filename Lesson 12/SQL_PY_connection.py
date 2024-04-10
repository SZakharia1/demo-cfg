import mysql.connector
from configuration import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


# Returns a mysql connection to a database with the given name
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# Return all of the tests records
def get_all_records():
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM abcreport"""
        cur.execute(query)
        result = cur.fetchall()
        print("Fetched results")

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
        print("DB connection is closed")


get_all_records()


def calc_commission(sold_items, commission):
    sales = []

    for item in sold_items:
        sales.append(item[2])

    commission = sum(sales) * (commission / 100)
    return commission


def get_all_records_for_rep(rep_name):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT Item, Units, Total FROM abcreport WHERE Rep = '{}'""".format(rep_name)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

        cur.close()

        comp = round(calc_commission(result, commission=10), 2)

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Commission for {} is £{}".format(rep_name, comp))
    return rep_name, comp

rep_name = "Andrews"
get_all_records_for_rep(rep_name)
