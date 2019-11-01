from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/pets', methods=['GET', 'POST'])
def pets_router():
    if request.method == 'POST':
        data = request.get_json()
        post_pets(
            data['name'],
            data['owner_id'],
            data['breed'],
            data['color'] )
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

@app.route('/pets/update/', methods=['PUT'])
def update_pet_details_route():
    update_pet_details(
        request.form.get('name'),
        request.form.get('owner_id'),
        request.form.get('breed'),
        request.form.get('color'),
        request.form.get('pet_id')
        )
    return 'The pet with id {id_} was updated.'

@app.route('/pets/checkin/<id_>')
def pet_checkin_route(id_):
    checkin_pet(id_)
    return 'Pet {id_} details updated'

# GET FUNCTION
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

# POST FUNCTION
def post_pets(name, owner_id, breed, color):
    conn = None
    query = "INSERT INTO pet (name, owner_id, breed, color) VALUES (%s, %s, %s, %s);"
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute(query, (name, owner_id, breed, color,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# DELETE FUNCTION :(
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

# PUT FUNCTION FOR DETAILS
def update_pet_details(name, owner_id, breed, color, pet_id):
    conn = None
    query = "UPDATE pet SET name = %s, owner_id=%s, breed=%s, color=%s WHERE id = %s;"
    try:
        conn = psycopg2.connect("dbname=pet_hotel")
        cur = conn.cursor()
        cur.execute(query, (name, owner_id, breed, color, pet_id,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# PUT FUNCTION FOR CHECKIN 
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