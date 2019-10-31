from flask import Flask
import psycopg2
import json


# def get_creatures():
#     conn = None
#     try:
#         conn = psycopg2.connect("dbname=mythical_creatures")
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM creatures;")
#         rows = cur.fetchall()
#         return(rows)
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()


# def add_creatures():
#     conn = None
#     try:
#         conn = psycopg2.connect("dbname=mythical_creatures")
#         cur = con.cursor()
#         cur.execute("ADD")


# app = Flask(__name__)


# @app.route("/", methods=['GET', 'POST'])
# def creatures():
#     creatures = json.dumps(get_creatures())
#     return(creatures)
