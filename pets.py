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
def delete_pet(id_):
    send_pet_to_farm(id_)
    return 'The pet with id {id_} was sent to the farm for good dogs.'

@app.route('/pets/update/<id_>')
def update_pet_details_route(id_):
    update_pet_details('Buddy', 3, 'German Shepherd', 'Brown', id_)
    return 'The pet with id {id_} was updated.'

@app.route('/pets/checkin/<id_>')
def pet_checkin_route(id_):
    checkin_pet(id_)
    return 'Pet {id_} details updated'

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

def update_pet_details(name, owner_id, breed, color, pet_id):
    conn = None
    query = "UPDATE pet SET name = %s, owner_id=%s, breed=%s, color=%s WHERE id = %s;"
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute(query, (name, owner_id, breed, color, pet_id))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def checkin_pet(pet_id):
    conn = None
    query = "UPDATE pet SET checked_in = current_date WHERE id = %s;"
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute(query, (pet_id))
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
# update_pet_details('Venus', 4)
# post_pets(name, owner_id, breed, color)