from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/count', methods=['GET'])
def count_router():
    count = get_count()
    return jsonify(count)
    
def get_count() : 
    conn = None
    query = "SELECT owner.name, count(*) FROM pet JOIN owner ON pet.owner_id = owner.id GROUP BY owner.name;"
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