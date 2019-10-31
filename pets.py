from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)


@app.route('/pets', methods=['GET', 'POST'])
def pets_router1():
    if request.method == 'POST':
        return 'POST'
    elif request.method == 'GET':
        pets = get_pets()
        return jsonify(pets)
    else: 
        return 'No valid method requested'

@app.route('/pets/<id_>', methods=['PUT', 'DELETE'])
def pets_router():
    if request.method == 'PUT':
        return 'PUT'
        # pets = get_pets()
    elif request.method == 'DELETE':
        return 'DELETE'
    else: 
        return 'No valid method requested'

def get_pets():
    conn = None
    query = "SELECT * FROM pet;"
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return(rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

