from flask import Flask
import psycopg2
import json


def get_owners():
    conn = None
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute("SELECT * FROM owner;")
        rows = cur.fetchall()
        return(rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# def add_owner():
#     conn = None
#     try:
#         conn = psycopg2.connect("dbname=pet_hotel")
#         cur = con.cursor()
#         cur.execute("ADD")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()


# app = Flask(__name__)


@app.route("/owner", methods=['GET', 'POST', 'DELETE'])
def owners():
    owners = json.dumps(get_owners())
    return(owners)
