from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/pets', methods=['GET', 'POST'])
def pets_router():
    if request.method == 'POST':
        post_pets(
            request.args.get('name'),
            request.args.get('owner_id'),
            request.args.get('breed'),
            request.args.get('color') )
        return 'Created'
    elif request.method == 'GET':
        pets = get_pets()
        return jsonify(pets)
    else: 
        return 'No valid method requested'

@app.route('/pets/remove/<id_>')
def update_delete_pets(id_):
    send_pet_to_farm(id_)
    return 'The pet with id {id_} was sent to the farm for good dogs.'

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

def post_pets(name, owner_id, breed, color):
    conn = None
    query = "INSERT INTO pet (name, owner_id, breed, color) VALUES (%s, %s, %s, %s);"
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute(query, (name, owner_id, breed, color))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def send_pet_to_farm(pet_id):
    conn = None
    query = "DELETE FROM pet WHERE id = %s;"
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute(query, (pet_id))
        return('Sent pet with id {pet_id} to the farm.')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# print('name:')
# name = input()
# print('owner_id:')
# owner_id = input()
# print('breed:')
# breed = input()
# print('color:')
# color = input()

# post_pets(name, owner_id, breed, color)