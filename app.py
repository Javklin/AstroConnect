from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",
    database="*******"
)

@app.route('/stars', methods=['GET'])
def get_stars():
    category = request.args.get('category')
    cursor = db.cursor(dictionary=True)

    if category == 'nearest':
        query = "SELECT * FROM stars ORDER BY dist DESC LIMIT 50"
    elif category == 'brightest':
        query = "SELECT * FROM stars ORDER BY mag DESC LIMIT 50"
    elif category == 'hottest':
        query = "SELECT * FROM stars ORDER BY spect DESC LIMIT 50"
    elif category == 'largest':
        query = "SELECT * FROM stars ORDER BY lum DESC LIMIT 50"
    elif category == 'planets':
        query = "SELECT * FROM stars WHERE con LIKE '%Sol%' LIMIT 50"
    elif category == 'const_nearest':
        query = "SELECT * FROM stars  ORDER BY dist LIMIT 50"
    elif category == 'const_brightest':
        query = "SELECT * FROM stars  ORDER BY mag LIMIT 50"
    elif category == 'const_hottest':
        query = "SELECT * FROM stars  ORDER BY spect LIMIT 50"  
    elif category == 'const_largest':
        query = "SELECT * FROM stars  ORDER BY lum LIMIT 50"    
    elif category == 'const_planets':
        query = "SELECT * FROM stars WHERE con LIKE '%Sol%' LIMIT 50"                                     
    else:
        query = "SELECT * FROM stars LIMIT 50"

    cursor.execute(query)
    stars = cursor.fetchall()
    cursor.close()

    return jsonify(stars)

if __name__ == '__main__':
    app.run(debug=True)
